# iBrain Desktop Assistant

macOS 桌面小助手：一点开即可按 **Student Skills** 生成正确话术，并预读 **GBrain** 记忆，再一键打开 Cursor 粘贴。

## 启动

```bash
# 终端
bash ~/Documents/iBrain/apps/desktop-assistant/launch.command

# 或双击桌面上的「iBrain助手.command」
```

## 按钮对应 Skill

| 按钮 | Skill |
|------|--------|
| 今日安排 / 接上 | session-recap + study-coach |
| 深度辅导 | study-coach |
| 考前冲刺 | exam-sprint |
| 误解纠偏 | misconception-fix |
| 新课建档 | course-onboard |
| 收束今天 | session-recap |

自动收束策略仍由 Cursor 内的 **recap-reflex** User Rule 负责。

## 依赖

- Python 3 + tkinter（macOS 自带）
- `gbrain` 在 `~/.local/bin`
- Cursor.app
