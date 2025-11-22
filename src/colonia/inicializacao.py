from tools.leitorDeArquivos import lerMatrizTxt
from tools.calculadoraDeGraus import calcularGraus
import config

def carregarDados():
    matrizDistancia = lerMatrizTxt("src/dados.txt")
    matrizFeromonio = lerMatrizTxt("src/feromonios.txt")
    graus = calcularGraus(matrizDistancia)
    return matrizDistancia, matrizFeromonio, graus