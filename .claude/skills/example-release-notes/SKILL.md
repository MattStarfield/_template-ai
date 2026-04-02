---
name: release-notes
description: |
  Generate release notes from git history between two tags or branches.
  Categorizes changes by type, lists contributors, and formats for
  GitHub releases or changelogs.

  Use PROACTIVELY when:
  - User wants to create a release
  - User mentions "release notes", "changelog", "what changed"
  - User is preparing a version bump or tag

  Examples:
  - <example>
    Context: User is preparing a release
    user: "Generate release notes for v1.2.0"
    assistant: "I'll generate release notes from the last tag to HEAD..."
  </example>
  - <example>
    Context: User wants to see what changed
    user: "What's changed since the last release?"
    assistant: "I'll compile the changes since the last tag..."
  </example>
---

# Release Notes Generator

## 🔴 EXECUTION MODE: INLINE ONLY — NEVER DELEGATE

**This workflow MUST be executed inline in the main conversation session.**

- **NEVER** launch this as a sub-agent via the Agent/Task tool
- **NEVER** delegate this workflow to a background agent
- **READ** this file, then execute each phase yourself, step by step

## Responsibilities

| This Skill DOES | This Skill DOES NOT |
|-----------------|---------------------|
| Gather commits between two refs | Create or push git tags |
| Categorize changes by type | Deploy or publish releases |
| Format release notes as markdown | Modify any code or config files |
| Present draft for user review | Post to GitHub without user approval |

## Workflow

### Phase 1: Determine Version Range

1. **Identify the target version** from user input or `$ARGUMENTS`
2. **Find the previous version tag**:
   ```bash
   PREV_TAG=$(git describe --tags --abbrev=0 HEAD^ 2>/dev/null || echo "")
   CURRENT_REF="HEAD"
   echo "Previous tag: $PREV_TAG"
   echo "Generating notes: $PREV_TAG..$CURRENT_REF"
   ```
3. If no previous tag exists, use the initial commit as the starting point

### Phase 2: Gather Changes

1. **Collect commits** in the range:
   ```bash
   git log $PREV_TAG..$CURRENT_REF --pretty=format:"%h %s (%an)" --no-merges
   ```
2. **Collect contributors**:
   ```bash
   git log $PREV_TAG..$CURRENT_REF --pretty=format:"%an" | sort -u
   ```
3. **Collect files changed** for scope assessment:
   ```bash
   git diff --stat $PREV_TAG..$CURRENT_REF
   ```

### Phase 3: Categorize Changes

Classify each commit by its conventional commit prefix:

| Prefix | Category | Emoji |
|--------|----------|-------|
| `feat` | Features | ✨ |
| `fix` | Bug Fixes | 🐛 |
| `docs` | Documentation | 📖 |
| `refactor` | Refactoring | ♻️ |
| `perf` | Performance | ⚡ |
| `test` | Tests | 🧪 |
| `chore` | Maintenance | 🔧 |
| `breaking` | Breaking Changes | 🚨 |

If commits don't follow conventional commit format, categorize by analyzing
the commit message content and files changed.

### Phase 4: Format Release Notes

**Structure:**

```markdown
## [vX.Y.Z] — YYYY-MM-DD

### 🚨 Breaking Changes
- Description of breaking change (#PR)

### ✨ Features
- Description of feature (#PR)

### 🐛 Bug Fixes
- Description of fix (#PR)

### ♻️ Improvements
- Description of refactor or improvement (#PR)

### 📖 Documentation
- Description of docs change

### Contributors
- @contributor1, @contributor2
```

**Rules:**
- Lead each item with a human-readable description, not the raw commit message
- Include PR/issue numbers where available
- Breaking changes go first with clear migration guidance
- Empty categories are omitted

### Phase 5: Present for Review

**🔴 HARD GATE — User must approve before posting**

Present the formatted release notes to the user and ask:
1. "Are these release notes accurate and complete?"
2. "Should I post these as a GitHub release, or just output them?"

Do NOT create a GitHub release without explicit user approval.

## Anti-Patterns

- **Never fabricate PR numbers** — only include numbers you verified with `git log` or `gh pr list`
- **Never post without approval** — release notes are user-facing; the user must review
- **Never include internal/WIP commits** — filter out fixup commits, WIP, and merge commits
- **Never skip the categorization** — uncategorized dump of commits is not release notes
