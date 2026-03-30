#!/bin/bash
set -e

# Default directory for virtual environment
VENV_DIR=".venv"

cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install requirements
echo "Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

# Run the harmonograph simulator
echo "Starting Interactive Harmonograph Simulator..."
python draft_version/harmonograph.py "$@"
