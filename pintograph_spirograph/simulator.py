import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import argparse
import time

class SpirographSimulator:
    def __init__(self, **kwargs):
        self.params = {
            'R': kwargs.get('R', 4.0),
            'r': kwargs.get('r', 1.0),
            'd': kwargs.get('d', 1.0),
        }
        
        # Calculate maximum theta depending on the ratio of R and r.
        # We need a long enough path to close the loop.
        self.t = np.linspace(0, 100 * np.pi, 20000)
        
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#111111')
        self.fig.canvas.manager.set_window_title('Pintograph / Spirograph Simulator')
        plt.subplots_adjust(left=0.1, bottom=0.3)
        self.ax.set_facecolor('#111111')
        self.ax.axis('off')
        
        x, y = self.calculate()
        self.line, = self.ax.plot(x, y, color='#00ffcc', linewidth=1.0, alpha=0.9)
        self.ax.set_aspect('equal')
        
        self.sliders = {}
        self.create_sliders()
        self.create_buttons()
        
    def calculate(self):
        p = self.params
        R, r, d = p['R'], p['r'], p['d']
        
        # Prevent division by zero
        if r == 0:
            r = 0.001
            
        x = (R - r) * np.cos(self.t) + d * np.cos((R - r) / r * self.t)
        y = (R - r) * np.sin(self.t) - d * np.sin((R - r) / r * self.t)
        return x, y
        
    def create_sliders(self):
        axcolor = 'darkgray'
        left = 0.2
        width = 0.6
        height = 0.03
        
        # Slider for R (fixed disk radius)
        ax_R = plt.axes([left, 0.20, width, height], facecolor=axcolor)
        self.sliders['R'] = Slider(ax_R, 'R', 0.1, 10.0, valinit=self.params['R'], color='#00ffcc')
        
        # Slider for r (moving disk radius)
        ax_r = plt.axes([left, 0.15, width, height], facecolor=axcolor)
        self.sliders['r'] = Slider(ax_r, 'r', 0.1, 10.0, valinit=self.params['r'], color='#00ffcc')
        
        # Slider for d (pen offset from center of moving disk)
        ax_d = plt.axes([left, 0.10, width, height], facecolor=axcolor)
        self.sliders['d'] = Slider(ax_d, 'd', 0.0, 10.0, valinit=self.params['d'], color='#00ffcc')
        
        for slider in self.sliders.values():
            slider.label.set_color('white')
            slider.valtext.set_color('white')
            slider.on_changed(self.update)

    def create_buttons(self):
        ax_save = plt.axes([0.45, 0.02, 0.15, 0.05])
        self.btn_save = Button(ax_save, 'Save Image', hovercolor='0.9')
        self.btn_save.on_clicked(self.save_image)
        
    def update(self, val):
        self.params['R'] = self.sliders['R'].val
        self.params['r'] = self.sliders['r'].val
        self.params['d'] = self.sliders['d'].val
            
        x, y = self.calculate()
        self.line.set_data(x, y)
        
        # Dynamic resizing
        limit = max(np.max(np.abs(x)), np.max(np.abs(y))) + 0.5
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.fig.canvas.draw_idle()
        
    def save_image(self, event):
        filename = f"spirograph_{int(time.time())}.png"
        extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        extent = extent.expanded(1.1, 1.1)
        self.fig.savefig(filename, bbox_inches=extent, facecolor='#111111', dpi=300)
        print(f"Saved spirograph artwork to {filename}")

    def show(self):
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Pintograph / Spirograph Generator")
    parser.add_argument('--R', type=float, default=4.0, help='Radius of fixed circle')
    parser.add_argument('--r', type=float, default=1.0, help='Radius of moving circle')
    parser.add_argument('--d', type=float, default=1.0, help='Distance from center of moving circle')
    args = parser.parse_args()
    
    app = SpirographSimulator(**vars(args))
    app.show()

if __name__ == "__main__":
    main()
