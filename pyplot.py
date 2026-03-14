from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5,]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.plot(x, y, color='red', linestyle='--', marker= "o", label='Série 1')
plt.legend()


plt.title("Exemplo de Gráfico de Linhas")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()