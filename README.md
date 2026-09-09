# Lab 2: Multi-Developer Python Automation

## Goal
Practice parallel feature development with Git branches.

## Your task
Simulate two developers:

### Developer A
Create branch `feature-disk-check`.
Add disk usage information to `inventory.py`.

### Developer B
Create branch `feature-memory-check`.
Add memory information to `inventory.py`.

Use Git branches to keep the work isolated.

For each branch:
1. Make the change.
2. Test the Python script.
3. Commit with a meaningful message.
4. Push the branch to GitHub.

Then:
5. Merge both features into `main`.
6. Verify the final Python program.
7. Push `main`.

## Deliverable
A GitHub repository containing both feature branches and the final merged version.
=======
# Lab 1: Production Hotfix and Python Health Check

## Goal
Practice Git branching while using Python and Bash automation.

## Starting point
`health_check.py` contains a simple health check. `check.sh` runs it.

## Your task
1. Create a branch named `hotfix-health-check`.
2. Inspect the existing Python and Bash code.
3. Improve the health check so a failed check returns a non-zero exit code.
4. Make the Bash wrapper detect failure and print a useful operational message.
5. Test your changes locally.
6. Commit the changes with a meaningful commit message.
7. Push the branch to GitHub.
8. Open a Pull Request against `main`.

## Deliverable
The GitHub repository must contain the hotfix branch and Pull Request.

