import random
import config
from colonia.probabilidade import calcularProbabilidades

def construirCaminho(matrizDistancia, matrizFeromonio):
    cidadeAtual = config.CIDADE_INICIAL
    visitadas = {cidadeAtual}
    caminho = [cidadeAtual]

    while len(visitadas) < config.CIDADES:
        probabilidades = calcularProbabilidades(
            cidadeAtual, visitadas, matrizDistancia, matrizFeromonio
        )

        if probabilidades is None:
            return None  # caminho impossível

        destino = random.choices(range(config.CIDADES), weights=probabilidades)[0]
        cidadeAtual = destino
        visitadas.add(destino)
        caminho.append(destino)

    # retornar à pizzaria
    if matrizDistancia[cidadeAtual][config.CIDADE_INICIAL] == 0:
        return None  # não consegue voltar

    caminho.append(config.CIDADE_INICIAL)
    return caminho
