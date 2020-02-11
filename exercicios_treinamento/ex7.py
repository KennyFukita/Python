#matriz tamanho customizado
matriz = []
linha = int(input("Informe quantia de linhas: "))
coluna = int(input("Informe quantia de colunas: "))
print()
for linha in range(0,linha):
    matriz.append([0]*coluna)

#preencher matriz
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        valor = int(input("Valor da {}° coluna e {}° linha: ".format(coluna,linha)))
        matriz[linha][coluna] = valor
        valor = 0
print()
#printar matriz
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        print(matriz[linha][coluna], "\t", end="")
    print()

##somatoria de cada linha
# soma = 0
# for linha in range(0, len(matriz)):
#     for coluna in range(0, len(matriz[linha])):
#         soma = matriz[linha][coluna] + soma
#     print("Somatoria da {} linha: {}".format(linha,soma))
#     soma = 0

##somatoria de cada coluna
# x = 0
# soma = 0
# for linha in range(0, len(matriz)):
#     for coluna in range(0, len(matriz[linha])):
#         soma = matriz[linha][x] + soma
#     x = x + 1
#     print("Somatoria da {} coluna: {}".format(linha,soma))
#     soma = 0

##maior valor de cada linha
# maiorvalor = 0
# for linha in range(0, len(matriz)):
#     for coluna in range(0, len(matriz[linha])):
#         if(matriz[linha][coluna] > maiorvalor):
#             maiorvalor = matriz[linha][coluna]
#     print("Maior valor da {} linha: {}".format(linha,maiorvalor))
#     maiorvalor = 0

##maior valor de cada coluna
