import math

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

k = 31
m = 60
t = np.linspace(0, 20, 10000)
x = [6, 0]
delta = 0.63

def wykres(t, x):
    result = (x[1], (-2 * delta * x[1] - (k/m) * x[0]))
    return result

solution = solve_ivp(wykres, [0, 1000], y0=x, t_eval=t)
plt.plot(solution.y[0], solution.y[1], color='r')
plt.title('Ruch układu w przestrzeni fazowej (x,v)', fontsize=20)
plt.grid(True)
plt.show()
