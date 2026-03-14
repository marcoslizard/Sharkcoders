import numpy as np

medicoes_temp  = np.random.normal(22,4,1000)
co2 = np.random.normal(400, 50, 1000)

condicao_critica = (medicoes_temp > 28) & (co2 > 450)

temperaturas_criticas = medicoes_temp[condicao_critica]
co2_criticos = co2[condicao_critica]

quantidade_criticos = len(temperaturas_criticas)
percentagem_criticos = (quantidade_criticos / len(medicoes_temp))

if quantidade_criticos > 0:
    media_temperaturas = np.mean(temperaturas_criticas)
    media_co2 = np.mean(co2_criticos)

print ("a média de temperaturas criticas foi : ", media_temperaturas)
print("a média de co2 foi :", media_co2)
print(" a quantidade de dias criticos foi de :" , quantidade_criticos)




