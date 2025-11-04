import config
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tools.leitorDeArquivos import lerMatrizTxt

# ==========================
# INICIALIZAÇÃO
# ==========================
config.cidades = lerMatrizTxt("src/dados.txt")
config.feromonios = lerMatrizTxt("src/feromonios.txt")

# ==========================
# DAQUI PRA FRENTE SÓ PRA TRÁS
# ==========================

# heurística do problema: distâncias
# mapa visual
mapa_cidades = np.array([
                         [2, 2], # 1
                         [2, 3], # 2
                         [3, 4], # 3
                         [4, 4], # 4
                         [5, 3], # 5
                         [5, 2], # 6
                         [5, 5], # 7
                         [5, 4], # 8
                         [4, 2], # 9
                         [2, 4], # 10                        
                         [2, 2] # volta config.inicio
                        ]) 

# retorna cidade nova
def prox_cidade(_atual, _tour):
    prob = 0
    ind = _atual

    soma = 0
    for c in range(config.CIDADES):
        w = np.where(_tour == c)
        if(len(w[0]) == 0):
            soma = soma + ((1 / config.distancia_cidades[_atual][c]) * feromonios[_atual][c])

    for c in range(config.CIDADES):
        w = np.where(_tour == c)
        if(len(w[0]) == 0):
            if(prob == 0): 
                prob = (((1 / config.distancia_cidades[_atual][c]) * feromonios[_atual][c]) / soma)
                ind = c
            else:
                aux = (((1 / config.distancia_cidades[_atual][c]) * feromonios[_atual][c]) / soma)
                if(aux > prob):
                    prob = aux
                    ind = c
    return ind


# apura custos dos config.tours
def custos_tours():
    global custos
    global melhor_agente

    custos.fill(0)
    for f in range(config.CIDADES):
        for a in range(config.CIDADES):
            if((a+1) <= config.CIDADES):
                custos[f] = custos[f] + config.distancia_cidades[config.tours[f][a].astype(int)][config.tours[f][a+1].astype(int)]

    print(custos)

    melhor_agente = -1
    aux = 0
    for a in range(config.CIDADES):
        config.qtde_feromonio[a] = Q / custos[a]

        if(aux == 0):
            aux = custos[a] 
            melhor_agente = a
        else: 
            if(custos[a] < aux): 
                aux = custos[a]
                melhor_agente = a

    print(melhor_agente, config.tours[melhor_agente])


# depositar/evaporar feromonio
def atualiza_feromonio():
    global feromonios

    print(feromonios)

    # evaporar feromônios de todas as arestas
    for c1 in range(config.CIDADES):
        for c2 in range(config.CIDADES):
            if(c1 != c2): 
                feromonios[c1][c2] = (1 - R) * feromonios[c1][c2]

    print(feromonios)

    # checar quem tem as cidades (arestas) do tour do melhor agente e depositor feromonio
    for m in range(config.CIDADES+1): # cidades do melhor agente
        if(m+1 < config.CIDADES):
            for a in range(config.CIDADES): #todos os agentes
                for c in range(config.CIDADES): #cidades dos agentes
                    if(c+1 < config.CIDADES):
                        if((config.tours[melhor_agente][m+0].astype(int) == config.tours[a][c+0].astype(int) and config.tours[melhor_agente][m+1].astype(int) == config.tours[a][c+1].astype(int)) or \
                           (config.tours[melhor_agente][m+0].astype(int) == config.tours[a][c+1].astype(int) and config.tours[melhor_agente][m+1].astype(int) == config.tours[a][c+0].astype(int))):
                            feromonios[m+0][m+1] = feromonios[m+0][m+1] + config.qtde_feromonio[a]
                            feromonios[m+1][m+0] = feromonios[m+1][m+0] + config.qtde_feromonio[a]
            
    print(feromonios)



# iteracoes (epocas)
for i in range(3):
    config.tours.fill(-1)

    # cidade inicial para cada formiga
    np.random.shuffle(config.inicio)

    for f in range(config.CIDADES):        
        print("Formiga", f, "iniciando tour na cidade", config.inicio[f])

        # fazendo o tour
        t = 0
        config.tours[f][t] = config.inicio[f]
        while(True):
            t = t+1
            if(t < config.CIDADES):
                config.tours[f][t] = prox_cidade(config.tours[f][t-1].astype(int), config.tours[f])
            else:
                config.tours[f][t] = config.inicio[f]
                break
        
        print(config.tours[f])

    # apura custos dos config.tours
    custos_tours()

    # plotar todos os config.tours
    str = ['A','B','C','D','E','F','G','H','I', 'J']
    x, y = mapa_cidades.T
    plt.plot(x, y, color='black', marker='o', markersize=5)
    for i in range(config.CIDADES):
        plt.annotate(str[i], (x[i], y[i]), xytext=(x[i]+0.03, y[i]+0.1), bbox=dict(boxstyle="round", alpha=0.1), color="red", size=10, fontweight="bold")

    graph = np.empty((config.CIDADES+1, 2))
    for f in range(config.CIDADES):
        for c in range(config.CIDADES+1):
            graph[c] = mapa_cidades[config.tours[f][c].astype(int)]

        x, y = graph.T
        plt.plot(x, y, linestyle='dashed', color='green')

    # plotar melhor tour
    for c in range(config.CIDADES+1):
        graph[c] = mapa_cidades[config.tours[melhor_agente][c].astype(int)]

    x, y = graph.T
    #plt.ion()
    plt.plot(x, y, color='blue')
    #plt.draw()
    #plt.pause(0.005)
    plt.show()

    # atualiza feromonios
    atualiza_feromonio()
