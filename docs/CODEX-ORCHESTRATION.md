# Codex Orchestration Playbook

Use this playbook to run The Agency skills in Codex with a stable workflow.

## Recommended Operating Mode

Default to **serial mainline + parallel side tracks**:

1. Mainline (serial): Product/Strategy -> Design -> Engineering -> Testing -> Release notes.
2. Side tracks (parallel): only for tasks that do not modify the same files/modules.
3. Merge gate: always run testing/reality-check skills before claiming done.

## Skill Set by Stage

- Planning: `product-sprint-prioritizer`, `project-manager-senior`
- UX/UI: `design-ux-architect`, `design-ui-designer`
- Build: `engineering-frontend-developer`, `engineering-backend-architect`
- QA: `testing-api-tester`, `testing-reality-checker`, `testing-test-results-analyzer`
- Go-to-market: `marketing-content-creator`, `marketing-growth-hacker`

## Template A: Serial Mainline

Use when the work is coupled and risks conflicts.

```text
Use these skills in order:
1) product-sprint-prioritizer
2) design-ux-architect
3) engineering-frontend-developer
4) testing-reality-checker

Task:
- Build [feature].
- Keep one active skill at a time.
- At each handoff, summarize decisions in 5 bullets max.
- Do not start implementation until scope is approved.
- End with verification commands and output summary.
```

## Template B: Serial + Parallel Side Tracks

Use when one core implementation can run with independent branches.

```text
Goal: deliver [feature] with docs and launch assets.

Mainline (serial):
1) product-sprint-prioritizer -> lock scope
2) engineering-frontend-developer -> implement
3) testing-api-tester + testing-reality-checker -> verify

Side track A (parallel, independent):
- marketing-content-creator -> release note + changelog draft

Side track B (parallel, independent):
- design-ui-designer -> visual polish suggestions

Rules:
- Side tracks must not edit mainline code files.
- Mainline decisions are source of truth.
- Final step must include verification evidence.
```

## Template C: Incident / Hotfix Flow

Use for production issues requiring fast recovery.

```text
Use these skills:
1) testing-evidence-collector
2) testing-api-tester
3) engineering-senior-developer
4) testing-reality-checker
5) support-executive-summary-generator

Task:
- Reproduce bug with concrete evidence.
- Implement minimal hotfix only (no scope creep).
- Verify fix + regression checks.
- Produce executive incident summary with root cause and next actions.
```

## Practical Rules

- Do not run more than 2 parallel branches unless tasks are truly isolated.
- If two branches need the same files, switch back to serial flow.
- Always include explicit acceptance criteria before build starts.
- Always finish with command-level verification evidence.

