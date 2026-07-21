# iBrain

> 基于 [GBrain](https://github.com/garrytan/gbrain) 的**场景化 AI 记忆与学习助手**。
> 仓库：[github.com/xuxinyue0619-max/iBrain](https://github.com/xuxinyue0619-max/iBrain)

第一个垂直场景：**Student Profile（学生版）** —— 不只「讲知识点」，而是**诊断、应用、融会贯通**。

长期方向：结合心理学 / 认知科学概念，做成真正帮得到学生的小工具；校内落地需与老师协作。今天先把 **交互协议** 与 **教学法贡献区** 做好。

---

## Student Skills（v0.3）

| Skill | 用途 |
|-------|------|
| [course-onboard](skillpacks/student/skills/course-onboard/SKILL.md) | 新学期/新课建档 |
| [study-coach](skillpacks/student/skills/study-coach/SKILL.md) | 日常深度辅导 |
| [misconception-fix](skillpacks/student/skills/misconception-fix/SKILL.md) | 单点误解纠偏 |
| [exam-sprint](skillpacks/student/skills/exam-sprint/SKILL.md) | 考前倒排冲刺 |
| [session-recap](skillpacks/student/skills/session-recap/SKILL.md) | 收束 + 明天第一步 |
| [artifact-builder](skillpacks/student/skills/artifact-builder/SKILL.md) | 闪卡 / 小测 / 窄产物 |
| recap-reflex | 自动收束策略（学习结束默认写回） |

- 使用示例（**参考形态，非固定模板**）：[docs/EXAMPLES.md](docs/EXAMPLES.md)
- 怎样提问：[docs/HOW-TO-ASK.md](docs/HOW-TO-ASK.md)
- 交互逻辑手册：[docs/INTERACTION-PROTOCOL.md](docs/INTERACTION-PROTOCOL.md)
- 社区教学法贡献：[community/](community/)
- 一键同步到 gbrain：`bash scripts/sync-skills.sh`

---

## 桌面助手

| 版本 | 启动 |
|------|------|
| **Pocket v2**（推荐） | 双击桌面 **iBrain Pocket v2.command** |
| v1 话术生成器 | 双击 **iBrain助手.command** |

```bash
bash ~/Documents/iBrain/apps/desktop-assistant/launch_pocket_v2.command
```

见 [apps/desktop-assistant/README.md](apps/desktop-assistant/README.md)。

## 快速开始

见 [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md)。

在 Cursor 试：

> 用 study-coach：特征值我只会算不懂几何意义，期中考 5 天后，今天 45 分钟，不要按模板回答。

---

## 路线图

见 [ROADMAP.md](ROADMAP.md)。当前 **v0.3.1** — 交互协议 + 社区教学法贡献区。
