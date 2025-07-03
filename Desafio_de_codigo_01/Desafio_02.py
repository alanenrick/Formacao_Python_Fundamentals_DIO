import sys

ano = int(input("Insira o ano: "))

def verificador_ano_bissexto(ano):
    
    resultado = "NÃO"
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado = "SIM"
    
    print(resultado)
      
# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:

verificador_ano_bissexto(ano)