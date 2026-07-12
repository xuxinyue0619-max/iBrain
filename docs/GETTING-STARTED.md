# iBrain 快速上手

## 1. 确保 GBrain 可用

```bash
gbrain --version
gbrain doctor
```

若 capture 失败，先配置 embedding：

```bash
# 选项 A：OpenAI
gbrain config set openai_api_key sk-...

# 选项 B：本地 Ollama
ollama serve
ollama pull nomic-embed-text
```

## 2. 安装 study-coach Skill

```bash
cd ~/Documents/iBrain
cp -r skillpacks/student/skills/study-coach ~/Documents/gbrain/skills/
```

或在 Cursor 项目根目录：

```bash
mkdir -p .cursor/skills
cp -r skillpacks/student/skills/study-coach .cursor/skills/
```

## 3. 接入 Cursor MCP

`~/.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "gbrain": {
      "command": "/Users/xxy/.local/bin/gbrain",
      "args": ["serve"]
    }
  }
}
```

重启 Cursor。

## 4. 添加 User Rule（推荐）

```
你连接了 GBrain。学习相关问题优先走 study-coach：
先查 brain 掌握度，再回答；禁止未诊断就给长篇讲义。

【recap-reflex】学生学习类 Skill 结束时，默认自动执行 session-recap 写回 brain，
除非用户明确说「不要收束/不用写回」。同一次对话不重复 recap。
```

## 5. 第一次测试

```bash
gbrain capture "测试：线性代数特征值 — 我会算但不会解释几何意义"
```

在 Cursor 说：

> 用 study-coach 帮我诊断特征值掌握度，并给 40 分钟复习计划
