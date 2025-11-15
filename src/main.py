from colonia.algoritmo import executarACO
import matplotlib.pyplot as plt

def main():
    caminho, custo, historico = executarACO()

    print("\nMelhor caminho encontrado:")
    print(caminho)
    print(f"Custo total: {custo:.2f}")

    plt.plot(historico)
    plt.xlabel("Iterações")
    plt.ylabel("Melhor Custo")
    plt.title("Convergência do ACO")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
