import config
import random

def calcularProbabilidades(cidadeAtual, visitadas, matrizDistancia, matrizFeromonio):
    probabilidades = []
    soma = 0

    for destino in range(len(matrizFeromonio)):
        if destino in visitadas or destino == cidadeAtual:
            probabilidades.append(0)
            continue

        distancia = matrizDistancia[cidadeAtual][destino]

        if distancia == 0:  # sem ligação
            probabilidades.append(0)
            continue

        print('CidadeAtual =>', cidadeAtual)
        print('destino =>', destino)
        print('len(matrizDistancia) =>', len(matrizDistancia))
        #print('matrizFeromonio =>', matrizFeromonio)

        fer = matrizFeromonio[cidadeAtual][destino] ** config.ALFA
        vis = (1 / distancia) ** config.BETA
        
        valor = fer * vis
        probabilidades.append(valor)
        soma += valor

    if soma == 0:  
        return None  # formiga fica presa (sem caminhos possíveis)

    return [p / soma for p in probabilidades]
