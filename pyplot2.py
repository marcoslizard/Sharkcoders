from matplotlib import pyplot as plt
import numpy as np

plt.subplot(1,2,1)
plt.plot([1,2,3],[1,4,9])
plt.title("Primeiro Gráfico")

plt.subplot(1,2,2)
plt.plot([1,2,3],[9,4,1])
plt.title("Segundo Gráfico")



plt.tight_layout()
plt.show()