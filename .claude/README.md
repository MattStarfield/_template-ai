# .claude/ Directory

Claude Code project configuration. This directory is managed per-project
and checked into version control (except sensitive files listed in .gitignore).

## Structure

```
.claude/
├── settings.json    # Permissions, hooks, environment variables
├── hooks/           # Event-driven scripts (PreToolUse, PostToolUse, etc.)
├── agents/          # Agent definitions for multi-step workflows
├── commands/        # Custom slash commands (/command-name)
├── skills/          # Skill definitions (directory-based, with SKILL.md)
├── templates/       # Issue body templates, workflow templates, etc.
└── README.md        # This file
```

## Adding Hooks

Place scripts in `hooks/` and register them in `settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": ".claude/hooks/my-hook.py" }]
      }
    ]
  }
}
```

**Hook events**: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `PostToolUseFailure`, `Stop`, `SessionStart`, `SessionResume`

**Hook contract**: Hooks receive JSON on stdin and emit JSON on stdout.
- PreToolUse/PostToolUse: `{"decision": "approve"|"deny"|"block", "reason": "..."}`
- UserPromptSubmit: `{"decision": "approve", "additionalContext": "injected instructions"}`
- Stop: `{"decision": "allow"|"block", "reason": "..."}`

See `hooks/example-dangerous-command-guard.py` for a working reference.

## Adding Commands

Create a markdown file in `commands/`:

```
commands/my-command.md    →  /my-command
commands/deploy.md        →  /deploy
```

**Frontmatter**:
```yaml
---
description: What this command does and when to use it
---
```

The file content becomes the prompt. Use `$ARGUMENTS` for user input.
See `commands/example-deploy.md` for a working reference.

## Adding Skills

Create a directory with a `SKILL.md` file:

```
skills/my-skill/SKILL.md    →  invoked by hooks or other agents
```

**Frontmatter**:
```yaml
---
name: my-skill
description: |
  When to use this skill and what it does.
---
```

Skills are directory-based bundles that can include supporting files alongside SKILL.md.
See `skills/example-release-notes/SKILL.md` for a working reference.

## Adding Agents

Agent definitions in `agents/` are markdown files describing multi-step
workflows. They're invoked by hooks, skills, or other agents.

**Frontmatter**:
```yaml
---
name: my-agent
description: What this agent does
tools: Read, Bash, Edit, Write
model: inherit
---
```

See `agents/example-code-reviewer.md` for a working reference.

## Adding Templates

Templates in `templates/` provide standardized formats for issue bodies,
workflow phases, handoff summaries, and other structured content.

## Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Skills Guide](https://docs.anthropic.com/en/docs/claude-code/skills)
