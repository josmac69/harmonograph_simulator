import sys
import numpy as np

# Load old simulator
import subprocess
try:
    subprocess.run(['git', 'checkout', 'HEAD~1', 'planetary_harmonograph/simulator.py'], check=True)
except Exception as e:
    print(f"Error checking out: {e}")

sys.path.append('.')
from planetary_harmonograph.simulator import PlanetaryHarmonographSimulator

app1 = PlanetaryHarmonographSimulator(years=8.0, res=100, zoom=1.0)
s1, _, _, _ = app1.calculate()
np.save('old_segments.npy', s1)

# Restore new simulator
subprocess.run(['git', 'checkout', 'HEAD', 'planetary_harmonograph/simulator.py'])

# We cannot easily re-import the module in the same process, so we just run a second script
