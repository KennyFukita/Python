# def imprimirVetor(vet):
#     for x in range(0,len(vet)):
#         vet[x] = int(input("Informe um valor:"))
#     x = 0
#     for x in range(0,len(vet)):
#         print(vet[x])
#
# tam = int(input("Informe o tamanho do vetor: "))
# vetor = [0]*tam
#
# imprimirVetor(vetor)

def imprimirVetor(v):
    for cont in range(len(v)):
        print(v[cont])

tam=int(input("Informe o tamanho do vetor: "))
vetor=[0]*tam

for cont in range(len(vetor)):
    vetor[cont]=int(input("Informe um valor do vetor:"))

imprimirVetor(vetor)
