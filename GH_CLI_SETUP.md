# GitHub CLI Setup Guide for Workflow

Your repository is already connected to GitHub at: https://github.com/vassar-robotics/arx-r5-sdk

Let's use the GitHub CLI to set up everything for automated PyPI publishing.

## 1. Install GitHub CLI (if not already installed)

### macOS (using Homebrew)
```bash
brew install gh
```

### Or download from
https://cli.github.com/

## 2. Authenticate GitHub CLI

```bash
# Login to GitHub
gh auth login

# Follow the prompts:
# - Choose: GitHub.com
# - Choose: HTTPS
# - Authenticate with: Login with a web browser
# - Copy the one-time code and press Enter to open browser
```

Verify authentication:
```bash
gh auth status
```

## 3. Create PyPI Account and Token

First, create your PyPI account and token:

1. Go to https://pypi.org/account/register/
2. Create account and verify email
3. Go to https://pypi.org/manage/account/
4. Scroll to "API tokens" → "Add API token"
5. Name: "vassar-arx-r5-sdk GitHub Actions"
6. Scope: "Entire account" (for first time) or select project later
7. Copy the token (starts with `pypi-`)

## 4. Add PyPI Secret to GitHub Repository

```bash
# Add PyPI token as repository secret
gh secret set PYPI_API_TOKEN --repo vassar-robotics/arx-r5-sdk

# Paste your PyPI token when prompted and press Ctrl+D (or Cmd+D on Mac)
```

## 5. (Optional) Add Test PyPI Token

If you want to test releases on Test PyPI first:

```bash
# Create account at https://test.pypi.org/
# Generate token same way as above
gh secret set TEST_PYPI_API_TOKEN --repo vassar-robotics/arx-r5-sdk
```

## 6. Verify Secrets

```bash
# List secrets (names only, values are hidden)
gh secret list --repo vassar-robotics/arx-r5-sdk
```

## 7. Initialize Git and Push Code

Since your repo is already connected, just push your changes:

```bash
# Add all files
git add .

# Commit
git commit -m "Add GitHub workflows for PyPI publishing"

# Push to main branch
git push origin main
```

## 8. Test the Workflow

### Option A: Test Build Only (without publishing)
```bash
# Push to a test branch
git checkout -b test-workflow
git push origin test-workflow

# Watch the workflow run
gh run watch --repo vassar-robotics/arx-r5-sdk
```

### Option B: Manual Workflow Run (with new enhanced workflow)
```bash
# List workflows
gh workflow list --repo vassar-robotics/arx-r5-sdk

# Run the test-and-publish workflow manually
gh workflow run test-and-publish.yml --repo vassar-robotics/arx-r5-sdk

# View runs
gh run list --repo vassar-robotics/arx-r5-sdk
```

## 9. Create Your First Release

When ready to publish to PyPI:

```bash
# Ensure you're on main branch
git checkout main
git pull origin main

# Create and push a version tag
git tag -a v0.1.0 -m "Initial release: Python SDK for ARX R5 Robot"
git push origin v0.1.0

# Watch the release workflow
gh run watch --repo vassar-robotics/arx-r5-sdk
```

## 10. Monitor Workflow Status

```bash
# View recent workflow runs
gh run list --repo vassar-robotics/arx-r5-sdk

# View specific run details
gh run view <run-id> --repo vassar-robotics/arx-r5-sdk

# Watch a running workflow
gh run watch --repo vassar-robotics/arx-r5-sdk

# View workflow logs if something fails
gh run view <run-id> --log --repo vassar-robotics/arx-r5-sdk
```

## Quick Commands Reference

```bash
# Add secret
gh secret set PYPI_API_TOKEN --repo vassar-robotics/arx-r5-sdk

# List secrets
gh secret list --repo vassar-robotics/arx-r5-sdk

# Trigger workflow manually
gh workflow run test-and-publish.yml --repo vassar-robotics/arx-r5-sdk

# View runs
gh run list --repo vassar-robotics/arx-r5-sdk

# Watch latest run
gh run watch --repo vassar-robotics/arx-r5-sdk

# Create release
gh release create v0.1.0 --title "v0.1.0" --notes "Initial release" --repo vassar-robotics/arx-r5-sdk
```

## Troubleshooting

If you get permission errors:
```bash
# Check your authentication
gh auth status

# Refresh authentication
gh auth refresh

# Check repository access
gh repo view vassar-robotics/arx-r5-sdk
```

If workflow fails:
```bash
# View failed run logs
gh run list --repo vassar-robotics/arx-r5-sdk
gh run view <run-id> --log --repo vassar-robotics/arx-r5-sdk
```