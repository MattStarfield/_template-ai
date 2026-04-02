# CLAUDE.md

<!-- This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. -->
<!-- Replace placeholder text (in angle brackets or HTML comments) with your project-specific content. -->

## Project Overview

<!-- Brief description: what this project does, who it's for, current state -->
<!-- Example: "HAPImatic is a web-based dashboard for remote Claude Code sessions. Monorepo: cli/ + server/ + web/." -->

## Project Links

<!-- These fields are auto-populated by the create-project skill. -->
<!-- Claude: use these links when the user references the project's Drive folder, repo, etc. -->

- **GitHub Repo**: <!-- GITHUB_REPO_URL -->
- **Google Drive**: <!-- GOOGLE_DRIVE_URL -->
- **Local Clone**: <!-- LOCAL_CLONE_PATH -->

## Quick Reference

<!-- Action-to-command mapping for the most common operations -->
<!-- Example:
| Action | Command |
|--------|---------|
| Build | `npm run build` |
| Test | `npm test` |
| Dev server | `npm run dev` |
| Lint | `npm run lint` |
| Type check | `npx tsc --noEmit` |
-->

## System Environment

<!-- Platform, runtime versions, key tools, paths -->
<!-- Example:
- **Platform**: Raspberry Pi 5 (16GB) · Linux 6.12 (Pi OS)
- **Runtime**: Node.js 20 (nvm), Python 3.11 (~venvs/)
- **Shell**: bash
-->

## Core Principles

**Workflow**: Understand → Plan → Execute → Verify
**Communication**: Direct, practical, safety-conscious

## 🔴 Safety Rules

### Solution Validation (CRITICAL)

**MANDATORY before implementing ANY solution:**

1. **Quote Exact Input**: Copy/paste the user's EXACT failing command, error message, or problematic input
2. **Validate Against Exact Input**: Explicitly explain how your solution catches/fixes THAT SPECIFIC input
3. **Test First Principle**: Before committing code, mentally trace through: "If user runs their exact command again, will my solution catch it?"
4. **No Assumptions**: Don't convert user's input into what you think they meant — solve for what they actually showed you

### Factual Information Verification (CRITICAL)

**NEVER fabricate, estimate, or create plausible-looking values. ALWAYS verify.**

When including factual information, you MUST:
1. **Run the actual command** to obtain the real value (e.g., `node --version`, `uname -r`)
2. **Read the actual file** if referencing file contents
3. **Query the actual system** for system information
4. **Mark as "Unknown — requires verification"** if you cannot verify

Zero tolerance for making up version numbers, system values, or technical claims.

### Project-Specific Safety

<!-- Add domain-specific safety rules here -->
<!-- Examples:
- ⚠️ Always check current state before modifying config
- ⚠️ Create backups before destructive operations
- ⚠️ Never commit secrets or credentials
- ⚠️ NEVER merge to main/prod without explicit user request
- ⚠️ Warn before restarting services that affect availability
-->

## Architecture

<!-- Key systems, directory structure, relationships -->
<!-- Example:
```
src/
├── api/        — REST endpoints
├── models/     — Database models
├── services/   — Business logic
└── utils/      — Shared utilities
```
-->

## Code Style & Conventions

<!-- Language-specific conventions if needed -->
<!-- Example:
- TypeScript strict mode, Prettier 80-char lines
- React: functional components + hooks only
- Python: ruff for linting, type hints required
- Naming: camelCase (JS/TS), snake_case (Python)
-->

## Key Files and Directories

<!-- Important paths and their purposes -->
<!-- Example:
| Path | Purpose |
|------|---------|
| `src/` | Application source code |
| `scripts/` | Utility and maintenance scripts |
| `tests/` | Test suite |
| `docs/` | Human-authored documentation |
| `claudedocs/` | Claude-generated reports and analyses |
| `.claude/` | Claude Code configuration |
-->

## Development Workflow

<!-- How to build, test, run, deploy -->
<!-- Example:
- **Build**: `npm run build`
- **Test**: `npm test`
- **Dev server**: `npm run dev` (port 3000)
- **Lint**: `npm run lint -- --fix`
- **Type check**: `npx tsc --noEmit`
-->

## Git Workflow

- Create feature branches for all work — never work on main directly
- Commit messages: `type(scope): description` (feat, fix, docs, chore, refactor)
- PR required for main branch changes
- Verify changes with `git diff` before staging

## Testing

<!-- Testing approach, frameworks, how to run -->
<!-- Example:
- **Unit tests**: `npm test` (Jest/Vitest)
- **E2E tests**: `npx playwright test`
- **Coverage**: `npm run test:coverage`
-->

## Deployment

<!-- Deployment procedures if applicable -->
<!-- Example:
- **Dev**: Automatic on push to dev branch
- **Prod**: Manual merge from dev → main, then deploy script
- **Verification**: Check health endpoint after deploy
-->

## Troubleshooting

<!-- Common issues and fixes -->
<!-- Example:
- **Build fails**: Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- **Port in use**: `lsof -i :3000` to find the process
- **Type errors**: Run `npx tsc --noEmit` for full diagnostic
-->

## Gotchas & Constraints

<!-- Infrastructure-specific pitfalls, known limitations -->
<!-- Example:
- SD card corruption risk on Pi — minimize writes
- Docker on NAS requires `sudo /usr/local/bin/docker`
- API rate limits: 100 req/min for external service
-->

## Tool Retry Limits

🔴 If ANY tool fails with the same error **3 consecutive times**, STOP and report to user.

Do not continue retrying in hopes it will work. Report: what failed, how many times, and the error message.

## External Integrations

<!-- MCP servers, APIs, external services used -->
<!-- Example:
- **Playwright MCP**: Browser automation and E2E testing
- **Context7**: Library documentation lookup
- **GitHub CLI**: Issue and PR management via `gh`
-->
