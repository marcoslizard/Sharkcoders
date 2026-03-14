from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.uniform(0, 120, 12)
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio" , "Junho",
         "Julho" , "Agosto" , "Setembro" , "Outubro" , "Novembro" , "Dezembro" ]
temperatura = [5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
precipitacao = [120, 90, 70, 60, 50, 30, 20, 25, 40, 80, 100, 130]

fig, ax1 = plt.subplots()

orange_color = "#ff9900"

ax1.bar(meses, numeros, color='skyblue')
ax1.set_xlabel("Meses")
ax1.set_ylabel("Precipitação (mm)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
plt.xticks(rotation=60)

ax2 = ax1.twinx()
ax2.plot(meses, temperatura, color= orange_color, marker='o')
ax2.set_ylabel("Temperatura (ºC)", color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title("Gráfico Termopluviométrico")
plt.tight_layout()
plt.show()