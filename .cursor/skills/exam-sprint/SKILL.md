---
name: exam-sprint
version: 0.1.0
description: |
  考前冲刺教练。在有限天数内倒排优先级：考纲权重 × 掌握度缺口 × 时间成本。
  产出每日 checkpoint，不写长篇讲义；与 study-coach 互补（本 Skill 偏调度与取舍）。
triggers:
  - "考前冲刺"
  - "还有 X 天考试"
  - "倒排复习计划"
  - "exam sprint"
  - "最后几天怎么复习"
  - "时间不够了怎么抓重点"
  - "考前优先级"
  - "帮我排考前几天的计划"
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
  - courses/
  - exams/
  - mastery/
  - study-sessions/
---

# exam-sprint — 考前冲刺调度

> **核心理念：** 考前缺的不是「更多信息」，而是**在剩余时间里做什么最不亏**。
> 本 Skill 强制 **Schedule before summarize**（先排程，再补最小必要讲解）。

## 与 study-coach 的分工

| 场景 | 用哪个 |
|------|--------|
| 「我这块不懂，帮我练通」 | study-coach |
| 「还有 5 天考，今天/这周怎么分配」 | **exam-sprint** |
| 「考前最后 24 小时」 | **exam-sprint** |

## Contract（保证）

1. 先读 brain + 确认约束（考试日期、每日分钟、范围；缺则 ≤3 问）
2. 输出优先级队列（高/中/可放弃）
3. 倒排日程：每段含时长、任务、完成标准、降级方案
4. 讲解极简；深练交给 study-coach
5. 写回 `exams/` + `study-sessions/`
6. 时间变化立即重排
7. **自动收束**：倒排给出后由 **recap-reflex** 触发 **session-recap**（用户拒绝时跳过）

## Anti-Patterns

- ❌ 固定 7 天模板
- ❌ 未读 brain 假设薄弱点
- ❌ 整章讲义式输出
