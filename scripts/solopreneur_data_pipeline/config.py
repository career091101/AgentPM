"""パイプライン設定"""

from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Config:
    """パイプライン設定クラス"""

    # ベースディレクトリ
    BASE_DIR: Path = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents")
    OUTPUT_DIR: Path = Path("/Users/yuichi/AIPM/aipm_v0/Flow/data_exports")

    # カテゴリ別パス
    APP_DIR: Path = BASE_DIR / "01_App/case_studies"
    NEWSLETTER_DIR: Path = BASE_DIR / "02_Newsletter/case_studies"
    SNS_DIR: Path = BASE_DIR / "03_SNS/case_studies"

    # スキーマディレクトリ
    SCHEMAS_DIR: Path = Path(__file__).parent / "schemas"

    # サポートバージョン
    SUPPORTED_VERSIONS: Dict[str, List[str]] = None

    def __post_init__(self):
        """初期化後処理"""
        self.SUPPORTED_VERSIONS = {
            "app": ["3.0", "4.0"],
            "sns": ["4.0", "5.0"],
            "newsletter": ["2.0", "2.1"]
        }

        # 出力ディレクトリ作成
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    def get_source_dir(self, category: str) -> Path:
        """カテゴリに応じたソースディレクトリを取得"""
        mapping = {
            "app": self.APP_DIR,
            "newsletter": self.NEWSLETTER_DIR,
            "sns": self.SNS_DIR
        }
        return mapping.get(category)

    def is_version_supported(self, category: str, version: str) -> bool:
        """バージョンがサポートされているか確認"""
        supported = self.SUPPORTED_VERSIONS.get(category, [])
        return version in supported


# デフォルトインスタンス
config = Config()
