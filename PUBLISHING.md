# Publishing vassar-arx-r5-sdk to PyPI

## Prerequisites

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Create a PyPI account at https://pypi.org/account/register/

3. Create an API token:
   - Go to https://pypi.org/manage/account/
   - Scroll to "API tokens" and create a new token
   - Save the token securely

## Building the Package

### Option 1: Build Locally (for testing)
```bash
# Build source distribution and wheel
./build_package.sh
```

### Option 2: Build manylinux wheels (recommended for PyPI)
Use GitHub Actions or build locally with cibuildwheel:

```bash
# Build manylinux wheels for current platform
pip install cibuildwheel
cibuildwheel --platform linux

# Or use Docker to build for multiple platforms
docker run --rm -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64 /io/build_manylinux.sh
```

## Testing the Package

1. Create a virtual environment:
   ```bash
   python -m venv test_env
   source test_env/bin/activate  # On Linux
   ```

2. Install the package locally:
   ```bash
   pip install dist/vassar-arx-r5-sdk-*.whl
   ```

3. Test the import:
   ```python
   python -c "from vassar_arx_r5_sdk.bimanual import SingleArm; print('Import successful!')"
   ```

## Publishing to PyPI

### First Time Setup
Configure your PyPI credentials:
```bash
# Create ~/.pypirc file
cat > ~/.pypirc << EOF
[pypi]
username = __token__
password = <your-api-token>
EOF

chmod 600 ~/.pypirc
```

### Upload to Test PyPI (recommended first)
```bash
# Upload to test PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Test installation from test PyPI
pip install --index-url https://test.pypi.org/simple/ vassar-arx-r5-sdk
```

### Upload to Production PyPI
```bash
twine upload dist/*
```

## Version Management

1. Update version in:
   - `setup.py`
   - `pyproject.toml`
   - `vassar_arx_r5_sdk/__init__.py`

2. Create a git tag:
   ```bash
   git tag -a v0.1.0 -m "Initial release"
   git push origin v0.1.0
   ```

## GitHub Actions

The repository includes a GitHub Actions workflow that:
1. Builds manylinux wheels for x86_64 and aarch64
2. Builds for Python 3.8-3.11
3. Automatically uploads to PyPI on tagged releases

To use it:
1. Add `PYPI_API_TOKEN` to your repository secrets
2. Push a tag starting with 'v' (e.g., v0.1.0)

## Platform Notes

- This package only supports Linux due to CAN interface requirements
- Wheels are built for:
  - manylinux_x86_64 (Intel/AMD 64-bit)
  - manylinux_aarch64 (ARM 64-bit)
- Python 3.6+ is supported

## Troubleshooting

If the package fails to build:
1. Ensure CMake and pybind11 are installed
2. Check that all C++ headers are included in MANIFEST.in
3. Verify the CMakeLists.txt paths are correct

If users report import errors:
1. Check they're on a supported Linux distribution
2. Verify they have the required system libraries
3. Ensure the .so files are properly included in the wheel