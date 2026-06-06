import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation

# =========================
# FIGURA E GRÁFICO
# =========================

fig, ax = plt.subplots()

tempo = [0]
preco = [100]

linha, = ax.plot(tempo, preco, color="blue")

ax.set_title("📈 Simulador de Bolsa de Valores")
ax.set_xlabel("Tempo")
ax.set_ylabel("Preço (€)")

# =========================
# ESTADO DO SISTEMA
# =========================

saldo = 1000
acoes = 0
t = 0

# =========================
# TEXTO FORA DO GRÁFICO (UI LIMPA)
# =========================

texto_ui = fig.text(
    0.02, 0.95,
    "",
    fontsize=12
)

# =========================
# ATUALIZAR UI
# =========================

def atualizar_ui():
    lucro = saldo + acoes * preco[-1] - 1000

    texto_ui.set_text(
        f"💰 Saldo: {saldo:.2f}€   "
        f"📦 Ações: {acoes}   "
        f"📊 Lucro: {lucro:.2f}€"
    )

# =========================
# MERCADO (MOVIMENTO RÁPIDO)
# =========================

def update(frame):
    global t

    t += 1
    tempo.append(t)

    # movimento base (rápido tipo bolsa real)
    variacao = np.random.normal(0, 2)

    novo_preco = preco[-1] + variacao

    # =========================
    # ANOMALIAS ALEATÓRIAS
    # =========================

    evento = np.random.random()

    # boom (5% chance)
    if evento < 0.05:
        novo_preco *= np.random.uniform(1.05, 1.25)

    # crash (5% chance)
    elif evento > 0.95:
        novo_preco *= np.random.uniform(0.75, 0.9)

    novo_preco = max(1, novo_preco)

    preco.append(novo_preco)

    linha.set_xdata(tempo)
    linha.set_ydata(preco)

    ax.relim()
    ax.autoscale_view()

    atualizar_ui()

# =========================
# COMPRAR / VENDER
# =========================

def comprar(event):
    global saldo, acoes

    if saldo >= preco[-1]:
        saldo -= preco[-1]
        acoes += 1

    atualizar_ui()

def vender(event):
    global saldo, acoes

    if acoes > 0:
        saldo += preco[-1]
        acoes -= 1

    atualizar_ui()

# =========================
# BOTÕES (FORA DO GRÁFICO)
# =========================

ax_buy = plt.axes([0.75, 0.02, 0.1, 0.05])
ax_sell = plt.axes([0.86, 0.02, 0.1, 0.05])

btn_buy = Button(ax_buy, "COMPRAR")
btn_sell = Button(ax_sell, "VENDER")

btn_buy.on_clicked(comprar)
btn_sell.on_clicked(vender)

# =========================
# ANIMAÇÃO (GRÁFICO RÁPIDO)
# =========================

ani = FuncAnimation(fig, update, interval=300)

plt.show()