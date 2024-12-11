#!/bin/bash

# Exit the script if any command fails
set -e

# Step 1: Clean up old builds
echo "Cleaning up old builds..."
rm -rf build/ dist/ *.egg-info

# Step 2: Build the package
echo "Building the package..."
python setup.py sdist bdist_wheel

# Step 3: Install the package
echo "Installing the package..."
pip install dist/*.whl

echo "Done! The module has been built and installed."
