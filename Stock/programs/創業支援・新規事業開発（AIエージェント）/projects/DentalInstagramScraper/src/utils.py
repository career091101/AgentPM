"""
Utility functions for DentalInstagramScraper.
"""
import logging
import os
from pathlib import Path
from typing import Dict, Any
import yaml
from dotenv import load_dotenv


def setup_logger(log_file: str, console_level: str = 'INFO', file_level: str = 'DEBUG') -> logging.Logger:
    """
    Set up logger with console and file handlers.

    Args:
        log_file: Path to log file
        console_level: Console log level (default: INFO)
        file_level: File log level (default: DEBUG)

    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger('dental_instagram_scraper')
    logger.setLevel(logging.DEBUG)

    # Clear existing handlers
    logger.handlers.clear()

    # Create formatters
    console_formatter = logging.Formatter(
        '[%(levelname)s] %(message)s'
    )
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, console_level.upper()))
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(getattr(logging, file_level.upper()))
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger


def load_config(config_path: str = 'config.yaml') -> Dict[str, Any]:
    """
    Load YAML configuration file and environment variables.

    Args:
        config_path: Path to YAML config file (default: config.yaml)

    Returns:
        Configuration dictionary
    """
    # Load environment variables from .env file
    load_dotenv()

    # Load YAML config
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Add environment variables to config
    config['env'] = {
        'INSTAGRAM_USERNAME': os.getenv('INSTAGRAM_USERNAME'),
        'INSTAGRAM_PASSWORD': os.getenv('INSTAGRAM_PASSWORD'),
        'ANTHROPIC_API_KEY': os.getenv('ANTHROPIC_API_KEY'),
    }

    return config


def show_progress(message: str):
    """
    Show progress message with formatting.

    Args:
        message: Progress message to display
    """
    print(f"\n{'='*60}")
    print(f"  {message}")
    print(f"{'='*60}\n")
