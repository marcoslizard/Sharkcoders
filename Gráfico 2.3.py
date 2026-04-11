from matplotlib import pyplot as plt
import numpy as np

# 1º gráfico
numeros = np.random.normal(2, 1, 600)

plt.subplot(1,3,1)
plt.hist(numeros, bins=25, color="coral", edgecolor='black')
plt.title("Histograma Normal")

# 2º gráfico
x = np.arange(10)
y = 2 ** x

plt.subplot(1,3,2)
plt.bar(x, y, color="skyblue", edgecolor="black")
plt.title("Potências de 2")

# 3º gráfico
pontos_x = np.random.rand(150)
pontos_y = np.random.rand(150)

plt.subplot(1,3,3)
plt.scatter(pontos_x, pontos_y, color="lime")
plt.title("Scatter Aleatório")

plt.tight_layout()
plt.show()

