import random
from .. import config

def gerarFeromonios(num_feromonios = config.CIDADES):

    with open("src/feromonios.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(", ")
        arquivo.write("Cidade da Pizzaria, ")
        for i in range(1, num_feromonios):
            arquivo.write(f"Cidade {i}, ")
        arquivo.write("\n")
        with open("src/dados.txt", "r", encoding="utf-8") as dados:
            linhas = dados.readlines()
            for i in range(num_feromonios):
                if i == 0:
                    arquivo.write("Cidade da Pizzaria, ")
                else:
                    arquivo.write(f"Cidade {i}, ")
                for y in range(num_feromonios):
                    if y == i:
                        distancia = 9.99
                    else:
                        # Remove espaços extras e quebra de linha
                        linhas[i+1] = linhas[i+1].strip()

                        # Remove o texto "Cidade X," do início
                        # e mantém apenas os números separados por vírgula
                        partes = linhas[i+1].split(",")
                        partes = [p.strip() for p in partes if p.strip() != ""]

                        # Ignora o primeiro elemento (ex: "Cidade 1")
                        if partes[y+1] != '0':
                            distancia = random.uniform(0.1, 0.4)
                        else:
                            distancia = 0
                            
                    if y < num_feromonios - 1:
                        arquivo.write(f"{distancia:.2f},")
                    else:
                        arquivo.write(f"{distancia:.2f}")
                if i < num_feromonios - 1:
                    arquivo.write("\n")

if __name__ == "__main__":
    gerarFeromonios()