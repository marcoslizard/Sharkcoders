from matplotlib import pyplot as plt
import numpy as np

dados = []


outliers_x = []
outliers_y = []

for i in range(100):
    if np.random.rand() < 0.05:
        valor = np.random.normal(10, 2)
        outliers_x.append(i)
        outliers_y.append(valor)
    else:
        valor = np.random.normal(0, 1)

    dados.append(valor)

plt.plot(dados, label="dados")
plt.scatter(outliers_x, outliers_y, color='red', label="outliers")
plt.legend()
plt.show()