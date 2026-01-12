# SNSフォルダ最適化プラン

## 現状の問題点

1. **3つのフォルダに分散**
   - `Stock/SNS_Knowledge/` - ナレッジベース（520K）
   - `Stock/programs/副業/projects/SNS/` - PMBOKプロジェクト（732K）
   - `Stock/programs/副業/projects/SNSノウハウ/` - 実践ノウハウ（1.1GB）

2. **重複と非効率**
   - プラットフォーム別フォルダが複数箇所に存在
   - どこに何があるか不明確
   - ナレッジの一元管理ができていない

## 最適化後の構造

```
Stock/
├── SNS_Knowledge/                      # 中核ナレッジベース
│   ├── README.md
│   ├── index.yaml
│   ├── _templates/
│   ├── _meta/
│   ├── X/
│   │   ├── algorithm.md
│   │   ├── best_practices.md
│   │   ├── case_studies/               # NEW: 成功事例
│   │   └── resources/                  # NEW: affiliatemanコンテンツ統合
│   ├── Instagram/
│   │   ├── algorithm.md
│   │   ├── best_practices.md
│   │   ├── case_studies/
│   │   └── resources/
│   ├── TikTok/                         # NEW: 追加
│   ├── YouTube/                        # NEW: 追加
│   ├── LinkedIn/
│   ├── Note/
│   ├── Facebook/
│   └── sources/                        # NEW: 元データ保管
│       ├── affiliateman/
│       │   ├── blog/
│       │   ├── video_transcripts/
│       │   ├── interviews/
│       │   └── zoom_consult/
│       └── あずさメソッド/
│
└── programs/副業/
    └── projects/
        └── SNS_Practice/               # 旧SNS → 改名
            ├── README.md
            ├── documents/              # PMBOK管理のみ
            │   ├── 1_initiating/
            │   ├── 2_discovery/
            │   ├── 3_planning/
            │   ├── 4_executing/
            │   ├── 5_monitoring/
            │   └── 6_closing/
            └── experiments/            # NEW: A/Bテスト・実験記録
```

## 移行ステップ

### Phase 1: SNS_Knowledgeの拡張

1. TikTok, YouTubeフォルダを追加
2. 各プラットフォームに`case_studies/`と`resources/`フォルダを追加
3. `sources/`フォルダを作成

### Phase 2: SNSノウハウコンテンツの移行

1. affiliatemanフォルダを`SNS_Knowledge/sources/affiliateman/`に移動
2. あずさメソッドを`SNS_Knowledge/sources/あずさメソッド/`に移動
3. 価値の高いコンテンツを各プラットフォームのcase_studiesやresourcesに反映

### Phase 3: SNSフォルダの整理

1. `SNS/`を`SNS_Practice/`に改名
2. プラットフォーム別フォルダを削除（SNS_Knowledgeに統合済み）
3. documentsのPMBOK構造のみ維持
4. experiments/フォルダを新設

### Phase 4: SNSノウハウフォルダの削除

1. コンテンツ移行完了を確認
2. `SNSノウハウ/`フォルダを削除

## メリット

1. **一元管理**: SNS_Knowledgeに全ナレッジが集約
2. **明確な役割分担**:
   - SNS_Knowledge: ナレッジベース（What/How）
   - SNS_Practice: プロジェクト管理・実験記録（When/Where）
3. **検索性向上**: フォルダ構造が明確化
4. **重複排除**: 1.1GB + 732K → 効率化
5. **拡張性**: 新プラットフォーム追加が容易

## 実行確認

この最適化を実行してよろしいですか？

- [ ] Phase 1のみ実行（構造準備）
- [ ] Phase 1-2を実行（コンテンツ移行まで）
- [ ] 全Phase実行（完全統合）
- [ ] カスタマイズしたい（詳細を教えてください）
