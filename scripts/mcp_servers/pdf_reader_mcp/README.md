# PDF Reader MCP Server

PDFファイルからテキストと画像を抽出し、Gemini Vision APIで画像を解析するMCPサーバーです。

## 機能

| ツール | 説明 |
|--------|------|
| `read_pdf` | PDFを読み込み、テキスト＋画像解析結果をMarkdown形式で出力 |
| `read_pdf_pages` | 指定したページのみを読み込み（大容量PDF対応） |
| `get_pdf_info` | PDFの基本情報（ページ数、メタデータ）を取得 |
| `extract_text_only` | テキストのみを高速抽出（画像解析なし） |

## セットアップ

### 1. 依存パッケージのインストール

```bash
cd /Users/yuichi/AIPM/aipm_v0/scripts/mcp_servers/pdf_reader_mcp
pip install -r requirements.txt
```

### 2. Gemini API Key の設定

画像解析機能を使用するには、Gemini API Keyが必要です。

**方法A: 環境変数で設定**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**方法B: 設定ファイルで設定**
```bash
mkdir -p ~/.config/pdf-reader-mcp
cat > ~/.config/pdf-reader-mcp/config.json << EOF
{
  "gemini_api_key": "your-api-key-here"
}
EOF
```

### 3. MCPサーバーとして登録

`.cursor/mcp.json` または対応するMCP設定ファイルに追加:

```json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "python",
      "args": ["-m", "pdf_reader_mcp.server"],
      "cwd": "/Users/yuichi/AIPM/aipm_v0/scripts/mcp_servers"
    }
  }
}
```

## 使用例

### 基本的な読み込み
```
PDFを読み込んで: /path/to/report.pdf
```

### ページ範囲指定
```
PDFの1〜10ページだけ読み込んで: /path/to/large-report.pdf
```

### テキストのみ抽出（高速）
```
PDFのテキストだけ抽出して: /path/to/document.pdf
```

## 注意事項

- 200ページ以上のPDFは処理に時間がかかります
- 画像解析はGemini API呼び出しが発生するため、コストに注意してください
- API Key未設定でも、テキスト抽出機能は利用可能です
