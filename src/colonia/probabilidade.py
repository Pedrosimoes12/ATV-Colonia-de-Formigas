import config

def calcularProbabilidades(cidadeAtual, visitadas, matrizDistancia, matrizFeromonio, graus):
    destinos_possiveis = []
    probabilidades = []
    soma = 0

    for destino in range(len(matrizFeromonio)):
        if destino in visitadas or destino == cidadeAtual:
            continue

        distancia = matrizDistancia[cidadeAtual][destino]

        if distancia == 0:  # sem ligação
            continue

        # print('CidadeAtual =>', cidadeAtual)
        # print('destino =>', destino)
        # print('len(matrizDistancia) =>', len(matrizDistancia))
        # print('matrizFeromonio =>', matrizFeromonio)
        
        grau_destino = graus[destino]
        grau = ((1/grau_destino) ** config.GRAU) 
        fer = matrizFeromonio[cidadeAtual][destino] ** config.FEROMONIO
        vis = (1 / distancia) ** config.CUSTO
        valor = fer * vis * grau
        
        destinos_possiveis.append(destino)
        probabilidades.append(valor)
        soma += valor

    
    if soma == 0:  
        # print(">>> ERRO: Nenhum destino possível saindo de", cidadeAtual)
        # print("Visitadas:", visitadas)
        # print("Sobrou para visitar:", set(range(len(matrizDistancia))) - visitadas)
        return None, None  # formiga fica presa (sem caminhos possíveis)

    return destinos_possiveis, [p / soma for p in probabilidades]
