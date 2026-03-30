import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import argparse
import time

class InteractiveHarmonograph:
    def __init__(self, **kwargs):
        # Default parameters loaded from kwargs
        self.params = {
            'A1': kwargs.get('A1', 2.0), 'A2': kwargs.get('A2', 2.0), 
            'A3': kwargs.get('A3', 2.0), 'A4': kwargs.get('A4', 2.0),
            
            'f1': kwargs.get('f1', 3.0), 'f2': kwargs.get('f2', 2.0), 
            'f3': kwargs.get('f3', 1.001), 'f4': kwargs.get('f4', 2.0),
            
            'p1': kwargs.get('p1', np.pi/2), 'p2': kwargs.get('p2', 0.0), 
            'p3': kwargs.get('p3', np.pi/4), 'p4': kwargs.get('p4', np.pi/2),
            
            'd1': kwargs.get('d1', 0.001), 'd2': kwargs.get('d2', 0.001), 
            'd3': kwargs.get('d3', 0.001), 'd4': kwargs.get('d4', 0.001)
        }
        
        self.t = np.linspace(0, 100, 100000)
        
        # Setup the main figure and axis
        self.fig, self.ax = plt.subplots(figsize=(12, 8), facecolor='black')
        self.fig.canvas.manager.set_window_title('Interactive Harmonograph Simulator')
        
        # Adjust layout to make room for sliders on the left and buttons on bottom
        plt.subplots_adjust(left=0.35, bottom=0.1)
        
        self.ax.set_facecolor('black')
        self.ax.axis('off')
        
        # Calculate initial path and plot
        x, y = self.calculate()
        self.line, = self.ax.plot(x, y, color='cyan', linewidth=0.5, alpha=0.7)
        self.ax.set_aspect('equal')
        
        # Dictionary to hold slider references (avoids garbage collection)
        self.sliders = {}
        self.create_sliders()
        self.create_buttons()
        
    def calculate(self):
        """Calculates the x and y coordinates based on the current parameters."""
        p = self.params
        x = (p['A1'] * np.sin(p['f1'] * self.t + p['p1']) * np.exp(-p['d1'] * self.t) +
             p['A2'] * np.sin(p['f2'] * self.t + p['p2']) * np.exp(-p['d2'] * self.t))
        
        y = (p['A3'] * np.sin(p['f3'] * self.t + p['p3']) * np.exp(-p['d3'] * self.t) +
             p['A4'] * np.sin(p['f4'] * self.t + p['p4']) * np.exp(-p['d4'] * self.t))
        return x, y
        
    def create_sliders(self):
        """Creates the 16 sliders dynamically."""
        axcolor = 'darkgray'
        
        # Layout metrics
        left = 0.05
        width = 0.20
        height = 0.015
        spacing = 0.02
        
        # Ranges for each parameter type
        ranges = {
            'A': (0.0, 5.0),
            'f': (0.0, 10.0),
            'p': (0.0, 2 * np.pi),
            'd': (0.0, 0.02)
        }
        
        row = 0
        # Group sliders by pendulums (1, 2, 3, 4)
        for i in range(1, 5):
            for param_type in ['A', 'f', 'p', 'd']:
                key = f"{param_type}{i}"
                
                # Introduce a slight gap between pendulum groups
                group_offset = (i - 1) * 0.02
                bottom = 0.90 - row * spacing - group_offset
                
                ax_slider = plt.axes([left, bottom, width, height], facecolor=axcolor)
                
                slider = Slider(
                    ax=ax_slider,
                    label=key,
                    valmin=ranges[param_type][0],
                    valmax=ranges[param_type][1],
                    valinit=self.params[key],
                    color='cyan'
                )
                slider.label.set_color('white')
                slider.valtext.set_color('white')
                
                slider.on_changed(self.update)
                self.sliders[key] = slider
                row += 1

    def create_buttons(self):
        """Creates action buttons at the bottom."""
        ax_save = plt.axes([0.45, 0.02, 0.12, 0.04])
        self.btn_save = Button(ax_save, 'Save Image', hovercolor='0.9')
        self.btn_save.on_clicked(self.save_image)
        
        ax_reset = plt.axes([0.65, 0.02, 0.12, 0.04])
        self.btn_reset = Button(ax_reset, 'Reset', hovercolor='0.9')
        self.btn_reset.on_clicked(self.reset_params)
        
    def update(self, val):
        """Callback for whenever a slider is moved."""
        for key, slider in self.sliders.items():
            self.params[key] = slider.val
            
        x, y = self.calculate()
        self.line.set_data(x, y)
        
        # Dynamically fit the view to the new data
        self.ax.set_xlim(x.min() - 0.5, x.max() + 0.5)
        self.ax.set_ylim(y.min() - 0.5, y.max() + 0.5)
        self.fig.canvas.draw_idle()
        
    def save_image(self, event):
        """Saves only the harmonograph plot area to a PNG."""
        filename = f"harmonograph_{int(time.time())}.png"
        
        # Extract just the plotting axis extent
        extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        # Add padding
        extent = extent.expanded(1.1, 1.1)
        self.fig.savefig(filename, bbox_inches=extent, facecolor='black', dpi=300)
        print(f"Saved harmonograph artwork to {filename}")
        
    def reset_params(self, event):
        """Resets all sliders back to their initial value."""
        for slider in self.sliders.values():
            slider.reset()
            
    def show(self):
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Interactive Harmonograph Generator")
    
    # Pendulum 1 Configuration
    parser.add_argument('--A1', type=float, default=2.0, help='Amplitude 1')
    parser.add_argument('--f1', type=float, default=3.0, help='Frequency 1')
    parser.add_argument('--p1', type=float, default=np.pi/2, help='Phase 1')
    parser.add_argument('--d1', type=float, default=0.001, help='Damping 1')
    
    # Pendulum 2 Configuration
    parser.add_argument('--A2', type=float, default=2.0, help='Amplitude 2')
    parser.add_argument('--f2', type=float, default=2.0, help='Frequency 2')
    parser.add_argument('--p2', type=float, default=0.0, help='Phase 2')
    parser.add_argument('--d2', type=float, default=0.001, help='Damping 2')
    
    # Pendulum 3 Configuration
    parser.add_argument('--A3', type=float, default=2.0, help='Amplitude 3')
    parser.add_argument('--f3', type=float, default=1.001, help='Frequency 3')
    parser.add_argument('--p3', type=float, default=np.pi/4, help='Phase 3')
    parser.add_argument('--d3', type=float, default=0.001, help='Damping 3')
    
    # Pendulum 4 Configuration
    parser.add_argument('--A4', type=float, default=2.0, help='Amplitude 4')
    parser.add_argument('--f4', type=float, default=2.0, help='Frequency 4')
    parser.add_argument('--p4', type=float, default=np.pi/2, help='Phase 4')
    parser.add_argument('--d4', type=float, default=0.001, help='Damping 4')
    
    args = parser.parse_args()
    
    app = InteractiveHarmonograph(**vars(args))
    app.show()

if __name__ == "__main__":
    main()
