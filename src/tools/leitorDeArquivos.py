def lerMatrizTxt(caminhoArquivo):
    matriz = []

    with open(caminhoArquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        # Ignora o cabeçalho completamente
        for linha in linhas[1:]:
            linha = linha.strip()

            partes = linha.split(",")

            # Remove strings vazias criadas por vírgulas extra
            partes = [p.strip() for p in partes if p.strip() != ""]

            # Remove nome ("Cidade X" ou "Cidade da Pizzaria")
            valores = []
            for item in partes[1:]:
                try:
                    valores.append(float(item))
                except:
                    valores.append(0.0)

            matriz.append(valores)

    # --- Ajuste final: torna a matriz quadrada ---
    n = min(len(matriz), len(matriz[0]))

    matrizCorrigida = []
    for i in range(n):
        matrizCorrigida.append(matriz[i][:n])

    return matrizCorrigida
