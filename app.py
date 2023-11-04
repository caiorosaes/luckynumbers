import requests
from flask import Flask, render_template

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
        import random
        combinacao_aleatoria = [random.randint(1, 60) for _ in range(6)]

        # Lógica para gerar combinações inteligentes (substitua com sua própria lógica)
        combinacao_inteligente = [1, 2, 3, 4, 5, 6]  # Exemplo de combinação inteligente

        return render_template('index.html', concurso=concurso, data_sorteio=data_sorteio, dezenas_sorteio=dezenas_sorteio, premiacoes=premiacoes, combinacao_aleatoria=combinacao_aleatoria, combinacao_inteligente=combinacao_inteligente)
    else:
        return "Não foi possível obter os dados da Mega-Sena no momento."

if __name__ == '__main__':
    app.run()
