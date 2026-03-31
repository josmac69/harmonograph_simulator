import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.collections import LineCollection
import argparse
import time

# Dictionary of planet parameters:
# format -> Planet: (Orbit Radius in AU, Orbit Period in Earth Years)
PLANETS = {
    'Mercury': (0.387, 0.241),
    'Venus':   (0.723, 0.615),
    'Earth':   (1.000, 1.000),
    'Mars':    (1.524, 1.881),
    'Jupiter': (5.203, 11.86),
    'Saturn':  (9.537, 29.46),
    'Uranus':  (19.19, 84.01),
    'Neptune': (30.07, 164.8)
}

class PlanetaryHarmonographSimulator:
    def __init__(self, **kwargs):
        self.params = {
            'p1_name': kwargs.get('p1', 'Earth'),
            'p2_name': kwargs.get('p2', 'Venus'),
            'years': kwargs.get('years', 8.0),
            'points_per_year': kwargs.get('res', 100),
            'zoom': kwargs.get('zoom', 1.0),
        }
        
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#111111')
        self.fig.canvas.manager.set_window_title('Planetary Harmonograph / Orbital Resonance')
        plt.subplots_adjust(left=0.35, bottom=0.15)
        self.ax.set_facecolor('#111111')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        for spine in self.ax.spines.values():
            spine.set_edgecolor('white')
            spine.set_linewidth(1.0)
            spine.set_visible(True)
        self.ax.set_aspect('equal')
        
        # We'll use a LineCollection for the connecting lines
        self.collection = LineCollection([], linewidths=0.5, alpha=0.3, colors='#00ffcc')
        self.ax.add_collection(self.collection)
        
        # Circles for orbits
        self.p1_orbit, = self.ax.plot([], [], color='#ff5555', linewidth=1.5, alpha=0.8, linestyle='--')
        self.p2_orbit, = self.ax.plot([], [], color='#55aaff', linewidth=1.5, alpha=0.8, linestyle='--')
        
        self.sliders = {}
        self.radios = {}
        self.create_gui()
        self.update(None)
        
    def calculate(self):
        p1 = PLANETS[self.params['p1_name']]
        p2 = PLANETS[self.params['p2_name']]
        
        R1, T1 = p1
        R2, T2 = p2
        
        total_years = self.params['years']
        num_points = int(total_years * self.params['points_per_year'])
        t = np.linspace(0, total_years, num_points)
        
        # Calculate instantaneous positions
        x1 = R1 * np.cos(2 * np.pi * t / T1)
        y1 = R1 * np.sin(2 * np.pi * t / T1)
        
        x2 = R2 * np.cos(2 * np.pi * t / T2)
        y2 = R2 * np.sin(2 * np.pi * t / T2)
        
        # Create line segments for the LineCollection
        # Each segment is an array of shape (2, 2) i.e. [[x1, y1], [x2, y2]]
        pts1 = np.column_stack((x1, y1))
        pts2 = np.column_stack((x2, y2))
        segments = np.stack((pts1, pts2), axis=1)
        
        # Full orbit paths for background reference
        theta = np.linspace(0, 2*np.pi, 200)
        orbit1_x = R1 * np.cos(theta)
        orbit1_y = R1 * np.sin(theta)
        
        orbit2_x = R2 * np.cos(theta)
        orbit2_y = R2 * np.sin(theta)
        
        return segments, (orbit1_x, orbit1_y), (orbit2_x, orbit2_y), max(R1, R2)
        
    def create_gui(self):
        axcolor = 'darkgray'
        
        # Sliders
        ax_zoom = plt.axes([0.35, 0.09, 0.45, 0.02], facecolor=axcolor)
        self.sliders['zoom'] = Slider(ax_zoom, 'Zoom', 1.0, 50.0, valinit=self.params.get('zoom', 1.0), valstep=0.1, color='#00ffcc')

        ax_years = plt.axes([0.35, 0.05, 0.45, 0.02], facecolor=axcolor)
        self.sliders['years'] = Slider(ax_years, 'Years', 1, 300, valinit=self.params['years'], valstep=1, color='#00ffcc')
        
        ax_res = plt.axes([0.35, 0.01, 0.45, 0.02], facecolor=axcolor)
        self.sliders['points_per_year'] = Slider(ax_res, 'Res (pts/yr)', 10, 500, valinit=self.params['points_per_year'], valstep=10, color='#00ffcc')
        
        for slider in self.sliders.values():
            slider.label.set_color('white')
            slider.valtext.set_color('white')
            slider.on_changed(self.update)
            
        # Radio buttons for planet selection
        labels = list(PLANETS.keys())
        
        ax_radio1 = plt.axes([0.05, 0.4, 0.12, 0.4], facecolor='#222222')
        self.radios['p1'] = RadioButtons(ax_radio1, labels, active=labels.index(self.params['p1_name']))
        for label in self.radios['p1'].labels: label.set_color('white')
        
        ax_radio2 = plt.axes([0.20, 0.4, 0.12, 0.4], facecolor='#222222')
        self.radios['p2'] = RadioButtons(ax_radio2, labels, active=labels.index(self.params['p2_name']))
        for label in self.radios['p2'].labels: label.set_color('white')
        
        # Label headers for Radio Buttons
        self.fig.text(0.11, 0.82, "Planet 1", color='white', ha='center', weight='bold')
        self.fig.text(0.26, 0.82, "Planet 2", color='white', ha='center', weight='bold')
        
        self.radios['p1'].on_clicked(self.update_p1)
        self.radios['p2'].on_clicked(self.update_p2)
        
        # Save Button
        ax_save = plt.axes([0.85, 0.02, 0.10, 0.04])
        self.btn_save = Button(ax_save, 'Save Image', hovercolor='0.9')
        self.btn_save.on_clicked(self.save_image)
        
    def update_p1(self, label):
        self.params['p1_name'] = label
        self.update(None)
        
    def update_p2(self, label):
        self.params['p2_name'] = label
        self.update(None)
        
    def update(self, val):
        if 'zoom' in self.sliders:
            self.params['zoom'] = self.sliders['zoom'].val
        self.params['years'] = self.sliders['years'].val
        self.params['points_per_year'] = self.sliders['points_per_year'].val
            
        segments, o1, o2, max_radius = self.calculate()
        
        # Update line collection
        self.collection.set_segments(segments)
        
        # Update orbit rings
        self.p1_orbit.set_data(o1[0], o1[1])
        self.p2_orbit.set_data(o2[0], o2[1])
        
        # Dynamic resizing based on maximum orbital radius
        limit = (max_radius * 1.05) / self.params.get('zoom', 1.0)
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.fig.canvas.draw_idle()
        
    def save_image(self, event):
        filename = f"planets_{self.params['p1_name']}_{self.params['p2_name']}_{int(time.time())}.png"
        extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        # Do not expand the extent to save only what is inside the graphical borders
        self.fig.savefig(filename, bbox_inches=extent, facecolor='#111111', dpi=300)
        print(f"Saved planetary artwork to {filename}")

    def show(self):
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Planetary Harmonograph (Orbital Resonance)")
    parser.add_argument('--p1', type=str, default='Earth', help='Planet 1')
    parser.add_argument('--p2', type=str, default='Venus', help='Planet 2')
    parser.add_argument('--years', type=float, default=8.0, help='Total simulated years')
    parser.add_argument('--zoom', type=float, default=1.0, help='Initial zoom factor')
    args = parser.parse_args()
    
    app = PlanetaryHarmonographSimulator(**vars(args))
    app.show()

if __name__ == "__main__":
    main()
