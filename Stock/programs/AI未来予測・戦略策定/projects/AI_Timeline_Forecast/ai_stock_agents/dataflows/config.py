# AI Stock Agents - Configuration Management
# Based on TradingAgents-main/tradingagents/dataflows/config.py

import sys
import os
from typing import Dict, Optional
from pathlib import Path

# Add parent directory to path to import default_ai_stock_config
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import default_ai_stock_config as default_config

# Use default config but allow it to be overridden
_config: Optional[Dict] = None
DATA_DIR: Optional[str] = None


def initialize_config():
    """Initialize the configuration with default values."""
    global _config, DATA_DIR
    if _config is None:
        _config = default_config.AI_STOCK_CONFIG.copy()
        # Set data directory (use current directory + data/ by default)
        base_dir = Path(__file__).parent.parent
        DATA_DIR = str(base_dir / "data")
        _config["data_dir"] = DATA_DIR


def set_config(config: Dict):
    """Update the configuration with custom values."""
    global _config, DATA_DIR
    if _config is None:
        _config = default_config.AI_STOCK_CONFIG.copy()
    _config.update(config)
    DATA_DIR = _config.get("data_dir", DATA_DIR)


def get_config() -> Dict:
    """Get the current configuration."""
    if _config is None:
        initialize_config()
    return _config.copy()


# Initialize with default config
initialize_config()
