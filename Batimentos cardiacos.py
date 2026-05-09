from matplotlib import pyplot as plt
import numpy as np

batimentos_lista = []
cor = "#00ff0d"
linha = "#cf0000"
plt.ion()

fig, ax = plt.subplots(facecolor= "black")

ax.set_facecolor("black")

for i in range(145):

    batimentos = np.random.normal(75, 5)

    # pico ocasional
    if np.random.rand() < 0.02:
        batimentos += np.random.choice([120, 145])

    batimentos_lista.append(batimentos)

    # limpa gráfico anterior
    ax.clear()

    # linha principal
    ax.plot(batimentos_lista, color= cor, label="Batimentos")

    # linha limite
    ax.axhline(120, color=linha, linestyle="--", label="Limite")


    x_altos = [j for j in range(len(batimentos_lista))
               if batimentos_lista[j] > 120]

    y_altos = [v for v in batimentos_lista
               if v > 120]

    ax.scatter(x_altos, y_altos,
               color="red",
               label="Picos")

    ax.set_title("Simulação | Batimentos Cardíacos" , color= "White")
    ax.set_xlabel("Tempo (s)", color="white")
    ax.set_ylabel("BPM", color="white")
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.legend()
    ax.grid(True)

    plt.pause(0.2)


plt.show()




