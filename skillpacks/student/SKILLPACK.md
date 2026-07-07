# iBrain Student Skillpack v0.1

## 包含 Skills

| Skill | 文件 | 说明 |
|-------|------|------|
| study-coach | `skills/study-coach/SKILL.md` | 深度学习教练：诊断 → 应用 → 计划 → 写回 |

## 安装

```bash
# 复制到你的 agent skills 目录
cp -r skillpacks/student/skills/study-coach /path/to/your/workspace/skills/

# 追加 resolver 触发词
cat ../../resolver/student-resolver-snippet.md >> /path/to/your/workspace/skills/RESOLVER.md
```

## 依赖

- GBrain >= 0.42
- MCP: search, query, get_page, put_page
- 可选：web 搜索 / Perplexity（Phase 2 靶向资料）
