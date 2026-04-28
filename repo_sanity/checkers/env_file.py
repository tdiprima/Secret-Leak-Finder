"""
Check: Is a .env file sitting in the repo?
"""

import os

from ..results import Finding


def check_env_file(repo_path):
    """Check whether .env is listed in .gitignore. Return findings."""
    findings = []
    gitignore_path = os.path.join(repo_path, ".gitignore")

    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r") as fh:
            lines = [line.strip() for line in fh]
        if ".env" in lines:
            findings.append(Finding("OK", ".env is listed in .gitignore"))
        else:
            findings.append(Finding("FAIL", ".env is NOT in .gitignore"))
    else:
        findings.append(Finding("FAIL", "no .gitignore file found"))

    return findings
