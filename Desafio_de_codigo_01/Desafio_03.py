import sys

def conta_vogais(texto):
    vogais = set("aeiouAEIOU")
    resultado = 0
    
    for char in texto:
        if char in vogais:
            resultado += 1
    
    return resultado

texto = sys.stdin.readline().strip()
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")





# # texto = input()

# def conta_vogais(texto):
#     # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
#     vogais = set("aeiouAEIOU")
#     # TODO: Inicialize um contador para contar as vogais:
#     resultado = 0
    
#     # Iteramos pelos caracteres da string
#     for char in texto:
#         # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
#         if char in vogais:
#             resultado += 1
    
#     return resultado

# # Solicitamos ao usuário que insira uma string
# texto = input("Insira um texto: ")

# # Chamamos a função conta_vogais e exibimos o resultado
# resultado = conta_vogais(texto)
# print(f"O número de vogais na string '{texto}' é: {resultado}")
