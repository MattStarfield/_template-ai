# Example Workflow Phase Template

This template demonstrates the standard structure for a multi-phase workflow.
Use this pattern when building skills, agents, or commands that coordinate
sequential work with approval gates.

---

## Phase N: [PHASE NAME]

**Objective**: [One sentence — what this phase accomplishes]

### Exact Steps

1. **[First action]**
   ```bash
   # Command to execute
   ```
   Expected output: [what you should see]

2. **[Second action]**
   - Detail A
   - Detail B

3. **[Third action]**
   ```bash
   # Another command
   ```

### Decision Gate

**🔴 HARD GATE — Do NOT proceed without user approval**

Present to the user:
- What was completed in this phase
- Key findings or decisions
- What the next phase will do

Ask: *"Phase N complete. Proceed to Phase N+1?"*

### Output Format

```markdown
## Phase N Summary
- **Status**: Complete
- **Key finding**: [what was discovered]
- **Decision**: [what was decided and why]
- **Next step**: [what Phase N+1 will do]
```

### Prohibited Actions

- ❌ Do NOT proceed to the next phase without approval
- ❌ Do NOT modify files outside the phase's scope
- ❌ Do NOT skip the decision gate even if the answer seems obvious

---

## Phase Conventions

When creating your own workflow phases, follow these conventions:

1. **Number phases sequentially** — Phase 1, Phase 2, etc.
2. **One objective per phase** — each phase does one thing well
3. **Exact commands** — provide copy-pasteable commands, not descriptions
4. **Decision gates at risk boundaries** — any irreversible action needs a gate
5. **Output format** — standardize what each phase produces
6. **Prohibited actions** — explicitly state what the phase must NOT do
7. **Signature** — agents should sign their GitHub posts with version + timestamp
