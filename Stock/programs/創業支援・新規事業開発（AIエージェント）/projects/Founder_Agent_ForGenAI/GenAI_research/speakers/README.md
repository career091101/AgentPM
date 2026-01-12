# Speakers - 話者別インデックス

このディレクトリには、話者別に分類されたトランスクリプトへのシンボリックリンクを格納します。

## 概要

各話者のフォルダが動的に作成され、その話者が登場する全トランスクリプトへのシンボリックリンクが配置されます。

## ディレクトリ構造（例）

```
speakers/
├── [話者名A]/
│   ├── yw3QQxX9FZQ.md -> ../../sources/Founder_Agent_Videos/yw3QQxX9FZQ.md
│   └── 8_liatgLkLc.md -> ../../sources/Founder_Agent_Videos/8_liatgLkLc.md
├── [話者名B]/
│   └── ...
└── README.md (this file)
```

## 使用方法

### 特定の話者のトランスクリプトを検索
```bash
cd speakers/[話者名]/
ls -lah  # その話者の全トランスクリプトを表示
```

### 話者一覧を取得
```bash
cd speakers/
ls -d */  # 全話者のフォルダ一覧
```

## 更新方法

T005-5タスクで自動分類スクリプト（`scripts/t005_5_classify_transcripts.py`）により、メタデータのspeakerフィールドに基づいてサブディレクトリとシンボリックリンクが自動生成されます。

## 話者名の取得方法

話者名はLLMによるトランスクリプト分析で抽出されます：
- トランスクリプト内の自己紹介を検出
- 話者の名前を推測
- メタデータのspeakerフィールドに記録

---

**管理者**: Founder Agent System
**最終更新**: 2025-12-30
