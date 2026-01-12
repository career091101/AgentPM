"""Gemini Vision API を使用した画像解析モジュール"""

# 警告を抑制（MCPのstdio通信を保護するため）
import warnings
warnings.filterwarnings("ignore")

import asyncio
import base64
from pathlib import Path
from typing import Optional

# google.generativeai は内部でエラーメッセージをprintする
# stdoutを一時的に抑制してからインポート
from . import suppress_output, restore_output

suppress_output()
try:
    import google.generativeai as genai
finally:
    restore_output()

from .config import get_config, Config


class VisionAnalyzer:
    """Gemini Vision APIを使用した画像解析"""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or get_config()
        self._model = None
        self._initialized = False
    
    def _ensure_initialized(self):
        """API初期化を確認"""
        if not self._initialized:
            if not self.config.gemini_api_key:
                raise ValueError("GEMINI_API_KEYが設定されていません")
            
            genai.configure(api_key=self.config.gemini_api_key)
            self._model = genai.GenerativeModel(self.config.gemini_model)
            self._initialized = True
    
    async def analyze_image(
        self,
        image_data: bytes,
        context: str = "",
        mime_type: str = "image/png"
    ) -> str:
        """
        画像を解析し、日本語で説明を生成
        
        Args:
            image_data: 画像のバイトデータ
            context: 追加のコンテキスト情報
            mime_type: 画像のMIMEタイプ
            
        Returns:
            画像の説明テキスト
        """
        self._ensure_initialized()
        
        # プロンプト生成
        context_text = f"\nコンテキスト: {context}" if context else ""
        prompt = self.config.vision_prompt_template.format(context=context_text)
        
        # 画像データを準備
        image_part = {
            "mime_type": mime_type,
            "data": base64.b64encode(image_data).decode("utf-8")
        }
        
        try:
            # 非同期で実行（同期APIをラップ）
            response = await asyncio.to_thread(
                self._model.generate_content,
                [prompt, image_part]
            )
            
            if response.text:
                return response.text.strip()
            else:
                return "[画像解析結果を取得できませんでした]"
                
        except Exception as e:
            return f"[画像解析エラー: {str(e)}]"
    
    async def analyze_image_file(
        self,
        file_path: str,
        context: str = ""
    ) -> str:
        """
        画像ファイルを解析
        
        Args:
            file_path: 画像ファイルのパス
            context: 追加のコンテキスト情報
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"画像ファイルが見つかりません: {file_path}")
        
        # MIMEタイプを推定
        suffix = path.suffix.lower()
        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }
        mime_type = mime_types.get(suffix, "image/png")
        
        image_data = path.read_bytes()
        return await self.analyze_image(image_data, context, mime_type)
    
    async def analyze_images_batch(
        self,
        images: list[tuple[bytes, str]],
        max_concurrent: int = 5
    ) -> list[str]:
        """
        複数の画像を並行解析
        
        Args:
            images: (画像データ, コンテキスト) のタプルリスト
            max_concurrent: 最大同時実行数
            
        Returns:
            解析結果のリスト
        """
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def analyze_with_limit(image_data: bytes, context: str) -> str:
            async with semaphore:
                return await self.analyze_image(image_data, context)
        
        tasks = [
            analyze_with_limit(img_data, ctx)
            for img_data, ctx in images
        ]
        
        return await asyncio.gather(*tasks)
