# Planetary Harmonograph (Dance of the Planets)

This variant visualizes the orbital resonance and relative geometry between any two planets in the solar system. Rather than using pendulums or rotating gears, this algorithm draws straight cords connecting the actual simulated positions of two planets over time.

## Mechanism
The simulator assumes circular, coplanar orbits. It calculates the instantaneous position of both selected planets based on their semimajor axes (in AU) and orbital periods (in Earth-years). 

At regular geometric intervals, it draws a semi-transparent straight line between `(P1_x, P1_y)` and `(P2_x, P2_y)`. Over hundreds of orbits, the envelope of these discrete lines forms beautiful, continuous geometric rosettes—often referred to as the "Dance of the Planets".

## Usage
Run the interactive simulator using:
```bash
python simulator.py
```
Use the GUI controls to tune:
- **Planet 1 & Planet 2**: Radio buttons to select the two planetary bodies you wish to simulate.
- **Years**: The total number of Earth-years to simulate. (For outer planets like Neptune, you may need to increase this significantly!).
- **Res (pts/yr)**: The resolution or density of the drawing. Determines how many connecting lines are drawn per simulated Earth-year. 

## Visual Characteristics
For perfectly resonant planets, the geometry closes into striking rosettes. For example, the famous Earth-Venus pair completes a distinct 5-petaled flower over exactly 8 Earth years, mirroring their 8:13 orbital resonance. Combining vastly disparate planets (like Mercury and Neptune) results in a dense annulus rather than a simple flower.
