from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,16)
y = x**2
green = "#65db84"
plt.subplot(2,1,1)
plt.plot(x,y, color= green ,linestyle='--', marker = "o")
plt.title("Quadrados dos Primeiros 15 Números")
plt.xlabel("Número")
plt.ylabel("Quadrado")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot( x,y, color='blue', marker = "^")
plt.title("Dispersão dos Dados Aleatórios")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.tight_layout()
plt.show()