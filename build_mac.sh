#!/bin/bash
# Build script for Mac executable
# Run this script on a Mac system

echo "Building Mac executable for MouseMover..."
echo "Make sure you have Python and pip installed"

# Install dependencies
echo "Installing dependencies..."
pip3 install pyautogui pyinstaller

# Build the executable
echo "Creating Mac executable..."
pyinstaller --onefile --windowed --name MouseMover-Mac mouse_mover.py

echo "Build complete! The Mac executable is in the dist/ folder."
echo "File: MouseMover-Mac" 