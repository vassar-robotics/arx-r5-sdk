# PyPI Publishing Quick Start

## One-Time Setup
1. Create PyPI account: https://pypi.org/account/register/
2. Create API token: https://pypi.org/manage/account/ → "API tokens" → "Add API token"
3. Add to GitHub: Repository Settings → Secrets → Actions → New secret
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI token (starts with `pypi-`)

## Publishing a New Version

### 1. Update Version (3 files)
```bash
# Update version in these files:
setup.py         # line 72: version="0.1.0"
pyproject.toml   # line 12: version = "0.1.0"  
vassar_arx_r5_sdk/__init__.py  # line 8: __version__ = "0.1.0"
```

### 2. Commit & Tag
```bash
git add setup.py pyproject.toml vassar_arx_r5_sdk/__init__.py
git commit -m "Bump version to 0.1.0"
git push origin main

# Create version tag (MUST start with 'v')
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

### 3. Monitor
- Go to: https://github.com/[your-username]/vassar-arx-r5-sdk/actions
- Wait for green checkmark (~10-20 minutes)
- Check PyPI: https://pypi.org/project/vassar-arx-r5-sdk/

## That's it! 🎉

The GitHub workflow automatically:
- Builds Linux wheels for Python 3.8-3.11
- Builds for x86_64 and aarch64
- Publishes to PyPI when you push a tag starting with 'v'