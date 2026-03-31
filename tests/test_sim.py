import sys
sys.path.append('.')
from planetary_harmonograph.simulator import PlanetaryHarmonographSimulator

app = PlanetaryHarmonographSimulator(years=8.0, res=100, zoom=1.0)
segments, o1, o2, rmax = app.calculate()
print("segments shape:", segments.shape)
print("segments [0]:\n", segments[0])
print("segments [-1]:\n", segments[-1])
print("max_radius:", rmax)
