import config
from colonia.inicializacao import carregarDados
from colonia.construtor import construirCaminho
from colonia.atualizacao import evaporarFeromonios, depositarFeromonios

def executarACO():
    matrizDistancia, matrizFeromonio = carregarDados()

    melhorCaminho = None
    melhorCusto = float("inf")
    historicoMelhores = []

    for iteracao in range(config.ITERACOES):
        caminhos = []

        for _ in range(config.FORMIGAS):
            caminho = construirCaminho(matrizDistancia, matrizFeromonio)
            if caminho is not None:
                caminhos.append(caminho)

        if not caminhos:
            print(f"Iteração {iteracao}: Nenhuma formiga conseguiu caminho válido.")
            continue

        # escolher melhor da iteração
        for caminho in caminhos:
            custo = sum(matrizDistancia[a][b] for a, b in zip(caminho[:-1], caminho[1:]))
            if custo < melhorCusto:
                melhorCusto = custo
                melhorCaminho = caminho

        historicoMelhores.append(melhorCusto)

        evaporarFeromonios(matrizFeromonio)
        depositarFeromonios(matrizFeromonio, caminhos, matrizDistancia)

        print(f"Iteração {iteracao}: Melhor custo atual = {melhorCusto:.2f}")

    return melhorCaminho, melhorCusto, historicoMelhores
