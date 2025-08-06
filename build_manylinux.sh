#!/bin/bash
# Build manylinux wheels inside the manylinux container

set -e

# Install dependencies
yum install -y cmake3 || yum install -y cmake

# Build wheels for different Python versions
for PYBIN in /opt/python/cp3{8,9,10,11}*/bin; do
    "${PYBIN}/pip" install pybind11 numpy wheel
    "${PYBIN}/pip" wheel /io/ -w /io/wheelhouse/
done

# Repair wheels to be manylinux compliant
for whl in /io/wheelhouse/*.whl; do
    auditwheel repair "$whl" -w /io/dist/
done

# Clean up
rm -rf /io/wheelhouse