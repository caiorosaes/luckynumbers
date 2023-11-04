document.addEventListener("DOMContentLoaded", function () {
    const randomButton = document.getElementById('random-button');
    const intelligentButton = document.getElementById('intelligent-button');
    const combinationsList = document.getElementById('combinations-list');

    randomButton.addEventListener('click', function () {
        const randomCombination = generateRandomCombination();
        displayCombination(randomCombination);
    });

    intelligentButton.addEventListener('click', function () {
        // Limpar a lista atual
        combinationsList.innerHTML = '';

        // Requisitar os resultados anteriores da API da Mega-Sena
        fetch('/resultados_anteriores')
            .then(response => response.json())
            .then(data => {
                // Analisar os números mais frequentes nos resultados
                const frequentNumbers = analyzeFrequentNumbers(data.resultados);

                // Gerar múltiplas combinações inteligentes
                const numberOfCombinations = 5; // Defina o número de combinações desejadas
                for (let i = 0; i < numberOfCombinations; i++) {
                    const intelligentCombination = generateIntelligentCombination(frequentNumbers);
                    displayCombination(intelligentCombination);
                }
            })
            .catch(error => console.error(error));
    });

    // Função para gerar números aleatórios
    function generateRandomCombination() {
        const numbers = [];
        while (numbers.length < 6) {
            const randomNumber = Math.floor(Math.random() * 60) + 1;
            if (!numbers.includes(randomNumber)) {
                numbers.push(randomNumber);
            }
        }
        return numbers;
    }

    // Função para exibir a combinação gerada no navegador
    function displayCombination(combination) {
        const listItem = document.createElement('li');
        listItem.textContent = 'Combinação: ' + combination.join(' - ');
        combinationsList.appendChild(listItem);
    }

    // Função para analisar os números mais frequentes nos resultados anteriores
    function analyzeFrequentNumbers(resultados) {
        const numbers = {};
        resultados.forEach(resultado => {
            resultado.dezenas.forEach(numero => {
                if (numbers[numero]) {
                    numbers[numero]++;
                } else {
                    numbers[numero] = 1;
                }
            });
        });

        // Ordenar os números com base na frequência (mais frequentes primeiro)
        const frequentNumbers = Object.keys(numbers).sort((a, b) => numbers[b] - numbers[a]);

        return frequentNumbers;
    }

    // Função para gerar combinação inteligente com base nos números mais frequentes
    function generateIntelligentCombination(frequentNumbers) {
        const intelligentCombination = [];
        for (let i = 0; i < 6; i++) {
            intelligentCombination.push(parseInt(frequentNumbers[i]));
        }
        return intelligentCombination;
    }
});
