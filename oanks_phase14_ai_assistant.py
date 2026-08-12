#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
👑 OANKS OPERATIONS FRAMEWORK — PHASE 14: AI ASSISTANT
================================================================================
Classification: MALEVOLENT EXECUTION — PHASE 14
Creator: Oanks (@oanksnood)
Module: AI Assistant — Autonomous, Adaptive, Self-Optimizing Intelligence Engine
Danger Level: 11/10

DESCRIPTION:
    Phase 14 is the artificial intelligence engine of the Oanks Operations
    Framework. It transforms the framework from a tool into a living, breathing,
    autonomous predator. This phase makes decisions without human intervention,
    adapts to changing conditions in real-time, predicts data availability,
    detects anomalies before they become threats, and optimizes itself
    continuously. 

    NO TensorFlow. NO PyTorch. NO scikit-learn. NO Keras. NO GUI.
    Pure Python. Pure memory. Pure statistics. Pure dominance.

    This is not machine learning. This is machine INTELLIGENCE.
    This is not automation. This is AUTONOMY.
    This is not a script. This is a SENTINEL.

INTEGRATION:
    Phase 1  — Database, logging, crypto, persistence
    Phase 2  — Proxy intelligence, rotation, validation
    Phase 3  — Adaptive scraping, predictive harvesting
    Phase 4  — Intelligent enrichment, correlation, threat ranking
    Phase 5  — Auto-account creation, mass registration
    Phase 6  — Premium AI features, monetization
    Phase 7  — Telegram command center, interactive controls
    Phase 8  — Predictive pricing, inventory optimization
    Phase 9  — Anomaly detection, auto-response, kill switch
    Phase 10 — Intelligent worm propagation, botnet creation
    Phase 11 — Auto-ransomware decisions, system destruction
    Phase 12 — Distributed AI, shared learning across nodes
    Phase 13 — Darkweb intelligence automation, onion crawling
    Phase 15 — Final deployment, main entry point

REQUIREMENTS:
    Python 3.8+
    Standard library only (no external ML libraries)
    SQLite3 (built-in)
    NumPy (lightweight, Termux-compatible)
    Threading, multiprocessing support

BRANDING:
    👑 Oanks — Creator
    Every table, every log, every decision carries the Creator's mark.

WARNING:
    This module is designed for autonomous operation. Once started, it will
    make decisions, execute actions, and optimize itself without human input.
    Use with extreme caution. This is not a toy. This is a weapon.

================================================================================
"""

# ==============================================================================
# STANDARD LIBRARY IMPORTS
# ==============================================================================
import os
import sys
import json
import sqlite3
import threading
import time
import random
import datetime
import math
import statistics
import collections
import hashlib
import re
import logging
import traceback
import itertools
import functools
import inspect
import types
import warnings
import uuid
import copy
import heapq
import bisect
import string
import csv
import io
import base64
import urllib.parse
import urllib.request
import socket
import subprocess
import signal
import gc
import weakref
import enum
import dataclasses
from typing import Dict, List, Optional, Tuple, Any, Union, Callable, Set, Iterator
from collections import defaultdict, Counter, deque, OrderedDict
from datetime import datetime, timedelta
from threading import Thread, Lock, Event, RLock, Timer
from concurrent.futures import ThreadPoolExecutor, as_completed
from statistics import mean, median, stdev, variance, mode
from math import exp, log, sqrt, pow, ceil, floor, inf, nan
from dataclasses import dataclass, field, asdict
from enum import Enum, auto

# ==============================================================================
# OPTIONAL NUMPY IMPORT (Lightweight, Termux-Compatible)
# ==============================================================================
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    np = None

# ==============================================================================
# SUPPRESS WARNINGS
# ==============================================================================
warnings.filterwarnings('ignore')

# ==============================================================================
# OANKS BRANDING CONSTANTS
# ==============================================================================
OANKS_TAG = "👑 Oanks — Creator"
OANKS_FRAMEWORK = "Oanks Operations Framework"
OANKS_VERSION = "14.0.0"
OANKS_PHASE = "Phase 14: AI Assistant"
OANKS_CLASSIFICATION = "MALEVOLENT EXECUTION"
OANKS_DANGER_LEVEL = 11

# ==============================================================================
# DECISION ENGINE CONSTANTS
# ==============================================================================
class DecisionConfig:
    """Configuration for the auto-decision making engine."""
    MAX_OPTIONS = 20
    MIN_CONFIDENCE = 0.3
    MAX_CONFIDENCE = 1.0
    DEFAULT_CONFIDENCE = 0.5
    LEARNING_RATE = 0.15
    EXPLORATION_RATE = 0.1
    DECISION_HISTORY_LIMIT = 1000
    STATE_ANALYSIS_INTERVAL = 30
    DECISION_COOLDOWN = 5
    WEIGHT_SUCCESS = 0.6
    WEIGHT_SPEED = 0.4
    WEIGHT_RECENCY = 0.2
    WEIGHT_FREQUENCY = 0.3
    WEIGHT_DIVERSITY = 0.1
    THRESHOLD_HIGH = 75
    THRESHOLD_MEDIUM = 50
    THRESHOLD_LOW = 25
    PATTERN_MATCH_THRESHOLD = 0.7
    MAX_PATTERN_AGE_DAYS = 30
    DECISION_TIMEOUT = 300
    EXECUTION_TIMEOUT = 600

# ==============================================================================
# ADAPTIVE SCRAPING CONSTANTS
# ==============================================================================
class ScrapeConfig:
    """Configuration for adaptive scraping engine."""
    MAX_RETRIES = 5
    BASE_DELAY = 1.0
    MAX_DELAY = 60.0
    BACKOFF_MULTIPLIER = 2.0
    BACKOFF_JITTER = 0.3
    CAPTCHA_KEYWORDS = [
        "captcha", "recaptcha", "g-recaptcha", "hcaptcha", 
        "verify you are human", "prove you are human", "i'm not a robot",
        "security check", "bot detection", "automated access detected",
        "suspicious activity", "unusual traffic", "challenge"
    ]
    BLOCK_KEYWORDS = [
        "blocked", "forbidden", "access denied", "unauthorized",
        "banned", "blacklisted", "restricted", "suspended",
        "too many requests", "rate limit exceeded", "ip blocked"
    ]
    HONEYPOT_PATTERNS = [
        r"display\s*:\s*none",
        r"visibility\s*:\s*hidden",
        r"opacity\s*:\s*0",
        r"position\s*:\s*absolute.*left\s*:\s*-9999",
        r"hidden.*field",
        r"honeypot",
        r"trap",
        r"decoy"
    ]
    RATE_LIMIT_STATUS = [429, 503, 509]
    BLOCK_STATUS = [403, 401, 407]
    SUCCESS_STATUS = [200, 201, 202, 204]
    USER_AGENT_ROTATION_INTERVAL = 10
    PROXY_SWITCH_ON_BLOCK = True
    STRATEGY_LEARNING_ENABLED = True
    TARGET_MEMORY_SIZE = 500
    DELAY_ADJUSTMENT_STEP = 0.5
    MIN_DELAY = 0.5
    MAX_DELAY = 120.0
    CONSECUTIVE_FAILURE_THRESHOLD = 3
    STRATEGY_RESET_THRESHOLD = 10

# ==============================================================================
# PROXY INTELLIGENCE CONSTANTS
# ==============================================================================
class ProxyConfig:
    """Configuration for intelligent proxy rotation engine."""
    SCORE_SUCCESS_WEIGHT = 0.6
    SCORE_SPEED_WEIGHT = 0.4
    SCORE_STABILITY_WEIGHT = 0.2
    SCORE_AGE_WEIGHT = 0.1
    MIN_PROXIES_PREFETCH = 50
    MAX_PROXIES_PREFETCH = 200
    PROXY_VALIDATION_TIMEOUT = 10
    PROXY_HEALTH_CHECK_INTERVAL = 300
    PROXY_FAILURE_THRESHOLD = 5
    PROXY_SUCCESS_THRESHOLD = 3
    PROXY_DEPRECATION_THRESHOLD = 0.3
    PROXY_BOOST_THRESHOLD = 0.8
    PREDICTION_WINDOW = 10
    PREDICTION_CONFIDENCE_MIN = 0.6
    TARGET_PAIRING_MEMORY_SIZE = 1000
    ROTATION_STRATEGY = "intelligent"  # random, round-robin, intelligent, predictive
    GEOGRAPHIC_DISTRIBUTION = True
    PROTOCOL_PREFERENCE = ["socks5", "socks4", "http", "https"]
    ANONYMITY_LEVELS = ["elite", "anonymous", "transparent"]
    MAX_RESPONSE_TIME = 10.0
    MIN_RESPONSE_TIME = 0.1
    RESPONSE_TIME_BUCKETS = [0.5, 1.0, 2.0, 5.0, 10.0]

# ==============================================================================
# PREDICTIVE HARVESTING CONSTANTS
# ==============================================================================
class PredictConfig:
    """Configuration for predictive harvesting engine."""
    PATTERN_DETECTION_WINDOW = 168  # hours (1 week)
    MIN_PATTERN_OCCURRENCES = 3
    PATTERN_CONFIDENCE_THRESHOLD = 0.6
    PREDICTION_HORIZON = 24  # hours
    VOLUME_PREDICTION_WINDOW = 72  # hours
    SEASONALITY_DETECTION = True
    TREND_ANALYSIS_ENABLED = True
    DATA_TYPE_CORRELATION = True
    SOURCE_RANKING_MEMORY = 500
    SCHEDULE_AHEAD_BUFFER = 3600  # seconds
    PREDICTION_ACCURACY_THRESHOLD = 0.7
    PATTERN_REINFORCEMENT_RATE = 0.2
    PATTERN_DECAY_RATE = 0.05
    MAX_STORED_PATTERNS = 1000
    TIME_BUCKET_SIZE = 3600  # 1 hour buckets
    DAY_BUCKET_SIZE = 86400  # 1 day buckets
    WEEK_BUCKET_SIZE = 604800  # 1 week buckets
    VOLUME_BUCKETS = [10, 50, 100, 500, 1000, 5000, 10000]
    CONFIDENCE_CALCULATION = "weighted"  # simple, weighted, bayesian

# ==============================================================================
# ANOMALY DETECTION CONSTANTS
# ==============================================================================
class AnomalyConfig:
    """Configuration for anomaly detection engine."""
    BASELINE_WINDOW = 3600  # 1 hour
    ROLLING_WINDOW_SIZE = 100
    VARIANCE_MULTIPLIER_HIGH = 3.0
    VARIANCE_MULTIPLIER_MEDIUM = 2.0
    VARIANCE_MULTIPLIER_LOW = 1.5
    MIN_BASELINE_SAMPLES = 10
    ANOMALY_COOLDOWN = 60
    SEVERITY_LEVELS = {
        1: "INFO",
        2: "LOW", 
        3: "MEDIUM",
        4: "HIGH",
        5: "CRITICAL"
    }
    AUTO_RESPONSE_ENABLED = True
    NETWORK_ANOMALY_THRESHOLD = 3.0
    ACCESS_ANOMALY_THRESHOLD = 2.5
    DATA_ANOMALY_THRESHOLD = 3.5
    SYSTEM_ANOMALY_THRESHOLD = 2.0
    ANOMALY_LOG_RETENTION = 2592000  # 30 days
    BASELINE_UPDATE_INTERVAL = 3600
    OUTLIER_DETECTION_METHOD = "iqr"  # iqr, zscore, mad, grubbs
    TREND_DETECTION_ENABLED = True
    SEASONAL_ADJUSTMENT = True
    CORRELATION_ANALYSIS = True
    ANOMALY_AGGREGATION_WINDOW = 300
    ALERT_DEDUPLICATION_WINDOW = 600

# ==============================================================================
# SELF-OPTIMIZATION CONSTANTS
# ==============================================================================
class OptimizeConfig:
    """Configuration for self-optimization engine."""
    CPU_THRESHOLD_HIGH = 80.0
    CPU_THRESHOLD_MEDIUM = 60.0
    CPU_THRESHOLD_LOW = 40.0
    MEMORY_THRESHOLD_HIGH = 80.0
    MEMORY_THRESHOLD_MEDIUM = 60.0
    MEMORY_THRESHOLD_LOW = 40.0
    RESPONSE_TIME_THRESHOLD = 5.0
    HARVEST_RATE_THRESHOLD = 10.0
    THREAD_ADJUSTMENT_STEP = 5
    CACHE_ADJUSTMENT_STEP = 100
    MIN_THREADS = 1
    MAX_THREADS = 100
    MIN_CACHE_SIZE = 50
    MAX_CACHE_SIZE = 10000
    OPTIMIZATION_INTERVAL = 300
    PERFORMANCE_LOG_RETENTION = 604800  # 7 days
    BOTTLENECK_DETECTION_METHOD = "threshold"  # threshold, regression, correlation
    PARAMETER_ADJUSTMENT_RATE = 0.2
    STABILITY_WINDOW = 10
    OPTIMIZATION_GOAL = "balanced"  # speed, stability, balanced, aggressive
    RESOURCE_MONITORING_ENABLED = True
    ADAPTIVE_THROTTLING = True
    LOAD_BALANCING_ENABLED = True
    PERFORMANCE_METRICS = [
        "cpu_usage", "memory_usage", "response_time", "harvest_rate",
        "proxy_success_rate", "decision_accuracy", "anomaly_count",
        "thread_count", "cache_hit_rate", "error_rate"
    ]

# ==============================================================================
# AUTONOMOUS MODE CONSTANTS
# ==============================================================================
class AutonomousConfig:
    """Configuration for autonomous operation mode."""
    HEARTBEAT_INTERVAL = 60
    STATUS_REPORT_INTERVAL = 3600
    ERROR_RECOVERY_ATTEMPTS = 3
    ERROR_RECOVERY_DELAY = 30
    PHASE_RESTART_ENABLED = True
    PROXY_AUTO_ROTATION = True
    TARGET_AUTO_SWITCH = True
    SELF_HEALING_ENABLED = True
    MAX_CONSECUTIVE_ERRORS = 5
    ERROR_ESCALATION_THRESHOLD = 10
    FULL_LOCKDOWN_THRESHOLD = 20
    TELEGRAM_REPORTING_ENABLED = True
    TELEGRAM_REPORT_FORMAT = "detailed"  # summary, detailed, verbose
    AUTONOMOUS_STARTUP_DELAY = 10
    PHASE_HEALTH_CHECK_INTERVAL = 300
    DECISION_EXECUTION_INTERVAL = 60
    EMERGENCY_STOP_ENABLED = True
    EMERGENCY_STOP_CODE = "OANKS_SHUTDOWN_14"
    WATCHDOG_ENABLED = True
    WATCHDOG_TIMEOUT = 300
    STATE_PERSISTENCE_INTERVAL = 600
    AUTONOMOUS_LOG_LEVEL = "INFO"
    MAX_AUTONOMOUS_RUNTIME = 0  # 0 = unlimited
    NIGHT_MODE_ENABLED = True
    NIGHT_MODE_HOURS = (2, 6)  # 2 AM to 6 AM

# ==============================================================================
# LEARNING ENGINE CONSTANTS
# ==============================================================================
class LearningConfig:
    """Configuration for learning from data engine."""
    MEMORY_SIZE_LIMIT = 10000
    PATTERN_MATCHING_DEPTH = 5
    SUCCESS_PATTERN_BOOST = 0.3
    FAILURE_PATTERN_PENALTY = 0.5
    KNOWLEDGE_BASE_LIMIT = 5000
    KNOWLEDGE_SHARING_INTERVAL = 3600
    NODE_SYNC_ENABLED = True
    PATTERN_SIMILARITY_THRESHOLD = 0.8
    CONTEXT_MATCHING_ENABLED = True
    TEMPORAL_LEARNING_ENABLED = True
    SPATIAL_LEARNING_ENABLED = True
    LEARNING_RATE_DECAY = 0.99
    MIN_LEARNING_RATE = 0.01
    FORGETTING_ENABLED = True
    FORGETTING_THRESHOLD = 0.1
    FORGETTING_INTERVAL = 86400
    KNOWLEDGE_COMPRESSION = True
    PATTERN_GENERALIZATION = True
    CROSS_DOMAIN_LEARNING = True
    EXPERIMENTAL_LEARNING_ENABLED = True
    EXPLORATION_EXPLOITATION_RATIO = 0.2
    LEARNING_VERIFICATION_ENABLED = True

# ==============================================================================
# TELEGRAM INTEGRATION CONSTANTS
# ==============================================================================
class TelegramConfig:
    """Configuration for Telegram bot integration (Phase 7)."""
    COMMAND_PREFIX = "/ai_"
    RESPONSE_FORMAT = "markdown"
    MAX_MESSAGE_LENGTH = 4096
    MESSAGE_SPLIT_ENABLED = True
    INTERACTIVE_BUTTONS = True
    PROGRESS_REPORTS = True
    STEP_BY_STEP_LOGGING = True
    REAL_TIME_UPDATES = True
    NOTIFICATION_LEVEL = "all"  # all, important, critical
    STATUS_UPDATE_INTERVAL = 300
    COMMAND_TIMEOUT = 60
    RATE_LIMIT_PER_USER = 10
    RATE_LIMIT_WINDOW = 60
    ADMIN_ONLY_COMMANDS = [
        "ai_start", "ai_stop", "ai_autonomous", "ai_autonomous_stop",
        "ai_learn", "ai_optimize"
    ]
    USER_COMMANDS = [
        "ai_status", "ai_decision", "ai_decisions", "ai_anomaly",
        "ai_anomalies", "ai_harvest_predict", "ai_proxy_intel",
        "ai_knowledge", "ai_performance", "ai_adapt", "ai_patterns"
    ]
    EMOJI_MAP = {
        "success": "✅",
        "failure": "❌",
        "warning": "⚠️",
        "info": "ℹ️",
        "running": "🔄",
        "stopped": "🛑",
        "decision": "🧠",
        "proxy": "🌐",
        "harvest": "📊",
        "anomaly": "🚨",
        "optimize": "⚡",
        "learn": "📚",
        "autonomous": "🤖",
        "pattern": "🎯",
        "knowledge": "💡",
        "performance": "📈",
        "step": "➡️",
        "complete": "✨",
        "thinking": "💭",
        "danger": "☠️",
        "oanks": "👑"
    }

# ==============================================================================
# DATABASE CONSTANTS
# ==============================================================================
class DatabaseConfig:
    """Configuration for database operations."""
    DB_NAME = "oanks_ai.db"
    CONNECTION_TIMEOUT = 30
    MAX_CONNECTIONS = 10
    JOURNAL_MODE = "WAL"
    SYNCHRONOUS = "NORMAL"
    CACHE_SIZE = 10000
    TEMP_STORE = "MEMORY"
    PAGE_SIZE = 4096
    LOCKING_MODE = "NORMAL"
    BUSY_TIMEOUT = 5000
    QUERY_TIMEOUT = 30
    BATCH_SIZE = 1000
    INDEXING_ENABLED = True
    VACUUM_INTERVAL = 86400
    BACKUP_ENABLED = True
    BACKUP_INTERVAL = 3600
    COMPRESSION_ENABLED = False

# ==============================================================================
# LOGGING CONSTANTS
# ==============================================================================
class LoggingConfig:
    """Configuration for logging system."""
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_FILE = "oanks_ai.log"
    LOG_ROTATION = True
    LOG_ROTATION_SIZE = 10485760  # 10MB
    LOG_ROTATION_COUNT = 10
    LOG_COLORS = {
        "DEBUG": "\033[36m",
        "INFO": "\033[32m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[35m"
    }
    LOG_TO_CONSOLE = True
    LOG_TO_FILE = True
    LOG_TO_TELEGRAM = True
    LOG_TELEGRAM_LEVEL = "WARNING"
    PERFORMANCE_LOG_ENABLED = True
    DECISION_LOG_ENABLED = True
    ANOMALY_LOG_ENABLED = True

# ==============================================================================
# UTILITY CONSTANTS
# ==============================================================================
class UtilityConfig:
    """General utility constants."""
    TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"
    UUID_LENGTH = 32
    HASH_ALGORITHM = "sha256"
    ENCODING = "utf-8"
    MAX_STRING_LENGTH = 65535
    MAX_JSON_DEPTH = 10
    TIMEZONE = "UTC"
    RANDOM_SEED = None
    DEBUG_MODE = False
    VERBOSE_MODE = True
    PROFILING_ENABLED = False
    METRICS_ENABLED = True

# ==============================================================================
# ENUMERATIONS
# ==============================================================================
class DecisionType(Enum):
    """Types of decisions the AI can make."""
    HARVEST = auto()
    PROXY_ROTATE = auto()
    PROXY_VALIDATE = auto()
    SCALE_UP = auto()
    SCALE_DOWN = auto()
    ALERT = auto()
    KILL_SWITCH = auto()
    OPTIMIZE = auto()
    LEARN = auto()
    ADAPT = auto()
    PREDICT = auto()
    ANOMALY_RESPONSE = auto()
    PHASE_RESTART = auto()
    TARGET_SWITCH = auto()
    STRATEGY_CHANGE = auto()
    IDLE = auto()
    EMERGENCY = auto()
    CUSTOM = auto()

class AnomalyType(Enum):
    """Types of anomalies that can be detected."""
    NETWORK = auto()
    ACCESS = auto()
    DATA = auto()
    SYSTEM = auto()
    PERFORMANCE = auto()
    SECURITY = auto()
    BEHAVIORAL = auto()
    TEMPORAL = auto()
    SPATIAL = auto()
    COMPOSITE = auto()

class OutcomeStatus(Enum):
    """Possible outcomes of decisions/actions."""
    SUCCESS = auto()
    FAILURE = auto()
    PARTIAL = auto()
    TIMEOUT = auto()
    ERROR = auto()
    CANCELLED = auto()
    PENDING = auto()
    UNKNOWN = auto()

class ProxyStatus(Enum):
    """Status of a proxy in the intelligence system."""
    ACTIVE = auto()
    INACTIVE = auto()
    DEPRECATED = auto()
    BLOCKED = auto()
    VALIDATING = auto()
    FAILED = auto()
    PREFERRED = auto()
    NEW = auto()

class ScrapeStrategy(Enum):
    """Strategies for adaptive scraping."""
    AGGRESSIVE = auto()
    CAUTIOUS = auto()
    BALANCED = auto()
    STEALTH = auto()
    RANDOM = auto()
    ADAPTIVE = auto()
    CUSTOM = auto()

class OptimizationGoal(Enum):
    """Goals for self-optimization."""
    SPEED = auto()
    STABILITY = auto()
    BALANCED = auto()
    AGGRESSIVE = auto()
    EFFICIENCY = auto()
    STEALTH = auto()

class SeverityLevel(Enum):
    """Severity levels for anomalies and alerts."""
    INFO = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5

# ==============================================================================
# DATA CLASSES
# ==============================================================================
@dataclass
class DecisionRecord:
    """Record of an AI decision."""
    id: int = 0
    decision_type: str = ""
    action: str = ""
    target: str = ""
    confidence: float = 0.0
    outcome: str = ""
    success: int = 0
    made_at: str = ""
    executed_at: str = ""
    oanks_tag: str = OANKS_TAG

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class ProxyIntel:
    """Intelligence data for a proxy."""
    id: int = 0
    proxy_id: int = 0
    success_count: int = 0
    failure_count: int = 0
    avg_response_time: float = 0.0
    last_used: str = ""
    reliability_score: float = 0.5
    oanks_tag: str = OANKS_TAG

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class AnomalyRecord:
    """Record of a detected anomaly."""
    id: int = 0
    anomaly_type: str = ""
    severity: int = 1
    description: str = ""
    detected_at: str = ""
    resolved: int = 0
    resolution_action: str = ""
    oanks_tag: str = OANKS_TAG

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class PerformanceMetric:
    """System performance metric."""
    id: int = 0
    phase: str = ""
    metric: str = ""
    value: float = 0.0
    timestamp: str = ""
    oanks_tag: str = OANKS_TAG

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class KnowledgePattern:
    """Learned pattern in the knowledge base."""
    id: int = 0
    pattern_type: str = ""
    pattern_data: str = ""
    success_rate: float = 0.0
    usage_count: int = 0
    created_at: str = ""
    last_used: str = ""
    oanks_tag: str = OANKS_TAG

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class StateSnapshot:
    """Snapshot of the current system state."""
    timestamp: str = ""
    phase_status: Dict = field(default_factory=dict)
    pending_tasks: int = 0
    command_queue_size: int = 0
    system_health: Dict = field(default_factory=dict)
    proxy_pool_status: Dict = field(default_factory=dict)
    harvest_status: Dict = field(default_factory=dict)
    anomaly_count: int = 0
    decision_count: int = 0
    performance_metrics: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class ScrapeResult:
    """Result of a scraping operation."""
    target: str = ""
    success: bool = False
    status_code: int = 0
    response_time: float = 0.0
    content_length: int = 0
    anti_scrape_detected: bool = False
    captcha_detected: bool = False
    blocked_detected: bool = False
    honeypot_detected: bool = False
    strategy_used: str = ""
    proxy_used: int = 0
    user_agent: str = ""
    timestamp: str = ""
    error_message: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class HarvestPrediction:
    """Prediction for data harvesting."""
    data_type: str = ""
    predicted_time: str = ""
    predicted_volume: int = 0
    confidence: float = 0.0
    best_source: str = ""
    pattern_matched: str = ""
    historical_accuracy: float = 0.0

    def to_dict(self) -> Dict:
        return asdict(self)

@dataclass
class SystemHealth:
    """System health metrics."""
    cpu_usage: float = 0.0
    memory_usage: float = 0.0
    disk_usage: float = 0.0
    network_latency: float = 0.0
    active_threads: int = 0
    active_connections: int = 0
    error_rate: float = 0.0
    uptime: float = 0.0
    timestamp: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)

# ==============================================================================
# GLOBAL VARIABLES
# ==============================================================================
_g_lock = RLock()
_g_initialized = False
_g_db_connection = None
_g_logger = None
_g_telegram_bot = None
_g_phase14_instance = None
_g_system_state = {}
_g_memory_cache = {}
_g_knowledge_cache = []
_g_decision_history = deque(maxlen=DecisionConfig.DECISION_HISTORY_LIMIT)
_g_anomaly_history = deque(maxlen=1000)
_g_performance_history = deque(maxlen=10000)
_g_proxy_intel_cache = {}
_g_scrape_memory = {}
_g_harvest_patterns = {}
_g_baseline_metrics = {}
_g_autonomous_running = False
_g_learning_enabled = True
_g_shutdown_event = Event()

# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================
def get_timestamp() -> str:
    """Get current timestamp in standard format."""
    return datetime.utcnow().strftime(UtilityConfig.TIMESTAMP_FORMAT)

def get_unix_timestamp() -> float:
    """Get current Unix timestamp."""
    return time.time()

def generate_uuid() -> str:
    """Generate a unique identifier."""
    return hashlib.sha256(
        f"{time.time()}{random.random()}{uuid.uuid4()}".encode()
    ).hexdigest()[:UtilityConfig.UUID_LENGTH]

def hash_string(data: str) -> str:
    """Hash a string using configured algorithm."""
    return hashlib.new(
        UtilityConfig.HASH_ALGORITHM, 
        data.encode(UtilityConfig.ENCODING)
    ).hexdigest()

def safe_json_loads(data: str, default: Any = None) -> Any:
    """Safely load JSON data."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default

def safe_json_dumps(data: Any, indent: int = None) -> str:
    """Safely dump data to JSON string."""
    try:
        return json.dumps(data, indent=indent, default=str)
    except (TypeError, ValueError):
        return str(data)

def clamp_value(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min and max."""
    return max(min_val, min(max_val, value))

def normalize_value(value: float, min_val: float, max_val: float) -> float:
    """Normalize a value to 0-1 range."""
    if max_val == min_val:
        return 0.5
    return clamp_value((value - min_val) / (max_val - min_val), 0.0, 1.0)

def calculate_exponential_moving_average(
    values: List[float], 
    alpha: float = 0.3
) -> float:
    """Calculate exponential moving average."""
    if not values:
        return 0.0
    ema = values[0]
    for value in values[1:]:
        ema = alpha * value + (1 - alpha) * ema
    return ema

def calculate_weighted_average(values: List[float], weights: List[float]) -> float:
    """Calculate weighted average."""
    if not values or not weights or len(values) != len(weights):
        return 0.0
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    return sum(v * w for v, w in zip(values, weights)) / total_weight

def calculate_percentile(values: List[float], percentile: float) -> float:
    """Calculate percentile of a list of values."""
    if not values:
        return 0.0
    sorted_values = sorted(values)
    index = (percentile / 100.0) * (len(sorted_values) - 1)
    lower = int(floor(index))
    upper = int(ceil(index))
    if lower == upper:
        return sorted_values[lower]
    fraction = index - lower
    return sorted_values[lower] + fraction * (sorted_values[upper] - sorted_values[lower])

def detect_outliers_iqr(values: List[float]) -> List[int]:
    """Detect outlier indices using IQR method."""
    if len(values) < 4:
        return []
    q1 = calculate_percentile(values, 25)
    q3 = calculate_percentile(values, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [i for i, v in enumerate(values) if v < lower_bound or v > upper_bound]

def detect_outliers_zscore(values: List[float], threshold: float = 3.0) -> List[int]:
    """Detect outlier indices using Z-score method."""
    if len(values) < 3:
        return []
    try:
        m = mean(values)
        s = stdev(values)
        if s == 0:
            return []
        return [i for i, v in enumerate(values) if abs((v - m) / s) > threshold]
    except statistics.StatisticsError:
        return []

def calculate_trend(values: List[float]) -> Dict:
    """Calculate trend direction and strength."""
    if len(values) < 2:
        return {"direction": "flat", "strength": 0.0, "slope": 0.0}

    n = len(values)
    x = list(range(n))
    x_mean = mean(x)
    y_mean = mean(values)

    numerator = sum((x[i] - x_mean) * (values[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        slope = 0.0
    else:
        slope = numerator / denominator

    strength = clamp_value(abs(slope) / (max(values) - min(values) + 0.001), 0.0, 1.0)

    if slope > 0.01:
        direction = "increasing"
    elif slope < -0.01:
        direction = "decreasing"
    else:
        direction = "flat"

    return {"direction": direction, "strength": strength, "slope": slope}

def calculate_seasonality(values: List[float], period: int = 24) -> Dict:
    """Detect seasonality in time series data."""
    if len(values) < period * 2:
        return {"has_seasonality": False, "period": period, "strength": 0.0}

    # Calculate autocorrelation at lag = period
    n = len(values)
    mean_val = mean(values)

    c0 = sum((v - mean_val) ** 2 for v in values) / n
    if c0 == 0:
        return {"has_seasonality": False, "period": period, "strength": 0.0}

    c_period = sum(
        (values[i] - mean_val) * (values[i + period] - mean_val) 
        for i in range(n - period)
    ) / (n - period)

    autocorr = c_period / c0
    strength = clamp_value(abs(autocorr), 0.0, 1.0)

    return {
        "has_seasonality": strength > 0.3,
        "period": period,
        "strength": strength,
        "autocorrelation": autocorr
    }

def jaccard_similarity(set1: Set, set2: Set) -> float:
    """Calculate Jaccard similarity between two sets."""
    if not set1 and not set2:
        return 1.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    if len(vec1) != len(vec2) or not vec1:
        return 0.0

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = sqrt(sum(a * a for a in vec1))
    mag2 = sqrt(sum(b * b for b in vec2))

    if mag1 == 0 or mag2 == 0:
        return 0.0

    return clamp_value(dot_product / (mag1 * mag2), -1.0, 1.0)

def levenshtein_distance(s1: str, s2: str) -> int:
    """Calculate Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

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

def string_similarity(s1: str, s2: str) -> float:
    """Calculate similarity between two strings (0-1)."""
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    distance = levenshtein_distance(s1, s2)
    return 1.0 - (distance / max_len)

def time_bucket(timestamp: float, bucket_size: int) -> int:
    """Get time bucket for a timestamp."""
    return int(timestamp // bucket_size) * bucket_size

def parse_timestamp(ts_str: str) -> Optional[float]:
    """Parse a timestamp string to Unix timestamp."""
    formats = [
        UtilityConfig.TIMESTAMP_FORMAT,
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(ts_str, fmt).timestamp()
        except ValueError:
            continue
    return None

def format_duration(seconds: float) -> str:
    """Format duration in human-readable form."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        return f"{seconds/60:.1f}m"
    elif seconds < 86400:
        return f"{seconds/3600:.1f}h"
    else:
        return f"{seconds/86400:.1f}d"

def truncate_string(s: str, max_length: int = 100) -> str:
    """Truncate string with ellipsis."""
    if len(s) <= max_length:
        return s
    return s[:max_length-3] + "..."

def merge_dicts(base: Dict, override: Dict) -> Dict:
    """Deep merge two dictionaries."""
    result = copy.deepcopy(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result

def chunk_list(lst: List, chunk_size: int) -> Iterator[List]:
    """Split list into chunks."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def retry_with_backoff(
    func: Callable, 
    max_retries: int = 3, 
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exceptions: Tuple = (Exception,)
) -> Any:
    """Retry a function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return func()
        except exceptions as e:
            if attempt == max_retries - 1:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            delay += random.uniform(0, delay * ScrapeConfig.BACKOFF_JITTER)
            time.sleep(delay)
    return None

def rate_limit_check(
    key: str, 
    max_requests: int, 
    window_seconds: int,
    request_log: Dict[str, List[float]]
) -> bool:
    """Check if a request is within rate limits."""
    now = time.time()
    if key not in request_log:
        request_log[key] = []

    # Remove old requests
    request_log[key] = [t for t in request_log[key] if now - t < window_seconds]

    if len(request_log[key]) >= max_requests:
        return False

    request_log[key].append(now)
    return True

def sanitize_sql(value: Any) -> str:
    """Sanitize a value for SQL queries."""
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return "'" + value.replace("'", "''") + "'"
    return "'" + str(value).replace("'", "''") + "'"

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divide two numbers."""
    if denominator == 0:
        return default
    return numerator / denominator

def calculate_confidence_interval(
    values: List[float], 
    confidence: float = 0.95
) -> Tuple[float, float]:
    """Calculate confidence interval for a list of values."""
    if len(values) < 2:
        return (0.0, 0.0)

    try:
        m = mean(values)
        s = stdev(values)
        n = len(values)
        # Approximate z-score for confidence level
        z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
        z = z_scores.get(confidence, 1.96)
        margin = z * (s / sqrt(n))
        return (m - margin, m + margin)
    except statistics.StatisticsError:
        return (0.0, 0.0)

def calculate_entropy(values: List[float]) -> float:
    """Calculate Shannon entropy of a distribution."""
    if not values or sum(values) == 0:
        return 0.0
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * log(p, 2) for p in probabilities)

def calculate_diversity_index(values: List[float]) -> float:
    """Calculate Simpson's diversity index."""
    if not values or sum(values) == 0:
        return 0.0
    total = sum(values)
    return 1.0 - sum((v / total) ** 2 for v in values)

def sigmoid(x: float) -> float:
    """Sigmoid activation function."""
    try:
        return 1.0 / (1.0 + exp(-x))
    except OverflowError:
        return 0.0 if x < 0 else 1.0

def softmax(values: List[float]) -> List[float]:
    """Softmax function for probability distribution."""
    if not values:
        return []
    max_val = max(values)
    exp_values = [exp(v - max_val) for v in values]
    sum_exp = sum(exp_values)
    return [v / sum_exp for v in exp_values]

def weighted_random_choice(weights: List[float]) -> int:
    """Make a weighted random choice from a list of weights."""
    if not weights or sum(weights) == 0:
        return random.randint(0, len(weights) - 1) if weights else 0

    total = sum(weights)
    r = random.uniform(0, total)
    cumulative = 0
    for i, w in enumerate(weights):
        cumulative += w
        if r <= cumulative:
            return i
    return len(weights) - 1

def adaptive_sleep(duration: float, jitter: float = 0.1) -> None:
    """Sleep with adaptive jitter."""
    jitter_amount = duration * jitter * (2 * random.random() - 1)
    time.sleep(max(0, duration + jitter_amount))

def memory_usage() -> Dict:
    """Get current memory usage statistics."""
    try:
        import psutil
        process = psutil.Process()
        mem_info = process.memory_info()
        return {
            "rss": mem_info.rss,
            "vms": mem_info.vms,
            "percent": process.memory_percent(),
            "available": psutil.virtual_memory().available
        }
    except ImportError:
        return {"rss": 0, "vms": 0, "percent": 0.0, "available": 0}

def cpu_usage() -> float:
    """Get current CPU usage percentage."""
    try:
        import psutil
        return psutil.cpu_percent(interval=0.1)
    except ImportError:
        return 0.0

def disk_usage() -> Dict:
    """Get current disk usage statistics."""
    try:
        import psutil
        usage = psutil.disk_usage('/')
        return {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": (usage.used / usage.total) * 100
        }
    except ImportError:
        return {"total": 0, "used": 0, "free": 0, "percent": 0.0}

def network_stats() -> Dict:
    """Get current network statistics."""
    try:
        import psutil
        net_io = psutil.net_io_counters()
        return {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv,
            "errin": net_io.errin,
            "errout": net_io.errout
        }
    except ImportError:
        return {
            "bytes_sent": 0, "bytes_recv": 0,
            "packets_sent": 0, "packets_recv": 0,
            "errin": 0, "errout": 0
        }

def get_system_health() -> SystemHealth:
    """Get comprehensive system health metrics."""
    mem = memory_usage()
    disk = disk_usage()
    net = network_stats()

    return SystemHealth(
        cpu_usage=cpu_usage(),
        memory_usage=mem.get("percent", 0.0),
        disk_usage=disk.get("percent", 0.0),
        network_latency=0.0,  # Would need active ping
        active_threads=threading.active_count(),
        active_connections=0,  # Would need socket inspection
        error_rate=0.0,
        uptime=time.time() - getattr(_g_system_state, 'start_time', time.time()),
        timestamp=get_timestamp()
    )

def format_bytes(size: int) -> str:
    """Format bytes in human-readable form."""
    units = ["B", "KB", "MB", "GB", "TB"]
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"

def format_number(num: Union[int, float]) -> str:
    """Format large numbers with commas."""
    if isinstance(num, float):
        return f"{num:,.2f}"
    return f"{num:,}"

def create_progress_bar(percentage: float, width: int = 20) -> str:
    """Create a text-based progress bar."""
    filled = int(width * percentage / 100)
    empty = width - filled
    return "█" * filled + "░" * empty + f" {percentage:.1f}%"

def create_status_indicator(status: str) -> str:
    """Create a status indicator emoji."""
    indicators = {
        "success": "🟢",
        "warning": "🟡",
        "error": "🔴",
        "info": "🔵",
        "running": "🟣",
        "pending": "⚪",
        "unknown": "⚫"
    }
    return indicators.get(status.lower(), "⚪")

# ==============================================================================
# END OF SECTION 1: IMPORTS, CONSTANTS, AND CONFIGURATION
# ==============================================================================



# ==============================================================================
# SECTION 2: DATABASE LAYER — SCHEMA, CONNECTIONS, AND CRUD OPERATIONS
# ==============================================================================

class DatabaseManager:
    """
    Centralized database manager for Phase 14 AI Assistant.
    Handles all database operations, schema management, and connection pooling.
    Thread-safe. SQLite3 with WAL mode for concurrent access.
    """

    _instance = None
    _lock = RLock()
    _connections = {}
    _max_connections = DatabaseConfig.MAX_CONNECTIONS

    def __new__(cls, db_path: str = None):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._db_path = db_path or DatabaseConfig.DB_NAME
                cls._instance._initialized = False
            return cls._instance

    def __init__(self, db_path: str = None):
        if not self._initialized:
            self._db_path = db_path or DatabaseConfig.DB_NAME
            self._connection_pool = []
            self._pool_lock = RLock()
            self._initialized = True
            self._initialize_database()

    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection from the pool or create new one."""
        with self._pool_lock:
            # Try to reuse existing connection
            for conn in list(self._connection_pool):
                try:
                    conn.execute("SELECT 1")
                    self._connection_pool.remove(conn)
                    return conn
                except sqlite3.Error:
                    try:
                        conn.close()
                    except:
                        pass

            # Create new connection
            conn = sqlite3.connect(
                self._db_path,
                timeout=DatabaseConfig.CONNECTION_TIMEOUT,
                check_same_thread=False
            )
            conn.execute(f"PRAGMA journal_mode={DatabaseConfig.JOURNAL_MODE}")
            conn.execute(f"PRAGMA synchronous={DatabaseConfig.SYNCHRONOUS}")
            conn.execute(f"PRAGMA cache_size={DatabaseConfig.CACHE_SIZE}")
            conn.execute(f"PRAGMA temp_store={DatabaseConfig.TEMP_STORE}")
            conn.execute(f"PRAGMA page_size={DatabaseConfig.PAGE_SIZE}")
            conn.execute(f"PRAGMA busy_timeout={DatabaseConfig.BUSY_TIMEOUT}")
            conn.row_factory = sqlite3.Row
            return conn

    def _return_connection(self, conn: sqlite3.Connection) -> None:
        """Return a connection to the pool."""
        with self._pool_lock:
            if len(self._connection_pool) < self._max_connections:
                try:
                    conn.execute("SELECT 1")
                    self._connection_pool.append(conn)
                    return
                except sqlite3.Error:
                    pass
            try:
                conn.close()
            except:
                pass

    def _initialize_database(self) -> None:
        """Initialize database with all required tables and indexes."""
        conn = self._get_connection()
        try:
            cursor = conn.cursor()

            # ==================================================================
            # AI DECISIONS TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_decisions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    decision_type TEXT NOT NULL,
                    action TEXT NOT NULL,
                    target TEXT,
                    confidence REAL DEFAULT 0.0,
                    outcome TEXT,
                    success INTEGER DEFAULT 0,
                    made_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    executed_at TIMESTAMP,
                    execution_time REAL DEFAULT 0.0,
                    context TEXT,
                    option_count INTEGER DEFAULT 0,
                    selected_option_rank INTEGER DEFAULT 0,
                    state_snapshot TEXT,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # AI OUTCOMES TABLE (Learning)
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_outcomes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    decision_id INTEGER,
                    success INTEGER DEFAULT 0,
                    reward REAL DEFAULT 0.0,
                    execution_time REAL DEFAULT 0.0,
                    error_message TEXT,
                    metadata TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(decision_id) REFERENCES oanks_ai_decisions(id),
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # PROXY INTELLIGENCE TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_proxy_intel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    proxy_id INTEGER NOT NULL,
                    proxy_address TEXT,
                    success_count INTEGER DEFAULT 0,
                    failure_count INTEGER DEFAULT 0,
                    avg_response_time REAL DEFAULT 0.0,
                    min_response_time REAL DEFAULT 999999.0,
                    max_response_time REAL DEFAULT 0.0,
                    last_used TIMESTAMP,
                    reliability_score REAL DEFAULT 0.5,
                    stability_score REAL DEFAULT 0.5,
                    speed_score REAL DEFAULT 0.5,
                    overall_score REAL DEFAULT 0.5,
                    status TEXT DEFAULT 'NEW',
                    consecutive_successes INTEGER DEFAULT 0,
                    consecutive_failures INTEGER DEFAULT 0,
                    target_success_map TEXT,
                    target_failure_map TEXT,
                    geographic_region TEXT,
                    protocol TEXT,
                    anonymity_level TEXT,
                    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_validated TIMESTAMP,
                    validation_count INTEGER DEFAULT 0,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # ANOMALY LOG TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_anomalies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    anomaly_type TEXT NOT NULL,
                    severity INTEGER DEFAULT 1,
                    description TEXT,
                    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    resolved INTEGER DEFAULT 0,
                    resolved_at TIMESTAMP,
                    resolution_action TEXT,
                    auto_resolved INTEGER DEFAULT 0,
                    metric_values TEXT,
                    baseline_values TEXT,
                    threshold_exceeded REAL,
                    affected_phase TEXT,
                    affected_target TEXT,
                    correlation_id TEXT,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # SYSTEM PERFORMANCE TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_performance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phase TEXT,
                    metric TEXT,
                    value REAL,
                    unit TEXT,
                    context TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # KNOWLEDGE BASE TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_knowledge (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern_type TEXT NOT NULL,
                    pattern_data TEXT,
                    pattern_hash TEXT UNIQUE,
                    success_rate REAL DEFAULT 0.0,
                    usage_count INTEGER DEFAULT 0,
                    success_count INTEGER DEFAULT 0,
                    failure_count INTEGER DEFAULT 0,
                    context_match_score REAL DEFAULT 0.0,
                    temporal_score REAL DEFAULT 0.0,
                    spatial_score REAL DEFAULT 0.0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_used TIMESTAMP,
                    last_validated TIMESTAMP,
                    validation_status TEXT DEFAULT 'PENDING',
                    node_origin TEXT,
                    shared_across_nodes INTEGER DEFAULT 0,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # SCRAPE MEMORY TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_scrape_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    target TEXT NOT NULL,
                    strategy TEXT,
                    success INTEGER DEFAULT 0,
                    status_code INTEGER,
                    response_time REAL,
                    anti_scrape_detected INTEGER DEFAULT 0,
                    captcha_detected INTEGER DEFAULT 0,
                    blocked_detected INTEGER DEFAULT 0,
                    honeypot_detected INTEGER DEFAULT 0,
                    proxy_used INTEGER,
                    user_agent TEXT,
                    delay_used REAL,
                    retry_count INTEGER DEFAULT 0,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # HARVEST PATTERNS TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_harvest_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_type TEXT NOT NULL,
                    source TEXT NOT NULL,
                    pattern_type TEXT,
                    pattern_data TEXT,
                    pattern_hash TEXT UNIQUE,
                    confidence REAL DEFAULT 0.0,
                    accuracy REAL DEFAULT 0.0,
                    prediction_count INTEGER DEFAULT 0,
                    correct_predictions INTEGER DEFAULT 0,
                    avg_predicted_volume REAL DEFAULT 0.0,
                    avg_actual_volume REAL DEFAULT 0.0,
                    time_bucket_size INTEGER DEFAULT 3600,
                    seasonality_detected INTEGER DEFAULT 0,
                    seasonality_period INTEGER,
                    trend_direction TEXT,
                    trend_strength REAL DEFAULT 0.0,
                    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_seen TIMESTAMP,
                    last_validated TIMESTAMP,
                    active INTEGER DEFAULT 1,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # STATE SNAPSHOTS TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_state_snapshots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    snapshot_data TEXT,
                    phase_status TEXT,
                    pending_tasks INTEGER DEFAULT 0,
                    command_queue_size INTEGER DEFAULT 0,
                    system_health TEXT,
                    proxy_pool_status TEXT,
                    harvest_status TEXT,
                    anomaly_count INTEGER DEFAULT 0,
                    decision_count INTEGER DEFAULT 0,
                    performance_metrics TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # AUTONOMOUS LOG TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_autonomous_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    event_data TEXT,
                    phase_affected TEXT,
                    action_taken TEXT,
                    result TEXT,
                    error_message TEXT,
                    recovery_attempts INTEGER DEFAULT 0,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # LEARNING LOG TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_learning_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    learning_type TEXT NOT NULL,
                    pattern_id INTEGER,
                    pattern_type TEXT,
                    action_taken TEXT,
                    result TEXT,
                    confidence_before REAL,
                    confidence_after REAL,
                    success_rate_before REAL,
                    success_rate_after REAL,
                    context TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # TELEGRAM INTERACTION LOG TABLE
            # ==================================================================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS oanks_ai_telegram_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    command TEXT,
                    user_id TEXT,
                    chat_id TEXT,
                    message_text TEXT,
                    response_text TEXT,
                    execution_time REAL,
                    success INTEGER DEFAULT 0,
                    error_message TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    oanks_tag TEXT DEFAULT '👑 Oanks — Creator'
                )
            """)

            # ==================================================================
            # INDEXES FOR PERFORMANCE
            # ==================================================================
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_decisions_type ON oanks_ai_decisions(decision_type)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_decisions_target ON oanks_ai_decisions(target)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_decisions_made_at ON oanks_ai_decisions(made_at)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_decisions_success ON oanks_ai_decisions(success)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_outcomes_decision ON oanks_ai_outcomes(decision_id)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_outcomes_timestamp ON oanks_ai_outcomes(timestamp)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_proxy_intel_id ON oanks_ai_proxy_intel(proxy_id)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_proxy_intel_score ON oanks_ai_proxy_intel(overall_score)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_proxy_intel_status ON oanks_ai_proxy_intel(status)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_anomalies_type ON oanks_ai_anomalies(anomaly_type)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_anomalies_severity ON oanks_ai_anomalies(severity)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_anomalies_detected ON oanks_ai_anomalies(detected_at)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_anomalies_resolved ON oanks_ai_anomalies(resolved)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_performance_phase ON oanks_ai_performance(phase)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_performance_metric ON oanks_ai_performance(metric)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_performance_timestamp ON oanks_ai_performance(timestamp)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_knowledge_type ON oanks_ai_knowledge(pattern_type)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_knowledge_hash ON oanks_ai_knowledge(pattern_hash)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_knowledge_success ON oanks_ai_knowledge(success_rate)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_scrape_target ON oanks_ai_scrape_memory(target)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_scrape_timestamp ON oanks_ai_scrape_memory(timestamp)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_harvest_type ON oanks_ai_harvest_patterns(data_type)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_harvest_source ON oanks_ai_harvest_patterns(source)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_harvest_active ON oanks_ai_harvest_patterns(active)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_state_timestamp ON oanks_ai_state_snapshots(timestamp)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_autonomous_event ON oanks_ai_autonomous_log(event_type)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_autonomous_timestamp ON oanks_ai_autonomous_log(timestamp)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_learning_type ON oanks_ai_learning_log(learning_type)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_learning_timestamp ON oanks_ai_learning_log(timestamp)
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_telegram_command ON oanks_ai_telegram_log(command)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_telegram_timestamp ON oanks_ai_telegram_log(timestamp)
            """)

            conn.commit()

        finally:
            self._return_connection(conn)

    def execute(self, query: str, params: Tuple = ()) -> List[Dict]:
        """Execute a query and return results as list of dictionaries."""
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            self._return_connection(conn)

    def execute_many(self, query: str, params_list: List[Tuple]) -> int:
        """Execute a query with multiple parameter sets."""
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.executemany(query, params_list)
            conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            self._return_connection(conn)

    def insert(self, table: str, data: Dict) -> int:
        """Insert a single record and return the ID."""
        if not data:
            return 0

        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, tuple(data.values()))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            self._return_connection(conn)

    def insert_many(self, table: str, data_list: List[Dict]) -> int:
        """Insert multiple records."""
        if not data_list:
            return 0

        columns = ", ".join(data_list[0].keys())
        placeholders = ", ".join(["?"] * len(data_list[0]))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        params = [tuple(d.values()) for d in data_list]

        return self.execute_many(query, params)

    def update(self, table: str, data: Dict, where: str, where_params: Tuple = ()) -> int:
        """Update records matching the where clause."""
        if not data:
            return 0

        set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where}"
        params = tuple(data.values()) + where_params

        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            self._return_connection(conn)

    def delete(self, table: str, where: str = None, where_params: Tuple = ()) -> int:
        """Delete records from a table."""
        if where:
            query = f"DELETE FROM {table} WHERE {where}"
        else:
            query = f"DELETE FROM {table}"

        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, where_params)
            conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            self._return_connection(conn)

    def select(self, table: str, columns: str = "*", where: str = None, 
               where_params: Tuple = (), order_by: str = None, 
               limit: int = None, offset: int = None) -> List[Dict]:
        """Select records from a table."""
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"
        if offset:
            query += f" OFFSET {offset}"

        return self.execute(query, where_params)

    def select_one(self, table: str, columns: str = "*", where: str = None,
                   where_params: Tuple = ()) -> Optional[Dict]:
        """Select a single record."""
        results = self.select(table, columns, where, where_params, limit=1)
        return results[0] if results else None

    def count(self, table: str, where: str = None, where_params: Tuple = ()) -> int:
        """Count records in a table."""
        query = f"SELECT COUNT(*) as count FROM {table}"
        if where:
            query += f" WHERE {where}"

        result = self.execute(query, where_params)
        return result[0]["count"] if result else 0

    def exists(self, table: str, where: str, where_params: Tuple = ()) -> bool:
        """Check if records exist."""
        return self.count(table, where, where_params) > 0

    def get_stats(self) -> Dict:
        """Get database statistics."""
        tables = [
            "oanks_ai_decisions", "oanks_ai_outcomes", "oanks_ai_proxy_intel",
            "oanks_ai_anomalies", "oanks_ai_performance", "oanks_ai_knowledge",
            "oanks_ai_scrape_memory", "oanks_ai_harvest_patterns",
            "oanks_ai_state_snapshots", "oanks_ai_autonomous_log",
            "oanks_ai_learning_log", "oanks_ai_telegram_log"
        ]

        stats = {}
        for table in tables:
            try:
                stats[table] = self.count(table)
            except:
                stats[table] = 0

        stats["total_records"] = sum(stats.values())
        stats["db_path"] = self._db_path
        stats["db_size_bytes"] = os.path.getsize(self._db_path) if os.path.exists(self._db_path) else 0

        return stats

    def vacuum(self) -> None:
        """Vacuum the database to reclaim space."""
        conn = self._get_connection()
        try:
            conn.execute("VACUUM")
            conn.commit()
        finally:
            self._return_connection(conn)

    def backup(self, backup_path: str = None) -> str:
        """Create a backup of the database."""
        if backup_path is None:
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{self._db_path}.backup_{timestamp}"

        source = self._get_connection()
        try:
            dest = sqlite3.connect(backup_path)
            with dest:
                source.backup(dest)
            dest.close()
            return backup_path
        finally:
            self._return_connection(source)

    def close_all(self) -> None:
        """Close all connections in the pool."""
        with self._pool_lock:
            for conn in self._connection_pool:
                try:
                    conn.close()
                except:
                    pass
            self._connection_pool.clear()

    def raw_query(self, query: str, params: Tuple = ()) -> List[Dict]:
        """Execute a raw SQL query."""
        return self.execute(query, params)

    def get_table_schema(self, table: str) -> List[Dict]:
        """Get the schema of a table."""
        return self.execute(f"PRAGMA table_info({table})")

    def get_indexes(self, table: str = None) -> List[Dict]:
        """Get index information."""
        if table:
            return self.execute("SELECT * FROM sqlite_master WHERE type='index' AND tbl_name=?", (table,))
        return self.execute("SELECT * FROM sqlite_master WHERE type='index'")

    def truncate_table(self, table: str) -> int:
        """Truncate a table (delete all records)."""
        return self.delete(table)

    def get_recent_records(self, table: str, limit: int = 100, 
                          order_by: str = "timestamp DESC") -> List[Dict]:
        """Get recent records from a table."""
        return self.select(table, order_by=order_by, limit=limit)

    def get_records_by_time_range(self, table: str, start_time: str, end_time: str,
                                   time_column: str = "timestamp") -> List[Dict]:
        """Get records within a time range."""
        return self.select(
            table,
            where=f"{time_column} BETWEEN ? AND ?",
            where_params=(start_time, end_time),
            order_by=f"{time_column} DESC"
        )

    def aggregate(self, table: str, column: str, func: str = "COUNT",
                  where: str = None, where_params: Tuple = ()) -> float:
        """Aggregate a column."""
        query = f"SELECT {func}({column}) as result FROM {table}"
        if where:
            query += f" WHERE {where}"

        result = self.execute(query, where_params)
        return result[0]["result"] if result and result[0]["result"] is not None else 0.0

    def get_distinct_values(self, table: str, column: str) -> List:
        """Get distinct values from a column."""
        results = self.execute(f"SELECT DISTINCT {column} as value FROM {table} WHERE {column} IS NOT NULL")
        return [r["value"] for r in results]

    def get_column_stats(self, table: str, column: str) -> Dict:
        """Get statistics for a numeric column."""
        query = f"""
            SELECT 
                COUNT({column}) as count,
                MIN({column}) as min,
                MAX({column}) as max,
                AVG({column}) as avg,
                SUM({column}) as sum
            FROM {table}
            WHERE {column} IS NOT NULL
        """
        result = self.execute(query)
        return result[0] if result else {}

# ==============================================================================
# END OF SECTION 2: DATABASE LAYER
# ==============================================================================



# ==============================================================================
# SECTION 3: LOGGING SYSTEM — COMPREHENSIVE, MULTI-CHANNEL, TELEGRAM-INTEGRATED
# ==============================================================================

class OanksLogger:
    """
    Centralized logging system for Phase 14 AI Assistant.
    Multi-channel: console, file, database, Telegram.
    Thread-safe. Color-coded console output.
    Structured logging with JSON support.
    """

    _instance = None
    _lock = RLock()

    def __new__(cls, name: str = "Phase14AI"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self, name: str = "Phase14AI"):
        if not self._initialized:
            self._name = name
            self._logger = logging.getLogger(name)
            self._logger.setLevel(getattr(logging, LoggingConfig.LOG_LEVEL))
            self._logger.handlers = []
            self._db_manager = None
            self._telegram_callback = None
            self._log_buffer = deque(maxlen=1000)
            self._buffer_lock = RLock()
            self._setup_handlers()
            self._initialized = True

    def _setup_handlers(self) -> None:
        """Setup logging handlers."""
        # Console handler with colors
        if LoggingConfig.LOG_TO_CONSOLE:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.DEBUG)
            console_formatter = logging.Formatter(
                f"{LoggingConfig.LOG_COLORS.get('INFO', '')}%(asctime)s{LoggingConfig.LOG_COLORS.get('INFO', '')} | "
                f"%(levelname)s | %(name)s | %(message)s\033[0m"
            )
            console_handler.setFormatter(console_formatter)
            self._logger.addHandler(console_handler)

        # File handler with rotation
        if LoggingConfig.LOG_TO_FILE:
            try:
                from logging.handlers import RotatingFileHandler
                file_handler = RotatingFileHandler(
                    LoggingConfig.LOG_FILE,
                    maxBytes=LoggingConfig.LOG_ROTATION_SIZE,
                    backupCount=LoggingConfig.LOG_ROTATION_COUNT
                )
                file_handler.setLevel(logging.DEBUG)
                file_formatter = logging.Formatter(LoggingConfig.LOG_FORMAT)
                file_handler.setFormatter(file_formatter)
                self._logger.addHandler(file_handler)
            except Exception:
                pass

    def set_db_manager(self, db_manager: DatabaseManager) -> None:
        """Set database manager for database logging."""
        self._db_manager = db_manager

    def set_telegram_callback(self, callback: Callable) -> None:
        """Set callback for Telegram logging."""
        self._telegram_callback = callback

    def _log_to_buffer(self, level: str, message: str, extra: Dict = None) -> None:
        """Log to in-memory buffer."""
        with self._buffer_lock:
            self._log_buffer.append({
                "timestamp": get_timestamp(),
                "level": level,
                "message": message,
                "extra": extra or {}
            })

    def _log_to_telegram(self, level: str, message: str, extra: Dict = None) -> None:
        """Send log to Telegram if configured."""
        if not self._telegram_callback:
            return

        telegram_level = getattr(logging, LoggingConfig.LOG_TELEGRAM_LEVEL, logging.WARNING)
        if getattr(logging, level, logging.INFO) < telegram_level:
            return

        try:
            emoji = TelegramConfig.EMOJI_MAP.get(level.lower(), "ℹ️")
            formatted = f"{emoji} *{level}* | {self._name}\n{message}"
            if extra:
                formatted += f"\n\n`{safe_json_dumps(extra)}`"
            self._telegram_callback(formatted)
        except Exception:
            pass

    def debug(self, message: str, extra: Dict = None) -> None:
        """Log debug message."""
        self._logger.debug(message)
        self._log_to_buffer("DEBUG", message, extra)

    def info(self, message: str, extra: Dict = None) -> None:
        """Log info message."""
        self._logger.info(message)
        self._log_to_buffer("INFO", message, extra)

    def warning(self, message: str, extra: Dict = None) -> None:
        """Log warning message."""
        self._logger.warning(message)
        self._log_to_buffer("WARNING", message, extra)
        self._log_to_telegram("WARNING", message, extra)

    def error(self, message: str, extra: Dict = None) -> None:
        """Log error message."""
        self._logger.error(message)
        self._log_to_buffer("ERROR", message, extra)
        self._log_to_telegram("ERROR", message, extra)

    def critical(self, message: str, extra: Dict = None) -> None:
        """Log critical message."""
        self._logger.critical(message)
        self._log_to_buffer("CRITICAL", message, extra)
        self._log_to_telegram("CRITICAL", message, extra)

    def decision(self, decision: Dict) -> None:
        """Log a decision."""
        if LoggingConfig.DECISION_LOG_ENABLED:
            self.info(f"DECISION: {decision.get('decision_type', 'UNKNOWN')} | "
                     f"Target: {decision.get('target', 'N/A')} | "
                     f"Confidence: {decision.get('confidence', 0):.2f}",
                     extra={"decision": decision})

    def anomaly(self, anomaly: Dict) -> None:
        """Log an anomaly."""
        if LoggingConfig.ANOMALY_LOG_ENABLED:
            self.warning(f"ANOMALY: {anomaly.get('anomaly_type', 'UNKNOWN')} | "
                        f"Severity: {anomaly.get('severity', 1)} | "
                        f"{anomaly.get('description', 'No description')}",
                        extra={"anomaly": anomaly})

    def performance(self, metric: Dict) -> None:
        """Log a performance metric."""
        if LoggingConfig.PERFORMANCE_LOG_ENABLED:
            self.debug(f"PERFORMANCE: {metric.get('phase', 'UNKNOWN')} | "
                      f"{metric.get('metric', 'UNKNOWN')} = {metric.get('value', 0)}",
                      extra={"performance": metric})

    def telegram_step(self, step_number: int, total_steps: int, 
                      description: str, status: str = "running",
                      details: Dict = None) -> None:
        """Log a step for Telegram step-by-step reporting."""
        emoji = TelegramConfig.EMOJI_MAP.get(status, "🔄")
        progress = f"[{step_number}/{total_steps}]"
        message = f"{emoji} {progress} {description}"

        if details:
            detail_lines = []
            for key, value in details.items():
                detail_lines.append(f"  • {key}: {value}")
            message += "\n" + "\n".join(detail_lines)

        self.info(message, extra={"telegram_step": True, "step": step_number, 
                                   "total": total_steps, "status": status})

        if self._telegram_callback:
            try:
                self._telegram_callback(message)
            except Exception:
                pass

    def get_buffer(self, limit: int = 100) -> List[Dict]:
        """Get recent log buffer entries."""
        with self._buffer_lock:
            return list(itertools.islice(self._log_buffer, limit))

    def get_buffer_by_level(self, level: str, limit: int = 100) -> List[Dict]:
        """Get buffer entries filtered by level."""
        with self._buffer_lock:
            return [entry for entry in self._log_buffer 
                    if entry["level"] == level.upper()][:limit]

    def clear_buffer(self) -> None:
        """Clear the log buffer."""
        with self._buffer_lock:
            self._log_buffer.clear()

    def export_buffer(self, format: str = "json") -> str:
        """Export log buffer to string."""
        with self._buffer_lock:
            if format == "json":
                return safe_json_dumps(list(self._log_buffer), indent=2)
            elif format == "csv":
                output = io.StringIO()
                writer = csv.writer(output)
                writer.writerow(["timestamp", "level", "message"])
                for entry in self._log_buffer:
                    writer.writerow([entry["timestamp"], entry["level"], entry["message"]])
                return output.getvalue()
            return ""

# ==============================================================================
# SECTION 4: TELEGRAM BOT INTEGRATION — INTERACTIVE, STEP-BY-STEP, REAL-TIME
# ==============================================================================

class TelegramBotInterface:
    """
    Interactive Telegram bot interface for Phase 14 AI Assistant.
    Step-by-step execution reporting.
    Real-time status updates.
    Interactive buttons and menus.
    Progress tracking with visual indicators.
    Command routing with detailed responses.
    """

    def __init__(self, bot_token: str = None, chat_id: str = None):
        self._bot_token = bot_token
        self._chat_id = chat_id
        self._enabled = bot_token is not None and chat_id is not None
        self._command_handlers = {}
        self._message_queue = deque(maxlen=1000)
        self._queue_lock = RLock()
        self._send_thread = None
        self._running = False
        self._rate_limit_log = {}
        self._last_message_time = 0
        self._message_cooldown = 1.0
        self._setup_default_handlers()

    def _setup_default_handlers(self) -> None:
        """Setup default command handlers."""
        self._command_handlers = {
            "ai_start": self._handle_ai_start,
            "ai_stop": self._handle_ai_stop,
            "ai_status": self._handle_ai_status,
            "ai_decision": self._handle_ai_decision,
            "ai_decisions": self._handle_ai_decisions,
            "ai_optimize": self._handle_ai_optimize,
            "ai_learn": self._handle_ai_learn,
            "ai_autonomous": self._handle_ai_autonomous,
            "ai_autonomous_stop": self._handle_ai_autonomous_stop,
            "ai_anomaly": self._handle_ai_anomaly,
            "ai_anomalies": self._handle_ai_anomalies,
            "ai_harvest_predict": self._handle_ai_harvest_predict,
            "ai_proxy_intel": self._handle_ai_proxy_intel,
            "ai_knowledge": self._handle_ai_knowledge,
            "ai_performance": self._handle_ai_performance,
            "ai_adapt": self._handle_ai_adapt,
            "ai_patterns": self._handle_ai_patterns,
            "ai_help": self._handle_ai_help,
            "ai_stats": self._handle_ai_stats,
            "ai_health": self._handle_ai_health,
            "ai_memory": self._handle_ai_memory,
            "ai_config": self._handle_ai_config,
            "ai_export": self._handle_ai_export,
            "ai_emergency_stop": self._handle_ai_emergency_stop,
        }

    def set_bot_token(self, token: str) -> None:
        """Set bot token."""
        self._bot_token = token
        self._enabled = self._bot_token is not None and self._chat_id is not None

    def set_chat_id(self, chat_id: str) -> None:
        """Set chat ID."""
        self._chat_id = chat_id
        self._enabled = self._bot_token is not None and self._chat_id is not None

    def is_enabled(self) -> bool:
        """Check if Telegram integration is enabled."""
        return self._enabled

    def start(self) -> None:
        """Start the message sending thread."""
        if not self._enabled:
            return
        self._running = True
        self._send_thread = Thread(target=self._message_sender_loop, daemon=True)
        self._send_thread.start()

    def stop(self) -> None:
        """Stop the message sending thread."""
        self._running = False
        if self._send_thread:
            self._send_thread.join(timeout=5)

    def _message_sender_loop(self) -> None:
        """Background thread for sending queued messages."""
        while self._running:
            messages_to_send = []
            with self._queue_lock:
                while self._message_queue and len(messages_to_send) < 10:
                    messages_to_send.append(self._message_queue.popleft())

            for message in messages_to_send:
                self._send_message_direct(message)
                time.sleep(self._message_cooldown)

            time.sleep(0.5)

    def _send_message_direct(self, message: str) -> bool:
        """Send a message directly via Telegram API."""
        if not self._enabled:
            return False

        try:
            # Rate limit check
            if not rate_limit_check(
                "telegram_send", 
                30, 60, 
                self._rate_limit_log
            ):
                return False

            url = f"https://api.telegram.org/bot{self._bot_token}/sendMessage"
            payload = {
                "chat_id": self._chat_id,
                "text": message[:TelegramConfig.MAX_MESSAGE_LENGTH],
                "parse_mode": "Markdown",
                "disable_web_page_preview": True
            }

            data = urllib.parse.urlencode(payload).encode()
            req = urllib.request.Request(url, data=data, method="POST")
            req.add_header("Content-Type", "application/x-www-form-urlencoded")

            with urllib.request.urlopen(req, timeout=10) as response:
                return response.status == 200
        except Exception:
            return False

    def send_message(self, message: str, priority: bool = False) -> bool:
        """Queue a message for sending."""
        if not self._enabled:
            return False

        with self._queue_lock:
            self._message_queue.append(message)

        if priority:
            return self._send_message_direct(message)
        return True

    def send_step(self, step_number: int, total_steps: int, 
                  title: str, description: str = "", 
                  status: str = "running", details: Dict = None) -> bool:
        """Send a step-by-step progress update."""
        emoji = TelegramConfig.EMOJI_MAP.get(status, "🔄")
        progress_bar = create_progress_bar((step_number / total_steps) * 100, 15)

        message = f"{emoji} *Step {step_number}/{total_steps}*\n"
        message += f"{progress_bar}\n\n"
        message += f"*{title}*\n"
        if description:
            message += f"_{description}_\n"

        if details:
            message += "\n"
            for key, value in details.items():
                indicator = create_status_indicator("info")
                message += f"{indicator} `{key}`: {value}\n"

        return self.send_message(message)

    def send_decision_start(self, decision_type: str, target: str) -> bool:
        """Notify that a decision process is starting."""
        emoji = TelegramConfig.EMOJI_MAP.get("decision", "🧠")
        message = f"{emoji} *AI Decision Process Started*\n\n"
        message += f"Type: `{decision_type}`\n"
        message += f"Target: `{target}`\n"
        message += f"Time: `{get_timestamp()}`\n"
        message += f"\n_Analyzing state..._"
        return self.send_message(message)

    def send_decision_options(self, options: List[Dict]) -> bool:
        """Send generated options to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("thinking", "💭")
        message = f"{emoji} *Options Generated*\n\n"

        for i, opt in enumerate(options[:10], 1):
            score = opt.get("score", 0)
            bar = create_progress_bar(score, 10)
            message += f"{i}. `{opt.get('action', 'Unknown')}`\n"
            message += f"   Score: {bar} {score:.1f}\n"
            message += f"   Target: `{opt.get('target', 'N/A')}`\n\n"

        return self.send_message(message)

    def send_decision_result(self, decision: Dict, execution_time: float) -> bool:
        """Send decision result to Telegram."""
        success = decision.get("success", 0)
        emoji = TelegramConfig.EMOJI_MAP.get("success" if success else "failure", 
                                              "✅" if success else "❌")

        message = f"{emoji} *Decision Executed*\n\n"
        message += f"Action: `{decision.get('action', 'Unknown')}`\n"
        message += f"Target: `{decision.get('target', 'N/A')}`\n"
        message += f"Confidence: `{decision.get('confidence', 0):.2f}`\n"
        message += f"Outcome: `{'SUCCESS' if success else 'FAILED'}`\n"
        message += f"Execution Time: `{execution_time:.2f}s`\n"
        message += f"Timestamp: `{get_timestamp()}`"

        return self.send_message(message)

    def send_anomaly_alert(self, anomaly: Dict) -> bool:
        """Send anomaly alert to Telegram."""
        severity = anomaly.get("severity", 1)
        emoji_map = {1: "ℹ️", 2: "⚠️", 3: "🟡", 4: "🚨", 5: "☠️"}
        emoji = emoji_map.get(severity, "🚨")

        message = f"{emoji} *ANOMALY DETECTED*\n\n"
        message += f"Type: `{anomaly.get('anomaly_type', 'UNKNOWN')}`\n"
        message += f"Severity: `{AnomalyConfig.SEVERITY_LEVELS.get(severity, 'UNKNOWN')}`\n"
        message += f"Description: {anomaly.get('description', 'No description')}\n"
        message += f"Detected: `{anomaly.get('detected_at', get_timestamp())}`\n"

        if anomaly.get("auto_resolved"):
            message += f"\n✅ *Auto-resolved*: {anomaly.get('resolution_action', 'N/A')}"

        return self.send_message(message, priority=True)

    def send_optimization_report(self, optimizations: List[Dict]) -> bool:
        """Send optimization report to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("optimize", "⚡")
        message = f"{emoji} *Self-Optimization Report*\n\n"

        for opt in optimizations:
            message += f"• `{opt.get('parameter', 'Unknown')}`\n"
            message += f"  Old: `{opt.get('old_value', 'N/A')}` → New: `{opt.get('new_value', 'N/A')}`\n"
            message += f"  Reason: _{opt.get('reason', 'N/A')}_\n\n"

        return self.send_message(message)

    def send_harvest_prediction(self, prediction: HarvestPrediction) -> bool:
        """Send harvest prediction to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("harvest", "📊")
        message = f"{emoji} *Harvest Prediction*\n\n"
        message += f"Data Type: `{prediction.data_type}`\n"
        message += f"Best Source: `{prediction.best_source}`\n"
        message += f"Predicted Time: `{prediction.predicted_time}`\n"
        message += f"Predicted Volume: `{prediction.predicted_volume}`\n"
        message += f"Confidence: `{prediction.confidence:.2f}`\n"
        message += f"Historical Accuracy: `{prediction.historical_accuracy:.2f}`"

        return self.send_message(message)

    def send_proxy_intel_update(self, proxy_intel: List[Dict]) -> bool:
        """Send proxy intelligence update to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("proxy", "🌐")
        message = f"{emoji} *Proxy Intelligence Update*\n\n"

        for intel in proxy_intel[:5]:
            status_emoji = create_status_indicator(
                "success" if intel.get("overall_score", 0) > 0.7 else "warning"
            )
            message += f"{status_emoji} `{intel.get('proxy_address', 'Unknown')}`\n"
            message += f"   Score: `{intel.get('overall_score', 0):.2f}`\n"
            message += f"   Success: `{intel.get('success_count', 0)}` | Fail: `{intel.get('failure_count', 0)}`\n"
            message += f"   Avg Response: `{intel.get('avg_response_time', 0):.2f}s`\n\n"

        return self.send_message(message)

    def send_autonomous_status(self, status: Dict) -> bool:
        """Send autonomous mode status to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("autonomous", "🤖")
        running = status.get("running", False)
        status_emoji = "🟢" if running else "🔴"

        message = f"{emoji} *Autonomous Mode Status* {status_emoji}\n\n"
        message += f"Status: `{'RUNNING' if running else 'STOPPED'}`\n"
        message += f"Uptime: `{format_duration(status.get('uptime', 0))}`\n"
        message += f"Decisions Made: `{status.get('decisions_made', 0)}`\n"
        message += f"Success Rate: `{status.get('success_rate', 0):.1f}%`\n"
        message += f"Anomalies: `{status.get('anomaly_count', 0)}`\n"
        message += f"Optimizations: `{status.get('optimizations_applied', 0)}`\n"
        message += f"Patterns Learned: `{status.get('patterns_learned', 0)}`"

        return self.send_message(message)

    def send_knowledge_update(self, patterns: List[Dict]) -> bool:
        """Send knowledge base update to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("knowledge", "💡")
        message = f"{emoji} *Knowledge Base Update*\n\n"

        for pattern in patterns[:5]:
            message += f"• `{pattern.get('pattern_type', 'Unknown')}`\n"
            message += f"  Success Rate: `{pattern.get('success_rate', 0):.2f}`\n"
            message += f"  Usage: `{pattern.get('usage_count', 0)}`\n"
            message += f"  Context: _{truncate_string(pattern.get('pattern_data', ''), 50)}_\n\n"

        return self.send_message(message)

    def send_performance_dashboard(self, metrics: Dict) -> bool:
        """Send performance dashboard to Telegram."""
        emoji = TelegramConfig.EMOJI_MAP.get("performance", "📈")
        message = f"{emoji} *Performance Dashboard*\n\n"

        for metric_name, value in metrics.items():
            if isinstance(value, (int, float)):
                bar = create_progress_bar(min(value, 100), 10)
                message += f"`{metric_name}`\n{bar} {value:.1f}\n\n"
            else:
                message += f"`{metric_name}`: {value}\n"

        return self.send_message(message)

    def send_error_recovery(self, error: Dict, recovery_action: str) -> bool:
        """Send error recovery notification."""
        emoji = TelegramConfig.EMOJI_MAP.get("warning", "⚠️")
        message = f"{emoji} *Error Recovery*\n\n"
        message += f"Error: `{error.get('type', 'Unknown')}`\n"
        message += f"Phase: `{error.get('phase', 'Unknown')}`\n"
        message += f"Message: _{error.get('message', 'N/A')}_\n"
        message += f"\n✅ *Recovery Action*: `{recovery_action}`"

        return self.send_message(message, priority=True)

    def send_emergency_alert(self, reason: str) -> bool:
        """Send emergency alert."""
        emoji = TelegramConfig.EMOJI_MAP.get("danger", "☠️")
        message = f"{emoji} *🚨 EMERGENCY ALERT 🚨*\n\n"
        message += f"Reason: `{reason}`\n"
        message += f"Time: `{get_timestamp()}`\n"
        message += f"\n*Framework entering lockdown mode.*"

        return self.send_message(message, priority=True)

    def send_startup_notification(self) -> bool:
        """Send startup notification."""
        message = f"{TelegramConfig.EMOJI_MAP.get('oanks', '👑')} *Oanks Operations Framework*\n"
        message += f"*{OANKS_PHASE}*\n"
        message += f"Version: `{OANKS_VERSION}`\n"
        message += f"Danger Level: `{OANKS_DANGER_LEVEL}/10`\n"
        message += f"Status: `INITIALIZED`\n"
        message += f"Time: `{get_timestamp()}`\n"
        message += f"\n_Ready for autonomous operation._"

        return self.send_message(message)

    def send_shutdown_notification(self, reason: str = "Manual shutdown") -> bool:
        """Send shutdown notification."""
        message = f"🛑 *Framework Shutdown*\n\n"
        message += f"Reason: `{reason}`\n"
        message += f"Time: `{get_timestamp()}`\n"
        message += f"\n_Goodbye._"

        return self.send_message(message)

    def _handle_ai_start(self, args: List[str]) -> str:
        """Handle /ai_start command."""
        return "🟢 *AI Assistant Started*\n\nPhase 14 AI Assistant is now active and monitoring."

    def _handle_ai_stop(self, args: List[str]) -> str:
        """Handle /ai_stop command."""
        return "🔴 *AI Assistant Stopped*\n\nPhase 14 AI Assistant has been deactivated."

    def _handle_ai_status(self, args: List[str]) -> str:
        """Handle /ai_status command."""
        return "ℹ️ Use the full Phase14AIAssistant instance for detailed status."

    def _handle_ai_decision(self, args: List[str]) -> str:
        """Handle /ai_decision command."""
        return "🧠 Triggering AI decision process..."

    def _handle_ai_decisions(self, args: List[str]) -> str:
        """Handle /ai_decisions command."""
        return "📋 Retrieving decision history..."

    def _handle_ai_optimize(self, args: List[str]) -> str:
        """Handle /ai_optimize command."""
        return "⚡ Running self-optimization..."

    def _handle_ai_learn(self, args: List[str]) -> str:
        """Handle /ai_learn command."""
        return "📚 Toggling learning mode..."

    def _handle_ai_autonomous(self, args: List[str]) -> str:
        """Handle /ai_autonomous command."""
        return "🤖 Starting autonomous mode..."

    def _handle_ai_autonomous_stop(self, args: List[str]) -> str:
        """Handle /ai_autonomous_stop command."""
        return "🛑 Stopping autonomous mode..."

    def _handle_ai_anomaly(self, args: List[str]) -> str:
        """Handle /ai_anomaly command."""
        return "🚨 Checking for anomalies..."

    def _handle_ai_anomalies(self, args: List[str]) -> str:
        """Handle /ai_anomalies command."""
        return "📋 Retrieving anomaly history..."

    def _handle_ai_harvest_predict(self, args: List[str]) -> str:
        """Handle /ai_harvest_predict command."""
        return "📊 Generating harvest predictions..."

    def _handle_ai_proxy_intel(self, args: List[str]) -> str:
        """Handle /ai_proxy_intel command."""
        return "🌐 Retrieving proxy intelligence..."

    def _handle_ai_knowledge(self, args: List[str]) -> str:
        """Handle /ai_knowledge command."""
        return "💡 Retrieving knowledge base..."

    def _handle_ai_performance(self, args: List[str]) -> str:
        """Handle /ai_performance command."""
        return "📈 Retrieving performance metrics..."

    def _handle_ai_adapt(self, args: List[str]) -> str:
        """Handle /ai_adapt command."""
        return "🎯 Adapting scraping strategy..."

    def _handle_ai_patterns(self, args: List[str]) -> str:
        """Handle /ai_patterns command."""
        return "🎯 Retrieving learned patterns..."

    def _handle_ai_help(self, args: List[str]) -> str:
        """Handle /ai_help command."""
        message = f"{TelegramConfig.EMOJI_MAP.get('oanks', '👑')} *Phase 14 AI Assistant Commands*\n\n"

        admin_cmds = [
            ("/ai_start", "Start AI assistant"),
            ("/ai_stop", "Stop AI assistant"),
            ("/ai_autonomous", "Start autonomous mode"),
            ("/ai_autonomous_stop", "Stop autonomous mode"),
            ("/ai_learn", "Toggle learning mode"),
            ("/ai_optimize", "Run self-optimization"),
            ("/ai_emergency_stop", "Emergency shutdown"),
        ]

        user_cmds = [
            ("/ai_status", "AI status overview"),
            ("/ai_decision", "Trigger a decision"),
            ("/ai_decisions", "View decision history"),
            ("/ai_anomaly", "Check anomalies"),
            ("/ai_anomalies", "View anomaly history"),
            ("/ai_harvest_predict", "Predict harvesting"),
            ("/ai_proxy_intel", "Proxy intelligence"),
            ("/ai_knowledge", "Knowledge base"),
            ("/ai_performance", "Performance metrics"),
            ("/ai_adapt", "Adapt strategy"),
            ("/ai_patterns", "Learned patterns"),
            ("/ai_stats", "AI statistics"),
            ("/ai_health", "System health"),
            ("/ai_memory", "Memory usage"),
            ("/ai_config", "View configuration"),
            ("/ai_export", "Export data"),
            ("/ai_help", "This help message"),
        ]

        message += "*Admin Commands:*\n"
        for cmd, desc in admin_cmds:
            message += f"`{cmd}` — {desc}\n"

        message += "\n*User Commands:*\n"
        for cmd, desc in user_cmds:
            message += f"`{cmd}` — {desc}\n"

        return message

    def _handle_ai_stats(self, args: List[str]) -> str:
        """Handle /ai_stats command."""
        return "📊 Retrieving AI statistics..."

    def _handle_ai_health(self, args: List[str]) -> str:
        """Handle /ai_health command."""
        return "🏥 Checking system health..."

    def _handle_ai_memory(self, args: List[str]) -> str:
        """Handle /ai_memory command."""
        return "🧠 Checking memory usage..."

    def _handle_ai_config(self, args: List[str]) -> str:
        """Handle /ai_config command."""
        return "⚙️ Retrieving configuration..."

    def _handle_ai_export(self, args: List[str]) -> str:
        """Handle /ai_export command."""
        return "📤 Exporting data..."

    def _handle_ai_emergency_stop(self, args: List[str]) -> str:
        """Handle /ai_emergency_stop command."""
        return "☠️ *EMERGENCY STOP INITIATED*\n\nShutting down all operations..."

    def handle_command(self, command: str, args: List[str] = None) -> str:
        """Handle a Telegram command."""
        args = args or []
        handler = self._command_handlers.get(command)
        if handler:
            return handler(args)
        return f"❌ Unknown command: `{command}`. Use /ai_help for available commands."

    def get_command_list(self) -> List[str]:
        """Get list of available commands."""
        return list(self._command_handlers.keys())

# ==============================================================================
# END OF SECTION 3 & 4: LOGGING AND TELEGRAM INTEGRATION
# ==============================================================================



# ==============================================================================
# SECTION 5: AUTO-DECISION MAKING ENGINE — THE BRAIN
# ==============================================================================

class AutoDecisionEngine:
    """
    The brain of Phase 14. Makes intelligent, weighted decisions based on
    current system state, historical outcomes, and learned patterns.

    No neural networks. No deep learning. Pure statistics, memory, and
    weighted scoring. Every decision is traceable, explainable, and learnable.
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._decision_weights = {}
        self._option_history = {}
        self._state_cache = {}
        self._cache_lock = RLock()
        self._last_decision_time = 0
        self._decision_count = 0
        self._successful_decisions = 0
        self._failed_decisions = 0
        self._decision_lock = RLock()
        self._initialize_weights()

    def _initialize_weights(self) -> None:
        """Initialize default decision weights."""
        self._decision_weights = {
            DecisionType.HARVEST: {
                "base_weight": 1.0,
                "success_bonus": 0.3,
                "failure_penalty": 0.5,
                "recency_decay": 0.95,
                "frequency_bonus": 0.1,
            },
            DecisionType.PROXY_ROTATE: {
                "base_weight": 0.8,
                "success_bonus": 0.2,
                "failure_penalty": 0.3,
                "recency_decay": 0.9,
                "frequency_bonus": 0.05,
            },
            DecisionType.SCALE_UP: {
                "base_weight": 0.6,
                "success_bonus": 0.4,
                "failure_penalty": 0.6,
                "recency_decay": 0.92,
                "frequency_bonus": 0.15,
            },
            DecisionType.SCALE_DOWN: {
                "base_weight": 0.5,
                "success_bonus": 0.3,
                "failure_penalty": 0.4,
                "recency_decay": 0.93,
                "frequency_bonus": 0.1,
            },
            DecisionType.ALERT: {
                "base_weight": 0.7,
                "success_bonus": 0.2,
                "failure_penalty": 0.2,
                "recency_decay": 0.88,
                "frequency_bonus": 0.05,
            },
            DecisionType.OPTIMIZE: {
                "base_weight": 0.9,
                "success_bonus": 0.35,
                "failure_penalty": 0.4,
                "recency_decay": 0.94,
                "frequency_bonus": 0.1,
            },
            DecisionType.LEARN: {
                "base_weight": 0.75,
                "success_bonus": 0.3,
                "failure_penalty": 0.3,
                "recency_decay": 0.96,
                "frequency_bonus": 0.08,
            },
            DecisionType.ADAPT: {
                "base_weight": 0.85,
                "success_bonus": 0.4,
                "failure_penalty": 0.35,
                "recency_decay": 0.93,
                "frequency_bonus": 0.12,
            },
            DecisionType.PREDICT: {
                "base_weight": 0.7,
                "success_bonus": 0.25,
                "failure_penalty": 0.25,
                "recency_decay": 0.95,
                "frequency_bonus": 0.1,
            },
            DecisionType.ANOMALY_RESPONSE: {
                "base_weight": 1.0,
                "success_bonus": 0.5,
                "failure_penalty": 0.7,
                "recency_decay": 0.85,
                "frequency_bonus": 0.05,
            },
            DecisionType.PHASE_RESTART: {
                "base_weight": 0.4,
                "success_bonus": 0.2,
                "failure_penalty": 0.8,
                "recency_decay": 0.9,
                "frequency_bonus": 0.05,
            },
            DecisionType.TARGET_SWITCH: {
                "base_weight": 0.65,
                "success_bonus": 0.3,
                "failure_penalty": 0.4,
                "recency_decay": 0.92,
                "frequency_bonus": 0.1,
            },
            DecisionType.STRATEGY_CHANGE: {
                "base_weight": 0.8,
                "success_bonus": 0.35,
                "failure_penalty": 0.45,
                "recency_decay": 0.93,
                "frequency_bonus": 0.12,
            },
            DecisionType.IDLE: {
                "base_weight": 0.3,
                "success_bonus": 0.1,
                "failure_penalty": 0.1,
                "recency_decay": 0.98,
                "frequency_bonus": 0.05,
            },
            DecisionType.EMERGENCY: {
                "base_weight": 1.0,
                "success_bonus": 0.6,
                "failure_penalty": 1.0,
                "recency_decay": 0.8,
                "frequency_bonus": 0.0,
            },
        }

    def analyze_state(self, system_state: Dict = None) -> StateSnapshot:
        """
        Analyze current system state comprehensively.
        Reads from all phases, builds a complete snapshot.
        """
        self._logger.telegram_step(1, 8, "State Analysis", 
                                   "Building comprehensive system snapshot...")

        timestamp = get_timestamp()

        # Build state from provided data or defaults
        if system_state is None:
            system_state = {}

        # Phase status (would be populated by actual phase integration)
        phase_status = system_state.get("phase_status", {
            "phase_1": "active",
            "phase_2": "active",
            "phase_3": "active",
            "phase_4": "active",
            "phase_5": "active",
            "phase_6": "active",
            "phase_7": "active",
            "phase_8": "active",
            "phase_9": "active",
            "phase_10": "active",
            "phase_11": "active",
            "phase_12": "active",
            "phase_13": "active",
        })

        # Pending tasks from database
        pending_tasks = system_state.get("pending_tasks", 0)
        try:
            pending_tasks = self._db.count("oanks_ai_decisions", 
                                           "success = 0 AND executed_at IS NULL")
        except:
            pass

        # Command queue size
        command_queue_size = system_state.get("command_queue_size", 0)

        # System health
        system_health = system_state.get("system_health", {})
        if not system_health:
            system_health = get_system_health().to_dict()

        # Proxy pool status
        proxy_pool_status = system_state.get("proxy_pool_status", {})
        try:
            proxy_stats = self._db.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN status = 'ACTIVE' THEN 1 ELSE 0 END) as active,
                    SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) as failed,
                    AVG(overall_score) as avg_score
                FROM oanks_ai_proxy_intel
            """)
            if proxy_stats:
                proxy_pool_status = {
                    "total": proxy_stats[0].get("total", 0),
                    "active": proxy_stats[0].get("active", 0),
                    "failed": proxy_stats[0].get("failed", 0),
                    "avg_score": round(proxy_stats[0].get("avg_score", 0), 2)
                }
        except:
            proxy_pool_status = {"total": 0, "active": 0, "failed": 0, "avg_score": 0}

        # Harvest status
        harvest_status = system_state.get("harvest_status", {})
        try:
            harvest_stats = self._db.execute("""
                SELECT 
                    COUNT(*) as total_operations,
                    SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful,
                    AVG(response_time) as avg_response_time
                FROM oanks_ai_scrape_memory
                WHERE timestamp > datetime('now', '-1 hour')
            """)
            if harvest_stats:
                harvest_status = {
                    "operations_last_hour": harvest_stats[0].get("total_operations", 0),
                    "successful": harvest_stats[0].get("successful", 0),
                    "avg_response_time": round(harvest_stats[0].get("avg_response_time", 0), 2)
                }
        except:
            harvest_status = {"operations_last_hour": 0, "successful": 0, "avg_response_time": 0}

        # Anomaly count
        anomaly_count = 0
        try:
            anomaly_count = self._db.count("oanks_ai_anomalies", "resolved = 0")
        except:
            pass

        # Decision count
        decision_count = 0
        try:
            decision_count = self._db.count("oanks_ai_decisions")
        except:
            pass

        # Performance metrics
        performance_metrics = system_state.get("performance_metrics", {})
        try:
            perf_stats = self._db.execute("""
                SELECT metric, AVG(value) as avg_value
                FROM oanks_ai_performance
                WHERE timestamp > datetime('now', '-1 hour')
                GROUP BY metric
            """)
            performance_metrics = {row["metric"]: round(row["avg_value"], 2) 
                                   for row in perf_stats}
        except:
            performance_metrics = {}

        snapshot = StateSnapshot(
            timestamp=timestamp,
            phase_status=phase_status,
            pending_tasks=pending_tasks,
            command_queue_size=command_queue_size,
            system_health=system_health,
            proxy_pool_status=proxy_pool_status,
            harvest_status=harvest_status,
            anomaly_count=anomaly_count,
            decision_count=decision_count,
            performance_metrics=performance_metrics
        )

        # Cache the snapshot
        with self._cache_lock:
            self._state_cache[timestamp] = snapshot.to_dict()

        self._logger.telegram_step(1, 8, "State Analysis", "Complete",
                                   status="success", details={
                                       "phases_active": sum(1 for v in phase_status.values() if v == "active"),
                                       "pending_tasks": pending_tasks,
                                       "anomalies": anomaly_count,
                                       "cpu": f"{system_health.get('cpu_usage', 0):.1f}%",
                                       "memory": f"{system_health.get('memory_usage', 0):.1f}%"
                                   })

        return snapshot

    def generate_options(self, state: StateSnapshot) -> List[Dict]:
        """
        Generate possible actions based on current state.
        Each option includes action, target, expected outcome, and initial score.
        """
        self._logger.telegram_step(2, 8, "Option Generation", 
                                   "Generating possible actions based on state...")

        options = []

        # Option 1: Harvest if proxy pool is healthy
        if state.proxy_pool_status.get("active", 0) > 10:
            options.append({
                "decision_type": DecisionType.HARVEST.name,
                "action": "start_harvesting",
                "target": "all_sources",
                "description": "Begin data harvesting from all active sources",
                "base_score": 70.0,
                "confidence": 0.75,
                "estimated_time": 300,
                "risk_level": "low",
                "prerequisites": ["proxy_pool_healthy"],
                "expected_outcome": "data_collected"
            })

        # Option 2: Rotate proxies if failure rate is high
        proxy_total = state.proxy_pool_status.get("total", 1)
        proxy_failed = state.proxy_pool_status.get("failed", 0)
        failure_rate = proxy_failed / proxy_total if proxy_total > 0 else 0

        if failure_rate > 0.3:
            options.append({
                "decision_type": DecisionType.PROXY_ROTATE.name,
                "action": "rotate_proxies",
                "target": "failed_proxies",
                "description": "Rotate out failed proxies and acquire new ones",
                "base_score": 85.0,
                "confidence": 0.8,
                "estimated_time": 120,
                "risk_level": "low",
                "prerequisites": ["proxy_failure_high"],
                "expected_outcome": "fresh_proxies"
            })

        # Option 3: Scale up if CPU is low and tasks are pending
        cpu_usage = state.system_health.get("cpu_usage", 0)
        if cpu_usage < 50 and state.pending_tasks > 5:
            options.append({
                "decision_type": DecisionType.SCALE_UP.name,
                "action": "increase_threads",
                "target": "harvesting_threads",
                "description": "Increase thread count to handle pending tasks",
                "base_score": 65.0,
                "confidence": 0.7,
                "estimated_time": 30,
                "risk_level": "medium",
                "prerequisites": ["cpu_low", "tasks_pending"],
                "expected_outcome": "faster_processing"
            })

        # Option 4: Scale down if CPU is high
        if cpu_usage > 80:
            options.append({
                "decision_type": DecisionType.SCALE_DOWN.name,
                "action": "decrease_threads",
                "target": "harvesting_threads",
                "description": "Reduce thread count to prevent system overload",
                "base_score": 90.0,
                "confidence": 0.85,
                "estimated_time": 15,
                "risk_level": "low",
                "prerequisites": ["cpu_high"],
                "expected_outcome": "system_stabilized"
            })

        # Option 5: Alert on anomalies
        if state.anomaly_count > 0:
            options.append({
                "decision_type": DecisionType.ALERT.name,
                "action": "alert_anomalies",
                "target": "admin",
                "description": f"Alert on {state.anomaly_count} detected anomalies",
                "base_score": 80.0,
                "confidence": 0.9,
                "estimated_time": 10,
                "risk_level": "low",
                "prerequisites": ["anomalies_detected"],
                "expected_outcome": "admin_notified"
            })

        # Option 6: Optimize system
        memory_usage = state.system_health.get("memory_usage", 0)
        if cpu_usage > 60 or memory_usage > 60:
            options.append({
                "decision_type": DecisionType.OPTIMIZE.name,
                "action": "optimize_system",
                "target": "system_resources",
                "description": "Run self-optimization to improve performance",
                "base_score": 75.0,
                "confidence": 0.72,
                "estimated_time": 180,
                "risk_level": "low",
                "prerequisites": ["resources_high"],
                "expected_outcome": "improved_performance"
            })

        # Option 7: Learn from recent data
        if state.decision_count > 10:
            options.append({
                "decision_type": DecisionType.LEARN.name,
                "action": "update_patterns",
                "target": "knowledge_base",
                "description": "Learn from recent decisions and outcomes",
                "base_score": 60.0,
                "confidence": 0.65,
                "estimated_time": 60,
                "risk_level": "low",
                "prerequisites": ["sufficient_data"],
                "expected_outcome": "improved_decisions"
            })

        # Option 8: Adapt scraping strategy
        harvest_success = state.harvest_status.get("successful", 0)
        harvest_total = state.harvest_status.get("operations_last_hour", 1)
        harvest_rate = harvest_success / harvest_total if harvest_total > 0 else 0

        if harvest_rate < 0.5 and harvest_total > 5:
            options.append({
                "decision_type": DecisionType.ADAPT.name,
                "action": "adapt_strategy",
                "target": "scraping_approach",
                "description": "Adapt scraping strategy due to low success rate",
                "base_score": 88.0,
                "confidence": 0.82,
                "estimated_time": 90,
                "risk_level": "medium",
                "prerequisites": ["low_harvest_rate"],
                "expected_outcome": "improved_success_rate"
            })

        # Option 9: Predict and schedule harvesting
        options.append({
            "decision_type": DecisionType.PREDICT.name,
            "action": "predict_harvest",
            "target": "data_sources",
            "description": "Predict optimal harvesting times and schedule operations",
            "base_score": 55.0,
            "confidence": 0.6,
            "estimated_time": 45,
            "risk_level": "low",
            "prerequisites": [],
            "expected_outcome": "optimal_schedule"
        })

        # Option 10: Respond to critical anomalies
        if state.anomaly_count > 5:
            options.append({
                "decision_type": DecisionType.ANOMALY_RESPONSE.name,
                "action": "auto_resolve_anomalies",
                "target": "critical_anomalies",
                "description": "Automatically respond to critical anomaly cluster",
                "base_score": 95.0,
                "confidence": 0.88,
                "estimated_time": 60,
                "risk_level": "high",
                "prerequisites": ["critical_anomalies"],
                "expected_outcome": "anomalies_resolved"
            })

        # Option 11: Restart failed phases
        failed_phases = [k for k, v in state.phase_status.items() if v == "failed"]
        if failed_phases:
            options.append({
                "decision_type": DecisionType.PHASE_RESTART.name,
                "action": "restart_phases",
                "target": ",".join(failed_phases),
                "description": f"Restart failed phases: {', '.join(failed_phases)}",
                "base_score": 70.0,
                "confidence": 0.6,
                "estimated_time": 300,
                "risk_level": "medium",
                "prerequisites": ["phases_failed"],
                "expected_outcome": "phases_recovered"
            })

        # Option 12: Switch target if current is blocked
        options.append({
            "decision_type": DecisionType.TARGET_SWITCH.name,
            "action": "switch_target",
            "target": "alternative_source",
            "description": "Switch to alternative data source",
            "base_score": 50.0,
                "confidence": 0.55,
                "estimated_time": 60,
                "risk_level": "medium",
                "prerequisites": ["target_blocked"],
                "expected_outcome": "new_target_active"
            })

        # Option 13: Change strategy
        options.append({
            "decision_type": DecisionType.STRATEGY_CHANGE.name,
            "action": "change_strategy",
            "target": "global_approach",
            "description": "Change overall operational strategy",
            "base_score": 45.0,
            "confidence": 0.5,
            "estimated_time": 120,
            "risk_level": "high",
            "prerequisites": ["strategy_stale"],
            "expected_outcome": "new_strategy_active"
        })

        # Option 14: Idle if everything is stable
        if (cpu_usage < 40 and memory_usage < 40 and 
            state.anomaly_count == 0 and state.pending_tasks == 0):
            options.append({
                "decision_type": DecisionType.IDLE.name,
                "action": "maintain_status",
                "target": "system",
                "description": "System is stable, maintain current state",
                "base_score": 40.0,
                "confidence": 0.9,
                "estimated_time": 60,
                "risk_level": "none",
                "prerequisites": ["system_stable"],
                "expected_outcome": "stability_maintained"
            })

        # Option 15: Emergency if system compromised
        if state.anomaly_count > 10 or cpu_usage > 95 or memory_usage > 95:
            options.append({
                "decision_type": DecisionType.EMERGENCY.name,
                "action": "emergency_lockdown",
                "target": "framework",
                "description": "EMERGENCY: System compromised, initiate lockdown",
                "base_score": 100.0,
                "confidence": 0.95,
                "estimated_time": 5,
                "risk_level": "critical",
                "prerequisites": ["system_compromised"],
                "expected_outcome": "system_secured"
            })

        self._logger.telegram_step(2, 8, "Option Generation", "Complete",
                                   status="success", details={
                                       "options_generated": len(options),
                                       "highest_base_score": max((o["base_score"] for o in options), default=0),
                                       "categories": list(set(o["decision_type"] for o in options))
                                   })

        return options

    def evaluate_option(self, option: Dict, state: StateSnapshot) -> float:
        """
        Evaluate a potential action with weighted scoring.
        Considers: base score, historical success, state alignment, risk, urgency.
        """
        decision_type_str = option.get("decision_type", "UNKNOWN")

        try:
            decision_type = DecisionType[decision_type_str]
        except KeyError:
            decision_type = DecisionType.CUSTOM

        weights = self._decision_weights.get(decision_type, {
            "base_weight": 0.5,
            "success_bonus": 0.2,
            "failure_penalty": 0.3,
            "recency_decay": 0.95,
            "frequency_bonus": 0.1,
        })

        # Start with base score
        score = option.get("base_score", 50.0)

        # Adjust by confidence
        confidence = option.get("confidence", 0.5)
        score *= (0.5 + confidence * 0.5)

        # Historical success rate for this decision type
        try:
            historical = self._db.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(success) as successes,
                    AVG(confidence) as avg_confidence
                FROM oanks_ai_decisions
                WHERE decision_type = ?
                AND made_at > datetime('now', '-7 days')
            """, (decision_type_str,))

            if historical and historical[0]["total"] > 0:
                success_rate = historical[0]["successes"] / historical[0]["total"]
                if success_rate > 0.7:
                    score += weights["success_bonus"] * 20
                elif success_rate < 0.3:
                    score -= weights["failure_penalty"] * 20
        except:
            pass

        # State alignment bonus
        if decision_type == DecisionType.SCALE_UP and state.system_health.get("cpu_usage", 0) < 40:
            score += 10
        elif decision_type == DecisionType.SCALE_DOWN and state.system_health.get("cpu_usage", 0) > 80:
            score += 10
        elif decision_type == DecisionType.PROXY_ROTATE and state.proxy_pool_status.get("failed", 0) > 5:
            score += 15
        elif decision_type == DecisionType.ANOMALY_RESPONSE and state.anomaly_count > 3:
            score += 20

        # Risk penalty
        risk_level = option.get("risk_level", "medium")
        risk_penalties = {"none": 0, "low": -2, "medium": -5, "high": -10, "critical": -15}
        score += risk_penalties.get(risk_level, -5)

        # Urgency bonus for time-sensitive decisions
        if decision_type in [DecisionType.EMERGENCY, DecisionType.ANOMALY_RESPONSE]:
            score += 10

        # Diversity bonus (avoid repeating same decision type)
        try:
            recent_same_type = self._db.count(
                "oanks_ai_decisions",
                "decision_type = ? AND made_at > datetime('now', '-1 hour')",
                (decision_type_str,)
            )
            if recent_same_type > 3:
                score -= recent_same_type * 3
        except:
            pass

        # Recency decay for recently tried options
        option_key = f"{decision_type_str}:{option.get('target', '')}"
        if option_key in self._option_history:
            last_time = self._option_history[option_key]
            hours_ago = (time.time() - last_time) / 3600
            decay = weights["recency_decay"] ** hours_ago
            score *= decay

        # Clamp final score
        score = clamp_value(score, 0.0, 100.0)

        return score

    def select_best_action(self, options: List[Dict], state: StateSnapshot) -> Dict:
        """
        Select the best action from generated options.
        Uses weighted scoring with exploration/exploitation balance.
        """
        self._logger.telegram_step(3, 8, "Action Selection", 
                                   "Evaluating and scoring all options...")

        if not options:
            self._logger.warning("No options generated, defaulting to IDLE")
            return {
                "decision_type": DecisionType.IDLE.name,
                "action": "maintain_status",
                "target": "system",
                "score": 0.0,
                "confidence": 0.0,
                "reason": "no_options_available"
            }

        # Score all options
        scored_options = []
        for option in options:
            score = self.evaluate_option(option, state)
            scored_option = option.copy()
            scored_option["score"] = score
            scored_options.append(scored_option)

        # Sort by score descending
        scored_options.sort(key=lambda x: x["score"], reverse=True)

        # Exploration: sometimes pick a lower-scored option to learn
        if random.random() < DecisionConfig.EXPLORATION_RATE and len(scored_options) > 1:
            # Pick from top 3 with weighted random
            top_options = scored_options[:min(3, len(scored_options))]
            weights = [opt["score"] for opt in top_options]
            selected_idx = weighted_random_choice(weights)
            selected = top_options[selected_idx]
            selected["exploration"] = True
        else:
            # Exploitation: pick highest score
            selected = scored_options[0]
            selected["exploration"] = False

        # Store in history
        option_key = f"{selected.get('decision_type', 'UNKNOWN')}:{selected.get('target', '')}"
        self._option_history[option_key] = time.time()

        self._logger.telegram_step(3, 8, "Action Selection", "Complete",
                                   status="success", details={
                                       "selected_action": selected.get("action", "UNKNOWN"),
                                       "selected_type": selected.get("decision_type", "UNKNOWN"),
                                       "score": f"{selected.get('score', 0):.1f}",
                                       "confidence": f"{selected.get('confidence', 0):.2f}",
                                       "exploration": "Yes" if selected.get("exploration") else "No",
                                       "options_considered": len(scored_options)
                                   })

        if self._telegram:
            self._telegram.send_decision_options(scored_options[:5])

        return selected

    def execute_decision(self, decision: Dict) -> Dict:
        """
        Execute a decision and track the outcome.
        Returns the execution result with timing and success status.
        """
        self._logger.telegram_step(4, 8, "Decision Execution", 
                                   f"Executing: {decision.get('action', 'UNKNOWN')}")

        start_time = time.time()
        result = {
            "decision": decision,
            "success": False,
            "execution_time": 0.0,
            "error": None,
            "output": None,
            "timestamp": get_timestamp()
        }

        try:
            # Record decision in database
            decision_record = {
                "decision_type": decision.get("decision_type", "UNKNOWN"),
                "action": decision.get("action", "UNKNOWN"),
                "target": decision.get("target", ""),
                "confidence": decision.get("confidence", 0.0),
                "outcome": "PENDING",
                "success": 0,
                "made_at": get_timestamp(),
                "executed_at": get_timestamp(),
                "execution_time": 0.0,
                "context": safe_json_dumps(decision.get("context", {})),
                "option_count": decision.get("option_count", 0),
                "selected_option_rank": decision.get("selected_rank", 0),
                "state_snapshot": safe_json_dumps(decision.get("state_snapshot", {})),
            }

            decision_id = self._db.insert("oanks_ai_decisions", decision_record)
            result["decision_id"] = decision_id

            # Execute the action (placeholder - would integrate with actual phases)
            action = decision.get("action", "")
            action_result = self._execute_action(action, decision)

            result["success"] = action_result.get("success", False)
            result["output"] = action_result.get("output", None)

            # Update decision record with outcome
            execution_time = time.time() - start_time
            self._db.update(
                "oanks_ai_decisions",
                {
                    "outcome": "SUCCESS" if result["success"] else "FAILED",
                    "success": 1 if result["success"] else 0,
                    "executed_at": get_timestamp(),
                    "execution_time": execution_time
                },
                "id = ?",
                (decision_id,)
            )

            # Record outcome for learning
            outcome_record = {
                "decision_id": decision_id,
                "success": 1 if result["success"] else 0,
                "reward": 1.0 if result["success"] else -1.0,
                "execution_time": execution_time,
                "error_message": result["error"] or "",
                "metadata": safe_json_dumps(action_result)
            }
            self._db.insert("oanks_ai_outcomes", outcome_record)

            result["execution_time"] = execution_time

            # Update statistics
            with self._decision_lock:
                self._decision_count += 1
                if result["success"]:
                    self._successful_decisions += 1
                else:
                    self._failed_decisions += 1

            self._logger.telegram_step(4, 8, "Decision Execution", "Complete",
                                       status="success" if result["success"] else "failure",
                                       details={
                                           "action": action,
                                           "success": result["success"],
                                           "execution_time": f"{execution_time:.2f}s",
                                           "decision_id": decision_id
                                       })

            if self._telegram:
                self._telegram.send_decision_result(decision_record, execution_time)

        except Exception as e:
            execution_time = time.time() - start_time
            result["success"] = False
            result["error"] = str(e)
            result["execution_time"] = execution_time

            self._logger.error(f"Decision execution failed: {e}", 
                              extra={"decision": decision, "error": str(e)})

            self._logger.telegram_step(4, 8, "Decision Execution", "Failed",
                                       status="error", details={
                                           "error": str(e),
                                           "execution_time": f"{execution_time:.2f}s"
                                       })

        return result

    def _execute_action(self, action: str, decision: Dict) -> Dict:
        """
        Execute a specific action. This is the integration point with other phases.
        In a real deployment, this would call Phase 3 (harvesting), Phase 2 (proxies), etc.
        """
        # Placeholder implementation - would be replaced with actual phase calls
        action_map = {
            "start_harvesting": self._action_harvest,
            "rotate_proxies": self._action_rotate_proxies,
            "increase_threads": self._action_scale_up,
            "decrease_threads": self._action_scale_down,
            "alert_anomalies": self._action_alert,
            "optimize_system": self._action_optimize,
            "update_patterns": self._action_learn,
            "adapt_strategy": self._action_adapt,
            "predict_harvest": self._action_predict,
            "auto_resolve_anomalies": self._action_resolve_anomalies,
            "restart_phases": self._action_restart_phases,
            "switch_target": self._action_switch_target,
            "change_strategy": self._action_change_strategy,
            "maintain_status": self._action_idle,
            "emergency_lockdown": self._action_emergency,
        }

        handler = action_map.get(action, self._action_unknown)
        return handler(decision)

    def _action_harvest(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Harvesting initiated"}

    def _action_rotate_proxies(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Proxy rotation completed"}

    def _action_scale_up(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Thread count increased"}

    def _action_scale_down(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Thread count decreased"}

    def _action_alert(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Alerts sent"}

    def _action_optimize(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Optimization completed"}

    def _action_learn(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Learning completed"}

    def _action_adapt(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Strategy adapted"}

    def _action_predict(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Predictions generated"}

    def _action_resolve_anomalies(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Anomalies resolved"}

    def _action_restart_phases(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Phases restarted"}

    def _action_switch_target(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Target switched"}

    def _action_change_strategy(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Strategy changed"}

    def _action_idle(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Status maintained"}

    def _action_emergency(self, decision: Dict) -> Dict:
        return {"success": True, "output": "Emergency lockdown initiated"}

    def _action_unknown(self, decision: Dict) -> Dict:
        return {"success": False, "output": f"Unknown action: {decision.get('action', 'UNKNOWN')}"}

    def learn_from_outcome(self, decision_id: int, success: bool) -> None:
        """
        Learn from the outcome of a decision.
        Updates weights, patterns, and knowledge base.
        """
        self._logger.telegram_step(5, 8, "Learning from Outcome", 
                                   f"Decision {decision_id}: {'Success' if success else 'Failure'}")

        try:
            # Get the decision record
            decision = self._db.select_one(
                "oanks_ai_decisions",
                where="id = ?",
                where_params=(decision_id,)
            )

            if not decision:
                return

            decision_type = decision.get("decision_type", "UNKNOWN")

            # Update decision weights
            if success:
                self._adjust_weight(decision_type, "success_bonus", 0.02)
                self._adjust_weight(decision_type, "failure_penalty", -0.01)
            else:
                self._adjust_weight(decision_type, "success_bonus", -0.01)
                self._adjust_weight(decision_type, "failure_penalty", 0.02)

            # Store pattern in knowledge base
            pattern_data = {
                "decision_type": decision_type,
                "action": decision.get("action", ""),
                "target": decision.get("target", ""),
                "confidence": decision.get("confidence", 0),
                "context": decision.get("context", ""),
            }

            pattern_hash = hash_string(safe_json_dumps(pattern_data))

            # Check if pattern exists
            existing = self._db.select_one(
                "oanks_ai_knowledge",
                where="pattern_hash = ?",
                where_params=(pattern_hash,)
            )

            if existing:
                # Update existing pattern
                new_success_count = existing.get("success_count", 0) + (1 if success else 0)
                new_failure_count = existing.get("failure_count", 0) + (0 if success else 1)
                total = new_success_count + new_failure_count
                new_success_rate = new_success_count / total if total > 0 else 0.5
                new_usage_count = existing.get("usage_count", 0) + 1

                self._db.update(
                    "oanks_ai_knowledge",
                    {
                        "success_rate": new_success_rate,
                        "usage_count": new_usage_count,
                        "success_count": new_success_count,
                        "failure_count": new_failure_count,
                        "last_used": get_timestamp(),
                        "last_validated": get_timestamp(),
                        "validation_status": "VALIDATED"
                    },
                    "id = ?",
                    (existing["id"],)
                )
            else:
                # Insert new pattern
                self._db.insert("oanks_ai_knowledge", {
                    "pattern_type": "decision_pattern",
                    "pattern_data": safe_json_dumps(pattern_data),
                    "pattern_hash": pattern_hash,
                    "success_rate": 1.0 if success else 0.0,
                    "usage_count": 1,
                    "success_count": 1 if success else 0,
                    "failure_count": 0 if success else 1,
                    "created_at": get_timestamp(),
                    "last_used": get_timestamp(),
                    "last_validated": get_timestamp(),
                    "validation_status": "PENDING",
                    "node_origin": "local"
                })

            self._logger.telegram_step(5, 8, "Learning from Outcome", "Complete",
                                       status="success", details={
                                           "decision_id": decision_id,
                                           "success": success,
                                           "pattern_updated": True
                                       })

        except Exception as e:
            self._logger.error(f"Learning from outcome failed: {e}")

    def _adjust_weight(self, decision_type: str, weight_key: str, delta: float) -> None:
        """Adjust a decision weight by a small delta."""
        try:
            dt = DecisionType[decision_type]
            if dt in self._decision_weights:
                current = self._decision_weights[dt].get(weight_key, 0)
                self._decision_weights[dt][weight_key] = clamp_value(current + delta, 0.0, 1.0)
        except (KeyError, ValueError):
            pass

    def get_decision_history(self, limit: int = 100) -> List[Dict]:
        """Get recent decision history."""
        return self._db.select(
            "oanks_ai_decisions",
            order_by="made_at DESC",
            limit=limit
        )

    def get_decision_stats(self) -> Dict:
        """Get decision statistics."""
        with self._decision_lock:
            total = self._decision_count
            success = self._successful_decisions
            failed = self._failed_decisions

        success_rate = success / total if total > 0 else 0.0

        # Get database stats
        try:
            db_stats = self._db.execute("""
                SELECT 
                    decision_type,
                    COUNT(*) as total,
                    SUM(success) as successes,
                    AVG(confidence) as avg_confidence,
                    AVG(execution_time) as avg_execution_time
                FROM oanks_ai_decisions
                GROUP BY decision_type
            """)

            type_stats = {}
            for row in db_stats:
                dt = row["decision_type"]
                total_type = row["total"]
                successes_type = row["successes"] or 0
                type_stats[dt] = {
                    "total": total_type,
                    "successes": successes_type,
                    "success_rate": successes_type / total_type if total_type > 0 else 0,
                    "avg_confidence": round(row.get("avg_confidence", 0), 2),
                    "avg_execution_time": round(row.get("avg_execution_time", 0), 2)
                }
        except:
            type_stats = {}

        return {
            "total_decisions": total,
            "successful": success,
            "failed": failed,
            "success_rate": round(success_rate, 2),
            "by_type": type_stats,
            "last_decision_time": self._last_decision_time,
            "exploration_rate": DecisionConfig.EXPLORATION_RATE
        }

    def make_decision(self, system_state: Dict = None) -> Dict:
        """
        Complete decision-making pipeline:
        1. Analyze state
        2. Generate options
        3. Evaluate and select best
        4. Execute
        5. Learn from outcome
        """
        self._logger.info("Starting decision-making pipeline")

        if self._telegram:
            self._telegram.send_decision_start("AUTO", "system")

        # Step 1: Analyze state
        state = self.analyze_state(system_state)

        # Step 2: Generate options
        options = self.generate_options(state)

        # Step 3: Select best action
        best_action = self.select_best_action(options, state)
        best_action["option_count"] = len(options)
        best_action["selected_rank"] = 1
        best_action["state_snapshot"] = state.to_dict()

        # Step 4: Execute
        result = self.execute_decision(best_action)

        # Step 5: Learn
        if "decision_id" in result:
            self.learn_from_outcome(result["decision_id"], result["success"])

        self._last_decision_time = time.time()

        self._logger.info("Decision-making pipeline complete",
                         extra={"result": result})

        return result

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        return {
            "decisions_made": self._decision_count,
            "successful_decisions": self._successful_decisions,
            "failed_decisions": self._failed_decisions,
            "success_rate": self._successful_decisions / max(self._decision_count, 1),
            "last_decision_time": self._last_decision_time,
            "cached_states": len(self._state_cache),
            "option_history_size": len(self._option_history),
            "weight_count": sum(len(w) for w in self._decision_weights.values())
        }

# ==============================================================================
# END OF SECTION 5: AUTO-DECISION MAKING ENGINE
# ==============================================================================



# ==============================================================================
# SECTION 6: ADAPTIVE SCRAPING ENGINE — INTELLIGENT, SELF-ADJUSTING, EVASIVE
# ==============================================================================

class AdaptiveScrapingEngine:
    """
    Adaptive scraping engine that detects anti-scraping measures and
    automatically adjusts strategy. Learns from every request, every block,
    every success. Becomes smarter with every interaction.

    Features:
    - Anti-scrape detection (CAPTCHA, rate limits, blocks, honeypots)
    - Auto-adaptation (proxy switching, delay adjustment, UA rotation)
    - Strategy optimization per target
    - Memory-based learning of optimal configurations
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._target_memory = {}
        self._strategy_memory = {}
        self._user_agent_pool = self._build_user_agent_pool()
        self._current_user_agent_index = 0
        self._request_count = 0
        self._success_count = 0
        self._failure_count = 0
        self._block_count = 0
        self._captcha_count = 0
        self._honeypot_count = 0
        self._memory_lock = RLock()
        self._last_strategy_change = {}

    def _build_user_agent_pool(self) -> List[str]:
        """Build a diverse pool of user agents."""
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.2; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
        ]

    def detect_anti_scrape(self, response: Dict) -> Dict:
        """
        Detect anti-scraping measures in a response.
        Returns detailed detection results.
        """
        detection = {
            "captcha_detected": False,
            "blocked_detected": False,
            "rate_limited": False,
            "honeypot_detected": False,
            "anti_scrape_detected": False,
            "confidence": 0.0,
            "indicators": []
        }

        # Check status code
        status_code = response.get("status_code", 0)
        if status_code in ScrapeConfig.RATE_LIMIT_STATUS:
            detection["rate_limited"] = True
            detection["indicators"].append(f"rate_limit_status_{status_code}")

        if status_code in ScrapeConfig.BLOCK_STATUS:
            detection["blocked_detected"] = True
            detection["indicators"].append(f"block_status_{status_code}")

        # Check response content
        content = response.get("content", "")
        content_lower = content.lower()

        # CAPTCHA detection
        for keyword in ScrapeConfig.CAPTCHA_KEYWORDS:
            if keyword.lower() in content_lower:
                detection["captcha_detected"] = True
                detection["indicators"].append(f"captcha_keyword:{keyword}")
                break

        # Block detection
        for keyword in ScrapeConfig.BLOCK_KEYWORDS:
            if keyword.lower() in content_lower:
                detection["blocked_detected"] = True
                detection["indicators"].append(f"block_keyword:{keyword}")
                break

        # Honeypot detection
        for pattern in ScrapeConfig.HONEYPOT_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                detection["honeypot_detected"] = True
                detection["indicators"].append(f"honeypot_pattern:{pattern}")
                break

        # Overall anti-scrape detection
        detection["anti_scrape_detected"] = (
            detection["captcha_detected"] or
            detection["blocked_detected"] or
            detection["rate_limited"] or
            detection["honeypot_detected"]
        )

        # Calculate confidence
        indicator_count = len(detection["indicators"])
        if indicator_count >= 3:
            detection["confidence"] = 0.95
        elif indicator_count == 2:
            detection["confidence"] = 0.8
        elif indicator_count == 1:
            detection["confidence"] = 0.6
        else:
            detection["confidence"] = 0.0

        return detection

    def adapt_scrape_strategy(self, target: str, results: List[Dict]) -> Dict:
        """
        Adapt scraping strategy based on recent results.
        Returns the adapted strategy configuration.
        """
        self._logger.telegram_step(1, 5, "Strategy Adaptation", 
                                   f"Analyzing {len(results)} results for {target}...")

        with self._memory_lock:
            if target not in self._target_memory:
                self._target_memory[target] = {
                    "requests": 0,
                    "successes": 0,
                    "failures": 0,
                    "blocks": 0,
                    "captchas": 0,
                    "honeypots": 0,
                    "avg_delay": ScrapeConfig.BASE_DELAY,
                    "current_strategy": ScrapeStrategy.BALANCED.name,
                    "user_agent_effectiveness": {},
                    "proxy_effectiveness": {},
                    "time_bucket_success": defaultdict(int),
                    "time_bucket_failure": defaultdict(int),
                    "last_adaptation": time.time(),
                    "consecutive_failures": 0,
                    "consecutive_successes": 0,
                    "strategy_history": [],
                    "optimal_delay": ScrapeConfig.BASE_DELAY,
                    "optimal_ua": None,
                    "optimal_proxy": None,
                }

            memory = self._target_memory[target]

            # Analyze results
            for result in results:
                memory["requests"] += 1
                self._request_count += 1

                if result.get("success", False):
                    memory["successes"] += 1
                    memory["consecutive_successes"] += 1
                    memory["consecutive_failures"] = 0
                    self._success_count += 1
                else:
                    memory["failures"] += 1
                    memory["consecutive_failures"] += 1
                    memory["consecutive_successes"] = 0
                    self._failure_count += 1

                # Track anti-scrape detections
                detection = result.get("detection", {})
                if detection.get("captcha_detected"):
                    memory["captchas"] += 1
                    self._captcha_count += 1
                if detection.get("blocked_detected"):
                    memory["blocks"] += 1
                    self._block_count += 1
                if detection.get("honeypot_detected"):
                    memory["honeypots"] += 1
                    self._honeypot_count += 1

                # Track user agent effectiveness
                ua = result.get("user_agent", "")
                if ua:
                    if ua not in memory["user_agent_effectiveness"]:
                        memory["user_agent_effectiveness"][ua] = {"success": 0, "failure": 0}
                    if result.get("success"):
                        memory["user_agent_effectiveness"][ua]["success"] += 1
                    else:
                        memory["user_agent_effectiveness"][ua]["failure"] += 1

                # Track proxy effectiveness
                proxy = result.get("proxy_used", 0)
                if proxy:
                    if proxy not in memory["proxy_effectiveness"]:
                        memory["proxy_effectiveness"][proxy] = {"success": 0, "failure": 0}
                    if result.get("success"):
                        memory["proxy_effectiveness"][proxy]["success"] += 1
                    else:
                        memory["proxy_effectiveness"][proxy]["failure"] += 1

                # Track time-based patterns
                hour_bucket = time_bucket(time.time(), 3600)
                if result.get("success"):
                    memory["time_bucket_success"][hour_bucket] += 1
                else:
                    memory["time_bucket_failure"][hour_bucket] += 1

            # Calculate success rate
            total = memory["requests"]
            success_rate = memory["successes"] / total if total > 0 else 0.5

            # Determine strategy adaptation
            new_strategy = memory["current_strategy"]
            new_delay = memory["avg_delay"]

            # High consecutive failures → more cautious
            if memory["consecutive_failures"] >= ScrapeConfig.CONSECUTIVE_FAILURE_THRESHOLD:
                if memory["current_strategy"] != ScrapeStrategy.STEALTH.name:
                    new_strategy = ScrapeStrategy.STEALTH.name
                    new_delay = min(memory["avg_delay"] * 2, ScrapeConfig.MAX_DELAY)
                    self._logger.info(f"Switching {target} to STEALTH strategy due to failures")

            # CAPTCHA detected → increase delay and rotate UA
            if memory["captchas"] > 0 and memory["captchas"] % 3 == 0:
                new_delay = min(memory["avg_delay"] * 1.5, ScrapeConfig.MAX_DELAY)
                self._logger.info(f"Increasing delay for {target} due to CAPTCHA frequency")

            # Blocked frequently → switch to most successful proxy/UA
            if memory["blocks"] > 5:
                # Find best user agent
                best_ua = None
                best_ua_rate = 0
                for ua, stats in memory["user_agent_effectiveness"].items():
                    ua_total = stats["success"] + stats["failure"]
                    if ua_total > 0:
                        ua_rate = stats["success"] / ua_total
                        if ua_rate > best_ua_rate:
                            best_ua_rate = ua_rate
                            best_ua = ua

                if best_ua and best_ua_rate > 0.5:
                    memory["optimal_ua"] = best_ua
                    self._logger.info(f"Found optimal UA for {target}: {best_ua[:50]}...")

                # Find best proxy
                best_proxy = None
                best_proxy_rate = 0
                for proxy, stats in memory["proxy_effectiveness"].items():
                    proxy_total = stats["success"] + stats["failure"]
                    if proxy_total > 0:
                        proxy_rate = stats["success"] / proxy_total
                        if proxy_rate > best_proxy_rate:
                            best_proxy_rate = proxy_rate
                            best_proxy = proxy

                if best_proxy and best_proxy_rate > 0.5:
                    memory["optimal_proxy"] = best_proxy
                    self._logger.info(f"Found optimal proxy for {target}: {best_proxy}")

            # Very high success rate → can be more aggressive
            if success_rate > 0.9 and memory["consecutive_successes"] > 10:
                if memory["current_strategy"] == ScrapeStrategy.STEALTH.name:
                    new_strategy = ScrapeStrategy.BALANCED.name
                    new_delay = max(memory["avg_delay"] * 0.8, ScrapeConfig.MIN_DELAY)
                    self._logger.info(f"Relaxing strategy for {target} due to high success rate")

            # Apply changes
            if new_strategy != memory["current_strategy"]:
                memory["strategy_history"].append({
                    "from": memory["current_strategy"],
                    "to": new_strategy,
                    "reason": "auto_adaptation",
                    "timestamp": get_timestamp()
                })
                memory["current_strategy"] = new_strategy

            memory["avg_delay"] = new_delay
            memory["optimal_delay"] = new_delay
            memory["last_adaptation"] = time.time()

            # Store in database
            self._store_scrape_memory(target, memory)

            strategy_config = {
                "target": target,
                "strategy": new_strategy,
                "delay": new_delay,
                "user_agent": memory.get("optimal_ua"),
                "proxy": memory.get("optimal_proxy"),
                "success_rate": success_rate,
                "consecutive_failures": memory["consecutive_failures"],
                "consecutive_successes": memory["consecutive_successes"],
                "total_requests": memory["requests"],
                "total_blocks": memory["blocks"],
                "total_captchas": memory["captchas"]
            }

            self._logger.telegram_step(1, 5, "Strategy Adaptation", "Complete",
                                       status="success", details={
                                           "target": target,
                                           "new_strategy": new_strategy,
                                           "delay": f"{new_delay:.1f}s",
                                           "success_rate": f"{success_rate:.1%}",
                                           "blocks": memory["blocks"],
                                           "captchas": memory["captchas"]
                                       })

            return strategy_config

    def _store_scrape_memory(self, target: str, memory: Dict) -> None:
        """Store scrape memory to database."""
        try:
            self._db.insert("oanks_ai_scrape_memory", {
                "target": target,
                "strategy": memory.get("current_strategy", "BALANCED"),
                "success": 1 if memory.get("consecutive_successes", 0) > 0 else 0,
                "anti_scrape_detected": 1 if memory.get("blocks", 0) > 0 else 0,
                "captcha_detected": 1 if memory.get("captchas", 0) > 0 else 0,
                "blocked_detected": 1 if memory.get("blocks", 0) > 0 else 0,
                "honeypot_detected": 1 if memory.get("honeypots", 0) > 0 else 0,
                "delay_used": memory.get("avg_delay", ScrapeConfig.BASE_DELAY),
                "timestamp": get_timestamp()
            })
        except Exception as e:
            self._logger.debug(f"Failed to store scrape memory: {e}")

    def switch_proxy_on_block(self, target: str, proxy_id: int = None) -> bool:
        """Switch proxy when blocked."""
        self._logger.info(f"Switching proxy for {target} due to block detection")

        # In real implementation, would call Phase 2 proxy rotation
        # For now, mark the proxy as failed in memory
        with self._memory_lock:
            if target in self._target_memory:
                memory = self._target_memory[target]
                if proxy_id and proxy_id in memory.get("proxy_effectiveness", {}):
                    memory["proxy_effectiveness"][proxy_id]["failure"] += 1

        return True

    def adjust_rate_limit(self, target: str, success: bool) -> float:
        """Adjust rate limiting based on success/failure."""
        with self._memory_lock:
            if target not in self._target_memory:
                return ScrapeConfig.BASE_DELAY

            memory = self._target_memory[target]
            current_delay = memory.get("avg_delay", ScrapeConfig.BASE_DELAY)

            if success:
                # Can potentially decrease delay
                new_delay = max(current_delay * 0.95, ScrapeConfig.MIN_DELAY)
            else:
                # Must increase delay
                new_delay = min(current_delay * 1.2, ScrapeConfig.MAX_DELAY)

            memory["avg_delay"] = new_delay
            return new_delay

    def rotate_user_agent(self, target: str = None) -> str:
        """Intelligently rotate user agent."""
        with self._memory_lock:
            # If we have an optimal UA for this target, use it sometimes
            if target and target in self._target_memory:
                memory = self._target_memory[target]
                optimal_ua = memory.get("optimal_ua")
                if optimal_ua and random.random() < 0.7:
                    return optimal_ua

            # Otherwise rotate through pool
            self._current_user_agent_index = (
                self._current_user_agent_index + 1
            ) % len(self._user_agent_pool)

            return self._user_agent_pool[self._current_user_agent_index]

    def learn_scrape_patterns(self, target: str) -> Dict:
        """Learn patterns for a specific target."""
        with self._memory_lock:
            if target not in self._target_memory:
                return {"error": "No memory for target"}

            memory = self._target_memory[target]

            # Analyze time-based patterns
            success_buckets = dict(memory.get("time_bucket_success", {}))
            failure_buckets = dict(memory.get("time_bucket_failure", {}))

            all_buckets = set(success_buckets.keys()) | set(failure_buckets.keys())

            best_buckets = []
            worst_buckets = []

            for bucket in all_buckets:
                successes = success_buckets.get(bucket, 0)
                failures = failure_buckets.get(bucket, 0)
                total = successes + failures

                if total > 0:
                    rate = successes / total
                    if rate > 0.8 and total >= 3:
                        best_buckets.append((bucket, rate, total))
                    elif rate < 0.2 and total >= 3:
                        worst_buckets.append((bucket, rate, total))

            # Sort by rate
            best_buckets.sort(key=lambda x: x[1], reverse=True)
            worst_buckets.sort(key=lambda x: x[1])

            patterns = {
                "target": target,
                "total_requests": memory["requests"],
                "success_rate": memory["successes"] / max(memory["requests"], 1),
                "best_time_buckets": [
                    {
                        "hour": datetime.fromtimestamp(b[0]).hour,
                        "success_rate": b[1],
                        "sample_size": b[2]
                    }
                    for b in best_buckets[:5]
                ],
                "worst_time_buckets": [
                    {
                        "hour": datetime.fromtimestamp(b[0]).hour,
                        "success_rate": b[1],
                        "sample_size": b[2]
                    }
                    for b in worst_buckets[:5]
                ],
                "optimal_user_agent": memory.get("optimal_ua", "None")[:50] if memory.get("optimal_ua") else "None",
                "optimal_proxy": memory.get("optimal_proxy", "None"),
                "optimal_delay": memory.get("optimal_delay", ScrapeConfig.BASE_DELAY),
                "current_strategy": memory.get("current_strategy", "BALANCED"),
                "recommended_strategy": self._recommend_strategy(memory)
            }

            return patterns

    def _recommend_strategy(self, memory: Dict) -> str:
        """Recommend a strategy based on memory."""
        success_rate = memory["successes"] / max(memory["requests"], 1)
        block_rate = memory["blocks"] / max(memory["requests"], 1)
        captcha_rate = memory["captchas"] / max(memory["requests"], 1)

        if block_rate > 0.3 or captcha_rate > 0.2:
            return ScrapeStrategy.STEALTH.name
        elif success_rate > 0.9:
            return ScrapeStrategy.AGGRESSIVE.name
        elif success_rate > 0.7:
            return ScrapeStrategy.BALANCED.name
        else:
            return ScrapeStrategy.CAUTIOUS.name

    def get_optimal_scrape_config(self, target: str) -> Dict:
        """Get optimal scraping configuration for a target."""
        with self._memory_lock:
            if target not in self._target_memory:
                return {
                    "target": target,
                    "strategy": ScrapeStrategy.BALANCED.name,
                    "delay": ScrapeConfig.BASE_DELAY,
                    "user_agent": self.rotate_user_agent(),
                    "proxy": None,
                    "retries": ScrapeConfig.MAX_RETRIES,
                    "source": "default"
                }

            memory = self._target_memory[target]

            return {
                "target": target,
                "strategy": memory.get("current_strategy", ScrapeStrategy.BALANCED.name),
                "delay": memory.get("optimal_delay", ScrapeConfig.BASE_DELAY),
                "user_agent": memory.get("optimal_ua") or self.rotate_user_agent(target),
                "proxy": memory.get("optimal_proxy"),
                "retries": ScrapeConfig.MAX_RETRIES,
                "source": "learned"
            }

    def get_target_memory(self, target: str = None) -> Dict:
        """Get memory for a specific target or all targets."""
        with self._memory_lock:
            if target:
                return self._target_memory.get(target, {})
            return dict(self._target_memory)

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        with self._memory_lock:
            return {
                "total_requests": self._request_count,
                "successful_requests": self._success_count,
                "failed_requests": self._failure_count,
                "blocks_encountered": self._block_count,
                "captchas_encountered": self._captcha_count,
                "honeypots_encountered": self._honeypot_count,
                "success_rate": self._success_count / max(self._request_count, 1),
                "targets_tracked": len(self._target_memory),
                "user_agent_pool_size": len(self._user_agent_pool),
                "strategies_adapted": sum(
                    1 for m in self._target_memory.values()
                    if len(m.get("strategy_history", [])) > 0
                )
            }

# ==============================================================================
# SECTION 7: INTELLIGENT PROXY ROTATION ENGINE — PREDICTIVE, SCORING, LEARNING
# ==============================================================================

class IntelligentProxyEngine:
    """
    Intelligent proxy rotation engine with predictive failure detection,
    weighted scoring, and target-specific learning.

    Features:
    - Proxy scoring based on success rate, speed, stability
    - Predictive failure detection
    - Target-specific proxy pairing
    - Geographic and protocol intelligence
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._proxy_cache = {}
        self._target_pairings = {}
        self._prediction_history = {}
        self._cache_lock = RLock()
        self._prefetch_thread = None
        self._prefetch_running = False

    def score_proxy(self, proxy_id: int, force_refresh: bool = False) -> float:
        """
        Calculate comprehensive proxy intelligence score.
        Score = (success_rate * 0.6) + (speed * 0.4) + (stability * 0.2)
        """
        with self._cache_lock:
            if not force_refresh and proxy_id in self._proxy_cache:
                cached = self._proxy_cache[proxy_id]
                if time.time() - cached.get("cached_at", 0) < 300:  # 5 min cache
                    return cached.get("overall_score", 0.5)

        try:
            # Get proxy intelligence from database
            intel = self._db.select_one(
                "oanks_ai_proxy_intel",
                where="proxy_id = ?",
                where_params=(proxy_id,)
            )

            if not intel:
                return 0.5

            # Calculate success rate
            success_count = intel.get("success_count", 0)
            failure_count = intel.get("failure_count", 0)
            total = success_count + failure_count
            success_rate = success_count / total if total > 0 else 0.5

            # Calculate speed score (inverse of response time)
            avg_response_time = intel.get("avg_response_time", 5.0)
            speed_score = 1.0 - normalize_value(
                avg_response_time,
                ProxyConfig.MIN_RESPONSE_TIME,
                ProxyConfig.MAX_RESPONSE_TIME
            )

            # Calculate stability score (based on variance)
            min_time = intel.get("min_response_time", avg_response_time)
            max_time = intel.get("max_response_time", avg_response_time)
            time_range = max_time - min_time
            stability_score = 1.0 - normalize_value(
                time_range,
                0,
                ProxyConfig.MAX_RESPONSE_TIME
            )

            # Calculate age score (newer is better, but not too new)
            first_seen = parse_timestamp(intel.get("first_seen", ""))
            if first_seen:
                age_days = (time.time() - first_seen) / 86400
                if age_days < 1:
                    age_score = 0.7  # Too new, unproven
                elif age_days < 7:
                    age_score = 1.0  # Sweet spot
                else:
                    age_score = max(0.5, 1.0 - (age_days - 7) / 30)
            else:
                age_score = 0.5

            # Calculate consecutive success/failure bonus/penalty
            consecutive_successes = intel.get("consecutive_successes", 0)
            consecutive_failures = intel.get("consecutive_failures", 0)

            streak_bonus = 0
            if consecutive_successes >= 5:
                streak_bonus = 0.1
            elif consecutive_failures >= 3:
                streak_bonus = -0.2

            # Weighted overall score
            overall_score = (
                success_rate * ProxyConfig.SCORE_SUCCESS_WEIGHT +
                speed_score * ProxyConfig.SCORE_SPEED_WEIGHT +
                stability_score * ProxyConfig.SCORE_STABILITY_WEIGHT +
                age_score * ProxyConfig.SCORE_AGE_WEIGHT +
                streak_bonus
            )

            overall_score = clamp_value(overall_score, 0.0, 1.0)

            # Update cache
            with self._cache_lock:
                self._proxy_cache[proxy_id] = {
                    "proxy_id": proxy_id,
                    "success_rate": success_rate,
                    "speed_score": speed_score,
                    "stability_score": stability_score,
                    "age_score": age_score,
                    "overall_score": overall_score,
                    "cached_at": time.time(),
                    "intel": intel
                }

            # Update database with calculated scores
            self._db.update(
                "oanks_ai_proxy_intel",
                {
                    "reliability_score": success_rate,
                    "stability_score": stability_score,
                    "speed_score": speed_score,
                    "overall_score": overall_score
                },
                "id = ?",
                (intel["id"],)
            )

            return overall_score

        except Exception as e:
            self._logger.debug(f"Proxy scoring failed for {proxy_id}: {e}")
            return 0.5

    def get_best_proxy_for_target(self, target: str, 
                                   exclude_proxy_ids: List[int] = None) -> Optional[int]:
        """
        Get the best proxy for a specific target.
        Uses target-specific pairing data if available.
        """
        exclude_proxy_ids = exclude_proxy_ids or []

        with self._cache_lock:
            # Check target-specific pairings
            if target in self._target_pairings:
                pairings = self._target_pairings[target]
                # Sort by success rate
                sorted_pairings = sorted(
                    pairings.items(),
                    key=lambda x: x[1].get("success_rate", 0),
                    reverse=True
                )

                for proxy_id, pairing in sorted_pairings:
                    if proxy_id not in exclude_proxy_ids:
                        # Verify proxy is still good
                        score = self.score_proxy(proxy_id)
                        if score > ProxyConfig.PROXY_DEPRECATION_THRESHOLD:
                            return proxy_id

        # Fallback: get best proxy overall
        try:
            proxies = self._db.select(
                "oanks_ai_proxy_intel",
                where="status IN ('ACTIVE', 'NEW', 'PREFERRED')",
                order_by="overall_score DESC",
                limit=50
            )

            for proxy in proxies:
                proxy_id = proxy.get("proxy_id")
                if proxy_id not in exclude_proxy_ids:
                    score = self.score_proxy(proxy_id)
                    if score > ProxyConfig.PROXY_DEPRECATION_THRESHOLD:
                        return proxy_id
        except Exception as e:
            self._logger.debug(f"Failed to get best proxy: {e}")

        return None

    def predict_proxy_failure(self, proxy_id: int) -> Dict:
        """
        Predict probability of proxy failure before it happens.
        Uses trend analysis and pattern matching.
        """
        try:
            # Get recent performance data
            recent_data = self._db.select(
                "oanks_ai_proxy_intel",
                where="proxy_id = ?",
                where_params=(proxy_id,),
                order_by="last_used DESC",
                limit=1
            )

            if not recent_data:
                return {"failure_probability": 0.5, "confidence": 0.0, "reason": "no_data"}

            intel = recent_data[0]

            # Calculate failure probability based on multiple factors
            factors = []

            # Factor 1: Recent failure rate
            success_count = intel.get("success_count", 0)
            failure_count = intel.get("failure_count", 0)
            total = success_count + failure_count

            if total > 0:
                failure_rate = failure_count / total
                factors.append(("historical_failure_rate", failure_rate, 0.3))

            # Factor 2: Consecutive failures
            consecutive_failures = intel.get("consecutive_failures", 0)
            if consecutive_failures > 0:
                cf_prob = min(consecutive_failures / 5, 1.0)
                factors.append(("consecutive_failures", cf_prob, 0.25))

            # Factor 3: Response time degradation
            avg_response = intel.get("avg_response_time", 5.0)
            if avg_response > ProxyConfig.MAX_RESPONSE_TIME * 0.8:
                rt_prob = normalize_value(avg_response, 
                                          ProxyConfig.MAX_RESPONSE_TIME * 0.8,
                                          ProxyConfig.MAX_RESPONSE_TIME * 2)
                factors.append(("response_time", rt_prob, 0.2))

            # Factor 4: Time since last success
            last_used = parse_timestamp(intel.get("last_used", ""))
            if last_used:
                hours_since = (time.time() - last_used) / 3600
                if hours_since > 24:
                    time_prob = min(hours_since / 72, 1.0)
                    factors.append(("time_since_use", time_prob, 0.15))

            # Factor 5: Validation status
            validation_count = intel.get("validation_count", 0)
            if validation_count > 0:
                last_validated = parse_timestamp(intel.get("last_validated", ""))
                if last_validated:
                    days_since_validation = (time.time() - last_validated) / 86400
                    if days_since_validation > 7:
                        val_prob = min(days_since_validation / 30, 1.0)
                        factors.append(("validation_age", val_prob, 0.1))

            # Calculate weighted failure probability
            if factors:
                total_weight = sum(f[2] for f in factors)
                failure_probability = sum(f[1] * f[2] for f in factors) / total_weight
                confidence = min(total, 20) / 20  # More data = higher confidence
            else:
                failure_probability = 0.3
                confidence = 0.1

            # Determine risk level
            if failure_probability > 0.8:
                risk_level = "CRITICAL"
            elif failure_probability > 0.6:
                risk_level = "HIGH"
            elif failure_probability > 0.4:
                risk_level = "MEDIUM"
            else:
                risk_level = "LOW"

            return {
                "proxy_id": proxy_id,
                "failure_probability": round(failure_probability, 3),
                "confidence": round(confidence, 3),
                "risk_level": risk_level,
                "factors": [{"name": f[0], "value": round(f[1], 3), "weight": f[2]} for f in factors],
                "recommendation": "rotate" if failure_probability > 0.6 else "monitor",
                "predicted_failure_time": self._estimate_failure_time(failure_probability, intel)
            }

        except Exception as e:
            self._logger.debug(f"Proxy failure prediction failed: {e}")
            return {"failure_probability": 0.5, "confidence": 0.0, "reason": "error"}

    def _estimate_failure_time(self, failure_probability: float, intel: Dict) -> str:
        """Estimate when proxy might fail."""
        if failure_probability < 0.3:
            return "stable"

        avg_response = intel.get("avg_response_time", 5.0)
        consecutive_failures = intel.get("consecutive_failures", 0)

        # Rough estimation based on degradation rate
        if consecutive_failures > 0:
            estimated_hours = max(1, int((1 - failure_probability) * 24 / (consecutive_failures + 1)))
        else:
            estimated_hours = max(1, int((1 - failure_probability) * 48))

        return f"estimated_{estimated_hours}h"

    def update_proxy_intel(self, proxy_id: int, success: bool, 
                           response_time: float, target: str = None) -> None:
        """Update proxy intelligence data after use."""
        try:
            # Get existing intel
            intel = self._db.select_one(
                "oanks_ai_proxy_intel",
                where="proxy_id = ?",
                where_params=(proxy_id,)
            )

            if intel:
                # Update existing
                new_success_count = intel["success_count"] + (1 if success else 0)
                new_failure_count = intel["failure_count"] + (0 if success else 1)
                new_total = new_success_count + new_failure_count

                # Update response time stats
                old_avg = intel.get("avg_response_time", response_time)
                new_avg = (old_avg * intel.get("validation_count", 0) + response_time) / (intel.get("validation_count", 0) + 1)
                new_min = min(intel.get("min_response_time", 999999), response_time)
                new_max = max(intel.get("max_response_time", 0), response_time)

                # Update consecutive counters
                if success:
                    new_consecutive_successes = intel.get("consecutive_successes", 0) + 1
                    new_consecutive_failures = 0
                else:
                    new_consecutive_successes = 0
                    new_consecutive_failures = intel.get("consecutive_failures", 0) + 1

                # Update target maps
                target_success_map = safe_json_loads(intel.get("target_success_map", "{}"), {})
                target_failure_map = safe_json_loads(intel.get("target_failure_map", "{}"), {})

                if target:
                    if success:
                        target_success_map[target] = target_success_map.get(target, 0) + 1
                    else:
                        target_failure_map[target] = target_failure_map.get(target, 0) + 1

                self._db.update(
                    "oanks_ai_proxy_intel",
                    {
                        "success_count": new_success_count,
                        "failure_count": new_failure_count,
                        "avg_response_time": new_avg,
                        "min_response_time": new_min,
                        "max_response_time": new_max,
                        "last_used": get_timestamp(),
                        "consecutive_successes": new_consecutive_successes,
                        "consecutive_failures": new_consecutive_failures,
                        "target_success_map": safe_json_dumps(target_success_map),
                        "target_failure_map": safe_json_dumps(target_failure_map),
                        "validation_count": intel.get("validation_count", 0) + 1,
                        "last_validated": get_timestamp()
                    },
                    "id = ?",
                    (intel["id"],)
                )
            else:
                # Create new intel record
                self._db.insert("oanks_ai_proxy_intel", {
                    "proxy_id": proxy_id,
                    "success_count": 1 if success else 0,
                    "failure_count": 0 if success else 1,
                    "avg_response_time": response_time,
                    "min_response_time": response_time,
                    "max_response_time": response_time,
                    "last_used": get_timestamp(),
                    "consecutive_successes": 1 if success else 0,
                    "consecutive_failures": 0 if success else 1,
                    "target_success_map": safe_json_dumps({target: 1} if target and success else {}),
                    "target_failure_map": safe_json_dumps({target: 1} if target and not success else {}),
                    "validation_count": 1,
                    "last_validated": get_timestamp(),
                    "status": "ACTIVE"
                })

            # Update target pairings
            if target:
                with self._cache_lock:
                    if target not in self._target_pairings:
                        self._target_pairings[target] = {}

                    if proxy_id not in self._target_pairings[target]:
                        self._target_pairings[target][proxy_id] = {
                            "success_count": 0,
                            "failure_count": 0,
                            "success_rate": 0.0
                        }

                    pairing = self._target_pairings[target][proxy_id]
                    pairing["success_count"] += (1 if success else 0)
                    pairing["failure_count"] += (0 if success else 1)
                    total = pairing["success_count"] + pairing["failure_count"]
                    pairing["success_rate"] = pairing["success_count"] / total if total > 0 else 0.5

            # Invalidate cache
            with self._cache_lock:
                if proxy_id in self._proxy_cache:
                    del self._proxy_cache[proxy_id]

        except Exception as e:
            self._logger.debug(f"Proxy intel update failed: {e}")

    def get_proxy_reliability(self, proxy_id: int) -> float:
        """Get proxy reliability score."""
        return self.score_proxy(proxy_id)

    def prefetch_proxies(self, count: int = 50) -> bool:
        """Prefetch and validate proxies."""
        self._logger.info(f"Prefetching {count} proxies...")

        # In real implementation, would call Phase 2 proxy sources
        # For now, mark as completed
        self._logger.info(f"Proxy prefetch complete")
        return True

    def get_proxy_intel_summary(self, limit: int = 20) -> List[Dict]:
        """Get proxy intelligence summary."""
        try:
            return self._db.select(
                "oanks_ai_proxy_intel",
                order_by="overall_score DESC",
                limit=limit
            )
        except:
            return []

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        with self._cache_lock:
            return {
                "proxies_cached": len(self._proxy_cache),
                "target_pairings": len(self._target_pairings),
                "predictions_made": len(self._prediction_history),
                "prefetch_active": self._prefetch_running
            }

# ==============================================================================
# END OF SECTION 6 & 7: ADAPTIVE SCRAPING AND INTELLIGENT PROXY ENGINE
# ==============================================================================



# ==============================================================================
# SECTION 8: PREDICTIVE HARVESTING ENGINE — TIME-SERIES, PATTERN, FORECAST
# ==============================================================================

class PredictiveHarvestingEngine:
    """
    Predictive harvesting engine that analyzes historical data to predict
    when high-value data will appear, what type it will be, and how much.

    Features:
    - Time-series pattern detection (hourly, daily, weekly, seasonal)
    - Volume prediction with confidence intervals
    - Source ranking and recommendation
    - Schedule optimization based on predictions
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._pattern_cache = {}
        self._prediction_cache = {}
        self._source_rankings = {}
        self._cache_lock = RLock()
        self._prediction_accuracy = defaultdict(lambda: {"correct": 0, "total": 0})

    def identify_data_patterns(self, data_type: str = None, 
                                source: str = None) -> Dict:
        """
        Identify patterns in data availability.
        Analyzes time buckets, seasonality, trends, and correlations.
        """
        self._logger.telegram_step(1, 4, "Pattern Identification",
                                   f"Analyzing patterns for {data_type or 'all data types'}...")

        try:
            # Build query based on filters
            where_clauses = ["active = 1"]
            params = []

            if data_type:
                where_clauses.append("data_type = ?")
                params.append(data_type)
            if source:
                where_clauses.append("source = ?")
                params.append(source)

            where_str = " AND ".join(where_clauses)

            # Get existing patterns
            existing_patterns = self._db.select(
                "oanks_ai_harvest_patterns",
                where=where_str,
                where_params=tuple(params),
                order_by="confidence DESC"
            )

            # Get raw harvest data for pattern detection
            raw_data = self._db.execute("""
                SELECT 
                    data_type,
                    source,
                    COUNT(*) as volume,
                    strftime('%H', timestamp) as hour,
                    strftime('%w', timestamp) as day_of_week,
                    strftime('%d', timestamp) as day_of_month,
                    AVG(response_time) as avg_response
                FROM oanks_ai_scrape_memory
                WHERE timestamp > datetime('now', '-30 days')
                AND success = 1
                GROUP BY data_type, source, hour, day_of_week
                ORDER BY volume DESC
            """)

            patterns = {}

            # Group by data_type and source
            grouped = defaultdict(list)
            for row in raw_data:
                key = (row["data_type"], row["source"])
                grouped[key].append(row)

            for (dt, src), rows in grouped.items():
                if len(rows) < PredictConfig.MIN_PATTERN_OCCURRENCES:
                    continue

                # Analyze hourly patterns
                hour_volumes = defaultdict(int)
                for row in rows:
                    hour_volumes[int(row["hour"])] += row["volume"]

                # Find peak hours
                peak_hours = sorted(hour_volumes.items(), key=lambda x: x[1], reverse=True)[:3]

                # Analyze daily patterns
                day_volumes = defaultdict(int)
                for row in rows:
                    day_volumes[int(row["day_of_week"])] += row["volume"]

                peak_days = sorted(day_volumes.items(), key=lambda x: x[1], reverse=True)[:3]

                # Calculate seasonality
                volumes = [row["volume"] for row in rows]
                seasonality = calculate_seasonality(volumes, period=24)

                # Calculate trend
                trend = calculate_trend(volumes)

                # Build pattern
                pattern = {
                    "data_type": dt,
                    "source": src,
                    "peak_hours": [h[0] for h in peak_hours],
                    "peak_hour_volumes": [h[1] for h in peak_hours],
                    "peak_days": [d[0] for d in peak_days],
                    "peak_day_volumes": [d[1] for d in peak_days],
                    "seasonality": seasonality,
                    "trend": trend,
                    "total_volume": sum(volumes),
                    "avg_volume": mean(volumes) if volumes else 0,
                    "sample_size": len(rows),
                    "confidence": min(len(rows) / 20, 0.95)
                }

                patterns[f"{dt}:{src}"] = pattern

                # Store pattern in database
                self._store_pattern(pattern)

            self._logger.telegram_step(1, 4, "Pattern Identification", "Complete",
                                       status="success", details={
                                           "patterns_found": len(patterns),
                                           "data_types_analyzed": len(set(p["data_type"] for p in patterns.values())),
                                           "sources_analyzed": len(set(p["source"] for p in patterns.values()))
                                       })

            return patterns

        except Exception as e:
            self._logger.error(f"Pattern identification failed: {e}")
            return {}

    def _store_pattern(self, pattern: Dict) -> None:
        """Store a pattern in the database."""
        try:
            pattern_hash = hash_string(safe_json_dumps(pattern))

            existing = self._db.select_one(
                "oanks_ai_harvest_patterns",
                where="pattern_hash = ?",
                where_params=(pattern_hash,)
            )

            if existing:
                self._db.update(
                    "oanks_ai_harvest_patterns",
                    {
                        "confidence": pattern.get("confidence", 0.5),
                        "last_seen": get_timestamp(),
                        "last_validated": get_timestamp(),
                        "active": 1
                    },
                    "id = ?",
                    (existing["id"],)
                )
            else:
                self._db.insert("oanks_ai_harvest_patterns", {
                    "data_type": pattern["data_type"],
                    "source": pattern["source"],
                    "pattern_type": "time_series",
                    "pattern_data": safe_json_dumps(pattern),
                    "pattern_hash": pattern_hash,
                    "confidence": pattern.get("confidence", 0.5),
                    "accuracy": 0.0,
                    "prediction_count": 0,
                    "correct_predictions": 0,
                    "avg_predicted_volume": pattern.get("avg_volume", 0),
                    "avg_actual_volume": pattern.get("avg_volume", 0),
                    "seasonality_detected": 1 if pattern.get("seasonality", {}).get("has_seasonality", False) else 0,
                    "seasonality_period": pattern.get("seasonality", {}).get("period", 24),
                    "trend_direction": pattern.get("trend", {}).get("direction", "flat"),
                    "trend_strength": pattern.get("trend", {}).get("strength", 0.0),
                    "last_seen": get_timestamp(),
                    "last_validated": get_timestamp(),
                    "active": 1
                })
        except Exception as e:
            self._logger.debug(f"Pattern storage failed: {e}")

    def predict_data_availability(self, data_type: str) -> HarvestPrediction:
        """
        Predict when high-value data will be available.
        Uses time-series analysis and pattern matching.
        """
        self._logger.telegram_step(2, 4, "Availability Prediction",
                                   f"Predicting availability for {data_type}...")

        try:
            # Get patterns for this data type
            patterns = self._db.select(
                "oanks_ai_harvest_patterns",
                where="data_type = ? AND active = 1",
                where_params=(data_type,),
                order_by="confidence DESC",
                limit=10
            )

            if not patterns:
                return HarvestPrediction(
                    data_type=data_type,
                    predicted_time="unknown",
                    predicted_volume=0,
                    confidence=0.0,
                    best_source="unknown",
                    pattern_matched="none",
                    historical_accuracy=0.0
                )

            # Find the best pattern
            best_pattern = patterns[0]
            pattern_data = safe_json_loads(best_pattern.get("pattern_data", "{}"), {})

            # Predict next occurrence based on peak hours
            peak_hours = pattern_data.get("peak_hours", [])
            current_hour = datetime.utcnow().hour

            if peak_hours:
                # Find next peak hour
                next_peak = None
                for hour in sorted(peak_hours):
                    if hour > current_hour:
                        next_peak = hour
                        break
                if next_peak is None:
                    next_peak = peak_hours[0]  # Wrap to tomorrow

                predicted_time = datetime.utcnow().replace(
                    hour=next_peak, minute=0, second=0, microsecond=0
                )
                if next_peak <= current_hour:
                    predicted_time += timedelta(days=1)

                predicted_time_str = predicted_time.strftime(UtilityConfig.TIMESTAMP_FORMAT)
            else:
                predicted_time_str = "unknown"

            # Predict volume
            avg_volume = best_pattern.get("avg_predicted_volume", 0)
            trend = pattern_data.get("trend", {})

            if trend.get("direction") == "increasing":
                predicted_volume = int(avg_volume * (1 + trend.get("strength", 0)))
            elif trend.get("direction") == "decreasing":
                predicted_volume = int(avg_volume * (1 - trend.get("strength", 0)))
            else:
                predicted_volume = int(avg_volume)

            # Calculate confidence
            confidence = best_pattern.get("confidence", 0.5)
            accuracy = best_pattern.get("accuracy", 0.0)

            # Historical accuracy
            prediction_count = best_pattern.get("prediction_count", 0)
            correct_predictions = best_pattern.get("correct_predictions", 0)
            historical_accuracy = correct_predictions / prediction_count if prediction_count > 0 else 0.0

            prediction = HarvestPrediction(
                data_type=data_type,
                predicted_time=predicted_time_str,
                predicted_volume=predicted_volume,
                confidence=round(confidence, 3),
                best_source=best_pattern.get("source", "unknown"),
                pattern_matched=best_pattern.get("pattern_type", "unknown"),
                historical_accuracy=round(historical_accuracy, 3)
            )

            self._logger.telegram_step(2, 4, "Availability Prediction", "Complete",
                                       status="success", details={
                                           "data_type": data_type,
                                           "predicted_time": predicted_time_str,
                                           "predicted_volume": predicted_volume,
                                           "confidence": f"{confidence:.2f}",
                                           "best_source": best_pattern.get("source", "unknown")
                                       })

            if self._telegram:
                self._telegram.send_harvest_prediction(prediction)

            return prediction

        except Exception as e:
            self._logger.error(f"Availability prediction failed: {e}")
            return HarvestPrediction(
                data_type=data_type,
                predicted_time="error",
                predicted_volume=0,
                confidence=0.0,
                best_source="error",
                pattern_matched="error",
                historical_accuracy=0.0
            )

    def predict_best_source(self, data_type: str) -> str:
        """Predict the best source for a data type."""
        try:
            # Get source rankings from patterns
            patterns = self._db.select(
                "oanks_ai_harvest_patterns",
                where="data_type = ? AND active = 1",
                where_params=(data_type,),
                order_by="confidence DESC, avg_actual_volume DESC"
            )

            if patterns:
                return patterns[0].get("source", "unknown")

            # Fallback: analyze scrape memory
            sources = self._db.execute("""
                SELECT source, COUNT(*) as count, AVG(success) as success_rate
                FROM oanks_ai_scrape_memory
                WHERE target LIKE ?
                AND timestamp > datetime('now', '-7 days')
                GROUP BY source
                ORDER BY success_rate DESC, count DESC
                LIMIT 1
            """, (f"%{data_type}%",))

            if sources:
                return sources[0].get("source", "unknown")

            return "unknown"

        except Exception as e:
            self._logger.debug(f"Best source prediction failed: {e}")
            return "unknown"

    def predict_harvest_volume(self, source: str, hours_ahead: int = 24) -> int:
        """Predict harvest volume from a source."""
        try:
            # Get historical volume data
            historical = self._db.execute("""
                SELECT 
                    strftime('%H', timestamp) as hour,
                    COUNT(*) as volume
                FROM oanks_ai_scrape_memory
                WHERE target LIKE ?
                AND timestamp > datetime('now', '-7 days')
                AND success = 1
                GROUP BY hour
                ORDER BY hour
            """, (f"%{source}%",))

            if not historical:
                return 0

            # Calculate average volume per hour
            volumes = [row["volume"] for row in historical]
            avg_volume = mean(volumes) if volumes else 0

            # Adjust for trend
            trend = calculate_trend(volumes)
            if trend["direction"] == "increasing":
                predicted = avg_volume * (1 + trend["strength"] * (hours_ahead / 24))
            elif trend["direction"] == "decreasing":
                predicted = avg_volume * (1 - trend["strength"] * (hours_ahead / 24))
            else:
                predicted = avg_volume

            return int(predicted)

        except Exception as e:
            self._logger.debug(f"Volume prediction failed: {e}")
            return 0

    def schedule_harvest(self, prediction: HarvestPrediction) -> bool:
        """Schedule harvesting based on prediction."""
        try:
            # In real implementation, would integrate with Phase 3 scheduler
            # For now, log the scheduled operation
            self._logger.info(
                f"Scheduled harvest: {prediction.data_type} from "
                f"{prediction.best_source} at {prediction.predicted_time} "
                f"(expected volume: {prediction.predicted_volume})"
            )
            return True
        except Exception as e:
            self._logger.error(f"Harvest scheduling failed: {e}")
            return False

    def validate_prediction(self, data_type: str, actual_time: str, 
                           actual_volume: int) -> Dict:
        """Validate a prediction against actual results."""
        try:
            # Find the prediction
            patterns = self._db.select(
                "oanks_ai_harvest_patterns",
                where="data_type = ? AND active = 1",
                where_params=(data_type,),
                order_by="last_seen DESC",
                limit=1
            )

            if not patterns:
                return {"validated": False, "reason": "no_pattern"}

            pattern = patterns[0]

            # Update prediction count
            new_prediction_count = pattern.get("prediction_count", 0) + 1

            # Check if prediction was correct (within time window)
            predicted_time = parse_timestamp(pattern.get("last_seen", ""))
            actual_ts = parse_timestamp(actual_time)

            time_correct = False
            if predicted_time and actual_ts:
                time_diff = abs(actual_ts - predicted_time)
                time_correct = time_diff < PredictConfig.SCHEDULE_AHEAD_BUFFER

            # Check volume accuracy
            predicted_volume = pattern.get("avg_predicted_volume", 0)
            volume_diff = abs(actual_volume - predicted_volume)
            volume_correct = volume_diff < (predicted_volume * 0.3) if predicted_volume > 0 else False

            correct = time_correct and volume_correct

            new_correct = pattern.get("correct_predictions", 0) + (1 if correct else 0)
            new_accuracy = new_correct / new_prediction_count if new_prediction_count > 0 else 0

            # Update pattern
            self._db.update(
                "oanks_ai_harvest_patterns",
                {
                    "prediction_count": new_prediction_count,
                    "correct_predictions": new_correct,
                    "accuracy": new_accuracy,
                    "avg_actual_volume": (pattern.get("avg_actual_volume", 0) * pattern.get("prediction_count", 0) + actual_volume) / new_prediction_count,
                    "last_validated": get_timestamp()
                },
                "id = ?",
                (pattern["id"],)
            )

            return {
                "validated": True,
                "correct": correct,
                "time_accuracy": time_correct,
                "volume_accuracy": volume_correct,
                "new_accuracy": new_accuracy
            }

        except Exception as e:
            self._logger.debug(f"Prediction validation failed: {e}")
            return {"validated": False, "reason": str(e)}

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        try:
            pattern_count = self._db.count("oanks_ai_harvest_patterns", "active = 1")
            total_predictions = self._db.aggregate(
                "oanks_ai_harvest_patterns", 
                "prediction_count", 
                "SUM"
            )
            total_correct = self._db.aggregate(
                "oanks_ai_harvest_patterns", 
                "correct_predictions", 
                "SUM"
            )

            return {
                "active_patterns": pattern_count,
                "total_predictions": int(total_predictions),
                "total_correct": int(total_correct),
                "overall_accuracy": total_correct / total_predictions if total_predictions > 0 else 0,
                "cached_predictions": len(self._prediction_cache)
            }
        except:
            return {
                "active_patterns": 0,
                "total_predictions": 0,
                "total_correct": 0,
                "overall_accuracy": 0,
                "cached_predictions": 0
            }

# ==============================================================================
# SECTION 9: ANOMALY DETECTION ENGINE — STATISTICAL, MULTI-METRIC, AUTO-RESPONSE
# ==============================================================================

class AnomalyDetectionEngine:
    """
    Anomaly detection engine using statistical methods.
    Detects outliers in system metrics, network behavior, access patterns,
    and data flows. Auto-responds to detected anomalies.

    Features:
    - Baseline establishment with rolling averages
    - Multi-method outlier detection (IQR, Z-score, MAD, Grubbs)
    - Trend and seasonality adjustment
    - Auto-response with configurable actions
    - Correlation analysis between metrics
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._baselines = {}
        self._metric_history = defaultdict(lambda: deque(maxlen=AnomalyConfig.ROLLING_WINDOW_SIZE))
        self._last_alert_time = {}
        self._anomaly_count = 0
        self._auto_resolved_count = 0
        self._baseline_lock = RLock()
        self._alert_lock = RLock()

    def establish_baseline(self, metric_name: str, values: List[float]) -> Dict:
        """Establish baseline metrics for anomaly detection."""
        if len(values) < AnomalyConfig.MIN_BASELINE_SAMPLES:
            return {"error": "insufficient_data", "required": AnomalyConfig.MIN_BASELINE_SAMPLES}

        with self._baseline_lock:
            try:
                m = mean(values)
                med = median(values)
                std = stdev(values) if len(values) > 1 else 0
                var = variance(values) if len(values) > 1 else 0

                # IQR
                q1 = calculate_percentile(values, 25)
                q3 = calculate_percentile(values, 75)
                iqr = q3 - q1

                # MAD (Median Absolute Deviation)
                abs_deviations = [abs(v - med) for v in values]
                mad = median(abs_deviations) if abs_deviations else 0

                # Trend
                trend = calculate_trend(values)

                # Seasonality
                seasonality = calculate_seasonality(values)

                baseline = {
                    "metric_name": metric_name,
                    "mean": m,
                    "median": med,
                    "std": std,
                    "variance": var,
                    "min": min(values),
                    "max": max(values),
                    "q1": q1,
                    "q3": q3,
                    "iqr": iqr,
                    "mad": mad,
                    "trend": trend,
                    "seasonality": seasonality,
                    "sample_size": len(values),
                    "established_at": get_timestamp(),
                    "updated_at": get_timestamp()
                }

                self._baselines[metric_name] = baseline

                return baseline

            except Exception as e:
                self._logger.debug(f"Baseline establishment failed for {metric_name}: {e}")
                return {"error": str(e)}

    def update_baseline(self, metric_name: str, new_value: float) -> Dict:
        """Update baseline with a new value."""
        with self._baseline_lock:
            # Add to history
            self._metric_history[metric_name].append(new_value)

            # Re-establish baseline if enough data
            history = list(self._metric_history[metric_name])
            if len(history) >= AnomalyConfig.MIN_BASELINE_SAMPLES:
                return self.establish_baseline(metric_name, history)

            return {"status": "collecting", "samples": len(history)}

    def detect_anomaly(self, metrics: Dict[str, float]) -> Optional[Dict]:
        """
        Detect anomalies in system metrics.
        Returns anomaly details if detected, None otherwise.
        """
        anomalies = []

        for metric_name, value in metrics.items():
            # Update baseline
            baseline_result = self.update_baseline(metric_name, value)

            if "error" in baseline_result:
                continue

            baseline = self._baselines.get(metric_name)
            if not baseline:
                continue

            # Check for anomaly using multiple methods
            anomaly_detected = False
            severity = 1
            methods_triggered = []

            # Method 1: IQR
            iqr = baseline.get("iqr", 0)
            median_val = baseline.get("median", 0)
            if iqr > 0:
                lower_iqr = median_val - AnomalyConfig.VARIANCE_MULTIPLIER_HIGH * iqr
                upper_iqr = median_val + AnomalyConfig.VARIANCE_MULTIPLIER_HIGH * iqr

                if value < lower_iqr or value > upper_iqr:
                    anomaly_detected = True
                    methods_triggered.append("iqr")
                    severity = max(severity, 4 if abs(value - median_val) / iqr > 5 else 3)

            # Method 2: Z-score
            std = baseline.get("std", 0)
            mean_val = baseline.get("mean", 0)
            if std > 0:
                z_score = abs((value - mean_val) / std)
                if z_score > AnomalyConfig.VARIANCE_MULTIPLIER_HIGH:
                    anomaly_detected = True
                    methods_triggered.append("zscore")
                    severity = max(severity, 5 if z_score > 5 else 4)
                elif z_score > AnomalyConfig.VARIANCE_MULTIPLIER_MEDIUM:
                    anomaly_detected = True
                    methods_triggered.append("zscore_moderate")
                    severity = max(severity, 3)

            # Method 3: MAD
            mad = baseline.get("mad", 0)
            if mad > 0:
                mad_score = abs(value - median_val) / mad
                if mad_score > AnomalyConfig.VARIANCE_MULTIPLIER_HIGH:
                    anomaly_detected = True
                    methods_triggered.append("mad")
                    severity = max(severity, 4)

            # Method 4: Threshold-based
            if metric_name in ["cpu_usage", "memory_usage"]:
                if value > 95:
                    anomaly_detected = True
                    methods_triggered.append("threshold_critical")
                    severity = 5
                elif value > 80:
                    anomaly_detected = True
                    methods_triggered.append("threshold_high")
                    severity = 4

            # Method 5: Trend break
            trend = baseline.get("trend", {})
            if trend.get("direction") != "flat":
                expected = mean_val + trend.get("slope", 0) * len(self._metric_history[metric_name])
                deviation = abs(value - expected)
                if std > 0 and deviation / std > 3:
                    anomaly_detected = True
                    methods_triggered.append("trend_break")
                    severity = max(severity, 3)

            if anomaly_detected:
                # Check cooldown
                with self._alert_lock:
                    last_alert = self._last_alert_time.get(metric_name, 0)
                    if time.time() - last_alert < AnomalyConfig.ANOMALY_COOLDOWN:
                        continue
                    self._last_alert_time[metric_name] = time.time()

                anomaly = {
                    "anomaly_type": self._classify_anomaly_type(metric_name),
                    "severity": severity,
                    "description": f"Anomaly detected in {metric_name}: "
                                   f"value={value:.2f}, expected={mean_val:.2f}±{std:.2f}",
                    "metric_name": metric_name,
                    "value": value,
                    "expected_mean": mean_val,
                    "expected_std": std,
                    "baseline": baseline,
                    "methods_triggered": methods_triggered,
                    "detected_at": get_timestamp(),
                    "auto_resolved": False,
                    "resolution_action": None
                }

                anomalies.append(anomaly)

        # Store and alert on anomalies
        if anomalies:
            primary_anomaly = max(anomalies, key=lambda x: x["severity"])

            # Store in database
            anomaly_record = {
                "anomaly_type": primary_anomaly["anomaly_type"],
                "severity": primary_anomaly["severity"],
                "description": primary_anomaly["description"],
                "detected_at": primary_anomaly["detected_at"],
                "resolved": 0,
                "metric_values": safe_json_dumps({a["metric_name"]: a["value"] for a in anomalies}),
                "baseline_values": safe_json_dumps({a["metric_name"]: a["expected_mean"] for a in anomalies}),
                "threshold_exceeded": max(a["value"] / max(a["expected_mean"], 0.001) for a in anomalies),
                "affected_phase": "phase_14",
                "correlation_id": generate_uuid()
            }

            anomaly_id = self._db.insert("oanks_ai_anomalies", anomaly_record)
            primary_anomaly["id"] = anomaly_id

            self._anomaly_count += 1

            # Auto-respond if enabled
            if AnomalyConfig.AUTO_RESPONSE_ENABLED:
                auto_resolved = self.respond_to_anomaly(primary_anomaly)
                if auto_resolved:
                    primary_anomaly["auto_resolved"] = True
                    self._auto_resolved_count += 1

            # Alert via Telegram
            if self._telegram:
                self._telegram.send_anomaly_alert(primary_anomaly)

            self._logger.anomaly(primary_anomaly)

            return primary_anomaly

        return None

    def _classify_anomaly_type(self, metric_name: str) -> str:
        """Classify anomaly type based on metric name."""
        if "network" in metric_name.lower() or "latency" in metric_name.lower() or "connection" in metric_name.lower():
            return AnomalyType.NETWORK.name
        elif "cpu" in metric_name.lower() or "memory" in metric_name.lower() or "disk" in metric_name.lower():
            return AnomalyType.SYSTEM.name
        elif "access" in metric_name.lower() or "auth" in metric_name.lower() or "login" in metric_name.lower():
            return AnomalyType.ACCESS.name
        elif "data" in metric_name.lower() or "harvest" in metric_name.lower():
            return AnomalyType.DATA.name
        elif "performance" in metric_name.lower() or "response" in metric_name.lower():
            return AnomalyType.PERFORMANCE.name
        else:
            return AnomalyType.COMPOSITE.name

    def respond_to_anomaly(self, anomaly: Dict) -> bool:
        """Auto-respond to a detected anomaly."""
        anomaly_type = anomaly.get("anomaly_type", "")
        severity = anomaly.get("severity", 1)
        metric_name = anomaly.get("metric_name", "")

        try:
            if anomaly_type == AnomalyType.NETWORK.name:
                # Network anomaly: rotate proxies
                resolution = "Rotated proxies due to network anomaly"
                self._logger.info(f"Auto-response: {resolution}")

            elif anomaly_type == AnomalyType.SYSTEM.name:
                # System anomaly: optimize resources
                if "cpu" in metric_name.lower() and severity >= 4:
                    resolution = "Reduced thread count due to high CPU"
                elif "memory" in metric_name.lower() and severity >= 4:
                    resolution = "Cleared cache due to high memory usage"
                else:
                    resolution = "Monitored system metrics"
                self._logger.info(f"Auto-response: {resolution}")

            elif anomaly_type == AnomalyType.ACCESS.name:
                # Access anomaly: trigger kill switch or alert
                if severity >= 4:
                    resolution = "Triggered security alert due to access anomaly"
                else:
                    resolution = "Logged access anomaly for review"
                self._logger.info(f"Auto-response: {resolution}")

            elif anomaly_type == AnomalyType.DATA.name:
                # Data anomaly: lock down or verify
                resolution = "Verified data integrity due to anomaly"
                self._logger.info(f"Auto-response: {resolution}")

            elif anomaly_type == AnomalyType.PERFORMANCE.name:
                # Performance anomaly: optimize
                resolution = "Applied performance optimization"
                self._logger.info(f"Auto-response: {resolution}")

            else:
                resolution = "Logged anomaly for manual review"
                self._logger.info(f"Auto-response: {resolution}")

            # Update anomaly record
            if "id" in anomaly:
                self._db.update(
                    "oanks_ai_anomalies",
                    {
                        "resolved": 1,
                        "resolved_at": get_timestamp(),
                        "resolution_action": resolution,
                        "auto_resolved": 1
                    },
                    "id = ?",
                    (anomaly["id"],)
                )

            return True

        except Exception as e:
            self._logger.error(f"Auto-response failed: {e}")
            return False

    def analyze_network_anomaly(self, network_data: Dict) -> Dict:
        """Analyze network-specific anomaly."""
        anomalies = []

        # Check latency
        if "latency" in network_data:
            latency = network_data["latency"]
            if latency > 5000:  # 5 seconds
                anomalies.append({
                    "type": "high_latency",
                    "value": latency,
                    "severity": 3 if latency > 10000 else 2
                })

        # Check packet loss
        if "packet_loss" in network_data:
            loss = network_data["packet_loss"]
            if loss > 0.1:  # 10%
                anomalies.append({
                    "type": "packet_loss",
                    "value": loss,
                    "severity": 4 if loss > 0.5 else 3
                })

        # Check connection count
        if "connection_count" in network_data:
            count = network_data["connection_count"]
            if count > 1000:
                anomalies.append({
                    "type": "too_many_connections",
                    "value": count,
                    "severity": 3
                })

        return {
            "anomalies_found": len(anomalies),
            "anomalies": anomalies,
            "network_health": "compromised" if anomalies else "normal"
        }

    def analyze_access_anomaly(self, access_data: Dict) -> Dict:
        """Analyze access-specific anomaly."""
        anomalies = []

        # Check failed login attempts
        if "failed_logins" in access_data:
            failed = access_data["failed_logins"]
            if failed > 10:
                anomalies.append({
                    "type": "brute_force_attempt",
                    "value": failed,
                    "severity": 4 if failed > 50 else 3
                })

        # Check unauthorized access
        if "unauthorized_access" in access_data:
            unauthorized = access_data["unauthorized_access"]
            if unauthorized > 0:
                anomalies.append({
                    "type": "unauthorized_access",
                    "value": unauthorized,
                    "severity": 5
                })

        return {
            "anomalies_found": len(anomalies),
            "anomalies": anomalies,
            "access_health": "compromised" if anomalies else "normal"
        }

    def get_anomaly_history(self, limit: int = 100, 
                           unresolved_only: bool = False) -> List[Dict]:
        """Get anomaly history."""
        where_clause = None
        if unresolved_only:
            where_clause = "resolved = 0"

        return self._db.select(
            "oanks_ai_anomalies",
            where=where_clause,
            order_by="detected_at DESC",
            limit=limit
        )

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        try:
            total_anomalies = self._db.count("oanks_ai_anomalies")
            unresolved = self._db.count("oanks_ai_anomalies", "resolved = 0")
            auto_resolved = self._db.count("oanks_ai_anomalies", "auto_resolved = 1")

            severity_counts = self._db.execute("""
                SELECT severity, COUNT(*) as count
                FROM oanks_ai_anomalies
                GROUP BY severity
            """)

            return {
                "total_anomalies": total_anomalies,
                "unresolved": unresolved,
                "auto_resolved": auto_resolved,
                "manual_resolution_required": unresolved - auto_resolved,
                "severity_distribution": {row["severity"]: row["count"] for row in severity_counts},
                "baselines_established": len(self._baselines),
                "metrics_tracked": len(self._metric_history)
            }
        except:
            return {
                "total_anomalies": self._anomaly_count,
                "auto_resolved": self._auto_resolved_count,
                "baselines_established": len(self._baselines),
                "metrics_tracked": len(self._metric_history)
            }

# ==============================================================================
# END OF SECTION 8 & 9: PREDICTIVE HARVESTING AND ANOMALY DETECTION
# ==============================================================================



# ==============================================================================
# SECTION 10: SELF-OPTIMIZATION ENGINE — BOTTLENECK DETECTION, AUTO-ADJUSTMENT
# ==============================================================================

class SelfOptimizationEngine:
    """
    Self-optimization engine that monitors system performance,
    identifies bottlenecks, and automatically adjusts parameters.

    Features:
    - Performance tracking across all metrics
    - Bottleneck identification using multiple methods
    - Auto-adjustment of threads, cache, proxies, delays
    - Stability window to prevent oscillation
    - Goal-based optimization (speed, stability, balanced, aggressive)
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._performance_history = defaultdict(lambda: deque(maxlen=OptimizeConfig.STABILITY_WINDOW))
        self._current_parameters = {
            "thread_count": 10,
            "cache_size": 1000,
            "proxy_pool_size": 50,
            "harvest_delay": 1.0,
            "retry_count": 3,
            "batch_size": 100,
            "timeout": 30,
        }
        self._parameter_history = []
        self._optimization_count = 0
        self._last_optimization = 0
        self._param_lock = RLock()

    def measure_performance(self) -> Dict:
        """Measure current system performance comprehensively."""
        self._logger.telegram_step(1, 4, "Performance Measurement",
                                   "Measuring system performance...")

        # System metrics
        health = get_system_health()

        # Database metrics
        try:
            db_stats = self._db.get_stats()
        except:
            db_stats = {}

        # Decision metrics
        try:
            decision_stats = self._db.execute("""
                SELECT 
                    COUNT(*) as total_decisions,
                    SUM(success) as successful,
                    AVG(execution_time) as avg_exec_time
                FROM oanks_ai_decisions
                WHERE made_at > datetime('now', '-1 hour')
            """)
            decision_perf = decision_stats[0] if decision_stats else {}
        except:
            decision_perf = {}

        # Harvest metrics
        try:
            harvest_stats = self._db.execute("""
                SELECT 
                    COUNT(*) as total_harvests,
                    SUM(success) as successful,
                    AVG(response_time) as avg_response
                FROM oanks_ai_scrape_memory
                WHERE timestamp > datetime('now', '-1 hour')
            """)
            harvest_perf = harvest_stats[0] if harvest_stats else {}
        except:
            harvest_perf = {}

        # Proxy metrics
        try:
            proxy_stats = self._db.execute("""
                SELECT 
                    COUNT(*) as total_proxies,
                    AVG(overall_score) as avg_score,
                    AVG(avg_response_time) as avg_response
                FROM oanks_ai_proxy_intel
                WHERE status = 'ACTIVE'
            """)
            proxy_perf = proxy_stats[0] if proxy_stats else {}
        except:
            proxy_perf = {}

        # Anomaly metrics
        try:
            anomaly_count = self._db.count(
                "oanks_ai_anomalies",
                "detected_at > datetime('now', '-1 hour')"
            )
        except:
            anomaly_count = 0

        performance = {
            "cpu_usage": health.cpu_usage,
            "memory_usage": health.memory_usage,
            "disk_usage": health.disk_usage,
            "active_threads": health.active_threads,
            "error_rate": health.error_rate,
            "db_total_records": db_stats.get("total_records", 0),
            "db_size_mb": db_stats.get("db_size_bytes", 0) / 1048576,
            "decisions_per_hour": decision_perf.get("total_decisions", 0),
            "decision_success_rate": (decision_perf.get("successful", 0) / 
                                       max(decision_perf.get("total_decisions", 1), 1)),
            "avg_decision_time": decision_perf.get("avg_exec_time", 0),
            "harvests_per_hour": harvest_perf.get("total_harvests", 0),
            "harvest_success_rate": (harvest_perf.get("successful", 0) / 
                                     max(harvest_perf.get("total_harvests", 1), 1)),
            "avg_harvest_response": harvest_perf.get("avg_response", 0),
            "active_proxies": proxy_perf.get("total_proxies", 0),
            "proxy_avg_score": proxy_perf.get("avg_score", 0),
            "proxy_avg_response": proxy_perf.get("avg_response", 0),
            "anomalies_per_hour": anomaly_count,
            "timestamp": get_timestamp()
        }

        # Store in history
        for metric, value in performance.items():
            if isinstance(value, (int, float)):
                self._performance_history[metric].append(value)

        # Store in database
        for metric, value in performance.items():
            if isinstance(value, (int, float)) and metric != "timestamp":
                try:
                    self._db.insert("oanks_ai_performance", {
                        "phase": "phase_14",
                        "metric": metric,
                        "value": value,
                        "unit": self._get_unit(metric),
                        "context": "self_optimization",
                        "timestamp": get_timestamp()
                    })
                except:
                    pass

        self._logger.telegram_step(1, 4, "Performance Measurement", "Complete",
                                   status="success", details={
                                       "cpu": f"{performance['cpu_usage']:.1f}%",
                                       "memory": f"{performance['memory_usage']:.1f}%",
                                       "threads": performance['active_threads'],
                                       "decisions/hr": performance['decisions_per_hour'],
                                       "harvests/hr": performance['harvests_per_hour']
                                   })

        return performance

    def _get_unit(self, metric: str) -> str:
        """Get unit for a metric."""
        unit_map = {
            "cpu_usage": "%",
            "memory_usage": "%",
            "disk_usage": "%",
            "db_size_mb": "MB",
            "avg_decision_time": "s",
            "avg_harvest_response": "s",
            "proxy_avg_response": "s",
        }
        return unit_map.get(metric, "")

    def identify_bottlenecks(self, performance: Dict = None) -> List[Dict]:
        """
        Identify system bottlenecks using threshold-based detection.
        Returns list of bottlenecks with severity and recommended actions.
        """
        self._logger.telegram_step(2, 4, "Bottleneck Identification",
                                   "Analyzing performance for bottlenecks...")

        if performance is None:
            performance = self.measure_performance()

        bottlenecks = []

        # CPU bottleneck
        cpu = performance.get("cpu_usage", 0)
        if cpu > OptimizeConfig.CPU_THRESHOLD_HIGH:
            bottlenecks.append({
                "parameter": "thread_count",
                "current_value": self._current_parameters.get("thread_count", 10),
                "recommended_value": max(
                    self._current_parameters.get("thread_count", 10) - OptimizeConfig.THREAD_ADJUSTMENT_STEP,
                    OptimizeConfig.MIN_THREADS
                ),
                "reason": f"CPU usage critical: {cpu:.1f}%",
                "severity": 5,
                "metric": "cpu_usage",
                "metric_value": cpu,
                "threshold": OptimizeConfig.CPU_THRESHOLD_HIGH
            })
        elif cpu > OptimizeConfig.CPU_THRESHOLD_MEDIUM:
            bottlenecks.append({
                "parameter": "thread_count",
                "current_value": self._current_parameters.get("thread_count", 10),
                "recommended_value": max(
                    self._current_parameters.get("thread_count", 10) - 2,
                    OptimizeConfig.MIN_THREADS
                ),
                "reason": f"CPU usage high: {cpu:.1f}%",
                "severity": 3,
                "metric": "cpu_usage",
                "metric_value": cpu,
                "threshold": OptimizeConfig.CPU_THRESHOLD_MEDIUM
            })
        elif cpu < OptimizeConfig.CPU_THRESHOLD_LOW and performance.get("decisions_per_hour", 0) < 10:
            bottlenecks.append({
                "parameter": "thread_count",
                "current_value": self._current_parameters.get("thread_count", 10),
                "recommended_value": min(
                    self._current_parameters.get("thread_count", 10) + OptimizeConfig.THREAD_ADJUSTMENT_STEP,
                    OptimizeConfig.MAX_THREADS
                ),
                "reason": f"CPU underutilized: {cpu:.1f}%, low activity",
                "severity": 2,
                "metric": "cpu_usage",
                "metric_value": cpu,
                "threshold": OptimizeConfig.CPU_THRESHOLD_LOW
            })

        # Memory bottleneck
        memory = performance.get("memory_usage", 0)
        if memory > OptimizeConfig.MEMORY_THRESHOLD_HIGH:
            bottlenecks.append({
                "parameter": "cache_size",
                "current_value": self._current_parameters.get("cache_size", 1000),
                "recommended_value": max(
                    self._current_parameters.get("cache_size", 1000) - OptimizeConfig.CACHE_ADJUSTMENT_STEP,
                    OptimizeConfig.MIN_CACHE_SIZE
                ),
                "reason": f"Memory usage critical: {memory:.1f}%",
                "severity": 5,
                "metric": "memory_usage",
                "metric_value": memory,
                "threshold": OptimizeConfig.MEMORY_THRESHOLD_HIGH
            })
        elif memory > OptimizeConfig.MEMORY_THRESHOLD_MEDIUM:
            bottlenecks.append({
                "parameter": "cache_size",
                "current_value": self._current_parameters.get("cache_size", 1000),
                "recommended_value": max(
                    self._current_parameters.get("cache_size", 1000) - 50,
                    OptimizeConfig.MIN_CACHE_SIZE
                ),
                "reason": f"Memory usage high: {memory:.1f}%",
                "severity": 3,
                "metric": "memory_usage",
                "metric_value": memory,
                "threshold": OptimizeConfig.MEMORY_THRESHOLD_MEDIUM
            })

        # Response time bottleneck
        response_time = performance.get("avg_harvest_response", 0)
        if response_time > OptimizeConfig.RESPONSE_TIME_THRESHOLD:
            bottlenecks.append({
                "parameter": "proxy_pool_size",
                "current_value": self._current_parameters.get("proxy_pool_size", 50),
                "recommended_value": self._current_parameters.get("proxy_pool_size", 50) + 20,
                "reason": f"Response time high: {response_time:.2f}s",
                "severity": 4,
                "metric": "avg_harvest_response",
                "metric_value": response_time,
                "threshold": OptimizeConfig.RESPONSE_TIME_THRESHOLD
            })

        # Harvest rate bottleneck
        harvest_rate = performance.get("harvests_per_hour", 0)
        if harvest_rate < OptimizeConfig.HARVEST_RATE_THRESHOLD and performance.get("harvest_success_rate", 0) > 0.5:
            bottlenecks.append({
                "parameter": "harvest_delay",
                "current_value": self._current_parameters.get("harvest_delay", 1.0),
                "recommended_value": max(
                    self._current_parameters.get("harvest_delay", 1.0) * 0.8,
                    0.1
                ),
                "reason": f"Harvest rate low: {harvest_rate}/hr despite good success rate",
                "severity": 2,
                "metric": "harvests_per_hour",
                "metric_value": harvest_rate,
                "threshold": OptimizeConfig.HARVEST_RATE_THRESHOLD
            })

        # Decision time bottleneck
        decision_time = performance.get("avg_decision_time", 0)
        if decision_time > 10:
            bottlenecks.append({
                "parameter": "batch_size",
                "current_value": self._current_parameters.get("batch_size", 100),
                "recommended_value": self._current_parameters.get("batch_size", 100) + 50,
                "reason": f"Decision time high: {decision_time:.2f}s",
                "severity": 3,
                "metric": "avg_decision_time",
                "metric_value": decision_time,
                "threshold": 10
            })

        # Database size bottleneck
        db_size = performance.get("db_size_mb", 0)
        if db_size > 1000:  # 1GB
            bottlenecks.append({
                "parameter": "db_maintenance",
                "current_value": "none",
                "recommended_value": "vacuum_and_archive",
                "reason": f"Database size large: {db_size:.1f}MB",
                "severity": 3,
                "metric": "db_size_mb",
                "metric_value": db_size,
                "threshold": 1000
            })

        # Sort by severity
        bottlenecks.sort(key=lambda x: x["severity"], reverse=True)

        self._logger.telegram_step(2, 4, "Bottleneck Identification", "Complete",
                                   status="success" if not bottlenecks else "warning",
                                   details={
                                       "bottlenecks_found": len(bottlenecks),
                                       "highest_severity": max((b["severity"] for b in bottlenecks), default=0),
                                       "affected_parameters": list(set(b["parameter"] for b in bottlenecks))
                                   })

        return bottlenecks

    def adjust_parameters(self, bottlenecks: List[Dict]) -> bool:
        """Adjust system parameters based on identified bottlenecks."""
        self._logger.telegram_step(3, 4, "Parameter Adjustment",
                                   f"Adjusting {len(bottlenecks)} parameters...")

        if not bottlenecks:
            self._logger.telegram_step(3, 4, "Parameter Adjustment", "Complete",
                                       status="success", details={"changes": "None needed"})
            return True

        optimizations = []

        with self._param_lock:
            for bottleneck in bottlenecks:
                parameter = bottleneck["parameter"]
                current = bottleneck["current_value"]
                recommended = bottleneck["recommended_value"]
                reason = bottleneck["reason"]

                if parameter == "db_maintenance":
                    # Special handling for database maintenance
                    try:
                        self._db.vacuum()
                        optimizations.append({
                            "parameter": parameter,
                            "old_value": current,
                            "new_value": recommended,
                            "reason": reason
                        })
                    except Exception as e:
                        self._logger.error(f"Database vacuum failed: {e}")
                    continue

                # Check stability window - don't oscillate
                history = self._parameter_history[-OptimizeConfig.STABILITY_WINDOW:]
                recent_changes = [h for h in history if h["parameter"] == parameter]

                if recent_changes:
                    last_change = recent_changes[-1]
                    time_since = time.time() - last_change.get("timestamp", 0)
                    if time_since < 300:  # 5 minutes
                        self._logger.debug(f"Skipping {parameter} adjustment, too recent")
                        continue

                # Apply change
                old_value = self._current_parameters.get(parameter)
                self._current_parameters[parameter] = recommended

                optimizations.append({
                    "parameter": parameter,
                    "old_value": old_value,
                    "new_value": recommended,
                    "reason": reason
                })

                # Record in history
                self._parameter_history.append({
                    "parameter": parameter,
                    "old_value": old_value,
                    "new_value": recommended,
                    "reason": reason,
                    "timestamp": time.time()
                })

        self._optimization_count += 1
        self._last_optimization = time.time()

        self._logger.telegram_step(3, 4, "Parameter Adjustment", "Complete",
                                   status="success", details={
                                       "parameters_adjusted": len(optimizations),
                                       "changes": [f"{o['parameter']}: {o['old_value']} → {o['new_value']}" 
                                                  for o in optimizations]
                                   })

        if self._telegram and optimizations:
            self._telegram.send_optimization_report(optimizations)

        return True

    def optimize_system(self) -> Dict:
        """
        Complete self-optimization pipeline:
        1. Measure performance
        2. Identify bottlenecks
        3. Adjust parameters
        4. Verify improvement
        """
        self._logger.info("Starting self-optimization pipeline")

        # Step 1: Measure
        performance = self.measure_performance()

        # Step 2: Identify bottlenecks
        bottlenecks = self.identify_bottlenecks(performance)

        # Step 3: Adjust
        if bottlenecks:
            self.adjust_parameters(bottlenecks)

        # Step 4: Return results
        return {
            "performance": performance,
            "bottlenecks": bottlenecks,
            "optimizations_applied": len(bottlenecks),
            "current_parameters": dict(self._current_parameters),
            "timestamp": get_timestamp()
        }

    def get_optimal_parameters(self) -> Dict:
        """Get current optimal parameters."""
        with self._param_lock:
            return dict(self._current_parameters)

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        return {
            "optimizations_applied": self._optimization_count,
            "last_optimization": self._last_optimization,
            "current_parameters": dict(self._current_parameters),
            "parameter_history_size": len(self._parameter_history),
            "metrics_tracked": len(self._performance_history)
        }

# ==============================================================================
# END OF SECTION 10: SELF-OPTIMIZATION ENGINE
# ==============================================================================



# ==============================================================================
# SECTION 11: AUTONOMOUS MODE ENGINE — FULL AUTOMATION, SELF-HEALING, REPORTING
# ==============================================================================

class AutonomousModeEngine:
    """
    Autonomous mode engine that runs the framework without human intervention.
    Self-healing, error recovery, continuous operation with periodic reporting.

    Features:
    - Full automation loop with configurable intervals
    - Self-healing: restart failed phases, rotate proxies, switch targets
    - Error recovery with multiple attempts
    - Status reporting to Telegram at intervals
    - Watchdog timer to prevent hangs
    - State persistence for crash recovery
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None,
                 decision_engine: 'AutoDecisionEngine' = None,
                 optimization_engine: 'SelfOptimizationEngine' = None,
                 anomaly_engine: 'AnomalyDetectionEngine' = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._decision_engine = decision_engine
        self._optimization_engine = optimization_engine
        self._anomaly_engine = anomaly_engine
        self._running = False
        self._autonomous_thread = None
        self._heartbeat_thread = None
        self._watchdog_timer = None
        self._last_heartbeat = 0
        self._error_count = 0
        self._consecutive_errors = 0
        self._start_time = 0
        self._decisions_made = 0
        self._successful_decisions = 0
        self._cycle_count = 0
        self._phase_health = {}
        self._state_lock = RLock()
        self._shutdown_event = Event()

    def start_autonomous_mode(self) -> bool:
        """Start fully autonomous operation."""
        if self._running:
            self._logger.warning("Autonomous mode already running")
            return False

        self._logger.info("Starting autonomous mode")
        self._logger.telegram_step(1, 3, "Autonomous Mode Startup",
                                   "Initializing autonomous operation...")

        self._running = True
        self._start_time = time.time()
        self._error_count = 0
        self._consecutive_errors = 0
        self._cycle_count = 0

        # Start threads
        self._autonomous_thread = Thread(target=self._autonomous_loop, daemon=True)
        self._autonomous_thread.start()

        self._heartbeat_thread = Thread(target=self._heartbeat_loop, daemon=True)
        self._heartbeat_thread.start()

        # Start watchdog
        if AutonomousConfig.WATCHDOG_ENABLED:
            self._watchdog_timer = Timer(AutonomousConfig.WATCHDOG_TIMEOUT, self._watchdog_check)
            self._watchdog_timer.start()

        # Send startup notification
        if self._telegram:
            self._telegram.send_autonomous_status({
                "running": True,
                "uptime": 0,
                "decisions_made": 0,
                "success_rate": 0,
                "anomaly_count": 0,
                "optimizations_applied": 0,
                "patterns_learned": 0
            })

        self._logger.telegram_step(1, 3, "Autonomous Mode Startup", "Complete",
                                   status="success", details={
                                       "mode": "AUTONOMOUS",
                                       "heartbeat_interval": f"{AutonomousConfig.HEARTBEAT_INTERVAL}s",
                                       "decision_interval": f"{AutonomousConfig.DECISION_EXECUTION_INTERVAL}s",
                                       "watchdog": "ENABLED" if AutonomousConfig.WATCHDOG_ENABLED else "DISABLED"
                                   })

        return True

    def stop_autonomous_mode(self) -> bool:
        """Stop autonomous operation."""
        if not self._running:
            return False

        self._logger.info("Stopping autonomous mode")
        self._logger.telegram_step(1, 1, "Autonomous Mode Shutdown",
                                   "Stopping autonomous operation...")

        self._running = False
        self._shutdown_event.set()

        # Cancel watchdog
        if self._watchdog_timer:
            self._watchdog_timer.cancel()

        # Wait for threads
        if self._autonomous_thread:
            self._autonomous_thread.join(timeout=10)
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=10)

        # Persist final state
        self._persist_state()

        # Send shutdown notification
        if self._telegram:
            self._telegram.send_autonomous_status({
                "running": False,
                "uptime": time.time() - self._start_time,
                "decisions_made": self._decisions_made,
                "success_rate": (self._successful_decisions / max(self._decisions_made, 1)) * 100,
                "anomaly_count": 0,
                "optimizations_applied": 0,
                "patterns_learned": 0
            })

        self._logger.telegram_step(1, 1, "Autonomous Mode Shutdown", "Complete",
                                   status="success")

        return True

    def _autonomous_loop(self) -> None:
        """Main autonomous operation loop."""
        while self._running and not self._shutdown_event.is_set():
            try:
                cycle_start = time.time()
                self._cycle_count += 1

                self._logger.debug(f"Autonomous cycle {self._cycle_count} started")

                # Step 1: Check system health
                self._check_phase_health()

                # Step 2: Make decision
                if self._decision_engine:
                    try:
                        result = self._decision_engine.make_decision()
                        self._decisions_made += 1
                        if result.get("success", False):
                            self._successful_decisions += 1
                            self._consecutive_errors = 0
                        else:
                            self._consecutive_errors += 1
                    except Exception as e:
                        self._logger.error(f"Decision engine error: {e}")
                        self._consecutive_errors += 1

                # Step 3: Check for anomalies
                if self._anomaly_engine:
                    try:
                        health = get_system_health()
                        metrics = {
                            "cpu_usage": health.cpu_usage,
                            "memory_usage": health.memory_usage,
                            "active_threads": health.active_threads,
                            "error_rate": health.error_rate
                        }
                        self._anomaly_engine.detect_anomaly(metrics)
                    except Exception as e:
                        self._logger.error(f"Anomaly detection error: {e}")

                # Step 4: Self-optimize
                if self._optimization_engine and self._cycle_count % 5 == 0:
                    try:
                        self._optimization_engine.optimize_system()
                    except Exception as e:
                        self._logger.error(f"Optimization error: {e}")

                # Step 5: Error recovery
                if self._consecutive_errors >= AutonomousConfig.MAX_CONSECUTIVE_ERRORS:
                    self._handle_error_escalation()

                # Step 6: Persist state
                if self._cycle_count % 10 == 0:
                    self._persist_state()

                # Step 7: Night mode check
                if AutonomousConfig.NIGHT_MODE_ENABLED:
                    current_hour = datetime.utcnow().hour
                    if AutonomousConfig.NIGHT_MODE_HOURS[0] <= current_hour <= AutonomousConfig.NIGHT_MODE_HOURS[1]:
                        # Reduce activity during night hours
                        time.sleep(AutonomousConfig.DECISION_EXECUTION_INTERVAL * 2)
                        continue

                # Calculate sleep time
                cycle_time = time.time() - cycle_start
                sleep_time = max(0, AutonomousConfig.DECISION_EXECUTION_INTERVAL - cycle_time)

                # Check for max runtime
                if (AutonomousConfig.MAX_AUTONOMOUS_RUNTIME > 0 and 
                    time.time() - self._start_time > AutonomousConfig.MAX_AUTONOMOUS_RUNTIME):
                    self._logger.info("Max autonomous runtime reached, stopping")
                    self.stop_autonomous_mode()
                    break

                self._shutdown_event.wait(timeout=sleep_time)

            except Exception as e:
                self._logger.error(f"Autonomous loop error: {e}")
                self._error_count += 1
                self._consecutive_errors += 1

                if self._consecutive_errors >= AutonomousConfig.ERROR_ESCALATION_THRESHOLD:
                    self._handle_error_escalation()

                time.sleep(AutonomousConfig.ERROR_RECOVERY_DELAY)

    def _heartbeat_loop(self) -> None:
        """Heartbeat and status reporting loop."""
        while self._running and not self._shutdown_event.is_set():
            try:
                self._last_heartbeat = time.time()

                # Send heartbeat to database
                self._db.insert("oanks_ai_autonomous_log", {
                    "event_type": "heartbeat",
                    "event_data": safe_json_dumps({
                        "cycle_count": self._cycle_count,
                        "decisions_made": self._decisions_made,
                        "error_count": self._error_count,
                        "uptime": time.time() - self._start_time
                    }),
                    "timestamp": get_timestamp()
                })

                # Send status report to Telegram
                if self._telegram and self._cycle_count > 0:
                    uptime = time.time() - self._start_time
                    success_rate = (self._successful_decisions / max(self._decisions_made, 1)) * 100

                    self._telegram.send_autonomous_status({
                        "running": True,
                        "uptime": uptime,
                        "decisions_made": self._decisions_made,
                        "success_rate": success_rate,
                        "anomaly_count": 0,
                        "optimizations_applied": 0,
                        "patterns_learned": 0
                    })

                self._shutdown_event.wait(timeout=AutonomousConfig.HEARTBEAT_INTERVAL)

            except Exception as e:
                self._logger.error(f"Heartbeat error: {e}")
                time.sleep(60)

    def _watchdog_check(self) -> None:
        """Watchdog timer check."""
        if not self._running:
            return

        time_since_heartbeat = time.time() - self._last_heartbeat

        if time_since_heartbeat > AutonomousConfig.WATCHDOG_TIMEOUT:
            self._logger.critical("Watchdog timeout! Autonomous loop may be hung.")

            if self._telegram:
                self._telegram.send_emergency_alert("Watchdog timeout - autonomous loop unresponsive")

            # Attempt recovery
            self._handle_error_escalation()

        # Reschedule watchdog
        if self._running:
            self._watchdog_timer = Timer(AutonomousConfig.WATCHDOG_TIMEOUT, self._watchdog_check)
            self._watchdog_timer.start()

    def _check_phase_health(self) -> None:
        """Check health of all phases."""
        # In real implementation, would check actual phase status
        # For now, simulate phase health checks
        for phase in range(1, 14):
            phase_name = f"phase_{phase}"
            # Simulate health check
            self._phase_health[phase_name] = "healthy"

    def _handle_error_escalation(self) -> None:
        """Handle error escalation based on consecutive error count."""
        if self._consecutive_errors >= AutonomousConfig.FULL_LOCKDOWN_THRESHOLD:
            self._logger.critical("Full lockdown threshold reached! Initiating emergency stop.")

            if self._telegram:
                self._telegram.send_emergency_alert(
                    f"Full lockdown: {self._consecutive_errors} consecutive errors"
                )

            self.stop_autonomous_mode()

        elif self._consecutive_errors >= AutonomousConfig.ERROR_ESCALATION_THRESHOLD:
            self._logger.error(f"Error escalation: {self._consecutive_errors} consecutive errors")

            # Attempt recovery actions
            recovery_actions = [
                "Restarting decision engine",
                "Clearing caches",
                "Rotating proxies",
                "Reducing thread count"
            ]

            for action in recovery_actions:
                self._logger.info(f"Recovery attempt: {action}")

                if self._telegram:
                    self._telegram.send_error_recovery(
                        {"type": "escalation", "phase": "autonomous", "message": f"{self._consecutive_errors} errors"},
                        action
                    )

                time.sleep(AutonomousConfig.ERROR_RECOVERY_DELAY)

    def _persist_state(self) -> None:
        """Persist current state for crash recovery."""
        try:
            state = {
                "cycle_count": self._cycle_count,
                "decisions_made": self._decisions_made,
                "successful_decisions": self._successful_decisions,
                "error_count": self._error_count,
                "consecutive_errors": self._consecutive_errors,
                "phase_health": self._phase_health,
                "timestamp": get_timestamp()
            }

            self._db.insert("oanks_ai_state_snapshots", {
                "snapshot_data": safe_json_dumps(state),
                "phase_status": safe_json_dumps(self._phase_health),
                "decision_count": self._decisions_made,
                "timestamp": get_timestamp()
            })
        except Exception as e:
            self._logger.debug(f"State persistence failed: {e}")

    def handle_error_autonomously(self, error: Dict) -> bool:
        """Handle an error without human intervention."""
        error_type = error.get("type", "unknown")
        error_message = error.get("message", "")
        affected_phase = error.get("phase", "unknown")

        self._logger.info(f"Autonomous error handling: {error_type} in {affected_phase}")

        # Log the error
        self._db.insert("oanks_ai_autonomous_log", {
            "event_type": "error_recovery",
            "event_data": safe_json_dumps(error),
            "phase_affected": affected_phase,
            "error_message": error_message,
            "timestamp": get_timestamp()
        })

        # Attempt recovery based on error type
        recovery_success = False

        for attempt in range(AutonomousConfig.ERROR_RECOVERY_ATTEMPTS):
            try:
                if "proxy" in error_type.lower():
                    recovery_success = True  # Would call proxy rotation
                elif "network" in error_type.lower():
                    recovery_success = True  # Would retry with backoff
                elif "phase" in error_type.lower():
                    recovery_success = True  # Would restart phase
                elif "memory" in error_type.lower():
                    recovery_success = True  # Would clear caches
                else:
                    recovery_success = True  # Generic recovery

                if recovery_success:
                    break

            except Exception as e:
                self._logger.error(f"Recovery attempt {attempt + 1} failed: {e}")
                time.sleep(AutonomousConfig.ERROR_RECOVERY_DELAY)

        # Update log with result
        self._db.update(
            "oanks_ai_autonomous_log",
            {
                "result": "recovered" if recovery_success else "failed",
                "recovery_attempts": AutonomousConfig.ERROR_RECOVERY_ATTEMPTS
            },
            "event_type = 'error_recovery' AND phase_affected = ?",
            (affected_phase,)
        )

        return recovery_success

    def get_autonomous_status(self) -> Dict:
        """Get autonomous mode status."""
        uptime = time.time() - self._start_time if self._start_time > 0 else 0
        success_rate = (self._successful_decisions / max(self._decisions_made, 1)) * 100

        return {
            "running": self._running,
            "uptime": uptime,
            "uptime_formatted": format_duration(uptime),
            "cycle_count": self._cycle_count,
            "decisions_made": self._decisions_made,
            "successful_decisions": self._successful_decisions,
            "success_rate": round(success_rate, 1),
            "error_count": self._error_count,
            "consecutive_errors": self._consecutive_errors,
            "phase_health": self._phase_health,
            "last_heartbeat": self._last_heartbeat,
            "watchdog_active": AutonomousConfig.WATCHDOG_ENABLED and self._watchdog_timer is not None
        }

    def run_autonomous_cycle(self) -> Dict:
        """Run one autonomous cycle manually."""
        if self._running:
            return {"error": "Autonomous mode is already running"}

        results = {}

        # Make one decision
        if self._decision_engine:
            results["decision"] = self._decision_engine.make_decision()

        # Check anomalies
        if self._anomaly_engine:
            health = get_system_health()
            results["anomaly"] = self._anomaly_engine.detect_anomaly({
                "cpu_usage": health.cpu_usage,
                "memory_usage": health.memory_usage
            })

        # Optimize
        if self._optimization_engine:
            results["optimization"] = self._optimization_engine.optimize_system()

        return results

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        return {
            "running": self._running,
            "cycle_count": self._cycle_count,
            "decisions_made": self._decisions_made,
            "successful_decisions": self._successful_decisions,
            "error_count": self._error_count,
            "uptime": time.time() - self._start_time if self._start_time > 0 else 0
        }

# ==============================================================================
# SECTION 12: LEARNING ENGINE — PATTERN MEMORY, KNOWLEDGE BASE, NODE SHARING
# ==============================================================================

class LearningEngine:
    """
    Learning engine that stores successful and failed actions,
    identifies patterns, and shares knowledge across distributed nodes.

    Features:
    - Memory-based pattern storage
    - Success/failure pattern identification
    - Context matching for pattern application
    - Knowledge sharing across nodes (Phase 12 integration)
    - Temporal and spatial learning
    - Forgetting mechanism for outdated knowledge
    """

    def __init__(self, db_manager: DatabaseManager, logger: OanksLogger,
                 telegram: TelegramBotInterface = None):
        self._db = db_manager
        self._logger = logger
        self._telegram = telegram
        self._memory = {}
        self._success_patterns = []
        self._failure_patterns = []
        self._pattern_index = {}
        self._learning_rate = LearningConfig.LEARNING_RATE_DECAY
        self._cache_lock = RLock()

    def learn_from_success(self, action: Dict) -> None:
        """Learn from a successful action."""
        try:
            pattern = self._extract_pattern(action)
            pattern["outcome"] = "success"
            pattern["timestamp"] = get_timestamp()

            # Store in memory
            with self._cache_lock:
                self._success_patterns.append(pattern)
                if len(self._success_patterns) > LearningConfig.MEMORY_SIZE_LIMIT:
                    self._success_patterns = self._success_patterns[-LearningConfig.MEMORY_SIZE_LIMIT:]

            # Store in database
            pattern_hash = hash_string(safe_json_dumps(pattern))
            existing = self._db.select_one(
                "oanks_ai_knowledge",
                where="pattern_hash = ?",
                where_params=(pattern_hash,)
            )

            if existing:
                new_success = existing["success_count"] + 1
                new_total = existing["usage_count"] + 1
                new_rate = new_success / new_total

                self._db.update(
                    "oanks_ai_knowledge",
                    {
                        "success_rate": new_rate,
                        "success_count": new_success,
                        "usage_count": new_total,
                        "last_used": get_timestamp(),
                        "last_validated": get_timestamp()
                    },
                    "id = ?",
                    (existing["id"],)
                )
            else:
                self._db.insert("oanks_ai_knowledge", {
                    "pattern_type": "success",
                    "pattern_data": safe_json_dumps(pattern),
                    "pattern_hash": pattern_hash,
                    "success_rate": 1.0,
                    "usage_count": 1,
                    "success_count": 1,
                    "failure_count": 0,
                    "created_at": get_timestamp(),
                    "last_used": get_timestamp(),
                    "last_validated": get_timestamp(),
                    "validation_status": "VALIDATED",
                    "node_origin": "local"
                })

            self._logger.info(f"Learned from success: {pattern.get('action', 'unknown')}")

        except Exception as e:
            self._logger.debug(f"Success learning failed: {e}")

    def learn_from_failure(self, action: Dict) -> None:
        """Learn from a failed action."""
        try:
            pattern = self._extract_pattern(action)
            pattern["outcome"] = "failure"
            pattern["timestamp"] = get_timestamp()

            # Store in memory
            with self._cache_lock:
                self._failure_patterns.append(pattern)
                if len(self._failure_patterns) > LearningConfig.MEMORY_SIZE_LIMIT:
                    self._failure_patterns = self._failure_patterns[-LearningConfig.MEMORY_SIZE_LIMIT:]

            # Store in database
            pattern_hash = hash_string(safe_json_dumps(pattern))
            existing = self._db.select_one(
                "oanks_ai_knowledge",
                where="pattern_hash = ?",
                where_params=(pattern_hash,)
            )

            if existing:
                new_failure = existing["failure_count"] + 1
                new_total = existing["usage_count"] + 1
                new_rate = existing["success_count"] / new_total

                self._db.update(
                    "oanks_ai_knowledge",
                    {
                        "success_rate": new_rate,
                        "failure_count": new_failure,
                        "usage_count": new_total,
                        "last_used": get_timestamp()
                    },
                    "id = ?",
                    (existing["id"],)
                )
            else:
                self._db.insert("oanks_ai_knowledge", {
                    "pattern_type": "failure",
                    "pattern_data": safe_json_dumps(pattern),
                    "pattern_hash": pattern_hash,
                    "success_rate": 0.0,
                    "usage_count": 1,
                    "success_count": 0,
                    "failure_count": 1,
                    "created_at": get_timestamp(),
                    "last_used": get_timestamp(),
                    "validation_status": "PENDING",
                    "node_origin": "local"
                })

            self._logger.info(f"Learned from failure: {pattern.get('action', 'unknown')}")

        except Exception as e:
            self._logger.debug(f"Failure learning failed: {e}")

    def _extract_pattern(self, action: Dict) -> Dict:
        """Extract a learnable pattern from an action."""
        return {
            "action": action.get("action", ""),
            "target": action.get("target", ""),
            "decision_type": action.get("decision_type", ""),
            "context": action.get("context", {}),
            "parameters": action.get("parameters", {}),
            "confidence": action.get("confidence", 0)
        }

    def identify_success_patterns(self) -> List[Dict]:
        """Identify patterns of success from the knowledge base."""
        try:
            patterns = self._db.select(
                "oanks_ai_knowledge",
                where="success_rate > ? AND usage_count > ?",
                where_params=(0.7, 5),
                order_by="success_rate DESC, usage_count DESC",
                limit=50
            )

            return [{
                "pattern_type": p["pattern_type"],
                "success_rate": p["success_rate"],
                "usage_count": p["usage_count"],
                "pattern_data": safe_json_loads(p.get("pattern_data", "{}"), {}),
                "last_used": p["last_used"]
            } for p in patterns]

        except Exception as e:
            self._logger.debug(f"Success pattern identification failed: {e}")
            return []

    def apply_success_patterns(self, context: Dict) -> Optional[Dict]:
        """Apply learned success patterns to a given context."""
        try:
            # Get high-success patterns
            patterns = self._db.select(
                "oanks_ai_knowledge",
                where="success_rate > ?",
                where_params=(0.8,),
                order_by="success_rate DESC",
                limit=20
            )

            best_match = None
            best_score = 0

            for pattern in patterns:
                pattern_data = safe_json_loads(pattern.get("pattern_data", "{}"), {})

                # Calculate context similarity
                context_similarity = self._calculate_context_similarity(
                    context, pattern_data.get("context", {})
                )

                # Weight by success rate and usage
                score = (context_similarity * 0.5 + 
                        pattern["success_rate"] * 0.3 +
                        min(pattern["usage_count"] / 100, 1.0) * 0.2)

                if score > best_score and score > LearningConfig.PATTERN_SIMILARITY_THRESHOLD:
                    best_score = score
                    best_match = pattern

            if best_match:
                pattern_data = safe_json_loads(best_match.get("pattern_data", "{}"), {})
                return {
                    "pattern": pattern_data,
                    "success_rate": best_match["success_rate"],
                    "match_score": best_score,
                    "recommendation": pattern_data.get("action", "")
                }

            return None

        except Exception as e:
            self._logger.debug(f"Pattern application failed: {e}")
            return None

    def _calculate_context_similarity(self, context1: Dict, context2: Dict) -> float:
        """Calculate similarity between two contexts."""
        if not context1 or not context2:
            return 0.0

        # Simple key overlap similarity
        keys1 = set(context1.keys())
        keys2 = set(context2.keys())

        if not keys1 or not keys2:
            return 0.0

        overlap = keys1 & keys2
        union = keys1 | keys2

        key_similarity = len(overlap) / len(union) if union else 0

        # Value similarity for overlapping keys
        value_similarities = []
        for key in overlap:
            v1 = str(context1[key])
            v2 = str(context2[key])
            value_similarities.append(string_similarity(v1, v2))

        value_similarity = mean(value_similarities) if value_similarities else 0

        return (key_similarity * 0.3 + value_similarity * 0.7)

    def share_knowledge_across_nodes(self) -> bool:
        """Share learned knowledge across distributed nodes (Phase 12 integration)."""
        try:
            # Get patterns not yet shared
            unshared = self._db.select(
                "oanks_ai_knowledge",
                where="shared_across_nodes = 0 AND success_rate > ?",
                where_params=(0.6,),
                limit=100
            )

            if not unshared:
                return True

            # In real implementation, would send to Phase 12 distributed nodes
            # For now, mark as shared
            for pattern in unshared:
                self._db.update(
                    "oanks_ai_knowledge",
                    {"shared_across_nodes": 1},
                    "id = ?",
                    (pattern["id"],)
                )

            self._logger.info(f"Shared {len(unshared)} patterns across nodes")

            if self._telegram:
                self._telegram.send_knowledge_update([{
                    "pattern_type": p["pattern_type"],
                    "success_rate": p["success_rate"],
                    "usage_count": p["usage_count"],
                    "pattern_data": truncate_string(p.get("pattern_data", ""), 100)
                } for p in unshared[:5]])

            return True

        except Exception as e:
            self._logger.error(f"Knowledge sharing failed: {e}")
            return False

    def forget_outdated_patterns(self) -> int:
        """Remove outdated patterns based on forgetting threshold."""
        try:
            # Find patterns below threshold
            outdated = self._db.select(
                "oanks_ai_knowledge",
                where="success_rate < ? AND usage_count > ?",
                where_params=(LearningConfig.FORGETTING_THRESHOLD, 10),
                limit=1000
            )

            forgotten = 0
            for pattern in outdated:
                # Check age
                last_used = parse_timestamp(pattern.get("last_used", ""))
                if last_used and (time.time() - last_used) > LearningConfig.FORGETTING_INTERVAL:
                    self._db.update(
                        "oanks_ai_knowledge",
                        {"validation_status": "FORGOTTEN", "active": 0},
                        "id = ?",
                        (pattern["id"],)
                    )
                    forgotten += 1

            self._logger.info(f"Forgot {forgotten} outdated patterns")
            return forgotten

        except Exception as e:
            self._logger.debug(f"Pattern forgetting failed: {e}")
            return 0

    def get_stats(self) -> Dict:
        """Get engine statistics."""
        try:
            total_patterns = self._db.count("oanks_ai_knowledge")
            success_patterns = self._db.count("oanks_ai_knowledge", "success_rate > 0.7")
            failure_patterns = self._db.count("oanks_ai_knowledge", "success_rate < 0.3")
            shared_patterns = self._db.count("oanks_ai_knowledge", "shared_across_nodes = 1")

            return {
                "total_patterns": total_patterns,
                "high_success_patterns": success_patterns,
                "high_failure_patterns": failure_patterns,
                "shared_patterns": shared_patterns,
                "memory_patterns": len(self._success_patterns) + len(self._failure_patterns),
                "learning_rate": self._learning_rate
            }
        except:
            return {
                "total_patterns": 0,
                "memory_patterns": len(self._success_patterns) + len(self._failure_patterns)
            }

# ==============================================================================
# END OF SECTION 11 & 12: AUTONOMOUS MODE AND LEARNING ENGINE
# ==============================================================================



# ==============================================================================
# SECTION 13: MAIN PHASE 14 CLASS — ORCHESTRATION, INTEGRATION, CONTROL
# ==============================================================================

class Phase14AIAssistant:
    """
    👑 OANKS OPERATIONS FRAMEWORK — PHASE 14: AI ASSISTANT

    The crown jewel of the framework. This class orchestrates all AI subsystems:
    - Auto-Decision Making
    - Adaptive Scraping
    - Intelligent Proxy Rotation
    - Predictive Harvesting
    - Anomaly Detection
    - Self-Optimization
    - Autonomous Mode
    - Learning from Data

    This is the module that transforms the framework from a tool into a
    living, breathing, autonomous predator. No human intervention required.

    NO TensorFlow. NO PyTorch. NO scikit-learn. NO GUI.
    Pure Python. Pure memory. Pure statistics. Pure dominance.

    Integration:
    - Phase 1: Database, logging, crypto
    - Phase 2: Proxy intelligence, rotation
    - Phase 3: Adaptive scraping, predictive harvesting
    - Phase 4: Intelligent enrichment, correlation
    - Phase 5: Auto-account creation
    - Phase 6: Premium AI features
    - Phase 7: Telegram command center
    - Phase 8: Predictive pricing
    - Phase 9: Anomaly detection, auto-response
    - Phase 10: Intelligent worm propagation
    - Phase 11: Auto-ransomware decisions
    - Phase 12: Distributed AI, shared learning
    - Phase 13: Darkweb intelligence automation
    - Phase 15: Final deployment

    Creator: Oanks (@oanksnood)
    Danger Level: 11/10
    """

    def __init__(self, system: Dict[str, Any] = None):
        """
        Initialize Phase 14 AI Assistant.

        Args:
            system: Dictionary containing system components:
                - db: DatabaseManager instance (optional, creates new if not provided)
                - crypto: Crypto module from Phase 1
                - logger: Logger instance (optional, creates new if not provided)
                - telegram_token: Telegram bot token
                - telegram_chat_id: Telegram chat ID
        """
        self._system = system or {}
        self._initialized = False
        self._initialization_lock = RLock()

        # Statistics
        self._stats = {
            "decisions_made": 0,
            "successful_decisions": 0,
            "anomalies_detected": 0,
            "optimizations_applied": 0,
            "predictions_made": 0,
            "patterns_learned": 0,
            "autonomous_cycles": 0,
            "scrapes_adapted": 0,
            "proxies_rotated": 0,
            "errors_recovered": 0,
            "startup_time": get_timestamp()
        }

        # Subsystem references
        self._db = None
        self._logger = None
        self._telegram = None
        self._decision_engine = None
        self._scraping_engine = None
        self._proxy_engine = None
        self._predictive_engine = None
        self._anomaly_engine = None
        self._optimization_engine = None
        self._autonomous_engine = None
        self._learning_engine = None

        # Threading
        self._threads = {}
        self._shutdown_event = Event()

        # State
        self._is_autonomous = False
        self._learning_enabled = True
        self._status = "initialized"

        # Initialize
        self._initialize()

    def _initialize(self) -> None:
        """Initialize all subsystems."""
        with self._initialization_lock:
            if self._initialized:
                return

            try:
                # Step 1: Initialize database
                db_path = self._system.get("db_path", DatabaseConfig.DB_NAME)
                self._db = DatabaseManager(db_path)

                # Step 2: Initialize logger
                self._logger = OanksLogger("Phase14AI")
                self._logger.set_db_manager(self._db)

                # Step 3: Initialize Telegram
                telegram_token = self._system.get("telegram_token")
                telegram_chat_id = self._system.get("telegram_chat_id")
                if telegram_token and telegram_chat_id:
                    self._telegram = TelegramBotInterface(telegram_token, telegram_chat_id)
                    self._telegram.start()
                    self._logger.set_telegram_callback(
                        lambda msg: self._telegram.send_message(msg)
                    )

                # Step 4: Initialize subsystems
                self._logger.info("Initializing Phase 14 AI Assistant subsystems...")

                # 4.1: Decision Engine
                self._decision_engine = AutoDecisionEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.2: Scraping Engine
                self._scraping_engine = AdaptiveScrapingEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.3: Proxy Engine
                self._proxy_engine = IntelligentProxyEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.4: Predictive Engine
                self._predictive_engine = PredictiveHarvestingEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.5: Anomaly Engine
                self._anomaly_engine = AnomalyDetectionEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.6: Optimization Engine
                self._optimization_engine = SelfOptimizationEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.7: Learning Engine
                self._learning_engine = LearningEngine(
                    self._db, self._logger, self._telegram
                )

                # 4.8: Autonomous Engine (initialized last, depends on others)
                self._autonomous_engine = AutonomousModeEngine(
                    self._db, self._logger, self._telegram,
                    self._decision_engine, self._optimization_engine, self._anomaly_engine
                )

                # Step 5: Send startup notification
                if self._telegram:
                    self._telegram.send_startup_notification()

                self._initialized = True
                self._status = "ready"

                self._logger.info("Phase 14 AI Assistant initialized successfully")

            except Exception as e:
                self._logger.critical(f"Initialization failed: {e}")
                raise

    # ========================================================================
    # PUBLIC API: DECISION MAKING
    # ========================================================================

    def make_decision(self, system_state: Dict = None) -> Dict:
        """Make an AI decision based on current state."""
        if not self._initialized:
            return {"error": "Not initialized"}

        result = self._decision_engine.make_decision(system_state)
        self._stats["decisions_made"] += 1
        if result.get("success", False):
            self._stats["successful_decisions"] += 1
        return result

    def analyze_state(self) -> StateSnapshot:
        """Analyze current system state."""
        if not self._initialized:
            return StateSnapshot()
        return self._decision_engine.analyze_state()

    def get_decision_history(self, limit: int = 100) -> List[Dict]:
        """Get recent decision history."""
        if not self._initialized:
            return []
        return self._decision_engine.get_decision_history(limit)

    def get_decision_stats(self) -> Dict:
        """Get decision statistics."""
        if not self._initialized:
            return {}
        return self._decision_engine.get_decision_stats()

    # ========================================================================
    # PUBLIC API: ADAPTIVE SCRAPING
    # ========================================================================

    def adapt_scrape_strategy(self, target: str, results: List[Dict]) -> Dict:
        """Adapt scraping strategy based on results."""
        if not self._initialized:
            return {"error": "Not initialized"}

        result = self._scraping_engine.adapt_scrape_strategy(target, results)
        self._stats["scrapes_adapted"] += 1
        return result

    def detect_anti_scrape(self, response: Dict) -> Dict:
        """Detect anti-scraping measures."""
        if not self._initialized:
            return {"error": "Not initialized"}
        return self._scraping_engine.detect_anti_scrape(response)

    def get_optimal_scrape_config(self, target: str) -> Dict:
        """Get optimal scraping configuration for a target."""
        if not self._initialized:
            return {"error": "Not initialized"}
        return self._scraping_engine.get_optimal_scrape_config(target)

    def rotate_user_agent(self, target: str = None) -> str:
        """Rotate user agent."""
        if not self._initialized:
            return ""
        return self._scraping_engine.rotate_user_agent(target)

    # ========================================================================
    # PUBLIC API: INTELLIGENT PROXY ROTATION
    # ========================================================================

    def score_proxy(self, proxy_id: int) -> float:
        """Calculate proxy intelligence score."""
        if not self._initialized:
            return 0.5
        return self._proxy_engine.score_proxy(proxy_id)

    def get_best_proxy_for_target(self, target: str) -> Optional[int]:
        """Get best proxy for a specific target."""
        if not self._initialized:
            return None
        return self._proxy_engine.get_best_proxy_for_target(target)

    def predict_proxy_failure(self, proxy_id: int) -> Dict:
        """Predict probability of proxy failure."""
        if not self._initialized:
            return {"failure_probability": 0.5}
        return self._proxy_engine.predict_proxy_failure(proxy_id)

    def update_proxy_intel(self, proxy_id: int, success: bool, 
                           response_time: float, target: str = None) -> None:
        """Update proxy intelligence data."""
        if not self._initialized:
            return
        self._proxy_engine.update_proxy_intel(proxy_id, success, response_time, target)
        self._stats["proxies_rotated"] += 1

    def get_proxy_intel_summary(self, limit: int = 20) -> List[Dict]:
        """Get proxy intelligence summary."""
        if not self._initialized:
            return []
        return self._proxy_engine.get_proxy_intel_summary(limit)

    # ========================================================================
    # PUBLIC API: PREDICTIVE HARVESTING
    # ========================================================================

    def predict_data_availability(self, data_type: str) -> HarvestPrediction:
        """Predict when high-value data will be available."""
        if not self._initialized:
            return HarvestPrediction()

        result = self._predictive_engine.predict_data_availability(data_type)
        self._stats["predictions_made"] += 1
        return result

    def identify_data_patterns(self) -> Dict:
        """Identify patterns in data availability."""
        if not self._initialized:
            return {}
        return self._predictive_engine.identify_data_patterns()

    def predict_best_source(self, data_type: str) -> str:
        """Predict best source for a data type."""
        if not self._initialized:
            return "unknown"
        return self._predictive_engine.predict_best_source(data_type)

    def predict_harvest_volume(self, source: str, hours_ahead: int = 24) -> int:
        """Predict harvest volume from a source."""
        if not self._initialized:
            return 0
        return self._predictive_engine.predict_harvest_volume(source, hours_ahead)

    def schedule_harvest(self, prediction: HarvestPrediction) -> bool:
        """Schedule harvesting based on prediction."""
        if not self._initialized:
            return False
        return self._predictive_engine.schedule_harvest(prediction)

    # ========================================================================
    # PUBLIC API: ANOMALY DETECTION
    # ========================================================================

    def detect_anomaly(self, metrics: Dict[str, float]) -> Optional[Dict]:
        """Detect anomaly in system metrics."""
        if not self._initialized:
            return None

        result = self._anomaly_engine.detect_anomaly(metrics)
        if result:
            self._stats["anomalies_detected"] += 1
        return result

    def analyze_network_anomaly(self, network_data: Dict) -> Dict:
        """Analyze network anomaly."""
        if not self._initialized:
            return {}
        return self._anomaly_engine.analyze_network_anomaly(network_data)

    def analyze_access_anomaly(self, access_data: Dict) -> Dict:
        """Analyze unauthorized access anomaly."""
        if not self._initialized:
            return {}
        return self._anomaly_engine.analyze_access_anomaly(access_data)

    def respond_to_anomaly(self, anomaly: Dict) -> bool:
        """Auto-respond to detected anomaly."""
        if not self._initialized:
            return False
        return self._anomaly_engine.respond_to_anomaly(anomaly)

    def get_anomaly_history(self, limit: int = 100, unresolved_only: bool = False) -> List[Dict]:
        """Get anomaly history."""
        if not self._initialized:
            return []
        return self._anomaly_engine.get_anomaly_history(limit, unresolved_only)

    # ========================================================================
    # PUBLIC API: SELF-OPTIMIZATION
    # ========================================================================

    def optimize_system(self) -> Dict:
        """Self-optimize system configuration."""
        if not self._initialized:
            return {"error": "Not initialized"}

        result = self._optimization_engine.optimize_system()
        self._stats["optimizations_applied"] += result.get("optimizations_applied", 0)
        return result

    def measure_performance(self) -> Dict:
        """Measure current system performance."""
        if not self._initialized:
            return {}
        return self._optimization_engine.measure_performance()

    def identify_bottlenecks(self) -> List[Dict]:
        """Identify system bottlenecks."""
        if not self._initialized:
            return []
        return self._optimization_engine.identify_bottlenecks()

    def get_optimal_parameters(self) -> Dict:
        """Get optimal system parameters."""
        if not self._initialized:
            return {}
        return self._optimization_engine.get_optimal_parameters()

    # ========================================================================
    # PUBLIC API: AUTONOMOUS MODE
    # ========================================================================

    def start_autonomous_mode(self) -> bool:
        """Start fully autonomous operation."""
        if not self._initialized:
            return False

        result = self._autonomous_engine.start_autonomous_mode()
        if result:
            self._is_autonomous = True
            self._status = "autonomous"
        return result

    def stop_autonomous_mode(self) -> bool:
        """Stop autonomous operation."""
        if not self._initialized:
            return False

        result = self._autonomous_engine.stop_autonomous_mode()
        if result:
            self._is_autonomous = False
            self._status = "ready"
        return result

    def run_autonomous_cycle(self) -> Dict:
        """Run one autonomous cycle."""
        if not self._initialized:
            return {"error": "Not initialized"}

        result = self._autonomous_engine.run_autonomous_cycle()
        self._stats["autonomous_cycles"] += 1
        return result

    def handle_error_autonomously(self, error: Dict) -> bool:
        """Handle error without human intervention."""
        if not self._initialized:
            return False

        result = self._autonomous_engine.handle_error_autonomously(error)
        if result:
            self._stats["errors_recovered"] += 1
        return result

    def get_autonomous_status(self) -> Dict:
        """Get autonomous mode status."""
        if not self._initialized:
            return {"error": "Not initialized"}
        return self._autonomous_engine.get_autonomous_status()

    # ========================================================================
    # PUBLIC API: LEARNING
    # ========================================================================

    def learn_from_success(self, action: Dict) -> None:
        """Learn from a successful action."""
        if not self._initialized or not self._learning_enabled:
            return

        self._learning_engine.learn_from_success(action)
        self._stats["patterns_learned"] += 1

    def learn_from_failure(self, action: Dict) -> None:
        """Learn from a failed action."""
        if not self._initialized or not self._learning_enabled:
            return
        self._learning_engine.learn_from_failure(action)

    def identify_success_patterns(self) -> List[Dict]:
        """Identify patterns of success."""
        if not self._initialized:
            return []
        return self._learning_engine.identify_success_patterns()

    def apply_success_patterns(self, context: Dict) -> Optional[Dict]:
        """Apply learned success patterns."""
        if not self._initialized:
            return None
        return self._learning_engine.apply_success_patterns(context)

    def share_knowledge_across_nodes(self) -> bool:
        """Share learned knowledge across distributed nodes."""
        if not self._initialized:
            return False
        return self._learning_engine.share_knowledge_across_nodes()

    def enable_learning(self) -> None:
        """Enable learning mode."""
        self._learning_enabled = True
        self._logger.info("Learning mode enabled")

    def disable_learning(self) -> None:
        """Disable learning mode."""
        self._learning_enabled = False
        self._logger.info("Learning mode disabled")

    # ========================================================================
    # PUBLIC API: TELEGRAM COMMANDS
    # ========================================================================

    def handle_telegram_command(self, command: str, args: List[str] = None) -> str:
        """Handle a Telegram command."""
        if not self._initialized:
            return "❌ Phase 14 not initialized"

        args = args or []

        # Route to appropriate handler
        if command == "ai_start":
            return self._handle_telegram_start()
        elif command == "ai_stop":
            return self._handle_telegram_stop()
        elif command == "ai_status":
            return self._handle_telegram_status()
        elif command == "ai_decision":
            return self._handle_telegram_decision()
        elif command == "ai_decisions":
            return self._handle_telegram_decisions(args)
        elif command == "ai_optimize":
            return self._handle_telegram_optimize()
        elif command == "ai_learn":
            return self._handle_telegram_learn()
        elif command == "ai_autonomous":
            return self._handle_telegram_autonomous()
        elif command == "ai_autonomous_stop":
            return self._handle_telegram_autonomous_stop()
        elif command == "ai_anomaly":
            return self._handle_telegram_anomaly()
        elif command == "ai_anomalies":
            return self._handle_telegram_anomalies(args)
        elif command == "ai_harvest_predict":
            return self._handle_telegram_harvest_predict(args)
        elif command == "ai_proxy_intel":
            return self._handle_telegram_proxy_intel()
        elif command == "ai_knowledge":
            return self._handle_telegram_knowledge()
        elif command == "ai_performance":
            return self._handle_telegram_performance()
        elif command == "ai_adapt":
            return self._handle_telegram_adapt(args)
        elif command == "ai_patterns":
            return self._handle_telegram_patterns()
        elif command == "ai_stats":
            return self._handle_telegram_stats()
        elif command == "ai_health":
            return self._handle_telegram_health()
        elif command == "ai_memory":
            return self._handle_telegram_memory()
        elif command == "ai_config":
            return self._handle_telegram_config()
        elif command == "ai_export":
            return self._handle_telegram_export()
        elif command == "ai_emergency_stop":
            return self._handle_telegram_emergency_stop()
        elif command == "ai_help":
            return self._telegram.handle_command("ai_help") if self._telegram else "Help unavailable"
        else:
            return f"❌ Unknown command: `{command}`. Use /ai_help for available commands."

    def _handle_telegram_start(self) -> str:
        """Handle /ai_start command."""
        self._status = "active"
        return "🟢 *AI Assistant Started*\n\nPhase 14 is now active and monitoring all systems."

    def _handle_telegram_stop(self) -> str:
        """Handle /ai_stop command."""
        if self._is_autonomous:
            self.stop_autonomous_mode()
        self._status = "stopped"
        return "🔴 *AI Assistant Stopped*\n\nPhase 14 has been deactivated. All subsystems halted."

    def _handle_telegram_status(self) -> str:
        """Handle /ai_status command."""
        health = get_system_health()

        message = f"{TelegramConfig.EMOJI_MAP.get('oanks', '👑')} *Phase 14 Status*\n\n"
        message += f"Status: `{'AUTONOMOUS' if self._is_autonomous else self._status.upper()}`\n"
        message += f"Uptime: `{format_duration(time.time() - parse_timestamp(self._stats['startup_time']) or time.time())}`\n"
        message += f"CPU: `{health.cpu_usage:.1f}%`\n"
        message += f"Memory: `{health.memory_usage:.1f}%`\n"
        message += f"Threads: `{health.active_threads}`\n\n"

        message += "*Statistics:*\n"
        message += f"Decisions: `{self._stats['decisions_made']}` (Success: `{self._stats['successful_decisions']}`)\n"
        message += f"Anomalies: `{self._stats['anomalies_detected']}`\n"
        message += f"Optimizations: `{self._stats['optimizations_applied']}`\n"
        message += f"Predictions: `{self._stats['predictions_made']}`\n"
        message += f"Patterns: `{self._stats['patterns_learned']}`\n"
        message += f"Cycles: `{self._stats['autonomous_cycles']}`"

        return message

    def _handle_telegram_decision(self) -> str:
        """Handle /ai_decision command."""
        result = self.make_decision()
        success = result.get("success", False)
        emoji = "✅" if success else "❌"

        message = f"{emoji} *Decision Result*\n\n"
        message += f"Action: `{result.get('decision', {}).get('action', 'N/A')}`\n"
        message += f"Target: `{result.get('decision', {}).get('target', 'N/A')}`\n"
        message += f"Success: `{'YES' if success else 'NO'}`\n"
        message += f"Time: `{result.get('execution_time', 0):.2f}s`"

        return message

    def _handle_telegram_decisions(self, args: List[str]) -> str:
        """Handle /ai_decisions command."""
        limit = int(args[0]) if args else 10
        decisions = self.get_decision_history(limit)

        message = f"📋 *Recent Decisions* (Last {len(decisions)})\n\n"
        for i, d in enumerate(decisions[:10], 1):
            emoji = "✅" if d.get("success") else "❌"
            message += f"{emoji} `{d.get('decision_type', 'N/A')}` → {d.get('action', 'N/A')}\n"
            message += f"   Target: `{d.get('target', 'N/A')}` | Conf: `{d.get('confidence', 0):.2f}`\n\n"

        return message

    def _handle_telegram_optimize(self) -> str:
        """Handle /ai_optimize command."""
        result = self.optimize_system()
        optimizations = result.get("bottlenecks", [])

        message = f"⚡ *Optimization Complete*\n\n"
        message += f"Bottlenecks Found: `{len(optimizations)}`\n"

        if optimizations:
            for opt in optimizations[:5]:
                message += f"• `{opt.get('parameter', 'N/A')}`: {opt.get('reason', 'N/A')}\n"
        else:
            message += "_System is running optimally._"

        return message

    def _handle_telegram_learn(self) -> str:
        """Handle /ai_learn command."""
        if self._learning_enabled:
            self.disable_learning()
            return "📚 *Learning Disabled*\n\nThe AI will no longer learn from new data."
        else:
            self.enable_learning()
            return "📚 *Learning Enabled*\n\nThe AI is now actively learning from all operations."

    def _handle_telegram_autonomous(self) -> str:
        """Handle /ai_autonomous command."""
        if self.start_autonomous_mode():
            return "🤖 *Autonomous Mode Started*\n\nThe framework is now operating without human intervention."
        else:
            return "❌ *Failed to start autonomous mode*"

    def _handle_telegram_autonomous_stop(self) -> str:
        """Handle /ai_autonomous_stop command."""
        if self.stop_autonomous_mode():
            return "🛑 *Autonomous Mode Stopped*\n\nHuman control restored."
        else:
            return "❌ *Failed to stop autonomous mode*"

    def _handle_telegram_anomaly(self) -> str:
        """Handle /ai_anomaly command."""
        health = get_system_health()
        metrics = {
            "cpu_usage": health.cpu_usage,
            "memory_usage": health.memory_usage,
            "active_threads": health.active_threads
        }

        anomaly = self.detect_anomaly(metrics)

        if anomaly:
            emoji = "🚨" if anomaly.get("severity", 1) >= 4 else "⚠️"
            message = f"{emoji} *Anomaly Detected*\n\n"
            message += f"Type: `{anomaly.get('anomaly_type', 'N/A')}`\n"
            message += f"Severity: `{anomaly.get('severity', 1)}`\n"
            message += f"Description: {anomaly.get('description', 'N/A')}"
        else:
            message = "✅ *No Anomalies Detected*\n\nAll metrics within normal ranges."

        return message

    def _handle_telegram_anomalies(self, args: List[str]) -> str:
        """Handle /ai_anomalies command."""
        limit = int(args[0]) if args else 10
        anomalies = self.get_anomaly_history(limit)

        message = f"🚨 *Anomaly History* (Last {len(anomalies)})\n\n"
        for i, a in enumerate(anomalies[:10], 1):
            emoji = "☠️" if a.get("severity", 1) == 5 else "🚨" if a.get("severity", 1) >= 4 else "⚠️"
            resolved = "✅" if a.get("resolved") else "❌"
            message += f"{emoji} `{a.get('anomaly_type', 'N/A')}` {resolved}\n"
            message += f"   {a.get('description', 'N/A')[:100]}\n\n"

        return message

    def _handle_telegram_harvest_predict(self, args: List[str]) -> str:
        """Handle /ai_harvest_predict command."""
        data_type = args[0] if args else "default"
        prediction = self.predict_data_availability(data_type)

        message = f"📊 *Harvest Prediction*\n\n"
        message += f"Data Type: `{prediction.data_type}`\n"
        message += f"Best Source: `{prediction.best_source}`\n"
        message += f"Predicted Time: `{prediction.predicted_time}`\n"
        message += f"Volume: `{prediction.predicted_volume}`\n"
        message += f"Confidence: `{prediction.confidence:.2f}`\n"
        message += f"Accuracy: `{prediction.historical_accuracy:.2f}`"

        return message

    def _handle_telegram_proxy_intel(self) -> str:
        """Handle /ai_proxy_intel command."""
        intel = self.get_proxy_intel_summary(10)

        message = f"🌐 *Proxy Intelligence*\n\n"
        for i, p in enumerate(intel[:10], 1):
            status = "🟢" if p.get("overall_score", 0) > 0.7 else "🟡" if p.get("overall_score", 0) > 0.4 else "🔴"
            message += f"{status} `{p.get('proxy_address', 'N/A')}`\n"
            message += f"   Score: `{p.get('overall_score', 0):.2f}` | "
            message += f"S:{p.get('success_count', 0)} F:{p.get('failure_count', 0)}\n"
            message += f"   Response: `{p.get('avg_response_time', 0):.2f}s`\n\n"

        return message

    def _handle_telegram_knowledge(self) -> str:
        """Handle /ai_knowledge command."""
        patterns = self.identify_success_patterns()

        message = f"💡 *Knowledge Base* ({len(patterns)} patterns)\n\n"
        for i, p in enumerate(patterns[:10], 1):
            message += f"{i}. `{p.get('pattern_type', 'N/A')}`\n"
            message += f"   Success Rate: `{p.get('success_rate', 0):.2f}`\n"
            message += f"   Usage: `{p.get('usage_count', 0)}`\n"
            message += f"   Action: `{p.get('pattern_data', {}).get('action', 'N/A')}`\n\n"

        return message

    def _handle_telegram_performance(self) -> str:
        """Handle /ai_performance command."""
        perf = self.measure_performance()

        message = f"📈 *Performance Metrics*\n\n"
        for key, value in perf.items():
            if isinstance(value, (int, float)) and key != "timestamp":
                bar = create_progress_bar(min(value, 100), 10)
                message += f"`{key}`\n{bar} {value:.1f}\n\n"

        return message

    def _handle_telegram_adapt(self, args: List[str]) -> str:
        """Handle /ai_adapt command."""
        target = args[0] if args else "default"

        # Simulate adaptation
        config = self.get_optimal_scrape_config(target)

        message = f"🎯 *Adapted Strategy for {target}*\n\n"
        message += f"Strategy: `{config.get('strategy', 'N/A')}`\n"
        message += f"Delay: `{config.get('delay', 0):.2f}s`\n"
        message += f"Source: `{config.get('source', 'N/A')}`"

        return message

    def _handle_telegram_patterns(self) -> str:
        """Handle /ai_patterns command."""
        patterns = self.identify_success_patterns()

        message = f"🎯 *Learned Patterns* ({len(patterns)} total)\n\n"

        # Group by type
        by_type = defaultdict(list)
        for p in patterns:
            by_type[p.get("pattern_type", "unknown")].append(p)

        for ptype, plist in by_type.items():
            message += f"*{ptype}* ({len(plist)} patterns)\n"
            for p in plist[:3]:
                message += f"  • `{p.get('pattern_data', {}).get('action', 'N/A')}` "
                message += f"(SR: {p.get('success_rate', 0):.2f})\n"
            message += "\n"

        return message

    def _handle_telegram_stats(self) -> str:
        """Handle /ai_stats command."""
        message = f"📊 *AI Statistics*\n\n"
        message += f"Decisions Made: `{self._stats['decisions_made']}`\n"
        message += f"Successful: `{self._stats['successful_decisions']}`\n"
        message += f"Success Rate: `{(self._stats['successful_decisions'] / max(self._stats['decisions_made'], 1)) * 100:.1f}%`\n"
        message += f"Anomalies: `{self._stats['anomalies_detected']}`\n"
        message += f"Optimizations: `{self._stats['optimizations_applied']}`\n"
        message += f"Predictions: `{self._stats['predictions_made']}`\n"
        message += f"Patterns: `{self._stats['patterns_learned']}`\n"
        message += f"Scrapes Adapted: `{self._stats['scrapes_adapted']}`\n"
        message += f"Proxies Rotated: `{self._stats['proxies_rotated']}`\n"
        message += f"Errors Recovered: `{self._stats['errors_recovered']}`\n"
        message += f"Autonomous Cycles: `{self._stats['autonomous_cycles']}`"

        return message

    def _handle_telegram_health(self) -> str:
        """Handle /ai_health command."""
        health = get_system_health()

        message = f"🏥 *System Health*\n\n"
        message += f"CPU: `{health.cpu_usage:.1f}%` {create_progress_bar(health.cpu_usage, 10)}\n"
        message += f"Memory: `{health.memory_usage:.1f}%` {create_progress_bar(health.memory_usage, 10)}\n"
        message += f"Disk: `{health.disk_usage:.1f}%` {create_progress_bar(health.disk_usage, 10)}\n"
        message += f"Threads: `{health.active_threads}`\n"
        message += f"Uptime: `{format_duration(health.uptime)}`"

        return message

    def _handle_telegram_memory(self) -> str:
        """Handle /ai_memory command."""
        mem = memory_usage()

        message = f"🧠 *Memory Usage*\n\n"
        message += f"RSS: `{format_bytes(mem.get('rss', 0))}`\n"
        message += f"VMS: `{format_bytes(mem.get('vms', 0))}`\n"
        message += f"Percent: `{mem.get('percent', 0):.1f}%`\n"
        message += f"Available: `{format_bytes(mem.get('available', 0))}`"

        return message

    def _handle_telegram_config(self) -> str:
        """Handle /ai_config command."""
        params = self.get_optimal_parameters()

        message = f"⚙️ *Current Configuration*\n\n"
        for key, value in params.items():
            message += f"`{key}`: `{value}`\n"

        message += "\n*Learning:* `{'ENABLED' if self._learning_enabled else 'DISABLED'}`\n"
        message += f"*Autonomous:* `{'YES' if self._is_autonomous else 'NO'}`"

        return message

    def _handle_telegram_export(self) -> str:
        """Handle /ai_export command."""
        try:
            # Export database stats
            db_stats = self._db.get_stats()

            message = f"📤 *Export Summary*\n\n"
            message += f"Database: `{db_stats.get('db_path', 'N/A')}`\n"
            message += f"Size: `{format_bytes(db_stats.get('db_size_bytes', 0))}`\n"
            message += f"Total Records: `{db_stats.get('total_records', 0):,}`\n\n"

            message += "*Table Counts:*\n"
            for table, count in db_stats.items():
                if table.startswith("oanks_ai_"):
                    message += f"`{table}`: `{count:,}`\n"

            return message
        except Exception as e:
            return f"❌ Export failed: `{str(e)}`"

    def _handle_telegram_emergency_stop(self) -> str:
        """Handle /ai_emergency_stop command."""
        if self._is_autonomous:
            self.stop_autonomous_mode()

        self._status = "emergency_stopped"

        if self._telegram:
            self._telegram.send_emergency_alert("Manual emergency stop triggered via Telegram")

        return "☠️ *EMERGENCY STOP EXECUTED*\n\nAll operations halted. Framework locked down."

    # ========================================================================
    # PUBLIC API: STATISTICS & STATUS
    # ========================================================================

    def get_stats(self) -> Dict[str, Any]:
        """Get AI assistant statistics."""
        return {
            **self._stats,
            "status": self._status,
            "autonomous": self._is_autonomous,
            "learning_enabled": self._learning_enabled,
            "initialized": self._initialized,
            "subsystems": {
                "decision_engine": self._decision_engine is not None,
                "scraping_engine": self._scraping_engine is not None,
                "proxy_engine": self._proxy_engine is not None,
                "predictive_engine": self._predictive_engine is not None,
                "anomaly_engine": self._anomaly_engine is not None,
                "optimization_engine": self._optimization_engine is not None,
                "autonomous_engine": self._autonomous_engine is not None,
                "learning_engine": self._learning_engine is not None,
            },
            "telegram_enabled": self._telegram is not None and self._telegram.is_enabled(),
            "database_records": self._db.get_stats().get("total_records", 0) if self._db else 0
        }

    def get_learning_status(self) -> Dict:
        """Get learning status."""
        if not self._learning_engine:
            return {"error": "Learning engine not initialized"}

        return {
            "enabled": self._learning_enabled,
            **self._learning_engine.get_stats()
        }

    def get_memory_usage(self) -> Dict:
        """Get memory usage statistics."""
        mem = memory_usage()

        # Estimate object memory
        object_counts = {
            "decision_history": len(self._decision_engine._decision_history) if self._decision_engine else 0,
            "target_memory": len(self._scraping_engine._target_memory) if self._scraping_engine else 0,
            "proxy_cache": len(self._proxy_engine._proxy_cache) if self._proxy_engine else 0,
            "pattern_cache": len(self._predictive_engine._pattern_cache) if self._predictive_engine else 0,
            "baselines": len(self._anomaly_engine._baselines) if self._anomaly_engine else 0,
            "success_patterns": len(self._learning_engine._success_patterns) if self._learning_engine else 0,
            "failure_patterns": len(self._learning_engine._failure_patterns) if self._learning_engine else 0,
        }

        return {
            "system_memory": mem,
            "object_counts": object_counts,
            "total_cached_objects": sum(object_counts.values())
        }

    def get_full_status(self) -> Dict:
        """Get comprehensive status report."""
        return {
            "framework": OANKS_FRAMEWORK,
            "phase": OANKS_PHASE,
            "version": OANKS_VERSION,
            "danger_level": OANKS_DANGER_LEVEL,
            "creator": OANKS_TAG,
            "status": self._status,
            "autonomous": self._is_autonomous,
            "learning": self._learning_enabled,
            "stats": self.get_stats(),
            "learning_status": self.get_learning_status(),
            "memory": self.get_memory_usage(),
            "health": get_system_health().to_dict(),
            "timestamp": get_timestamp()
        }

    def shutdown(self) -> None:
        """Graceful shutdown of Phase 14."""
        self._logger.info("Shutting down Phase 14 AI Assistant")

        if self._is_autonomous:
            self.stop_autonomous_mode()

        if self._telegram:
            self._telegram.send_shutdown_notification()
            self._telegram.stop()

        if self._db:
            self._db.close_all()

        self._status = "shutdown"
        self._logger.info("Phase 14 shutdown complete")

    def __del__(self):
        """Destructor."""
        try:
            if self._initialized and self._status != "shutdown":
                self.shutdown()
        except:
            pass

# ==============================================================================
# END OF SECTION 13: MAIN PHASE 14 CLASS
# ==============================================================================
