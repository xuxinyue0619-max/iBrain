#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iBrain Desktop Assistant — macOS mini launcher
Wires GBrain memory + iBrain student skills into a one-click desk companion.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path
from tkinter import (
    BOTH,
    END,
    LEFT,
    RIGHT,
    TOP,
    WORD,
    Button,
    Entry,
    Frame,
    Label,
    StringVar,
    Text,
    Tk,
    X,
    Y,
    messagebox,
)

# Paths
HOME = Path.home()
IBRAIN = Path(os.environ.get("IBRAIN", HOME / "Documents" / "iBrain"))
GBRAIN_BIN = HOME / ".local" / "bin" / "gbrain"
PATH_EXTRA = f"{HOME / '.local' / 'bin'}:{HOME / '.bun' / 'bin'}"

SKILL_PROMPTS = {
    "today": {
        "title": "今日安排 / 接上",
        "skill": "session-recap + study-coach",
        "hint": "先读 brain，再给今天可执行计划（默认短）",
        "template": (
            "用 session-recap：我{gap_day}没连上学习，从 brain 接上；"
            "若今天只想安排，不要开新课。然后用 study-coach 只给今天 {minutes} 分钟的可执行计划，"
            "基于 mastery / study-sessions，别整章讲义。科目偏好：{topic}"
        ),
    },
    "study": {
        "title": "深度辅导",
        "skill": "study-coach",
        "hint": "诊断 → 应用练习 → 写回",
        "template": (
            "用 study-coach：{topic}，我卡在：{block}。"
            "今天 {minutes} 分钟，别重讲整章，不要固定模板。"
            "先查 brain 掌握度再诊断；结束用 session-recap 收束。"
        ),
    },
    "exam": {
        "title": "考前冲刺",
        "skill": "exam-sprint",
        "hint": "倒排优先级 + checkpoint",
        "template": (
            "用 exam-sprint：{topic} 还有 {days} 天考试，每天大约 {minutes} 分钟。"
            "最虚的是：{block}。先查 brain 的 exams/mastery，再倒排；深练交给 study-coach。"
        ),
    },
    "fix": {
        "title": "误解纠偏",
        "skill": "misconception-fix",
        "hint": "错误模型 vs 正确模型 + 1 道验证",
        "template": (
            "用 misconception-fix：关于 {topic}，我总以为 {block}。"
            "帮我纠偏，{minutes} 分钟内专注 1 个误解；结束后自动收束写回。"
        ),
    },
    "onboard": {
        "title": "新课建档",
        "skill": "course-onboard",
        "hint": "courses/ + mastery/ 骨架",
        "template": (
            "用 course-onboard：我选了 {topic}。"
            "请检查 brain 是否已有该课，再建 courses/ 与 mastery/ 骨架。"
            "补充信息：{block}。建完给下一步 study-coach / exam-sprint 触发句。"
        ),
    },
    "recap": {
        "title": "收束今天",
        "skill": "session-recap",
        "hint": "明日第一步 + 写回 brain",
        "template": (
            "用 session-recap：今天练了 {topic}；还卡：{block}；"
            "明天大约只有 {minutes} 分钟。不要学新内容，只收束写回 brain。"
        ),
    },
}


def env_with_path() -> dict:
    env = os.environ.copy()
    env["PATH"] = PATH_EXTRA + ":" + env.get("PATH", "")
    return env


def run_gbrain(*args: str, timeout: int = 25) -> tuple[bool, str]:
    bin_path = GBRAIN_BIN if GBRAIN_BIN.exists() else shutil.which("gbrain")
    if not bin_path:
        return False, "找不到 gbrain。请确认已安装并在 PATH 中（~/.local/bin/gbrain）。"
    try:
        proc = subprocess.run(
            [str(bin_path), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env_with_path(),
        )
        out = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode == 0, out.strip() or "(无输出)"
    except subprocess.TimeoutExpired:
        return False, "gbrain 超时（可能 embedding/网络卡住）。"
    except Exception as e:
        return False, f"运行失败：{e}"


def clipboard(text: str) -> None:
    subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=False)


def open_cursor() -> None:
    # Open iBrain project in Cursor so Agent can see skills
    subprocess.Popen(
        ["open", "-a", "Cursor", str(IBRAIN)],
        env=env_with_path(),
    )


def open_howto() -> None:
    path = IBRAIN / "docs" / "HOW-TO-ASK.md"
    if path.exists():
        subprocess.Popen(["open", "-a", "Cursor", str(path)])
    else:
        messagebox.showinfo("提示", f"找不到 {path}")


class AssistantApp:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("iBrain 学习助手")
        self.root.geometry("720x640")
        self.root.minsize(640, 560)

        self.topic = StringVar(value="（科目/单元，如 AP 生物 Unit 3）")
        self.block = StringVar(value="（卡点，如：串不起来 / 总以为氧气是…）")
        self.minutes = StringVar(value="25")
        self.days = StringVar(value="5")
        self.gap_day = StringVar(value="隔了两天")
        self.current_mode = "today"
        self.brain_cache = ""

        self._build()
        self.refresh_brain(silent=True)

    def _build(self) -> None:
        header = Frame(self.root, padx=14, pady=10)
        header.pack(fill=X)
        Label(
            header,
            text="iBrain 学习助手",
            font=("Helvetica", 18, "bold"),
        ).pack(anchor="w")
        Label(
            header,
            text="GBrain 记忆 + Student Skills · 点按钮 → 生成话术 → 复制/打开 Cursor",
            font=("Helvetica", 11),
            fg="#555",
        ).pack(anchor="w")

        form = Frame(self.root, padx=14, pady=6)
        form.pack(fill=X)
        self._row(form, "科目 / 单元", self.topic)
        self._row(form, "卡点 / 补充", self.block)
        row2 = Frame(form)
        row2.pack(fill=X, pady=3)
        Label(row2, text="今天分钟", width=12, anchor="w").pack(side=LEFT)
        Entry(row2, textvariable=self.minutes, width=8).pack(side=LEFT)
        Label(row2, text="  考前天数", width=10, anchor="w").pack(side=LEFT)
        Entry(row2, textvariable=self.days, width=6).pack(side=LEFT)
        Label(row2, text="  间隔描述", width=10, anchor="w").pack(side=LEFT)
        Entry(row2, textvariable=self.gap_day, width=14).pack(side=LEFT)

        btns = Frame(self.root, padx=14, pady=8)
        btns.pack(fill=X)
        for key in ("today", "study", "exam", "fix", "onboard", "recap"):
            meta = SKILL_PROMPTS[key]
            Button(
                btns,
                text=meta["title"],
                width=12,
                command=lambda k=key: self.select_mode(k),
            ).pack(side=LEFT, padx=3, pady=2)

        actions = Frame(self.root, padx=14, pady=4)
        actions.pack(fill=X)
        Button(actions, text="刷新 Brain 记忆", command=self.refresh_brain).pack(
            side=LEFT, padx=3
        )
        Button(actions, text="生成话术", command=self.generate).pack(side=LEFT, padx=3)
        Button(actions, text="复制并打开 Cursor", command=self.copy_and_open).pack(
            side=LEFT, padx=3
        )
        Button(actions, text="HOW-TO-ASK", command=open_howto).pack(side=LEFT, padx=3)

        Label(self.root, text="Brain 摘要（只读）", padx=14, anchor="w").pack(fill=X)
        self.brain_box = Text(self.root, height=8, wrap=WORD, font=("Menlo", 11))
        self.brain_box.pack(fill=BOTH, expand=False, padx=14, pady=4)

        Label(self.root, text="将发给 Cursor 的话术", padx=14, anchor="w").pack(fill=X)
        self.prompt_box = Text(self.root, height=10, wrap=WORD, font=("Menlo", 12))
        self.prompt_box.pack(fill=BOTH, expand=True, padx=14, pady=4)

        self.status = StringVar(value="就绪 · 建议先点「今日安排」或「刷新 Brain」")
        Label(self.root, textvariable=self.status, fg="#333", padx=14, pady=6).pack(
            fill=X
        )

    def _row(self, parent: Frame, label: str, var: StringVar) -> None:
        row = Frame(parent)
        row.pack(fill=X, pady=3)
        Label(row, text=label, width=12, anchor="w").pack(side=LEFT)
        Entry(row, textvariable=var).pack(side=LEFT, fill=X, expand=True)

    def select_mode(self, key: str) -> None:
        self.current_mode = key
        meta = SKILL_PROMPTS[key]
        self.status.set(f"已选：{meta['title']}（{meta['skill']}）— {meta['hint']}")
        self.generate()

    def _clean(self, s: str, placeholder_prefix: str = "（") -> str:
        s = (s or "").strip()
        if s.startswith(placeholder_prefix) or s.startswith("("):
            return ""
        return s

    def refresh_brain(self, silent: bool = False) -> None:
        self.status.set("正在查询 GBrain…")
        self.root.update_idletasks()
        chunks: list[str] = []
        ok1, out1 = run_gbrain("search", "study-sessions OR tomorrow_first_step OR mastery")
        if ok1:
            chunks.append("【search】\n" + out1[:1800])
        else:
            chunks.append("【search 失败】\n" + out1[:800])
        ok2, out2 = run_gbrain("search", "courses OR exams OR session-recap")
        if ok2:
            chunks.append("【courses/exams】\n" + out2[:1200])
        text = "\n\n".join(chunks) if chunks else "(brain 暂无内容 — 可用 course-onboard / 辅导后写回)"
        self.brain_cache = text
        self.brain_box.delete("1.0", END)
        self.brain_box.insert(END, text)
        if not silent:
            self.status.set("Brain 已刷新 · " + date.today().isoformat())
        else:
            self.status.set("已静默读取 Brain · 可以开始点按钮")

    def generate(self) -> None:
        meta = SKILL_PROMPTS[self.current_mode]
        topic = self._clean(self.topic.get()) or "（请补充科目/单元）"
        block = self._clean(self.block.get()) or "（请补充卡点）"
        minutes = self._clean(self.minutes.get()) or "25"
        days = self._clean(self.days.get()) or "5"
        gap_day = self._clean(self.gap_day.get()) or "隔了一段时间"

        prompt = meta["template"].format(
            topic=topic,
            block=block,
            minutes=minutes,
            days=days,
            gap_day=gap_day,
        )
        # Attach lean brain tip for Agent (not a lecture)
        footer = (
            "\n\n【Agent 上下文提示】\n"
            "- 必须先 gbrain search/query 读 mastery 与最近 study-sessions。\n"
            "- 遵守对应 Skill Contract；禁止未诊断就长篇讲义。\n"
            "- 结束走 recap-reflex → session-recap 写回。\n"
            f"- 日期：{date.today().isoformat()}\n"
        )
        if self.brain_cache and "失败" not in self.brain_cache[:20]:
            footer += "- 桌面助手已预取 brain 摘要，以最新 MCP 查询为准。\n"

        full = prompt + footer
        self.prompt_box.delete("1.0", END)
        self.prompt_box.insert(END, full)
        self.status.set(f"已生成「{meta['title']}」话术 — 可复制并打开 Cursor")

    def copy_and_open(self) -> None:
        text = self.prompt_box.get("1.0", END).strip()
        if not text:
            self.generate()
            text = self.prompt_box.get("1.0", END).strip()
        clipboard(text)
        open_cursor()
        self.status.set(
            "已复制到剪贴板，并打开 Cursor（iBrain 项目）。在聊天框粘贴即可（Cmd+V）。"
        )
        messagebox.showinfo(
            "下一步",
            "1. Cursor 已打开 iBrain 项目\n"
            "2. 话术已在剪贴板\n"
            "3. 在 Agent 聊天框 Cmd+V 发送\n\n"
            "确保 MCP gbrain 已连接，且 User Rule 含 recap-reflex。",
        )


def main() -> None:
    if sys.platform != "darwin":
        print("当前仅为 macOS 桌面助手设计。")
    app = AssistantApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()
