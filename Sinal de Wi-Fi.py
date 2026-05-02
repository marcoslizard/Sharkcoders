import numpy as np
import matplotlib.pyplot as plt

tempos = []
intensidades = []

t = 0

plt.ion()
fig, ax = plt.subplots()

while True:
    intensidade = np.random.normal(loc=-50, scale=5)

    tempos.append(t)
    intensidades.append(intensidade)

    if len(tempos) > 120:
        tempos = tempos[-120:]
        intensidades = intensidades[-120:]

    ax.clear()

    ax.plot(tempos, intensidades, label="Sinal (dBm)")

    fracos_x = [tempos[i] for i in range(len(intensidades)) if intensidades[i] < -70]
    fracos_y = [v for v in intensidades if v < -70]

    ax.scatter(fracos_x, fracos_y, color="red", label="Sinal fraco (< -70 dBm)")

    ax.axhline(y=-70, color="orange", linestyle="--", label="Limite -70 dBm")

    ax.set_title("Simulação de Intensidade de Sinal WiFi")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Intensidade (dBm)")
    ax.grid(True)
    ax.legend()

    plt.pause(0.5)
#plt.axhline(-8
    t += 0.5