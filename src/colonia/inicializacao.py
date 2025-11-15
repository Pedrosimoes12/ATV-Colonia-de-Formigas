from tools.leitorDeArquivos import lerMatrizTxt
import config

def carregarDados():
    matrizDistancia = lerMatrizTxt("../src/dados.txt")
    matrizFeromonio = lerMatrizTxt("../src/feromonios.txt")
    return matrizDistancia, matrizFeromonio
