---
name: recap-reflex
version: 0.1.0
description: |
  跨 Skill 收束策略（always-on policy）。当学生学习类 Skill 接近尾声时，
  自动调用 session-recap，无需学生每次手动说「收束」。
policy: always-on
applies_to:
  - study-coach
  - exam-sprint
  - misconception-fix
  - course-onboard
triggers: []  # 非用户主动触发；由结束信号或 applies_to Skill 尾声激活
tools:
  - search
  - put_page
---

# recap-reflex — 自动收束策略

> **核心理念：** 收束不是可选项，是每次学习 session 的**默认尾声**。
> 本文件是 **policy Skill**，不单独做辅导；执行时 **委托 session-recap**。

---

## 何时自动触发（满足任一即执行）

### A. 用户结束信号

- 「好了」「今天就到这」「先这样」「晚安」「时间到了」「没有了」
- 「收束」「总结一下」— 仍走 session-recap，本 policy 不重复问要不要收束

### B. 辅导 Skill 自然结束

以下 Skill 完成 Contract 中**除写回外**的主线后，**必须**自动进入 session-recap：

- study-coach（Phase 4 计划给出后）
- exam-sprint（倒排日程给出后）
- misconception-fix（验证题完成后）
- course-onboard（骨架建完后 — 轻量 recap：下一步触发句 + 可选写 sessions）

### C. 对话即将结束

Agent 判断本次对话属于学习辅导，且将回复告别/结束时 → **先 recap 再结束**。

---

## 何时不自动触发

- 用户明确说：**「不要收束」「不用写回」「只要答案」**
- 纯闲聊、与学习无关
- 用户**刚开始**辅导（<3 轮），尚无实质内容可收束
- 已在本次对话中执行过 session-recap（同 session 不重复）

---

## 执行协议（Agent 必须遵守）

1. **不打断主线** — 先完成当前 Skill 的辅导内容
2. **过渡一句**（自然语言，不必说 policy 名称）：
   - 「我帮你收个尾，记一下明天从哪接上。」
3. **委托 session-recap** — 执行 `skills/session-recap/SKILL.md` 的 Phase 0–2（+ 可选 Phase 3）
4. **写回 brain 后方可结束对话**
5. 收束体量 ≤5 分钟阅读；**禁止**在 recap 时开新课

---

## 与 session-recap 的关系

```text
recap-reflex  = 什么时候自动收束（policy）
session-recap = 怎么收束、写什么（executor）
```

不要在本 policy 里重复 session-recap 的模板；直接按 session-recap 写回。

---

## Cursor User Rule 片段（推荐粘贴）

```
【recap-reflex】学生学习类 Skill 结束时，默认自动执行 session-recap 写回 brain，
除非用户明确拒绝。同一次对话不重复 recap。
```

---

## Anti-Patterns

- ❌ 问「要不要帮你总结一下？」— 默认直接做，用户可打断
- ❌ 收束时又讲 500 字新知识
- ❌ 跳过写回直接告别
- ❌ 每次对话开头就 recap（应在尾声）
