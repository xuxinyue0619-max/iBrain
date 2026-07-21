# SKILL-ABSTRACTS — Skill 摘要索引

> 每个 Skill 的「名片」。详细规则仍在各 `SKILL.md`。  
> 新 Skill 时：先写 Abstract → 更新本表 → 在 [DEV-DIARY](./DEV-DIARY.md) 记一条。

设计立场（贯穿全部 Skill）：

1. **客观** — 输出要可检验（计划、练习、纠偏、收束），不是漂亮的资料拼盘  
2. **反僵化** — 参考形态 ≠ 填空模板  
3. **三面向** — 帮学生执行 / 帮老师（或贡献者）沉淀有效教法 / 帮提问者问对问题  

---

## 摘要一览

| Skill | 一句话 | 主要帮谁 |
|-------|--------|----------|
| [study-coach](../skillpacks/student/skills/study-coach/SKILL.md) | 诊断卡点 → 应用练习 → 可执行计划 → 写回 | 学生 |
| [exam-sprint](../skillpacks/student/skills/exam-sprint/SKILL.md) | 按剩余天数倒排，每日 checkpoint | 学生 |
| [misconception-fix](../skillpacks/student/skills/misconception-fix/SKILL.md) | 一次只纠一个稳定误解 | 学生 |
| [course-onboard](../skillpacks/student/skills/course-onboard/SKILL.md) | 新课建档，不急着讲内容 | 学生 |
| [session-recap](../skillpacks/student/skills/session-recap/SKILL.md) | 收束 + 明天第一步 | 学生 |
| [recap-reflex](../skillpacks/student/skills/recap-reflex/SKILL.md) | 学习结束自动收束策略 | 学生 / Agent |
| [artifact-builder](../skillpacks/student/skills/artifact-builder/SKILL.md) | 窄产物：闪卡 / 小测 / 图，非整 App | 学生 |
| — | 有效提问 | 提问者 → 见 [HOW-TO-ASK](./HOW-TO-ASK.md) |
| — | 有效教法贡献 | 老师 / 同学 → 见 [community/](../community/) |
| — | 交互逻辑 | Agent / 协作者 → 见 [INTERACTION-PROTOCOL](./INTERACTION-PROTOCOL.md) |

---

## study-coach

**帮谁：** 日常觉得「AI 讲了一堆但练不通」的学生。  
**客观问题：** 从「知道约 70–80%」到「能口述 / 能做迁移题 / 有今日计划」。  
**不做：** 未诊断长篇讲义；复制 EXAMPLES 模板。  
**触发：** `用 study-coach：<科目> + <卡点> + <时间>`

## exam-sprint

**帮谁：** 考前时间紧、需要抓重点的学生。  
**客观问题：** 有倒排表 + 每日可检验 checkpoint，而不是「再看一遍书」。  
**不做：** 假装能覆盖全书。  
**触发：** `用 exam-sprint：还有 X 天，每天 Y 分钟`

## misconception-fix

**帮谁：** 卡在「我是不是理解错了」的学生。  
**客观问题：** 错误模型 vs 正确模型对比 + 至少 1 道验证题。  
**不做：** 一次纠三个误解。  
**触发：** `用 misconception-fix：…`

## course-onboard

**帮谁：** 新学期 / 新课要建档案的学生。  
**客观问题：** courses/ + mastery/ 骨架就绪，可被后续 Skill 读取。  
**不做：** 建档时开整章辅导。  
**触发：** `用 course-onboard：…`

## session-recap / recap-reflex

**帮谁：** 需要隔天接上的学生；需要默认收束的 Agent。  
**客观问题：** 今日摘要 + **明天第一步** 写回 brain。  
**不做：** 收束时再开新大课。  
**触发：** 明确「收束」或学习 Skill 尾声自动。

## artifact-builder

**帮谁：** 要「可带走的一小份材料」的学生。  
**客观问题：** 闪卡 / 小测 / 因果图等窄产物，20–40 分钟可做完。  
**不做：** 一上来做完整复习 App。  
**触发：** `用 artifact-builder：…`

---

## 文档型「能力」（不是 Skill，但算产品的一部分）

| 文档 | 客观作用 |
|------|----------|
| HOW-TO-ASK | 教会**如何有效提问** |
| INTERACTION-PROTOCOL | 规定 Agent **如何客观互动** |
| community/ | 沉淀老师/同学的**有效教法** |
| DEV-DIARY | 记录作者**真实进度与动机** |

---

## 更新清单（给未来的 Agent）

你要求新 Skill 时，请帮作者完成：

1. `SKILL.md` 内 `## Abstract`（5–8 行）  
2. 本文件增加一节 + 更新一览表  
3. `DEV-DIARY.md` 增加当天条目  
4. 如需：更新 `SKILLPACK.md` / resolver / README 表  
