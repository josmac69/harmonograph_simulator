# Chaotic Double Pendulum

This variant simulates a two-joint swinging arm (or classic double pendulum) driving a pen point. Compared to linear harmonographs, this architecture naturally produces both smooth quasi-periodic motion and wild chaotic transitions depending on energy and damping.

## Mechanism
While classical harmonographs rely on linear uncoupled ODEs, the double pendulum is a non-linear dynamical system modeled using Lagrangian mechanics. Calculating the trajectory of the outer bob requires numerical time-stepping integration (via `scipy.integrate.solve_ivp` using an RK45 solver) rather than instantaneous analytical closed forms.

The resulting curves are no longer simple exponential decaying envelopes, but can fold back on themselves unpredictably, exhibiting extreme sensitivity to initial conditions.

## Usage
Run the interactive simulator using:
```bash
python simulator.py
```
Use the GUI sliders to tune:
- **Mass 2**: The mass of the outer pendulum bob.
- **Length 2**: The length of the outer pendulum arm.
- **Init θ1, θ2**: The exact starting release angles. Sub-millimeter adjustments to these values can completely alter the resulting drawing.
- **Damping c1, d2**: Friction acting on the joints.

## Visual Characteristics
Produces filigree-like scribbles, sudden motif changes, and thick "scribble" clusters. Because the system is deterministic yet chaotic, the drawn lines can suddenly change direction violently before settling into recognizable orbits as energy dissipates.
