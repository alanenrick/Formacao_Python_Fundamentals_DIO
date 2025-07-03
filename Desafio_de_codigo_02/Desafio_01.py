

def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")


# import sys

# # Lê a linha de entrada e divide os números
# lista_strings = sys.stdin.readline().strip().split()

# # Converte os elementos da lista de strings para inteiros
# elementos = tuple(map(int, lista_strings))

# # Calcula a soma dos elementos da tupla
# soma = sum(elementos)

# # Imprime a saída no formato exigido
# print(f"A soma dos elementos da tupla é: {soma}")