---
name: course-onboard
version: 0.1.0
description: |
  新课程/新学期 onboarding。建立 courses/、mastery/、exams/ 骨架，为其他 Skill 提供上下文。
triggers:
  - "新学期开始了"
  - "加一门新课"
  - "course onboard"
  - "帮我建课程档案"
  - "导入这门课"
  - "课程 onboarding"
  - "初始化学习档案"
  - "我选了新课"
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
  - mastery/
  - exams/
  - concepts/
  - assignments/
---

# course-onboard — 课程建档

> **核心理念：** 先建档，再复习。强制 **Structure before study**。

## Contract（保证）

1. 检查 brain 是否已有该课（避免重复）
2. 收集最小信息（≤5 问）
3. 创建 `courses/` + `mastery/` 骨架；有考试日期则建 `exams/`
4. 可选指引 `gbrain import`
5. 给出 study-coach / exam-sprint 下一步触发句

## 最小信息集

- 课程名（必填）
- 学期/学年（推荐）
- 考试/ddl 日期（推荐）
- 笔记路径（可选）

## Anti-Patterns

- ❌ 不查重就新建
- ❌ onboarding 变考纲讲义
- ❌ 要求一次填完所有字段
