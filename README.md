# repo-sanity

My own sanity-checker.  
A Python CLI tool that checks a repo for dumb security mistakes.

## Usage

```bash
python main.py /path/to/your/repo
```

## Project Structure

```
repo-sanity/
├── main.py                 # Entry point. Orchestrates everything.
├── scanner.py              # Walks the repo, feeds files to checkers.
├── printer.py              # Prints colored results. That's it.
├── results.py              # One tiny data class for findings.
├── requirements.txt        # Zero dependencies (just stdlib!)
│
└── checkers/               # Each file checks ONE type of problem.
    ├── __init__.py
    ├── env_file.py         # .env committed?
    ├── gitignore.py        # Missing .gitignore?
    ├── api_keys.py         # API keys in source?
    ├── private_keys.py     # Private keys in source?
    ├── shell_true.py       # subprocess(shell=True)?
    ├── debug_prints.py     # print() left in code?
    └── secret_files.py     # World-readable secret files?
```

Each checker is independent. Add new ones by dropping a file in `checkers/`.

<br>
