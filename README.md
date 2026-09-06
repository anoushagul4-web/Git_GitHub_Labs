# Lab 5: CI-Ready Python Automation with Pull Request

## Goal
Practice GitHub Pull Requests and prepare Python/Bash automation for CI.

## Your task
1. Create branch `feature-system-check`.
2. Improve `system_check.py` so it validates that the required environment variables exist.
3. Keep the script safe: never print secret values.
4. Test the script locally.
5. Commit and push the branch.
6. Create a Pull Request into `main`.
7. Add a GitHub Actions workflow under `.github/workflows/ci.yml`.
8. The workflow should install/use Python and run `python3 system_check.py`.
9. Observe the check on the Pull Request.
10. Merge only after the check passes.

## Deliverable
A merged Pull Request with a passing GitHub Actions check.
