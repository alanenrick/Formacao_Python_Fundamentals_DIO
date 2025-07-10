




## Decoradores com funções de operações

# def calculadora(operacao):
#     def soma(a, b):
#         return a + b
    
#     def subtracao (a, b):
#         return a - b
    
#     def multiplicacao (a, b):
#         return a * b
    
#     def divisao (a, b):
#         return a / b
    
#     def potencia (a, b):
#         return a ** b
    
#     match operacao:
#         case "+": 
#             return soma
#         case "-": 
#             return subtracao
#         case "*": 
#             return multiplicacao
#         case "/": 
#             return divisao
#         case "^": 
#             return potencia

# op = calculadora(input("insira o simbolo da operação: "))
# print(op(10, 2))

# op = calculadora(input("insira o simbolo da operação: "))
# print(op(10, 2))

# op = calculadora(input("insira o simbolo da operação: "))
# print(op(10, 2))

# op = calculadora(input("insira o simbolo da operação: "))
# print(op(10, 2))

# op = calculadora(input("insira o simbolo da operação: "))
# print(op(10, 2))




## Decoradores com funções 

# def mensagem (nome):
#     print ("executando mensagem")
#     return f"Oi {nome}"

# def mensagem_longa (nome):
#     print ("executando mensagem longa")
#     return f"Olá tudo bem com você {nome}"

# def executar (funcao, nome):
#     print ("executando executar")
#     return funcao(nome)

# print(executar(mensagem, "Alan"))
# print(mensagem_longa ("Alan"))