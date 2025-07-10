with open(
    r"C:\Users\Alanenrick\Documents\GitHub\Formacao_Python_Fundamentals_DIO\Aulas\ArquivoTeste.txt", "a"
) as arquivo:
    arquivo.write("\nEscrevendo no arquivo!!!")
    arquivo.write("\nEscrevendo no arquivo!!!")

with open(
    r"C:\Users\Alanenrick\Documents\GitHub\Formacao_Python_Fundamentals_DIO\Aulas\ArquivoTeste.txt", "r"
) as arquivo:
    print(arquivo.read())