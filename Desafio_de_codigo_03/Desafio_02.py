class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    def formatar_dados(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:
pessoa = Pessoa(nome, idade)
#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
print(pessoa.formatar_dados())