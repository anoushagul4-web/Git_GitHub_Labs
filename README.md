# Lab 4: Secure Python/Bash Repository

## Goal
Practice repository hygiene and secret-leak prevention.

## Your task
1. Inspect all supplied files.
2. Identify files that should not be committed.
3. Create a `.gitignore` covering:
   - `.env`
   - log files
   - Python cache
   - virtual environments
   - generated reports
4. Verify ignored files with `git status`.
5. Improve `report.py` so it reads configuration from environment variables rather than hard-coded credentials.
6. Use `generate_report.sh` to run the Python report.
7. Commit only safe source/configuration files.
8. Push to GitHub.
9. Explain in this README why each ignored pattern exists.

Do not publish real credentials. The supplied values are placeholders only.
