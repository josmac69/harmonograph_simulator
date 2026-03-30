# Coupled Pendulums

This variant simulates two parallel pendulums that are connected via a mechanical spring. Rather than swinging independently, energy is constantly exchanged back and forth through the spring coupling.

## Mechanism
The mathematical representation requires tracking the coupling constant (spring stiffness) alongside the gravitational restorative forces and viscous damping. The corresponding linear coupled ODEs are evaluated using the `scipy.integrate.solve_ivp` solver.

When energy transfers back and forth, it results in "beat frequencies"—one pendulum decays to a near-complete stop while the second pendulum simultaneously absorbs that energy and swings at maximum amplitude, before the cycle reverses.

## Usage
Run the interactive simulator using:
```bash
python simulator.py
```
Use the GUI sliders to tune:
- **Coupling (k)**: The stiffness of the spring connecting them. A stronger spring transfers energy much faster.
- **w1², w2²**: The squares of the natural frequencies (inversely proportional to pendulum length).
- **Damping c1, c2**: Viscous friction parameters.
- **Init θ1, θ2**: The initial starting angles.

## Visual Characteristics
Produces a trace that bulges and pinches in sweeping, undulating patterns ("beats") as the energy sloshes between the two axes, causing the trajectory to rotate and morph symmetrically over long periods.
