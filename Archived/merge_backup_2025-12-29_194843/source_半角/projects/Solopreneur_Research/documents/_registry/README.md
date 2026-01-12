# Person Registry

**作成日**: 2025-12-29
**バージョン**: 1.0
**総登録人数**: 50名

## 概要

Solopreneur_Researchプロジェクトの全カテゴリ（App/Newsletter/SNS）に分散している同一人物の情報を統合管理するレジストリです。

## ファイル構成

```
_registry/
├── person_registry.md       # メインレジストリ（YAML形式）
├── README.md                # このファイル
└── ../analysis/quality_scores/person_registry_stats.csv  # CSV統計データ
```

## 統計サマリー

### 登録人数
- **総登録人数**: 50名
- **3軸統合（App+Newsletter+SNS）**: 1名
  - Courtland Allen (@csallen)
- **2軸統合**: 17名
- **単一カテゴリのみ**: 32名

### Japan Relevance
- **平均スコア**: 3.75点 / 5.0点
- **算出対象**: 43名（7名はスコアなし）

### カテゴリ別内訳
- **App登録あり**: 29名
- **Newsletter登録あり**: 8名
- **SNS登録あり**: 20名

## Top 10 Persons（Presence順）

| Rank | Name | Twitter | App | NL | SNS | Total | Japan |
|------|------|---------|-----|----|----|-------|-------|
| 1 | Sam Parr | @unknown | 0 | 31 | 0 | 31 | 4.2 |
| 2 | 匿名化（複数ソロプレナー） | @na | 0 | 4 | 0 | 4 | 4.3 |
| 3 | Courtland Allen | @csallen | 1 | 1 | 1 | 3 | 4.0 |
| 4 | Pieter Levels | @levelsio | 2 | 0 | 1 | 3 | 3.9 |
| 5 | Lenny Rachitsky | @lennysan | 0 | 2 | 1 | 3 | 4.2 |
| 6 | Sebastian Röhl | @sebastianroehl | 2 | 0 | 0 | 2 | 3.8 |
| 7 | Tony Dinh | @tdinh_me | 2 | 0 | 0 | 2 | 4.3 |
| 8 | Andrey Azimov | @andreyazimov | 1 | 0 | 1 | 2 | 3.8 |
| 9 | Jon Yongfook | @yongfook | 1 | 0 | 1 | 2 | 3.15 |
| 10 | Steph Smith | @stephsmithio | 1 | 0 | 1 | 2 | 4.0 |

## 3軸統合人物（App+Newsletter+SNS）

### Courtland Allen (@csallen)
- **App**: APP_136 - Indie Hackers
- **Newsletter**: NL_CASE_P1_012 - Indie Hackers Newsletter
- **SNS**: SNS_courtland_allen
- **Japan Relevance**: 4.0
- **Known For**: Indie Hackersコミュニティ創業者、起業家コミュニティ構築

**分析コメント**: Courtland Allenは唯一の3軸統合人物。Indie Hackersというプロダクトを中心に、Newsletter、SNSの全てで存在感を持つ典型的なソロプレナーのエコシステム構築モデル。日本市場でも再現性高い。

## 2軸統合人物（注目17名）

### 主要2軸統合ケース

1. **Pieter Levels (@levelsio)**
   - App×2 (Nomad List, PhotoAI) + SNS
   - Japan: 3.9
   - 複数プロダクト × 強力なSNS発信

2. **Lenny Rachitsky (@lennysan)**
   - Newsletter×2 + SNS
   - Japan: 4.2
   - Newsletter特化型の成功モデル

3. **Ben Tossell (@bentossell)**
   - App + Newsletter
   - Japan: 4.5
   - Makerpad創業者、ノーコードコミュニティ

4. **Sam Parr (@thesamparr)**
   - Newsletter + SNS
   - Japan: 3.4
   - The Hustle創業者（$27M Exit）

## 使い方

### Person IDでの検索

```bash
# YAML registryから特定人物を検索
grep -A 20 "PERSON_CSALLEN" person_registry.md
```

### Twitter handleでの検索

```bash
# Twitter handleから人物情報を取得
grep -B 2 "@levelsio" person_registry.md
```

### CSVでの分析

```bash
# Japan relevanceでソート
sort -t',' -k8 -nr person_registry_stats.csv | head -20
```

## データ取得方法

### 自動抽出ルール

1. **App Case Studies**
   - YAMLフロントマター: `subject.name`, `subject.twitter_handle`
   - ファイル: `documents/01_App/case_studies/*.md`

2. **Newsletter Case Studies**
   - YAMLフロントマター: `founder_name`, `founder_twitter`
   - ファイル: `documents/02_Newsletter/case_studies/*.md`

3. **SNS Case Studies**
   - テキスト抽出: 基本情報テーブルから`**人物名**`, `**ハンドル**`
   - ファイル: `documents/03_SNS/**/sns_analysis.md`

### 同一人物検出ロジック

- **完全一致**: Twitter handleの正規化後の一致
- **正規化ルール**:
  - 小文字変換
  - `@`プレフィックス削除
  - 英数字とアンダースコアのみ保持

## 今後の拡張

### Phase 2: 人物情報の充実化

- [ ] `known_for`タグの自動抽出（プロダクト名、実績）
- [ ] `name_ja`の追加（日本語名）
- [ ] 国籍情報の全件補完
- [ ] 外部リンク（LinkedIn, GitHub）の追加

### Phase 3: クロスリファレンス強化

- [ ] 各ケーススタディに`person_registry_id`フィールド追加
- [ ] 逆引きインデックス（Product → Person）
- [ ] コラボレーション関係の可視化

### Phase 4: 定期更新自動化

- [ ] 新規ケーススタディ追加時の自動更新スクリプト
- [ ] Twitter handle変更の追跡
- [ ] Presenceスコアの時系列追跡

## 技術ノート

### Python依存パッケージ

```bash
# PyYAML（YAML解析）
pip install pyyaml
```

### 更新コマンド

```bash
# Person Registryの再生成
cd /path/to/Solopreneur_Research
python3 scripts/generate_person_registry.py
```

## ライセンス・クレジット

このPerson Registryは、各ケーススタディの情報を統合したメタデータです。個人情報の取り扱いには十分注意し、公開情報のみを収集しています。

---

**最終更新**: 2025-12-29
**メンテナ**: Solopreneur_Research Project Team
