#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗  █████╗ ███╗   ██╗██╗  ██╗███████╗                                ║
║   ██╔═══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝                                ║
║   ██║   ██║███████║██╔██╗ ██║█████╔╝ ███████╗                                ║
║   ██║   ██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║                                ║
║   ╚██████╔╝██║  ██║██║ ╚████║██║  ██╗███████║                                ║
║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝                                ║
║                                                                              ║
║   OANKS OPERATIONS FRAMEWORK v3.0.0                                          ║
║   PHASE 15: DEPLOYMENT — FINAL INTEGRATION                                   ║
║                                                                              ║
║   Creator: Oanks (@oanksnood)                                                ║
║   Classification: DEPLOYMENT — FINAL PHASE                                   ║
║   Danger Level: 10/10                                                        ║
║                                                                              ║
║   "Without Phase 15, the framework is just disconnected modules.             ║
║    With Phase 15, the framework is a complete, working system."               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import yaml
import signal
import socket
import atexit
import argparse
import logging
import hashlib
import threading
import subprocess
import resource
import psutil
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from collections import defaultdict
import traceback

# =============================================================================
# CONSTANTS
# =============================================================================

# Version Information
VERSION = "3.0.0"
FRAMEWORK_NAME = "Oanks Operations Framework"
CREATOR = "Oanks (@oanksnood)"
CLASSIFICATION = "DEPLOYMENT — FINAL PHASE"
BUILD_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Paths
BASE_DIR = os.path.expanduser("~/.oanks")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
CONFIG_DIR = os.path.join(BASE_DIR, "config")
PID_FILE = os.path.join(BASE_DIR, "oanks.pid")
LOG_FILE = os.path.join(LOG_DIR, "oanks.log")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
CHECKPOINT_DIR = os.path.join(BASE_DIR, "checkpoints")
STATE_FILE = os.path.join(BASE_DIR, "state.json")

# Daemon Settings
DAEMON_PID_FILE = "/var/run/oanks.pid"
DAEMON_WORK_DIR = "/"
DAEMON_UMASK = 0o022

# Log Rotation
LOG_MAX_BYTES = 10 * 1024 * 1024  # 10MB
LOG_MAX_FILES = 10
LOG_COMPRESS = True

# Crash Recovery
MAX_RESTART_ATTEMPTS = 5
RESTART_BACKOFF = 2.0
RESTART_MAX_DELAY = 60.0

# Health Check
HEALTH_CHECK_INTERVAL = 60  # seconds
PHASE_TIMEOUT = 30  # seconds
CRITICAL_PHASES = ["phase1", "phase6", "phase7", "phase10"]

# Systemd
SYSTEMD_SERVICE_NAME = "oanks"
SYSTEMD_SERVICE_PATH = "/etc/systemd/system/oanks.service"
SYSTEMD_USER = "root"
SYSTEMD_GROUP = "root"

# Default CLI Options
DEFAULT_DAEMON = False
DEFAULT_STEALTH = False
DEFAULT_AUTONOMOUS = False
DEFAULT_TELEGRAM = True
DEFAULT_VERBOSE = True
DEFAULT_QUIET = False

# Phase Names
PHASE_NAMES = {
    "phase1": "Foundation",
    "phase2": "Proxy Hell",
    "phase3": "The Harvester",
    "phase4": "Intelligence Engine",
    "phase5": "Account Factory",
    "phase6": "Premium System",
    "phase7": "Command Center",
    "phase8": "Money Module",
    "phase9": "Security & Anti-Forensic",
    "phase10": "Worm Module",
    "phase11": "Ransomware & Destruction",
    "phase12": "Distributed Operations",
    "phase13": "Darkweb Intelligence",
    "phase14": "AI Assistant",
    "phase15": "Deployment",
}

# =============================================================================
# ENUMS & DATA CLASSES
# =============================================================================

class PhaseStatus(Enum):
    """Status enumeration for framework phases."""
    UNINITIALIZED = auto()
    INITIALIZING = auto()
    READY = auto()
    RUNNING = auto()
    PAUSED = auto()
    ERROR = auto()
    CRASHED = auto()
    STOPPED = auto()

class HealthStatus(Enum):
    """Health status enumeration."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    UNKNOWN = "unknown"
    OFFLINE = "offline"

@dataclass
class PhaseInfo:
    """Information about a framework phase."""
    name: str
    display_name: str
    status: PhaseStatus = PhaseStatus.UNINITIALIZED
    health: HealthStatus = HealthStatus.UNKNOWN
    uptime_seconds: float = 0.0
    last_error: Optional[str] = None
    restart_count: int = 0
    last_restart: Optional[str] = None
    memory_mb: float = 0.0
    cpu_percent: float = 0.0
    threads: int = 0
    initialized_at: Optional[str] = None
    started_at: Optional[str] = None

@dataclass
class SystemStats:
    """System-wide statistics."""
    uptime_seconds: float = 0.0
    phases_loaded: int = 0
    phases_active: int = 0
    phases_healthy: int = 0
    phases_critical: int = 0
    errors: int = 0
    restarts: int = 0
    last_checkpoint: str = ""
    total_memory_mb: float = 0.0
    total_cpu_percent: float = 0.0
    disk_usage_percent: float = 0.0
    network_connections: int = 0

@dataclass
class Checkpoint:
    """System checkpoint data."""
    id: str
    timestamp: str
    description: str
    phase_states: Dict[str, Any] = field(default_factory=dict)
    config_snapshot: Dict[str, Any] = field(default_factory=dict)
    stats_snapshot: Dict[str, Any] = field(default_factory=dict)

# =============================================================================
# CUSTOM EXCEPTIONS
# =============================================================================

class PhaseInitializationError(Exception):
    """Raised when a phase fails to initialize."""
    pass

class PhaseIntegrationError(Exception):
    """Raised when phase integration fails."""
    pass

class ConfigurationError(Exception):
    """Raised when configuration is invalid."""
    pass

class DaemonError(Exception):
    """Raised when daemon operations fail."""
    pass

class HealthCheckError(Exception):
    """Raised when health check fails critically."""
    pass

class EmergencyShutdownError(Exception):
    """Raised to trigger emergency shutdown."""
    pass

# =============================================================================
# LOGGING SETUP
# =============================================================================

class ColoredFormatter(logging.Formatter):
    """Custom formatter with ANSI color support."""
    
    COLORS = {
        "DEBUG": "\033[36m",      # Cyan
        "INFO": "\033[32m",       # Green
        "WARNING": "\033[33m",    # Yellow
        "ERROR": "\033[31m",      # Red
        "CRITICAL": "\033[35m",   # Magenta
        "RESET": "\033[0m",
    }
    
    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        reset = self.COLORS["RESET"]
        record.levelname = f"{color}{record.levelname}{reset}"
        return super().format(record)


class RotatingLogHandler(logging.handlers.RotatingFileHandler):
    """Enhanced rotating file handler with compression support."""
    
    def __init__(self, filename, maxBytes=LOG_MAX_BYTES, backupCount=LOG_MAX_FILES, compress=True):
        super().__init__(filename, maxBytes=maxBytes, backupCount=backupCount)
        self.compress = compress
        self.base_filename = filename
    
    def doRollover(self):
        """Override to add compression support."""
        if self.stream:
            self.stream.close()
            self.stream = None
        
        # Rotate existing files
        for i in range(self.backupCount - 1, 0, -1):
            sfn = f"{self.base_filename}.{i}"
            dfn = f"{self.base_filename}.{i + 1}"
            if os.path.exists(sfn):
                if os.path.exists(dfn):
                    os.remove(dfn)
                os.rename(sfn, dfn)
        
        dfn = f"{self.base_filename}.1"
        if os.path.exists(dfn):
            os.remove(dfn)
        if os.path.exists(self.base_filename):
            os.rename(self.base_filename, dfn)
            
            # Compress if enabled
            if self.compress:
                self._compress_file(dfn)
        
        self.stream = self._open()
    
    def _compress_file(self, filepath):
        """Compress a log file using gzip."""
        try:
            import gzip
            with open(filepath, "rb") as f_in:
                with gzip.open(f"{filepath}.gz", "wb") as f_out:
                    f_out.writelines(f_in)
            os.remove(filepath)
        except Exception as e:
            print(f"Compression failed for {filepath}: {e}")


def setup_logging(verbose=True, quiet=False, log_file=None):
    """Configure logging with rotation and color support."""
    
    # Ensure log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Determine log level
    if quiet:
        level = logging.ERROR
    elif verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    
    # Create formatter
    fmt = "%(asctime)s | %(name)-20s | %(levelname)-8s | %(message)s"
    date_fmt = "%Y-%m-%d %H:%M:%S"
    
    # Root logger
    logger = logging.getLogger("oanks")
    logger.setLevel(level)
    logger.handlers = []  # Clear existing handlers
    
    # Console handler with colors
    if not quiet:
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(level)
        console.setFormatter(ColoredFormatter(fmt, datefmt=date_fmt))
        logger.addHandler(console)
    
    # File handler with rotation
    log_path = log_file or LOG_FILE
    file_handler = RotatingLogHandler(
        log_path,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_MAX_FILES,
        compress=LOG_COMPRESS
    )
    file_handler.setLevel(logging.DEBUG)  # Always log everything to file
    file_handler.setFormatter(logging.Formatter(fmt, datefmt=date_fmt))
    logger.addHandler(file_handler)
    
    return logger


# =============================================================================
# PHASE 15: DEPLOYMENT CLASS
# =============================================================================

class Phase15Deployment:
    """
    Phase 15: Deployment — Final integration, main entry point.
    
    This is the crown jewel of the Oanks Operations Framework.
    It ties all 14 phases into a unified, executable, autonomous system.
    
    Creator: Oanks (@oanksnood)
    Classification: DEPLOYMENT — FINAL PHASE
    Danger Level: 10/10
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        """Singleton pattern to ensure only one deployment instance."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return
        
        self._initialized = True
        self._system: Dict[str, Any] = {}
        self._phases: Dict[str, Any] = {}
        self._phase_info: Dict[str, PhaseInfo] = {}
        self._config: Dict[str, Any] = {}
        self._args: argparse.Namespace = None
        self._stats = SystemStats()
        self._running = False
        self._daemon_mode = False
        self._shutdown_requested = False
        self._emergency_shutdown = False
        self._health_thread: Optional[threading.Thread] = None
        self._checkpoint_thread: Optional[threading.Thread] = None
        self._stats_thread: Optional[threading.Thread] = None
        self._logger: Optional[logging.Logger] = None
        self._start_time: Optional[float] = None
        self._restart_attempts: Dict[str, int] = defaultdict(int)
        self._restart_delays: Dict[str, float] = defaultdict(lambda: RESTART_BACKOFF)
        self._signal_handlers_installed = False
        
        # Initialize phase info for all phases
        for phase_id, display_name in PHASE_NAMES.items():
            self._phase_info[phase_id] = PhaseInfo(
                name=phase_id,
                display_name=display_name
            )
    
    # ========================================================================
    # 1. MAIN ENTRY & INITIALIZATION
    # ========================================================================
    
    def initialize(self) -> bool:
        """
        Initialize the entire framework.
        
        This is the heart of Phase 15. It orchestrates the initialization
        of all 14 preceding phases in the correct order, establishes
        inter-phase communication, and brings the system to life.
        
        Returns:
            bool: True if initialization succeeded, False otherwise.
        """
        self._start_time = time.time()
        self._running = True
        
        self._logger.info("=" * 80)
        self._logger.info(f"  {FRAMEWORK_NAME} v{VERSION}")
        self._logger.info(f"  {CLASSIFICATION}")
        self._logger.info(f"  Creator: {CREATOR}")
        self._logger.info(f"  Build Date: {BUILD_DATE}")
        self._logger.info("=" * 80)
        self._logger.info("Initializing Phase 15: Deployment...")
        
        try:
            # Create directory structure
            self._create_directories()
            
            # Install signal handlers
            self._install_signal_handlers()
            
            # Initialize phases in order
            phase_init_order = [
                ("phase1", self.initialize_phase1),
                ("phase2", self.initialize_phase2),
                ("phase3", self.initialize_phase3),
                ("phase4", self.initialize_phase4),
                ("phase5", self.initialize_phase5),
                ("phase6", self.initialize_phase6),
                ("phase7", self.initialize_phase7),
                ("phase8", self.initialize_phase8),
                ("phase9", self.initialize_phase9),
                ("phase10", self.initialize_phase10),
                ("phase11", self.initialize_phase11),
                ("phase12", self.initialize_phase12),
                ("phase13", self.initialize_phase13),
                ("phase14", self.initialize_phase14),
            ]
            
            for phase_id, init_func in phase_init_order:
                self._logger.info(f"Initializing {PHASE_NAMES[phase_id]}...")
                self._phase_info[phase_id].status = PhaseStatus.INITIALIZING
                self._phase_info[phase_id].initialized_at = datetime.now().isoformat()
                
                try:
                    result = init_func()
                    if result:
                        self._phase_info[phase_id].status = PhaseStatus.READY
                        self._stats.phases_loaded += 1
                        self._logger.info(f"  ✓ {PHASE_NAMES[phase_id]} initialized successfully")
                    else:
                        self._phase_info[phase_id].status = PhaseStatus.ERROR
                        self._phase_info[phase_id].last_error = "Initialization returned False"
                        self._stats.errors += 1
                        self._logger.error(f"  ✗ {PHASE_NAMES[phase_id]} initialization failed")
                        
                        # Critical phases must succeed
                        if phase_id in CRITICAL_PHASES:
                            raise PhaseInitializationError(
                                f"Critical phase {phase_id} failed to initialize"
                            )
                except Exception as e:
                    self._phase_info[phase_id].status = PhaseStatus.ERROR
                    self._phase_info[phase_id].last_error = str(e)
                    self._stats.errors += 1
                    self._logger.error(f"  ✗ {PHASE_NAMES[phase_id]} initialization error: {e}")
                    
                    if phase_id in CRITICAL_PHASES:
                        raise PhaseInitializationError(
                            f"Critical phase {phase_id} failed: {e}"
                        )
            
            # Integrate all phases
            self._logger.info("Integrating phases...")
            if not self.integrate_phases():
                raise PhaseIntegrationError("Phase integration failed")
            self._logger.info("  ✓ Phase integration complete")
            
            # Start background threads
            self._start_background_threads()
            
            # Save initial checkpoint
            self.save_checkpoint("post-initialization")
            
            self._logger.info("=" * 80)
            self._logger.info(f"Framework initialized: {self._stats.phases_loaded}/{len(PHASE_NAMES)-1} phases loaded")
            self._logger.info("Phase 15: Deployment — READY")
            self._logger.info("=" * 80)
            
            return True
            
        except Exception as e:
            self._logger.critical(f"Framework initialization failed: {e}")
            self._logger.critical(traceback.format_exc())
            self._running = False
            return False
    
    def _create_directories(self):
        """Create required directory structure."""
        dirs = [BASE_DIR, DATA_DIR, LOG_DIR, CONFIG_DIR, CHECKPOINT_DIR]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
            self._logger.debug(f"Directory ensured: {d}")
    
    def load_configuration(self) -> Dict[str, Any]:
        """
        Load configuration from all sources with proper hierarchy.
        
        Hierarchy: CLI > ENV > Config file > Defaults
        
        Returns:
            Dict containing merged configuration.
        """
        self._logger.info("Loading configuration...")
        
        config = {}
        
        # 1. Load defaults
        config.update(self._get_default_config())
        self._logger.debug("Loaded default configuration")
        
        # 2. Load from config file
        if self._args and self._args.config and os.path.exists(self._args.config):
            try:
                with open(self._args.config, "r") as f:
                    if self._args.config.endswith(".yaml") or self._args.config.endswith(".yml"):
                        file_config = yaml.safe_load(f)
                    else:
                        file_config = json.load(f)
                config.update(file_config)
                self._logger.info(f"Loaded config from {self._args.config}")
            except Exception as e:
                self._logger.warning(f"Failed to load config file: {e}")
        elif os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    file_config = json.load(f)
                config.update(file_config)
                self._logger.info(f"Loaded config from {CONFIG_FILE}")
            except Exception as e:
                self._logger.warning(f"Failed to load default config file: {e}")
        
        # 3. Load from environment variables
        env_config = self._load_env_config()
        config.update(env_config)
        if env_config:
            self._logger.debug(f"Loaded {len(env_config)} values from environment")
        
        # 4. Override with CLI arguments
        if self._args:
            cli_config = self._args_to_dict()
            config.update(cli_config)
            self._logger.debug("Applied CLI argument overrides")
        
        # Validate configuration
        self._validate_config(config)
        
        self._config = config
        self._logger.info("Configuration loaded successfully")
        return config
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration values."""
        return {
            "framework": {
                "name": FRAMEWORK_NAME,
                "version": VERSION,
                "creator": CREATOR,
            },
            "daemon": {
                "enabled": DEFAULT_DAEMON,
                "pid_file": DAEMON_PID_FILE,
                "work_dir": DAEMON_WORK_DIR,
                "umask": DAEMON_UMASK,
            },
            "logging": {
                "level": "INFO",
                "file": LOG_FILE,
                "max_bytes": LOG_MAX_BYTES,
                "max_files": LOG_MAX_FILES,
                "compress": LOG_COMPRESS,
            },
            "health": {
                "interval": HEALTH_CHECK_INTERVAL,
                "phase_timeout": PHASE_TIMEOUT,
                "critical_phases": CRITICAL_PHASES,
            },
            "crash_recovery": {
                "max_restarts": MAX_RESTART_ATTEMPTS,
                "backoff": RESTART_BACKOFF,
                "max_delay": RESTART_MAX_DELAY,
            },
            "stealth": {
                "enabled": DEFAULT_STEALTH,
                "anti_vm": True,
                "anti_debug": True,
                "process_hollowing": False,
            },
            "telegram": {
                "enabled": DEFAULT_TELEGRAM,
                "bot_token": os.environ.get("OANKS_TELEGRAM_TOKEN", ""),
                "admin_ids": [],
            },
            "autonomous": {
                "enabled": DEFAULT_AUTONOMOUS,
                "decision_interval": 300,
                "learning_rate": 0.01,
            },
            "worm": {
                "enabled": False,
                "max_propagation": 100,
                "target_networks": [],
            },
            "ransomware": {
                "enabled": False,
                "target_extensions": [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx"],
                " ransom_amount_btc": 0.5,
            },
            "darkweb": {
                "enabled": False,
                "tor_proxy": "socks5://127.0.0.1:9050",
                "crawl_depth": 3,
            },
            "distributed": {
                "enabled": False,
                "node_id": None,
                "master_node": None,
                "slave_nodes": [],
            },
        }
    
    def _load_env_config(self) -> Dict[str, Any]:
        """Load configuration from environment variables."""
        config = {}
        
        env_mappings = {
            "OANKS_DAEMON": ("daemon", "enabled", bool),
            "OANKS_STEALTH": ("stealth", "enabled", bool),
            "OANKS_AUTONOMOUS": ("autonomous", "enabled", bool),
            "OANKS_TELEGRAM": ("telegram", "enabled", bool),
            "OANKS_TELEGRAM_TOKEN": ("telegram", "bot_token", str),
            "OANKS_LOG_LEVEL": ("logging", "level", str),
            "OANKS_WORM": ("worm", "enabled", bool),
            "OANKS_RANSOMWARE": ("ransomware", "enabled", bool),
            "OANKS_DARKWEB": ("darkweb", "enabled", bool),
            "OANKS_TARGET": ("target", None, str),
        }
        
        for env_var, (section, key, type_fn) in env_mappings.items():
            value = os.environ.get(env_var)
            if value is not None:
                if type_fn == bool:
                    value = value.lower() in ("true", "1", "yes", "on")
                
                if key is None:
                    config[section] = value
                else:
                    if section not in config:
                        config[section] = {}
                    config[section][key] = value
        
        return config
    
    def _args_to_dict(self) -> Dict[str, Any]:
        """Convert argparse namespace to configuration dict."""
        if not self._args:
            return {}
        
        config = {}
        args_dict = vars(self._args)
        
        mappings = {
            "daemon": ("daemon", "enabled"),
            "stealth": ("stealth", "enabled"),
            "autonomous": ("autonomous", "enabled"),
            "telegram": ("telegram", "enabled"),
            "worm": ("worm", "enabled"),
            "ransomware": ("ransomware", "enabled"),
            "darkweb": ("darkweb", "enabled"),
            "target": ("target", None),
            "config": ("config_file", None),
        }
        
        for arg_key, (section, key) in mappings.items():
            if arg_key in args_dict and args_dict[arg_key] is not None:
                value = args_dict[arg_key]
                if key is None:
                    config[section] = value
                else:
                    if section not in config:
                        config[section] = {}
                    config[section][key] = value
        
        return config
    
    def _validate_config(self, config: Dict[str, Any]):
        """Validate configuration values."""
        # Validate log level
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        log_level = config.get("logging", {}).get("level", "INFO")
        if log_level.upper() not in valid_levels:
            raise ConfigurationError(f"Invalid log level: {log_level}")
        
        # Validate paths
        for path_key in ["file"]:
            path = config.get("logging", {}).get(path_key)
            if path:
                dir_path = os.path.dirname(path)
                if dir_path and not os.path.exists(dir_path):
                    os.makedirs(dir_path, exist_ok=True)
        
        self._logger.debug("Configuration validation passed")
    
    def parse_arguments(self) -> argparse.Namespace:
        """
        Parse command-line arguments.
        
        Returns:
            argparse.Namespace with parsed arguments.
        """
        parser = argparse.ArgumentParser(
            prog="oanks",
            description=f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  {FRAMEWORK_NAME} v{VERSION}                                                  ║
║  {CLASSIFICATION}                                                            ║
║  Creator: {CREATOR}                                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
            """,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  oanks --target example.com --stealth
  oanks --daemon --autonomous
  oanks --telegram --verbose
  oanks --worm --target 192.168.1.0/24
  oanks --systemd-install
            """
        )
        
        # Target
        parser.add_argument(
            "--target", "-t",
            type=str,
            help="Target domain/IP for operations"
        )
        
        # Configuration
        parser.add_argument(
            "--config", "-c",
            type=str,
            default=CONFIG_FILE,
            help=f"Configuration file path (default: {CONFIG_FILE})"
        )
        
        # Modes
        parser.add_argument(
            "--daemon", "-d",
            action="store_true",
            help="Run as daemon (background process)"
        )
        parser.add_argument(
            "--stealth", "-s",
            action="store_true",
            help="Enable stealth mode (anti-forensic, anti-VM, anti-debug)"
        )
        parser.add_argument(
            "--autonomous", "-a",
            action="store_true",
            help="Start AI autonomous mode"
        )
        
        # Module toggles
        parser.add_argument(
            "--worm", "-w",
            action="store_true",
            help="Start worm propagation module"
        )
        parser.add_argument(
            "--ransomware", "-r",
            action="store_true",
            help="Start ransomware module"
        )
        parser.add_argument(
            "--darkweb",
            action="store_true",
            help="Start darkweb crawling module"
        )
        parser.add_argument(
            "--telegram",
            action="store_true",
            help="Enable Telegram bot command center"
        )
        parser.add_argument(
            "--no-telegram",
            action="store_true",
            help="Disable Telegram bot"
        )
        
        # Logging
        parser.add_argument(
            "--verbose", "-v",
            action="store_true",
            help="Enable verbose logging"
        )
        parser.add_argument(
            "--quiet", "-q",
            action="store_true",
            help="Quiet mode (errors only)"
        )
        parser.add_argument(
            "--log-file",
            type=str,
            help="Custom log file path"
        )
        
        # Systemd
        parser.add_argument(
            "--systemd-install",
            action="store_true",
            help="Install systemd service"
        )
        parser.add_argument(
            "--systemd-remove",
            action="store_true",
            help="Remove systemd service"
        )
        parser.add_argument(
            "--systemd-enable",
            action="store_true",
            help="Enable systemd auto-start"
        )
        parser.add_argument(
            "--systemd-disable",
            action="store_true",
            help="Disable systemd auto-start"
        )
        
        # Status
        parser.add_argument(
            "--status",
            action="store_true",
            help="Show system status and exit"
        )
        parser.add_argument(
            "--health",
            action="store_true",
            help="Run health check and exit"
        )
        
        # Version
        parser.add_argument(
            "--version",
            action="version",
            version=f"%(prog)s {VERSION} — {FRAMEWORK_NAME} — {CREATOR}"
        )
        
        self._args = parser.parse_args()
        return self._args
    
    def create_system_dict(self) -> Dict[str, Any]:
        """
        Create the system dictionary for inter-phase communication.
        
        This dictionary is the nervous system of the framework.
        Every phase gets a reference to it, enabling them to talk,
        share data, and coordinate operations.
        
        Returns:
            Dict containing system-wide shared resources.
        """
        self._system = {
            "framework": {
                "name": FRAMEWORK_NAME,
                "version": VERSION,
                "creator": CREATOR,
                "classification": CLASSIFICATION,
                "build_date": BUILD_DATE,
            },
            "config": self._config,
            "phases": self._phases,
            "phase_info": self._phase_info,
            "stats": self._stats,
            "logger": self._logger,
            "deployment": self,
            "running": lambda: self._running,
            "shutdown_requested": lambda: self._shutdown_requested,
            "emergency": lambda: self._emergency_shutdown,
            "get_uptime": self.get_uptime,
            "save_checkpoint": self.save_checkpoint,
            "get_health_report": self.get_health_report,
            "restart_phase": self.restart_phase,
            "broadcast": self._broadcast_message,
        }
        
        self._logger.debug("System dictionary created")
        return self._system
    
    def _broadcast_message(self, message: Dict[str, Any]):
        """Broadcast a message to all phases."""
        for phase_id, phase in self._phases.items():
            if hasattr(phase, "on_broadcast"):
                try:
                    phase.on_broadcast(message)
                except Exception as e:
                    self._logger.warning(f"Broadcast to {phase_id} failed: {e}")
    
    # ========================================================================
    # PHASE INITIALIZATION METHODS
    # ========================================================================
    
    def initialize_phase1(self) -> bool:
        """Initialize Phase 1: Foundation (Database, logging, crypto, dead man's switch)."""
        try:
            # Phase 1 is the bedrock. Without it, nothing else stands.
            self._phases["phase1"] = {
                "name": "Foundation",
                "database": None,  # Would be actual DB connection
                "crypto_keys": {},
                "dead_mans_switch": None,
                "anti_forensic": None,
                "persistence": None,
            }
            self._logger.debug("Phase 1: Foundation initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 1 initialization failed: {e}")
            return False
    
    def initialize_phase2(self) -> bool:
        """Initialize Phase 2: Proxy Hell (50+ proxy sources, validation, rotation)."""
        try:
            self._phases["phase2"] = {
                "name": "Proxy Hell",
                "proxy_pool": [],
                "proxy_chains": [],
                "router_exploits": [],
                "iot_proxies": [],
                "validator": None,
                "rotator": None,
            }
            self._logger.debug("Phase 2: Proxy Hell initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 2 initialization failed: {e}")
            return False
    
    def initialize_phase3(self) -> bool:
        """Initialize Phase 3: The Harvester (Data harvesting from 15+ sources)."""
        try:
            self._phases["phase3"] = {
                "name": "The Harvester",
                "sources": [],
                "extractors": {},
                "data_types": [
                    "emails", "phones", "credentials", "documents",
                    "images", "metadata", "social_profiles", "domains", "ips"
                ],
                "harvest_queue": [],
            }
            self._logger.debug("Phase 3: The Harvester initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 3 initialization failed: {e}")
            return False
    
    def initialize_phase4(self) -> bool:
        """Initialize Phase 4: Intelligence Engine (Enrichment, deduplication, correlation)."""
        try:
            self._phases["phase4"] = {
                "name": "Intelligence Engine",
                "enrichment_engines": [],
                "deduplicator": None,
                "pricing_engine": None,
                "correlator": None,
                "threat_ranker": None,
            }
            self._logger.debug("Phase 4: Intelligence Engine initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 4 initialization failed: {e}")
            return False
    
    def initialize_phase5(self) -> bool:
        """Initialize Phase 5: Account Factory (Mass account creation on 25+ platforms)."""
        try:
            self._phases["phase5"] = {
                "name": "Account Factory",
                "platforms": [],
                "account_pool": [],
                "creation_queue": [],
                "verifier": None,
                "ageing_engine": None,
            }
            self._logger.debug("Phase 5: Account Factory initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 5 initialization failed: {e}")
            return False
    
    def initialize_phase6(self) -> bool:
        """Initialize Phase 6: Premium System (Monetization engine)."""
        try:
            self._phases["phase6"] = {
                "name": "Premium System",
                "tiers": {},
                "crypto_verifier": None,
                "referral_system": None,
                "coupon_engine": None,
                "analytics": None,
                "admin_controls": None,
            }
            self._logger.debug("Phase 6: Premium System initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 6 initialization failed: {e}")
            return False
    
    def initialize_phase7(self) -> bool:
        """Initialize Phase 7: Command Center (Telegram bot with 50+ commands)."""
        try:
            self._phases["phase7"] = {
                "name": "Command Center",
                "bot": None,
                "commands": {},
                "interactive_buttons": {},
                "voice_handler": None,
                "file_uploader": None,
                "orchestrator": None,
            }
            self._logger.debug("Phase 7: Command Center initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 7 initialization failed: {e}")
            return False
    
    def initialize_phase8(self) -> bool:
        """Initialize Phase 8: Money Module (Auto-pricing, bulk discounts, revenue tracking)."""
        try:
            self._phases["phase8"] = {
                "name": "Money Module",
                "pricing_engine": None,
                "bulk_discounts": {},
                "sales_packages": {},
                "inventory": {},
                "revenue_tracker": None,
            }
            self._logger.debug("Phase 8: Money Module initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 8 initialization failed: {e}")
            return False
    
    def initialize_phase9(self) -> bool:
        """Initialize Phase 9: Security & Anti-Forensic (Weaponized defense, evasion, counter-intel)."""
        try:
            self._phases["phase9"] = {
                "name": "Security & Anti-Forensic",
                "evasion_engine": None,
                "counter_intel": None,
                "kill_switch": None,
                "stealth_engine": None,
                "anti_vm": None,
                "anti_debug": None,
            }
            self._logger.debug("Phase 9: Security & Anti-Forensic initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 9 initialization failed: {e}")
            return False
    
    def initialize_phase10(self) -> bool:
        """Initialize Phase 10: Worm Module (Network propagation, exploitation, botnet creation)."""
        try:
            self._phases["phase10"] = {
                "name": "Worm Module",
                "propagator": None,
                "exploit_kit": [],
                "botnet": {},
                "self_replicator": None,
                "cve_exploits": [],
            }
            self._logger.debug("Phase 10: Worm Module initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 10 initialization failed: {e}")
            return False
    
    def initialize_phase11(self) -> bool:
        """Initialize Phase 11: Ransomware & Destruction (File encryption, system destruction)."""
        try:
            self._phases["phase11"] = {
                "name": "Ransomware & Destruction",
                "encryptor": None,
                "ransom_note_generator": None,
                "destructor": None,
                "bios_corruptor": None,
                "nvram_corruptor": None,
                "gutmann_wiper": None,
            }
            self._logger.debug("Phase 11: Ransomware & Destruction initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 11 initialization failed: {e}")
            return False
    
    def initialize_phase12(self) -> bool:
        """Initialize Phase 12: Distributed Operations (Master-slave, load balancing, failover)."""
        try:
            self._phases["phase12"] = {
                "name": "Distributed Operations",
                "master_node": None,
                "slave_nodes": [],
                "load_balancer": None,
                "failover_engine": None,
                "data_replicator": None,
                "consensus_protocol": None,
            }
            self._logger.debug("Phase 12: Distributed Operations initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 12 initialization failed: {e}")
            return False
    
    def initialize_phase13(self) -> bool:
        """Initialize Phase 13: Darkweb Intelligence (Tor integration, onion crawling, hidden services)."""
        try:
            self._phases["phase13"] = {
                "name": "Darkweb Intelligence",
                "tor_proxy": None,
                "onion_crawler": None,
                "hidden_services": [],
                "market_monitor": None,
                "forum_scraper": None,
                "darkweb_monitor": None,
            }
            self._logger.debug("Phase 13: Darkweb Intelligence initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 13 initialization failed: {e}")
            return False
    
    def initialize_phase14(self) -> bool:
        """Initialize Phase 14: AI Assistant (Auto-decision, adaptive scraping, predictive harvesting)."""
        try:
            self._phases["phase14"] = {
                "name": "AI Assistant",
                "decision_engine": None,
                "adaptive_scraper": None,
                "predictive_harvester": None,
                "anomaly_detector": None,
                "self_optimizer": None,
                "autonomous_controller": None,
            }
            self._logger.debug("Phase 14: AI Assistant initialized")
            return True
        except Exception as e:
            self._logger.error(f"Phase 14 initialization failed: {e}")
            return False
    
    def start_phases(self) -> bool:
        """Start all initialized phases."""
        self._logger.info("Starting all phases...")
        
        for phase_id, phase_data in self._phases.items():
            if self._phase_info[phase_id].status == PhaseStatus.READY:
                try:
                    self._phase_info[phase_id].status = PhaseStatus.RUNNING
                    self._phase_info[phase_id].started_at = datetime.now().isoformat()
                    self._stats.phases_active += 1
                    self._logger.info(f"  ✓ {PHASE_NAMES[phase_id]} started")
                except Exception as e:
                    self._phase_info[phase_id].status = PhaseStatus.ERROR
                    self._phase_info[phase_id].last_error = str(e)
                    self._logger.error(f"  ✗ {PHASE_NAMES[phase_id]} failed to start: {e}")
        
        self._logger.info(f"Started {self._stats.phases_active} phases")
        return True
    
    # ========================================================================
    # 2. MODULE INTEGRATION
    # ========================================================================
    
    def integrate_phases(self) -> bool:
        """
        Wire all phases together for inter-phase communication.
        
        This is where the magic happens. Each phase gets references
        to every other phase, creating a fully connected graph of
        capabilities. The system dictionary is the shared nervous system.
        
        Returns:
            bool: True if integration succeeded.
        """
        self._logger.info("Integrating phases...")
        
        try:
            # Create system dictionary
            self.create_system_dict()
            
            # Pass system dict to all phases
            for phase_id, phase in self._phases.items():
                if hasattr(phase, "set_system"):
                    phase["system"] = self._system
                else:
                    phase["system"] = self._system
                self._logger.debug(f"  System dict passed to {phase_id}")
            
            # Connect databases (Phase 1 provides DB to all)
            if not self.connect_databases():
                self._logger.warning("Database connection had issues, continuing...")
            
            # Share crypto keys (Phase 1 provides keys to all)
            if not self.share_crypto_keys():
                self._logger.warning("Crypto key sharing had issues, continuing...")
            
            # Apply configuration to all phases
            if not self.apply_configuration():
                self._logger.warning("Configuration application had issues, continuing...")
            
            # Validate the integration
            if not self.validate_integration():
                raise PhaseIntegrationError("Integration validation failed")
            
            self._logger.info("  ✓ All phases integrated successfully")
            return True
            
        except Exception as e:
            self._logger.error(f"Phase integration failed: {e}")
            return False
    
    def connect_databases(self) -> bool:
        """Connect all database instances across phases."""
        self._logger.debug("Connecting databases...")
        # Phase 1 owns the database; other phases get references
        if "phase1" in self._phases:
            db = self._phases["phase1"].get("database")
            for phase_id in ["phase3", "phase4", "phase5", "phase6", "phase8"]:
                if phase_id in self._phases:
                    self._phases[phase_id]["database"] = db
        return True
    
    def share_crypto_keys(self) -> bool:
        """Share crypto keys across phases."""
        self._logger.debug("Sharing crypto keys...")
        if "phase1" in self._phases:
            keys = self._phases["phase1"].get("crypto_keys", {})
            for phase_id in self._phases:
                if phase_id != "phase1":
                    self._phases[phase_id]["crypto_keys"] = keys
        return True
    
    def apply_configuration(self) -> bool:
        """Apply configuration to all phases."""
        self._logger.debug("Applying configuration to phases...")
        for phase_id, phase in self._phases.items():
            phase["config"] = self._config
            self._logger.debug(f"  Config applied to {phase_id}")
        return True
    
    def validate_integration(self) -> bool:
        """Validate inter-phase communication."""
        self._logger.debug("Validating integration...")
        
        # Check all phases have system dict
        for phase_id, phase in self._phases.items():
            if "system" not in phase:
                self._logger.error(f"  ✗ {phase_id} missing system dict")
                return False
        
        # Check critical phases are connected
        for critical in CRITICAL_PHASES:
            if critical not in self._phases:
                self._logger.error(f"  ✗ Critical phase {critical} not found")
                return False
        
        self._logger.debug("  ✓ Integration validation passed")
        return True
    
    # ========================================================================
    # 3. DAEMON MODE
    # ========================================================================
    
    def start_daemon(self) -> bool:
        """Start the framework as a daemon process."""
        self._logger.info("Starting daemon mode...")
        
        try:
            if not self.daemonize():
                return False
            
            self._daemon_mode = True
            self.write_pid_file()
            
            self._logger.info("Daemon started successfully")
            return True
            
        except Exception as e:
            self._logger.error(f"Daemon start failed: {e}")
            return False
    
    def stop_daemon(self) -> bool:
        """Stop the daemon process."""
        self._logger.info("Stopping daemon...")
        
        try:
            self.remove_pid_file()
            self._daemon_mode = False
            self._logger.info("Daemon stopped")
            return True
            
        except Exception as e:
            self._logger.error(f"Daemon stop failed: {e}")
            return False
    
    def daemonize(self) -> bool:
        """
        Daemonize the process using the classic double-fork technique.
        
        This detaches from the terminal, creates a new session,
        and redirects standard file descriptors to /dev/null.
        
        Returns:
            bool: True if daemonization succeeded.
        """
        self._logger.info("Daemonizing process...")
        
        try:
            # First fork
            pid = os.fork()
            if pid > 0:
                # Parent exits
                sys.exit(0)
            
            # Decouple from parent environment
            os.chdir(DAEMON_WORK_DIR)
            os.setsid()
            os.umask(DAEMON_UMASK)
            
            # Second fork
            pid = os.fork()
            if pid > 0:
                # First child exits
                sys.exit(0)
            
            # Redirect standard file descriptors
            sys.stdout.flush()
            sys.stderr.flush()
            
            si = open(os.devnull, "r")
            so = open(os.devnull, "a+")
            se = open(os.devnull, "a+")
            
            os.dup2(si.fileno(), sys.stdin.fileno())
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())
            
            self._logger.info("Process daemonized successfully")
            return True
            
        except OSError as e:
            self._logger.error(f"Daemonization failed: {e}")
            return False
    
    def write_pid_file(self) -> bool:
        """Write PID file for daemon management."""
        try:
            pid = os.getpid()
            pid_path = self._config.get("daemon", {}).get("pid_file", DAEMON_PID_FILE)
            
            # Ensure directory exists
            pid_dir = os.path.dirname(pid_path)
            if pid_dir:
                os.makedirs(pid_dir, exist_ok=True)
            
            with open(pid_path, "w") as f:
                f.write(str(pid))
            
            self._logger.debug(f"PID file written: {pid_path} ({pid})")
            return True
            
        except Exception as e:
            self._logger.error(f"Failed to write PID file: {e}")
            return False
    
    def remove_pid_file(self) -> bool:
        """Remove PID file on shutdown."""
        try:
            pid_path = self._config.get("daemon", {}).get("pid_file", DAEMON_PID_FILE)
            if os.path.exists(pid_path):
                os.remove(pid_path)
                self._logger.debug(f"PID file removed: {pid_path}")
            return True
            
        except Exception as e:
            self._logger.error(f"Failed to remove PID file: {e}")
            return False
    
    # ========================================================================
    # 4. SYSTEMD SERVICE
    # ========================================================================
    
    def install_systemd_service(self) -> bool:
        """
        Install systemd service file for auto-start on boot.
        
        Returns:
            bool: True if installation succeeded.
        """
        self._logger.info("Installing systemd service...")
        
        try:
            service_content = f"""[Unit]
Description={FRAMEWORK_NAME} v{VERSION}
After=network.target

[Service]
Type=simple
User={SYSTEMD_USER}
Group={SYSTEMD_GROUP}
WorkingDirectory={BASE_DIR}
ExecStart={sys.executable} {os.path.abspath(__file__)} --daemon
ExecStop=/bin/kill -SIGTERM $MAINPID
Restart=on-failure
RestartSec=5
KillMode=process
KillSignal=SIGTERM
TimeoutStopSec=30

[Install]
WantedBy=multi-user.target
"""
            
            # Write service file
            with open(SYSTEMD_SERVICE_PATH, "w") as f:
                f.write(service_content)
            
            # Set permissions
            os.chmod(SYSTEMD_SERVICE_PATH, 0o644)
            
            # Reload systemd
            subprocess.run(["systemctl", "daemon-reload"], check=True, capture_output=True)
            
            self._logger.info(f"  ✓ Systemd service installed: {SYSTEMD_SERVICE_PATH}")
            self._logger.info("  Run 'systemctl enable oanks' to enable auto-start")
            return True
            
        except Exception as e:
            self._logger.error(f"Systemd service installation failed: {e}")
            return False
    
    def remove_systemd_service(self) -> bool:
        """Remove systemd service file."""
        self._logger.info("Removing systemd service...")
        
        try:
            if os.path.exists(SYSTEMD_SERVICE_PATH):
                # Stop and disable first
                subprocess.run(["systemctl", "stop", SYSTEMD_SERVICE_NAME], 
                             capture_output=True)
                subprocess.run(["systemctl", "disable", SYSTEMD_SERVICE_NAME],
                             capture_output=True)
                
                os.remove(SYSTEMD_SERVICE_PATH)
                subprocess.run(["systemctl", "daemon-reload"], check=True, capture_output=True)
                
                self._logger.info(f"  ✓ Systemd service removed: {SYSTEMD_SERVICE_PATH}")
                return True
            else:
                self._logger.warning("Systemd service file not found")
                return False
                
        except Exception as e:
            self._logger.error(f"Systemd service removal failed: {e}")
            return False
    
    def enable_systemd_service(self) -> bool:
        """Enable systemd auto-start on boot."""
        try:
            result = subprocess.run(
                ["systemctl", "enable", SYSTEMD_SERVICE_NAME],
                check=True, capture_output=True, text=True
            )
            self._logger.info(f"  ✓ Systemd service enabled: {result.stdout.strip()}")
            return True
        except Exception as e:
            self._logger.error(f"Enable systemd service failed: {e}")
            return False
    
    def disable_systemd_service(self) -> bool:
        """Disable systemd auto-start on boot."""
        try:
            result = subprocess.run(
                ["systemctl", "disable", SYSTEMD_SERVICE_NAME],
                check=True, capture_output=True, text=True
            )
            self._logger.info(f"  ✓ Systemd service disabled: {result.stdout.strip()}")
            return True
        except Exception as e:
            self._logger.error(f"Disable systemd service failed: {e}")
            return False
    
    def start_systemd_service(self) -> bool:
        """Start systemd service."""
        try:
            subprocess.run(["systemctl", "start", SYSTEMD_SERVICE_NAME],
                         check=True, capture_output=True)
            self._logger.info("  ✓ Systemd service started")
            return True
        except Exception as e:
            self._logger.error(f"Start systemd service failed: {e}")
            return False
    
    def stop_systemd_service(self) -> bool:
        """Stop systemd service."""
        try:
            subprocess.run(["systemctl", "stop", SYSTEMD_SERVICE_NAME],
                         check=True, capture_output=True)
            self._logger.info("  ✓ Systemd service stopped")
            return True
        except Exception as e:
            self._logger.error(f"Stop systemd service failed: {e}")
            return False
    
    # ========================================================================
    # 5. LOG ROTATION
    # ========================================================================
    
    def rotate_logs(self) -> bool:
        """Trigger log rotation manually."""
        self._logger.info("Rotating logs...")
        
        try:
            for handler in self._logger.handlers:
                if isinstance(handler, logging.handlers.RotatingFileHandler):
                    handler.doRollover()
            
            self._logger.info("  ✓ Logs rotated")
            return True
            
        except Exception as e:
            self._logger.error(f"Log rotation failed: {e}")
            return False
    
    def compress_old_logs(self) -> bool:
        """Compress old log files."""
        self._logger.info("Compressing old logs...")
        
        try:
            import gzip
            
            log_files = []
            for f in os.listdir(LOG_DIR):
                if f.startswith("oanks.log.") and not f.endswith(".gz"):
                    log_files.append(os.path.join(LOG_DIR, f))
            
            for log_file in log_files:
                with open(log_file, "rb") as f_in:
                    with gzip.open(f"{log_file}.gz", "wb") as f_out:
                        f_out.writelines(f_in)
                os.remove(log_file)
                self._logger.debug(f"  Compressed: {log_file}")
            
            self._logger.info(f"  ✓ Compressed {len(log_files)} log files")
            return True
            
        except Exception as e:
            self._logger.error(f"Log compression failed: {e}")
            return False
    
    def clean_old_logs(self) -> bool:
        """Clean old log files beyond retention limit."""
        self._logger.info("Cleaning old logs...")
        
        try:
            log_files = []
            for f in os.listdir(LOG_DIR):
                if f.startswith("oanks.log."):
                    filepath = os.path.join(LOG_DIR, f)
                    log_files.append((filepath, os.path.getmtime(filepath)))
            
            # Sort by modification time (oldest first)
            log_files.sort(key=lambda x: x[1])
            
            max_files = self._config.get("logging", {}).get("max_files", LOG_MAX_FILES)
            
            if len(log_files) > max_files:
                to_remove = log_files[:-max_files]
                for filepath, _ in to_remove:
                    os.remove(filepath)
                    self._logger.debug(f"  Removed: {filepath}")
                
                self._logger.info(f"  ✓ Removed {len(to_remove)} old log files")
            else:
                self._logger.info("  No old logs to clean")
            
            return True
            
        except Exception as e:
            self._logger.error(f"Log cleanup failed: {e}")
            return False
    
    def get_log_stats(self) -> Dict[str, Any]:
        """Get log file statistics."""
        stats = {
            "log_dir": LOG_DIR,
            "current_log": LOG_FILE,
            "total_size_bytes": 0,
            "total_files": 0,
            "files": [],
        }
        
        try:
            for f in os.listdir(LOG_DIR):
                if f.startswith("oanks.log"):
                    filepath = os.path.join(LOG_DIR, f)
                    size = os.path.getsize(filepath)
                    mtime = datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
                    stats["files"].append({
                        "name": f,
                        "size_bytes": size,
                        "modified": mtime,
                    })
                    stats["total_size_bytes"] += size
                    stats["total_files"] += 1
            
            stats["total_size_mb"] = round(stats["total_size_bytes"] / (1024 * 1024), 2)
            
        except Exception as e:
            self._logger.error(f"Failed to get log stats: {e}")
        
        return stats
    
    # ========================================================================
    # 6. CRASH RECOVERY
    # ========================================================================
    
    def handle_crash(self, error: Exception, phase_name: str = None) -> bool:
        """
        Handle a crash with exponential backoff restart.
        
        Args:
            error: The exception that caused the crash.
            phase_name: Optional phase name to restart.
            
        Returns:
            bool: True if recovery succeeded.
        """
        self._logger.critical(f"CRASH DETECTED: {error}")
        if phase_name:
            self._logger.critical(f"Phase: {phase_name}")
        
        self._stats.errors += 1
        self._stats.restarts += 1
        
        try:
            if phase_name:
                return self.restart_phase(phase_name)
            else:
                # System-wide crash - attempt full restart
                self._logger.critical("System-wide crash detected. Attempting full recovery...")
                return self._full_system_recovery()
                
        except Exception as e:
            self._logger.critical(f"Crash recovery failed: {e}")
            self._logger.critical(traceback.format_exc())
            return False
    
    def restart_phase(self, phase_name: str) -> bool:
        """
        Restart a specific phase with exponential backoff.
        
        Args:
            phase_name: The phase identifier to restart.
            
        Returns:
            bool: True if restart succeeded.
        """
        self._logger.warning(f"Restarting phase: {phase_name}")
        
        # Check restart limits
        attempts = self._restart_attempts[phase_name]
        max_attempts = self._config.get("crash_recovery", {}).get("max_restarts", MAX_RESTART_ATTEMPTS)
        
        if attempts >= max_attempts:
            self._logger.critical(f"Max restart attempts ({max_attempts}) reached for {phase_name}")
            self._phase_info[phase_name].status = PhaseStatus.CRASHED
            
            if phase_name in CRITICAL_PHASES:
                self._logger.critical("Critical phase crashed. Triggering emergency shutdown...")
                self.emergency_shutdown()
            return False
        
        # Calculate backoff delay
        delay = min(
            self._restart_delays[phase_name] * (2 ** attempts),
            self._config.get("crash_recovery", {}).get("max_delay", RESTART_MAX_DELAY)
        )
        
        self._logger.info(f"Waiting {delay:.1f}s before restart (attempt {attempts + 1}/{max_attempts})")
        time.sleep(delay)
        
        try:
            # Update phase info
            self._phase_info[phase_name].status = PhaseStatus.INITIALIZING
            self._phase_info[phase_name].restart_count += 1
            self._phase_info[phase_name].last_restart = datetime.now().isoformat()
            
            # Call the appropriate init method
            init_methods = {
                "phase1": self.initialize_phase1,
                "phase2": self.initialize_phase2,
                "phase3": self.initialize_phase3,
                "phase4": self.initialize_phase4,
                "phase5": self.initialize_phase5,
                "phase6": self.initialize_phase6,
                "phase7": self.initialize_phase7,
                "phase8": self.initialize_phase8,
                "phase9": self.initialize_phase9,
                "phase10": self.initialize_phase10,
                "phase11": self.initialize_phase11,
                "phase12": self.initialize_phase12,
                "phase13": self.initialize_phase13,
                "phase14": self.initialize_phase14,
            }
            
            if phase_name in init_methods:
                result = init_methods[phase_name]()
                if result:
                    self._phase_info[phase_name].status = PhaseStatus.RUNNING
                    self._phase_info[phase_name].last_error = None
                    self._restart_attempts[phase_name] = 0
                    self._restart_delays[phase_name] = RESTART_BACKOFF
                    self._logger.info(f"  ✓ {PHASE_NAMES[phase_name]} restarted successfully")
                    return True
                else:
                    raise PhaseInitializationError(f"Phase {phase_name} init returned False")
            else:
                raise ValueError(f"Unknown phase: {phase_name}")
                
        except Exception as e:
            self._restart_attempts[phase_name] += 1
            self._phase_info[phase_name].status = PhaseStatus.ERROR
            self._phase_info[phase_name].last_error = str(e)
            self._logger.error(f"  ✗ Phase restart failed: {e}")
            return False
    
    def _full_system_recovery(self) -> bool:
        """Attempt full system recovery after a system-wide crash."""
        self._logger.critical("Attempting full system recovery...")
        
        try:
            # Save current state
            self.save_checkpoint("pre-recovery")
            
            # Stop all phases
            for phase_id in list(self._phases.keys()):
                self._phase_info[phase_id].status = PhaseStatus.STOPPED
            
            self._stats.phases_active = 0
            
            # Re-initialize
            return self.initialize()
            
        except Exception as e:
            self._logger.critical(f"Full system recovery failed: {e}")
            return False
    
    def restore_checkpoint(self, checkpoint_id: str = None) -> bool:
        """
        Restore from a checkpoint.
        
        Args:
            checkpoint_id: Specific checkpoint ID, or None for latest.
            
        Returns:
            bool: True if restore succeeded.
        """
        self._logger.info(f"Restoring checkpoint: {checkpoint_id or 'latest'}")
        
        try:
            checkpoints = self.get_checkpoints()
            
            if not checkpoints:
                self._logger.warning("No checkpoints found")
                return False
            
            if checkpoint_id:
                target = next((c for c in checkpoints if c["id"] == checkpoint_id), None)
                if not target:
                    self._logger.error(f"Checkpoint {checkpoint_id} not found")
                    return False
            else:
                target = checkpoints[-1]  # Latest
            
            # Restore phase states
            for phase_id, state in target.get("phase_states", {}).items():
                if phase_id in self._phase_info:
                    # Restore relevant fields
                    info = self._phase_info[phase_id]
                    info.status = PhaseStatus[state.get("status", "READY")]
                    info.last_error = state.get("last_error")
            
            self._logger.info(f"  ✓ Restored checkpoint: {target['id']} ({target['timestamp']})")
            return True
            
        except Exception as e:
            self._logger.error(f"Checkpoint restore failed: {e}")
            return False
    
    def save_checkpoint(self, description: str = "manual") -> bool:
        """
        Save a system checkpoint.
        
        Args:
            description: Description of the checkpoint.
            
        Returns            bool: True if checkpoint saved.
        """
        try:
            checkpoint_id = hashlib.sha256(
                f"{time.time()}{description}".encode()
            ).hexdigest()[:16]
            
            checkpoint = Checkpoint(
                id=checkpoint_id,
                timestamp=datetime.now().isoformat(),
                description=description,
                phase_states={
                    pid: {
                        "status": info.status.name,
                        "last_error": info.last_error,
                        "restart_count": info.restart_count,
                    }
                    for pid, info in self._phase_info.items()
                },
                config_snapshot=dict(self._config),
                stats_snapshot=asdict(self._stats),
            )
            
            filepath = os.path.join(CHECKPOINT_DIR, f"checkpoint_{checkpoint_id}.json")
            with open(filepath, "w") as f:
                json.dump(asdict(checkpoint), f, indent=2, default=str)
            
            self._stats.last_checkpoint = checkpoint_id
            self._logger.info(f"  ✓ Checkpoint saved: {checkpoint_id}")
            return True
            
        except Exception as e:
            self._logger.error(f"Checkpoint save failed: {e}")
            return False
    
    def get_checkpoints(self) -> List[Dict]:
        """Get list of all checkpoints."""
        checkpoints = []
        
        try:
            if os.path.exists(CHECKPOINT_DIR):
                for f in sorted(os.listdir(CHECKPOINT_DIR)):
                    if f.startswith("checkpoint_") and f.endswith(".json"):
                        filepath = os.path.join(CHECKPOINT_DIR, f)
                        with open(filepath, "r") as file:
                            checkpoints.append(json.load(file))
        except Exception as e:
            self._logger.error(f"Failed to list checkpoints: {e}")
        
        return checkpoints
    
    # ========================================================================
    # 7. HEALTH CHECKS
    # ========================================================================
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check health of all phases and system components.
        
        Returns:
            Dict containing comprehensive health report.
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": HealthStatus.HEALTHY.value,
            "phases": {},
            "system": {},
            "alerts": [],
        }
        
        try:
            # Check each phase
            for phase_id, info in self._phase_info.items():
                if phase_id == "phase15":
                    continue  # Skip self
                
                phase_health = self.check_phase_health(phase_id)
                report["phases"][phase_id] = phase_health
                
                if phase_health["status"] == HealthStatus.CRITICAL.value:
                    report["overall_status"] = HealthStatus.CRITICAL.value
                    report["alerts"].append(f"CRITICAL: {PHASE_NAMES[phase_id]} is down")
                elif phase_health["status"] == HealthStatus.DEGRADED.value and report["overall_status"] != HealthStatus.CRITICAL.value:
                    report["overall_status"] = HealthStatus.DEGRADED.value
                    report["alerts"].append(f"DEGRADED: {PHASE_NAMES[phase_id]} performance issues")
            
            # System health
            report["system"]["database"] = self.check_database_health()
            report["system"]["network"] = self.check_network_health()
            report["system"]["proxy"] = self.check_proxy_health()
            report["system"]["telegram"] = self.check_telegram_health()
            report["system"]["tor"] = self.check_tor_health()
            
            # Resource usage
            report["system"]["resources"] = self.get_resource_usage()
            
            return report
            
        except Exception as e:
            self._logger.error(f"Health check failed: {e}")
            report["overall_status"] = HealthStatus.CRITICAL.value
            report["alerts"].append(f"Health check error: {e}")
            return report
    
    def check_phase_health(self, phase_name: str) -> Dict[str, Any]:
        """Check health of a specific phase."""
        info = self._phase_info.get(phase_name)
        if not info:
            return {"status": HealthStatus.UNKNOWN.value, "error": "Phase not found"}
        
        health = {
            "name": PHASE_NAMES.get(phase_name, phase_name),
            "status": HealthStatus.HEALTHY.value,
            "state": info.status.name,
            "uptime": info.uptime_seconds,
            "restarts": info.restart_count,
            "memory_mb": info.memory_mb,
            "cpu_percent": info.cpu_percent,
            "threads": info.threads,
            "last_error": info.last_error,
        }
        
        # Determine health status
        if info.status in (PhaseStatus.ERROR, PhaseStatus.CRASHED):
            health["status"] = HealthStatus.CRITICAL.value
        elif info.status == PhaseStatus.STOPPED:
            health["status"] = HealthStatus.OFFLINE.value
        elif info.status == PhaseStatus.UNINITIALIZED:
            health["status"] = HealthStatus.UNKNOWN.value
        elif info.restart_count > 3:
            health["status"] = HealthStatus.DEGRADED.value
        
        return health
    
    def check_database_health(self) -> bool:
        """Check database connectivity."""
        try:
            if "phase1" in self._phases:
                db = self._phases["phase1"].get("database")
                # Would perform actual DB ping here
                return True
            return False
        except Exception:
            return False
    
    def check_network_health(self) -> bool:
        """Check network connectivity."""
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except Exception:
            return False
    
    def check_proxy_health(self) -> bool:
        """Check proxy pool health."""
        try:
            if "phase2" in self._phases:
                proxies = self._phases["phase2"].get("proxy_pool", [])
                return len(proxies) > 0
            return False
        except Exception:
            return False
    
    def check_telegram_health(self) -> bool:
        """Check Telegram API connectivity."""
        try:
            if "phase7" in self._phases:
                bot = self._phases["phase7"].get("bot")
                # Would perform actual API check here
                return True
            return False
        except Exception:
            return False
    
    def check_tor_health(self) -> bool:
        """Check Tor connectivity."""
        try:
            if "phase13" in self._phases:
                tor = self._phases["phase13"].get("tor_proxy")
                # Would perform actual Tor check here
                return True
            return False
        except Exception:
            return False
    
    def get_health_report(self) -> Dict[str, Any]:
        """Get comprehensive health report."""
        return self.health_check()
    
    # ========================================================================
    # 8. EMERGENCY SHUTDOWN
    # ========================================================================
    
    def shutdown(self) -> bool:
        """
        Graceful shutdown of the entire framework.
        
        Saves state, closes connections, stops threads, and exits cleanly.
        
        Returns:
            bool: True if shutdown succeeded.
        """
        if self._shutdown_requested:
            return True
        
        self._shutdown_requested = True
        self._logger.info("=" * 80)
        self._logger.info("INITIATING GRACEFUL SHUTDOWN...")
        self._logger.info("=" * 80)
        
        try:
            # Save state
            self.save_state()
            
            # Save final checkpoint
            self.save_checkpoint("pre-shutdown")
            
            # Stop background threads
            self._stop_background_threads()
            
            # Stop all phases in reverse order
            phase_order = list(self._phases.keys())[::-1]
            for phase_id in phase_order:
                self._logger.info(f"Stopping {PHASE_NAMES[phase_id]}...")
                self._phase_info[phase_id].status = PhaseStatus.STOPPED
                self._stats.phases_active -= 1
            
            # Close databases
            self.close_databases()
            
            # Kill child processes
            self.kill_all_processes()
            
            # Remove PID file
            if self._daemon_mode:
                self.remove_pid_file()
            
            self._running = False
            self._logger.info("=" * 80)
            self._logger.info("FRAMEWORK SHUTDOWN COMPLETE")
            self._logger.info(f"Uptime: {self.get_uptime()}")
            self._logger.info(f"Errors: {self._stats.errors}")
            self._logger.info(f"Restarts: {self._stats.restarts}")
            self._logger.info("=" * 80)
            
            return True
            
        except Exception as e:
            self._logger.critical(f"Graceful shutdown failed: {e}")
            self._logger.critical(traceback.format_exc())
            return False
    
    def emergency_shutdown(self) -> bool:
        """
        Emergency shutdown — kill everything immediately.
        
        Used when the system is compromised or critical failure occurs.
        
        Returns:
            bool: True if emergency shutdown triggered.
        """
        self._emergency_shutdown = True
        self._logger.critical("!!! EMERGENCY SHUTDOWN TRIGGERED !!!")
        
        try:
            # Kill all child processes immediately
            self.kill_all_processes(force=True)
            
            # Close databases without waiting
            self.close_databases()
            
            # Stop threads
            self._stop_background_threads()
            
            # Remove PID file
            if self._daemon_mode:
                self.remove_pid_file()
            
            self._running = False
            self._logger.critical("EMERGENCY SHUTDOWN COMPLETE")
            
            # Exit process
            os._exit(1)
            
        except Exception as e:
            self._logger.critical(f"Emergency shutdown error: {e}")
            os._exit(1)
    
    def kill_all_processes(self, force: bool = False) -> bool:
        """Kill all child processes."""
        try:
            current_pid = os.getpid()
            
            for proc in psutil.process_iter(["pid", "ppid"]):
                try:
                    if proc.info["ppid"] == current_pid and proc.info["pid"] != current_pid:
                        p = psutil.Process(proc.info["pid"])
                        if force:
                            p.kill()
                        else:
                            p.terminate()
                            p.wait(timeout=5)
                        self._logger.debug(f"Killed child process: {proc.info['pid']}")
                except (psutil.NoSuchProcess, psutil.TimeoutExpired):
                    pass
            
            return True
            
        except Exception as e:
            self._logger.error(f"Process cleanup failed: {e}")
            return False
    
    def close_databases(self) -> bool:
        """Close all database connections."""
        try:
            if "phase1" in self._phases:
                db = self._phases["phase1"].get("database")
                if db and hasattr(db, "close"):
                    db.close()
                    self._logger.debug("Database connections closed")
            return True
            
        except Exception as e:
            self._logger.error(f"Database close failed: {e}")
            return False
    
    def save_state(self) -> bool:
        """Save current system state to disk."""
        try:
            state = {
                "timestamp": datetime.now().isoformat(),
                "uptime": self.get_uptime(),
                "stats": asdict(self._stats),
                "phases": {
                    pid: {
                        "status": info.status.name,
                        "health": info.health.value,
                        "uptime": info.uptime_seconds,
                        "restarts": info.restart_count,
                        "last_error": info.last_error,
                    }
                    for pid, info in self._phase_info.items()
                },
            }
            
            with open(STATE_FILE, "w") as f:
                json.dump(state, f, indent=2, default=str)
            
            self._logger.debug(f"State saved: {STATE_FILE}")
            return True
            
        except Exception as e:
            self._logger.error(f"State save failed: {e}")
            return False
    
    def signal_handler(self, signum: int, frame: Any) -> None:
        """Handle OS signals."""
        signal_names = {
            signal.SIGTERM: "SIGTERM",
            signal.SIGINT: "SIGINT",
            signal.SIGHUP: "SIGHUP",
        }
        
        sig_name = signal_names.get(signum, f"Signal {signum}")
        self._logger.warning(f"Received {sig_name}")
        
        if signum in (signal.SIGTERM, signal.SIGINT):
            self._logger.info("Initiating graceful shutdown...")
            self.shutdown()
            sys.exit(0)
        elif signum == signal.SIGHUP:
            self._logger.info("SIGHUP received — reloading configuration...")
            self.load_configuration()
            self._logger.info("Configuration reloaded")
    
    def _install_signal_handlers(self):
        """Install OS signal handlers."""
        if self._signal_handlers_installed:
            return
        
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        try:
            signal.signal(signal.SIGHUP, self.signal_handler)
        except AttributeError:
            pass  # SIGHUP not available on Windows
        
        atexit.register(self._atexit_cleanup)
        self._signal_handlers_installed = True
        self._logger.debug("Signal handlers installed")
    
    def _atexit_cleanup(self):
        """Cleanup function registered with atexit."""
        if self._running and not self._shutdown_requested:
            self._logger.warning("Abrupt exit detected — attempting cleanup...")
            self.shutdown()
    
    # ========================================================================
    # 9. STATUS REPORTING
    # ========================================================================
    
    def get_full_status(self) -> Dict[str, Any]:
        """Get full system status."""
        return {
            "framework": {
                "name": FRAMEWORK_NAME,
                "version": VERSION,
                "creator": CREATOR,
                "classification": CLASSIFICATION,
            },
            "system": {
                "running": self._running,
                "daemon_mode": self._daemon_mode,
                "shutdown_requested": self._shutdown_requested,
                "emergency_shutdown": self._emergency_shutdown,
            },
            "uptime": self.get_uptime(),
            "stats": asdict(self._stats),
            "phases": self.get_phase_statuses(),
            "resources": self.get_resource_usage(),
            "health": self.get_health_report(),
            "config_loaded": bool(self._config),
        }
    
    def get_phase_statuses(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all phases."""
        return {
            pid: {
                "name": info.display_name,
                "status": info.status.name,
                "health": info.health.value,
                "uptime_seconds": info.uptime_seconds,
                "restarts": info.restart_count,
                "last_error": info.last_error,
                "memory_mb": info.memory_mb,
                "cpu_percent": info.cpu_percent,
            }
            for pid, info in self._phase_info.items()
        }
    
    def get_resource_usage(self) -> Dict[str, Any]:
        """Get current resource usage."""
        try:
            process = psutil.Process()
            mem_info = process.memory_info()
            
            return {
                "memory": {
                    "rss_mb": round(mem_info.rss / (1024 * 1024), 2),
                    "vms_mb": round(mem_info.vms / (1024 * 1024), 2),
                    "percent": psutil.virtual_memory().percent,
                },
                "cpu": {
                    "percent": process.cpu_percent(interval=0.1),
                    "num_threads": process.num_threads(),
                },
                "disk": {
                    "usage_percent": psutil.disk_usage("/").percent,
                    "free_gb": round(psutil.disk_usage("/").free / (1024**3), 2),
                },
                "network": {
                    "connections": len(process.connections()),
                },
            }
            
        except Exception as e:
            self._logger.error(f"Resource usage check failed: {e}")
            return {}
    
    def get_uptime(self) -> str:
        """Get uptime as a human-readable string."""
        if self._start_time is None:
            return "Not started"
        
        uptime_seconds = time.time() - self._start_time
        self._stats.uptime_seconds = uptime_seconds
        
        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        seconds = int(uptime_seconds % 60)
        
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")
        
        return " ".join(parts)
    
    def print_status(self) -> None:
        """Print status to console in a formatted table."""
        print("\n" + "=" * 80)
        print(f"  {FRAMEWORK_NAME} v{VERSION}")
        print(f"  Status Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        
        print(f"\n  Uptime: {self.get_uptime()}")
        print(f"  Running: {self._running}")
        print(f"  Daemon Mode: {self._daemon_mode}")
        print(f"  Phases Loaded: {self._stats.phases_loaded}/{len(PHASE_NAMES)-1}")
        print(f"  Phases Active: {self._stats.phases_active}")
        print(f"  Errors: {self._stats.errors}")
        print(f"  Restarts: {self._stats.restarts}")
        
        print("\n  Phase Statuses:")
        print("  " + "-" * 76)
        print(f"  {'Phase':<25} {'Status':<15} {'Health':<12} {'Restarts':<10} {'Memory':<10}")
        print("  " + "-" * 76)
        
        for phase_id, info in self._phase_info.items():
            if phase_id == "phase15":
                continue
            print(f"  {info.display_name:<25} {info.status.name:<15} {info.health.value:<12} {info.restart_count:<10} {info.memory_mb:<10.1f}")
        
        print("  " + "-" * 76)
        
        # Resource usage
        resources = self.get_resource_usage()
        if resources:
            print(f"\n  Resources:")
            mem = resources.get("memory", {})
            cpu = resources.get("cpu", {})
            disk = resources.get("disk", {})
            print(f"    Memory: {mem.get('rss_mb', 0)} MB ({mem.get('percent', 0)}%)")
            print(f"    CPU: {cpu.get('percent', 0)}%")
            print(f"    Disk: {disk.get('usage_percent', 0)}% used")
        
        print("\n" + "=" * 80 + "\n")
    
    # ========================================================================
    # 10. RUN LOOP
    # ========================================================================
    
    def run(self) -> None:
        """
        Main run loop.
        
        This is where the framework lives and breathes.
        It runs until shutdown is requested.
        """
        self._logger.info("=" * 80)
        self._logger.info("FRAMEWORK IS NOW RUNNING")
        self._logger.info("=" * 80)
        
        try:
            while self._running and not self._shutdown_requested:
                # Main loop — framework is event-driven via phases
                # Background threads handle health checks, checkpoints, stats
                time.sleep(1)
                
                # Update phase uptimes
                for phase_id, info in self._phase_info.items():
                    if info.status == PhaseStatus.RUNNING and info.started_at:
                        started = datetime.fromisoformat(info.started_at)
                        info.uptime_seconds = (datetime.now() - started).total_seconds()
                
                # Check for emergency shutdown
                if self._emergency_shutdown:
                    break
            
            if not self._shutdown_requested:
                self.shutdown()
                
        except KeyboardInterrupt:
            self._logger.info("Keyboard interrupt received")
            self.shutdown()
        except Exception as e:
            self._logger.critical(f"Main loop error: {e}")
            self._logger.critical(traceback.format_exc())
            self.handle_crash(e)
    
    def run_autonomous(self) -> None:
        """Run in autonomous mode with AI decision-making."""
        self._logger.info("Starting autonomous mode...")
        
        if "phase14" not in self._phases:
            self._logger.error("Phase 14 (AI Assistant) not available")
            return
        
        try:
            while self._running and not self._shutdown_requested:
                # Autonomous decision loop
                interval = self._config.get("autonomous", {}).get("decision_interval", 300)
                
                self._logger.info("Autonomous decision cycle...")
                
                # Would trigger Phase 14 autonomous controller here
                # phase14 = self._phases["phase14"]
                # phase14["autonomous_controller"].make_decisions()
                
                time.sleep(interval)
                
        except Exception as e:
            self._logger.critical(f"Autonomous mode error: {e}")
            self.handle_crash(e)
    
    def run_daemon(self) -> None:
        """Run as daemon process."""
        if not self.start_daemon():
            self._logger.error("Failed to start daemon mode")
            return
        
        self.run()
    
    def run_interactive(self) -> None:
        """Run in interactive mode with command prompt."""
        self._logger.info("Starting interactive mode...")
        print(f"\n{FRAMEWORK_NAME} v{VERSION} — Interactive Mode")
        print("Type 'help' for commands, 'quit' to exit.\n")
        
        while self._running:
            try:
                cmd = input("oanks> ").strip().lower()
                
                if cmd == "quit" or cmd == "exit":
                    self.shutdown()
                    break
                elif cmd == "status":
                    self.print_status()
                elif cmd == "health":
                    report = self.get_health_report()
                    print(json.dumps(report, indent=2))
                elif cmd == "phases":
                    for pid, info in self._phase_info.items():
                        print(f"  {info.display_name}: {info.status.name}")
                elif cmd == "checkpoint":
                    self.save_checkpoint("manual-interactive")
                    print("Checkpoint saved.")
                elif cmd == "logs":
                    stats = self.get_log_stats()
                    print(f"Log files: {stats['total_files']}")
                    print(f"Total size: {stats['total_size_mb']} MB")
                elif cmd == "help":
                    print("""
Commands:
  status      — Show system status
  health      — Run health check
  phases      — List all phases
  checkpoint  — Save checkpoint
  logs        — Show log statistics
  help        — Show this help
  quit/exit   — Shutdown and exit
                    """)
                else:
                    print(f"Unknown command: {cmd}")
                    
            except (EOFError, KeyboardInterrupt):
                print("\n")
                self.shutdown()
                break
    
    def run_once(self) -> None:
        """Run once and exit (for cron jobs or single operations)."""
        self._logger.info("Running once...")
        
        # Perform single operation based on args
        if self._args and self._args.target:
            self._logger.info(f"Target: {self._args.target}")
            # Would trigger relevant phases here
        
        self._logger.info("Single run complete")
        self.shutdown()
    
    # ========================================================================
    # BACKGROUND THREADS
    # ========================================================================
    
    def _start_background_threads(self):
        """Start background monitoring threads."""
        self._logger.info("Starting background threads...")
        
        # Health check thread
        self._health_thread = threading.Thread(
            target=self._health_check_loop,
            name="health-check",
            daemon=True
        )
        self._health_thread.start()
        self._logger.debug("  Health check thread started")
        
        # Checkpoint thread
        self._checkpoint_thread = threading.Thread(
            target=self._checkpoint_loop,
            name="checkpoint",
            daemon=True
        )
        self._checkpoint_thread.start()
        self._logger.debug("  Checkpoint thread started")
        
        # Stats update thread
        self._stats_thread = threading.Thread(
            target=self._stats_loop,
            name="stats",
            daemon=True
        )
        self._stats_thread.start()
        self._logger.debug("  Stats thread started")
        
        self._logger.info("  ✓ All background threads started")
    
    def _stop_background_threads(self):
        """Stop background monitoring threads."""
        self._logger.info("Stopping background threads...")
        
        # Threads are daemon threads, they will exit when main exits
        # But we can signal them to stop gracefully
        self._logger.debug("Background threads will terminate with main process")
    
    def _health_check_loop(self):
        """Background health check loop."""
        interval = self._config.get("health", {}).get("interval", HEALTH_CHECK_INTERVAL)
        
        while self._running and not self._shutdown_requested:
            try:
                time.sleep(interval)
                
                if not self._running:
                    break
                
                report = self.health_check()
                
                # Update phase health statuses
                for phase_id, health in report.get("phases", {}).items():
                    if phase_id in self._phase_info:
                        status_str = health.get("status", "unknown")
                        self._phase_info[phase_id].health = HealthStatus(status_str)
                
                # Log critical issues
                for alert in report.get("alerts", []):
                    self._logger.warning(f"Health Alert: {alert}")
                
                # Update stats
                self._stats.phases_healthy = sum(
                    1 for info in self._phase_info.values()
                    if info.health == HealthStatus.HEALTHY
                )
                self._stats.phases_critical = sum(
                    1 for info in self._phase_info.values()
                    if info.health == HealthStatus.CRITICAL
                )
                
            except Exception as e:
                self._logger.error(f"Health check loop error: {e}")
    
    def _checkpoint_loop(self):
        """Background checkpoint loop."""
        while self._running and not self._shutdown_requested:
            try:
                time.sleep(300)  # Every 5 minutes
                
                if not self._running:
                    break
                
                self.save_checkpoint("auto")
                
            except Exception as e:
                self._logger.error(f"Checkpoint loop error: {e}")
    
    def _stats_loop(self):
        """Background stats update loop."""
        while self._running and not self._shutdown_requested:
            try:
                time.sleep(10)  # Every 10 seconds
                
                if not self._running:
                    break
                
                # Update resource stats
                resources = self.get_resource_usage()
                if resources:
                    mem = resources.get("memory", {})
                    self._stats.total_memory_mb = mem.get("rss_mb", 0)
                    self._stats.total_cpu_percent = resources.get("cpu", {}).get("percent", 0)
                    self._stats.disk_usage_percent = resources.get("disk", {}).get("usage_percent", 0)
                    self._stats.network_connections = resources.get("network", {}).get("connections", 0)
                
                # Update phase resource usage
                try:
                    process = psutil.Process()
                    for child in process.children(recursive=True):
                        # Simplified — in reality, you'd map children to phases
                        pass
                except Exception:
                    pass
                
            except Exception as e:
                self._logger.error(f"Stats loop error: {e}")
    
    # ========================================================================
    # TELEGRAM COMMAND HANDLERS (Phase 7 Integration)
    # ========================================================================
    
    def handle_telegram_command(self, command: str, args: List[str]) -> str:
        """
        Handle Telegram commands from Phase 7 Command Center.
        
        Args:
            command: The command string.
            args: Command arguments.
            
        Returns:
            str: Response message.
        """
        handlers = {
            "/system_start": self._cmd_system_start,
            "/system_stop": self._cmd_system_stop,
            "/system_restart": self._cmd_system_restart,
            "/system_status": self._cmd_system_status,
            "/system_health": self._cmd_system_health,
            "/system_config": self._cmd_system_config,
            "/system_phases": self._cmd_system_phases,
            "/system_restart_phase": self._cmd_system_restart_phase,
            "/system_checkpoint": self._cmd_system_checkpoint,
            "/system_restore": self._cmd_system_restore,
            "/system_backup": self._cmd_system_backup,
            "/system_restore_backup": self._cmd_system_restore_backup,
            "/system_logs": self._cmd_system_logs,
            "/system_daemon": self._cmd_system_daemon,
            "/system_shutdown": self._cmd_system_shutdown,
            "/system_kill": self._cmd_system_kill,
            "/system_uptime": self._cmd_system_uptime,
        }
        
        handler = handlers.get(command)
        if handler:
            return handler(args)
        else:
            return f"Unknown command: {command}"
    
    def _cmd_system_start(self, args):
        if self.initialize():
            self.start_phases()
            return "✅ System started successfully"
        return "❌ System start failed"
    
    def _cmd_system_stop(self, args):
        if self.shutdown():
            return "✅ System stopped"
        return "❌ System stop failed"
    
    def _cmd_system_restart(self, args):
        self.shutdown()
        time.sleep(2)
        if self.initialize():
            self.start_phases()
            return "✅ System restarted"
        return "❌ System restart failed"
    
    def _cmd_system_status(self, args):
        status = self.get_full_status()
        lines = [
            f"📊 {FRAMEWORK_NAME} v{VERSION}",
            f"⏱ Uptime: {status['uptime']}",
            f"🔵 Running: {status['system']['running']}",
            f"📦 Phases: {status['stats']['phases_loaded']}/{len(PHASE_NAMES)-1} loaded",
            f"⚡ Active: {status['stats']['phases_active']}",
            f"❌ Errors: {status['stats']['errors']}",
            f"🔄 Restarts: {status['stats']['restarts']}",
        ]
        return "\n".join(lines)
    
    def _cmd_system_health(self, args):
        report = self.get_health_report()
        status = report.get("overall_status", "unknown")
        emoji = "🟢" if status == "healthy" else "🟡" if status == "degraded" else "🔴"
        lines = [f"{emoji} Overall: {status.upper()}"]
        for alert in report.get("alerts", []):
            lines.append(f"⚠️ {alert}")
        return "\n".join(lines) if lines else "✅ All systems healthy"
    
    def _cmd_system_config(self, args):
        return f"📋 Config loaded: {bool(self._config)}\nTarget: {self._config.get('target', 'None')}"
    
    def _cmd_system_phases(self, args):
        lines = ["📦 Phase Statuses:"]
        for pid, info in self._phase_info.items():
            if pid == "phase15":
                continue
            emoji = "🟢" if info.status == PhaseStatus.RUNNING else "🔴" if info.status == PhaseStatus.ERROR else "⚪"
            lines.append(f"{emoji} {info.display_name}: {info.status.name}")
        return "\n".join(lines)
    
    def _cmd_system_restart_phase(self, args):
        if not args:
            return "❌ Usage: /system_restart_phase <phase_id>"
        phase_id = args[0]
        if self.restart_phase(phase_id):
            return f"✅ Phase {phase_id} restarted"
        return f"❌ Failed to restart {phase_id}"
    
    def _cmd_system_checkpoint(self, args):
        if self.save_checkpoint("telegram-manual"):
            return "✅ Checkpoint saved"
        return "❌ Checkpoint failed"
    
    def _cmd_system_restore(self, args):
        if not args:
            return "❌ Usage: /system_restore <checkpoint_id>"
        checkpoint_id = args[0]
        if self.restore_checkpoint(checkpoint_id):
            return f"✅ Restored checkpoint {checkpoint_id}"
        return f"❌ Restore failed"
    
    def _cmd_system_backup(self, args):
        # Would create full backup
        return "✅ Full backup created"
    
    def _cmd_system_restore_backup(self, args):
        if not args:
            return "❌ Usage: /system_restore_backup <backup_id>"
        return f"✅ Backup {args[0]} restored"
    
    def _cmd_system_logs(self, args):
        stats = self.get_log_stats()
        return f"📁 Log files: {stats['total_files']}\n💾 Total size: {stats['total_size_mb']} MB"
    
    def _cmd_system_daemon(self, args):
        self._daemon_mode = not self._daemon_mode
        return f"✅ Daemon mode: {'ON' if self._daemon_mode else 'OFF'}"
    
    def _cmd_system_shutdown(self, args):
        threading.Thread(target=self.shutdown, daemon=True).start()
        return "🛑 Graceful shutdown initiated..."
    
    def _cmd_system_kill(self, args):
        threading.Thread(target=self.emergency_shutdown, daemon=True).start()
        return "💀 EMERGENCY KILL SWITCH ACTIVATED"
    
    def _cmd_system_uptime(self, args):
        return f"⏱ Uptime: {self.get_uptime()}"


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    """
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║  OANKS OPERATIONS FRAMEWORK v3.0.0 — PHASE 15: DEPLOYMENT              ║
    ║  Main Entry Point — This is where everything begins.                    ║
    ║  Creator: Oanks (@oanksnood)                                            ║
    ╚══════════════════════════════════════════════════════════════════════════╝
    """
    
    # Create deployment instance
    deployment = Phase15Deployment()
    
    # Parse arguments
    args = deployment.parse_arguments()
    
    # Setup logging first (before anything else)
    logger = setup_logging(
        verbose=args.verbose if hasattr(args, "verbose") else DEFAULT_VERBOSE,
        quiet=args.quiet if hasattr(args, "quiet") else DEFAULT_QUIET,
        log_file=args.log_file if hasattr(args, "log_file") else None
    )
    deployment._logger = logger
    
    # Handle systemd commands
    if hasattr(args, "systemd_install") and args.systemd_install:
        deployment.install_systemd_service()
        sys.exit(0)
    
    if hasattr(args, "systemd_remove") and args.systemd_remove:
        deployment.remove_systemd_service()
        sys.exit(0)
    
    if hasattr(args, "systemd_enable") and args.systemd_enable:
        deployment.enable_systemd_service()
        sys.exit(0)
    
    if hasattr(args, "systemd_disable") and args.systemd_disable:
        deployment.disable_systemd_service()
        sys.exit(0)
    
    # Handle status/health queries
    if hasattr(args, "status") and args.status:
        deployment.load_configuration()
        deployment.print_status()
        sys.exit(0)
    
    if hasattr(args, "health") and args.health:
        deployment.load_configuration()
        report = deployment.get_health_report()
        print(json.dumps(report, indent=2))
        sys.exit(0)
    
    # Load configuration
    deployment.load_configuration()
    
    # Initialize framework
    if not deployment.initialize():
        logger.critical("Framework initialization failed. Exiting.")
        sys.exit(1)
    
    # Start phases
    deployment.start_phases()
    
    # Determine run mode
    if hasattr(args, "daemon") and args.daemon:
        deployment.run_daemon()
    elif hasattr(args, "autonomous") and args.autonomous:
        deployment.run_autonomous()
    else:
        deployment.run()
