"""
AI Agent Strategy Wrapper

既存のAgentSkillsシステムをバックテストエンジンから呼び出すためのアダプター
"""

from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path
import sys

# 親ディレクトリをパスに追加（既存のエージェントシステムにアクセス）
agent_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(agent_root))


class AIAgentStrategy:
    """
    AI Agent Strategy Wrapper

    バックテストエンジンの戦略関数インターフェース（decision_date, available_tickers）と
    既存のAgentSkillsシステムを統合
    """

    def __init__(
        self,
        enable_agents: bool = False,  # AgentSkills有効化（False = 等ウェイト）
        use_simple_fallback: bool = True,  # エージェント失敗時に等ウェイトへフォールバック
    ):
        """
        Args:
            enable_agents: AgentSkillsシステムを使用するか（False = 等ウェイト戦略）
            use_simple_fallback: エージェント失敗時の等ウェイトフォールバック
        """
        self.enable_agents = enable_agents
        self.use_simple_fallback = use_simple_fallback

        # AgentSkillsシステムの初期化（実装時に追加）
        self.agent_graph = None
        if enable_agents:
            try:
                self._initialize_agent_system()
            except Exception as e:
                print(f"⚠️  Failed to initialize agent system: {e}")
                if not use_simple_fallback:
                    raise

    def __call__(
        self,
        decision_date: datetime,
        available_tickers: List[str],
    ) -> Dict[str, float]:
        """
        バックテストエンジンから呼び出される戦略関数

        Args:
            decision_date: 判断日（この日までのデータのみ使用可能）
            available_tickers: 投資可能な銘柄リスト

        Returns:
            {ticker: weight} の辞書（合計1.0）
        """
        # エージェントシステムが有効な場合
        if self.enable_agents and self.agent_graph:
            try:
                return self._run_agent_strategy(decision_date, available_tickers)
            except Exception as e:
                print(f"❌ Agent strategy failed: {e}")
                if not self.use_simple_fallback:
                    raise

        # フォールバック: 等ウェイト戦略
        return self._equal_weight_strategy(available_tickers)

    def _initialize_agent_system(self) -> None:
        """
        AgentSkillsシステムの初期化

        TODO: 実装時に以下を実装
        - AgentSkills初期化
        - 各種エージェント（アナリスト、トレーダー等）の設定
        - データソース接続
        """
        # 現時点ではプレースホルダー
        print("📊 AgentSkills initialization (placeholder)")
        # from skills.setup import SkillsSetup
        # self.agent_graph = SkillsSetup(...).setup_agents()

    def _run_agent_strategy(
        self,
        decision_date: datetime,
        available_tickers: List[str],
    ) -> Dict[str, float]:
        """
        AgentSkillsシステムを実行してポートフォリオウェイトを取得

        Args:
            decision_date: 判断日
            available_tickers: 投資可能銘柄

        Returns:
            {ticker: weight} の辞書
        """
        # TODO: 実装時に以下を実装
        # 1. decision_dateとavailable_tickersを使ってStateを構築
        # 2. agent_graph.invoke(state)を実行
        # 3. final_portfolio_decisionからウェイトを抽出
        # 4. available_tickersのみに絞り込み

        # 現時点ではプレースホルダー（等ウェイト返却）
        print(f"🤖 Running AI agents for {decision_date.date()} ({len(available_tickers)} stocks)")
        return self._equal_weight_strategy(available_tickers)

    def _equal_weight_strategy(self, tickers: List[str]) -> Dict[str, float]:
        """
        等ウェイト戦略（フォールバック）

        Args:
            tickers: ティッカーリスト

        Returns:
            {ticker: weight} の辞書
        """
        if not tickers:
            return {}

        weight = 1.0 / len(tickers)
        return {ticker: weight for ticker in tickers}


# ヘルパー関数


def create_ai_agent_strategy(
    enable_agents: bool = False,
    use_simple_fallback: bool = True,
) -> AIAgentStrategy:
    """
    AI Agent Strategy作成（ファクトリー関数）

    Args:
        enable_agents: 14エージェント有効化
        use_simple_fallback: フォールバック有効化

    Returns:
        AIAgentStrategy callable
    """
    return AIAgentStrategy(
        enable_agents=enable_agents,
        use_simple_fallback=use_simple_fallback,
    )
