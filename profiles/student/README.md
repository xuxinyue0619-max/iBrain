# Student Profile（学生场景）

iBrain 的第一个垂直 Profile。目标：让 AI 辅导**针对个人掌握度**，而非泛化讲义。

## 推荐 Brain 目录结构

```
brain-repo/
├── courses/           # 课程页（syllabus、老师、ddl）
│   └── linear-algebra-2026-spring.md
├── concepts/          # 知识点页（定义、你的理解、链接）
│   └── eigenvalues.md
├── assignments/       # 作业与提交记录
├── exams/             # 考试范围、成绩、反思
├── mastery/           # 掌握度地图（study-coach 维护）
│   └── linear-algebra.md
├── study-sessions/    # 每次 AI 辅导记录
│   └── 2026-07-07-eigenvalues.md
└── resources/         # 靶向资料（视频/文章 + 看哪一段）
    └── eigenvalues-visual.md
```

## 学生 Profile 页（建议创建）

路径：`mastery/_student-profile.md`

```markdown
---
type: student-profile
updated: 2026-07-07
---

## 基本信息
- 年级/专业：
- 当前课程：

## 学习偏好
- 讲解深度：minimal / standard / deep
- 单次 session 时长上限：40 分钟

## 当前压力
- 最近 ddl：
- 自评精力：1-10
```

## 与 study-coach 的配合

1. 导入现有笔记 → `gbrain import ~/notes/`
2. 创建 `courses/` 和 `mastery/` 页面
3. 在 Cursor Rules 加入 brain-first protocol
4. 触发：`帮我复习 XX，我卡在 YY`

## 未来 Schema Pack（v0.2）

计划用 GBrain schema 声明类型：

- `course`, `assignment`, `exam`, `concept`, `mastery-map`

见 [schema-hints.yaml](./schema-hints.yaml)。
