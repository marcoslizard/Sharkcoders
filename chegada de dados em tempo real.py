from matplotlib import pyplot as plt
import numpy as np




dados = []

for _ in range(100):
    if np.random.rand() < 0.05:   # 5% de probabilidade
        # outlier (valor estranho)
        valor = np.random.normal(10, 2)
    else:
        # valor normal
        valor = np.random.normal(0, 1)

    dados.append(valor)

plt.plot(valor)
plt.show()
