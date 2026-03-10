# 🔎 Secret Leak Finder

## Problem
CI pipelines often run without basic security checks.

## Solution
This tool scans repositories for common DevSecOps issues before deployment.

Things it detects:

* API keys
* AWS credentials
* `.env` files
* private keys
* tokens in config files

Example:

```bash
python main.py /path/to/your/repo
```

Output:

```
⚠ Possible AWS key in config/settings.py
⚠ .env file detected
✔ No private keys found
```

Why it's important:

To catch leaks before CI or GitHub scanners do.
