
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
soma = 0
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        soma = matriz[linha][coluna] + soma
    print()
print(soma)
