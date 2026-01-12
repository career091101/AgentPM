"""設定管理モジュール"""

import os
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Config:
    """PDF Reader MCP Server 設定"""
    
    # Gemini API設定
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.0-flash-exp"
    
    # 処理設定
    max_concurrent_requests: int = 5
    image_analysis_timeout: int = 30
    
    # 出力設定
    output_dir: Optional[str] = None
    temp_dir: str = "/tmp/pdf_reader_mcp"
    
    # Vision解析プロンプト
    vision_prompt_template: str = """この画像の内容を日本語で詳しく説明してください。
特に以下の点に注目してください：
- チャートやグラフの場合：トレンド、数値、重要なポイント
- 図表の場合：構造と主要な情報
- テキストが含まれる場合：その内容

{context}"""

    @classmethod
    def load(cls) -> "Config":
        """設定を読み込む（環境変数 → 設定ファイル → デフォルト）"""
        config = cls()
        
        # 環境変数から読み込み
        config.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        
        if env_model := os.getenv("GEMINI_MODEL"):
            config.gemini_model = env_model
        
        if env_output := os.getenv("PDF_READER_OUTPUT_DIR"):
            config.output_dir = env_output
        
        # 設定ファイルから読み込み（存在する場合）
        config_file = Path.home() / ".config" / "pdf-reader-mcp" / "config.json"
        if config_file.exists():
            try:
                with open(config_file) as f:
                    file_config = json.load(f)
                    
                # API Keyが環境変数にない場合のみファイルから取得
                if not config.gemini_api_key:
                    config.gemini_api_key = file_config.get("gemini_api_key", "")
                
                # その他の設定
                if "gemini_model" in file_config:
                    config.gemini_model = file_config["gemini_model"]
                if "output_dir" in file_config:
                    config.output_dir = file_config["output_dir"]
                if "max_concurrent_requests" in file_config:
                    config.max_concurrent_requests = file_config["max_concurrent_requests"]
            except (json.JSONDecodeError, OSError):
                pass  # 設定ファイルの読み込みに失敗した場合は無視
        
        return config
    
    def validate(self) -> list[str]:
        """設定を検証し、エラーメッセージのリストを返す"""
        errors = []
        
        if not self.gemini_api_key:
            errors.append("GEMINI_API_KEY が設定されていません。環境変数または設定ファイルで指定してください。")
        
        return errors


# シングルトンインスタンス
_config: Optional[Config] = None


def get_config() -> Config:
    """設定シングルトンを取得"""
    global _config
    if _config is None:
        _config = Config.load()
    return _config
