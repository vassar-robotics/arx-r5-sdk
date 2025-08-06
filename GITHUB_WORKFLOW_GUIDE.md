# GitHub Workflow Guide for Publishing to PyPI

Your repository already has a GitHub workflow configured to automatically build and publish your package to PyPI. Here's how to use it:

## Quick Start

1. **Set up PyPI API Token** (one-time setup)
2. **Tag a release** to trigger automatic publishing

## Detailed Steps

### 1. Set up PyPI API Token

First, you need to create a PyPI API token and add it to your GitHub repository:

#### Create PyPI API Token:
1. Go to https://pypi.org/account/register/ and create an account (if you don't have one)
2. Log in to PyPI
3. Go to https://pypi.org/manage/account/
4. Scroll down to "API tokens" section
5. Click "Add API token"
6. Give it a name (e.g., "vassar-arx-r5-sdk GitHub Actions")
7. Choose scope: "Entire account" or just for this project (once it exists)
8. Click "Add token"
9. **IMPORTANT**: Copy the token immediately (it starts with `pypi-`). You won't be able to see it again!

#### Add Token to GitHub:
1. Go to your GitHub repository settings: https://github.com/[your-username]/vassar-arx-r5-sdk/settings
2. Click on "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Paste the token you copied from PyPI
6. Click "Add secret"

### 2. How the Workflow Works

The workflow (`.github/workflows/build-wheels.yml`) automatically:

- **On every push/PR**: Builds wheels for testing (but doesn't publish)
- **On version tags (v*)**: Builds and publishes to PyPI

It builds:
- Linux wheels for Python 3.8, 3.9, 3.10, 3.11
- Both x86_64 and aarch64 architectures
- Source distribution (sdist)

### 3. Publishing a Release

To publish a new version to PyPI:

1. **Update version numbers** in these files:
   ```bash
   # Edit these files and update version (e.g., 0.1.0 → 0.2.0)
   - setup.py (line 72)
   - pyproject.toml (line 12)
   - vassar_arx_r5_sdk/__init__.py (add: __version__ = "0.2.0")
   ```

2. **Commit your changes**:
   ```bash
   git add setup.py pyproject.toml vassar_arx_r5_sdk/__init__.py
   git commit -m "Bump version to 0.2.0"
   git push origin main
   ```

3. **Create and push a version tag**:
   ```bash
   # Tag format must start with 'v'
   git tag -a v0.2.0 -m "Release version 0.2.0"
   git push origin v0.2.0
   ```

4. **Monitor the workflow**:
   - Go to https://github.com/[your-username]/vassar-arx-r5-sdk/actions
   - You'll see the workflow running
   - It will build all wheels and then publish to PyPI

### 4. Testing Before Release (Optional)

You can test the workflow without publishing:

```bash
# Push to a branch to test building
git checkout -b test-build
git push origin test-build
```

Check the Actions tab to see if wheels build successfully.

### 5. First-Time Publishing Tips

For your first release:

1. **Consider using TestPyPI first**:
   - Create an account at https://test.pypi.org/
   - Create a separate API token for TestPyPI
   - Modify the workflow temporarily to use TestPyPI:
     ```yaml
     - name: Publish to TestPyPI
       uses: pypa/gh-action-pypi-publish@release/v1
       with:
         user: __token__
         password: ${{ secrets.TEST_PYPI_API_TOKEN }}
         repository_url: https://test.pypi.org/legacy/
     ```

2. **Reserve your package name**:
   - You might want to upload a simple version first to reserve the name
   - Or use `twine` locally for the first upload

### 6. Workflow Triggers

The workflow runs on:
- **Push to main branch**: Builds only (no publishing)
- **Pull requests to main**: Builds only (no publishing)
- **Tags starting with 'v'**: Builds and publishes to PyPI
- **Manual trigger**: You can run it manually from the Actions tab

### 7. Troubleshooting

If the workflow fails:

1. **Check build logs**: Click on the failed job in Actions tab
2. **Common issues**:
   - Missing PYPI_API_TOKEN secret
   - Version already exists on PyPI (can't overwrite)
   - Build errors (missing dependencies, CMake issues)
   - Token permissions (make sure token has upload permissions)

3. **Test locally** with cibuildwheel:
   ```bash
   pip install cibuildwheel
   cibuildwheel --platform linux
   ```

## Summary Checklist

- [ ] Create PyPI account
- [ ] Generate PyPI API token
- [ ] Add PYPI_API_TOKEN to GitHub secrets
- [ ] Update version in setup.py, pyproject.toml, and __init__.py
- [ ] Commit and push changes
- [ ] Create and push version tag (e.g., v0.1.0)
- [ ] Monitor GitHub Actions for successful publication
- [ ] Verify package on https://pypi.org/project/vassar-arx-r5-sdk/

## Available Workflows

You now have two workflows:

1. **build-wheels.yml**: Original workflow (simple and straightforward)
2. **test-and-publish.yml**: Enhanced workflow with:
   - Import testing after building
   - Test PyPI support for testing releases
   - Manual workflow dispatch option

## Using Test PyPI (with enhanced workflow)

To test publishing before the real release:

1. Create Test PyPI account: https://test.pypi.org/account/register/
2. Create Test PyPI token and add as `TEST_PYPI_API_TOKEN` secret
3. Either:
   - Use manual trigger: Actions → test-and-publish.yml → Run workflow → Check "Publish to Test PyPI"
   - Or push a release candidate tag: `git tag v0.1.0rc1 && git push origin v0.1.0rc1`

## Notes

- The workflow only builds for Linux (as specified in your package requirements)
- It uses manylinux2014 for compatibility with older Linux distributions
- The package name on PyPI will be exactly: `vassar-arx-r5-sdk`
- Users will install it with: `pip install vassar-arx-r5-sdk`