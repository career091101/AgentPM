"""
Instagram dental clinic scraper package.
"""
from .models import (
    InstagramProfile,
    ExtractedData,
    FactCheckResult,
    FinalOutput
)
from .data_extractor import DataExtractor
from .fact_checker import FactChecker
from .instagram_collector import InstagramCollector
from .csv_exporter import CSVExporter
from . import utils

__all__ = [
    'InstagramProfile',
    'ExtractedData',
    'FactCheckResult',
    'FinalOutput',
    'DataExtractor',
    'FactChecker',
    'InstagramCollector',
    'CSVExporter',
    'utils',
]

__version__ = '1.0.0'
