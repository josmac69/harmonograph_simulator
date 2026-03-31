import sys
import numpy as np
sys.path.append('.')
from planetary_harmonograph.simulator import PlanetaryHarmonographSimulator

app2 = PlanetaryHarmonographSimulator(years=8.0, res=100, zoom=1.0)
s2, _, _, _ = app2.calculate()
np.save('new_segments.npy', s2)

s1 = np.load('old_segments.npy')
print("Shapes match?", s1.shape == s2.shape)
print("Arrays equal?", np.allclose(s1, s2))
