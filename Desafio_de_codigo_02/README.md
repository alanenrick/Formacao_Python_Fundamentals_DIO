# Desafio 01

Descrição
Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.

Explicação de Resolução:

1. Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()".
2. Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings".
3. Armazene o resultado em uma variável chamada "elementos".

Documentação Oficial:
https://docs.python.org/pt-br/3/library/stdtypes.html#tuple

Entrada
A entrada para o seu programa será uma única linha de texto contendo vários números inteiros separados por espaços. Esses números devem ser lidos e convertidos para uma tupla de inteiros.

Saída
A saída do seu programa deve ser a soma de todos os números inteiros presentes na tupla. O resultado deve ser exibido de forma clara e amigável, seguindo o formato especificado. Aqui estão os passos detalhados para a saída:

1. Calcule a soma de todos os elementos da tupla.

2. Exiba a soma do valor calculado no formato: A soma dos elementos da tupla é: <soma>

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
2 5 6 7 9	A soma dos elementos da tupla é: 29
9 8 7 6 5	A soma dos elementos da tupla é: 35
50 50 50 50	A soma dos elementos da tupla é: 200
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.

# Desafio 02

Descrição
Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

Detalhamento:

Função elementos_comuns:
1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/introduction.html#lists

Entrada
Duas listas de inteiros separados apenas por espaço, por exemplo: 1 2 3 4 e 3 4 5 6.

Saída
Uma lista com os elementos comuns, por exemplo: [3, 4]. Caso a entrada seja diferente do esperado, retorne: "Entrada inválida."

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
1 2 3 4
3 4 5 6	Elementos comuns às duas listas: [3, 4]
9 8 7 6 5
5 2 3 7	Elementos comuns às duas listas: [5, 7]
a b c d
a e i o u	Entrada inválida.
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.

# Desafio 03

Descrição
O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries

Entrada
A função espera receber uma única string como entrada. Neste desafio, consideramos como casos de teste apenas strings textuais.

Saída
A função retorna um dicionário onde cada chave é um caractere presente na string de entrada e o valor associado a cada chave é a quantidade de vezes que o caractere ocorre na string.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
collections	{'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1}
numpy	{'n': 1, 'u': 1, 'm': 1, 'p': 1, 'y': 1}
datetime	{'d': 1, 'a': 1, 't': 2, 'e': 2, 'i': 1, 'm': 1}
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.