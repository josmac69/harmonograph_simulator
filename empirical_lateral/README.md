# Empirical Lateral Harmonograph

This variant simulates the classic "multi-sinusoid" harmonograph. Rather than simulating the physical forces and non-linearities of the device, it utilizes a deeply empirical approximation based on the superposition of exponentially damped sinusoids acting on orthogonal (X and Y) axes. 

## Mechanism
While not a first-principles model, this is the most common visual representation of a harmonograph. It assumes four "virtual" pendulums (two acting on the X-axis, two on the Y-axis), each with its own independent frequency, phase, amplitude, and linear viscous damping coefficient.

## Usage
Run the interactive simulator using:
```bash
python harmonograph.py
```
Use the Matplotlib GUI sliders to dynamically adjust:
- **A1-A4**: Initial amplitudes
- **f1-f4**: Frequencies 
- **p1-p4**: Phase offsets
- **d1-d4**: Damping coefficients

## Visual Characteristics 
- Perfect for exploring Lissajous-like repeating geometry
- Generates precise rosettes, decaying loops, and dense moiré patterns
- Extremely fast to compute, as it relies on vectorized continuous trigonometric arrays rather than numerical time-stepping integration.
