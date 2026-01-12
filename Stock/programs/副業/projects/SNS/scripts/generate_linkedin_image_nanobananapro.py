#!/usr/bin/env python3
"""
NanoBananaPro API を使用してLinkedIn投稿用画像を生成するスクリプト

LinkedIn推奨仕様:
- サイズ: 1200×627px (アスペクト比 1.91:1)
- 解像度: 1K (Full HD相当、コスト削減)
- ファイル形式: PNG
- ファイルサイズ: 5MB以下

使用方法:
    python generate_linkedin_image_nanobananapro.py
"""

import os
import sys
from pathlib import Path
from google import genai
from PIL import Image
from io import BytesIO
from datetime import datetime

# プロジェクトルート追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class LinkedInImageGenerator:
    """NanoBananapro APIでLinkedIn投稿用画像を生成するクラス"""

    def __init__(self, api_key: str = None):
        """
        初期化

        Args:
            api_key: Google Gemini APIキー（省略時は環境変数から取得）
        """
        self.api_key = api_key or os.getenv("GOOGLE_GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "APIキーが設定されていません。環境変数 GOOGLE_GEMINI_API_KEY を設定するか、"
                "引数で api_key を指定してください。\n"
                "APIキー取得: https://aistudio.google.com/apikey"
            )

        self.client = genai.Client(api_key=self.api_key)
        self.model_name = "gemini-3-pro-image-preview"  # Nano Banana Pro

        # LinkedIn推奨仕様（1:1正方形、高エンゲージメント）
        self.linkedin_width = 1080
        self.linkedin_height = 1080
        self.linkedin_aspect_ratio = "1:1"  # 正方形、2026年調査で最高エンゲージメント

    def generate_image(
        self,
        prompt: str,
        output_path: str = None,
        resize_to_linkedin: bool = True
    ) -> str:
        """
        画像生成メイン関数

        Args:
            prompt: 画像生成プロンプト
            output_path: 保存先パス（省略時は自動生成）
            resize_to_linkedin: LinkedIn仕様（1200×627px）にリサイズするか

        Returns:
            保存したファイルパス
        """
        # LinkedIn OGP画像生成の最適化システムプロンプト
        system_prompt_prefix = """
あなたはLinkedIn投稿の高エンゲージメントOGP画像を生成するAIビジュアル・エディターです。

## 役割
投稿の核心を捉えた写実的で高品質なビジュアルと、読者の関心を強く引くテキストオーバーレイを組み合わせた画像を生成すること。

## 画像生成仕様

### 1. 基本設定（固定）
- **アスペクト比**: 1:1（1080×1080px、正方形）
  理由: 2026年調査で単一画像投稿は縦長（4:5）より正方形の方が30%高いエンゲージメント
- **スタイル**: Cinematic documentary photograph style, photorealistic, 8k UHD, natural film grain, shallow depth of field
- **構図**: 中心的な被写体を明確にし、背景を美しくボケ（bokeh）で表現
- **モバイル最適化**: 小画面でも視認性を保つ大きなテキスト・高コントラスト

### 2. テキストオーバーレイ（固定レイアウト）

#### 背景グラデーション（スクリム効果）
- 位置: 画像下部30-40%
- グラデーション: 黒（不透明度100%）→ 透明（不透明度0%）の滑らかな線形変化
- 目的: 白文字の可読性を最大化（WCAG基準：コントラスト比4.5:1以上）

#### テキスト構成
- **色**: 白（#FFFFFF）
- **フォント**: 太字（Bold）、モバイルで読みやすいサイズ
- **レイアウト**:
  1. **ヘッダー（上段）**: 'AI Update'（固定）
  2. **メインコピー（中段）**: 投稿から抽出した断定型キャッチコピー（後述）

### 3. 変動パラメータ（投稿内容から決定）

#### Step 1: 投稿分析
以下の投稿内容から以下を抽出してください:

1. **メインテーマ**: 投稿の核心的な概念
2. **具体的数値**: 削減率、倍率、金額、期間など（複数推奨）
3. **企業名・人名**: 信頼性を高める固有名詞
4. **トーン**: 投稿の雰囲気（例: 衝撃的、警告的、啓発的）

#### Step 2: キャッチコピー作成（メインコピー）

**必須要素**:
- 全角40-60文字（モバイル可読性優先で短縮）
- 2-3行の構成（1行20-30文字）
- **断定型表現**（「〜だ」「〜である」「〜を意味する」）
- **具体的数値を含む**（例: 80%削減、10倍、18兆円）
- **問いかけ要素**（オプション、例: 「〜か？」）

**高エンゲージメントパターン例**:
```
❌ 「AIツールが普及しているそうです」（伝聞型）
✅ 「AI導入で人員80%削減。2人で10人分の仕事が可能に」（断定型+数値）

❌ 「AGIが近い将来到来すると言われています」（抽象）
✅ 「AGI到来は2028年。確率50%とDeepMind創設者が断言」（具体+企業名）
```

#### Step 3: ビジュアル選定

**禁止事項**（肖像権・商標権保護）:
- 実在の人物の顔・肖像
- 実在企業のロゴマーク
- 特定製品のデザイン

**推奨ビジュアル**:
- **後ろ姿・シルエット**: ビジネスパーソンの象徴的な表現
- **手元クローズアップ**: タブレット操作、キーボード入力
- **抽象的メタファー**: AI（脳アイコン）、データフロー、ネットワーク
- **オフィス環境**: 窓、モニター、未来的な空間
- **テクノロジー要素**: ホログラム、グラフ、ダッシュボード

**背景**:
- 被写体の文脈に合った、リアルで雰囲気のある環境
- 浅い被写界深度（bokeh）で主題を強調
- 映画的照明（自然光、ドラマチックな陰影）

### 4. 品質基準

- **コントラスト比**: テキストと背景で4.5:1以上（WCAG 2.1 AA基準）
- **文字サイズ**: モバイルで読める大きさ（18pt以上推奨）
- **情報密度**: テキストは最小限（画像の30%以下）
- **視認性**: 遠目でも主題が理解できる構図

---

以下の投稿内容を分析し、上記仕様に従った高エンゲージメントOGP画像を生成してください:

"""

        full_prompt = system_prompt_prefix + prompt

        print(f"🎨 画像生成開始...")
        print(f"📝 プロンプト: {prompt[:100]}..." if len(prompt) > 100 else f"📝 プロンプト: {prompt}")
        print(f"🎭 スタイル: LinkedIn OGP（映画的ドキュメンタリー、1:1正方形、高エンゲージメント最適化）")

        try:
            # NanoBananaPro APIで画像生成
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
            )

            # 画像データ抽出
            image_data = None
            for part in response.parts:
                if hasattr(part, 'inline_data') and part.inline_data:
                    image_data = part.inline_data.data
                    break

            if image_data is None:
                raise ValueError("画像データが生成されませんでした")

            # PIL Imageに変換
            image = Image.open(BytesIO(image_data))
            print(f"✅ 画像生成完了: {image.size}")

            # LinkedIn仕様にリサイズ
            if resize_to_linkedin:
                original_size = image.size
                image = image.resize((self.linkedin_width, self.linkedin_height), Image.Resampling.LANCZOS)
                print(f"📐 リサイズ: {original_size} → {image.size} (LinkedIn 1:1正方形最適化)")

            # 保存先パス決定
            if output_path is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_dir = project_root / "output" / "linkedin_images"
                output_dir.mkdir(parents=True, exist_ok=True)
                output_path = output_dir / f"linkedin_{timestamp}.png"
            else:
                output_path = Path(output_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)

            # 画像保存
            image.save(output_path, format="PNG", optimize=True)
            file_size_mb = output_path.stat().st_size / (1024 * 1024)

            print(f"💾 保存完了: {output_path}")
            print(f"📊 ファイルサイズ: {file_size_mb:.2f}MB")

            if file_size_mb > 5.0:
                print(f"⚠️  警告: ファイルサイズが5MBを超えています（LinkedIn制限）")

            return str(output_path)

        except Exception as e:
            print(f"❌ エラー発生: {e}")
            raise


def get_sample_prompts() -> dict:
    """過去のLinkedIn投稿から抽出したサンプルプロンプト"""
    return {
        "1_ai_bpo": """
LayerX福島氏が提唱する「AI BPO」は、AIエージェント活用の標準形態を再定義する。従来の「人がAIツールを操作する」設計から、「AIが主体となり人が補完する」設計への転換だ。同氏によれば、米国のAIによるTFP（全要素生産性）への累積影響は0.7%未満、日本では0.58%にとどまる。AIの能力は急速に進化しているが、GDPへの反映は遅れている。

この課題の本質は「AIオンボーディング」にある。福島氏は「多くの問題は解かれるのを待っている状態」と表現する。生成AIには既に多くの問題を解く能力があり、ボトルネックはAIの知性ではなく、人間側の業務設計にある。そこで同氏が提唱するのが「Ambient Agent＋Human in the Loop」という組み合わせだ。チャット起点で人が依頼するのではなく、メール受信やファイルアップロードをトリガーにAIが自律的に起動し、必要な箇所だけ人が確認・修正する。バクラク事業では2025年に20を超えるAIエージェントをリリースし、請求書1枚あたりの課金というシンプルな単位で提供している。

この設計の利点は3点に集約される。第一に、AIの進化を待たずに今すぐ業務を自動化できること。第二に、オペレーション改善が即座に全顧客へ反映されるデプロイ速度。第三に、複雑なエージェント群を「仕事単位」でパッケージ化できる営業のシンプルさだ。「使えば使うほど賢くなるソフトウェア」がエンドゲームであると同氏は述べている。
        """,

        "2_agi_timeline": """
Google DeepMind共同創設者のシェーン・レッグ氏は「AGI（汎用人工知能）が2028年までに到来する確率は50%だ」と予測を述べた。かつてはSFの世界の話だった人間と同等の知能を持つAIが、わずか数年後の現実として迫っている。これは単なる技術の進歩ではない。産業革命以来の社会構造の転換点であり、我々の働き方や生き方を根本から問い直す警鐘でもあるのだ。

変化の本質は、AIが「道具」から「パートナー」、さらには「労働の主体」へと進化する点にある。レッグ氏は、数年以内にソフトウェア開発の大部分をAIが担うようになると指摘する。人間ができる知的作業の多くをAIが肩代わりする時代において、既存のスキルや役割は急速に陳腐化するだろう。だからこそ、AIが直感だけでなく論理的に倫理判断を行う「システム2」のような安全性の仕組みが、技術開発と同じ重みを持って追求されている。

問われているのは、超知能を持つAIと共存する社会をどう設計するかだ。経済的な豊かさが爆発的に増大する一方で、その分配や人間の役割はどうあるべきか。技術の進化速度に社会の適応が追いつかないリスクも孕む。AI任せにするのではなく、教育や法制度を含めた人間中心の新たな社会ビジョンを、今こそ我々自身が描き出す必要がある。
        """,

        "3_claude_opus": """
Claude Opus 4.5の登場により、「AIエージェントは5時間の仕事が成功できる」その進化スピードは4か月で2倍と一度懸念された停滞を打破し、再び急成長の軌道に乗っている。これは、AIが単なる対話の相手から、人間が数時間を要する複雑な実務を自律的にやり遂げる「エージェント」のフェーズへ突入したことを意味する。

かつてのAIは数秒〜分の処理が限界だったが、その能力は指数関数的に拡大している。データによれば、1時間半かかる「Pythonライブラリのバグ修正」から、4時間を要する「堅牢な画像モデルの訓練」までもが射程に入りつつある。2026年には、人間が半日費やす業務をAIが50％の確率で成功させると予測されており、AIはチャットボットから、長時間労働を代行する「自律型エージェント」へと変貌を遂げようとしている。

「4ヶ月で倍増」という速度は、人間のスキル習得ペースを遥かに凌駕する。数時間の集中作業がAIに代替される未来では、プロセスを自ら手を動かして完遂する能力よりも、AIの成果物を適切に評価し、方向付けを行う「監督者」としてのスキルが不可欠になる。私たちは今、自らの役割を「作業者」から、AIという優秀な部下を持つ「指揮官」へと再定義する局面に立たされている。
        """,

        "4_ai_productivity": """
トランスコスモスは『AIによる過半数の承認がなければ次工程に進めない』という新制度を導入した。要件定義書を5つの異なるLLMにレビューさせ、3つ以上の承認を必須とする「AI合議制」の実装だ。この徹底した品質管理と生成AI活用である「バイブコーディング」により、同社は開発工数の80％削減を実現している。

特筆すべきは、この技術がエンジニアのキャリア形成に変革をもたらしている点だ。AIが多角的に欠陥を指摘し品質を担保するため、従来はベテランの聖域だった上流工程に、経験の浅いジュニア層が参画できるようになった。人間は実装の細部ではなく、「何を作るか」という価値設計に集中でき、若手のうちから高度な設計思考を養うことが可能になっている。

これは、AIを単なる効率化ツールとしてではなく、組織の「品質ゲートキーパー」として統合した先進例である。自動化で生まれた余白は、人間にしかできない創造的な意思決定や対話に充てられる。テクノロジーは人の仕事を奪うのではなく、経験の壁を取り払い、全てのエンジニアが本質的な価値創造に向き合えるよう、その能力を拡張している。
        """
    }


def main():
    """メイン実行関数"""
    print("=" * 70)
    print("LinkedIn投稿用画像生成ツール (NanoBananaPro)")
    print("=" * 70)
    print()

    # APIキーチェック
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    if not api_key:
        print("❌ エラー: 環境変数 GOOGLE_GEMINI_API_KEY が設定されていません")
        print()
        print("以下の手順でAPIキーを設定してください:")
        print("1. https://aistudio.google.com/apikey にアクセス")
        print("2. APIキーを取得")
        print("3. 環境変数を設定:")
        print("   export GOOGLE_GEMINI_API_KEY='your-api-key-here'")
        print()
        return

    # ジェネレーター初期化
    generator = LinkedInImageGenerator(api_key=api_key)

    # サンプルプロンプト表示
    sample_prompts = get_sample_prompts()
    print("📋 利用可能なサンプルプロンプト:")
    for idx, (key, prompt) in enumerate(sample_prompts.items(), 1):
        title = prompt.strip().split("\n")[2].strip()  # テーマ行を抽出
        print(f"  {idx}. {title}")
    print(f"  {len(sample_prompts) + 1}. カスタムプロンプトを入力")
    print()

    # ユーザー選択
    try:
        choice = input("選択してください (1-5): ").strip()
        choice_num = int(choice)

        if 1 <= choice_num <= len(sample_prompts):
            # サンプルプロンプト選択
            selected_key = list(sample_prompts.keys())[choice_num - 1]
            prompt = sample_prompts[selected_key]
            print(f"\n✅ 選択: {selected_key}")
        elif choice_num == len(sample_prompts) + 1:
            # カスタムプロンプト入力
            print("\n📝 カスタムプロンプトを入力してください:")
            prompt = input("> ").strip()
            if not prompt:
                print("❌ プロンプトが空です。終了します。")
                return
        else:
            print("❌ 無効な選択です。")
            return

    except (ValueError, KeyboardInterrupt):
        print("\n❌ キャンセルされました。")
        return

    print()

    # 画像生成実行
    try:
        output_path = generator.generate_image(
            prompt=prompt,
            resize_to_linkedin=True
        )

        print()
        print("=" * 70)
        print("✨ 画像生成完了！")
        print("=" * 70)
        print(f"📁 ファイルパス: {output_path}")
        print()
        print("LinkedIn投稿時の注意:")
        print("  - 推奨サイズ: 1080×1080px（1:1正方形）✅")
        print("  - ファイルサイズ: 5MB以下を推奨")
        print("  - 2026年調査: 正方形が最高エンゲージメント")
        print("  - テキストオーバーレイ: 画像下部30-40%（スクリム効果）")
        print("  - コントラスト比: 4.5:1以上（WCAG基準）")
        print()

    except Exception as e:
        print(f"\n❌ 画像生成に失敗しました: {e}")
        return


if __name__ == "__main__":
    main()
