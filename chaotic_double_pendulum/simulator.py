import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import solve_ivp
import argparse
import time

class ChaoticDoublePendulumSimulator:
    def __init__(self, **kwargs):
        self.params = {
            'L1': kwargs.get('L1', 1.0),
            'L2': kwargs.get('L2', 1.0),
            'm1': kwargs.get('m1', 1.0),
            'm2': kwargs.get('m2', 1.0),
            'g': kwargs.get('g', 9.81),
            'd1': kwargs.get('d1', 0.05),
            'd2': kwargs.get('d2', 0.05),
            'theta0_1': kwargs.get('theta0_1', 3.0),
            'theta0_2': kwargs.get('theta0_2', 3.0),
        }
        
        self.t_span = (0, 30)
        self.t_eval = np.linspace(*self.t_span, 15000)
        
        self.fig, self.ax = plt.subplots(figsize=(10, 8), facecolor='#111111')
        self.fig.canvas.manager.set_window_title('Chaotic Double Pendulum')
        plt.subplots_adjust(left=0.25, bottom=0.35)
        self.ax.set_facecolor('#111111')
        self.ax.axis('off')
        
        self.line, = self.ax.plot([], [], color='#ff0055', linewidth=0.6, alpha=0.8)
        self.ax.set_aspect('equal')
        
        self.sliders = {}
        self.create_sliders()
        self.create_buttons()
        self.update(None)
        
    def odes(self, t, y, p):
        theta1, omega1, theta2, omega2 = y
        
        L1, L2 = p['L1'], p['L2']
        m1, m2 = p['m1'], p['m2']
        g = p['g']
        
        delta = theta1 - theta2
        den1 = L1 * (2*m1 + m2 - m2*np.cos(2*delta))
        den2 = L2 * (2*m1 + m2 - m2*np.cos(2*delta))
        
        domega1 = (-g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - 
                   2*np.sin(delta)*m2*(omega2**2*L2 + omega1**2*L1*np.cos(delta))) / den1 - p['d1'] * omega1
                   
        domega2 = (2*np.sin(delta)*(omega1**2*L1*(m1+m2) + g*(m1+m2)*np.cos(theta1) + 
                   omega2**2*L2*m2*np.cos(delta))) / den2 - p['d2'] * omega2
                   
        return [omega1, domega1, omega2, domega2]
        
    def calculate(self):
        y0 = [self.params['theta0_1'], 0.0, self.params['theta0_2'], 0.0]
        
        sol = solve_ivp(
            fun=lambda t, y: self.odes(t, y, self.params),
            t_span=self.t_span,
            y0=y0,
            t_eval=self.t_eval,
            method='RK45',
            rtol=1e-6,
            atol=1e-8
        )
        
        theta1, theta2 = sol.y[0], sol.y[2]
        L1, L2 = self.params['L1'], self.params['L2']
        
        x1 = L1 * np.sin(theta1)
        y1 = -L1 * np.cos(theta1)
        
        x2 = x1 + L2 * np.sin(theta2)
        y2 = y1 - L2 * np.cos(theta2)
        
        return x2, y2
        
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
        
        add_slider('m2', 'Mass 2', 0.1, 5.0, '#ff0055')
        add_slider('L2', 'Length 2', 0.1, 3.0, '#ff0055')
        add_slider('d1', 'Damping c1', 0.0, 1.0, '#ff0055')
        add_slider('d2', 'Damping c2', 0.0, 1.0, '#ff0055')
        add_slider('theta0_1', 'Init θ1', -np.pi, np.pi, '#ff0055')
        add_slider('theta0_2', 'Init θ2', -np.pi, np.pi, '#ff0055')

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
        filename = f"double_pendulum_{int(time.time())}.png"
        extent = self.ax.get_window_extent().transformed(self.fig.dpi_scale_trans.inverted())
        extent = extent.expanded(1.1, 1.1)
        self.fig.savefig(filename, bbox_inches=extent, facecolor='#111111', dpi=300)
        print(f"Saved chaotic pendulum artwork to {filename}")

    def show(self):
        plt.show()

if __name__ == "__main__":
    app = ChaoticDoublePendulumSimulator()
    app.show()
