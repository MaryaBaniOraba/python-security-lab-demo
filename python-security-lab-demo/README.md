# Python Security Lab Demo

This repo intentionally includes:
- A **vulnerable dependency** (`PyYAML==5.3.1`) so Dependabot raises an alert.
- A **Python code issue** (`os.system` command injection; unsafe `yaml.full_load`) so **Bandit** flags findings.

## What to do (submission checklist)
1. Create a new GitHub repo (public recommended) and upload these files.
2. Enable **Dependabot alerts** in **Settings → Security → Advanced Security**.
3. Commit, then wait for Dependabot to raise an alert on `PyYAML==5.3.1`.
4. Keep the default **Bandit** GitHub Actions workflow below; it will run on push/PR and publish results to **Security → Code scanning**.
5. Screenshot:
   - Dependabot alert for PyYAML
   - Bandit findings (at least: high/medium severity for `os.system`)
6. (Optional) Fix on a new branch using the provided `main_fixed.py` and update `requirements.txt` to a safe PyYAML. Open a PR; observe Bandit/Dependabot changes.

---

## Files overview

```
.
├── README.md
├── requirements.txt              # vulnerable on purpose
├── config.yaml                   # sample input
├── main.py                       # intentionally unsafe
├── main_fixed.py                 # safer alternative (for remediation step)
└── .github
    ├── dependabot.yml            # enables version update PRs for pip
    └── workflows
        └── bandit.yml           # Bandit → SARIF → Code scanning
```

## Expected Alerts

- **Dependabot**: vulnerable PyYAML (< 5.4) advisory, suggests updating to ≥ 6.0.1.
- **Bandit**:
  - `subprocess`/`os.system` command execution (injection risk).
  - Unsafe YAML loader (`yaml.full_load` with old PyYAML).

## Remediation (optional, for the report)

- Replace `os.system` with `subprocess.run([...], check=True)` and strict argument handling.
- Replace `yaml.full_load` with `yaml.safe_load` and pin `pyyaml>=6.0.1`.

