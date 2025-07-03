def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}  
#TODO: Itere através de cada caractere na string string.
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:

    for caractere in string:  # Itera cada caractere da string
        if caractere in contador:
            contador[caractere] += 1  # Incrementa se já existe
        else:
            contador[caractere] = 1   # Adiciona com valor 1 se é novo  
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)