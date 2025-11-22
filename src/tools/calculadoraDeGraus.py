def calcularGraus(matrizDistancia):
    graus = []
    for cidade in matrizDistancia:
        conexoes = sum(1 for d in cidade if d != 0)
        graus.append(conexoes)
    return graus