# Desafio 01
Python

Em Python existe várias formas de implementar o STDIN e STDOUT recomendamos utilizar sys.stdin.readline para o STDIN e o print para o STDOUT.

Exemplo:
import sys
a = int(sys.stdin.readline()) // Lê a linha de entrada
print(a); // Imprime o dado

Descrição
Neste desafio, você deve escreva uma solução que receba um número inteiro como entrada e determine se ele é par ou ímpar. Dessa forma, a solução deve retornar uma string indicando Par se o número for par e Ímpar se o número for ímpar.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html

Entrada
A entrada do programa é um único número inteiro.

Saída
A saída do programa é uma string que será Par se o número for par e Ímpar se o número for ímpar.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
2	Par
5	Ímpar
6	Par
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.

# Desafio 02

Descrição
Escreva uma solução que informe se um determinado ano é bissexto. Um ano é considerado bissexto se ele for divisível por 4. No entanto, anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400. Esta regra é usada para corrigir o calendário, de modo que ele fique em conformidade com o ano solar.

REGRA:

Um ano é bissexto se:
1. Ele é divisível por 4 e não é divisível por 100.
2. Ou ele é divisível por 400.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html

Entrada
O programa deve receber um número inteiro que representa o ano a ser verificado.

Saída
O programa deve imprimir SIM se o ano for bissexto, ou NÃO se não for bissexto.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
1975	NÃO
1986	NÃO
1992	SIM
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.

# Desafio 03

Descrição
Neste desafio, implemente uma solução para completar a função conta_vogais que conta o número de vogais em uma string fornecida como entrada. Vogais são caracteres específicos sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas (aeiouAEIOU).

Para resolver este desafio, siga os passos abaixo:

1. Defina um conjunto de vogais: Primeiramente, crie um conjunto contendo todas as vogais sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas.

2. Inicialize um contador: Em seguida, crie uma variável para contar o número de vogais encontradas na string, começando com zero.

3. Itere pelos caracteres da string: Aqui percorremos cada caractere na string de entrada para verificar se é uma vogal.

4. Verifique se o caractere é uma vogal: Para cada caractere, verifique se ele está presente no conjunto de vogais definido no passo 1. Se o caractere for uma vogal, incremente o contador em 1.

5. Retorne o contador: Após percorrer todos os caracteres da string, retorne o valor do contador, que representa o número total de vogais na string.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements

Entrada
A função recebe como entrada uma única string contendo letras/palavras.

Saída
A função deve retornar um número inteiro que representa o total de vogais encontradas na string de entrada.
 

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Python	O número de vogais na string 'Python' é: 1
Programação	O número de vogais na string 'Programação' é: 4
Função	O número de vogais na string 'Função' é: 2
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.