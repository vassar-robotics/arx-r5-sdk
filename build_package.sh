#!/bin/bash

# Build script for ARX R5 SDK package

echo "Building ARX R5 SDK package..."

# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build source distribution and wheel
python -m pip install --upgrade pip setuptools wheel
python -m pip install pybind11 cmake

# Build the package
python setup.py sdist bdist_wheel

echo "Build complete. Check dist/ directory for packages."
echo ""
echo "To test installation locally:"
echo "  pip install dist/vassar-arx-r5-sdk-*.whl"
echo ""
echo "To upload to PyPI:"
echo "  pip install twine"
echo "  twine upload dist/*"