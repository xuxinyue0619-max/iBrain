---
name: session-recap
version: 0.1.0
description: |
  学习 session 收束教练。5 分钟内总结本次学了什么、还卡什么、明天第一步；
  写回 study-sessions/ 并可选更新 mastery/。解决跨天/中断后「接不上」的问题。
triggers:
  - "收束今天"
  - "session recap"
  - "总结一下今天"
  - "明天从哪继续"
  - "下次怎么接"
  - "学习收束"
  - "wrap up"
  - "今天学到哪了"
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
  - study-sessions/
  - mastery/
---

# session-recap — 学习收束

> **核心理念：** 学习价值的一半在「下次能否接着上」。
> 本 Skill 强制 **Close the loop**（闭环写回，一步可续）。

---

## 当前体系的不足（本 Skill 要补的）

| 缺口 | 现状 | session-recap 补什么 |
|------|------|----------------------|
| 跨天断层 | 外出几天无 progress，brain 有旧页但无「接入口」 | 产出明确的 **tomorrow_first_step** |
| 写回格式不一 | study-coach 等只说「写 study-sessions/」，无统一字段 | 固定 frontmatter + 短正文模板 |
| 收束被跳过 | 辅导结束常直接结束对话 | 可独立触发，也可被其他 Skill 尾声调用 |
| mastery 不更新 | session 记了，掌握度地图滞后 | 可选 PATCH `mastery/` 1–3 行 |
| 无 session 链 | 各次辅导互不相指 | `continues_from` 指向上次 session |

---

## 与 study-coach 的分工

| 场景 | 用哪个 |
|------|--------|
| 完整辅导（诊断+练习+计划） | study-coach |
| **只收束 / 要接上次 / 睡前 5 分钟总结** | **session-recap** |
| 其他 Skill 尾声 | 可说「用 session-recap 收束」或 Agent 自动套用本 Skill Phase 2–4 |

---

## Contract（保证）

1. **先读近期 brain**（最近 3 条 `study-sessions/` + 相关 `mastery/`）
2. **对照当次对话**（若无当次辅导，基于 brain + 用户一句口述）
3. **输出 ≤5 分钟体量**：今日要点、仍卡、明天第一步（可检验）
4. **写回** `study-sessions/YYYY-MM-DD-recap-<slug>.md`（用下方模板）
5. **可选**更新 `mastery/<course>.md` 中 1–3 个主题状态
6. **禁止**展开新知识点教学（收束不是开新课）

---

## Phase 0 — 读取

`search` / `list_pages` / `get_page`：

- `study-sessions/` 最近 3 条
- `mastery/` 当前课程
- `courses/` 上下文（若有）

若 brain 几乎为空 → 只问：「今天学了什么？明天想先碰哪一块？」（≤2 问）

---

## Phase 1 — 收束摘要（给学生看）

自然语言，建议含四块（可合并，不必标题僵化）：

1. **今日完成**（动词+对象，≤3 条）
2. **仍卡 / 待确认**（≤2 条，无则写「无」）
3. **掌握度变化**（若有：如 shaky→solid 或仍 gap）
4. **明天第一步**（一步、可检验、含预估分钟）

**明天第一步格式：**

```text
[明天] <动作> <对象> — 完成标准：<怎样算做完> — 约 <N> 分钟
```

---

## Phase 2 — 写回 Brain（必做）

路径：`study-sessions/YYYY-MM-DD-recap-<topic-slug>.md`

```markdown
---
type: study-session-recap
date: YYYY-MM-DD
course: courses/<slug> | unknown
duration_min: <N>
continues_from: study-sessions/<previous-slug> | none
tomorrow_first_step: "<一步动作>"
mastery_delta:
  - topic: "<主题>"
    from: shaky | gap | unknown
    to: solid | shaky | gap
---

## 今日完成
- ...

## 仍卡
- ...

## 明天第一步
...

## 备注
（可选：学生偏好、时间约束）
```

正文保持精简；**禁止**复制 Skill 或 EXAMPLES 全文。

---

## Phase 3 — 更新 mastery（可选）

仅当本次有明确掌握度变化时，PATCH `mastery/<course>.md` 对应行。  
无变化则跳过，不凑更新。

---



---

## 自动收束（配合 recap-reflex）

当 **recap-reflex** policy 激活时，本 Skill **无需用户说「session recap」** 即应执行。

自动触发后仍走 Phase 0–2；向用户呈现时合并为简短收尾，不必声明「正在执行 policy」。

## 被其他 Skill 调用

study-coach / exam-sprint / misconception-fix 结束时，Agent 可：

- 用户说「收束」→ 切 session-recap
- 或自动执行本 Skill Phase 1–2（不重复长篇辅导）

---

## Anti-Patterns（禁止）

- ❌ 收束时又开始讲新课
- ❌ 明天第一步模糊（「继续复习生物」）
- ❌ 不写回 brain
- ❌ 忽略已有 study-sessions 历史，从零编造
- ❌ 固定六段式回复

---

## 示例触发

```
用 session-recap：今天 AP 生物 Unit 3 练了 25 分钟，光合还混，明天只有 20 分钟。
```

```
session recap — 我两天没学了，帮我从 brain 接上，告诉我明天第一步。
```
