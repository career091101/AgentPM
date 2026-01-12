#!/bin/bash
# リアルタイムエージェント監視スクリプト
# 作成日: 2025-12-29

DOCS_DIR="/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents"
LOG_FILE="/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-29/agent_monitor.log"
START_TIME=$(date +%s)

# 初期カウント
INITIAL_COUNT=$(find "$DOCS_DIR" -name "*.md" -type f | wc -l | tr -d ' ')

echo "╔══════════════════════════════════════════════════════════════╗" | tee "$LOG_FILE"
echo "║    Founder Research エージェント監視システム                  ║" | tee -a "$LOG_FILE"
echo "╠══════════════════════════════════════════════════════════════╣" | tee -a "$LOG_FILE"
echo "║ 開始時刻: $(date '+%Y-%m-%d %H:%M:%S')                              ║" | tee -a "$LOG_FILE"
echo "║ ベースライン: $INITIAL_COUNT ファイル                                  ║" | tee -a "$LOG_FILE"
echo "╚══════════════════════════════════════════════════════════════╝" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# 前回の新規ファイルリストを保存
PREV_FILES=$(mktemp)
find "$DOCS_DIR" -name "*.md" -type f > "$PREV_FILES"

iteration=0

while true; do
  iteration=$((iteration + 1))

  # 現在のファイル数
  CURRENT_COUNT=$(find "$DOCS_DIR" -name "*.md" -type f | wc -l | tr -d ' ')
  FILES_CREATED=$((CURRENT_COUNT - INITIAL_COUNT))

  # ティア別カウント
  LEGENDARY=$(find "$DOCS_DIR/01_Legendary" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  UNICORN=$(find "$DOCS_DIR/02_Unicorn" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  VC_BACKED=$(find "$DOCS_DIR/03_VC_Backed" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  IPO_JAPAN=$(find "$DOCS_DIR/04_IPO_Japan" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  IPO_GLOBAL=$(find "$DOCS_DIR/05_IPO_Global" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  PIVOT=$(find "$DOCS_DIR/06_Pivot_Success" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  FAILURE=$(find "$DOCS_DIR/07_Failure_Study" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  EMERGING=$(find "$DOCS_DIR/08_Emerging" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

  # アクティブプロセス数
  ACTIVE_AGENTS=$(ps aux | grep "claude" | grep -v grep | wc -l | tr -d ' ')

  # 経過時間
  CURRENT_TIME=$(date +%s)
  ELAPSED=$((CURRENT_TIME - START_TIME))
  ELAPSED_MIN=$((ELAPSED / 60))
  ELAPSED_SEC=$((ELAPSED % 60))

  # 画面クリア (30秒ごとに更新)
  clear

  echo "╔══════════════════════════════════════════════════════════════╗"
  echo "║    Founder Research エージェント監視システム                  ║"
  echo "╠══════════════════════════════════════════════════════════════╣"
  echo "║ 時刻: $(date '+%H:%M:%S')          経過: ${ELAPSED_MIN}分${ELAPSED_SEC}秒                   ║"
  echo "║ ステータス: ⚙️  実行中 (反復 #$iteration)                            ║"
  echo "╠══════════════════════════════════════════════════════════════╣"
  echo "║ エージェント                                                  ║"
  echo "║   アクティブプロセス: $ACTIVE_AGENTS                                        ║"
  echo "╠══════════════════════════════════════════════════════════════╣"
  echo "║ ファイル進捗                                                  ║"
  echo "║   総ファイル数: $CURRENT_COUNT (開始時: $INITIAL_COUNT)                           ║"
  echo "║   新規作成: +$FILES_CREATED ファイル                                    ║"
  echo "╠══════════════════════════════════════════════════════════════╣"
  echo "║ ティア別内訳                                                  ║"
  echo "║   Legendary: $LEGENDARY    Unicorn: $UNICORN    VC_Backed: $VC_BACKED              ║"
  echo "║   IPO_Japan: $IPO_JAPAN    IPO_Global: $IPO_GLOBAL    Pivot: $PIVOT                  ║"
  echo "║   Failure: $FAILURE    Emerging: $EMERGING                                  ║"
  echo "╚══════════════════════════════════════════════════════════════╝"

  # 新規作成ファイルを検出 (過去30秒)
  CURRENT_FILES=$(mktemp)
  find "$DOCS_DIR" -name "*.md" -type f > "$CURRENT_FILES"

  NEW_FILES=$(comm -13 "$PREV_FILES" "$CURRENT_FILES")

  if [ -n "$NEW_FILES" ]; then
    echo ""
    echo "📝 新規作成ファイル (この30秒):"
    echo "$NEW_FILES" | while read -r file; do
      filename=$(basename "$file")
      tier=$(echo "$file" | sed 's|.*/\([^/]*\)/[^/]*$|\1|')
      echo "  ✅ [$tier] $filename"
    done
  fi

  # 最近更新されたファイル (過去5分)
  RECENT_UPDATES=$(find "$DOCS_DIR" -name "*.md" -mmin -5 2>/dev/null | wc -l | tr -d ' ')
  if [ "$RECENT_UPDATES" -gt 0 ]; then
    echo ""
    echo "🔄 過去5分の更新: $RECENT_UPDATES ファイル"
  fi

  # ファイルリスト更新
  mv "$CURRENT_FILES" "$PREV_FILES"

  # ログに記録
  echo "$(date '+%H:%M:%S') | Total: $CURRENT_COUNT | Active: $ACTIVE_AGENTS | New: +$FILES_CREATED | Recent: $RECENT_UPDATES" >> "$LOG_FILE"

  # 完了チェック
  if [ "$ACTIVE_AGENTS" -le 2 ] && [ "$iteration" -gt 2 ]; then
    echo ""
    echo "🎉 エージェント実行完了の可能性あり (アクティブプロセス: $ACTIVE_AGENTS)"
    echo "最終カウント: $CURRENT_COUNT ファイル (+$FILES_CREATED 新規)"
    echo ""
    echo "ログ保存先: $LOG_FILE"

    # 最終サマリーをログに記録
    echo "" >> "$LOG_FILE"
    echo "=== 最終サマリー ===" >> "$LOG_FILE"
    echo "総ファイル数: $CURRENT_COUNT (+$FILES_CREATED)" >> "$LOG_FILE"
    echo "Legendary: $LEGENDARY, Unicorn: $UNICORN, VC_Backed: $VC_BACKED" >> "$LOG_FILE"
    echo "IPO_Japan: $IPO_JAPAN, IPO_Global: $IPO_GLOBAL, Pivot: $PIVOT" >> "$LOG_FILE"
    echo "Failure: $FAILURE, Emerging: $EMERGING" >> "$LOG_FILE"
    echo "実行時間: ${ELAPSED_MIN}分${ELAPSED_SEC}秒" >> "$LOG_FILE"

    break
  fi

  # 30秒待機
  sleep 30
done

# クリーンアップ
rm -f "$PREV_FILES"

echo ""
echo "✅ 監視完了"
