# Pintograph and Spirograph Kinematics

This variant simulates the kinematic motion of rotating disks and rigid linkages, rather than pendulums responding to gravity. Historically, these mechanics align with spirographs, modern motorised drawing machines, and Ford Pinto-inspired "pintograph" mechanisms.

## Mechanism
This simulator specifically models Epitrochoid / Hypotrochoid geometries driven by relative rotations. The pen position is structurally constrained by the relative motion of a moving disk rolling around a fixed base disk.

The parametric equations utilized are:
- `x(θ) = (R - r) cos(θ) + d cos((R-r)/r * θ)`
- `y(θ) = (R - r) sin(θ) - d sin((R-r)/r * θ)`

## Usage
Run the interactive simulator using:
```bash
python simulator.py
```
Use the Matplotlib GUI sliders to tune the linkage parameters:
- **R**: Radius of the fixed base circle.
- **r**: Radius of the moving orbital circle.
- **d**: Distance of the pen nib from the center of the moving circle.

## Visual Characteristics
Unlike decaying pendulums, the resulting curves are perfectly periodic and do not "decay" towards the center. The mathematical ratio of `R` to `r` dictates symmetry. For example, setting `R/r` to exactly `4` yields a crisp four-pointed hypocycloid, while a slight detuning, like `R/r = 3.01`, produces a slowly sweeping flower with dense, repeating layers before the loop closes.
