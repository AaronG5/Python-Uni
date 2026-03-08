# Pirmoji namų darbų užduotis

import numpy as np 
import sympy as sp
from matplotlib import pyplot as plt

# 1.
def task_1():
   return np.linspace(-1.3, 2.5, 64)

# 2.
def task_2():
   arr = np.array([1, 2, 3, 4])
   N = 3
   return np.tile(arr, N)

# 3.
def task_3():
   arr = np.array([3, 4])
   N = 4
   return np.repeat(arr, N)

# 4.
def task_4():
   arr = np.zeros((10, 10), dtype=int)
   return np.pad(arr, 1, constant_values=1)

# 5. 
def task_5():
   y, x = np.indices((8, 8), dtype=int)
   return (x + y) & 1

# 6.
def task_6():
   n = 8
   i, j = np.indices((n, n), dtype=int)
   return i+j

# 7. 
def task_7():
   arr = np.random.rand(5, 5)
   return arr[arr[:, 1].argsort()]

# 8. 
def task_8():
   arr = np.random.randint(0, 3, (3, 3))
   try:
      res = np.linalg.eig(arr)
   except Exception:
      return None

   return res

# 9. 
def task_9():
   func = np.poly1d([0.5, 5, 4])
   deriv_1 = np.polyder(func, 1)
   deriv_2 = np.polyder(deriv_1, 1)

   return (deriv_1, deriv_2)

# 10.
def task_10():
   x = sp.symbols('x')
   f = sp.exp(-x)
   integral_indef = sp.integrate(f, x)
   integral_def = sp.integrate(f, (x, 0, 1))

   return (integral_indef, integral_def)

# 11. 
def task_11():
   theta = np.linspace(0, 2*np.pi, 1000)
   a = 1
   r = 2 * a * (1 - np.cos(theta))

   plt.polar(theta, r)
   plt.title("task_11")
   plt.show()

# 12. 
def task_12():
   V = 5.4
   D = 1.2
   return np.random.normal(V, D, 1000)

tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10, task_11, task_12]

for i, task in enumerate(tasks):
   print(f"{i+1}.\n{task()}\n")