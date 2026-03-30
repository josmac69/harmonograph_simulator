# Harmonograph Simulator

A Python-based interactive simulator for a 4-pen harmonograph, allowing users to create complex geometric patterns by adjusting pendulum parameters in real-time.

## Features

- **Interactive Sliders**: Adjust Amplitudes (A), Frequencies (f), Phases (p), and Dampings (d) for four independent pendulums.
- **Real-time Visualization**: Watch the drawing pen trace the Lissajous-like figure as you adjust parameters.
- **Save Artwork**: Save the current drawing as a high-resolution PNG image.
- **Reset Functionality**: Instantly reset all parameters to their default values.
- **Command-line Interface**: Launch the simulator with custom initial parameters.

## Installation

1.  **Clone the repository** (or download the source code).

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running with Default Parameters

To start the simulator with the default settings:

```bash
./run.sh
```

### Running with Custom Parameters

You can override any default parameter from the command line. For example, to create a specific pattern:

```bash
python3 harmonograph.py --A1 3.0 --f1 2.5 --f2 1.5 --d1 0.002
```

### Controls

- **Sliders**: Drag the sliders to change the values. The drawing updates immediately.
- **Save Image**: Click the "Save Image" button to save the current drawing to a file (e.g., `harmonograph_1774868992.png`).
- **Reset**: Click the "Reset" button to restore all sliders to their initial values.

## License

MIT