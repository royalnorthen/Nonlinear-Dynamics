import matplotlib.pyplot as plt
import numpy as np

def xdot(r, x):
    return r - x - np.exp(-x) # for reference

def xdot_zeros(x):
    return x + np.exp(-x) # calculated by hand; r as a function of x*

def xdot_derivative(x):
    return (-1) + np.exp(-x) # calculated by hand

x_plot = np.arange(-10, 10, 0.05)
r_unstable_plot = []
r_stable_plot = []
x_unstable_plot = []
x_stable_plot = []
for i in x_plot:
    if xdot_derivative(i) < 0: 
        r_stable_plot.append(xdot_zeros(i))
        x_stable_plot.append(i)
    if xdot_derivative(i) >= 0: 
        r_unstable_plot.append(xdot_zeros(i))
        x_unstable_plot.append(i)

plt.grid()
plt.plot(x_stable_plot, r_stable_plot)
plt.plot(x_unstable_plot, r_unstable_plot, linestyle='dashed')
plt.axis([-10, 10, -10, 10])
plt.xlabel("r")
plt.ylabel("x*")

plt.savefig('HW1_bifurcation_diagram.png', bbox_inches='tight')