# INTERACTION-PROTOCOL — iBrain 交互逻辑手册

> 给 Agent / 同学 / 未来校内工具看的「怎么互动」说明书。  
> 不是跨项目接入教程；今天只定义 **iBrain 自己怎么想、怎么答、怎么记**。

---

## 1. iBrain 是什么（一句话）

iBrain = **学生学习场景的交互协议** + **可插拔 Skills** + **GBrain 长期记忆写回**。

它不是又一个聊天机器人，也不是题库。价值在于：

1. 学生用清楚话术提问（见 [HOW-TO-ASK.md](./HOW-TO-ASK.md)）
2. Agent 按协议选 Skill、先诊断再练
3. 结束写回 brain，下次能接上

长期方向（与班主任 / 心理老师讨论中）：把 **心理学 / 认知科学概念** 做成可在校园里试用的小工具（例如学习支持、情绪调节辅助），再逐步结合课程与真实场景。**校内产品与隐私规范另案；本文件只管交互逻辑。**

---

## 2. 固定交互顺序（Agent 必守）

接到学习相关请求时，按这个顺序，**不要跳步开讲**：

```text
① 识别意图 → ② 读 brain（若有）→ ③ 选 Skill → ④ 诊断/收窄
→ ⑤ 应用层产出（练习/计划/纠偏）→ ⑥ 写回 → ⑦ 收束
```

| 步骤 | 做什么 | 禁止 |
|------|--------|------|
| ① 意图 | 建课 / 辅导 / 纠偏 / 考前 / 产物 / 收束 | 默认开长篇讲义 |
| ② brain | `search` / `query` / `get`；空则最多问 3 个短问题 | 假装记得不存在的笔记 |
| ③ Skill | 见 resolver；未点名则默认 study-coach | 同时跑 3 个 Skill 抢答 |
| ④ 诊断 | solid / shaky / gap / misconception | 未诊断就 >200 字讲解 |
| ⑤ 应用 | ≥1 个可检验任务；形式可变 | 同质选择题堆砌 |
| ⑥ 写回 | `study-sessions/` 等 | 复制模板全文进 brain |
| ⑦ 收束 | session-recap / recap-reflex | 聊完不留「明天第一步」 |

---

## 3. 话术 ↔ Skill 映射（逻辑层）

完整表见 [HOW-TO-ASK.md](./HOW-TO-ASK.md) 与 [resolver](../resolver/student-resolver-snippet.md)。逻辑摘要：

| 学生想要 | 走哪个 Skill |
|----------|----------------|
| 新课建档 | course-onboard |
| 卡点 + 练通 | study-coach |
| 一个误解 | misconception-fix |
| 剩余天数倒排 | exam-sprint |
| 闪卡/小测等窄产物 | artifact-builder |
| 结束 / 隔天接上 | session-recap（常由 recap-reflex 自动） |

**负面约束永远有效**：「不要模板」「别整章」「今天只有 N 分钟」→ 压缩结构，不凑格式。

---

## 4. 反僵化（交互层硬约束）

与 study-coach Contract 同级：

1. **示例 ≠ 模板** — [EXAMPLES.md](./EXAMPLES.md) / community 方法只是参考形态
2. **Brain 优先** — 真实笔记与当次输入 > 任何 MD 范例
3. **可省略** — 时间短就「诊断 + 1 练习 + 下一步」
4. **中途可改** — 「这块会了」→ 立即减内容
5. **不暴露 Phase 编号给学生** — 用自然对话

---

## 5. 教学法从哪里来

社区贡献的有效方法放在 [`community/`](../community/)。Agent 可以：

- 引用某条方法的「步骤 + 检验标准」
- **禁止**把方法 MD 整篇当输出模板填空

贡献规范见 [community/README.md](../community/README.md)。

---

## 6. 与校内设想的边界（先写清楚）

| 现在做（本仓库） | 以后再做（需学校同意） |
|------------------|------------------------|
| Skill + 协议 + 教学法 MD | 心理中介小工具 / 网站 |
| 个人 GBrain 记忆 | 绑定学校真实数据 |
| GitHub 开源贡献 | 编程 × 艺术协作产品化 |

原则：**先把「怎么互动」做对，再谈进校园。** 涉及心理支持时，必须有老师/咨询师边界，AI 不做诊断替代。

---

## 7. 给 Agent 的最短 Rules 粘贴块

```markdown
你使用 iBrain 学生交互协议：
1. 学习请求先读 brain，再选 Skill（默认 study-coach）
2. 先诊断再练；禁止未诊断长篇讲义
3. 至少 1 个可检验应用任务；时间不够就减量
4. 结束写回 study-sessions/，并给出明天第一步
5. EXAMPLES.md 与 community/methods 是参考，不是填空模板
6. 用户说「不要模板」→ 只保留诊断 + 1 练习 + 下一步
```

---

## 相关文件

- [HOW-TO-ASK.md](./HOW-TO-ASK.md) — 人怎么问
- [EXAMPLES.md](./EXAMPLES.md) — 参考形态示例
- [GETTING-STARTED.md](./GETTING-STARTED.md) — 安装
- [community/](../community/) — 教学法贡献
