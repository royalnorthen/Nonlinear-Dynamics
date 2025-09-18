import matplotlib.pyplot as plt
import numpy as np

def xnplusone(r, xn):
    return r*xn - xn**3 # for reference

def r_bifurcation(x):
    return 1 + x**2 # calculated by hand; r as a function of x*, excludes trivial solution

def xnplusone_derivative(r, xn):
    return r - 3*xn**2 # calculated by hand

x_plot = np.arange(-10, 10, 0.05)
r_unstable_plot = []
r_stable_plot = []
x_unstable_plot = []
x_stable_plot = []
for i in x_plot:
    if xnplusone_derivative(r_bifurcation(i), i) < 1: 
        r_stable_plot.append(r_bifurcation(i))
        x_stable_plot.append(i)
    if xnplusone_derivative(r_bifurcation(i), i) >= 1: 
        r_unstable_plot.append(r_bifurcation(i))
        x_unstable_plot.append(i)

r_trivial_plot = np.arange(0, 5, 0.01) # x* = 0 trivial solution
r_stable_plot_2 = []
x_stable_plot_2 = [] # it was connecting the plots with a stupid line that was stupid
for i in r_trivial_plot:
    if xnplusone_derivative(i, 0) < 1: 
        r_stable_plot_2.append(i)
        x_stable_plot_2.append(0)
    if xnplusone_derivative(i, 0) >= 1: 
        r_unstable_plot.append(i)
        x_unstable_plot.append(0)



plt.grid()
plt.plot(r_stable_plot, x_stable_plot, c='k')
plt.plot(r_stable_plot_2, x_stable_plot_2, c='k')
plt.plot(r_unstable_plot, x_unstable_plot, linestyle='dashed', c='r')
plt.axis([0, 5, -5, 5])
plt.xlabel("r")
plt.ylabel("x*")

plt.savefig('HW2_bifurcation_diagram.png', bbox_inches='tight')