#!/usr/bin/env python3
"""
画像にテキストオーバーレイを追加するスクリプト
"""

from PIL import Image, ImageDraw, ImageFont
import sys
from pathlib import Path

def add_text_overlay(
    image_path: str,
    output_path: str = None,
    title: str = "AI BPO",
    subtitle1: str = "人間→AIツール操作 から",
    subtitle2: str = "AI→自律実行、人→確認・修正 へ"
):
    """
    画像にテキストオーバーレイを追加

    Args:
        image_path: 入力画像パス
        output_path: 出力パス（省略時は元ファイルに_text追加）
        title: タイトルテキスト
        subtitle1: サブタイトル1
        subtitle2: サブタイトル2
    """
    # 画像を開く
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    # システムフォントを使用（日本語対応）
    try:
        # macOSの日本語フォント
        title_font = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc", 80)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc", 40)
    except:
        try:
            # フォールバック（Arial）
            title_font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 80)
            subtitle_font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 40)
        except:
            # デフォルトフォント
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            print("⚠️  警告: 日本語フォントが見つかりません。デフォルトフォントを使用します。")

    # テキスト配置位置
    title_y = height * 0.15
    subtitle1_y = height * 0.45
    subtitle2_y = height * 0.65

    # テキスト描画（縁取り付き）
    def draw_text_with_outline(text, font, y_position, outline_width=4):
        """縁取り付きテキストを描画"""
        # テキストサイズを取得
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2

        # 黒い縁取り
        for offset_x in range(-outline_width, outline_width + 1):
            for offset_y in range(-outline_width, outline_width + 1):
                draw.text(
                    (x + offset_x, y_position + offset_y),
                    text,
                    font=font,
                    fill=(0, 0, 0, 255)  # 黒
                )

        # 白いテキスト
        draw.text(
            (x, y_position),
            text,
            font=font,
            fill=(255, 255, 255, 255)  # 白
        )

    # テキスト描画
    draw_text_with_outline(title, title_font, title_y, outline_width=6)
    draw_text_with_outline(subtitle1, subtitle_font, subtitle1_y, outline_width=3)
    draw_text_with_outline(subtitle2, subtitle_font, subtitle2_y, outline_width=3)

    # 保存
    if output_path is None:
        input_path = Path(image_path)
        output_path = input_path.parent / f"{input_path.stem}_text{input_path.suffix}"

    img.save(output_path, format="PNG", optimize=True)
    print(f"✅ テキスト追加完了: {output_path}")
    print(f"📊 ファイルサイズ: {Path(output_path).stat().st_size / (1024 * 1024):.2f}MB")

    return str(output_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python add_text_to_image.py <画像パス>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = add_text_overlay(input_image)
    print(f"\n💾 保存先: {output_image}")
