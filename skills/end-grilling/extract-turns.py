#!/usr/bin/env python3
"""Print a Claude Code session transcript (.jsonl) as question/answer turns.

Each user turn is preceded by the assistant text it answered. Tool calls, tool results, system reminders and
skill bodies are dropped; pasted content is kept and marked.

Usage: python3 -I extract-turns.py <session.jsonl> > turns.md
"""

import json
import re
import sys

SKIP_PREFIXES = ("<system-reminder>", "Base directory for this skill:", "<command-name>/clear", "Caveat:")


def text_of(content):
    if isinstance(content, str):
        return content
    parts = []
    for block in content or []:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block["text"])
    return "\n".join(parts)


def clean_user(text):
    text = re.sub(r"<system-reminder>.*?</system-reminder>", "", text, flags=re.S)
    text = re.sub(r"<pasted_content[^>]*>", "\n[pasted]\n", text)
    text = re.sub(r"</pasted_content[^>]*>", "\n[/pasted]\n", text)
    return text.strip()


def main(path):
    last_assistant = ""
    turn = 0
    for line in open(path, encoding="utf-8"):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = entry.get("type")
        message = entry.get("message") or {}
        if kind == "assistant":
            text = text_of(message.get("content")).strip()
            if text:
                last_assistant = text
        elif kind == "user":
            content = message.get("content")
            if isinstance(content, list) and any(
                isinstance(b, dict) and b.get("type") == "tool_result" for b in content
            ):
                continue
            text = clean_user(text_of(content))
            if not text or text.startswith(SKIP_PREFIXES):
                continue
            turn += 1
            print(f"## Turn {turn}\n")
            if last_assistant:
                print("### Assistant\n")
                print(last_assistant + "\n")
            print("### User\n")
            print(text + "\n")
            last_assistant = ""


if __name__ == "__main__":
    main(sys.argv[1])
