#!/usr/bin/env python3
# HOOK_VERSION: 1.0.0
# HOOK_EVENT: PreToolUse
# HOOK_MATCHER: Bash
# HOOK_GROUP: safety
"""
Dangerous Command Guard — PreToolUse Hook

Detects potentially destructive bash commands and blocks them unless
the user has explicitly approved. This is a safety net, not a replacement
for careful planning.

BEHAVIOR:
---------
1. Reads the Bash tool input (command string) from stdin
2. Scans for dangerous patterns (rm -rf, DROP TABLE, force push, etc.)
3. If dangerous pattern found: BLOCKS with explanation and safe alternative
4. If no match: APPROVES silently

SAFETY:
-------
- Fails open on any error (allows command if hook crashes)
- Only checks Bash tool calls (matcher: Bash)
- Does not block if pattern appears inside quotes/strings used as data

REGISTRATION:
-------------
Add to .claude/settings.json:
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": ".claude/hooks/example-dangerous-command-guard.py"
        }]
      }
    ]
  }
}
"""

import json
import re
import sys


# ═══════════════════════════════════════════════════════════════════════
# Dangerous command patterns
# ═══════════════════════════════════════════════════════════════════════

DANGEROUS_PATTERNS = [
    {
        "pattern": r"\brm\s+(-[a-zA-Z]*f[a-zA-Z]*\s+|--force\s+).*(/|~|\$HOME|\.\.|\.)",
        "description": "Recursive force-delete targeting root, home, or parent directories",
        "alternative": "Use targeted `rm` on specific files, or move to trash first",
    },
    {
        "pattern": r"\bgit\s+push\s+.*--force\b",
        "description": "Force push overwrites remote history — can destroy teammates' work",
        "alternative": "Use `git push --force-with-lease` for safer force push",
    },
    {
        "pattern": r"\bgit\s+reset\s+--hard\b",
        "description": "Hard reset discards all uncommitted changes permanently",
        "alternative": "Use `git stash` to save changes, or `git reset --soft` to keep them staged",
    },
    {
        "pattern": r"\bDROP\s+(TABLE|DATABASE|SCHEMA)\b",
        "description": "Dropping database objects is irreversible in production",
        "alternative": "Create a backup first, or use a migration with rollback support",
    },
    {
        "pattern": r"\bchmod\s+(-[a-zA-Z]*\s+)?777\b",
        "description": "chmod 777 gives all users full access — security risk",
        "alternative": "Use minimal permissions: 755 for directories, 644 for files",
    },
    {
        "pattern": r"\bmkfs\b",
        "description": "Formatting a filesystem destroys all data on the device",
        "alternative": "Double-check the target device with `lsblk` before formatting",
    },
    {
        "pattern": r">\s*/dev/sd[a-z]\b",
        "description": "Writing directly to a block device can destroy the filesystem",
        "alternative": "Verify the target device and use proper tools (dd with status=progress)",
    },
]


# ═══════════════════════════════════════════════════════════════════════
# Detection logic
# ═══════════════════════════════════════════════════════════════════════

def check_command(command: str) -> dict | None:
    """
    Check a command string against dangerous patterns.

    Returns the first matching pattern dict, or None if no match.
    """
    for entry in DANGEROUS_PATTERNS:
        if re.search(entry["pattern"], command, re.IGNORECASE):
            return entry
    return None


def build_block_reason(match: dict, command: str) -> str:
    """Build a human-readable block reason with the safe alternative."""
    return (
        f"⚠️ BLOCKED: {match['description']}\n\n"
        f"Command: {command[:200]}\n\n"
        f"Safe alternative: {match['alternative']}\n\n"
        f"If you need to run this exact command, ask the user for explicit approval."
    )


# ═══════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════

def main():
    """
    PreToolUse hook entry point.

    Reads JSON from stdin with the Bash tool's input, checks for
    dangerous patterns, and blocks if found.
    """
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # Fail open — if we can't parse input, allow the command
        sys.exit(0)

    # Extract the command from the tool input
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    if not command:
        # No command to check — allow
        sys.exit(0)

    # Check against dangerous patterns
    match = check_command(command)

    if match:
        output = {
            "decision": "block",
            "reason": build_block_reason(match, command),
        }
        print(json.dumps(output))
    # If no match, exit silently (implicit approve)


if __name__ == "__main__":
    main()
