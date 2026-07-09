# iBrain Student Skillpack v0.2

## 包含 Skills

| Skill | 文件 | 说明 |
|-------|------|------|
| study-coach | `skills/study-coach/SKILL.md` | 深度学习教练：诊断 → 应用 → 计划 → 写回 |
| exam-sprint | `skills/exam-sprint/SKILL.md` | 考前冲刺：倒排优先级 + 每日 checkpoint |
| misconception-fix | `skills/misconception-fix/SKILL.md` | 误解纠偏：错误/正确模型对比 + 验证题 |
| course-onboard | `skills/course-onboard/SKILL.md` | 新课程建档：courses/ + mastery/ 骨架 |

## 推荐工作流

```text
course-onboard（新学期/新课）
    ↓
study-coach（日常深度练习）
    ↓
misconception-fix（卡在一个具体误解时）
    ↓
exam-sprint（考前倒排）
```

## 安装

```bash
cd ~/Documents/iBrain

# 复制全部 skills 到 gbrain
for s in study-coach exam-sprint misconception-fix course-onboard; do
  cp -r "skillpacks/student/skills/$s" ~/Documents/gbrain/skills/
done

# 或复制到 Cursor 项目（本仓库已含 .cursor/skills/）
cp -r .cursor/skills/* .cursor/skills/  # 已在仓库内则跳过
```

一键同步脚本：`scripts/sync-skills.sh`

## Resolver

将 [student-resolver-snippet.md](../../resolver/student-resolver-snippet.md) 追加到你的 `RESOLVER.md` 或 Cursor User Rules。

## 依赖

- GBrain >= 0.42
- MCP: search, query, get_page, put_page
- 可选：web 搜索（study-coach Phase 2）
