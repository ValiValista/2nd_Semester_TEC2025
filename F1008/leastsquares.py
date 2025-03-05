import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([2, 3, 4, 7, 9])
y = np.array([4, 5, 7, 10, 15])

# Cálculo de sumatorias necesarias
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Cálculo de los coeficientes de la recta (mínimos cuadrados)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

# Cálculo de las incertidumbres
y_pred = m * x + b
residuals = y - y_pred
sigma2 = np.sum(residuals**2) / (n - 2)
delta_m = np.sqrt(sigma2 / (sum_x2 - (sum_x**2 / n)))
delta_b = delta_m * np.sqrt(sum_x2 / n)

# Graficar datos y ajuste
plt.scatter(x, y, label="Datos", color="blue")
plt.plot(x, y_pred, label=f"Ajuste: y = {m:.2f}x + {b:.2f}", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Ajuste por mínimos cuadrados")
plt.grid(True)
plt.show()

# Mostrar resultados
m, delta_m, b, delta_b

'''
Resultados:
    Pendiente: m=1.50±0.15
    Intersección con el eje y: b=0.70±0.85
    Ajuste: y = 1.50x + 0.70
'''