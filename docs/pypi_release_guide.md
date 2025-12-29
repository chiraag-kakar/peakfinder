# PyPI Release Guide

Complete guide for publishing `peakfinder` to TestPyPI and production PyPI.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Build Package](#build-package)
- [TestPyPI Workflow](#testpypi-workflow)
- [Production PyPI Workflow](#production-pypi-workflow)
- [Verification](#verification)

---

## Prerequisites

### Required Tools
```bash
# Install build tools
python3 -m pip install build twine

# Verify installation
python3 -m build --version
python3 -m twine --version
```

### Create Accounts
1. **TestPyPI**: https://test.pypi.org/account/register/
2. **Production PyPI**: https://pypi.org/account/register/

---

## Setup

### Step 1: Generate API Tokens

**For TestPyPI:**
1. Go to: https://test.pypi.org/manage/account/tokens/
2. Create token named `peakfinder-testpypi`
3. Copy the token (you won't be able to see it again)

**For Production PyPI:**
1. Go to: https://pypi.org/manage/account/tokens/
2. Create token named `peakfinder-pypi`
3. Copy the token

### Step 2: Configure ~/.pypirc

Create or update `~/.pypirc` with both repositories:

```bash
cat >> ~/.pypirc << 'EOF'
[distutils]
  index-servers =
    testpypi
    pypi

[testpypi]
  repository = https://test.pypi.org/legacy/
  username = __token__
  password = pypi-AgENdGVzdC5weXBpLm9yZwIk...  # Your TestPyPI token

[pypi]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = pypi-AgEIcHlwaS5vcmc...  # Your production PyPI token
EOF
```

**Important:** Replace token placeholders with actual tokens.

### Step 3: Set Proper Permissions

```bash
chmod 600 ~/.pypirc
```

---

## Build Package

### Clean Previous Builds
```bash
rm -rf build/ dist/ *.egg-info
```

### Build Distribution Files
```bash
python3 -m build
```

This creates:
- `dist/peakfinder-0.1.0.tar.gz` (source distribution)
- `dist/peakfinder-0.1.0-py3-none-any.whl` (wheel distribution)

### Validate Package
```bash
python3 -m twine check dist/*
```

Expected output:
```
Checking dist/peakfinder-0.1.0-py3-none-any.whl: PASSED
Checking dist/peakfinder-0.1.0.tar.gz: PASSED
```

---

## TestPyPI Workflow

### Step 1: Upload to TestPyPI
```bash
python3 -m twine upload --repository testpypi dist/*
```

Expected output:
```
Uploading distributions to https://test.pypi.org/legacy/
Uploading peakfinder-0.1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.9/23.9 kB
Uploading peakfinder-0.1.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 28.3/28.3 kB

View at:
https://test.pypi.org/project/peakfinder/0.1.0/
```

### Step 2: Test Installation

**In a clean virtual environment:**
```bash
python3 -m venv test_env
source test_env/bin/activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ peakfinder

# Test import
python3 -c "from peakfinder import PeakDetector; print('Success!')"

# Cleanup
deactivate
rm -rf test_env
```

### Step 3: Verify on TestPyPI
Visit: https://test.pypi.org/project/peakfinder/

Check:
- ✅ Correct version displayed
- ✅ README renders properly
- ✅ Package files available
- ✅ Installation works

---

## Production PyPI Workflow

### Prerequisites
- ✅ Tested on TestPyPI
- ✅ All tests passing
- ✅ Version bumped in `pyproject.toml`
- ✅ CHANGELOG.md updated
- ✅ Git tag created (optional but recommended)

### Step 1: Create Git Tag (Recommended)
```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

### Step 2: Upload to Production PyPI
```bash
python3 -m twine upload --repository pypi dist/*
```

Expected output:
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading peakfinder-0.1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.9/23.9 kB
Uploading peakfinder-0.1.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 28.3/28.3 kB

View at:
https://pypi.org/project/peakfinder/0.1.0/
```

### Step 3: Test Production Installation

```bash
# Install from PyPI (official)
pip install peakfinder

# Verify version
pip show peakfinder

# Test import
python3 -c "from peakfinder import PeakDetector; print('Success!')"
```

### Step 4: Verify on PyPI
Visit: https://pypi.org/project/peakfinder/

Check:
- ✅ Correct version displayed
- ✅ README renders properly
- ✅ Installation works globally
- ✅ Package discoverable on PyPI

---

## Verification

### Check Package Contents
```bash
# List tar.gz contents
tar -tzf dist/peakfinder-0.1.0.tar.gz | head -20

# List wheel contents
unzip -l dist/peakfinder-0.1.0-py3-none-any.whl | head -20
```

### Verify Installation
```bash
python3 -c "
import peakfinder
print(f'Version: {peakfinder.__version__}')
from peakfinder import PeakDetector
print('Import successful!')
"
```

### Check PyPI Page
- TestPyPI: https://test.pypi.org/project/peakfinder/
- PyPI: https://pypi.org/project/peakfinder/

---

## Troubleshooting

### Issue: `zsh: command not found: twine`
**Solution:** Use module syntax instead:
```bash
python3 -m twine upload --repository testpypi dist/*
```

### Issue: 403 Forbidden when uploading
**Solutions:**
- Verify token is correct in `~/.pypirc`
- Check token hasn't expired
- Ensure username is `__token__` (not your PyPI username)
- Verify repository URL matches (testpypi vs pypi)

### Issue: Package already exists
**Solution:** Increment version in `pyproject.toml` and rebuild:
```toml
version = "0.1.1"  # Change from 0.1.0
```

Then rebuild:
```bash
rm -rf build/ dist/ *.egg-info
python3 -m build
```

### Issue: Invalid package metadata
**Solution:** Validate before uploading:
```bash
python3 -m twine check dist/*
```

Fix any reported issues, then rebuild.

---

## Quick Reference Commands

### One-time Setup
```bash
# Install tools
python3 -m pip install build twine

# Configure credentials
cat >> ~/.pypirc << 'EOF'
[testpypi]
  repository = https://test.pypi.org/legacy/
  username = __token__
  password = pypi-YOUR-TOKEN-HERE

[pypi]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = pypi-YOUR-TOKEN-HERE
EOF

chmod 600 ~/.pypirc
```

### Release Workflow
```bash
# Build
rm -rf build/ dist/ *.egg-info
python3 -m build

# Validate
python3 -m twine check dist/*

# Test
python3 -m twine upload --repository testpypi dist/*

# Production (after testing)
python3 -m twine upload --repository pypi dist/*
```

---

## References

- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 517 - Build Backend](https://www.python.org/dev/peps/pep-0517/)
