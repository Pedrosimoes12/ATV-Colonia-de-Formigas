import config

def evaporarFeromonios(matrizFeromonio):
    n = len(matrizFeromonio)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrizFeromonio[i][j] *= (1 - config.EVAPORACAO) 
                
def depositarFeromonios(matrizFeromonio, caminhosValidos, custosCaminhos):
    qtCidades = len(matrizFeromonio) 
    for i in range(len(caminhosValidos)): 
        caminho = caminhosValidos[i] 
        custoCaminho = custosCaminhos[i] 
        deposito = config.DEPOSITO / custoCaminho 
        for j in range(qtCidades - 1):
            cidadeAtual = caminho[j]
            cidadeProxima = caminho[j + 1]
            matrizFeromonio[cidadeAtual][cidadeProxima] += deposito

# def depositarFeromonios(matrizFeromonio, caminhosValidos, melhorCaminho):
#     qtCidades = len(melhorCaminho[:-1])
    
#     for i in range(qtCidades + 1):
#         if (i+1 < qtCidades):
#             for y in range(len(caminhosValidos)):
#                 for x in range(qtCidades):
#                     if (x+1 < qtCidades):
#                         if (caminhosValidos[y][x] == melhorCaminho[i] and caminhosValidos[y][x + 1] == melhorCaminho[i + 1]):      
#                             matrizFeromonio[caminhosValidos[y][x]][caminhosValidos[y][x + 1]] += config.DEPOSITO