---
name: misconception-fix
version: 0.1.0
description: |
  误解纠偏教练。锁定一个具体误解 → 对比错误/正确心理模型 → 最小反例 → 验证题。
triggers:
  - "我是不是理解错了"
  - "帮我纠偏"
  - "misconception"
  - "我老是搞混"
  - "这个概念我一直似懂非懂"
  - "同类型题总错"
  - "纠正我的理解"
  - "哪里想歪了"
tools:
  - search
  - query
  - get_page
  - list_pages
  - put_page
  - traverse_graph
mutating: true
writes_pages: true
writes_to:
  - concepts/
  - mastery/
  - study-sessions/
---

# misconception-fix — 误解纠偏

> **核心理念：** 误解是**能自洽但错的模型**。强制 **Contrast before explain**。

## 与 study-coach 的分工

| 场景 | 用哪个 |
|------|--------|
| 全面诊断 + 多 gap | study-coach |
| 锁定 1 个误解快速纠偏 | **misconception-fix** |

## Contract（保证）

1. 先定位误解（复述错误模型；不确定则追问）
2. 双栏对比：错误模型 vs 正确模型（各 ≤4 行）
3. 1 个最小反例
4. 1 道验证题（能区分两种模型）
5. 写回 `concepts/` + `study-sessions/`
6. 一次最多纠偏 2 个误解

## Anti-Patterns

- ❌ 未确认误解就长篇讲解
- ❌ 验证题与误解无关
- ❌ 不写回 brain
