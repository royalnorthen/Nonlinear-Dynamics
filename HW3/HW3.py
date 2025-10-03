import matplotlib.pyplot as plt
import numpy as np

def xdot(a, x, y):
    return a - x - (4*x*y)/(1 + x**2)

def ydot(b, x, y):
    return b*x*(1 - y/(1 + x**2))

def b_critical(a):
    return 3*a/5 - 25/a

def RungeKutta4_DE(func, x0, t0, t_final, steps=1000): # this is borrowed from one of my computational physics assignments, but I was the one who wrote it
    t_plot = np.linspace(t0, t_final, steps)
    t_step = (t_final - t0) / steps
    x_plot = np.zeros([steps, len(x0)])
    for i in range(steps):
        k1 = func(x0, t0) * t_step
        k2 = func(x0 + k1/2, t0 + t_step/2) * t_step
        k3 = func(x0 + k2/2, t0 + t_step/2) * t_step
        k4 = func(x0 + k3, t0 + t_step) * t_step
        x0 = x0 + (k1 + k2*2 + k3*2 + k4)/6
        x_plot[i] = x0
        t0 += t_step
    return x_plot, t_plot

def input_func(r, t):
    dxdt = xdot(universal_a, r[0], r[1])
    dydt = ydot(universal_b, r[0], r[1])
    return np.array([dxdt, dydt])

start_pos = np.array([1, 1])
universal_a = 9 # varying this parameter is very interesting-- it seems to change the size of the loops
t_f = 20

universal_b = b_critical(universal_a) / 2
r_points_b_half, t_points_b_half = RungeKutta4_DE(input_func, start_pos, 0, t_f)
r_points_b_half_inside, t_points_b_half_inside = RungeKutta4_DE(input_func, np.array([1.5, 4.5]), 0, t_f)

universal_b = b_critical(universal_a) * 2
r_points_b_double, t_points_b_double = RungeKutta4_DE(input_func, start_pos, 0, t_f)

universal_b = b_critical(universal_a) / 4
r_points_b_quarter, t_points_b_quarter = RungeKutta4_DE(input_func, start_pos, 0, t_f) 

plt.plot(r_points_b_quarter[:,0], r_points_b_quarter[:,1], c='r', label="$\mathregular{\dfrac{b_c}{4}}$")
plt.plot(r_points_b_half[:,0], r_points_b_half[:,1], c='orange', label="$\mathregular{\dfrac{b_c}{2}}$")
plt.plot(r_points_b_half_inside[:,0], r_points_b_half_inside[:,1], c='g', label="$\mathregular{\dfrac{b_c}{2}}$ inside")
plt.plot(r_points_b_double[:,0], r_points_b_double[:,1], c='b', label="$\mathregular{2b_c}$")
plt.legend()
plt.title("Phase Plot of Spirals")
plt.xlabel("x")
plt.ylabel("y")

plt.savefig('HW3_phase_plot.png', bbox_inches='tight')