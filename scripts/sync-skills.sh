#!/usr/bin/env bash
set -euo pipefail
IBRAIN="${IBRAIN:-$HOME/Documents/iBrain}"
GBRAIN_SKILLS="${GBRAIN_SKILLS:-$HOME/Documents/gbrain/skills}"
SKILLS=(study-coach exam-sprint misconception-fix course-onboard session-recap)
mkdir -p "$GBRAIN_SKILLS"
for s in "${SKILLS[@]}"; do
  cp -r "$IBRAIN/skillpacks/student/skills/$s" "$GBRAIN_SKILLS/"
  echo "synced $s -> gbrain"
done
mkdir -p "$IBRAIN/.cursor/skills"
for s in "${SKILLS[@]}"; do
  cp -r "$IBRAIN/skillpacks/student/skills/$s" "$IBRAIN/.cursor/skills/"
done
echo "Done."
