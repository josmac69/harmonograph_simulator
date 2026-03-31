# Fractal Harmonograph

This architecture extends the classical concept of a harmonograph into the mathematical realm of fractals by applying recursive trigonometric layering. Instead of simulating physical pendulums, it plots accumulated sinusoidal equations, adding increasingly smaller, higher-frequency waves on top of each other.

## Mechanism
The rendering function generates continuous X/Y coordinates by accumulating waves over a parametric time variable `t`. For each 'Depth' layer added:
- The base frequencies (`Freq X`, `Freq Y`) are multiplied by `Freq Mult`.
- The amplitude (`Scale`) of the additional wave is reduced mathematically.
- A controlled `Phase` offset is introduced to create complex angular variations.

The result is a distinct, infinite-looking fractal curve that mimics the complexities found in theoretical chaos patterns but built entirely from deterministic, clean sine waves.

### Selectable Formulas
You can toggle the core underlying geometry using the radio buttons on the left:
1. **Lissajous**: The standard orthogonal phase calculation `(X=sin, Y=sin)`. Creates woven, grid-like harmonic shapes.
2. **Rose**: Uses a radial accumulation `r=sin(theta)`. Synthesizes recursive flower petals growing out of the tips of primary petals.
3. **Epicycle**: Mimics nested circles (akin to planetary epicycles or complex spirographs). Draws sharp, stellar geometric patterns rotating in symmetry `(X=cos(a)+cos(b), Y=sin(a)-sin(b))`.

## Usage
Run the interactive simulator using:
```bash
python simulator.py
```

Use the GUI controls to tune:
- **Depth**: The number of recursive harmonic layers stacked together. 1 equals a simple primary curve, while higher depths create intricate, fuzzy, complex fractal outlines.
- **Freq X / Freq Y**: The base frequencies determining the primary shape of the harmonograph.
- **Scale**: How much the amplitude is reduced for each consecutive layer (must be < 1.0 to converge nicely).
- **Freq Mult**: The frequency multiplier applied sequentially to each layer.
- **Phase**: An angular shift added per recursive depth.
- **Zoom**: Allows you to zoom into the geometric figure. The simulation viewport is delineated by a white quadratic border. When you click "Save Image", the exact view within these boundaries is saved.
