import random
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Função para formatar valores em float com precisão
def floatformat(value, precision=2):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value
    return round(value, precision)

# Função para buscar informações da Mega-Sena
def buscar_informacoes_mega_sena():
    url = 'https://loteriascaixa-api.herokuapp.com/api/megasena/latest'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Rota para retornar resultados anteriores da Mega-Sena
@app.route('/resultados_anteriores')
def resultados_anteriores():
    url = 'https://loteriascaixa-api.herokuapp.com/api/megasena'
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json()
        return jsonify(resultados)
    else:
        return jsonify([])

# Rota principal
@app.route('/')
def home():
    data = buscar_informacoes_mega_sena()
    if data:
        concurso = data['concurso']
        data_sorteio = data['data']
        dezenas_sorteio = data['dezenasOrdemSorteio']
        premiacoes = data['premiacoes']

        # Lógica para gerar combinações aleatórias
        combinacao_aleatoria = [random.randint(1, 60) for _ in range(6)]

        # Lógica para gerar combinações inteligentes (substitua com sua própria lógica)
        combinacao_inteligente = [1, 2, 3, 4, 5, 6]  # Exemplo de combinação inteligente

        return render_template('index.html', concurso=concurso, data_sorteio=data_sorteio, dezenas_sorteio=dezenas_sorteio, premiacoes=premiacoes, combinacao_aleatoria=combinacao_aleatoria, combinacao_inteligente=combinacao_inteligente)
    else:
        return "Não foi possível obter os dados da Mega-Sena no momento."

# Função para buscar resultados da Mega-Sena na API
def buscar_resultados_mega_sena():
    url = 'https://loteriascaixa-api.herokuapp.com/api/megasena'
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json()
        return resultados
    else:
        return None

# Função para identificar os números mais frequentes
def numeros_mais_frequentes(resultados):
    numeros = {}
    for resultado in resultados:
        dezenas = resultado['dezenas']
        for numero in dezenas:
            if numero in numeros:
                numeros[numero] += 1
            else:
                numeros[numero] = 1
    numeros_ordenados = sorted(numeros.items(), key=lambda x: x[1], reverse=True)
    numeros_frequentes = [numero[0] for numero in numeros_ordenados[:6]]
    return numeros_frequentes

# Função para gerar combinações inteligentes
def gerar_combinacoes_inteligentes(resultados, numeros_frequentes, quantidade_combinacoes=5):
    combinacoes = set()  # Usando um conjunto para garantir combinações únicas
    while len(combinacoes) < quantidade_combinacoes:
        combinacao = random.sample(numeros_frequentes, 6)
        combinacao.sort()
        combinacoes.add(tuple(combinacao))  # Usando uma tupla para tornar as combinações imutáveis
    return list(combinacoes)

# Rota para exibir as combinações inteligentes
@app.route('/combinacoes_inteligentes')
def combinacoes_inteligentes():
    resultados = buscar_resultados_mega_sena()
    if resultados:
        numeros_frequentes = numeros_mais_frequentes(resultados)
        combinacoes = gerar_combinacoes_inteligentes(resultados, numeros_frequentes, quantidade_combinacoes=1)
        return jsonify(combinacoes=combinacoes)
    else:
        return "Não foi possível obter os resultados da Mega-Sena na API no momento."
    
if __name__ == '__main__':
    app.run()
