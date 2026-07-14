#!/bin/bash
# Double-click to launch iBrain Desktop Assistant
cd "$(dirname "$0")" || exit 1
export PATH="$HOME/.local/bin:$HOME/.bun/bin:$PATH"
export IBRAIN="${IBRAIN:-$HOME/Documents/iBrain}"
exec /usr/bin/python3 "$IBRAIN/apps/desktop-assistant/ibrain_assistant.py"
