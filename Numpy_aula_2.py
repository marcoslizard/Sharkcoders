import numpy as np

dados  = np.random.normal(20,5,360)

dias_quentes = dados[dados > 30]
percentagem = (len(dias_quentes) / len(dados)) * 100
print(f"Array Filtrada: \n{dias_quentes}")
print(f"Percentagem de dias muito quentes: \n{percentagem}" )
