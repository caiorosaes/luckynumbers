# LuckyNumbers - Geração de Combinações da Mega-Sena

Este é um projeto de aplicativo web para gerar combinações de números da Mega-Sena de forma aleatória ou inteligente com base em análises de resultados passados.

## Funcionalidades

- Mostra os resultados mais recentes da Mega-Sena.
- Permite a geração de combinações de números da Mega-Sena de duas maneiras: aleatória e inteligente (com base na análise de resultados passados).
- Exibe as combinações geradas na interface do usuário.

## Pré-requisitos

- Python 3.x instalado
- Pacotes Python listados no arquivo `requirements.txt`

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/luckynumbers.git
   cd luckynumbers
   ```

2. Opcional: Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o aplicativo Flask:
   ```bash
   flask run
   ```

2. Abra seu navegador e acesse `http://localhost:5000` para usar o aplicativo.

## Estrutura de Arquivos

- `app.py`: Arquivo principal do aplicativo Flask.
- `templates/index.html`: Modelo HTML para a interface do usuário.
- `static/style.css`: Arquivo CSS para estilizar a página.
- `data/mega_sena_results.csv`: Arquivo CSV com resultados passados da Mega-Sena.

## Personalização

Você pode personalizar este projeto adicionando recursos adicionais, melhorando o layout, ou estendendo a funcionalidade de acordo com suas necessidades específicas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para criar pull requests, relatar problemas ou sugerir melhorias.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
