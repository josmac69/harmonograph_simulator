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

echo ""
echo "Please select a harmonograph architecture to simulate:"
options=(
    "Empirical Lateral Harmonograph (Classic)" 
    "Pintograph & Spirograph" 
    "Coupled Pendulums" 
    "Chaotic Double Pendulum" 
    "Planetary Motions (Orbital Resonance)"
    "Quit"
)

select opt in "${options[@]}"; do
    case "$REPLY" in
        1)
            echo "Starting Empirical Lateral Simulator..."
            python empirical_lateral/harmonograph.py "$@"
            break
            ;;
        2)
            echo "Starting Pintograph / Spirograph Simulator..."
            python pintograph_spirograph/simulator.py "$@"
            break
            ;;
        3)
            echo "Starting Coupled Pendulums Simulator..."
            python coupled_pendulums/simulator.py "$@"
            break
            ;;
        4)
            echo "Starting Chaotic Double Pendulum Simulator..."
            python chaotic_double_pendulum/simulator.py "$@"
            break
            ;;
        5)
            echo "Starting Planetary Harmonograph Simulator..."
            python planetary_harmonograph/simulator.py "$@"
            break
            ;;
        6)
            echo "Exiting."
            exit 0
            ;;
        *)
            echo "Invalid option. Please enter a number from 1 to 6."
            ;;
    esac
done
