"""PDF Reader MCP Server - PDFからテキストと画像を抽出しLLMで解析"""

# ========================================
# MCPはstdioでJSON-RPC通信を行うため、
# 警告メッセージがstdoutに出力されると通信が壊れる。
# パッケージ読み込み時に最初に警告を抑制し、
# stdoutへの不正な出力を完全にブロックする。
# ========================================
import warnings
import os
import sys
import io

# 全ての警告を抑制
warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

# Pythonの警告出力先をstderrに固定
import logging
logging.captureWarnings(True)

# ========================================
# 重要: google-generativeaiパッケージは内部でprintを使って
# エラーメッセージを出力する。これをキャプチャするため、
# 問題のあるモジュールをインポートする際にstdoutを一時的に抑制する。
# ========================================
_original_stdout = sys.stdout
_original_stderr = sys.stderr

def suppress_output():
    """stdout/stderrを一時的に抑制"""
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

def restore_output():
    """stdout/stderrを復元"""
    sys.stdout = _original_stdout
    sys.stderr = _original_stderr

__version__ = "0.1.0"
