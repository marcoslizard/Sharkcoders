import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


COR_FUNDO_APP = "#0f172a"
COR_FUNDO_PAINEL = "#1e293b"
COR_TITULOS = "#94a3b8"
COR_TEXTO_PADRAO = "#f8fafc"
COR_DESTAQUE_AZUL = "#38bdf8"
COR_VERDE = "#22c55e"
COR_VERMELHO = "#ef4444"


#COR_TESTE = "#FEED5A"

class Empresa:
    def __init__(self, nome, preco_inicial, volatilidade):
        self.nome = nome
        self.preco = preco_inicial
        self.volatilidade = volatilidade
        self.historico = []

    def atualizar_preco(self):
        variacao = np.random.normal(0, self.volatilidade)
        self.preco += variacao
        if self.preco < 1:
            self.preco = 1
        self.historico.append(self.preco)

empresas = [
    Empresa("Tesla", 700, 8),
    Empresa("BMW", 95, 3),
    Empresa("Ford", 12, 4),
    Empresa("Microsoft", 400, 2),
    Empresa("Google", 150, 3),
    Empresa("Amazon", 180, 5),
    Empresa("Nvidia", 900, 9),
    Empresa("Visa", 250, 2),
    Empresa("Shell", 65, 3),
    Empresa("Galp", 14, 3)
]

dinheiro = 10000
acoes = {empresa.nome: 0 for empresa in empresas}

root = tk.Tk()
root.title("Simulador de Bolsa")
root.configure(bg=COR_FUNDO_APP)

frame = tk.Frame(root, bg=COR_FUNDO_APP)
frame.pack(fill="x", padx=15, pady=10)

control_moldura = tk.Frame(frame, bg=COR_FUNDO_APP)
control_moldura.grid(row=0, column=0, sticky="nw")

empresa_selecionada = tk.StringVar()
combo = ttk.Combobox(control_moldura, textvariable=empresa_selecionada, state="readonly", font=("Arial", 11))
combo['values'] = [e.nome for e in empresas]
combo.current(0)
combo.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

btn_comprar = tk.Button(control_moldura, text="Comprar", command=lambda: negociar(1), bg=COR_VERDE, fg="white", font=("Arial", 11, "bold"), width=10)
btn_comprar.grid(row=1, column=0, padx=5, pady=5)

btn_vender = tk.Button(control_moldura, text="Vender", command=lambda: negociar(-1), bg=COR_VERMELHO, fg="white", font=("Arial", 11, "bold"), width=10)
btn_vender.grid(row=1, column=1, padx=5, pady=5)

frame.grid_columnconfigure(1, weight=1)

dados_frame = tk.Frame(frame, bg=COR_FUNDO_PAINEL, bd=2, relief="groove", padx=15, pady=10)
dados_frame.grid(row=0, column=2, sticky="ne")

tk.Label(dados_frame, text="DINHEIRO", fg=COR_TITULOS, bg=COR_FUNDO_PAINEL, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, sticky="w")
tk.Label(dados_frame, text="AÇÕES RETIDAS", fg=COR_TITULOS, bg=COR_FUNDO_PAINEL, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, sticky="w")
tk.Label(dados_frame, text="LUCRO / PREJUÍZO", fg=COR_TITULOS, bg=COR_FUNDO_PAINEL, font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10, sticky="w")

lbl_dinheiro = tk.Label(dados_frame, text="", fg=COR_TEXTO_PADRAO, bg=COR_FUNDO_PAINEL, font=("Arial", 16, "bold"))
lbl_dinheiro.grid(row=1, column=0, padx=10, pady=(2, 0), sticky="w")

lbl_acoes = tk.Label(dados_frame, text="", fg=COR_DESTAQUE_AZUL, bg=COR_FUNDO_PAINEL, font=("Arial", 16, "bold"))
lbl_acoes.grid(row=1, column=1, padx=10, pady=(2, 0), sticky="w")

lbl_lucro = tk.Label(dados_frame, text="", fg=COR_VERDE, bg=COR_FUNDO_PAINEL, font=("Arial", 16, "bold"))
lbl_lucro.grid(row=1, column=2, padx=10, pady=(2, 0), sticky="w")

def negociar(direcao):
    global dinheiro
    nome = empresa_selecionada.get()
    empresa = next(e for e in empresas if e.nome == nome)

    if direcao == 1 and dinheiro >= empresa.preco:
        dinheiro -= empresa.preco
        acoes[nome] += 1
    elif direcao == -1 and acoes[nome] > 0:
        dinheiro += empresa.preco
        acoes[nome] -= 1

fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

def update(frame_anim):
    global dinheiro

    ax.clear()

    for empresa in empresas:
        empresa.atualizar_preco()

    nome = empresa_selecionada.get()
    empresa = next(e for e in empresas if e.nome == nome)
    precos = empresa.historico

    ax.set_facecolor(COR_FUNDO_APP)
    fig.patch.set_facecolor(COR_FUNDO_APP)

    for i in range(1, len(precos)):
        cor = COR_VERDE if precos[i] >= precos[i - 1] else COR_VERMELHO
        ax.plot([i - 1, i], [precos[i - 1], precos[i]], color=cor, linewidth=2)

    ax.grid(color=COR_FUNDO_PAINEL, linestyle="--", linewidth=0.5)
    ax.tick_params(colors=COR_TEXTO_PADRAO)
    for spine in ax.spines.values():
        spine.set_color(COR_TEXTO_PADRAO)

    ax.set_title(f"Gráfico em Tempo Real: {nome}", color=COR_TEXTO_PADRAO, fontsize=12, fontweight="bold")
    ax.set_xlabel("Tempo", color=COR_TEXTO_PADRAO)
    ax.set_ylabel("Preço (€)", color=COR_TEXTO_PADRAO)

    valor_acoes = sum(e.preco * acoes[e.nome] for e in empresas)
    total = dinheiro + valor_acoes
    lucro = total - 10000

    lbl_dinheiro.config(text=f"{dinheiro:,.2f}€".replace(",", " "))
    lbl_acoes.config(text=f"{acoes[nome]} un.")

    if lucro >= 0:
        lbl_lucro.config(text=f"+{lucro:,.2f}€".replace(",", " "), fg=COR_VERDE)
    else:
        lbl_lucro.config(text=f"{lucro:,.2f}€".replace(",", " "), fg=COR_VERMELHO)

    canvas.draw()

ani = FuncAnimation(fig, update, interval=500, cache_frame_data=False)

root.mainloop()