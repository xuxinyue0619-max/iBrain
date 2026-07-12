# Student Resolver 片段

将以下内容追加到你的 agent `RESOLVER.md`（或 Cursor User Rules）：

## 学生学习 Skills

| Trigger | Skill |
|---------|-------|
| "新学期", "加一门新课", "建课程档案", "course onboard" | `skills/course-onboard/SKILL.md` |
| "帮我复习", "我卡在这个知识点", "怎么融会贯通" | `skills/study-coach/SKILL.md` |
| "出几道题练练", "针对性练习", "深度复习", "study coach" | `skills/study-coach/SKILL.md` |
| "制定学习计划", "今天只有 X 分钟"（非纯倒排） | `skills/study-coach/SKILL.md` |
| "考前冲刺", "还有 X 天考试", "倒排复习", "exam sprint" | `skills/exam-sprint/SKILL.md` |
| "我是不是理解错了", "帮我纠偏", "老是搞混", "misconception" | `skills/misconception-fix/SKILL.md` |
| "帮我诊断掌握度", "我不只是想知道定义" | `skills/study-coach/SKILL.md` |
| "收束今天", "session recap", "明天从哪继续", "总结今天" | `skills/session-recap/SKILL.md` |

### 路由优先级（冲突时）

0. **recap-reflex**（always-on policy）— 学习 Skill 尾声自动委托 session-recap；不抢开场路由
1. **course-onboard** — 用户明确要「建课/新学期」
2. **session-recap** — 用户明确要「收束/接上/明天第一步」（不新开辅导）
3. **exam-sprint** — 用户强调剩余天数 + 抓重点/倒排
4. **misconception-fix** — 用户锁定 1 个具体误解
5. **study-coach** — 默认深度学习辅导
