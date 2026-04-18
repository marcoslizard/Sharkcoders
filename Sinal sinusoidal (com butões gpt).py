import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# dados iniciais
x = np.arange(100)
y = np.random.normal(0, 1, 100)

fig, ax = plt.subplots()
linha, = ax.plot(x, y)

ax.set_ylim(-4, 4)

# função que atualiza os dados
def atualizar(event):
    novo_y = np.random.normal(0, 1, 100)
    linha.set_ydata(novo_y)
    fig.canvas.draw()

# botão
ax_botao = plt.axes([0.8, 0.01, 0.1, 0.05])
botao = Button(ax_botao, 'Mudar')

botao.on_clicked(atualizar)

plt.show()