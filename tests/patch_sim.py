with open("planetary_harmonograph/simulator.py", "r") as f:
    code = f.read()

# Make sure we don't accidentally do bad string replacement
code = code.replace(
    "num_points = int(total_years * self.params['points_per_year'])",
    """# Scale resolution with zoom to prevent jagged polygons at high zoom levels
        zoom_factor = max(1.0, self.params.get('zoom', 1.0) / 2.0)
        effective_pts_per_year = self.params['points_per_year'] * zoom_factor
        num_points = int(total_years * effective_pts_per_year)
        # Cap to prevent memory issues but allow dense resonance patterns
        num_points = max(100, min(1000000, num_points))"""
)

code = code.replace(
    "self.collection.set_segments(segments)",
    """self.collection.set_segments(segments)
        
        # Adjust line visual density based on years simulated, to prevent solid blocks of white/cyan
        # when simulating hundreds of years of orbits
        years = self.params.get('years', 8.0)
        density_ratio = max(1.0, years / 8.0)
        new_alpha = max(0.02, 0.3 / (density_ratio ** 0.5))
        new_lw = max(0.05, 0.5 / (density_ratio ** 0.5))
        self.collection.set_alpha(new_alpha)
        self.collection.set_linewidth(new_lw)"""
)

with open("planetary_harmonograph/simulator.py", "w") as f:
    f.write(code)

print("Patched!")
