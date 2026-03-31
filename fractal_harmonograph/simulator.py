import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import argparse
import time

class FractalHarmonographSimulator:
    def __init__(self, **kwargs):
        self.params = {
            'depth': kwargs.get('depth', 3),
            'freq_x': kwargs.get('freq_x', 2.0),
            'freq_y': kwargs.get('freq_y', 3.0),
            'scale': kwargs.get('scale', 0.4),
            'freq_multiplier': kwargs.get('freq_multiplier', 3.0),
            'phase': kwargs.get('phase', 1.57),
            'zoom': kwargs.get('zoom', 1.0)
        }
        
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#111111')
        self.fig.canvas.manager.set_window_title('Fractal Harmonograph Simulator')
        plt.subplots_adjust(left=0.15, bottom=0.35)
        self.ax.set_facecolor('#111111')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        for spine in self.ax.spines.values():
            spine.set_edgecolor('white')
            spine.set_linewidth(1.0)
            spine.set_visible(True)
        self.ax.set_aspect('equal')
        
        self.line, = self.ax.plot([], [], color='cyan', linewidth=0.5, alpha=0.9)
        
        self.sliders = {}
        self.create_gui()
        self.update(None)
        
    def calculate(self):
        depth = int(self.params['depth'])
        freq_x = self.params['freq_x']
        freq_y = self.params['freq_y']
        scale = self.params['scale']
        freq_mult = self.params['freq_multiplier']
        phase = self.params['phase']
        
        t = np.linspace(0, 100 * np.pi, 100000)
        X = np.zeros_like(t)
        Y = np.zeros_like(t)
        
        for k in range(depth):
            current_scale = scale ** k
            current_freq_mult = freq_mult ** k
            X += current_scale * np.sin(freq_x * current_freq_mult * t + phase * k)
            Y += current_scale * np.sin(freq_y * current_freq_mult * t)
            
        return X, Y
        
    def create_gui(self):
        axcolor = 'darkgray'
        
        # Sliders
        ax_depth = plt.axes([0.2, 0.25, 0.6, 0.02], facecolor=axcolor)
        self.sliders['depth'] = Slider(ax_depth, 'Depth', 1, 10, valinit=self.params['depth'], valstep=1, color='#00ffcc')
        
        ax_freq_x = plt.axes([0.2, 0.21, 0.6, 0.02], facecolor=axcolor)
        self.sliders['freq_x'] = Slider(ax_freq_x, 'Freq X', 0.1, 10.0, valinit=self.params['freq_x'], valstep=0.1, color='#00ffcc')
        
        ax_freq_y = plt.axes([0.2, 0.17, 0.6, 0.02], facecolor=axcolor)
        self.sliders['freq_y'] = Slider(ax_freq_y, 'Freq Y', 0.1, 10.0, valinit=self.params['freq_y'], valstep=0.1, color='#00ffcc')

        ax_scale = plt.axes([0.2, 0.13, 0.6, 0.02], facecolor=axcolor)
        self.sliders['scale'] = Slider(ax_scale, 'Scale', 0.1, 1.0, valinit=self.params['scale'], valstep=0.01, color='#00ffcc')

        ax_mult = plt.axes([0.2, 0.09, 0.6, 0.02], facecolor=axcolor)
        self.sliders['freq_multiplier'] = Slider(ax_mult, 'Freq Mult', 1.0, 10.0, valinit=self.params['freq_multiplier'], valstep=0.1, color='#00ffcc')

        ax_phase = plt.axes([0.2, 0.05, 0.6, 0.02], facecolor=axcolor)
        self.sliders['phase'] = Slider(ax_phase, 'Phase', 0.0, 2*np.pi, valinit=self.params['phase'], valstep=0.01, color='#00ffcc')

        ax_zoom = plt.axes([0.2, 0.01, 0.6, 0.02], facecolor=axcolor)
        self.sliders['zoom'] = Slider(ax_zoom, 'Zoom', 1.0, 50.0, valinit=self.params['zoom'], valstep=0.1, color='#00ffcc')
        
        for slider in self.sliders.values():
            slider.label.set_color('white')
            slider.valtext.set_color('white')
            slider.on_changed(self.update)
            
        # Save Button
        ax_save = plt.axes([0.85, 0.02, 0.10, 0.04])
        self.btn_save = Button(ax_save, 'Save Image', hovercolor='0.9')
        self.btn_save.on_clicked(self.save_image)
        
    def update(self, val):
        for k in self.sliders:
            self.params[k] = self.sliders[k].val
            
        X, Y = self.calculate()
        self.line.set_data(X, Y)
        
        max_extent = max(np.max(np.abs(X)), np.max(np.abs(Y)))
        if max_extent == 0:
            max_extent = 1.0
            
        limit = (max_extent * 1.05) / self.params['zoom']
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.ax.set_title(f"Fractal Harmonograph\nDepth: {int(self.params['depth'])} | Base Freq: ({self.params['freq_x']:.1f}, {self.params['freq_y']:.1f}) | Zoom: {self.params['zoom']:.1f}x", color='white', pad=20)
        self.fig.canvas.draw_idle()
        
    def save_image(self, event):
        filename = f"fractal_{int(time.time())}.png"
        extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        self.fig.savefig(filename, bbox_inches=extent, facecolor='#111111', dpi=300)
        print(f"Saved fractal artwork to {filename}")

    def show(self):
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Fractal Harmonograph Simulator")
    parser.add_argument('--depth', type=int, default=3, help='Recursive depth')
    parser.add_argument('--freq_x', type=float, default=2.0)
    parser.add_argument('--freq_y', type=float, default=3.0)
    parser.add_argument('--scale', type=float, default=0.4)
    parser.add_argument('--freq_multiplier', type=float, default=3.0)
    parser.add_argument('--phase', type=float, default=1.57)
    parser.add_argument('--zoom', type=float, default=1.0)
    args = parser.parse_args()
    
    app = FractalHarmonographSimulator(**vars(args))
    app.show()

if __name__ == "__main__":
    main()
