---
description: Deploy the application using a 5-phase safety protocol (research, backup, execute, verify, document)
---

# Deploy Command

**Purpose**: Safe, documented deployment using a mandatory 5-phase protocol
**Pattern**: RESEARCH → BACKUP → EXECUTE → VERIFY → DOCUMENT

This command demonstrates the recommended structure for any operation that
modifies production systems. Adapt the phases to your deployment target.

## Five-Phase Protocol (MANDATORY)

### Phase 1: RESEARCH 🔍

**Purpose**: Understand current state before making changes

**Actions**:
1. Check current deployment status (running version, health checks)
2. Review what will change (git log, diff from current deployed version)
3. Identify potential risks or breaking changes
4. Check for blockers (pending migrations, dependency updates, config changes)

**Output**:
- Current version deployed
- Changes to be deployed (commit range)
- Risk assessment (breaking changes, migration needs)
- Confidence level (High/Medium/Low)

**User Approval Gate**: Present findings and ask: *"Ready to proceed with deployment?"*

---

### Phase 2: BACKUP 💾

**Purpose**: Create restore point before any changes

**Actions**:
1. Record current deployment state (version, config, environment)
2. Create backup or snapshot if applicable
3. Verify backup integrity
4. Document rollback procedure

**Critical Rules**:
- ⚠️ NEVER proceed without a verified backup or rollback plan
- ⚠️ If backup fails, ABORT and report to user

**Output**:
- Backup location/identifier
- Verified rollback procedure
- Confirmation backup is complete

**User Approval Gate**: *"Backup verified. Proceed with deployment?"*

---

### Phase 3: EXECUTE 🚀

**Purpose**: Perform the deployment

**Actions**:
1. Run build process
2. Run test suite (must pass — do not deploy with failing tests)
3. Deploy to target environment
4. Wait for deployment to complete

**Error Handling**:
- If build fails: Report error, do NOT deploy
- If tests fail: Report failures, do NOT deploy
- If deployment fails: Report error, initiate rollback procedure

**Output**:
- Build status
- Test results
- Deployment status (success/failure)

---

### Phase 4: VERIFY ✅

**Purpose**: Confirm deployment succeeded

**Verification Steps**:
1. Check service health endpoint
2. Verify new version is running
3. Run smoke tests against deployed environment
4. Check logs for errors or warnings
5. Compare before/after metrics if available

**Output**:
- Health check status
- Version confirmation
- Smoke test results
- Any warnings or anomalies

**User Notification**: Report verification results.

---

### Phase 5: DOCUMENT 📝

**Purpose**: Record deployment for future reference

**Actions**:
1. Log deployment details:
   - Timestamp
   - Version deployed (from → to)
   - Who triggered it
   - Any issues encountered
2. Update any deployment tracking (changelog, release notes)
3. Notify relevant stakeholders if applicable

**Output**:
- Deployment record created
- Summary of changes deployed

---

## Usage

```
/deploy                    # Deploy with full 5-phase protocol
/deploy staging            # Deploy to staging environment
/deploy --skip-backup      # Skip backup phase (use with caution)
```

$ARGUMENTS

## Safety Rules

### ⚠️ NEVER:
- Deploy without running tests first
- Skip the verification phase
- Deploy multiple unrelated changes at once
- Deploy without a rollback plan

### ✅ ALWAYS:
- Research current state first
- Create and verify backups
- Get user approval at critical gates
- Verify after deployment
- Document what was deployed
