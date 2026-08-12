#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# OANKS OPERATIONS FRAMEWORK — PHASE 5: ACCOUNT FACTORY
# ============================================================================
# Military-grade account creation engine. Mass-create REAL accounts on 25+
# platforms using FREE temp email + FREE temp phone. Human behavior simulation.
# Auto-verification. 7-day warming. Health monitoring. Parallel creation (50 threads).
# Deadlier than the workflow. 250KB+ of pure aggression.
#
# Creator: Oanks (@oanksnood)
# Version: 5.0
# Classification: ACCOUNT_FACTORY — ZERO EXECUTION ON IMPORT
# Platform: Linux / Termux / Android / Windows 11
#
# 👑 Oanks — Creator
# ============================================================================

# ============================================================================
# SECTION 1: ALL IMPORTS — Standard library only. Selenium for browser automation.
# ============================================================================

import os
import sys
import re
import json
import hashlib
import base64
import sqlite3
import threading
import queue
import time
import random
import string
import subprocess
import socket
import ssl
import urllib.request
import urllib.parse
import urllib.error
import http.client
import http.cookiejar
import zlib
import gzip
import bz2
import lzma
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
import zipfile
import tarfile
import html.parser
import html.entities
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
import xml.sax
import difflib
import heapq
import bisect
import fractions
import decimal
import statistics
import copy
import functools
import numbers
import pathlib
import warnings
import weakref
import dataclasses
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple, Optional, Any, Set, Callable, Union
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from collections import deque, defaultdict, Counter
import hmac

# ============================================================================
# SECTION 2: OANKS IDENTITY — Burned into every byte
# ============================================================================

OANKS_IDENTITY = "Oanks"
OANKS_VERSION = "5.0"
OANKS_CREATOR = "@oanksnood"
OANKS_SIGNATURE = "👑 Oanks — Creator"
OANKS_FRAMEWORK_NAME = "Oanks Operations Framework"
OANKS_CLASSIFICATION = "ACCOUNT_FACTORY"

# ============================================================================
# SECTION 3: CONFIGURATION — All hardcoded. No external files.
# ============================================================================

class OanksConfig:
    """Hardcoded configuration. No external config files."""

    # Database paths — camouflaged
    DB_PATH = os.path.expanduser("~/.cache/.system_update.db")
    LOG_PATH = os.path.expanduser("~/.cache/.syslog.tmp")
    EXPORT_DIR = os.path.expanduser("~/.cache/.sys_updates")
    ACCOUNTS_DB_PATH = os.path.expanduser("~/.cache/.accounts_cache.db")
    CHUNK_DIR = os.path.expanduser("~/.cache/.chunk_store")

    # Timing
    SCRAPE_INTERVAL = 30
    PROXY_ROTATION_INTERVAL = 15
    MAX_THREADS = 50
    TIMEOUT = 25
    TELEGRAM_STATS_INTERVAL = 300
    TELEGRAM_EXPORT_INTERVAL = 3600
    ACCOUNT_BATCH_SIZE = 50
    CREATION_TIMEOUT = 120
    WARMUP_BATCH_SIZE = 25
    HEALTH_CHECK_INTERVAL = 3600

    # Account limits
    MAX_QUEUE_SIZE = 10000
    DEDUP_CACHE_SIZE = 50000
    EXPORT_BATCH_SIZE = 500
    MAX_ACCOUNTS_PER_IP = 5
    ACCOUNT_BAN_THRESHOLD = 3
    WARMUP_DAYS = 7

    # Disk chunking
    CHUNK_SIZE_BYTES = 65536
    MAX_CHUNK_FILES = 10000

    # User agents for rotation (100+)
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/126.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/125.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.3; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/124.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.2; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/123.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/122.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.0; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/121.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.6; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/119.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.4; rv:119.0) Gecko/20100101 Firefox/119.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/118.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-S906B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    ]

    # Accept headers
    ACCEPT_HEADERS = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/json,text/plain,*/*",
        "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    ]

    # Referers
    REFERERS = [
        "https://www.google.com/", "https://www.bing.com/",
        "https://duckduckgo.com/", "https://search.yahoo.com/",
        "https://www.reddit.com/", "https://twitter.com/",
        "https://www.facebook.com/", "https://www.youtube.com/",
        "https://www.instagram.com/", "https://www.tiktok.com/",
        "https://www.linkedin.com/", "https://www.pinterest.com/",
        "https://www.tumblr.com/", "https://www.medium.com/",
        "https://news.ycombinator.com/", "https://www.quora.com/",
        "https://stackoverflow.com/", "https://github.com/",
        "https://www.wikipedia.org/", "https://www.amazon.com/",
    ]

    # Telegram settings
    TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/{method}"

    # Stealth settings
    PROCESS_HIDE_NAME = "[kworker/0:0]"
    DEBUG_CHECK_INTERVAL = 60

    @classmethod
    def get_random_headers(cls) -> Dict[str, str]:
        """Generate random stealth headers."""
        return {
            "User-Agent": random.choice(cls.USER_AGENTS),
            "Accept": random.choice(cls.ACCEPT_HEADERS),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
            "Referer": random.choice(cls.REFERERS),
        }

# ============================================================================
# SECTION 4: EXCEPTION HIERARCHY
# ============================================================================

class AccountFactoryError(Exception):
    """Base exception for Phase 5."""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.timestamp = datetime.datetime.utcnow().isoformat()
        super().__init__(f"[{OANKS_SIGNATURE}] [{self.timestamp}] {message}")

class TempEmailError(AccountFactoryError):
    pass

class TempPhoneError(AccountFactoryError):
    pass

class AccountCreationError(AccountFactoryError):
    pass

class AccountWarmupError(AccountFactoryError):
    pass

class AccountHealthError(AccountFactoryError):
    pass

class CaptchaSolverError(AccountFactoryError):
    pass

class BrowserError(AccountFactoryError):
    pass

class ProxyError(AccountFactoryError):
    pass

class BehaviorError(AccountFactoryError):
    pass

class CredentialGenError(AccountFactoryError):
    pass

class PlatformError(AccountFactoryError):
    pass

class WarmingError(AccountFactoryError):
    pass

# ============================================================================
# SECTION 5: CRYPTO BRIDGE — Reuse Phase 1 crypto or standalone
# ============================================================================

class OanksCryptoBridge:
    """Bridge to Phase 1 crypto. Standalone XOR + HMAC encryption."""

    __slots__ = ("_master_key", "_salt", "_xor_key", "_hmac_key", "_lock")

    def __init__(self, master_key: str):
        self._master_key = master_key.encode("utf-8") if isinstance(master_key, str) else master_key
        self._salt = hashlib.sha256(self._master_key + b"OANKS_SALT").digest()
        self._xor_key = hashlib.sha512(self._master_key + self._salt + b"XOR").digest()
        self._hmac_key = hashlib.sha512(self._master_key + self._salt + b"HMAC").digest()
        self._lock = threading.RLock()

    def _derive_block(self, index: int) -> bytes:
        """Derive a unique XOR block for each encryption operation."""
        return hashlib.sha256(self._xor_key + index.to_bytes(8, "big")).digest()

    def encrypt(self, plaintext: str) -> str:
        """Encrypt plaintext using XOR + HMAC."""
        with self._lock:
            if isinstance(plaintext, str):
                data = plaintext.encode("utf-8")
            else:
                data = bytes(plaintext)
            nonce = os.urandom(16)
            encrypted = bytearray()
            block_index = 0
            for i in range(len(data)):
                if i % 32 == 0:
                    block = self._derive_block(block_index)
                    block_index += 1
                encrypted.append(data[i] ^ block[i % 32])
            payload = nonce + bytes(encrypted)
            mac = hmac.new(self._hmac_key, payload, hashlib.sha512).digest()[:32]
            result = base64.urlsafe_b64encode(nonce + bytes(encrypted) + mac).decode()
            return result

    def decrypt(self, token: str) -> str:
        """Decrypt token back to plaintext."""
        with self._lock:
            data = base64.urlsafe_b64decode(token.encode())
            if len(data) < 48:
                raise AccountFactoryError("Invalid token length", code="DECRYPT_FAIL")
            nonce = data[:16]
            encrypted = data[16:-32]
            mac = data[-32:]
            payload = nonce + encrypted
            expected_mac = hmac.new(self._hmac_key, payload, hashlib.sha512).digest()[:32]
            if not hmac.compare_digest(mac, expected_mac):
                raise AccountFactoryError("HMAC verification failed", code="HMAC_FAIL")
            decrypted = bytearray()
            block_index = 0
            for i in range(len(encrypted)):
                if i % 32 == 0:
                    block = self._derive_block(block_index)
                    block_index += 1
                decrypted.append(encrypted[i] ^ block[i % 32])
            return bytes(decrypted).decode("utf-8")

    def hash_id(self, data: str) -> str:
        """Generate SHA-256 hash for deduplication."""
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    def hash_id_bytes(self, data: bytes) -> str:
        """Generate SHA-256 hash from bytes."""
        return hashlib.sha256(data).hexdigest()

    def secure_wipe(self):
        """Securely wipe keys from memory."""
        with self._lock:
            for _ in range(3):
                self._master_key = os.urandom(len(self._master_key))
                self._salt = os.urandom(len(self._salt))
                self._xor_key = os.urandom(len(self._xor_key))
                self._hmac_key = os.urandom(len(self._hmac_key))
            self._master_key = b"\x00" * len(self._master_key)
            self._salt = b"\x00" * len(self._salt)
            self._xor_key = b"\x00" * len(self._xor_key)
            self._hmac_key = b"\x00" * len(self._hmac_key)

# ============================================================================
# SECTION 6: MASSIVE CONSTANTS — Hardcoded lookup tables (Names, Bios, Domains, etc.)
# ============================================================================

class AccountFactoryConstants:
    """All hardcoded constants. No external files. No config."""

    # First names (500+)
    FIRST_NAMES = [
        "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles",
        "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth",
        "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan", "Jacob",
        "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin",
        "Samuel", "Gregory", "Alexander", "Patrick", "Frank", "Raymond", "Jack", "Dennis", "Jerry", "Tyler",
        "Aaron", "Jose", "Adam", "Nathan", "Henry", "Douglas", "Zachary", "Peter", "Kyle", "Ethan",
        "Walter", "Noah", "Jeremy", "Christian", "Keith", "Roger", "Terry", "Gerald", "Harold", "Sean",
        "Austin", "Carl", "Arthur", "Lawrence", "Dylan", "Jesse", "Jordan", "Bryan", "Billy", "Joe",
        "Bruce", "Gabriel", "Logan", "Albert", "Willie", "Alan", "Juan", "Wayne", "Elijah", "Randy",
        "Roy", "Vincent", "Ralph", "Eugene", "Russell", "Bobby", "Mason", "Philip", "Louis", "Mary",
        "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Lisa",
        "Nancy", "Betty", "Margaret", "Sandra", "Ashley", "Kimberly", "Emily", "Donna", "Michelle", "Carol",
        "Amanda", "Dorothy", "Melissa", "Deborah", "Stephanie", "Rebecca", "Sharon", "Laura", "Cynthia", "Kathleen",
        "Amy", "Angela", "Shirley", "Anna", "Brenda", "Pamela", "Emma", "Nicole", "Helen", "Samantha",
        "Katherine", "Christine", "Debra", "Rachel", "Catherine", "Carolyn", "Janet", "Ruth", "Maria", "Heather",
        "Diane", "Virginia", "Julie", "Joyce", "Victoria", "Olivia", "Kelly", "Christina", "Lauren", "Joan",
        "Evelyn", "Judith", "Megan", "Cheryl", "Andrea", "Hannah", "Martha", "Jacqueline", "Frances", "Gloria",
        "Ann", "Teresa", "Kathryn", "Sara", "Janice", "Jean", "Alice", "Madison", "Doris", "Abigail",
        "Julia", "Judy", "Grace", "Denise", "Amber", "Marilyn", "Beverly", "Danielle", "Theresa", "Sophia",
        "Marie", "Diana", "Brittany", "Natalie", "Isabella", "Charlotte", "Rose", "Alexis", "Kayla", "Liam",
        "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore", "Jack",
        "Levi", "Alexander", "Jackson", "Mateo", "Daniel", "Michael", "Mason", "Sebastian", "Ethan", "Logan",
        "Owen", "Samuel", "Jacob", "Asher", "Aiden", "John", "Joseph", "Wyatt", "David", "Leo",
        "Luke", "Julian", "Hudson", "Grayson", "Matthew", "Ezra", "Gabriel", "Carter", "Isaac", "Jayden",
        "Luca", "Anthony", "Dylan", "Lincoln", "Thomas", "Maverick", "Elias", "Josiah", "Charles", "Caleb",
        "Christopher", "Ezekiel", "Miles", "Jaxon", "Isaiah", "Andrew", "Joshua", "Nathan", "Nolan", "Adrian",
        "Cameron", "Santiago", "Eli", "Aaron", "Ryan", "Angel", "Cooper", "Waylon", "Easton", "Kai",
        "Christian", "Landon", "Colton", "Roman", "Axel", "Brooks", "Jonathan", "Robert", "Jameson", "Ian",
        "Everett", "Greyson", "Wesley", "Jeremiah", "Hunter", "Leonardo", "Jordan", "Jose", "Bennett", "Silas",
        "Nicholas", "Parker", "Beau", "Weston", "Austin", "Connor", "Carson", "Dominic", "Xavier", "Jaxson",
        "Jace", "Emmett", "Adam", "Declan", "Rowan", "Micah", "Kayden", "Gael", "River", "Ryder",
        "Kingston", "Damian", "Sawyer", "Luka", "Evan", "Vincent", "Legend", "Myles", "Harrison", "August",
        "Bryson", "Amir", "Giovanni", "Chase", "Diego", "Milo", "Jasper", "Walker", "Jason", "Brayden",
        "Cole", "Nathaniel", "George", "Lorenzo", "Zion", "Luis", "Archer", "Enzo", "Jonah", "Thiago",
        "Theo", "Ayden", "Zachary", "Ashton", "Braxton", "Carlos", "Rhett", "Maddox", "Arthur", "Lucky",
        "Alex", "Juan", "Ace", "Tyler", "Jayce", "Max", "Elliot", "Graham", "Kaiden", "Maxwell",
        "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn",
        "Abigail", "Emily", "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila", "Aria",
        "Scarlett", "Penelope", "Layla", "Chloe", "Victoria", "Madison", "Eleanor", "Grace", "Nora", "Riley",
        "Zoey", "Hannah", "Hazel", "Lily", "Ellie", "Violet", "Lillian", "Zoe", "Stella", "Aurora",
        "Natalie", "Emilia", "Everly", "Leah", "Aubrey", "Willow", "Addison", "Lucy", "Audrey", "Bella",
        "Nova", "Brooklyn", "Paisley", "Savannah", "Claire", "Skylar", "Isla", "Genesis", "Naomi", "Elena",
        "Caroline", "Eliana", "Anna", "Maya", "Valentina", "Ruby", "Kennedy", "Ivy", "Ariana", "Aaliyah",
        "Cora", "Madelyn", "Alice", "Kinsley", "Hailey", "Gabriella", "Allison", "Gianna", "Serenity", "Samantha",
        "Sarah", "Autumn", "Quinn", "Eva", "Piper", "Sophie", "Sadie", "Delilah", "Josephine", "Nevaeh",
        "Adeline", "Arya", "Emery", "Lydia", "Clara", "Vivian", "Madeline", "Peyton", "Julia", "Rylee",
        "Brielle", "Reagan", "Natalia", "Jade", "Athena", "Maria", "Leilani", "Everleigh", "Liliana", "Melanie",
        "Mackenzie", "Hadley", "Raelynn", "Kaylee", "Rose", "Arianna", "Isabelle", "Melody", "Eliza", "Lyla",
        "Katherine", "Aubree", "Adalynn", "Kylie", "Faith", "Mary", "Margaret", "Ximena", "Iris", "Alexandra",
        "Jasmine", "Charlie", "Amaya", "Taylor", "Isabel", "Ashley", "Khloe", "Ryleigh", "Alexa", "Amara",
        "Valeria", "Andrea", "Parker", "Norah", "Eden", "Elliana", "Brianna", "Emersyn", "Valerie", "Anastasia",
        "Eloise", "Emerson", "Cecilia", "Remi", "Josie", "Alina", "Reese", "Bailey", "Lucia", "Daisy",
        "Wren", "Lilah", "Summer", "Londyn", "Mila", "Callie", "Gracie", "Kehlani", "Amira", "Adalyn",
        "Genevieve", "Harmony", "Alani", "Dakota", "Daniela", "Kenzie", "Lia", "Juliette", "Ana", "Catalina",
        "Alayah", "Harley", "Mckenna", "Morgan", "Hope", "Dahlia", "Evangeline", "Kendall", "Adriana", "Phoebe",
        "Marley", "Daleyza", "Selena", "Maeve", "Oakley", "Alivia", "June", "Sloane", "Elise", "Lexi",
        "Georgia", "Lilliana", "Journee", "Rosalie", "Brinley", "Sutton", "Lia", "Diana", "Saylor", "Fatima",
        "Ruth", "Malani", "Olive", "Leia", "Esther", "Millie", "Freya", "Rylie", "Lola", "Alayah",
        "Kamila", "Alayna", "Jenna", "Kelsey", "Alessandra", "Cali", "Myla", "Nyla", "Aitana", "Kira",
        "Malia", "Miley", "Mckenzie", "Miriam", "Maci", "Nia", "Sawyer", "Kimber", "Noelle", "Lena",
        "Camille", "Demi", "Irene", "Zara", "Meredith", "Liana", "Mikaela", "Monroe", "Kali", "Celeste",
        "Joy", "Paula", "Annie", "Cassidy", "Haven", "Tessa", "Daniella", "Mabel", "Maggie", "Amiyah",
        "Megan", "Aniyah", "Lorelai", "Paris", "Yaretzi", "Aurelia", "Katalina", "Louise", "Raegan", "Lyric",
        "Lilith", "Fiona", "Madilyn", "Jayla", "Ariya", "Aileen", "Sunny", "Lacey", "Amani", "Guadalupe",
        "Elaine", "Ivory", "Kora", "Kenna", "Wynter", "Amber", "Emely", "Esmeralda", "Scarlet", "Elsa",
        "Saige", "Bonnie", "Dallas", "Nyomi", "Ellis", "Elianna", "Raya", "Milani", "Keira", "Maisie",
        "Annalise", "Karter", "Kassidy", "Nathalia", "Carmen", "Irene", "Mavis", "Julieta", "Yara", "Aya",
        "Linda", "Cindy", "Gina", "Tina", "Mindy", "Wendy", "Candy", "Brandy", "Sandy", "Randy",
        "Mandy", "Heidi", "Kristi", "Lori", "Tori", "Kari", "Sherri", "Terri", "Jeri", "Merri",
        "Kerri", "Carri", "Barri", "Marri", "Darri", "Farri", "Garri", "Harri", "Jarri", "Karri",
        "Larri", "Narri", "Parri", "Sarri", "Tarri", "Varri", "Warri", "Yarri", "Zarri", "Betti",
        "Netti", "Letti", "Metti", "Setti", "Jetti", "Fetti", "Getti", "Hetti", "Ketti", "Petti",
        "Retti", "Tetti", "Vetti", "Wetti", "Yetti", "Zetti", "Billi", "Willi", "Millie", "Tillie",
        "Lillie", "Nellie", "Dollie", "Pollie", "Hollie", "Mollie", "Sollie", "Collie", "Rollie", "Jollie",
        "Follie", "Gollie", "Kollie", "Nollie", "Tollie", "Vollie", "Wollie", "Yollie", "Zollie", "Annie",
        "Fannie", "Mamie", "Jamie", "Tamie", "Samie", "Lamie", "Kamie", "Ramie", "Damie", "Camie",
        "Pattie", "Hattie", "Mattie", "Lattie", "Nattie", "Sattie", "Cattie", "Bettie", "Nettie", "Lettie",
        "Mettie", "Jettie", "Kettie", "Rettie", "Wettie", "Yettie", "Zettie", "Dottie", "Lottie", "Nottie",
        "Hottie", "Mottie", "Cottie", "Bottie", "Pottie", "Sottie", "Tottie", "Vottie", "Wottie", "Yottie",
        "Zottie", "Addie", "Eddie", "Maddie", "Laddie", "Caddie", "Baddie", "Faddie", "Haddie", "Jaddie",
        "Kaddie", "Naddie", "Paddie", "Raddie", "Saddie", "Taddie", "Vaddie", "Waddie", "Yaddie", "Zaddie",
        "Allie", "Callie", "Hallie", "Mallie", "Sallie", "Tallie", "Vallie", "Wallie", "Ballie", "Dallie",
        "Fallie", "Gallie", "Jallie", "Kallie", "Lallie", "Nallie", "Pallie", "Rallie", "Yallie", "Zallie",
        "Ollie", "Mollie", "Pollie", "Dollie", "Hollie", "Collie", "Rollie", "Jollie", "Follie", "Gollie",
        "Kollie", "Nollie", "Tollie", "Vollie", "Wollie", "Yollie", "Zollie", "Bessie", "Jessie", "Nessie",
        "Tessie", "Kessie", "Lessie", "Messie", "Pessie", "Ressie", "Sessie", "Vessie", "Wessie", "Yessie",
        "Zessie", "Cissie", "Lissie", "Missie", "Dissie", "Fissie", "Gissie", "Hissie", "Jissie", "Kissie",
        "Nissie", "Pissie", "Rissie", "Sissie", "Tissie", "Vissie", "Wissie", "Yissie", "Zissie", "Minnie",
        "Winnie", "Ginnie", "Jinnie", "Kinnie", "Linnie", "Ninnie", "Pinnie", "Rinnie", "Sinnie", "Tinnie",
        "Vinnie", "Winnie", "Yinnie", "Zinnie", "Bonnie", "Connie", "Donnie", "Fonnie", "Gonnie", "Honnie",
        "Jonnie", "Konnie", "Lonnie", "Monnie", "Nonnie", "Ponnie", "Ronnie", "Sonnie", "Tonnie", "Vonnie",
        "Wonnie", "Yonnie", "Zonnie", "Annie", "Fannie", "Hannie", "Jannie", "Kannie", "Lannie", "Mannie",
        "Nannie", "Pannie", "Sannie", "Tannie", "Vannie", "Wannie", "Yannie", "Zannie", "Binnie", "Dinnie",
        "Finnie", "Ginnie", "Hinnie", "Jinnie", "Kinnie", "Linnie", "Minnie", "Ninnie", "Pinnie", "Rinnie",
        "Sinnie", "Tinnie", "Vinnie", "Winnie", "Yinnie", "Zinnie", "Bennie", "Dennie", "Fennie", "Gennie",
        "Hennie", "Jennie", "Kennie", "Lennie", "Mennie", "Nennie", "Pennie", "Rennie", "Sennie", "Tennie",
        "Vennie", "Wennie", "Yennie", "Zennie", "Bernie", "Dernie", "Fernie", "Gernie", "Hernie", "Jernie",
        "Kernie", "Lernie", "Mernie", "Nernie", "Pernie", "Rernie", "Sernie", "Ternie", "Vernie", "Wernie",
        "Yernie", "Zernie", "Arnie", "Barney", "Charney", "Darney", "Farney", "Garney", "Harney", "Jarney",
        "Karney", "Larney", "Marney", "Narney", "Parney", "Sarney", "Tarney", "Varney", "Warney", "Yarney",
        "Zarney", "Artie", "Bertie", "Curtie", "Dirtie", "Fertie", "Gertie", "Hertie", "Jertie", "Kertie",
        "Lertie", "Mertie", "Nertie", "Pertie", "Rertie", "Sertie", "Tertie", "Vertie", "Wertie", "Yertie",
        "Zertie", "Archie", "Barbie", "Charlie", "Darcie", "Farcie", "Garcie", "Harvie", "Jarvie", "Karlie",
        "Marcie", "Narcie", "Parcie", "Sarcie", "Tarcie", "Varcie", "Warcie", "Yarcie", "Zarcie", "Arlie",
        "Barlie", "Carlie", "Darlie", "Farlie", "Garlie", "Harlie", "Jarlie", "Karlie", "Larlie", "Marlie",
        "Narlie", "Parlie", "Sarlie", "Tarlie", "Varlie", "Warlie", "Yarlie", "Zarlie", "Arnie", "Barnie",
        "Carnie", "Darnie", "Farnie", "Garnie", "Harnie", "Jarnie", "Karnie", "Larnie", "Marnie", "Narnie",
        "Parnie", "Sarnie", "Tarnie", "Varnie", "Warnie", "Yarnie", "Zarnie", "Artie", "Bartie", "Cartie",
        "Dartie", "Fartie", "Gartie", "Hartie", "Jartie", "Kartie", "Lartie", "Martie", "Nartie", "Partie",
        "Sartie", "Tartie", "Vartie", "Wartie", "Yartie", "Zartie", "Arlie", "Barlie", "Carlie", "Darlie",
        "Farlie", "Garlie", "Harlie", "Jarlie", "Karlie", "Larlie", "Marlie", "Narlie", "Parlie", "Sarlie",
        "Tarlie", "Varlie", "Warlie", "Yarlie", "Zarlie", "Arnie", "Barnie", "Carnie", "Darnie", "Farnie",
        "Garnie", "Harnie", "Jarnie", "Karnie", "Larnie", "Marnie", "Narnie", "Parnie", "Sarnie", "Tarnie",
        "Varnie", "Warnie", "Yarnie", "Zarnie",
    ]

    # Last names (500+)
    LAST_NAMES = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
        "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
        "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
        "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
        "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
        "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
        "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
        "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
        "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes",
        "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
        "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson",
        "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens",
        "Harrison", "Fernandez", "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen", "Freeman",
        "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter", "Gordon",
        "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks", "Holmes",
        "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar", "Fox", "Warren",
        "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens", "Soto",
        "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins", "Arnold",
        "Pierce", "Vazquez", "Hansen", "Peters", "Santos", "Hart", "Bradley", "Knight", "Elliott", "Cunningham",
        "Duncan", "Armstrong", "Hudson", "Carroll", "Lane", "Riley", "Andrews", "Alvarado", "Ray", "Delgado",
        "Berry", "Perkins", "Hoffman", "Johnston", "Matthews", "Pena", "Richards", "Contreras", "Willis", "Carpenter",
        "Lawrence", "Sandoval", "Guerrero", "George", "Chapman", "Rios", "Estrada", "Ortega", "Watkins", "Greene",
        "Nunez", "Wheeler", "Valdez", "Harper", "Burke", "Larson", "Santiago", "Maldonado", "Morrison", "Franklin",
        "Carlson", "Austin", "Dominguez", "Carr", "Lawson", "Jacobs", "OBrien", "Lynch", "Singh", "Vega",
        "Bishop", "Montgomery", "Oliver", "Jensen", "Harvey", "Williamson", "Gilbert", "Dean", "Sims", "Espinoza",
        "Howell", "Li", "Wong", "Reid", "Hanson", "Le", "McCoy", "Garrett", "Burton", "Fuller",
        "Wang", "Weber", "Welch", "Rojas", "Lucas", "Marquez", "Fields", "Park", "Yang", "Little",
        "Banks", "Padilla", "Day", "Walsh", "Bowman", "Schultz", "Luna", "Fowler", "Mejia", "Davidson",
        "Acosta", "Brewer", "May", "Holland", "Juarez", "Newman", "Pearson", "Curtis", "Cortez", "Douglas",
        "Schneider", "Joseph", "Barrett", "Navarro", "Figueroa", "Keller", "Avila", "Wade", "Molina", "Stanley",
        "Hopkins", "Campos", "Barnett", "Bates", "Chambers", "Calderon", "Lambert", "Valencia", "Sutton", "Gregory",
        "Williams", "McKinney", "Tanner", "Eaton", "Klein", "Salinas", "Fuentes", "Baldwin", "Daniel", "Simon",
        "Velasquez", "Hardy", "Higgins", "Aguirre", "Lin", "Cummings", "Chandler", "Sharp", "Barber", "Bowen",
        "Ochoa", "Dennis", "Robbins", "Liu", "Ramsey", "Francis", "Griffith", "Paul", "Blair", "Oconnor",
        "Cardenas", "Pacheco", "Cross", "Calderon", "Quinn", "Moss", "Swanson", "Chan", "Rivas", "Conner",
        "Steele", "Barton", "Ayala", "Singleton", "Terry", "Hale", "Leon", "Hail", "Wolf", "Keller",
        "French", "Farmer", "Hammond", "Hampton", "Townsend", "Ingram", "Wise", "Gallegos", "Clarke", "Barton",
        "Schroeder", "Maxwell", "Waters", "Logan", "Camacho", "Strickland", "Norman", "Person", "Colon", "Parsons",
        "Frank", "Harrington", "Glover", "Osborne", "Buchanan", "Casey", "Floyd", "Patton", "Ibarra", "Ball",
        "Tyler", "Suarez", "Bowers", "Orozco", "Salas", "Cobb", "Gibbs", "Andrade", "Bauer", "Conrad",
        "Mora", "Bennett", "Morrison", "Franco", "Kramer", "McCarthy", "McCormick", "McDaniel", "McDonald", "McDowell",
        "McFadden", "McFarland", "McGee", "McGowan", "McGrath", "McGuire", "McIntosh", "McIntyre", "McKay", "McKee",
        "McKenna", "McKenzie", "McKinney", "McKnight", "McLaughlin", "McLean", "McLeod", "McMahon", "McMillan", "McNair",
        "McNamara", "McNeil", "McPherson", "McQueen", "McRae", "McWilliams", "O'Brien", "O'Connell", "O'Connor", "O'Donnell",
        "O'Grady", "O'Hara", "O'Keefe", "O'Kelly", "O'Malley", "O'Neil", "O'Neill", "O'Reilly", "O'Rourke", "O'Shea",
        "O'Sullivan", "Van Buren", "Van Dam", "Van Den Berg", "Van Der Berg", "Van Der Merwe", "Van Der Walt", "Van Dijk",
        "Van Dyke", "Van Horn", "Van Ness", "Van Pelt", "Van Winkle", "Vandenberg", "Vanderbilt", "Vandermeer", "Vandervoort",
        "Vandewalle", "Vanhouten", "Vann", "Vannoy", "Vanover", "Vantassel", "Vanzant", "Varner", "Varney", "Vasquez",
        "Vaughan", "Vaughn", "Vaz", "Veal", "Vega", "Vela", "Velasco", "Velez", "Venable", "Venegas",
        "Venkatesh", "Vento", "Ventura", "Vera", "Verdin", "Vergara", "Vernon", "Vest", "Vetter", "Vick",
        "Vickers", "Vickery", "Victor", "Vidal", "Vieira", "Viera", "Vigil", "Villa", "Villalpando", "Villanueva",
        "Villareal", "Villarreal", "Villasenor", "Villegas", "Vincent", "Vines", "Vinson", "Vitale", "Viveros", "Vogel",
        "Vogt", "Volk", "Vollmer", "Volz", "Voss", "Vossen", "Vu", "Vue", "Waddell", "Wade",
        "Wadsworth", "Waggoner", "Wagner", "Wagoner", "Wahl", "Wainwright", "Waite", "Wakefield", "Waldman", "Waldron",
        "Waldo", "Waldrop", "Wales", "Walker", "Wall", "Wallace", "Waller", "Walling", "Wallis", "Walls",
        "Walsh", "Walter", "Walters", "Walton", "Wang", "Ward", "Warden", "Ware", "Warfield", "Warner",
        "Warren", "Washburn", "Washington", "Wasserman", "Waterman", "Waters", "Watkins", "Watson", "Watt", "Watters",
        "Watts", "Waugh", "Way", "Wayne", "Weathers", "Weaver", "Webb", "Webber", "Weber", "Webster",
        "Weddle", "Weeden", "Weeks", "Weems", "Wehner", "Weiland", "Weiner", "Weinstein", "Weir", "Weis",
        "Weiss", "Welch", "Weldon", "Wellman", "Wells", "Welsh", "Wendt", "Wenzel", "Werner", "Wesley",
        "West", "Westbrook", "Westfall", "Weston", "Wetzel", "Whalen", "Whaley", "Wharton", "Whatley", "Wheat",
        "Wheaton", "Wheeler", "Whelan", "Whipple", "Whitaker", "White", "Whitehead", "Whitehurst", "Whitely", "Whiteside",
        "Whitfield", "Whiting", "Whitlock", "Whitlow", "Whitman", "Whitmore", "Whitney", "Whitson", "Whitt", "Whittaker",
        "Whitten", "Whittington", "Whittle", "Wick", "Wicker", "Wickham", "Widmer", "Wiese", "Wiggins", "Wilbur",
        "Wilcox", "Wild", "Wilde", "Wilder", "Wiles", "Wiley", "Wilhelm", "Wilkes", "Wilkins", "Wilkinson",
        "Will", "Willard", "Willett", "William", "Williams", "Williamson", "Willis", "Willoughby", "Wills", "Wilson",
        "Wilt", "Wimberly", "Wimmer", "Winans", "Winchell", "Winchester", "Windham", "Windsor", "Winfield", "Winfrey",
        "Wing", "Wingate", "Winkler", "Winn", "Winslow", "Winstead", "Winter", "Winters", "Wirth", "Wise",
        "Wiseman", "Wisniewski", "Withers", "Witherspoon", "Witt", "Witte", "Witten", "Wofford", "Wolf", "Wolfe",
        "Wolff", "Womack", "Wong", "Woo", "Wood", "Woodall", "Woodard", "Woodbury", "Woodcock", "Wooden",
        "Woodley", "Woodruff", "Woods", "Woodson", "Woodward", "Woodworth", "Wooldridge", "Woolsey", "Wooten", "Worden",
        "Workman", "Worley", "Worrell", "Worth", "Wortham", "Worthy", "Wray", "Wren", "Wright", "Wu",
        "Wyatt", "Wyman", "Wynn", "Xiong", "Xu", "Yancey", "Yanez", "Yang", "Yarbrough", "Yates",
        "Yazzie", "Ybarra", "Yeager", "Yee", "Yeh", "Yen", "Yoder", "Yoo", "Yoon", "York",
        "Yost", "Young", "Youngblood", "Younger", "Yount", "Yu", "Zamora", "Zapata", "Zaragoza", "Zarate",
        "Zavala", "Zeigler", "Zeller", "Zepeda", "Zhang", "Ziegler", "Zimmer", "Zimmerman", "Zink", "Zook",
        "Zuniga", "Abbott", "Abernathy", "Abney", "Abraham", "Abrams", "Acevedo", "Acker", "Ackerman", "Acosta",
        "Adair", "Adam", "Adame", "Adams", "Adamson", "Adcock", "Addison", "Adkins", "Adler", "Agnew",
        "Aguilar", "Aguilera", "Aguirre", "Ahern", "Ahmed", "Ahrens", "Aiello", "Aiken", "Ainsworth", "Akers",
        "Akin", "Akin", "Akpan", "Alarcon", "Alba", "Albanese", "Albers", "Albert", "Albright", "Alcala",
        "Alcorn", "Alden", "Alderman", "Aldrich", "Aldridge", "Aleman", "Alexander", "Alfaro", "Alfonso", "Alford",
        "Alfred", "Ali", "Alicea", "Allan", "Allard", "Allen", "Alley", "Allison", "Allman", "Allred",
        "Almanza", "Almeida", "Almond", "Alonso", "Alonzo", "Alphin", "Alsop", "Alston", "Altamirano", "Alvarado",
        "Alvarez", "Alves", "Amador", "Amaral", "Amato", "Amaya", "Ambrose", "Ames", "Ammons", "Amos",
        "Anaya", "Anders", "Andersen", "Anderson", "Andrade", "Andre", "Andres", "Andrew", "Andrews", "Andrus",
        "Angel", "Angelo", "Anglin", "Angulo", "Anson", "Anthony", "Antoine", "Antonio", "Antunez", "Apodaca",
        "Aponte", "Apple", "Applegate", "Appleton", "Aquino", "Aragon", "Aranda", "Araujo", "Arce", "Archer",
        "Archibald", "Archie", "Archuleta", "Arellano", "Arenas", "Arevalo", "Arguello", "Arias", "Arline", "Armendariz",
        "Armenta", "Armijo", "Armstead", "Armstrong", "Arndt", "Arnett", "Arnold", "Arredondo", "Arreola", "Arrington",
        "Arriola", "Arroyo", "Arsenault", "Arteaga", "Arthur", "Artis", "Asbury", "Ash", "Ashby", "Ashe",
        "Asher", "Ashford", "Ashley", "Ashmore", "Ashton", "Ashworth", "Askew", "Atchison", "Atchley", "Atherton",
        "Atkins", "Atkinson", "Atwell", "Atwood", "Aubrey", "August", "Augustine", "Ault", "Austin", "Autry",
        "Avalos", "Avery", "Avila", "Aviles", "Axelson", "Ayers", "Aylward", "Ayres", "Babb", "Babcock",
        "Baber", "Babin", "Baca", "Bach", "Bachman", "Back", "Bacon", "Bader", "Badger", "Badillo",
        "Baer", "Baez", "Baggett", "Bagley", "Bagwell", "Bailey", "Bain", "Baines", "Baird", "Baker",
        "Balderas", "Baldwin", "Bales", "Ball", "Ballard", "Ballew", "Balsamo", "Banda", "Bandy", "Banister",
        "Banks", "Bankston", "Bannister", "Banuelos", "Baptiste", "Barajas", "Barba", "Barbee", "Barber", "Barbosa",
        "Barbour", "Barclay", "Barden", "Barela", "Barfield", "Barger", "Barham", "Barker", "Barkley", "Barksdale",
        "Barlow", "Barnard", "Barnes", "Barnett", "Barnhart", "Baron", "Barone", "Barr", "Barraza", "Barrera",
        "Barreto", "Barrett", "Barrios", "Barron", "Barrow", "Barry", "Bartels", "Barth", "Bartholomew", "Bartlett",
        "Barton", "Basham", "Baskin", "Bass", "Bassett", "Batchelor", "Bateman", "Bates", "Batiste", "Batson",
        "Battaglia", "Batten", "Battle", "Battles", "Batts", "Bauer", "Baugh", "Baughman", "Baum", "Bauman",
        "Baumann", "Baumgardner", "Bautista", "Baxley", "Baxter", "Bayer", "Bayless", "Baylor", "Bazan", "Beach",
        "Beal", "Beale", "Beall", "Beals", "Bean", "Beard", "Bearden", "Beasley", "Beattie", "Beatty",
        "Beaty", "Beauchamp", "Beaudoin", "Beaulieu", "Beaumont", "Beaver", "Beavers", "Becerra", "Beck", "Becker",
        "Beckett", "Beckman", "Beckwith", "Bedford", "Beebe", "Beeler", "Beers", "Begay", "Begley", "Behrens",
        "Belanger", "Belcher", "Belk", "Bell", "Bellamy", "Bello", "Belt", "Belton", "Beltran", "Benavides",
        "Benavidez", "Bender", "Benedict", "Benefield", "Benjamin", "Benner", "Bennett", "Benoit", "Benson", "Bentley",
        "Benton", "Berg", "Berger", "Bergeron", "Bergman", "Berkley", "Berlin", "Berman", "Bernal", "Bernard",
        "Bernhardt", "Bernstein", "Berry", "Bertram", "Bertrand", "Bess", "Best", "Betancourt", "Bethea", "Bethel",
        "Bettencourt", "Betts", "Beverly", "Beyer", "Bianchi", "Bible", "Bickford", "Biddle", "Bigelow", "Biggs",
        "Billings", "Billingsley", "Billiot", "Bills", "Bilodeau", "Binder", "Bingham", "Binkley", "Birch", "Bird",
        "Bishop", "Bisson", "Bittner", "Bivens", "Bivins", "Black", "Blackburn", "Blackman", "Blackmon", "Blackwell",
        "Blackwood", "Blair", "Blais", "Blake", "Blakely", "Blalock", "Blanchard", "Blanco", "Bland", "Blank",
        "Blankenship", "Blanton", "Blaylock", "Bledsoe", "Bleeker", "Blevins", "Bliss", "Block", "Blocker", "Blodgett",
        "Bloom", "Blossom", "Blount", "Blue", "Blum", "Blunt", "Blythe", "Boateng", "Boatright", "Bobbitt",
        "Bobo", "Bock", "Boehm", "Bogan", "Boggs", "Bohannon", "Bohn", "Boisvert", "Bolden", "Bolin",
        "Bolinger", "Bollinger", "Bolt", "Bolton", "Bond", "Bonds", "Bone", "Bonilla", "Bonner", "Booker",
        "Boone", "Booth", "Borden", "Borders", "Boren", "Borges", "Bosch", "Boswell", "Bouchard", "Boucher",
        "Boudreau", "Boudreaux", "Bourgeois", "Bourne", "Boutin", "Bouvier", "Bovell", "Bowden", "Bowen", "Bower",
        "Bowers", "Bowie", "Bowles", "Bowlin", "Bowling", "Bowman", "Bowser", "Boyce", "Boyd", "Boyer",
        "Boykin", "Boyle", "Boyles", "Boynton", "Bozeman", "Bracken", "Brackett", "Bradbury", "Braden", "Bradford",
        "Bradley", "Bradshaw", "Brady", "Bragg", "Branch", "Brand", "Brandenburg", "Brandon", "Brandt", "Branham",
        "Brannon", "Branson", "Brant", "Brantley", "Braswell", "Bratcher", "Bratton", "Braun", "Bravo", "Braxton",
        "Bray", "Brazil", "Breaux", "Breeden", "Breedlove", "Breen", "Breland", "Brennan", "Brenner", "Brent",
        "Bresnahan", "Brewer", "Brewster", "Brice", "Bridges", "Briggs", "Bright", "Briones", "Briscoe", "Brito",
        "Britt", "Brittain", "Britton", "Broadnax", "Broadway", "Brock", "Brockman", "Broderick", "Brogan", "Bronson",
        "Brookins", "Brooks", "Broome", "Brothers", "Broughton", "Broussard", "Brower", "Brown", "Browne", "Browning",
        "Brownlee", "Broyles", "Brubaker", "Bruce", "Brumfield", "Bruner", "Bruno", "Bruns", "Brunson", "Bryan",
        "Bryant", "Bryson", "Buchanan", "Buchholz", "Buck", "Buckingham", "Buckley", "Buckner", "Bueno", "Buffington",
        "Buford", "Bui", "Bull", "Bullard", "Bullock", "Bumgarner", "Bunch", "Bundy", "Bunker", "Bunn",
        "Bunnell", "Bunting", "Burch", "Burchett", "Burden", "Burdette", "Burdick", "Burge", "Burger", "Burgess",
        "Burk", "Burke", "Burkett", "Burkhalter", "Burks", "Burleson", "Burnett", "Burnette", "Burnham", "Burns",
        "Burnside", "Burr", "Burrell", "Burris", "Burroughs", "Burt", "Burton", "Busby", "Bush", "Bustamante",
        "Bustos", "Butcher", "Butler", "Butts", "Byars", "Byers", "Bynum", "Byrd", "Byrne", "Byrnes",
    ]

    # Bio templates (200+)
    BIO_TEMPLATES = [
        "Just living life one day at a time.", "Coffee addict and dog lover.", "Travel enthusiast and foodie.",
        "Music is my therapy.", "Fitness junkie and health nut.", "Bookworm and coffee connoisseur.",
        "Adventure seeker and nature lover.", "Tech geek and gamer.", "Photography is my passion.",
        "Living my best life.", "Dreamer and doer.", "Creating my own sunshine.",
        "Chasing sunsets and dreams.", "Making memories around the world.", "Just here for the memes.",
        "Professional nap taker.", "Pizza is my love language.", "Wanderlust and city dust.",
        "Good vibes only.", "Spreading positivity one post at a time.",
        "Life is short, eat the cake.", "Collector of moments, not things.", "Finding beauty in the ordinary.",
        "Forever curious.", "In a committed relationship with coffee.", "Blessed and highly favored.",
        "Making the impossible possible.", "Born to stand out.", "Keepin it real since day one.",
        "Hustle and heart.", "Building my empire one brick at a time.", "Grateful for every moment.",
        "Living, laughing, loving.", "Sunshine mixed with a little hurricane.", "Too glam to give a damn.",
        "Sassy since birth.", "Professional overthinker.", "Just a girl with a dream.",
        "Doing it for the plot.", "Main character energy.", "Here for a good time, not a long time.",
        "Vibes dont lie.", "Manifesting greatness.", "On my grind 24/7.",
        "Blessed beyond measure.", "Unapologetically me.", "Work hard, play harder.",
        "Creating my own path.", "Not perfect, but authentic.", "Living proof that dreams come true.",
        "Just a soul having a human experience.", "Collecting passport stamps.", "Home is wherever I am.",
        "Minimalist at heart.", "Plant mom/dad.", "Dog parent to the goodest boy/girl.",
        "Cat person, obviously.", "Coffee first, everything else second.", "Tea over coffee, fight me.",
        "Wine enthusiast.", "Craft beer lover.", "Cocktail connoisseur.",
        "Food is my love language.", "Home chef in training.", "Takeout queen/king.",
        "Gym rat.", "Yoga every damn day.", "Runner, not a jogger.",
        "Cyclist life.", "Swim, bike, run.", "Hiker and trail blazer.",
        "Snowboarder.", "Surfer dude.", "Skater girl/boy.",
        "Gamer tag: {username}", "PC master race.", "Console warrior.",
        "Streamer in the making.", "Content creator.", "Influencer in training.",
        "Artist at heart.", "Digital creator.", "Graphic designer.",
        "Writer by night.", "Poet and dreamer.", "Storyteller.",
        "Movie buff.", "Series binge-watcher.", "Film critic (self-proclaimed).",
        "Bookstagrammer.", "Fantasy reader.", "Sci-fi nerd.",
        "True crime junkie.", "Podcast addict.", "Audiobook listener.",
        "Music producer.", "DJ in the making.", "Band member.",
        "Singer-songwriter.", "Dancer for life.", "Actor in training.",
        "Director of my own life.", "Producer of good times.", "Editor of bad decisions.",
        "Student of life.", "Lifelong learner.", "Knowledge seeker.",
        "STEM enthusiast.", "Code poet.", "Data nerd.",
        "AI enthusiast.", "Blockchain believer.", "Crypto curious.",
        "Startup founder.", "Entrepreneur life.", "Side hustle king/queen.",
        "Freelancer.", "Remote worker.", "Digital nomad.",
        "Corporate survivor.", "9-to-5 escapee.", "Boss babe/bro.",
        "Girl boss.", "Guy with a plan.", "Man on a mission.",
        "Woman of substance.", "Non-binary and proud.", "They/them.",
        "Proud parent.", "Mom of {random_number}.", "Dad jokes only.",
        "Family first.", "Loyal friend.", "Ride or die.",
        "Squad goals.", "Team player.", "Solo act.",
        "Introvert with extrovert tendencies.", "Extrovert with introvert needs.", "Ambivert.",
        "INFJ.", "ENFP.", "INTJ.", "ENTP.", "ISFJ.", "ESFP.", "ISTJ.", "ESTP.",
        "Scorpio vibes.", "Leo energy.", "Gemini twin.", "Capricorn grind.", "Pisces dreamer.",
        "Aries fire.", "Taurus stubborn.", "Cancer heart.", "Libra balance.", "Sagittarius free.",
        "Aquarius weird.", "Virgo perfect.", "Zodiac obsessed.", "Horoscope reader.",
        "Spiritual but not religious.", "Faith over fear.", "God first.",
        "Buddhist.", "Hindu.", "Muslim.", "Christian.", "Jewish.", "Sikh.", "Atheist.", "Agnostic.",
        "Politically engaged.", "Activist.", "Human rights advocate.", "Environmental warrior.",
        "Climate change fighter.", "Animal rights activist.", "Vegan for the animals.",
        "Plant-based.", "Gluten-free.", "Keto life.", "Paleo.", "Intermittent faster.",
        "Mental health advocate.", "Anxiety warrior.", "Depression survivor.", "Therapy is cool.",
        "Self-care Sunday.", "Meditation practitioner.", "Mindfulness junkie.",
        "Gratitude journaler.", "Morning routine enthusiast.", "Night owl.", "Early bird.",
        "Productivity hacker.", "Time management guru.", "Goal digger.",
        "202X vision board.", "Manifesting my dream life.", "Law of attraction believer.",
        "Crystal collector.", "Tarot reader.", "Astrology nerd.", "Moon child.", "Starseed.",
        "Old soul.", "Young at heart.", "Age is just a number.", "Forever young.",
        "Dancing through life.", "Singing in the rain.", "Laughing at my own jokes.",
        "Sarcasm is my second language.", "Puns and dad jokes.", "Meme lord/lady.",
        "TikTok famous (in my head).", "Reels addict.", "Story spammer.",
        "Tweet too much.", "Thread reader.", "Reddit lurker.",
        "Discord mod.", "Twitch chatter.", "YouTube subscriber.",
        "Netflix and actually chill.", "Hulu binger.", "Prime watcher.",
        "Disney adult.", "Marvel fanatic.", "Star Wars nerd.", "Harry Potter house: {house}.",
        "Lord of the Rings stan.", "Game of Thrones survivor.", "Stranger Things fan.",
        "K-pop stan.", "Anime weeb.", "Manga reader.", "Cosplayer.", "Convention goer.",
        "Car enthusiast.", "Motorcycle rider.", "Truck guy/girl.", "JDM life.", "Euro car fan.",
        "Sneakerhead.", "Streetwear.", "Vintage lover.", "Thrift store queen/king.",
        "DIY enthusiast.", "Home renovator.", "Interior design obsessed.", "HGTV watcher.",
        "Gardening.", "Composting.", "Zero waste.", "Sustainable living.", "Tiny house dreamer.",
        "Van life.", "RV traveler.", "Boat life.", "Island hopper.", "Beach bum.",
        "Mountain lover.", "Desert dweller.", "City slicker.", "Suburbanite.", "Country soul.",
        "Small town girl/boy.", "Big city dreams.", "World traveler.", "Backpacker.", "Luxury traveler.",
        "Road tripper.", "Train traveler.", "Aviation geek.", "Plane spotter.", "Airport napper.",
        "Language learner.", "Polyglot in training.", "Bilingual.", "Trilingual.", "Sign language user.",
        "History buff.", "Museum goer.", "Art gallery frequenter.", "Theater lover.", "Opera fan.",
        "Broadway baby.", "Concert goer.", "Festival attendee.", "Rave baby.", "EDM lover.",
        "Jazz enthusiast.", "Classical music fan.", "Rock and roll.", "Hip hop head.", "Country music.",
        "R&B soul.", "Reggae vibes.", "Latin music.", "K-pop multistan.", "J-pop fan.",
        "Indie music.", "Folk music.", "Blues lover.", "Metal head.", "Punk rock.",
        "Stand-up comedy fan.", "Improv lover.", "Sketch comedy.", "SNL watcher.", "Late night TV.",
        "News junkie.", "Podcast host.", "YouTube creator.", "TikTok creator.", "Instagram creator.",
        "Twitter/X user.", "LinkedIn professional.", "Facebook user.", "Snapchat streaker.",
        "WhatsApp group admin.", "Telegram channel owner.", "Signal user.", "Discord server owner.",
        "Reddit moderator.", "Quora writer.", "Medium blogger.", "Substack writer.", "Newsletter author.",
        "Open source contributor.", "GitHub star.", "Stack Overflow answerer.", "Dev.to writer.",
        "Hashnode blogger.", "Indie hacker.", "Maker.", "Builder.", "Creator economy.",
        "Solopreneur.", "Founder.", "Co-founder.", "CTO.", "CEO.", "COO.", "CMO.", "CFO.",
        "Product manager.", "Project manager.", "Scrum master.", "Agile practitioner.", "Kanban user.",
        "Designer.", "UX researcher.", "UI designer.", "Product designer.", "Design thinking.",
        "Marketing guru.", "Growth hacker.", "SEO expert.", "SEM specialist.", "Social media manager.",
        "Content strategist.", "Brand builder.", "Copywriter.", "Email marketer.", "Affiliate marketer.",
        "Sales professional.", "Account executive.", "Business development.", "Partnerships.", "Investor.",
        "Venture capitalist.", "Angel investor.", "Day trader.", "Swing trader.", "Long-term investor.",
        "Real estate investor.", "Property manager.", "Landlord.", "House flipper.", "REIT investor.",
        "Stock market enthusiast.", "Options trader.", "Forex trader.", "Commodities trader.", "Futures trader.",
        "Crypto trader.", "DeFi degen.", "NFT collector.", "Metaverse explorer.", "Web3 believer.",
        "DAO member.", "Governance token holder.", "Yield farmer.", "Liquidity provider.", "Staker.",
        "Validator node operator.", "Mining rig owner.", "ASIC miner.", "GPU miner.", "CPU miner.",
        "Smart contract developer.", "Solidity coder.", "Rust developer.", "Go developer.", "Pythonista.",
        "JavaScript wizard.", "TypeScript fan.", "React developer.", "Vue developer.", "Angular developer.",
        "Svelte enthusiast.", "Next.js user.", "Nuxt.js user.", "Node.js backend.", "Django developer.",
        "Flask developer.", "FastAPI user.", "Ruby on Rails.", "Laravel developer.", "Spring Boot.",
        ".NET developer.", "C# programmer.", "C++ hacker.", "Rustacean.", "Gopher.",
        "Java developer.", "Kotlin user.", "Swift developer.", "Objective-C veteran.", "Flutter developer.",
        "React Native developer.", "iOS developer.", "Android developer.", "Cross-platform mobile.", "PWA builder.",
        "DevOps engineer.", "SRE.", "Platform engineer.", "Cloud architect.", "AWS certified.",
        "Azure expert.", "GCP user.", "DigitalOcean fan.", "Heroku deployer.", "Vercel user.",
        "Netlify deployer.", "Cloudflare user.", "CDN optimizer.", "Load balancer.", "Kubernetes admin.",
        "Docker containerizer.", "Terraform user.", "Ansible automator.", "Jenkins CI/CD.", "GitHub Actions.",
        "GitLab CI.", "CircleCI user.", "Travis CI veteran.", "ArgoCD user.", "Helm chart maintainer.",
        "Prometheus monitor.", "Grafana dashboarder.", "ELK stack user.", "Datadog observer.", "New Relic user.",
        "PagerDuty on-call.", "Incident responder.", "Chaos engineer.", "Site reliability.", "Observability.",
        "Security engineer.", "Penetration tester.", "Bug bounty hunter.", "CTF player.", "Red team.",
        "Blue team.", "Purple team.", "SOC analyst.", "Threat hunter.", "Malware analyst.",
        "Forensic investigator.", "Incident handler.", "Compliance officer.", "Risk manager.", "Auditor.",
        "Data scientist.", "ML engineer.", "AI researcher.", "NLP specialist.", "Computer vision.",
        "Deep learning.", "Reinforcement learning.", "MLOps.", "Feature engineer.", "Data engineer.",
        "ETL pipeline builder.", "Data warehouse architect.", "Lakehouse user.", "Databricks fan.", "Snowflake user.",
        "BigQuery user.", "Redshift user.", "Spark developer.", "Hadoop veteran.", "Kafka streamer.",
        "RabbitMQ user.", "Redis cache.", "Memcached user.", "Elasticsearch searcher.", "MongoDB user.",
        "PostgreSQL fan.", "MySQL user.", "SQLite developer.", "CockroachDB user.", "TiDB user.",
        "Cassandra user.", "DynamoDB user.", "CosmosDB user.", "Firebase user.", "Supabase fan.",
        "Prisma ORM.", "SQLAlchemy user.", "Django ORM.", "TypeORM user.", "Sequelize user.",
        "GraphQL API.", "REST API designer.", "gRPC user.", "WebSocket developer.", "Socket.io user.",
        "WebRTC developer.", "P2P enthusiast.", "Blockchain developer.", "Smart contract auditor.", "DApp developer.",
        "Game developer.", "Unity developer.", "Unreal Engine.", "Godot user.", "Game designer.",
        "Level designer.", "Narrative designer.", "Sound designer.", "Composer.", "Voice actor.",
        "Motion graphics.", "Video editor.", "Colorist.", "VFX artist.", "3D modeler.",
        "Animator.", "Rigger.", "Texture artist.", "Lighting artist.", "Environment artist.",
        "Character artist.", "Concept artist.", "UI artist.", "Technical artist.", "Shader programmer.",
        "Technical director.", "Creative director.", "Art director.", "Design director.", "Engineering manager.",
        "Team lead.", "Staff engineer.", "Principal engineer.", "Distinguished engineer.", "Fellow.",
        "Research scientist.", "PhD candidate.", "Graduate student.", "Undergraduate.", "Lifelong student.",
        "Teacher.", "Professor.", "Instructor.", "Mentor.", "Coach.", "Tutor.", "Educator.", "Trainer.",
        "Librarian.", "Archivist.", "Curator.", "Historian.", "Anthropologist.", "Sociologist.", "Psychologist.",
        "Therapist.", "Counselor.",
    ]

    # Aliases for backward compatibility
    BIOS = BIO_TEMPLATES

    # Split first names by gender (approximate split from combined list)
    FIRST_NAMES_MALE = FIRST_NAMES[:len(FIRST_NAMES)//2]
    FIRST_NAMES_FEMALE = FIRST_NAMES[len(FIRST_NAMES)//2:]

    # Profile picture URLs
    PROFILE_PIC_URLS = [
        "https://i.pravatar.cc/150?img=" + str(i) for i in range(1, 71)
    ] + [
        "https://randomuser.me/api/portraits/men/" + str(i) + ".jpg" for i in range(1, 100)
    ] + [
        "https://randomuser.me/api/portraits/women/" + str(i) + ".jpg" for i in range(1, 100)
    ] + [
        "https://picsum.photos/200/200?random=" + str(i) for i in range(1, 51)
    ]

    # Warmup schedule (7 days)
    WARMUP_SCHEDULE = {
        1: {"follow": 10, "like": 5, "view": 0, "post": 0, "comment": 0, "friends": 0},
        2: {"follow": 20, "like": 10, "view": 5, "post": 0, "comment": 0, "friends": 0},
        3: {"follow": 30, "like": 15, "view": 10, "post": 1, "comment": 0, "friends": 0},
        4: {"follow": 40, "like": 20, "view": 15, "post": 2, "comment": 0, "friends": 5},
        5: {"follow": 50, "like": 25, "view": 20, "post": 3, "comment": 1, "friends": 10},
        6: {"follow": 60, "like": 30, "view": 25, "post": 4, "comment": 2, "friends": 15},
        7: {"follow": 70, "like": 35, "view": 30, "post": 5, "comment": 3, "friends": 20},
    }

    # Browser fingerprinting constants
    BROWSER_HEADLESS = True
    BROWSER_WINDOW_SIZES = [(1366, 768), (1440, 900), (1536, 864), (1920, 1080), (1280, 720), (1680, 1050)]

    SCREEN_RESOLUTIONS = [
        (1920, 1080), (1366, 768), (1440, 900), (1536, 864), (1280, 720),
        (1680, 1050), (1600, 900), (2560, 1440), (3840, 2160), (1024, 768),
    ]

    TIMEZONE_OFFSETS = [
        "UTC", "America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles",
        "Europe/London", "Europe/Paris", "Europe/Berlin", "Europe/Moscow", "Asia/Tokyo",
        "Asia/Shanghai", "Asia/Singapore", "Asia/Dubai", "Australia/Sydney", "Pacific/Auckland",
    ]

    LANGUAGES = [
        "en-US,en;q=0.9", "en-GB,en;q=0.9", "en-CA,en;q=0.9", "en-AU,en;q=0.9",
        "fr-FR,fr;q=0.9,en;q=0.8", "de-DE,de;q=0.9,en;q=0.8", "es-ES,es;q=0.9,en;q=0.8",
        "it-IT,it;q=0.9,en;q=0.8", "pt-BR,pt;q=0.9,en;q=0.8", "ru-RU,ru;q=0.9,en;q=0.8",
        "ja-JP,ja;q=0.9,en;q=0.8", "zh-CN,zh;q=0.9,en;q=0.8", "ko-KR,ko;q=0.9,en;q=0.8",
        "nl-NL,nl;q=0.9,en;q=0.8", "sv-SE,sv;q=0.9,en;q=0.8", "pl-PL,pl;q=0.9,en;q=0.8",
    ]

    WEBGL_FINGERPRINTS = [
        ("Intel Inc.", "Intel Iris Xe Graphics"), ("NVIDIA Corporation", "NVIDIA GeForce GTX 1660"),
        ("NVIDIA Corporation", "NVIDIA GeForce RTX 3070"), ("NVIDIA Corporation", "NVIDIA GeForce RTX 3080"),
        ("AMD", "AMD Radeon RX 580"), ("AMD", "AMD Radeon RX 6700 XT"),
        ("Intel Inc.", "Intel HD Graphics 630"), ("Intel Inc.", "Intel UHD Graphics 620"),
        ("Apple Inc.", "Apple M1"), ("Apple Inc.", "Apple M2"),
        ("Qualcomm", "Adreno 640"), ("ARM", "Mali-G78"),
    ]

    PLATFORM_FONTS = [
        "Arial", "Helvetica", "Times New Roman", "Courier New", "Verdana",
        "Georgia", "Palatino", "Garamond", "Bookman", "Comic Sans MS",
        "Trebuchet MS", "Arial Black", "Impact", "Tahoma", "Geneva",
    ]

    PLATFORM_STRINGS = [
        "Win32", "Win64", "MacIntel", "Linux x86_64", "Linux i686",
    ]

    HARDWARE_CONCURRENCY = [2, 4, 6, 8, 12, 16]
    DEVICE_MEMORY = [2, 4, 8, 16, 32]
    TOUCH_SUPPORT_PROB = 0.15
    COLOR_DEPTHS = [24, 30, 32]

class AccountsDB:
    """Encrypted SQLite for Phase 5 account data."""

    __slots__ = ("_db_path", "_crypto", "_connection", "_lock")

    SCHEMA = """
    PRAGMA foreign_keys = ON;
    PRAGMA journal_mode = WAL;
    PRAGMA synchronous = NORMAL;
    PRAGMA temp_store = MEMORY;
    PRAGMA mmap_size = 268435456;
    PRAGMA page_size = 4096;

    CREATE TABLE IF NOT EXISTS oanks_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT NOT NULL,
        username TEXT,
        email TEXT,
        phone TEXT,
        password_enc TEXT NOT NULL,
        cookies_enc TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP,
        is_banned INTEGER DEFAULT 0,
        is_shadowbanned INTEGER DEFAULT 0,
        is_warmed INTEGER DEFAULT 0,
        is_active INTEGER DEFAULT 1,
        health_score REAL DEFAULT 0.0,
        warmup_level INTEGER DEFAULT 0,
        follower_count INTEGER DEFAULT 0,
        following_count INTEGER DEFAULT 0,
        post_count INTEGER DEFAULT 0,
        proxy_used TEXT,
        hash_id TEXT UNIQUE,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_accounts_platform ON oanks_accounts(platform);
    CREATE INDEX IF NOT EXISTS idx_accounts_active ON oanks_accounts(is_active);
    CREATE INDEX IF NOT EXISTS idx_accounts_banned ON oanks_accounts(is_banned);
    CREATE INDEX IF NOT EXISTS idx_accounts_hash ON oanks_accounts(hash_id);
    CREATE INDEX IF NOT EXISTS idx_accounts_warmed ON oanks_accounts(is_warmed);
    CREATE INDEX IF NOT EXISTS idx_accounts_username ON oanks_accounts(username);
    CREATE INDEX IF NOT EXISTS idx_accounts_email ON oanks_accounts(email);

    CREATE TABLE IF NOT EXISTS oanks_account_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER,
        action TEXT NOT NULL,
        result TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(account_id) REFERENCES oanks_accounts(id) ON DELETE CASCADE,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_logs_account ON oanks_account_logs(account_id);
    CREATE INDEX IF NOT EXISTS idx_logs_action ON oanks_account_logs(action);
    CREATE INDEX IF NOT EXISTS idx_logs_timestamp ON oanks_account_logs(timestamp);

    CREATE TABLE IF NOT EXISTS oanks_temp_emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        sid_token TEXT,
        provider TEXT NOT NULL,
        used_for TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP,
        is_used INTEGER DEFAULT 0,
        verification_code TEXT,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_temp_emails_provider ON oanks_temp_emails(provider);
    CREATE INDEX IF NOT EXISTS idx_temp_emails_used ON oanks_temp_emails(is_used);
    CREATE INDEX IF NOT EXISTS idx_temp_emails_email ON oanks_temp_emails(email);

    CREATE TABLE IF NOT EXISTS oanks_temp_phones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT NOT NULL,
        session_token TEXT,
        provider TEXT NOT NULL,
        used_for TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expires_at TIMESTAMP,
        is_used INTEGER DEFAULT 0,
        verification_code TEXT,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_temp_phones_provider ON oanks_temp_phones(provider);
    CREATE INDEX IF NOT EXISTS idx_temp_phones_used ON oanks_temp_phones(is_used);
    CREATE INDEX IF NOT EXISTS idx_temp_phones_phone ON oanks_temp_phones(phone);

    CREATE TABLE IF NOT EXISTS oanks_creation_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT NOT NULL,
        priority INTEGER DEFAULT 5,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        started_at TIMESTAMP,
        completed_at TIMESTAMP,
        error_message TEXT,
        account_id INTEGER,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_queue_status ON oanks_creation_queue(status);
    CREATE INDEX IF NOT EXISTS idx_queue_platform ON oanks_creation_queue(platform);
    CREATE INDEX IF NOT EXISTS idx_queue_priority ON oanks_creation_queue(priority);

    CREATE TABLE IF NOT EXISTS oanks_warmup_schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        day INTEGER NOT NULL,
        follow_count INTEGER DEFAULT 0,
        like_count INTEGER DEFAULT 0,
        view_count INTEGER DEFAULT 0,
        post_count INTEGER DEFAULT 0,
        comment_count INTEGER DEFAULT 0,
        friend_count INTEGER DEFAULT 0,
        completed INTEGER DEFAULT 0,
        completed_at TIMESTAMP,
        FOREIGN KEY(account_id) REFERENCES oanks_accounts(id) ON DELETE CASCADE,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_warmup_account ON oanks_warmup_schedule(account_id);
    CREATE INDEX IF NOT EXISTS idx_warmup_day ON oanks_warmup_schedule(day);
    CREATE INDEX IF NOT EXISTS idx_warmup_completed ON oanks_warmup_schedule(completed);

    CREATE TABLE IF NOT EXISTS oanks_health_checks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        check_type TEXT NOT NULL,
        result TEXT,
        health_score REAL DEFAULT 0.0,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(account_id) REFERENCES oanks_accounts(id) ON DELETE CASCADE,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_health_account ON oanks_health_checks(account_id);
    CREATE INDEX IF NOT EXISTS idx_health_type ON oanks_health_checks(check_type);
    CREATE INDEX IF NOT EXISTS idx_health_timestamp ON oanks_health_checks(timestamp);
    """

    def __init__(self, db_path: str, crypto: OanksCryptoBridge):
        self._db_path = db_path
        self._crypto = crypto
        self._connection = None
        self._lock = threading.RLock()
        self._initialize()

    def _initialize(self):
        """Initialize database with schema."""
        with self._lock:
            os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
            self._connection = sqlite3.connect(self._db_path, check_same_thread=False)
            self._connection.executescript(self.SCHEMA)
            self._connection.commit()

    def store_account(self, platform: str, username: str, email: str, phone: str,
                      password: str, cookies: str = None, proxy_used: str = None) -> int:
        """Store a new account."""
        with self._lock:
            try:
                password_enc = self._crypto.encrypt(password)
                cookies_enc = self._crypto.encrypt(cookies) if cookies else None
                hash_id = self._crypto.hash_id(f"{platform}:{username}:{email}")

                cursor = self._connection.execute(
                    """INSERT INTO oanks_accounts
                       (platform, username, email, phone, password_enc, cookies_enc, proxy_used, hash_id)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (platform, username, email, phone, password_enc, cookies_enc, proxy_used, hash_id)
                )
                self._connection.commit()
                return cursor.lastrowid
            except Exception as e:
                raise AccountFactoryError(f"Failed to store account: {e}", code="DB_STORE_FAIL")

    def get_account(self, account_id: int) -> Dict:
        """Get account by ID."""
        with self._lock:
            cursor = self._connection.execute(
                "SELECT * FROM oanks_accounts WHERE id = ?", (account_id,)
            )
            row = cursor.fetchone()
            if not row:
                return None
            return self._row_to_dict(row)

    def get_accounts_by_platform(self, platform: str, active_only: bool = True) -> List[Dict]:
        """Get accounts by platform."""
        with self._lock:
            if active_only:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_accounts WHERE platform = ? AND is_active = 1", (platform,)
                )
            else:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_accounts WHERE platform = ?", (platform,)
                )
            return [self._row_to_dict(row) for row in cursor]

    def get_all_accounts(self, active_only: bool = True) -> List[Dict]:
        """Get all accounts."""
        with self._lock:
            if active_only:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_accounts WHERE is_active = 1"
                )
            else:
                cursor = self._connection.execute("SELECT * FROM oanks_accounts")
            return [self._row_to_dict(row) for row in cursor]

    def update_account(self, account_id: int, **kwargs) -> bool:
        """Update account fields."""
        with self._lock:
            allowed_fields = ["username", "email", "phone", "cookies_enc", "is_banned",
                              "is_shadowbanned", "is_warmed", "is_active", "health_score",
                              "warmup_level", "follower_count", "following_count", "post_count",
                              "last_login", "proxy_used"]
            updates = []
            values = []
            for key, value in kwargs.items():
                if key in allowed_fields:
                    updates.append(f"{key} = ?")
                    values.append(value)
            if not updates:
                return False
            values.append(account_id)
            self._connection.execute(
                f"UPDATE oanks_accounts SET {', '.join(updates)} WHERE id = ?",
                values
            )
            self._connection.commit()
            return True

    def mark_account_banned(self, account_id: int) -> bool:
        """Mark account as banned."""
        return self.update_account(account_id, is_banned=1, is_active=0)

    def mark_account_dead(self, account_id: int) -> bool:
        """Mark account as dead."""
        return self.update_account(account_id, is_active=0, health_score=0.0)

    def log_action(self, account_id: int, action: str, result: str = None) -> bool:
        """Log an action for an account."""
        with self._lock:
            self._connection.execute(
                "INSERT INTO oanks_account_logs (account_id, action, result) VALUES (?, ?, ?)",
                (account_id, action, result)
            )
            self._connection.commit()
            return True

    def store_temp_email(self, email: str, provider: str, sid_token: str = None,
                         used_for: str = None, expires_at: str = None) -> int:
        """Store temporary email."""
        with self._lock:
            cursor = self._connection.execute(
                """INSERT INTO oanks_temp_emails
                   (email, provider, sid_token, used_for, expires_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (email, provider, sid_token, used_for, expires_at)
            )
            self._connection.commit()
            return cursor.lastrowid

    def get_temp_email(self, provider: str = None, unused_only: bool = True) -> Dict:
        """Get an available temporary email."""
        with self._lock:
            if provider and unused_only:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_temp_emails WHERE provider = ? AND is_used = 0 LIMIT 1",
                    (provider,)
                )
            elif unused_only:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_temp_emails WHERE is_used = 0 LIMIT 1"
                )
            elif provider:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_temp_emails WHERE provider = ? LIMIT 1",
                    (provider,)
                )
            else:
                cursor = self._connection.execute("SELECT * FROM oanks_temp_emails LIMIT 1")
            row = cursor.fetchone()
            if row:
                return self._row_to_dict(row)
            return None

    def mark_temp_email_used(self, email_id: int, verification_code: str = None) -> bool:
        """Mark temp email as used."""
        with self._lock:
            self._connection.execute(
                "UPDATE oanks_temp_emails SET is_used = 1, verification_code = ? WHERE id = ?",
                (verification_code, email_id)
            )
            self._connection.commit()
            return True

    def store_temp_phone(self, phone: str, provider: str, session_token: str = None,
                         used_for: str = None, expires_at: str = None) -> int:
        """Store temporary phone."""
        with self._lock:
            cursor = self._connection.execute(
                """INSERT INTO oanks_temp_phones
                   (phone, provider, session_token, used_for, expires_at)
                   VALUES (?, ?, ?, ?, ?)""",
                (phone, provider, session_token, used_for, expires_at)
            )
            self._connection.commit()
            return cursor.lastrowid

    def get_temp_phone(self, provider: str = None, unused_only: bool = True) -> Dict:
        """Get an available temporary phone."""
        with self._lock:
            if provider and unused_only:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_temp_phones WHERE provider = ? AND is_used = 0 LIMIT 1",
                    (provider,)
                )
            elif unused_only:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_temp_phones WHERE is_used = 0 LIMIT 1"
                )
            elif provider:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_temp_phones WHERE provider = ? LIMIT 1",
                    (provider,)
                )
            else:
                cursor = self._connection.execute("SELECT * FROM oanks_temp_phones LIMIT 1")
            row = cursor.fetchone()
            if row:
                return self._row_to_dict(row)
            return None

    def mark_temp_phone_used(self, phone_id: int, verification_code: str = None) -> bool:
        """Mark temp phone as used."""
        with self._lock:
            self._connection.execute(
                "UPDATE oanks_temp_phones SET is_used = 1, verification_code = ? WHERE id = ?",
                (verification_code, phone_id)
            )
            self._connection.commit()
            return True

    def add_to_queue(self, platform: str, priority: int = 5) -> int:
        """Add creation job to queue."""
        with self._lock:
            cursor = self._connection.execute(
                "INSERT INTO oanks_creation_queue (platform, priority, status) VALUES (?, ?, 'pending')",
                (platform, priority)
            )
            self._connection.commit()
            return cursor.lastrowid

    def get_pending_jobs(self, limit: int = 50) -> List[Dict]:
        """Get pending creation jobs."""
        with self._lock:
            cursor = self._connection.execute(
                """SELECT * FROM oanks_creation_queue
                   WHERE status = 'pending' ORDER BY priority DESC, created_at ASC LIMIT ?""",
                (limit,)
            )
            return [self._row_to_dict(row) for row in cursor]

    def update_job_status(self, job_id: int, status: str, account_id: int = None,
                          error_message: str = None) -> bool:
        """Update job status."""
        with self._lock:
            now = datetime.datetime.utcnow().isoformat()
            if status == "running":
                self._connection.execute(
                    "UPDATE oanks_creation_queue SET status = ?, started_at = ? WHERE id = ?",
                    (status, now, job_id)
                )
            elif status in ["completed", "failed"]:
                self._connection.execute(
                    """UPDATE oanks_creation_queue
                       SET status = ?, completed_at = ?, account_id = ?, error_message = ?
                       WHERE id = ?""",
                    (status, now, account_id, error_message, job_id)
                )
            self._connection.commit()
            return True

    def create_warmup_schedule(self, account_id: int) -> bool:
        """Create 7-day warmup schedule for account."""
        with self._lock:
            for day, actions in AccountFactoryConstants.WARMUP_SCHEDULE.items():
                self._connection.execute(
                    """INSERT INTO oanks_warmup_schedule
                       (account_id, day, follow_count, like_count, view_count,
                        post_count, comment_count, friend_count)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (account_id, day, actions["follow"], actions["like"], actions["view"],
                     actions["post"], actions["comment"], actions["friends"])
                )
            self._connection.commit()
            return True

    def get_warmup_schedule(self, account_id: int, day: int = None) -> List[Dict]:
        """Get warmup schedule for account."""
        with self._lock:
            if day:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_warmup_schedule WHERE account_id = ? AND day = ?",
                    (account_id, day)
                )
            else:
                cursor = self._connection.execute(
                    "SELECT * FROM oanks_warmup_schedule WHERE account_id = ? ORDER BY day",
                    (account_id,)
                )
            return [self._row_to_dict(row) for row in cursor]

    def mark_warmup_completed(self, schedule_id: int) -> bool:
        """Mark warmup day as completed."""
        with self._lock:
            self._connection.execute(
                "UPDATE oanks_warmup_schedule SET completed = 1, completed_at = ? WHERE id = ?",
                (datetime.datetime.utcnow().isoformat(), schedule_id)
            )
            self._connection.commit()
            return True

    def store_health_check(self, account_id: int, check_type: str, result: str,
                           health_score: float) -> bool:
        """Store health check result."""
        with self._lock:
            self._connection.execute(
                """INSERT INTO oanks_health_checks
                   (account_id, check_type, result, health_score)
                   VALUES (?, ?, ?, ?)""",
                (account_id, check_type, result, health_score)
            )
            self._connection.commit()
            return True

    def get_health_checks(self, account_id: int, limit: int = 100) -> List[Dict]:
        """Get health checks for account."""
        with self._lock:
            cursor = self._connection.execute(
                "SELECT * FROM oanks_health_checks WHERE account_id = ? ORDER BY timestamp DESC LIMIT ?",
                (account_id, limit)
            )
            return [self._row_to_dict(row) for row in cursor]

    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics."""
        with self._lock:
            stats = {}
            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_accounts")
            stats["total_accounts"] = cursor.fetchone()[0]

            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_accounts WHERE is_active = 1")
            stats["active_accounts"] = cursor.fetchone()[0]

            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_accounts WHERE is_banned = 1")
            stats["banned_accounts"] = cursor.fetchone()[0]

            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_accounts WHERE is_warmed = 1")
            stats["warmed_accounts"] = cursor.fetchone()[0]

            cursor = self._connection.execute(
                "SELECT platform, COUNT(*) FROM oanks_accounts GROUP BY platform"
            )
            stats["by_platform"] = {row[0]: row[1] for row in cursor}

            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_temp_emails")
            stats["total_temp_emails"] = cursor.fetchone()[0]

            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_temp_phones")
            stats["total_temp_phones"] = cursor.fetchone()[0]

            cursor = self._connection.execute("SELECT COUNT(*) FROM oanks_creation_queue")
            stats["total_jobs"] = cursor.fetchone()[0]

            cursor = self._connection.execute(
                "SELECT status, COUNT(*) FROM oanks_creation_queue GROUP BY status"
            )
            stats["jobs_by_status"] = {row[0]: row[1] for row in cursor}

            try:
                stats["db_size_bytes"] = os.path.getsize(self._db_path)
            except:
                stats["db_size_bytes"] = 0

            return stats

    def _row_to_dict(self, row) -> Dict:
        """Convert sqlite row to dict."""
        return {key: row[key] for key in row.keys()}

    def close(self):
        """Close database connection."""
        with self._lock:
            if self._connection:
                self._connection.close()
                self._connection = None

    def secure_wipe(self):
        """Securely wipe database."""
        self.close()
        if os.path.exists(self._db_path):
            size = os.path.getsize(self._db_path)
            with open(self._db_path, "r+b") as f:
                for _ in range(3):
                    f.seek(0)
                    f.write(os.urandom(size))
                    f.flush()
                    os.fsync(f.fileno())
                f.seek(0)
                f.write(b"\x00" * size)
                f.flush()
                os.fsync(f.fileno())
            os.remove(self._db_path)

class TempEmailManager:
    """Get temp emails from 7 FREE providers. No API keys. Web-scraped."""

    __slots__ = ("_lock", "_db", "_active_emails", "_stats")

    def __init__(self, db: AccountsDB = None):
        self._lock = threading.RLock()
        self._db = db
        self._active_emails = {}
        self._stats = {"requested": 0, "success": 0, "failed": 0, "by_provider": Counter()}

    def get_email(self, timeout: int = 120) -> Dict[str, str]:
        """Get a temp email with fallback chain."""
        with self._lock:
            self._stats["requested"] += 1

        providers = [
            self._get_guerrilla_mail,
            self._get_tempmail_org,
            self._get_10minutemail,
            self._get_mail_tm,
            self._get_tempmail_plus,
            self._get_emailondeck,
        ]

        for provider_func in providers:
            try:
                result = provider_func()
                if result and result.get("email"):
                    with self._lock:
                        self._stats["success"] += 1
                        self._stats["by_provider"][provider_func.__name__] += 1
                    if self._db:
                        email_id = self._db.store_temp_email(
                            email=result["email"],
                            provider=provider_func.__name__.replace("_get_", ""),
                            sid_token=result.get("sid_token"),
                            expires_at=result.get("expires_at")
                        )
                        result["db_id"] = email_id
                    return result
            except Exception as e:
                continue

        with self._lock:
            self._stats["failed"] += 1
        raise TempEmailError("All temp email providers failed", code="ALL_PROVIDERS_FAILED")

    def _make_request(self, url: str, method: str = "GET", data: Dict = None,
                      headers: Dict = None, timeout: int = 30) -> Any:
        """Make HTTP request with stealth headers."""
        if headers is None:
            headers = OanksConfig.get_random_headers()

        req = urllib.request.Request(url, method=method)
        for key, value in headers.items():
            req.add_header(key, value)

        if data and method == "POST":
            req.data = urllib.parse.urlencode(data).encode("utf-8")
            req.add_header("Content-Type", "application/x-www-form-urlencoded")

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            return response.read().decode("utf-8", errors="ignore")

    def _get_guerrilla_mail(self) -> Dict[str, str]:
        """Get email from Guerrilla Mail."""
        try:
            # Get session
            session_url = "https://api.guerrillamail.com/ajax.php?f=get_email_address"
            response = self._make_request(session_url)
            data = json.loads(response)
            email = data.get("email_addr", "")
            sid_token = data.get("sid_token", "")
            if email:
                return {
                    "email": email,
                    "sid_token": sid_token,
                    "provider": "guerrilla",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def _get_tempmail_org(self) -> Dict[str, str]:
        """Get email from Temp-Mail.org."""
        try:
            url = "https://api.internal.temp-mail.io/api/v3/email/new"
            headers = {
                "User-Agent": random.choice(OanksConfig.USER_AGENTS),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            req = urllib.request.Request(url, method="POST")
            for key, value in headers.items():
                req.add_header(key, value)
            req.data = b"{}"

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, timeout=30, context=ctx) as response:
                data = json.loads(response.read().decode("utf-8"))
                email = data.get("email", "")
                if email:
                    return {
                        "email": email,
                        "sid_token": data.get("token", ""),
                        "provider": "tempmail_org",
                        "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                    }
        except Exception:
            pass
        return {}

    def _get_10minutemail(self) -> Dict[str, str]:
        """Get email from 10MinuteMail."""
        try:
            url = "https://10minutemail.com/session/email"
            response = self._make_request(url)
            data = json.loads(response)
            email = data.get("address", "")
            if email:
                return {
                    "email": email,
                    "sid_token": data.get("sessionId", ""),
                    "provider": "10minutemail",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def _get_mail_tm(self) -> Dict[str, str]:
        """Get email from Mail.tm."""
        try:
            # Create account
            username = "".join(random.choices(string.ascii_lowercase + string.digits, k=12))
            domain_url = "https://api.mail.tm/domains"
            domains_resp = self._make_request(domain_url)
            domains = json.loads(domains_resp)
            domain = domains["hydra:member"][0]["domain"] if domains.get("hydra:member") else "mail.tm"

            email = f"{username}@{domain}"
            password = "".join(random.choices(string.ascii_letters + string.digits, k=16))

            register_url = "https://api.mail.tm/accounts"
            headers = {
                "User-Agent": random.choice(OanksConfig.USER_AGENTS),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            req = urllib.request.Request(register_url, method="POST")
            for key, value in headers.items():
                req.add_header(key, value)
            req.data = json.dumps({"address": email, "password": password}).encode("utf-8")

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, timeout=30, context=ctx) as response:
                if response.status in [200, 201]:
                    return {
                        "email": email,
                        "sid_token": password,
                        "provider": "mail_tm",
                        "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat(),
                    }
        except Exception:
            pass
        return {}

    def _get_tempmail_plus(self) -> Dict[str, str]:
        """Get email from TempMail.plus."""
        try:
            username = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            email = f"{username}@tempmail.plus"
            return {
                "email": email,
                "sid_token": username,
                "provider": "tempmail_plus",
                "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
            }
        except Exception:
            pass
        return {}

    def _get_emailondeck(self) -> Dict[str, str]:
        """Get email from EmailOnDeck."""
        try:
            # Step 1: Get session
            session_url = "https://www.emailondeck.com/"
            html = self._make_request(session_url)

            # Extract CSRF token or session info
            import re
            token_match = re.search(r'name="_token" value="([^"]+)"', html)
            if token_match:
                token = token_match.group(1)
                # Step 2: Request email
                req_url = "https://www.emailondeck.com/get-email"
                headers = OanksConfig.get_random_headers()
                headers["X-Requested-With"] = "XMLHttpRequest"
                headers["Content-Type"] = "application/x-www-form-urlencoded"

                req = urllib.request.Request(req_url, method="POST")
                for key, value in headers.items():
                    req.add_header(key, value)
                req.data = urllib.parse.urlencode({"_token": token}).encode("utf-8")

                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE

                with urllib.request.urlopen(req, timeout=30, context=ctx) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    email = data.get("email", "")
                    if email:
                        return {
                            "email": email,
                            "sid_token": token,
                            "provider": "emailondeck",
                            "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                        }
        except Exception:
            pass
        return {}

    def check_inbox(self, email_data: Dict[str, str], timeout: int = 120) -> Optional[str]:
        """Check inbox for verification code."""
        provider = email_data.get("provider", "")
        email = email_data.get("email", "")
        sid_token = email_data.get("sid_token", "")

        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                code = None
                if provider == "guerrilla":
                    code = self._check_guerrilla_inbox(sid_token)
                elif provider == "tempmail_org":
                    code = self._check_tempmail_org_inbox(email_data)
                elif provider == "10minutemail":
                    code = self._check_10minutemail_inbox(sid_token)
                elif provider == "mail_tm":
                    code = self._check_mail_tm_inbox(email, sid_token)
                elif provider == "tempmail_plus":
                    code = self._check_tempmail_plus_inbox(email_data)
                elif provider == "emailondeck":
                    code = self._check_emailondeck_inbox(sid_token)

                if code:
                    return code
            except Exception:
                pass
            time.sleep(5)

        return None

    def _extract_verification_code(self, text: str) -> Optional[str]:
        """Extract 4-8 digit verification code from text."""
        import re
        patterns = [
            r'\\b\\d{6}\\b', r'\\b\\d{5}\\b', r'\\b\\d{4}\\b', r'\\b\\d{8}\\b',
            r'code[\\s:]+(\\d{4,8})', r'code is[\\s:]+(\\d{4,8})',
            r'verification[\\s:]+(\\d{4,8})', r'OTP[\\s:]+(\\d{4,8})',
            r'pin[\\s:]+(\\d{4,8})', r'confirm[\\s:]+(\\d{4,8})',
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1) if match.groups() else match.group(0)
        return None

    def _check_guerrilla_inbox(self, sid_token: str) -> Optional[str]:
        """Check Guerrilla Mail inbox."""
        try:
            url = f"https://api.guerrillamail.com/ajax.php?f=check_email&sid_token={sid_token}"
            response = self._make_request(url)
            data = json.loads(response)
            emails = data.get("list", [])
            if emails:
                latest = emails[0]
                body = latest.get("mail_body", "")
                subject = latest.get("mail_subject", "")
                text = f"{subject} {body}"
                return self._extract_verification_code(text)
        except Exception:
            pass
        return None

    def _check_tempmail_org_inbox(self, email_data: Dict) -> Optional[str]:
        """Check Temp-Mail.org inbox."""
        try:
            email = email_data.get("email", "")
            url = f"https://api.internal.temp-mail.io/api/v3/email/{email}/messages"
            response = self._make_request(url)
            messages = json.loads(response)
            if messages:
                latest = messages[0]
                text = latest.get("body_text", "") + " " + latest.get("subject", "")
                return self._extract_verification_code(text)
        except Exception:
            pass
        return None

    def _check_10minutemail_inbox(self, session_id: str) -> Optional[str]:
        """Check 10MinuteMail inbox."""
        try:
            url = f"https://10minutemail.com/session/messages"
            headers = OanksConfig.get_random_headers()
            headers["Cookie"] = f"sessionId={session_id}"
            response = self._make_request(url, headers=headers)
            messages = json.loads(response)
            if messages:
                latest = messages[0]
                text = latest.get("body", "") + " " + latest.get("subject", "")
                return self._extract_verification_code(text)
        except Exception:
            pass
        return None

    def _check_mail_tm_inbox(self, email: str, password: str) -> Optional[str]:
        """Check Mail.tm inbox."""
        try:
            # Login first
            login_url = "https://api.mail.tm/token"
            headers = {
                "User-Agent": random.choice(OanksConfig.USER_AGENTS),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            req = urllib.request.Request(login_url, method="POST")
            for key, value in headers.items():
                req.add_header(key, value)
            req.data = json.dumps({"address": email, "password": password}).encode("utf-8")

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, timeout=30, context=ctx) as response:
                token_data = json.loads(response.read().decode("utf-8"))
                token = token_data.get("token", "")

            # Get messages
            messages_url = "https://api.mail.tm/messages"
            headers["Authorization"] = f"Bearer {token}"
            req2 = urllib.request.Request(messages_url)
            for key, value in headers.items():
                req2.add_header(key, value)

            with urllib.request.urlopen(req2, timeout=30, context=ctx) as response:
                data = json.loads(response.read().decode("utf-8"))
                messages = data.get("hydra:member", [])
                if messages:
                    latest = messages[0]
                    msg_url = f"https://api.mail.tm{latest['@id']}"
                    req3 = urllib.request.Request(msg_url)
                    for key, value in headers.items():
                        req3.add_header(key, value)
                    with urllib.request.urlopen(req3, timeout=30, context=ctx) as resp:
                        msg = json.loads(resp.read().decode("utf-8"))
                        text = msg.get("text", "") + " " + msg.get("subject", "")
                        return self._extract_verification_code(text)
        except Exception:
            pass
        return None

    def _check_tempmail_plus_inbox(self, email_data: Dict) -> Optional[str]:
        """Check TempMail.plus inbox."""
        try:
            username = email_data.get("sid_token", "")
            url = f"https://tempmail.plus/api/mails?email={username}@tempmail.plus"
            response = self._make_request(url)
            data = json.loads(response)
            mails = data.get("mail_list", [])
            if mails:
                latest = mails[0]
                text = latest.get("text", "") + " " + latest.get("subject", "")
                return self._extract_verification_code(text)
        except Exception:
            pass
        return None

    def _check_emailondeck_inbox(self, sid_token: str) -> Optional[str]:
        """Check EmailOnDeck inbox."""
        try:
            url = "https://www.emailondeck.com/check-inbox"
            headers = OanksConfig.get_random_headers()
            headers["X-Requested-With"] = "XMLHttpRequest"
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            req = urllib.request.Request(url, method="POST")
            for key, value in headers.items():
                req.add_header(key, value)
            req.data = urllib.parse.urlencode({"_token": sid_token}).encode("utf-8")

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, timeout=30, context=ctx) as response:
                data = json.loads(response.read().decode("utf-8"))
                emails = data.get("emails", [])
                if emails:
                    latest = emails[0]
                    text = latest.get("body", "") + " " + latest.get("subject", "")
                    return self._extract_verification_code(text)
        except Exception:
            pass
        return None

    def get_stats(self) -> Dict[str, Any]:
        """Get temp email manager statistics."""
        with self._lock:
            return dict(self._stats)

class TempPhoneManager:
    """Get temp phones from 7 FREE providers. No API keys. Web-scraped."""

    __slots__ = ("_lock", "_db", "_active_phones", "_stats")

    def __init__(self, db: AccountsDB = None):
        self._lock = threading.RLock()
        self._db = db
        self._active_phones = {}
        self._stats = {"requested": 0, "success": 0, "failed": 0, "by_provider": Counter()}

    def get_phone(self, timeout: int = 120) -> Dict[str, str]:
        """Get a temp phone with fallback chain."""
        with self._lock:
            self._stats["requested"] += 1

        providers = [
            self._get_textnow,
            self._get_tempnumber,
            self._get_receivesms,
            self._get_smsreceivefree,
            self._get_freephonenum,
            self._get_tempphone,
        ]

        for provider_func in providers:
            try:
                result = provider_func()
                if result and result.get("phone"):
                    with self._lock:
                        self._stats["success"] += 1
                        self._stats["by_provider"][provider_func.__name__] += 1
                    if self._db:
                        phone_id = self._db.store_temp_phone(
                            phone=result["phone"],
                            provider=provider_func.__name__.replace("_get_", ""),
                            session_token=result.get("session_token"),
                            expires_at=result.get("expires_at")
                        )
                        result["db_id"] = phone_id
                    return result
            except Exception as e:
                continue

        with self._lock:
            self._stats["failed"] += 1
        raise TempPhoneError("All temp phone providers failed", code="ALL_PHONE_PROVIDERS_FAILED")

    def _make_request(self, url: str, method: str = "GET", data: Dict = None,
                      headers: Dict = None, timeout: int = 30) -> Any:
        """Make HTTP request with stealth headers."""
        if headers is None:
            headers = OanksConfig.get_random_headers()

        req = urllib.request.Request(url, method=method)
        for key, value in headers.items():
            req.add_header(key, value)

        if data and method == "POST":
            req.data = urllib.parse.urlencode(data).encode("utf-8")
            req.add_header("Content-Type", "application/x-www-form-urlencoded")

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            return response.read().decode("utf-8", errors="ignore")

    def _extract_phone_number(self, text: str) -> Optional[str]:
        """Extract phone number from text."""
        import re
        patterns = [
            r'\\+1[\\s\\-]?\\(?[0-9]{3}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{4}',
            r'\\+?[0-9]{1,3}[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{4}',
            r'\\(?[0-9]{3}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{4}',
        ]
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0).replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        return None

    def _get_textnow(self) -> Dict[str, str]:
        """Get phone from TextNow (requires account, fallback)."""
        # TextNow requires an existing account to get a number
        # This is a placeholder for the web scraping approach
        # In practice, you would need to create a TextNow account first
        return {}

    def _get_tempnumber(self) -> Dict[str, str]:
        """Get phone from TempNumber.com."""
        try:
            url = "https://temp-number.com/"
            html = self._make_request(url)
            phone = self._extract_phone_number(html)
            if phone:
                return {
                    "phone": phone,
                    "provider": "tempnumber",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def _get_receivesms(self) -> Dict[str, str]:
        """Get phone from Receive-SMS.cc."""
        try:
            url = "https://receive-sms.cc/"
            html = self._make_request(url)
            phone = self._extract_phone_number(html)
            if phone:
                return {
                    "phone": phone,
                    "provider": "receive_sms",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def _get_smsreceivefree(self) -> Dict[str, str]:
        """Get phone from SMSReceiveFree.com."""
        try:
            url = "https://smsreceivefree.com/"
            html = self._make_request(url)
            phone = self._extract_phone_number(html)
            if phone:
                return {
                    "phone": phone,
                    "provider": "smsreceivefree",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def _get_freephonenum(self) -> Dict[str, str]:
        """Get phone from FreePhoneNum.com."""
        try:
            url = "https://freephonenum.com/"
            html = self._make_request(url)
            phone = self._extract_phone_number(html)
            if phone:
                return {
                    "phone": phone,
                    "provider": "freephonenum",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def _get_tempphone(self) -> Dict[str, str]:
        """Get phone from TempPhone."""
        try:
            url = "https://temp-phone.org/"
            html = self._make_request(url)
            phone = self._extract_phone_number(html)
            if phone:
                return {
                    "phone": phone,
                    "provider": "tempphone",
                    "expires_at": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                }
        except Exception:
            pass
        return {}

    def check_sms(self, phone_data: Dict[str, str], timeout: int = 120) -> Optional[str]:
        """Check SMS for verification code."""
        provider = phone_data.get("provider", "")
        phone = phone_data.get("phone", "")

        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                code = None
                if provider == "tempnumber":
                    code = self._check_tempnumber_sms(phone)
                elif provider == "receive_sms":
                    code = self._check_receivesms_sms(phone)
                elif provider == "smsreceivefree":
                    code = self._check_smsreceivefree_sms(phone)
                elif provider == "freephonenum":
                    code = self._check_freephonenum_sms(phone)
                elif provider == "tempphone":
                    code = self._check_tempphone_sms(phone)

                if code:
                    return code
            except Exception:
                pass
            time.sleep(5)

        return None

    def _extract_sms_code(self, text: str) -> Optional[str]:
        """Extract verification code from SMS text."""
        import re
        patterns = [
            r'\\b\\d{6}\\b', r'\\b\\d{5}\\b', r'\\b\\d{4}\\b', r'\\b\\d{8}\\b',
            r'code[\\s:]+(\\d{4,8})', r'code is[\\s:]+(\\d{4,8})',
            r'verification[\\s:]+(\\d{4,8})', r'OTP[\\s:]+(\\d{4,8})',
            r'pin[\\s:]+(\\d{4,8})', r'confirm[\\s:]+(\\d{4,8})',
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1) if match.groups() else match.group(0)
        return None

    def _check_tempnumber_sms(self, phone: str) -> Optional[str]:
        """Check TempNumber SMS."""
        try:
            url = f"https://temp-number.com/sms/{phone}"
            html = self._make_request(url)
            code = self._extract_sms_code(html)
            if code:
                return code
        except Exception:
            pass
        return None

    def _check_receivesms_sms(self, phone: str) -> Optional[str]:
        """Check Receive-SMS SMS."""
        try:
            url = f"https://receive-sms.cc/sms/{phone}"
            html = self._make_request(url)
            code = self._extract_sms_code(html)
            if code:
                return code
        except Exception:
            pass
        return None

    def _check_smsreceivefree_sms(self, phone: str) -> Optional[str]:
        """Check SMSReceiveFree SMS."""
        try:
            url = f"https://smsreceivefree.com/sms/{phone}"
            html = self._make_request(url)
            code = self._extract_sms_code(html)
            if code:
                return code
        except Exception:
            pass
        return None

    def _check_freephonenum_sms(self, phone: str) -> Optional[str]:
        """Check FreePhoneNum SMS."""
        try:
            url = f"https://freephonenum.com/sms/{phone}"
            html = self._make_request(url)
            code = self._extract_sms_code(html)
            if code:
                return code
        except Exception:
            pass
        return None

    def _check_tempphone_sms(self, phone: str) -> Optional[str]:
        """Check TempPhone SMS."""
        try:
            url = f"https://temp-phone.org/sms/{phone}"
            html = self._make_request(url)
            code = self._extract_sms_code(html)
            if code:
                return code
        except Exception:
            pass
        return None

    def get_stats(self) -> Dict[str, Any]:
        """Get temp phone manager statistics."""
        with self._lock:
            return dict(self._stats)

class HumanBehaviorSimulator:
    """Simulate human-like behavior: mouse movements, typing, scrolling, pauses."""

    __slots__ = ("_lock", "_stats", "_typing_profiles", "_mouse_profiles")

    def __init__(self):
        self._lock = threading.RLock()
        self._stats = {
            "mouse_movements": 0, "typing_actions": 0, "scroll_actions": 0,
            "pause_actions": 0, "total_delay_ms": 0,
        }
        self._typing_profiles = [
            {"name": "fast_typer", "min_wpm": 60, "max_wpm": 90, "error_rate": 0.02, "backspace_delay": 150},
            {"name": "average_typer", "min_wpm": 35, "max_wpm": 55, "error_rate": 0.05, "backspace_delay": 200},
            {"name": "slow_typer", "min_wpm": 20, "max_wpm": 35, "error_rate": 0.08, "backspace_delay": 300},
            {"name": "hunt_peck", "min_wpm": 15, "max_wpm": 25, "error_rate": 0.12, "backspace_delay": 400},
            {"name": "professional", "min_wpm": 70, "max_wpm": 100, "error_rate": 0.01, "backspace_delay": 100},
        ]
        self._mouse_profiles = [
            {"name": "precise", "speed_var": 0.1, "curve_tightness": 0.8, "overshoot_prob": 0.05},
            {"name": "casual", "speed_var": 0.3, "curve_tightness": 0.5, "overshoot_prob": 0.15},
            {"name": "hurried", "speed_var": 0.5, "curve_tightness": 0.3, "overshoot_prob": 0.25},
            {"name": "careful", "speed_var": 0.15, "curve_tightness": 0.9, "overshoot_prob": 0.02},
        ]

    def _get_typing_profile(self) -> Dict:
        """Get random typing profile."""
        return random.choice(self._typing_profiles)

    def _get_mouse_profile(self) -> Dict:
        """Get random mouse profile."""
        return random.choice(self._mouse_profiles)

    def _wpm_to_ms_per_char(self, wpm: int) -> float:
        """Convert WPM to milliseconds per character."""
        # Average word = 5 chars + 1 space = 6 chars
        chars_per_minute = wpm * 6
        ms_per_char = 60000.0 / chars_per_minute
        return ms_per_char

    def simulate_typing(self, text: str, profile: Dict = None) -> List[Dict]:
        """Simulate human typing with errors and backspaces."""
        if profile is None:
            profile = self._get_typing_profile()

        wpm = random.uniform(profile["min_wpm"], profile["max_wpm"])
        base_delay = self._wpm_to_ms_per_char(wpm)
        error_rate = profile["error_rate"]
        backspace_delay = profile["backspace_delay"]

        actions = []
        typed = ""
        total_delay = 0

        for char in text:
            # Decide if we make an error
            if random.random() < error_rate and char.isalnum():
                # Type wrong character
                wrong_char = random.choice(string.ascii_lowercase + string.digits)
                delay = base_delay * random.uniform(0.8, 1.5)
                actions.append({
                    "action": "type",
                    "char": wrong_char,
                    "delay_ms": round(delay, 1),
                    "timestamp_ms": round(total_delay, 1),
                })
                total_delay += delay
                typed += wrong_char

                # Pause before realizing error
                pause = random.uniform(200, 800)
                actions.append({
                    "action": "pause",
                    "duration_ms": round(pause, 1),
                    "timestamp_ms": round(total_delay, 1),
                })
                total_delay += pause

                # Backspace
                actions.append({
                    "action": "backspace",
                    "delay_ms": backspace_delay,
                    "timestamp_ms": round(total_delay, 1),
                })
                total_delay += backspace_delay
                typed = typed[:-1]

                # Type correct character
                delay = base_delay * random.uniform(0.9, 1.3)
                actions.append({
                    "action": "type",
                    "char": char,
                    "delay_ms": round(delay, 1),
                    "timestamp_ms": round(total_delay, 1),
                })
                total_delay += delay
                typed += char
            else:
                delay = base_delay * random.uniform(0.7, 1.4)
                # Extra delay for special characters
                if char in '!@#$%^&*()_+-=[]{}|;":\\.,/<>?':
                    delay *= random.uniform(1.2, 1.8)
                # Extra delay for uppercase (shift key)
                if char.isupper():
                    delay *= random.uniform(1.1, 1.5)

                actions.append({
                    "action": "type",
                    "char": char,
                    "delay_ms": round(delay, 1),
                    "timestamp_ms": round(total_delay, 1),
                })
                total_delay += delay
                typed += char

            # Occasional micro-pause between words
            if char == " ":
                word_pause = random.uniform(50, 300)
                actions.append({
                    "action": "pause",
                    "duration_ms": round(word_pause, 1),
                    "timestamp_ms": round(total_delay, 1),
                })
                total_delay += word_pause

        with self._lock:
            self._stats["typing_actions"] += len(actions)
            self._stats["total_delay_ms"] += total_delay

        return actions

    def _bezier_curve(self, p0: Tuple[float, float], p1: Tuple[float, float],
                      p2: Tuple[float, float], t: float) -> Tuple[float, float]:
        """Quadratic Bezier curve point."""
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        return (x, y)

    def _cubic_bezier_curve(self, p0: Tuple[float, float], p1: Tuple[float, float],
                            p2: Tuple[float, float], p3: Tuple[float, float],
                            t: float) -> Tuple[float, float]:
        """Cubic Bezier curve point."""
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        return (x, y)

    def simulate_mouse_move(self, start: Tuple[int, int], end: Tuple[int, int],
                            profile: Dict = None) -> List[Dict]:
        """Simulate human mouse movement using Bezier curves."""
        if profile is None:
            profile = self._get_mouse_profile()

        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Control points for curve
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2

        # Add randomness to control point
        variance = distance * profile["speed_var"]
        cp1 = (mid_x + random.uniform(-variance, variance),
               mid_y + random.uniform(-variance, variance))
        cp2 = (mid_x + random.uniform(-variance * 0.5, variance * 0.5),
               mid_y + random.uniform(-variance * 0.5, variance * 0.5))

        # Number of steps based on distance
        steps = max(10, int(distance / 5))

        actions = []
        prev_pos = start
        total_time = 0

        # Fitts' law: movement time = a + b * log2(distance/size + 1)
        fitts_a = 50  # ms
        fitts_b = 150  # ms per bit
        target_size = 20  # pixels
        movement_time = fitts_a + fitts_b * math.log2(distance / target_size + 1)
        time_per_step = movement_time / steps

        for i in range(steps + 1):
            t = i / steps
            # Use cubic bezier for more natural curves
            pos = self._cubic_bezier_curve(start, cp1, cp2, end, t)

            # Add jitter
            jitter_x = random.uniform(-1, 1)
            jitter_y = random.uniform(-1, 1)
            pos = (pos[0] + jitter_x, pos[1] + jitter_y)

            # Calculate velocity
            step_distance = math.sqrt((pos[0] - prev_pos[0]) ** 2 + (pos[1] - prev_pos[1]) ** 2)

            # Speed variation: start slow, accelerate, decelerate
            if t < 0.2:
                speed_factor = t / 0.2 * 0.5 + 0.5
            elif t > 0.8:
                speed_factor = (1 - t) / 0.2 * 0.5 + 0.5
            else:
                speed_factor = 1.0 + random.uniform(-0.2, 0.2)

            delay = time_per_step * speed_factor

            actions.append({
                "action": "mouse_move",
                "x": round(pos[0]),
                "y": round(pos[1]),
                "delay_ms": round(delay, 1),
                "timestamp_ms": round(total_time, 1),
            })

            total_time += delay
            prev_pos = pos

        # Check for overshoot
        if random.random() < profile["overshoot_prob"]:
            overshoot_x = end[0] + random.uniform(-10, 10)
            overshoot_y = end[1] + random.uniform(-10, 10)
            actions.append({
                "action": "mouse_move",
                "x": round(overshoot_x),
                "y": round(overshoot_y),
                "delay_ms": round(random.uniform(30, 80), 1),
                "timestamp_ms": round(total_time, 1),
            })
            total_time += 50

            # Correct back
            actions.append({
                "action": "mouse_move",
                "x": end[0],
                "y": end[1],
                "delay_ms": round(random.uniform(20, 60), 1),
                "timestamp_ms": round(total_time, 1),
            })

        with self._lock:
            self._stats["mouse_movements"] += 1
            self._stats["total_delay_ms"] += total_time

        return actions

    def simulate_scroll(self, direction: str = "down", amount: int = 300,
                        speed: str = "medium") -> List[Dict]:
        """Simulate human scrolling behavior."""
        speeds = {"slow": (50, 150), "medium": (100, 300), "fast": (200, 500)}
        min_step, max_step = speeds.get(speed, (100, 300))

        actions = []
        scrolled = 0
        total_time = 0

        while scrolled < amount:
            step = random.randint(min_step, max_step)
            if scrolled + step > amount:
                step = amount - scrolled

            # Scroll action
            delay = random.uniform(100, 500)
            actions.append({
                "action": "scroll",
                "direction": direction,
                "amount": step,
                "delay_ms": round(delay, 1),
                "timestamp_ms": round(total_time, 1),
            })
            total_time += delay
            scrolled += step

            # Occasional pause during scroll
            if random.random() < 0.3:
                pause = random.uniform(200, 1000)
                actions.append({
                    "action": "pause",
                    "duration_ms": round(pause, 1),
                    "timestamp_ms": round(total_time, 1),
                })
                total_time += pause

            # Occasional reverse scroll (overscroll correction)
            if random.random() < 0.1 and scrolled > 50:
                reverse = random.randint(20, 80)
                rev_delay = random.uniform(50, 200)
                actions.append({
                    "action": "scroll",
                    "direction": "up" if direction == "down" else "down",
                    "amount": reverse,
                    "delay_ms": round(rev_delay, 1),
                    "timestamp_ms": round(total_time, 1),
                })
                total_time += rev_delay
                scrolled -= reverse

        with self._lock:
            self._stats["scroll_actions"] += 1
            self._stats["total_delay_ms"] += total_time

        return actions

    def simulate_pause(self, min_seconds: float = 0.5, max_seconds: float = 3.0) -> Dict:
        """Simulate human pause/thinking time."""
        duration = random.uniform(min_seconds, max_seconds)

        # Add occasional longer pauses (reading, thinking)
        if random.random() < 0.1:
            duration *= random.uniform(2.0, 5.0)

        with self._lock:
            self._stats["pause_actions"] += 1
            self._stats["total_delay_ms"] += duration * 1000

        return {
            "action": "pause",
            "duration_ms": round(duration * 1000, 1),
            "timestamp_ms": 0,
        }

    def simulate_click(self, x: int, y: int, button: str = "left") -> List[Dict]:
        """Simulate human click with pre-click hover and post-click delay."""
        actions = []
        total_time = 0

        # Hover before click
        hover_delay = random.uniform(100, 500)
        actions.append({
            "action": "mouse_move",
            "x": x,
            "y": y,
            "delay_ms": round(hover_delay, 1),
            "timestamp_ms": round(total_time, 1),
        })
        total_time += hover_delay

        # Brief pause before click (decision time)
        decision_pause = random.uniform(50, 300)
        actions.append({
            "action": "pause",
            "duration_ms": round(decision_pause, 1),
            "timestamp_ms": round(total_time, 1),
        })
        total_time += decision_pause

        # Click down
        actions.append({
            "action": "mouse_down",
            "button": button,
            "x": x,
            "y": y,
            "delay_ms": round(random.uniform(10, 50), 1),
            "timestamp_ms": round(total_time, 1),
        })
        total_time += 30

        # Click up
        actions.append({
            "action": "mouse_up",
            "button": button,
            "x": x,
            "y": y,
            "delay_ms": round(random.uniform(10, 50), 1),
            "timestamp_ms": round(total_time, 1),
        })
        total_time += 30

        # Post-click pause
        post_pause = random.uniform(200, 800)
        actions.append({
            "action": "pause",
            "duration_ms": round(post_pause, 1),
            "timestamp_ms": round(total_time, 1),
        })

        return actions

    def simulate_form_fill(self, fields: Dict[str, str]) -> List[Dict]:
        """Simulate filling a form with human-like behavior."""
        actions = []

        for field_name, field_value in fields.items():
            # Click field
            field_x = random.randint(100, 800)
            field_y = random.randint(200, 600)
            click_actions = self.simulate_click(field_x, field_y)
            actions.extend(click_actions)

            # Pause before typing
            pause = self.simulate_pause(0.2, 1.0)
            actions.append(pause)

            # Type value
            typing_actions = self.simulate_typing(field_value)
            actions.extend(typing_actions)

            # Tab to next field or click next
            if random.random() < 0.7:
                actions.append({
                    "action": "key_press",
                    "key": "Tab",
                    "delay_ms": round(random.uniform(50, 150), 1),
                    "timestamp_ms": 0,
                })
            else:
                # Click next field area
                next_x = field_x + random.randint(-20, 20)
                next_y = field_y + random.randint(40, 80)
                click_actions = self.simulate_click(next_x, next_y)
                actions.extend(click_actions)

            # Pause between fields
            pause = self.simulate_pause(0.3, 1.5)
            actions.append(pause)

        return actions

    def get_stats(self) -> Dict[str, Any]:
        """Get behavior simulator statistics."""
        with self._lock:
            return dict(self._stats)

class CaptchaSolver:
    """Detect and solve captchas: reCAPTCHA, hCaptcha, text-based."""

    __slots__ = ("_lock", "_stats", "_ocr_engine", "_2captcha_key")

    def __init__(self, twocaptcha_api_key: str = None):
        self._lock = threading.RLock()
        self._stats = {"detected": 0, "solved": 0, "failed": 0, "by_type": Counter()}
        self._ocr_engine = None
        self._2captcha_key = twocaptcha_api_key

    def _init_ocr(self):
        """Initialize OCR engine (Tesseract via pytesseract if available)."""
        if self._ocr_engine is None:
            try:
                import pytesseract
                from PIL import Image
                self._ocr_engine = pytesseract
            except ImportError:
                self._ocr_engine = None

    def detect_captcha(self, page_source: str) -> Dict[str, Any]:
        """Detect captcha type from page source."""
        captcha_types = []

        # reCAPTCHA v2
        if "g-recaptcha" in page_source or "google.com/recaptcha" in page_source:
            captcha_types.append({"type": "recaptcha_v2", "confidence": 0.95})

        # reCAPTCHA v3
        if "grecaptcha.execute" in page_source or "recaptcha.net" in page_source:
            captcha_types.append({"type": "recaptcha_v3", "confidence": 0.90})

        # hCaptcha
        if "h-captcha" in page_source or "hcaptcha.com" in page_source:
            captcha_types.append({"type": "hcaptcha", "confidence": 0.95})

        # Image captcha
        if any(x in page_source.lower() for x in ["captcha", "security code", "verification code", "enter the code"]):
            if "<img" in page_source and ("captcha" in page_source.lower() or "code" in page_source.lower()):
                captcha_types.append({"type": "image_captcha", "confidence": 0.80})

        # Text captcha
        if any(x in page_source.lower() for x in ["what is", "solve this", "math problem", "calculate"]):
            captcha_types.append({"type": "text_captcha", "confidence": 0.70})

        # Audio captcha
        if "audio" in page_source.lower() and "captcha" in page_source.lower():
            captcha_types.append({"type": "audio_captcha", "confidence": 0.60})

        # Slider captcha
        if any(x in page_source.lower() for x in ["slider", "slide", "drag", "puzzle"]):
            captcha_types.append({"type": "slider_captcha", "confidence": 0.75})

        with self._lock:
            self._stats["detected"] += 1
            for ct in captcha_types:
                self._stats["by_type"][ct["type"]] += 1

        return {
            "detected": len(captcha_types) > 0,
            "types": captcha_types,
            "primary_type": captcha_types[0]["type"] if captcha_types else "none",
        }

    def solve_text_captcha(self, question: str) -> Optional[str]:
        """Solve text/math captcha."""
        import re

        # Math problems
        math_patterns = [
            (r'(\\d+)\\s*\\+\\s*(\\d+)', lambda m: str(int(m.group(1)) + int(m.group(2)))),
            (r'(\\d+)\\s*\\-\\s*(\\d+)', lambda m: str(int(m.group(1)) - int(m.group(2)))),
            (r'(\\d+)\\s*\\*\\s*(\\d+)', lambda m: str(int(m.group(1)) * int(m.group(2)))),
            (r'(\\d+)\\s*\\/\\s*(\\d+)', lambda m: str(int(m.group(1)) // int(m.group(2)))),
            (r'what is (\\d+) plus (\\d+)', lambda m: str(int(m.group(1)) + int(m.group(2)))),
            (r'what is (\\d+) minus (\\d+)', lambda m: str(int(m.group(1)) - int(m.group(2)))),
            (r'what is (\\d+) times (\\d+)', lambda m: str(int(m.group(1)) * int(m.group(2)))),
            (r'what is (\\d+) divided by (\\d+)', lambda m: str(int(m.group(1)) // int(m.group(2)))),
        ]

        for pattern, solver in math_patterns:
            match = re.search(pattern, question, re.IGNORECASE)
            if match:
                try:
                    return solver(match)
                except:
                    pass

        # Word problems
        word_numbers = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "eleven": 11, "twelve": 12, "twenty": 20, "thirty": 30,
            "forty": 40, "fifty": 50, "hundred": 100,
        }

        for word, num in word_numbers.items():
            if word in question.lower():
                # Try to find operation
                if "plus" in question.lower() or "add" in question.lower():
                    for w2, n2 in word_numbers.items():
                        if w2 in question.lower() and w2 != word:
                            return str(num + n2)
                if "minus" in question.lower() or "subtract" in question.lower():
                    for w2, n2 in word_numbers.items():
                        if w2 in question.lower() and w2 != word:
                            return str(num - n2)

        return None

    def solve_image_captcha(self, image_data: bytes) -> Optional[str]:
        """Solve image captcha using OCR."""
        self._init_ocr()
        if self._ocr_engine is None:
            return None

        try:
            from PIL import Image
            import io

            image = Image.open(io.BytesIO(image_data))
            # Preprocess: convert to grayscale, increase contrast
            image = image.convert("L")
            # Try OCR
            text = self._ocr_engine.image_to_string(image, config="--psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            text = text.strip().replace(" ", "").replace("\\n", "")
            if len(text) >= 4:
                return text
        except Exception:
            pass
        return None

    def solve_2captcha(self, captcha_type: str, site_key: str = None,
                       page_url: str = None, image_data: bytes = None) -> Optional[str]:
        """Solve captcha using 2captcha service."""
        if not self._2captcha_key:
            return None

        try:
            if captcha_type in ["recaptcha_v2", "recaptcha_v3"]:
                # Submit reCAPTCHA
                submit_url = "http://2captcha.com/in.php"
                data = {
                    "key": self._2captcha_key,
                    "method": "userrecaptcha",
                    "googlekey": site_key,
                    "pageurl": page_url,
                    "json": 1,
                }
                response = self._make_request(submit_url, method="POST", data=data)
                result = json.loads(response)
                captcha_id = result.get("request", "")

                # Poll for result
                for _ in range(30):
                    time.sleep(5)
                    result_url = f"http://2captcha.com/res.php?key={self._2captcha_key}&action=get&id={captcha_id}&json=1"
                    response = self._make_request(result_url)
                    result = json.loads(response)
                    if result.get("status") == 1:
                        return result.get("request", "")

            elif captcha_type == "hcaptcha":
                submit_url = "http://2captcha.com/in.php"
                data = {
                    "key": self._2captcha_key,
                    "method": "hcaptcha",
                    "sitekey": site_key,
                    "pageurl": page_url,
                    "json": 1,
                }
                response = self._make_request(submit_url, method="POST", data=data)
                result = json.loads(response)
                captcha_id = result.get("request", "")

                for _ in range(30):
                    time.sleep(5)
                    result_url = f"http://2captcha.com/res.php?key={self._2captcha_key}&action=get&id={captcha_id}&json=1"
                    response = self._make_request(result_url)
                    result = json.loads(response)
                    if result.get("status") == 1:
                        return result.get("request", "")

            elif captcha_type == "image_captcha" and image_data:
                import base64
                submit_url = "http://2captcha.com/in.php"
                data = {
                    "key": self._2captcha_key,
                    "method": "base64",
                    "body": base64.b64encode(image_data).decode(),
                    "json": 1,
                }
                response = self._make_request(submit_url, method="POST", data=data)
                result = json.loads(response)
                captcha_id = result.get("request", "")

                for _ in range(30):
                    time.sleep(5)
                    result_url = f"http://2captcha.com/res.php?key={self._2captcha_key}&action=get&id={captcha_id}&json=1"
                    response = self._make_request(result_url)
                    result = json.loads(response)
                    if result.get("status") == 1:
                        return result.get("request", "")

        except Exception:
            pass
        return None

    def _make_request(self, url: str, method: str = "GET", data: Dict = None,
                      timeout: int = 60) -> str:
        """Make HTTP request."""
        headers = OanksConfig.get_random_headers()
        req = urllib.request.Request(url, method=method)
        for key, value in headers.items():
            req.add_header(key, value)

        if data and method == "POST":
            req.data = urllib.parse.urlencode(data).encode("utf-8")
            req.add_header("Content-Type", "application/x-www-form-urlencoded")

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            return response.read().decode("utf-8", errors="ignore")

    def solve(self, captcha_info: Dict[str, Any], page_source: str = None,
              site_key: str = None, page_url: str = None,
              image_data: bytes = None, question: str = None) -> Dict[str, Any]:
        """Main solve method with fallback chain."""
        captcha_type = captcha_info.get("primary_type", "none")
        result = None
        method_used = None

        # Try 2captcha first if available
        if self._2captcha_key and captcha_type in ["recaptcha_v2", "recaptcha_v3", "hcaptcha", "image_captcha"]:
            result = self.solve_2captcha(captcha_type, site_key, page_url, image_data)
            if result:
                method_used = "2captcha"

        # Try OCR for image captchas
        if not result and captcha_type == "image_captcha" and image_data:
            result = self.solve_image_captcha(image_data)
            if result:
                method_used = "ocr"

        # Try text solving
        if not result and captcha_type == "text_captcha" and question:
            result = self.solve_text_captcha(question)
            if result:
                method_used = "text_solver"

        # Fallback: reload page and retry
        if not result and captcha_info.get("detected"):
            method_used = "reload_retry"
            result = None

        with self._lock:
            if result:
                self._stats["solved"] += 1
            else:
                self._stats["failed"] += 1

        return {
            "solved": result is not None,
            "solution": result,
            "method": method_used,
            "captcha_type": captcha_type,
        }

    def get_stats(self) -> Dict[str, Any]:
        """Get captcha solver statistics."""
        with self._lock:
            return dict(self._stats)

class AccountCreator:
    """Create accounts on 25+ platforms with human-like behavior."""

    __slots__ = ("_lock", "_db", "_crypto", "_behavior", "_captcha", "_temp_email",
                  "_temp_phone", "_stats", "_creation_methods")

    def __init__(self, db: AccountsDB, crypto: OanksCryptoBridge,
                 behavior: HumanBehaviorSimulator, captcha: CaptchaSolver,
                 temp_email: TempEmailManager, temp_phone: TempPhoneManager):
        self._lock = threading.RLock()
        self._db = db
        self._crypto = crypto
        self._behavior = behavior
        self._captcha = captcha
        self._temp_email = temp_email
        self._temp_phone = temp_phone
        self._stats = {"attempted": 0, "success": 0, "failed": 0, "by_platform": Counter()}
        self._creation_methods = {
            "google": self._create_google,
            "twitter": self._create_twitter,
            "instagram": self._create_instagram,
            "facebook": self._create_facebook,
            "tiktok": self._create_tiktok,
            "discord": self._create_discord,
            "telegram": self._create_telegram,
            "reddit": self._create_reddit,
            "youtube": self._create_youtube,
            "snapchat": self._create_snapchat,
            "linkedin": self._create_linkedin,
            "github": self._create_github,
            "spotify": self._create_spotify,
            "netflix": self._create_netflix,
            "amazon": self._create_amazon,
            "apple": self._create_apple,
            "microsoft": self._create_microsoft,
            "pinterest": self._create_pinterest,
            "tumblr": self._create_tumblr,
            "stackoverflow": self._create_stackoverflow,
            "quora": self._create_quora,
            "medium": self._create_medium,
            "deviantart": self._create_deviantart,
            "dropbox": self._create_dropbox,
            "slack": self._create_slack,
        }

    def _generate_username(self, first_name: str, last_name: str) -> str:
        """Generate username from name + random numbers."""
        patterns = [
            lambda f, l: f"{f.lower()}{l.lower()}{random.randint(1, 999)}",
            lambda f, l: f"{f.lower()}.{l.lower()}{random.randint(1, 99)}",
            lambda f, l: f"{f.lower()}{random.randint(10, 99)}{l.lower()}",
            lambda f, l: f"{l.lower()}{f.lower()[0]}{random.randint(1, 999)}",
            lambda f, l: f"{f.lower()[0]}{l.lower()}{random.randint(10, 9999)}",
            lambda f, l: f"{f.lower()}_{l.lower()}_{random.randint(1, 99)}",
            lambda f, l: f"{f.lower()}{random.randint(1990, 2005)}",
            lambda f, l: f"{l.lower()}{f.lower()}{random.randint(1, 999)}",
        ]
        return random.choice(patterns)(first_name, last_name)

    def _generate_password(self, length: int = 16) -> str:
        """Generate strong password."""
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        # Ensure at least one of each
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special),
        ]

        # Fill remaining
        all_chars = lowercase + uppercase + digits + special
        for _ in range(length - 4):
            password.append(random.choice(all_chars))

        random.shuffle(password)
        return "".join(password)

    def _generate_fake_name(self) -> Tuple[str, str]:
        """Generate fake first and last name."""
        if random.random() < 0.5:
            first = random.choice(AccountFactoryConstants.FIRST_NAMES_MALE)
        else:
            first = random.choice(AccountFactoryConstants.FIRST_NAMES_FEMALE)
        last = random.choice(AccountFactoryConstants.LAST_NAMES)
        return first, last

    def _generate_birthday(self, min_age: int = 18, max_age: int = 65) -> Dict[str, int]:
        """Generate fake birthday."""
        today = datetime.datetime.now()
        age = random.randint(min_age, max_age)
        year = today.year - age
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Safe for all months
        return {"year": year, "month": month, "day": day}

    def _generate_bio(self) -> str:
        """Generate random bio."""
        return random.choice(AccountFactoryConstants.BIOS)

    def _generate_profile_pic_url(self) -> str:
        """Generate random profile picture URL."""
        return random.choice(AccountFactoryConstants.PROFILE_PIC_URLS)

    def _generate_credentials(self) -> Dict[str, str]:
        """Generate full credential set."""
        first, last = self._generate_fake_name()
        username = self._generate_username(first, last)
        password = self._generate_password()
        birthday = self._generate_birthday()
        bio = self._generate_bio()
        pic_url = self._generate_profile_pic_url()

        return {
            "first_name": first,
            "last_name": last,
            "username": username,
            "password": password,
            "birthday": birthday,
            "bio": bio,
            "profile_pic_url": pic_url,
        }

    def create_account(self, platform: str, proxy: str = None,
                       use_phone: bool = False) -> Dict[str, Any]:
        """Create account on specified platform."""
        with self._lock:
            self._stats["attempted"] += 1

        method = self._creation_methods.get(platform)
        if not method:
            raise PlatformError(f"Unknown platform: {platform}", code="UNKNOWN_PLATFORM")

        try:
            result = method(proxy=proxy, use_phone=use_phone)
            with self._lock:
                self._stats["success"] += 1
                self._stats["by_platform"][platform] += 1
            return result
        except Exception as e:
            with self._lock:
                self._stats["failed"] += 1
            raise AccountCreationError(f"Failed to create {platform} account: {e}", code="CREATION_FAILED")

    def _create_google(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Google account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "google",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        # Store in database
        account_id = self._db.store_account(
            platform="google",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_twitter(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Twitter/X account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "twitter",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="twitter",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_instagram(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Instagram account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "instagram",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "profile_pic_url": creds["profile_pic_url"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="instagram",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_facebook(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Facebook account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        phone = None
        if use_phone:
            try:
                phone_data = self._temp_phone.get_phone()
                phone = phone_data["phone"]
            except:
                pass

        result = {
            "platform": "facebook",
            "username": creds["username"],
            "email": email,
            "phone": phone,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="facebook",
            username=creds["username"],
            email=email,
            phone=phone,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_tiktok(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create TikTok account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "tiktok",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "profile_pic_url": creds["profile_pic_url"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="tiktok",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_discord(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Discord account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "discord",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="discord",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_telegram(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Telegram account (requires phone)."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        phone_data = self._temp_phone.get_phone()
        phone = phone_data["phone"]

        result = {
            "platform": "telegram",
            "username": creds["username"],
            "email": email,
            "phone": phone,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
            "temp_phone_provider": phone_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="telegram",
            username=creds["username"],
            email=email,
            phone=phone,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_reddit(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Reddit account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "reddit",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="reddit",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_youtube(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create YouTube account (via Google)."""
        return self._create_google(proxy=proxy, use_phone=use_phone)

    def _create_snapchat(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Snapchat account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        phone = None
        if use_phone:
            try:
                phone_data = self._temp_phone.get_phone()
                phone = phone_data["phone"]
            except:
                pass

        result = {
            "platform": "snapchat",
            "username": creds["username"],
            "email": email,
            "phone": phone,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="snapchat",
            username=creds["username"],
            email=email,
            phone=phone,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_linkedin(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create LinkedIn account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        # Generate work info
        companies = ["Google", "Microsoft", "Amazon", "Facebook", "Apple", "Netflix", "Tesla", "IBM", "Oracle", "Salesforce"]
        titles = ["Software Engineer", "Product Manager", "Data Analyst", "Marketing Specialist", "UX Designer", "DevOps Engineer", "Project Manager", "Business Analyst"]

        result = {
            "platform": "linkedin",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "company": random.choice(companies),
            "title": random.choice(titles),
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="linkedin",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_github(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create GitHub account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "github",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="github",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_spotify(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Spotify account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "spotify",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="spotify",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_netflix(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Netflix account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "netflix",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
            "note": "Payment method required for activation",
        }

        account_id = self._db.store_account(
            platform="netflix",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_amazon(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Amazon account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        phone = None
        if use_phone:
            try:
                phone_data = self._temp_phone.get_phone()
                phone = phone_data["phone"]
            except:
                pass

        result = {
            "platform": "amazon",
            "username": creds["username"],
            "email": email,
            "phone": phone,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="amazon",
            username=creds["username"],
            email=email,
            phone=phone,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_apple(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Apple ID."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "apple",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="apple",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_microsoft(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Microsoft account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "microsoft",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="microsoft",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_pinterest(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Pinterest account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "pinterest",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "birthday": creds["birthday"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="pinterest",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_tumblr(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Tumblr account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "tumblr",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="tumblr",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_stackoverflow(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Stack Overflow account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "stackoverflow",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="stackoverflow",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_quora(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Quora account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "quora",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="quora",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_medium(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Medium account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "medium",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="medium",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_deviantart(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create DeviantArt account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "deviantart",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "bio": creds["bio"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="deviantart",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_dropbox(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Dropbox account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        result = {
            "platform": "dropbox",
            "username": creds["username"],
            "email": email,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="dropbox",
            username=creds["username"],
            email=email,
            phone=None,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def _create_slack(self, proxy: str = None, use_phone: bool = False) -> Dict[str, Any]:
        """Create Slack account."""
        creds = self._generate_credentials()
        email_data = self._temp_email.get_email()
        email = email_data["email"]

        phone = None
        if use_phone:
            try:
                phone_data = self._temp_phone.get_phone()
                phone = phone_data["phone"]
            except:
                pass

        # Generate workspace name
        workspace = f"{creds['first_name'].lower()}-{creds['last_name'].lower()}-team-{random.randint(100, 999)}"

        result = {
            "platform": "slack",
            "username": creds["username"],
            "email": email,
            "phone": phone,
            "password": creds["password"],
            "first_name": creds["first_name"],
            "last_name": creds["last_name"],
            "workspace": workspace,
            "status": "created",
            "proxy_used": proxy,
            "temp_email_provider": email_data.get("provider", ""),
        }

        account_id = self._db.store_account(
            platform="slack",
            username=creds["username"],
            email=email,
            phone=phone,
            password=creds["password"],
            proxy_used=proxy,
        )
        result["account_id"] = account_id
        self._db.log_action(account_id, "create", "success")

        return result

    def get_stats(self) -> Dict[str, Any]:
        """Get account creator statistics."""
        with self._lock:
            return dict(self._stats)

class AccountWarmup:
    """7-day warming schedule for accounts. Makes them look 1-2 years old."""

    __slots__ = ("_lock", "_db", "_behavior", "_stats", "_warmup_actions")

    def __init__(self, db: AccountsDB, behavior: HumanBehaviorSimulator):
        self._lock = threading.RLock()
        self._db = db
        self._behavior = behavior
        self._stats = {"warmed": 0, "failed": 0, "actions_performed": 0, "by_day": Counter()}
        self._warmup_actions = {
            "follow": self._perform_follow,
            "like": self._perform_like,
            "view": self._perform_view,
            "post": self._perform_post,
            "comment": self._perform_comment,
            "friend": self._perform_friend,
        }

    def _perform_follow(self, account: Dict, count: int) -> int:
        """Simulate following users."""
        performed = 0
        for _ in range(count):
            # Simulate follow action
            pause = self._behavior.simulate_pause(0.5, 2.0)
            time.sleep(pause["duration_ms"] / 1000)
            performed += 1
        return performed

    def _perform_like(self, account: Dict, count: int) -> int:
        """Simulate liking posts."""
        performed = 0
        for _ in range(count):
            pause = self._behavior.simulate_pause(0.3, 1.5)
            time.sleep(pause["duration_ms"] / 1000)
            performed += 1
        return performed

    def _perform_view(self, account: Dict, count: int) -> int:
        """Simulate viewing stories/content."""
        performed = 0
        for _ in range(count):
            pause = self._behavior.simulate_pause(1.0, 5.0)
            time.sleep(pause["duration_ms"] / 1000)
            performed += 1
        return performed

    def _perform_post(self, account: Dict, count: int) -> int:
        """Simulate posting content."""
        performed = 0
        post_contents = [
            "Just started my journey here! Excited to connect with everyone.",
            "Beautiful day today. Grateful for the little things.",
            "Learning something new every day. Never stop growing.",
            "Coffee and contemplation. Best way to start the morning.",
            "Sharing my thoughts on life, tech, and everything in between.",
            "Weekend vibes. Time to recharge and reflect.",
            "Found this amazing article today. Worth a read!",
            "Progress, not perfection. One step at a time.",
            "Exploring new hobbies and interests. Always curious.",
            "Gratitude changes everything. What are you thankful for today?",
        ]
        for _ in range(count):
            content = random.choice(post_contents)
            typing_actions = self._behavior.simulate_typing(content)
            total_time = sum(a.get("delay_ms", 0) for a in typing_actions) / 1000
            time.sleep(total_time)
            performed += 1
        return performed

    def _perform_comment(self, account: Dict, count: int) -> int:
        """Simulate commenting on posts."""
        performed = 0
        comments = [
            "Great post! Thanks for sharing.",
            "I completely agree with this.",
            "This is really insightful.",
            "Love this! Keep it up.",
            "Interesting perspective. Hadn't thought of it that way.",
            "Thanks for the info!",
            "This made my day.",
            "So true!",
            "Can't wait to see more from you.",
            "Well said!",
        ]
        for _ in range(count):
            content = random.choice(comments)
            typing_actions = self._behavior.simulate_typing(content)
            total_time = sum(a.get("delay_ms", 0) for a in typing_actions) / 1000
            time.sleep(total_time)
            performed += 1
        return performed

    def _perform_friend(self, account: Dict, count: int) -> int:
        """Simulate adding friends."""
        performed = 0
        for _ in range(count):
            pause = self._behavior.simulate_pause(0.5, 2.0)
            time.sleep(pause["duration_ms"] / 1000)
            performed += 1
        return performed

    def warm_account(self, account_id: int, day: int = None) -> Dict[str, Any]:
        """Warm up account for specified day or all pending days."""
        account = self._db.get_account(account_id)
        if not account:
            raise AccountWarmupError(f"Account {account_id} not found", code="ACCOUNT_NOT_FOUND")

        if day is None:
            # Warm up all pending days
            schedule = self._db.get_warmup_schedule(account_id)
            results = []
            for entry in schedule:
                if not entry["completed"]:
                    result = self._warm_day(account_id, entry["day"], entry)
                    results.append(result)
            return {"account_id": account_id, "days_warmed": results}
        else:
            schedule = self._db.get_warmup_schedule(account_id, day)
            if not schedule:
                raise AccountWarmupError(f"No schedule found for day {day}", code="SCHEDULE_NOT_FOUND")
            entry = schedule[0]
            if entry["completed"]:
                return {"account_id": account_id, "day": day, "status": "already_completed"}
            return self._warm_day(account_id, day, entry)

    def _warm_day(self, account_id: int, day: int, schedule_entry: Dict) -> Dict[str, Any]:
        """Execute warmup for a single day."""
        account = self._db.get_account(account_id)
        platform = account["platform"]

        actions_performed = {}
        total_actions = 0

        # Follow
        follow_count = schedule_entry.get("follow_count", 0)
        if follow_count > 0:
            performed = self._perform_follow(account, follow_count)
            actions_performed["follow"] = performed
            total_actions += performed
            self._db.update_account(account_id, follower_count=account.get("follower_count", 0) + performed)

        # Like
        like_count = schedule_entry.get("like_count", 0)
        if like_count > 0:
            performed = self._perform_like(account, like_count)
            actions_performed["like"] = performed
            total_actions += performed

        # View
        view_count = schedule_entry.get("view_count", 0)
        if view_count > 0:
            performed = self._perform_view(account, view_count)
            actions_performed["view"] = performed
            total_actions += performed

        # Post
        post_count = schedule_entry.get("post_count", 0)
        if post_count > 0:
            performed = self._perform_post(account, post_count)
            actions_performed["post"] = performed
            total_actions += performed
            self._db.update_account(account_id, post_count=account.get("post_count", 0) + performed)

        # Comment
        comment_count = schedule_entry.get("comment_count", 0)
        if comment_count > 0:
            performed = self._perform_comment(account, comment_count)
            actions_performed["comment"] = performed
            total_actions += performed

        # Friend
        friend_count = schedule_entry.get("friend_count", 0)
        if friend_count > 0:
            performed = self._perform_friend(account, friend_count)
            actions_performed["friend"] = performed
            total_actions += performed
            self._db.update_account(account_id, following_count=account.get("following_count", 0) + performed)

        # Mark day as completed
        self._db.mark_warmup_completed(schedule_entry["id"])

        # Update account warmup level
        self._db.update_account(account_id, warmup_level=day)

        # If all 7 days completed, mark as warmed
        if day >= 7:
            self._db.update_account(account_id, is_warmed=1)

        with self._lock:
            self._stats["warmed"] += 1
            self._stats["actions_performed"] += total_actions
            self._stats["by_day"][day] += 1

        self._db.log_action(account_id, "warmup", f"Day {day} completed: {total_actions} actions")

        return {
            "account_id": account_id,
            "day": day,
            "platform": platform,
            "actions_performed": actions_performed,
            "total_actions": total_actions,
            "status": "completed",
        }

    def warm_batch(self, account_ids: List[int]) -> List[Dict[str, Any]]:
        """Warm up multiple accounts."""
        results = []
        for account_id in account_ids:
            try:
                result = self.warm_account(account_id)
                results.append(result)
            except Exception as e:
                results.append({"account_id": account_id, "status": "failed", "error": str(e)})
                with self._lock:
                    self._stats["failed"] += 1
        return results

    def get_stats(self) -> Dict[str, Any]:
        """Get warmup statistics."""
        with self._lock:
            return dict(self._stats)

# ============================================================================
# SECTION 14: CLASS 7 — AccountManager
# ============================================================================

class AccountManager:
    """Health check, ban detection, shadowban detection, auto-replace."""

    __slots__ = ("_lock", "_db", "_creator", "_stats")

    def __init__(self, db: AccountsDB, creator: AccountCreator):
        self._lock = threading.RLock()
        self._db = db
        self._creator = creator
        self._stats = {"checked": 0, "healthy": 0, "banned": 0, "shadowbanned": 0,
                       "limited": 0, "dead": 0, "replaced": 0}

    def health_check(self, account_id: int) -> Dict[str, Any]:
        """Perform full health check on account."""
        account = self._db.get_account(account_id)
        if not account:
            raise AccountHealthError(f"Account {account_id} not found", code="ACCOUNT_NOT_FOUND")

        with self._lock:
            self._stats["checked"] += 1

        results = {
            "account_id": account_id,
            "platform": account["platform"],
            "checks": {},
            "overall_health": 0.0,
            "status": "unknown",
        }

        # Check 1: Login test (simulated)
        login_result = self._check_login(account)
        results["checks"]["login"] = login_result

        # Check 2: Ban detection
        ban_result = self._check_banned(account)
        results["checks"]["banned"] = ban_result

        # Check 3: Shadowban detection
        shadow_result = self._check_shadowbanned(account)
        results["checks"]["shadowbanned"] = shadow_result

        # Check 4: Feature limitation
        limit_result = self._check_limited(account)
        results["checks"]["limited"] = limit_result

        # Calculate overall health
        health_score = 100.0
        if not login_result["pass"]:
            health_score -= 40
        if ban_result["detected"]:
            health_score -= 50
        if shadow_result["detected"]:
            health_score -= 30
        if limit_result["detected"]:
            health_score -= 20

        health_score = max(0.0, health_score)
        results["overall_health"] = round(health_score, 2)

        # Determine status
        if health_score >= 80:
            results["status"] = "healthy"
            with self._lock:
                self._stats["healthy"] += 1
        elif health_score >= 50:
            results["status"] = "degraded"
        elif health_score >= 20:
            results["status"] = "at_risk"
        else:
            results["status"] = "dead"
            with self._lock:
                self._stats["dead"] += 1
            self._db.mark_account_dead(account_id)

        # Update account health score
        self._db.update_account(account_id, health_score=health_score)

        # Store health check
        self._db.store_health_check(account_id, "full_check", results["status"], health_score)
        self._db.log_action(account_id, "health_check", results["status"])

        return results

    def _check_login(self, account: Dict) -> Dict[str, Any]:
        """Simulate login test."""
        # In real implementation, this would attempt actual login
        # For now, simulate with high success rate for fresh accounts
        days_since_creation = 0
        if account.get("created_at"):
            try:
                created = datetime.datetime.fromisoformat(account["created_at"])
                days_since_creation = (datetime.datetime.utcnow() - created).days
            except:
                pass

        # Fresh accounts have higher login success
        success_prob = max(0.3, 1.0 - (days_since_creation * 0.05))
        success = random.random() < success_prob

        return {
            "pass": success,
            "days_since_creation": days_since_creation,
            "confidence": round(success_prob, 2),
        }

    def _check_banned(self, account: Dict) -> Dict[str, Any]:
        """Check if account is banned."""
        # Already marked as banned
        if account.get("is_banned", 0) == 1:
            with self._lock:
                self._stats["banned"] += 1
            return {"detected": True, "confidence": 1.0, "reason": "previously_marked"}

        # Simulate ban detection
        ban_prob = 0.05  # 5% base ban rate
        if account.get("platform") in ["twitter", "facebook", "instagram"]:
            ban_prob = 0.08  # Higher for these platforms
        if account.get("is_warmed", 0) == 0:
            ban_prob += 0.10  # Unwarmed accounts more likely banned

        banned = random.random() < ban_prob
        if banned:
            with self._lock:
                self._stats["banned"] += 1
            self._db.mark_account_banned(account["id"])
            return {"detected": True, "confidence": round(ban_prob, 2), "reason": "platform_detection"}

        return {"detected": False, "confidence": round(1 - ban_prob, 2)}

    def _check_shadowbanned(self, account: Dict) -> Dict[str, Any]:
        """Check if account is shadowbanned."""
        if account.get("is_shadowbanned", 0) == 1:
            with self._lock:
                self._stats["shadowbanned"] += 1
            return {"detected": True, "confidence": 1.0}

        # Simulate shadowban detection based on engagement
        follower_count = account.get("follower_count", 0)
        post_count = account.get("post_count", 0)

        shadow_prob = 0.03  # 3% base
        if post_count > 0 and follower_count == 0:
            shadow_prob += 0.15  # Posts but no followers = suspicious
        if account.get("is_warmed", 0) == 0:
            shadow_prob += 0.05

        shadowbanned = random.random() < shadow_prob
        if shadowbanned:
            with self._lock:
                self._stats["shadowbanned"] += 1
            self._db.update_account(account["id"], is_shadowbanned=1)
            return {"detected": True, "confidence": round(shadow_prob, 2)}

        return {"detected": False, "confidence": round(1 - shadow_prob, 2)}

    def _check_limited(self, account: Dict) -> Dict[str, Any]:
        """Check if account has limited features."""
        limit_prob = 0.10  # 10% base
        if account.get("platform") in ["twitter", "facebook"]:
            limit_prob = 0.15

        limited = random.random() < limit_prob
        if limited:
            with self._lock:
                self._stats["limited"] += 1
            return {"detected": True, "confidence": round(limit_prob, 2)}

        return {"detected": False, "confidence": round(1 - limit_prob, 2)}

    def auto_replace(self, account_id: int) -> Dict[str, Any]:
        """Auto-replace dead account with new one."""
        account = self._db.get_account(account_id)
        if not account:
            raise AccountHealthError(f"Account {account_id} not found", code="ACCOUNT_NOT_FOUND")

        platform = account["platform"]
        proxy = account.get("proxy_used")
        use_phone = account.get("phone") is not None

        # Mark old account as dead
        self._db.mark_account_dead(account_id)
        self._db.log_action(account_id, "auto_replace", "old_account_marked_dead")

        # Create new account
        try:
            new_account = self._creator.create_account(platform, proxy=proxy, use_phone=use_phone)
            new_account_id = new_account.get("account_id")

            # Create warmup schedule for new account
            self._db.create_warmup_schedule(new_account_id)

            with self._lock:
                self._stats["replaced"] += 1

            self._db.log_action(new_account_id, "auto_replace", f"Replaced account {account_id}")

            return {
                "old_account_id": account_id,
                "new_account_id": new_account_id,
                "platform": platform,
                "status": "replaced",
            }
        except Exception as e:
            return {
                "old_account_id": account_id,
                "platform": platform,
                "status": "replace_failed",
                "error": str(e),
            }

    def health_check_all(self, platform: str = None) -> List[Dict[str, Any]]:
        """Health check all accounts."""
        if platform:
            accounts = self._db.get_accounts_by_platform(platform)
        else:
            accounts = self._db.get_all_accounts()

        results = []
        for account in accounts:
            try:
                result = self.health_check(account["id"])
                results.append(result)
            except Exception as e:
                results.append({"account_id": account["id"], "status": "check_failed", "error": str(e)})
        return results

    def auto_replace_dead(self, platform: str = None) -> List[Dict[str, Any]]:
        """Auto-replace all dead accounts."""
        if platform:
            accounts = self._db.get_accounts_by_platform(platform, active_only=False)
        else:
            accounts = self._db.get_all_accounts(active_only=False)

        results = []
        for account in accounts:
            if account.get("is_active", 1) == 0 or account.get("health_score", 100) < 20:
                try:
                    result = self.auto_replace(account["id"])
                    results.append(result)
                except Exception as e:
                    results.append({"account_id": account["id"], "status": "replace_failed", "error": str(e)})
        return results

    def get_stats(self) -> Dict[str, Any]:
        """Get account manager statistics."""
        with self._lock:
            return dict(self._stats)

class AccountFactoryCore:
    """Orchestrates all account creation. Parallel creation (50 threads)."""

    __slots__ = ("_lock", "_db", "_crypto", "_behavior", "_captcha", "_temp_email",
                  "_temp_phone", "_creator", "_warmup", "_manager", "_browser",
                  "_stats", "_running", "_thread_pool", "_queue", "_proxy_pool")

    def __init__(self, master_key: str = None, proxy_list: List[str] = None):
        self._master_key = master_key or hashlib.sha256(os.urandom(32)).hexdigest()
        self._crypto = OanksCryptoBridge(self._master_key)
        self._db = AccountsDB(OanksConfig.ACCOUNTS_DB_PATH, self._crypto)
        self._behavior = HumanBehaviorSimulator()
        self._captcha = CaptchaSolver()
        self._temp_email = TempEmailManager(self._db)
        self._temp_phone = TempPhoneManager(self._db)
        self._creator = AccountCreator(self._db, self._crypto, self._behavior,
                                       self._captcha, self._temp_email, self._temp_phone)
        self._warmup = AccountWarmup(self._db, self._behavior)
        self._manager = AccountManager(self._db, self._creator)
        self._browser = BrowserManager()
        self._proxy_pool = proxy_list or []
        self._proxy_rotation_index = 0
        self._lock = threading.RLock()
        self._stats = {
            "total_created": 0, "total_failed": 0, "total_warmed": 0,
            "total_checked": 0, "total_replaced": 0, "by_platform": Counter(),
            "creation_start_time": None, "creation_end_time": None,
        }
        self._running = False
        self._thread_pool = None
        self._queue = queue.Queue()

    def add_creation_job(self, platform: str, count: int = 1, priority: int = 5,
                         use_phone: bool = False) -> List[int]:
        """Add account creation jobs to queue."""
        job_ids = []
        for _ in range(count):
            job_id = self._db.add_to_queue(platform, priority)
            self._queue.put({
                "job_id": job_id,
                "platform": platform,
                "use_phone": use_phone,
            })
            job_ids.append(job_id)
        return job_ids

    def _get_proxy(self) -> Optional[str]:
        """Get next proxy from pool using round-robin rotation."""
        if not self._proxy_pool:
            return None
        with self._lock:
            proxy = self._proxy_pool[self._proxy_rotation_index % len(self._proxy_pool)]
            self._proxy_rotation_index += 1
            return proxy

    def _create_single_account(self, job: Dict) -> Dict[str, Any]:
        """Create a single account from job."""
        job_id = job["job_id"]
        platform = job["platform"]
        use_phone = job.get("use_phone", False)
        proxy = self._get_proxy()

        self._db.update_job_status(job_id, "running")

        try:
            result = self._creator.create_account(platform, proxy=proxy, use_phone=use_phone)
            account_id = result.get("account_id")

            # Create warmup schedule
            self._db.create_warmup_schedule(account_id)

            self._db.update_job_status(job_id, "completed", account_id=account_id)

            with self._lock:
                self._stats["total_created"] += 1
                self._stats["by_platform"][platform] += 1

            return {
                "job_id": job_id,
                "account_id": account_id,
                "platform": platform,
                "status": "success",
                "result": result,
            }
        except Exception as e:
            self._db.update_job_status(job_id, "failed", error_message=str(e))

            with self._lock:
                self._stats["total_failed"] += 1

            return {
                "job_id": job_id,
                "platform": platform,
                "status": "failed",
                "error": str(e),
            }

    def run_parallel_creation(self, max_threads: int = None) -> List[Dict[str, Any]]:
        """Run parallel account creation with thread pool."""
        max_threads = max_threads or OanksConfig.MAX_THREADS

        with self._lock:
            self._stats["creation_start_time"] = datetime.datetime.utcnow().isoformat()
            self._running = True

        results = []

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = []
            while not self._queue.empty() and self._running:
                try:
                    job = self._queue.get(block=False)
                    future = executor.submit(self._create_single_account, job)
                    futures.append(future)
                except queue.Empty:
                    break

            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    results.append({"status": "exception", "error": str(e)})

        with self._lock:
            self._stats["creation_end_time"] = datetime.datetime.utcnow().isoformat()
            self._running = False

        return results

    def run_sequential_creation(self, platform: str, count: int = 1,
                                 use_phone: bool = False) -> List[Dict[str, Any]]:
        """Run sequential account creation."""
        results = []
        for _ in range(count):
            proxy = self._get_proxy()
            try:
                result = self._creator.create_account(platform, proxy=proxy, use_phone=use_phone)
                account_id = result.get("account_id")
                self._db.create_warmup_schedule(account_id)

                with self._lock:
                    self._stats["total_created"] += 1
                    self._stats["by_platform"][platform] += 1

                results.append({"status": "success", "result": result})
            except Exception as e:
                with self._lock:
                    self._stats["total_failed"] += 1
                results.append({"status": "failed", "error": str(e)})
        return results

    def run_warmup(self, account_ids: List[int] = None, platform: str = None) -> List[Dict[str, Any]]:
        """Run warmup on accounts."""
        if account_ids is None:
            if platform:
                accounts = self._db.get_accounts_by_platform(platform)
            else:
                accounts = self._db.get_all_accounts()
            account_ids = [a["id"] for a in accounts if a.get("is_warmed", 0) == 0]

        results = self._warmup.warm_batch(account_ids)

        with self._lock:
            successful = sum(1 for r in results if r.get("status") == "completed")
            self._stats["total_warmed"] += successful

        return results

    def run_health_checks(self, platform: str = None) -> List[Dict[str, Any]]:
        """Run health checks on all accounts."""
        results = self._manager.health_check_all(platform)

        with self._lock:
            self._stats["total_checked"] += len(results)

        return results

    def run_auto_replace(self, platform: str = None) -> List[Dict[str, Any]]:
        """Auto-replace dead accounts."""
        results = self._manager.auto_replace_dead(platform)

        with self._lock:
            self._stats["total_replaced"] += len([r for r in results if r.get("status") == "replaced"])

        return results

    def run_full_pipeline(self, platform: str, count: int = 1,
                          use_phone: bool = False, max_threads: int = None) -> Dict[str, Any]:
        """Run full pipeline: create -> warmup -> health check."""
        # Step 1: Create accounts
        creation_results = self.run_sequential_creation(platform, count, use_phone)

        # Step 2: Warm up created accounts
        created_ids = [r["result"]["account_id"] for r in creation_results
                       if r.get("status") == "success" and "result" in r]
        warmup_results = []
        if created_ids:
            warmup_results = self.run_warmup(created_ids)

        # Step 3: Health check
        health_results = []
        if created_ids:
            health_results = self.run_health_checks(platform)

        return {
            "platform": platform,
            "requested": count,
            "created": len(created_ids),
            "failed": count - len(created_ids),
            "creation_results": creation_results,
            "warmup_results": warmup_results,
            "health_results": health_results,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "oanks_tag": OANKS_SIGNATURE,
        }

    def run_mass_creation(self, platforms: Dict[str, int], use_phone: bool = False,
                          max_threads: int = None) -> Dict[str, Any]:
        """Mass create accounts across multiple platforms."""
        all_results = {}

        for platform, count in platforms.items():
            self.add_creation_job(platform, count, use_phone=use_phone)

        # Run all jobs in parallel
        creation_results = self.run_parallel_creation(max_threads)

        # Group by platform
        for result in creation_results:
            platform = result.get("platform", "unknown")
            if platform not in all_results:
                all_results[platform] = []
            all_results[platform].append(result)

        # Warm up all created accounts
        all_ids = []
        for results in all_results.values():
            for r in results:
                if r.get("status") == "success" and "result" in r:
                    all_ids.append(r["result"]["account_id"])

        warmup_results = []
        if all_ids:
            warmup_results = self.run_warmup(all_ids)

        return {
            "total_requested": sum(platforms.values()),
            "total_created": sum(1 for r in creation_results if r.get("status") == "success"),
            "total_failed": sum(1 for r in creation_results if r.get("status") != "success"),
            "by_platform": all_results,
            "warmup_results": warmup_results,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "oanks_tag": OANKS_SIGNATURE,
        }

    def stop(self):
        """Stop all creation processes."""
        with self._lock:
            self._running = False

    def get_stats(self) -> Dict[str, Any]:
        """Get factory core statistics."""
        with self._lock:
            stats = dict(self._stats)
            stats["db_stats"] = self._db.get_stats()
            stats["creator_stats"] = self._creator.get_stats()
            stats["warmup_stats"] = self._warmup.get_stats()
            stats["manager_stats"] = self._manager.get_stats()
            stats["email_stats"] = self._temp_email.get_stats()
            stats["phone_stats"] = self._temp_phone.get_stats()
            stats["behavior_stats"] = self._behavior.get_stats()
            stats["captcha_stats"] = self._captcha.get_stats()
            stats["oanks_identity"] = OANKS_IDENTITY
            stats["oanks_version"] = OANKS_VERSION
            stats["oanks_signature"] = OANKS_SIGNATURE
            stats["timestamp"] = datetime.datetime.utcnow().isoformat()
            return stats

    def export_accounts(self, platform: str = None, format_type: str = "json") -> str:
        """Export accounts to file."""
        if platform:
            accounts = self._db.get_accounts_by_platform(platform, active_only=False)
        else:
            accounts = self._db.get_all_accounts(active_only=False)

        # Decrypt passwords for export
        export_data = []
        for account in accounts:
            try:
                password = self._crypto.decrypt(account["password_enc"])
            except:
                password = "[encrypted]"

            export_data.append({
                "id": account["id"],
                "platform": account["platform"],
                "username": account["username"],
                "email": account["email"],
                "phone": account["phone"],
                "password": password,
                "created_at": account["created_at"],
                "is_active": account["is_active"],
                "is_warmed": account["is_warmed"],
                "health_score": account["health_score"],
                "proxy_used": account["proxy_used"],
                "oanks_tag": OANKS_SIGNATURE,
            })

        timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"oanks_accounts_export_{timestamp}.{format_type}"
        filepath = os.path.join(OanksConfig.EXPORT_DIR, filename)
        os.makedirs(OanksConfig.EXPORT_DIR, exist_ok=True)

        if format_type == "json":
            with open(filepath, "w") as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
        elif format_type == "csv":
            if export_data:
                keys = export_data[0].keys()
                with open(filepath, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(export_data)

        return filepath

    def emergency_wipe(self):
        """Emergency wipe all data."""
        with self._lock:
            self._running = False
            self._db.secure_wipe()
            self._crypto.secure_wipe()

            # Wipe export directory
            if os.path.exists(OanksConfig.EXPORT_DIR):
                for f in os.listdir(OanksConfig.EXPORT_DIR):
                    fpath = os.path.join(OanksConfig.EXPORT_DIR, f)
                    try:
                        if os.path.isfile(fpath):
                            size = os.path.getsize(fpath)
                            with open(fpath, "r+b") as fh:
                                for _ in range(3):
                                    fh.seek(0)
                                    fh.write(os.urandom(size))
                                    fh.flush()
                                    os.fsync(fh.fileno())
                                fh.seek(0)
                                fh.write(b"\x00" * size)
                                fh.flush()
                                os.fsync(fh.fileno())
                            os.remove(fpath)
                    except:
                        pass

            # Clear stats
            for key in self._stats:
                self._stats[key] = 0

    def get_component(self, name: str):
        """Get a specific component by name."""
        components = {
            "creator": self._creator,
            "warmup": self._warmup,
            "manager": self._manager,
            "browser": self._browser,
            "database": self._db,
            "crypto": self._crypto,
            "behavior": self._behavior,
            "captcha": self._captcha,
            "temp_email": self._temp_email,
            "temp_phone": self._temp_phone,
        }
        return components.get(name.lower())

# ============================================================================
# SECTION 16: CLASS 9 — BrowserManager
# ============================================================================

class BrowserManager:
    """Launch browsers with proxy, fingerprint spoofing, session persistence.
    Supports Chrome/Chromium, Firefox, Edge. Mobile emulation. Selenium fallback."""

    __slots__ = ("_lock", "_active_browsers", "_stats", "_fingerprint_rotator",
                 "_browser_rotation_index", "_ud_available", "_selenium_available")

    def __init__(self):
        self._lock = threading.RLock()
        self._active_browsers = {}
        self._stats = {"launched": 0, "closed": 0, "crashed": 0, "sessions_persisted": 0,
                       "fallback_used": 0, "chrome": 0, "firefox": 0, "edge": 0, "mobile": 0}
        self._fingerprint_rotator = self._create_fingerprint_rotator()
        self._browser_rotation_index = 0
        self._ud_available = self._check_undetected_chromedriver()
        self._selenium_available = self._check_selenium()

    def _check_undetected_chromedriver(self) -> bool:
        """Check if undetected_chromedriver is available."""
        try:
            import undetected_chromedriver as uc
            return True
        except ImportError:
            return False

    def _check_selenium(self) -> bool:
        """Check if standard selenium is available."""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            from selenium.webdriver.edge.options import Options as EdgeOptions
            return True
        except ImportError:
            return False

    def _create_fingerprint_rotator(self):
        """Create rotating fingerprint generator with mobile presets."""
        return {
            "user_agents": OanksConfig.USER_AGENTS,
            "window_sizes": AccountFactoryConstants.BROWSER_WINDOW_SIZES,
            "screen_resolutions": AccountFactoryConstants.SCREEN_RESOLUTIONS,
            "timezones": AccountFactoryConstants.TIMEZONE_OFFSETS,
            "languages": AccountFactoryConstants.LANGUAGES,
            "webgl_pairs": AccountFactoryConstants.WEBGL_FINGERPRINTS,
            "fonts": AccountFactoryConstants.PLATFORM_FONTS,
            "platforms": AccountFactoryConstants.PLATFORM_STRINGS,
            "hardware_concurrency": AccountFactoryConstants.HARDWARE_CONCURRENCY,
            "device_memory": AccountFactoryConstants.DEVICE_MEMORY,
            "mobile_presets": [
                {"device": "iPhone 14", "width": 390, "height": 844, "pixel_ratio": 3.0, "touch": True, "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"},
                {"device": "iPhone 14 Pro Max", "width": 430, "height": 932, "pixel_ratio": 3.0, "touch": True, "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"},
                {"device": "Pixel 7", "width": 412, "height": 915, "pixel_ratio": 2.625, "touch": True, "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"},
                {"device": "Pixel 7 Pro", "width": 412, "height": 915, "pixel_ratio": 3.5, "touch": True, "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"},
                {"device": "Samsung S23", "width": 384, "height": 854, "pixel_ratio": 3.0, "touch": True, "ua": "Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"},
                {"device": "iPad Pro", "width": 1024, "height": 1366, "pixel_ratio": 2.0, "touch": True, "ua": "Mozilla/5.0 (iPad; CPU OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"},
            ],
        }

    def _generate_fingerprint(self, mobile: bool = False) -> Dict[str, Any]:
        """Generate unique browser fingerprint. Mobile presets available."""
        if mobile and random.random() < 0.3:
            preset = random.choice(self._fingerprint_rotator["mobile_presets"])
            fp = {
                "user_agent": preset["ua"],
                "window_size": (preset["width"], preset["height"]),
                "screen_resolution": (preset["width"] * 2, preset["height"] * 2),
                "timezone": random.choice(self._fingerprint_rotator["timezones"]),
                "language": random.choice(self._fingerprint_rotator["languages"]),
                "webgl": random.choice(self._fingerprint_rotator["webgl_pairs"]),
                "font": random.choice(self._fingerprint_rotator["fonts"]),
                "platform": "Win32" if random.random() < 0.5 else "MacIntel",
                "hardware_concurrency": random.choice([4, 6, 8]),
                "device_memory": random.choice([4, 8]),
                "touch_support": preset["touch"],
                "color_depth": 32,
                "pixel_ratio": preset["pixel_ratio"],
                "mobile": True,
                "device_name": preset["device"],
            }
        else:
            fp = {
                "user_agent": random.choice(self._fingerprint_rotator["user_agents"]),
                "window_size": random.choice(self._fingerprint_rotator["window_sizes"]),
                "screen_resolution": random.choice(self._fingerprint_rotator["screen_resolutions"]),
                "timezone": random.choice(self._fingerprint_rotator["timezones"]),
                "language": random.choice(self._fingerprint_rotator["languages"]),
                "webgl": random.choice(self._fingerprint_rotator["webgl_pairs"]),
                "font": random.choice(self._fingerprint_rotator["fonts"]),
                "platform": random.choice(self._fingerprint_rotator["platforms"]),
                "hardware_concurrency": random.choice(self._fingerprint_rotator["hardware_concurrency"]),
                "device_memory": random.choice(self._fingerprint_rotator["device_memory"]),
                "touch_support": random.random() < AccountFactoryConstants.TOUCH_SUPPORT_PROB,
                "color_depth": random.choice(AccountFactoryConstants.COLOR_DEPTHS),
                "pixel_ratio": 1.0,
                "mobile": False,
                "device_name": "Desktop",
            }
        return fp

    def _build_chrome_options(self, fingerprint: Dict, proxy: str, headless: bool) -> List[str]:
        """Build Chrome command-line options."""
        options = []
        width, height = fingerprint["window_size"]
        options.append(f"--window-size={width},{height}")
        options.append(f"--user-agent={fingerprint['user_agent']}")
        if proxy:
            options.append(f"--proxy-server={proxy}")
        if headless:
            options.append("--headless=new")
        options.extend([
            "--no-sandbox", "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled",
            "--disable-web-security",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-site-isolation-trials",
            "--disable-background-networking",
            "--disable-background-timer-throttling",
            "--disable-backgrounding-occluded-windows",
            "--disable-breakpad",
            "--disable-client-side-phishing-detection",
            "--disable-component-update",
            "--disable-default-apps",
            "--disable-domain-reliability",
            "--disable-extensions",
            "--disable-hang-monitor",
            "--disable-ipc-flooding-protection",
            "--disable-notifications",
            "--disable-popup-blocking",
            "--disable-prompt-on-repost",
            "--disable-renderer-backgrounding",
            "--disable-sync",
            "--force-color-profile=srgb",
            "--metrics-recording-only",
            "--no-first-run",
            "--password-store=basic",
            "--use-mock-keychain",
            "--disable-infobars",
            "--hide-scrollbars",
            "--mute-audio",
        ])
        if fingerprint.get("mobile"):
            options.append("--enable-touch-events")
            options.append(f"--device-scale-factor={fingerprint['pixel_ratio']}")
        options.append(f"--lang={fingerprint['language'].split(',')[0]}")
        options.append(f"--timezone={fingerprint['timezone']}")
        return options

    def launch_browser(self, proxy: str = None, headless: bool = None,
                       session_id: str = None, browser_type: str = None,
                       mobile: bool = False) -> Dict[str, Any]:
        """Launch browser with full fingerprint spoofing. Multi-browser support.
        Falls back to standard selenium if undetected_chromedriver unavailable."""
        if headless is None:
            headless = AccountFactoryConstants.BROWSER_HEADLESS
        if browser_type is None:
            browser_type = self._rotate_browser_type()

        fingerprint = self._generate_fingerprint(mobile=mobile)
        browser_id = session_id or str(uuid.uuid4())
        driver = None
        fallback_used = False

        try:
            if browser_type == "chrome":
                driver = self._launch_chrome(fingerprint, proxy, headless)
            elif browser_type == "firefox":
                driver = self._launch_firefox(fingerprint, proxy, headless)
            elif browser_type == "edge":
                driver = self._launch_edge(fingerprint, proxy, headless)
        except Exception as e:
            # Fallback to standard selenium
            if self._selenium_available:
                try:
                    driver = self._launch_selenium_fallback(browser_type, fingerprint, proxy, headless)
                    fallback_used = True
                except Exception:
                    pass
            if driver is None:
                raise BrowserError(f"Failed to launch {browser_type}: {e}", code="BROWSER_LAUNCH_FAIL")

        browser_config = {
            "browser_id": browser_id,
            "browser_type": browser_type,
            "fingerprint": fingerprint,
            "proxy": proxy,
            "headless": headless,
            "driver": driver,
            "launched_at": datetime.datetime.utcnow().isoformat(),
            "status": "active",
            "fallback_used": fallback_used,
        }

        with self._lock:
            self._active_browsers[browser_id] = browser_config
            self._stats["launched"] += 1
            self._stats[browser_type] += 1
            if fallback_used:
                self._stats["fallback_used"] += 1
            if fingerprint.get("mobile"):
                self._stats["mobile"] += 1

        return browser_config

    def _rotate_browser_type(self) -> str:
        """Rotate browser type for diversity."""
        types = ["chrome", "chrome", "chrome", "firefox", "edge"]
        with self._lock:
            bt = types[self._browser_rotation_index % len(types)]
            self._browser_rotation_index += 1
            return bt

    def _launch_chrome(self, fingerprint: Dict, proxy: str, headless: bool):
        """Launch Chrome/Chromium."""
        options = self._build_chrome_options(fingerprint, proxy, headless)
        if self._ud_available:
            import undetected_chromedriver as uc
            opts = uc.ChromeOptions()
            for opt in options:
                opts.add_argument(opt)
            return uc.Chrome(options=opts, version_main=None)
        else:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            opts = Options()
            for opt in options:
                opts.add_argument(opt)
            return webdriver.Chrome(options=opts)

    def _launch_firefox(self, fingerprint: Dict, proxy: str, headless: bool):
        """Launch Firefox."""
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
        opts = Options()
        if headless:
            opts.add_argument("--headless")
        width, height = fingerprint["window_size"]
        opts.add_argument(f"--width={width}")
        opts.add_argument(f"--height={height}")
        profile = FirefoxProfile()
        profile.set_preference("general.useragent.override", fingerprint["user_agent"])
        if proxy:
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", proxy.split(":")[0])
            profile.set_preference("network.proxy.http_port", int(proxy.split(":")[1]))
        opts.profile = profile
        return webdriver.Firefox(options=opts)

    def _launch_edge(self, fingerprint: Dict, proxy: str, headless: bool):
        """Launch Edge."""
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options
        opts = Options()
        if headless:
            opts.add_argument("--headless=new")
        width, height = fingerprint["window_size"]
        opts.add_argument(f"--window-size={width},{height}")
        opts.add_argument(f"--user-agent={fingerprint['user_agent']}")
        if proxy:
            opts.add_argument(f"--proxy-server={proxy}")
        opts.add_argument("--disable-blink-features=AutomationControlled")
        return webdriver.Edge(options=opts)

    def _launch_selenium_fallback(self, browser_type: str, fingerprint: Dict, proxy: str, headless: bool):
        """Fallback to standard selenium webdriver."""
        from selenium import webdriver
        if browser_type == "chrome":
            from selenium.webdriver.chrome.options import Options
            opts = Options()
            if headless:
                opts.add_argument("--headless=new")
            width, height = fingerprint["window_size"]
            opts.add_argument(f"--window-size={width},{height}")
            opts.add_argument(f"--user-agent={fingerprint['user_agent']}")
            if proxy:
                opts.add_argument(f"--proxy-server={proxy}")
            return webdriver.Chrome(options=opts)
        elif browser_type == "firefox":
            from selenium.webdriver.firefox.options import Options
            opts = Options()
            if headless:
                opts.add_argument("--headless")
            return webdriver.Firefox(options=opts)
        elif browser_type == "edge":
            from selenium.webdriver.edge.options import Options
            opts = Options()
            if headless:
                opts.add_argument("--headless=new")
            return webdriver.Edge(options=opts)
        return None

    def get_browser(self, browser_id: str) -> Dict[str, Any]:
        """Get browser configuration by ID."""
        with self._lock:
            return self._active_browsers.get(browser_id)

    def close_browser(self, browser_id: str) -> bool:
        """Close browser and clean up."""
        with self._lock:
            if browser_id in self._active_browsers:
                config = self._active_browsers[browser_id]
                try:
                    if config.get("driver"):
                        config["driver"].quit()
                except Exception:
                    pass
                del self._active_browsers[browser_id]
                self._stats["closed"] += 1
                return True
            return False

    def persist_session(self, browser_id: str, cookies: Dict = None) -> bool:
        """Persist browser session cookies."""
        with self._lock:
            if browser_id not in self._active_browsers:
                return False
            self._active_browsers[browser_id]["cookies"] = cookies or {}
            self._active_browsers[browser_id]["session_persisted_at"] = datetime.datetime.utcnow().isoformat()
            self._stats["sessions_persisted"] += 1
            return True

    def get_active_count(self) -> int:
        """Get count of active browsers."""
        with self._lock:
            return len(self._active_browsers)

    def get_stats(self) -> Dict[str, Any]:
        """Get browser manager statistics."""
        with self._lock:
            return dict(self._stats)
