from colonia.algoritmo import executarACO
import matplotlib.pyplot as plt
import networkx as nx

def main():
    caminho, custo, historico, matrizDistancia = executarACO()

    print("\nMelhor caminho encontrado:")
    print(caminho)
    print(f"Custo total: {custo:.2f}")

    plt.plot(historico)
    plt.xlabel("Iterações")
    plt.ylabel("Melhor Custo")
    plt.title("Convergência do ACO")
    plt.grid()
    plt.show()
    
    G = nx.Graph()

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        distancia = matrizDistancia[origem][destino]

        G.add_edge(origem, destino, weight=distancia)

    pos = nx.kamada_kawai_layout(G)

    plt.figure(figsize=(18, 18))
    nx.draw(G, pos, with_labels=True, node_size=300, font_size=8)

    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=7)

    plt.title("Grafo do Melhor Caminho com Distâncias da matrizDistancia")
    plt.show()

if __name__ == "__main__":
    main()
