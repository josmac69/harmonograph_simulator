import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import solve_ivp
import argparse
import time

class CoupledPendulumSimulator:
    def __init__(self, **kwargs):
        self.params = {
            'w1_sq': kwargs.get('w1_sq', 4.0),
            'w2_sq': kwargs.get('w2_sq', 4.1),
            'k': kwargs.get('k', 0.5), # spring coupling term
            'c1': kwargs.get('c1', 0.05),
            'c2': kwargs.get('c2', 0.05),
            'theta0_1': kwargs.get('theta0_1', 1.0),
            'theta0_2': kwargs.get('theta0_2', 0.0),
        }
        
        self.t_span = (0, 100)
        self.t_eval = np.linspace(*self.t_span, 10000)
        
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#111111')
        self.fig.canvas.manager.set_window_title('Coupled Pendulum Simulator')
        plt.subplots_adjust(left=0.25, bottom=0.35)
        self.ax.set_facecolor('#111111')
        self.ax.axis('off')
        
        self.line, = self.ax.plot([], [], color='#ffcc00', linewidth=0.8, alpha=0.9)
        self.ax.set_aspect('equal')
        
        self.sliders = {}
        self.create_sliders()
        self.create_buttons()
        self.update(None)
        
    def odes(self, t, y, p):
        theta1, omega1, theta2, omega2 = y
        dtheta1_dt = omega1
        domega1_dt = -p['w1_sq'] * theta1 - p['k'] * (theta1 - theta2) - p['c1'] * omega1
        dtheta2_dt = omega2
        domega2_dt = -p['w2_sq'] * theta2 + p['k'] * (theta1 - theta2) - p['c2'] * omega2
        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]
        
    def calculate(self):
        y0 = [self.params['theta0_1'], 0.0, self.params['theta0_2'], 0.0]
        
        # solve ODE
        sol = solve_ivp(
            fun=lambda t, y: self.odes(t, y, self.params),
            t_span=self.t_span,
            y0=y0,
            t_eval=self.t_eval,
            method='RK45',
            rtol=1e-6,
            atol=1e-8
        )
        
        # map angles to X and Y directly (simplest mapping for harmonograph visuals)
        return sol.y[0] * 5.0, sol.y[2] * 5.0
        
    def create_sliders(self):
        axcolor = 'darkgray'
        left = 0.2
        width = 0.6
        h = 0.02
        ypos = 0.25
        
        def add_slider(name, label, vmin, vmax, color):
            nonlocal ypos
            ax = plt.axes([left, ypos, width, h], facecolor=axcolor)
            self.sliders[name] = Slider(ax, label, vmin, vmax, valinit=self.params[name], color=color)
            self.sliders[name].label.set_color('white')
            self.sliders[name].valtext.set_color('white')
            self.sliders[name].on_changed(self.update)
            ypos -= 0.04
        
        add_slider('k', 'Coupling (k)', 0.0, 5.0, '#ffcc00')
        add_slider('w1_sq', 'w1²', 1.0, 10.0, '#ffcc00')
        add_slider('w2_sq', 'w2²', 1.0, 10.0, '#ffcc00')
        add_slider('c1', 'Damping c1', 0.0, 1.0, '#ffcc00')
        add_slider('theta0_1', 'Init θ1', -2.0, 2.0, '#ffcc00')
        add_slider('theta0_2', 'Init θ2', -2.0, 2.0, '#ffcc00')

    def create_buttons(self):
        ax_save = plt.axes([0.45, 0.02, 0.15, 0.05])
        self.btn_save = Button(ax_save, 'Save Image', hovercolor='0.9')
        self.btn_save.on_clicked(self.save_image)
        
    def update(self, val):
        for name, slider in self.sliders.items():
            self.params[name] = slider.val
            
        x, y = self.calculate()
        self.line.set_data(x, y)
        
        limit = max(np.max(np.abs(x)), np.max(np.abs(y))) + 0.5
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.fig.canvas.draw_idle()
        
    def save_image(self, event):
        filename = f"coupled_{int(time.time())}.png"
        extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        extent = extent.expanded(1.1, 1.1)
        self.fig.savefig(filename, bbox_inches=extent, facecolor='#111111', dpi=300)
        print(f"Saved coupled pendulum artwork to {filename}")

    def show(self):
        plt.show()

if __name__ == "__main__":
    app = CoupledPendulumSimulator()
    app.show()
