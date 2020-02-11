#import random

##Criar um vetor
# tam = int(input("Informe o tamanho do vetor: "))
# vetor = [0] * tam
# x = 0

##Preencher o vetor
# while (x < tam):
#     vetor[x] = int(input("Informe os valores do vetor: "))
#     x = x + 1

##Printar o vetor
# x = 0
# while (x < tam):
#     print(vetor[x])
#     x = x + 1

##Criar uma matriz
# -> caso querer criar uma matriz com valores predefinidos // matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matriz = []
linha = int(input("Informe a quantidade de linhas da matriz: "))
coluna = int(input("Informe a quantidade de colunas da matriz: "))
valor = 0

#matriz tamanho customizado
for linha in range(0, linha):
    matriz.append([0] * coluna)

#preencher a matriz
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        valor = int(input("Informe o valor da {}° linha e {}° coluna: ".format(linha, coluna)))
        matriz[linha][coluna] = valor
        valor = 0

#preencher matriz com valores aleatorios //ps: tem que usar o "import random"
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        matriz[linha][coluna] = random.randint(5,30) #os valores entre parenteses são o inicio e o fim a ser sorteado
        valor = 0

#printar a matriz
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        print(matriz[linha][coluna], "  ", end="")
    print()
