import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x
x = np.linspace(0, 5, 100)

# Definir los valores de temperatura
T_values = [50, 25, 20]
colors = ['blue', 'green', 'red']

plt.figure(figsize=(8, 6))

# Calcular y graficar las isotermas
for T, color in zip(T_values, colors):
    y = -(x + np.log(T / 100)) / 2
    plt.plot(x, y, label=f'$T={T}$', color=color)

# Etiquetas y título
plt.xlabel('$x$ (cm)')
plt.ylabel('$y$ (cm)')
plt.title('Isotermas de $T(x,y)$')
plt.legend()
plt.grid()

# Mostrar la gráfica
plt.show()
