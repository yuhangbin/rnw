# Complete Dependency Management Guide

## Understanding Your pyproject.toml Structure

Your project uses a sophisticated dependency management system with different groups for different purposes.

### 🎯 **Runtime Dependencies** (What End Users Need)
```toml
[project]
dependencies = [
    "requests>=2.28.0",  # HTTP library - users need this
]
```
**When to use:** Libraries that your code imports and uses directly.

### 🛠️ **Development Dependencies** (What Developers Need)
```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",      # Testing framework
    "black>=22.0.0",       # Code formatter
    "flake8>=5.0.0",       # Code linter
    "mypy>=1.0.0",         # Type checker
    "pytest-cov>=4.0.0",  # Test coverage
]
```
**When to use:** Tools for development, testing, and code quality.

## Installation Commands by Scenario

### 👨‍💻 **Developer Setup** (Most Common)
```bash
# Activate virtual environment
source .venv/bin/activate

# Install everything for development
pip install -e ".[dev]"

# This installs:
# ✅ Your package in editable mode
# ✅ All runtime dependencies (requests)
# ✅ All development tools (pytest, black, etc.)
```

### 🚀 **Production Deployment**
```bash
# Install only what's needed to run the app
pip install .

# For web applications in production:
pip install ".[production,web]"

# This installs:
# ✅ Your package
# ✅ Runtime dependencies only
# ❌ No development tools (smaller, faster)
```

### 🧪 **CI/CD Pipeline**
```bash
# Install testing dependencies only
pip install ".[test,ci]"

# This installs:
# ✅ Testing tools
# ✅ Coverage reporting
# ✅ CI-specific tools
# ❌ No formatting/linting tools
```

### 📚 **Documentation Building**
```bash
# Install documentation tools
pip install ".[docs]"

# This installs:
# ✅ Sphinx documentation generator
# ✅ Documentation themes
```

## Real-World Examples

### Example 1: Adding a New Runtime Dependency

Let's say you want to add `pandas` for data analysis:

1. **Edit pyproject.toml:**
```toml
dependencies = [
    "requests>=2.28.0",
    "pandas>=1.3.0",  # ← Add this line
]
```

2. **Reinstall:**
```bash
pip install -e ".[dev]"
```

3. **Use in your code:**
```python
import pandas as pd
# Now you can use pandas
```

### Example 2: Adding Development Tools

Want to add `isort` for import sorting?

1. **Edit pyproject.toml:**
```toml
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0", 
    "black>=22.0.0",
    "flake8>=5.0.0",
    "mypy>=1.0.0",
    "isort>=5.0.0",  # ← Add this line
]
```

2. **Reinstall:**
```bash
pip install -e ".[dev]"
```

3. **Use the tool:**
```bash
isort src/ tests/
```

### Example 3: Environment-Specific Dependencies

Different environments need different things:

```bash
# Local development
pip install -e ".[dev]"

# Testing server
pip install ".[test,ci]"

# Production server
pip install ".[production]"

# Documentation server
pip install ".[docs]"

# Full-featured web app
pip install ".[web,production]"
```

## Dependency Groups Explained

### 🔧 **dev** - Development Tools
- `pytest` - Testing framework
- `black` - Code formatter
- `flake8` - Code linter
- `mypy` - Type checker
- `pytest-cov` - Test coverage

### 🧪 **test** - Testing Only
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `pytest-mock` - Mocking utilities

### 📖 **docs** - Documentation
- `sphinx` - Documentation generator
- `sphinx-rtd-theme` - Documentation theme

### 🌐 **web** - Web Features
- `fastapi` - Web framework
- `uvicorn` - Development server

### 🏭 **production** - Production Deployment
- `gunicorn` - Production web server
- `psycopg2-binary` - PostgreSQL database

### 🤖 **ci** - Continuous Integration
- `pytest` - Testing
- `pytest-cov` - Coverage
- `codecov` - Coverage reporting service

## Best Practices

### ✅ **Do This**
```toml
# Use version ranges for flexibility
dependencies = [
    "requests>=2.28.0,<3.0.0",
    "pandas>=1.3.0",
]

# Group related dependencies
[project.optional-dependencies]
web = ["fastapi>=0.68.0", "uvicorn>=0.15.0"]
database = ["sqlalchemy>=1.4.0", "psycopg2-binary>=2.9.0"]
```

### ❌ **Avoid This**
```toml
# Don't pin exact versions unless necessary
dependencies = [
    "requests==2.28.0",  # Too restrictive
]

# Don't mix runtime and dev dependencies
dependencies = [
    "requests>=2.28.0",
    "pytest>=7.0.0",  # This belongs in [dev]
]
```

## Troubleshooting

### Problem: "Module not found" after adding dependency
**Solution:** Reinstall the package
```bash
pip install -e ".[dev]"
```

### Problem: Dependency conflicts
**Solution:** Use version ranges
```toml
dependencies = [
    "package>=1.0.0,<2.0.0",
]
```

### Problem: Too many dependencies in production
**Solution:** Use specific groups
```bash
# Instead of this:
pip install ".[dev]"

# Do this in production:
pip install ".[production]"
```

## Quick Reference

| Command | Use Case | Installs |
|---------|----------|----------|
| `pip install .` | Production | Runtime only |
| `pip install ".[dev]"` | Development | Runtime + dev tools |
| `pip install ".[test]"` | Testing | Runtime + test tools |
| `pip install ".[web,production]"` | Web app | Runtime + web + production |
| `pip install ".[dev,docs]"` | Full development | Runtime + dev + docs |

## Your Current Setup Summary

✅ **Runtime Dependencies:** `requests` (HTTP library)  
✅ **Development Tools:** `pytest`, `black`, `flake8`, `mypy`, `pytest-cov`  
✅ **Multiple Environment Support:** dev, test, docs, web, production, ci  
✅ **Modern Standards:** Using pyproject.toml instead of requirements.txt  

Your dependency management is already following best practices!