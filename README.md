# Harmonograph Simulator

A collection of Python-based interactive simulators modeling different architectures of mathematical drawing machines. By translating the physical kinematic constraints of lateral pendulums, motorized pintograph linkages, and chaotic coupled dynamical systems into rigorous Python arrays, these scripts allow for real-time generative exploration far surpassing the physical limitations of wood and brass.

## Available Architectures

This repository contains four distinct simulation architectures, each isolated in its own directory with a dedicated README:

1. **[Empirical Lateral Harmonograph](empirical_lateral/README.md)**
   - **Type**: Linear superposition of damped sinusoids.
   - **Characteristics**: Extremely fast, predictable. Used for exploring Lissajous-like repeating geometric figures and moiré patterns without full physical constraints.
   - **Run**: `cd empirical_lateral && python harmonograph.py`

2. **[Pintograph & Spirograph](pintograph_spirograph/README.md)**
   - **Type**: Kinematic motion of rotating disks and rigid linkages.
   - **Characteristics**: Constant-speed parametric curves (Epitrochoid / Hypotrochoid). Produces perfectly repeating, non-decaying geometric blooms.
   - **Run**: `cd pintograph_spirograph && python simulator.py`

3. **[Coupled Pendulums](coupled_pendulums/README.md)**
   - **Type**: Linear spring-coupled oscillators.
   - **Characteristics**: Energy sloshes back and forth between two pendulums connected by a simulated mechanical spring, resulting in sweeping, undulating "beat" patterns.
   - **Run**: `cd coupled_pendulums && python simulator.py`

4. **[Chaotic Double Pendulum](chaotic_double_pendulum/README.md)**
   - **Type**: Non-linear dynamical system (Lagrangian mechanics).
   - **Characteristics**: A deterministically chaotic system solved using `scipy.integrate.solve_ivp`. Traces highly unpredictable scribbles that fold back on themselves violently before dissipating energy. Highly sensitive to initial release angles.
   - **Run**: `cd chaotic_double_pendulum && python simulator.py`

## Shared Features (Interactive GUI)
Every simulator is built identically using standard `matplotlib`:
- **Real-time Vectorization**: Watch the drawing update at 60Hz as you slide parameters.
- **Physical Parameter Tuning**: Dynamically adjust parameters acting as surrogates for physical properties (like damping, masses, linkage radii, spring stiffness).
- **Export Artwork**: One-click saving of the generated plots directly to high-resolution PNGs.

## Installation

1. **Clone the repository** (or download the source code).

2. **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## External Research & References
The variants included here are based on the extensive taxonomy detailed in the historical literature and physical kinematics presented in the `docs/` directory.

## License
MIT