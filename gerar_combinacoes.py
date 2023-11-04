import csv
from itertools import combinations
import random

# Leitura do arquivo CSV e análise dos números mais frequentes
resultados = []
with open('resultados_mega_sena.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dezenas = list(map(int, row['dezenas'].split('-')))
        resultados.append(dezenas)

numeros = {}
for resultado in resultados:
    for numero in resultado:
        if numero in numeros:
            numeros[numero] += 1
        else:
            numeros[numero] = 1

# Gerar combinações inteligentes com base nos números mais frequentes
numeros_ordenados = sorted(numeros.items(), key=lambda x: x[1], reverse=True)
numeros_frequentes = [numero[0] for numero in numeros_ordenados[:6]]

# Função para gerar uma única combinação inteligente
def gerar_combinacao_inteligente():
    comb = random.sample(numeros_frequentes, 6)
    comb.sort()
    return comb

# Gere uma combinação inteligente
comb_inteligente = gerar_combinacao_inteligente()
