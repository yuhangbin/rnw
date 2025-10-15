# Python Development Cheat Sheet

## Virtual Environment Commands

```bash
# Create virtual environment (once)
python -m venv venv

# Activate (every time you start working)
source venv/bin/activate

# Deactivate (when done working)
deactivate

# Install project
pip install -e .[dev]
```

## Daily Commands

```bash
# Run your program
python main.py

# Run tests
pytest

# Run tests with coverage
pytest --cov=src/rnw

# Format code
black src/ tests/ main.py

# Check code style
flake8 src/ tests/ main.py
```

## Adding Dependencies

1. Edit `pyproject.toml`
2. Add to `dependencies = []` section
3. Run `pip install -e .[dev]`

## Project Structure

```
rnw/
├── src/rnw/           # Your Python package
├── tests/             # Your tests
├── venv/              # Virtual environment (don't commit)
├── main.py            # Demo script
├── pyproject.toml     # Project configuration
├── .gitignore         # Files to ignore in git
└── CHEATSHEET.md      # This file
```

## Signs You're in Virtual Environment

- Your terminal prompt shows `(venv)`
- `which python` shows path with `venv`
- `pip list` shows only project dependencies

## Git Commands

```bash
# Check what files are tracked
git status

# Add files to commit
git add .

# Commit changes
git commit -m "Your commit message"

# Push to remote
git push
```

## Important: Files Git Ignores

- `venv/` - Virtual environment
- `__pycache__/` - Compiled Python files
- `.pytest_cache/` - Test cache
- `*.pyc` - Bytecode files
- `.coverage` - Coverage reports