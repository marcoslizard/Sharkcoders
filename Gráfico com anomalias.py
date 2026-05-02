from matplotlib import pyplot as plt
import numpy as np

plt.ion()

valores = []
indice = []

for i in range(100):
    valor = np.random.normal(0,1)

    if np.random.rand()< 0.05:
        valor += np.random.choice([-10,10])

    valores.append(valor)
    indice.append(i)

    media = np.mean(valores)
    desvio = np.std(valores)

    limites = (media - 3 * desvio, media + 3 * desvio)

    plt.clf()
    plt.title("Detectar Anomalias")
    plt.xlabel("Tempo")
    plt.ylabel("Valores")

    valores_array = np.array(valores)
    outliers = (valores_array < limites[0]) | (valores_array > limites[1])

    plt.plot(indice,valores, color='blue', label='Normal')
    plt.scatter(np.array(indice)[outliers],
                valores_array[outliers],
                color='red', label = 'Anomalias')
    plt.legend()
    plt.pause(0.02)

plt.ioff()
plt.show()

