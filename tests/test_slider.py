import sys
import matplotlib
matplotlib.use('Agg')
sys.path.append('.')
from planetary_harmonograph.simulator import PlanetaryHarmonographSimulator

app = PlanetaryHarmonographSimulator()
print("years value:", app.sliders['years'].val)
print("res value:", app.sliders['points_per_year'].val)
print("zoom value:", app.sliders['zoom'].val)
