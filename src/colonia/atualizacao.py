import config

def evaporarFeromonios(matrizFeromonio):
    n = len(matrizFeromonio)
    for i in range(n):
        for j in range(n):
            matrizFeromonio[i][j] *= (1 - config.EVAPORACAO)

def depositarFeromonios(matrizFeromonio, caminhosValidos, matrizDistancia):
    for caminho in caminhosValidos:
        custo = 0
        for a, b in zip(caminho[:-1], caminho[1:]):
            custo += matrizDistancia[a][b]

        for a, b in zip(caminho[:-1], caminho[1:]):
            matrizFeromonio[a][b] += 1 / custo
