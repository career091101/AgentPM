#!/usr/bin/env python3
"""
LinkedIn コンテンツ品質分析スクリプト
Phase 1: フック品質の解剖
Phase 2: 構造品質の診断
Phase 3: 問いかけ品質の精査
"""

import pandas as pd
import json
import re
from pathlib import Path
from datetime import datetime

# ファイルパス設定
BASE_DIR = Path(__file__).parent.parent
LINKEDIN_CSV = BASE_DIR / "X" / "linkedin-2026-01-01.csv"
POPULAR_CSV = BASE_DIR / "LinkedIn" / "linkedin_人気の投稿.csv"
TAKANO_MD = BASE_DIR / "knowledge" / "LinkedIn" / "research_reports" / "takano_writing_method.md"
OUTPUT_DIR = BASE_DIR / "LinkedIn"

# 出力ファイル
OUTPUT_JSON = OUTPUT_DIR / "linkedin_content_quality_analysis.json"

# ================================================================
# Phase 1: フック品質分析
# ================================================================

def analyze_hook(text):
    """
    1行目のフック品質を分析

    Returns:
        dict: {
            'first_line': str,
            'length': int,
            'has_number': bool,
            'has_company': bool,
            'has_question': bool,
            'is_assertive': bool,
            'hook_score': int (0-20点)
        }
    """
    if not isinstance(text, str) or not text.strip():
        return {
            'first_line': '',
            'length': 0,
            'has_number': False,
            'has_company': False,
            'has_question': False,
            'is_assertive': False,
            'hook_score': 0
        }

    # 1行目抽出
    first_line = text.split('\n')[0] if '\n' in text else text[:150]
    first_line = first_line.strip()

    # 基本特徴抽出
    has_number = bool(re.search(r'\d+', first_line))
    has_company = bool(re.search(r'(OpenAI|Google|Tesla|Meta|Apple|Amazon|Microsoft|AI|ChatGPT)', first_line))
    has_question = '?' in first_line or '？' in first_line
    is_assertive = bool(re.search(r'(だ|である|した|です|ます)。?$', first_line))

    # 衝撃度スコアリング（20点満点）
    score = 0

    # 1. 具体性（0-5点）
    if has_number and has_company:
        score += 5  # 数字+企業名
    elif has_number or has_company:
        score += 3  # どちらか
    elif len(first_line) > 20:
        score += 1  # 最低限の情報量

    # 2. 意外性（0-5点）
    surprise_keywords = ['ヤバい', 'マジで', '衝撃', '異常', '前代未聞', '史上最', '完全に壊れる', 'ありえない']
    if any(kw in first_line for kw in surprise_keywords):
        score += 5
    elif '!' in first_line or '！' in first_line:
        score += 2

    # 3. 緊急性（0-5点）
    urgency_keywords = ['今', '今すぐ', '本日', '速報', '緊急', '発表', '開始', '終了']
    if any(kw in first_line for kw in urgency_keywords):
        score += 5
    elif has_number:
        score += 2  # 数字は具体性=緊急性

    # 4. ターゲット明確性（0-5点）
    target_keywords = ['経営者', 'CEO', '起業家', 'スタートアップ', '社長', '経営']
    if any(kw in first_line for kw in target_keywords):
        score += 5
    elif 'ビジネス' in first_line or '企業' in first_line:
        score += 3

    return {
        'first_line': first_line,
        'length': len(first_line),
        'has_number': has_number,
        'has_company': has_company,
        'has_question': has_question,
        'is_assertive': is_assertive,
        'hook_score': min(score, 20)  # 最大20点
    }

# ================================================================
# Phase 2: 構造品質分析
# ================================================================

def analyze_structure(text):
    """
    段落構成と情報密度を分析

    Returns:
        dict: {
            'num_paragraphs': int,
            'avg_para_length': float,
            'total_chars': int,
            'company_count': int,
            'number_count': int,
            'has_data': bool,
            'has_example': bool,
            'has_insight': bool,
            'has_cta': bool,
            'structure_score': int (0-7点)
        }
    """
    if not isinstance(text, str) or not text.strip():
        return {
            'num_paragraphs': 0,
            'avg_para_length': 0,
            'total_chars': 0,
            'company_count': 0,
            'number_count': 0,
            'has_data': False,
            'has_example': False,
            'has_insight': False,
            'has_cta': False,
            'structure_score': 0
        }

    # 段落分割
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    num_paragraphs = len(paragraphs)
    total_chars = len(text)
    avg_para_length = total_chars / num_paragraphs if num_paragraphs > 0 else 0

    # 企業名・固有名詞のカウント
    company_pattern = r'(OpenAI|Google|Tesla|Meta|Apple|Amazon|Microsoft|孫正義|イーロン・マスク|サム・アルトマン)'
    company_count = len(re.findall(company_pattern, text))

    # 数値データのカウント
    number_pattern = r'\d+[,\.]\d+|\d+%|\d+億|\d+兆|\d+万'
    number_count = len(re.findall(number_pattern, text))

    # 高野メソッド7要素適合度チェック
    has_data = number_count >= 2  # ②データ/事例
    has_example = company_count >= 1  # ②事例
    has_insight = bool(re.search(r'(つまり|ポイントは|注目すべきは|本質は|重要なのは)', text))  # ④洞察
    has_cta = bool(re.search(r'(と思う\?|どう思いますか|はいかが|でしょうか)', text))  # ⑥問いかけ

    # 構造品質スコア（7点満点 = 高野メソッド7要素）
    score = 0
    score += 1 if avg_para_length > 50 else 0  # ①引き込み（段落が十分な長さ）
    score += 1 if has_data else 0  # ②データ
    score += 1 if has_example else 0  # ②事例
    score += 1  # ③共感（全投稿に存在すると仮定）
    score += 1 if has_insight else 0  # ④洞察
    score += 1  # ⑤アドバイス（仮定）
    score += 1 if has_cta else 0  # ⑥問いかけ
    # ⑦固有名詞はcompany_countで別途評価

    return {
        'num_paragraphs': num_paragraphs,
        'avg_para_length': round(avg_para_length, 1),
        'total_chars': total_chars,
        'company_count': company_count,
        'number_count': number_count,
        'has_data': has_data,
        'has_example': has_example,
        'has_insight': has_insight,
        'has_cta': has_cta,
        'structure_score': score
    }

# ================================================================
# Phase 3: 問いかけ品質分析
# ================================================================

def analyze_question(text):
    """
    問いかけのタイプと深さを分析

    Returns:
        dict: {
            'has_question': bool,
            'question_position': str ('beginning'|'middle'|'end'|'none'),
            'question_type': str ('yes_no'|'choice'|'why'|'what'|'how'|'none'),
            'question_depth': int (1-5),
            'target_clarity': str ('CEO'|'business'|'general')
        }
    """
    if not isinstance(text, str) or not text.strip():
        return {
            'has_question': False,
            'question_position': 'none',
            'question_type': 'none',
            'question_depth': 0,
            'target_clarity': 'general'
        }

    # 問いかけ検出パターン
    question_patterns = [
        r'か？', r'か\?', r'でしょうか', r'ますか', r'ませんか',
        r'のでは', r'だろうか', r'はいかが', r'どう思いますか',
        r'どう思う？', r'どう思う\?', r'成功すると思う？', r'成功すると思う\?'
    ]

    has_question = any(re.search(p, text) for p in question_patterns)

    if not has_question:
        return {
            'has_question': False,
            'question_position': 'none',
            'question_type': 'none',
            'question_depth': 0,
            'target_clarity': 'general'
        }

    # 問いかけの位置
    lines = text.split('\n')
    total_lines = len(lines)
    question_line = 0
    for i, line in enumerate(lines):
        if any(re.search(p, line) for p in question_patterns):
            question_line = i
            break

    if question_line < total_lines * 0.3:
        position = 'beginning'
    elif question_line > total_lines * 0.7:
        position = 'end'
    else:
        position = 'middle'

    # 問いかけのタイプ
    question_text = text[max(0, len(text) - 200):]  # 末尾200文字

    if re.search(r'(成功すると思う|同意します|そう思います)', question_text):
        q_type = 'yes_no'
    elif re.search(r'(どちらが|AかBか)', question_text):
        q_type = 'choice'
    elif re.search(r'なぜ', question_text):
        q_type = 'why'
    elif re.search(r'(どう|どのように)', question_text):
        q_type = 'how'
    else:
        q_type = 'what'

    # 深さレベル（1-5）
    depth = 1  # デフォルト: 表層
    if re.search(r'(あなたの会社|御社|貴社)', question_text):
        depth = 3  # 意見レベル
    if re.search(r'(どう対処|どう活用|どう取り組む)', question_text):
        depth = 4  # 戦略レベル
    if re.search(r'(今すぐ|明日|来週)', question_text):
        depth = 5  # 行動レベル

    # ターゲット明確性
    if re.search(r'(経営者|CEO|起業家|社長)', text):
        target = 'CEO'
    elif re.search(r'(ビジネス|企業|会社)', text):
        target = 'business'
    else:
        target = 'general'

    return {
        'has_question': True,
        'question_position': position,
        'question_type': q_type,
        'question_depth': depth,
        'target_clarity': target
    }

# ================================================================
# メイン処理
# ================================================================

def main():
    print("=" * 60)
    print("LinkedIn コンテンツ品質分析")
    print("=" * 60)

    # データ読み込み
    print("\n[1/6] データ読み込み中...")
    try:
        df_posts = pd.read_csv(LINKEDIN_CSV, encoding='utf-8-sig')
        print(f"  ✓ linkedin-2026-01-01.csv: {len(df_posts)}投稿")
    except Exception as e:
        print(f"  ✗ エラー: {e}")
        return

    try:
        df_popular = pd.read_csv(POPULAR_CSV, encoding='utf-8-sig')
        print(f"  ✓ linkedin_人気の投稿.csv: {len(df_popular)}投稿")
    except Exception as e:
        print(f"  ⚠ 警告: 人気投稿データ読み込み失敗: {e}")
        df_popular = None

    # カラム名確認
    print(f"\n[2/6] カラム確認...")
    print(f"  利用可能なカラム: {df_posts.columns.tolist()}")

    # 本文カラムを特定
    text_col = None
    for col in ['media-description', 'description', 'content', 'text', 'body']:
        if col in df_posts.columns:
            text_col = col
            break

    if not text_col:
        print(f"  ✗ エラー: 本文カラムが見つかりません")
        return

    print(f"  ✓ 本文カラム: {text_col}")

    # Phase 1-3: 全投稿を分析
    print(f"\n[3/6] Phase 1: フック品質分析中...")
    hook_results = []
    for idx, row in df_posts.iterrows():
        text = row[text_col]
        result = analyze_hook(text)
        result['post_id'] = idx
        hook_results.append(result)

    hook_df = pd.DataFrame(hook_results)
    print(f"  ✓ 完了: 平均スコア {hook_df['hook_score'].mean():.1f}/20点")

    print(f"\n[4/6] Phase 2: 構造品質分析中...")
    structure_results = []
    for idx, row in df_posts.iterrows():
        text = row[text_col]
        result = analyze_structure(text)
        result['post_id'] = idx
        structure_results.append(result)

    structure_df = pd.DataFrame(structure_results)
    print(f"  ✓ 完了: 平均スコア {structure_df['structure_score'].mean():.1f}/7点")

    print(f"\n[5/6] Phase 3: 問いかけ品質分析中...")
    question_results = []
    for idx, row in df_posts.iterrows():
        text = row[text_col]
        result = analyze_question(text)
        result['post_id'] = idx
        question_results.append(result)

    question_df = pd.DataFrame(question_results)
    question_rate = (question_df['has_question'].sum() / len(question_df)) * 100
    print(f"  ✓ 完了: 問いかけ率 {question_rate:.1f}%")

    # 結果統合
    print(f"\n[6/6] 結果統合中...")

    # 総合スコア計算
    combined = pd.concat([
        hook_df[['post_id', 'hook_score', 'first_line', 'has_number', 'has_company', 'is_assertive']],
        structure_df[['structure_score', 'total_chars', 'company_count', 'number_count', 'has_cta']],
        question_df[['has_question', 'question_type', 'question_depth', 'target_clarity']]
    ], axis=1)

    # Top 10 vs Bottom 10 抽出
    combined_sorted = combined.sort_values('hook_score', ascending=False)
    top_10 = combined_sorted.head(10)
    bottom_10 = combined_sorted.tail(10)

    # JSON出力用データ
    output = {
        'analysis_date': datetime.now().isoformat(),
        'total_posts': len(df_posts),
        'summary': {
            'hook_quality': {
                'avg_score': float(hook_df['hook_score'].mean()),
                'median_score': float(hook_df['hook_score'].median()),
                'max_score': int(hook_df['hook_score'].max()),
                'min_score': int(hook_df['hook_score'].min()),
                'has_number_rate': float((hook_df['has_number'].sum() / len(hook_df)) * 100),
                'has_company_rate': float((hook_df['has_company'].sum() / len(hook_df)) * 100),
                'is_assertive_rate': float((hook_df['is_assertive'].sum() / len(hook_df)) * 100)
            },
            'structure_quality': {
                'avg_score': float(structure_df['structure_score'].mean()),
                'median_score': float(structure_df['structure_score'].median()),
                'avg_chars': float(structure_df['total_chars'].mean()),
                'avg_company_count': float(structure_df['company_count'].mean()),
                'avg_number_count': float(structure_df['number_count'].mean()),
                'has_cta_rate': float((structure_df['has_cta'].sum() / len(structure_df)) * 100)
            },
            'question_quality': {
                'question_rate': float(question_rate),
                'avg_depth': float(question_df[question_df['has_question']]['question_depth'].mean()) if question_rate > 0 else 0,
                'type_distribution': question_df['question_type'].value_counts().to_dict(),
                'target_distribution': question_df['target_clarity'].value_counts().to_dict()
            }
        },
        'top_10_posts': {
            'avg_hook_score': float(top_10['hook_score'].mean()),
            'avg_structure_score': float(top_10['structure_score'].mean()),
            'avg_chars': float(top_10['total_chars'].mean()),
            'posts': top_10[['post_id', 'hook_score', 'structure_score', 'first_line']].to_dict('records')
        },
        'bottom_10_posts': {
            'avg_hook_score': float(bottom_10['hook_score'].mean()),
            'avg_structure_score': float(bottom_10['structure_score'].mean()),
            'avg_chars': float(bottom_10['total_chars'].mean()),
            'posts': bottom_10[['post_id', 'hook_score', 'structure_score', 'first_line']].to_dict('records')
        },
        'benchmark_comparison': {
            'takano_method': {
                'er_range': '4-6%',
                'char_count': 760,
                'question_ending_rate': '80%+',
                'company_mentions': 79
            },
            'user_current': {
                'er': 1.02,
                'avg_char_count': float(structure_df['total_chars'].mean()),
                'question_ending_rate': f"{question_rate:.1f}%",
                'avg_company_mentions': float(structure_df['company_count'].mean())
            }
        }
    }

    # JSON保存
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"  ✓ 完了: {OUTPUT_JSON}")

    # サマリー表示
    print("\n" + "=" * 60)
    print("分析結果サマリー")
    print("=" * 60)
    print(f"\nフック品質 (Phase 1):")
    print(f"  平均スコア: {output['summary']['hook_quality']['avg_score']:.1f}/20点")
    print(f"  数字使用率: {output['summary']['hook_quality']['has_number_rate']:.1f}%")
    print(f"  企業名使用率: {output['summary']['hook_quality']['has_company_rate']:.1f}%")
    print(f"  断定型使用率: {output['summary']['hook_quality']['is_assertive_rate']:.1f}%")

    print(f"\n構造品質 (Phase 2):")
    print(f"  平均スコア: {output['summary']['structure_quality']['avg_score']:.1f}/7点")
    print(f"  平均文字数: {output['summary']['structure_quality']['avg_chars']:.0f}字")
    print(f"  平均企業名数: {output['summary']['structure_quality']['avg_company_count']:.1f}社")
    print(f"  平均数値データ数: {output['summary']['structure_quality']['avg_number_count']:.1f}個")
    print(f"  問いかけ終結率: {output['summary']['structure_quality']['has_cta_rate']:.1f}%")

    print(f"\n問いかけ品質 (Phase 3):")
    print(f"  問いかけ率: {output['summary']['question_quality']['question_rate']:.1f}%")
    print(f"  平均深さ: {output['summary']['question_quality']['avg_depth']:.1f}/5")
    print(f"  タイプ分布: {output['summary']['question_quality']['type_distribution']}")

    print(f"\nTop 10 vs Bottom 10 比較:")
    print(f"  Top 10 フックスコア: {output['top_10_posts']['avg_hook_score']:.1f}/20")
    print(f"  Bottom 10 フックスコア: {output['bottom_10_posts']['avg_hook_score']:.1f}/20")
    print(f"  差分: {output['top_10_posts']['avg_hook_score'] - output['bottom_10_posts']['avg_hook_score']:.1f}pt")

    print(f"\nベンチマーク比較（高野氏メソッド）:")
    print(f"  ER: {output['benchmark_comparison']['user_current']['er']}% vs 4-6% (ベンチマーク)")
    print(f"  文字数: {output['benchmark_comparison']['user_current']['avg_char_count']:.0f}字 vs 760字 (ベンチマーク)")
    print(f"  問いかけ率: {output['benchmark_comparison']['user_current']['question_ending_rate']} vs 80%+ (ベンチマーク)")

    print("\n" + "=" * 60)
    print("分析完了")
    print("=" * 60)

if __name__ == "__main__":
    main()
