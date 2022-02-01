import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
import math
sns.set()

t = np.linspace(0, 60, 1000)

k = 31
m = 60
delta = 0.63


x = [0, 0]
#omega = math.sqrt(k/m)
omega = 2*math.sqrt(k/m)
#omega =  0.5*math.sqrt(k/m)
A = 0.1


def wykres(t, x):
    result = [x[1], (-2 * delta * x[1] - (k / m) * x[0] + A * math.sin(1 * omega*t))]
    return result


solution = solve_ivp(wykres(), [0, 1000], y0=x, t_eval=t)
plt.plot(t, solution.y[0], 'b')
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator z tłumieniem i z wymuszeniem', fontsize=20)
plt.grid(True)
plt.show()
