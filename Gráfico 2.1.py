from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.normal(0, 1, 1000)

plt.figure()
plt.subplot(2,1,1)
plt.hist(numeros, bins= 30, color='skyblue' , edgecolor= 'black')
plt.title("Histograma - Distribuição Normal")

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

x = np.random.uniform(0, 1, 100)
y = np.random.uniform(0, 1, 100)

plt.figure()
plt.subplot(2,1,1)
plt.scatter(x , y , color = "red")
plt.title("Scatter Plot Aleatório")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.show()