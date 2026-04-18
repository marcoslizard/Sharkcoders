from matplotlib import pyplot as plt
import numpy as np

y = list(np.random.normal(0, 1, 100))
x = list(range(100))

plt.ion()
fig, ax = plt.subplots()
linha, = ax.plot(x, y)
ax.set_ylim(-4, 4)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Gráfico sinusoidal")
ax.set_ylabel("y", rotation=0)

while True:
    novo = np.random.normal(0, 1)
    y.append(novo)
    y.pop(0)
    linha.set_ydata(y)
    plt.pause(0.1)