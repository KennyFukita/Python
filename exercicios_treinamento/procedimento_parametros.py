# 1) A- Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(),
# que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.
# def somar(valor1, valor2):
#     print("Soma dos dois valores:",valor1+valor2)
# a = int(input("Informe o primeiro valor: "))
# b = int(input("Informe o segundo valor: "))
# somar(a, b)
#
# B- Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(),
# que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
# def multiplicar(valor1, valor2):
#     print("O produto dos dois valores:",valor1*valor2)
# a = int(input("Informe o primeiro valor: "))
# b = int(input("Informe o segundo valor: "))
# multiplicar(a, b)
#
# C- Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz().
# O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
# def calcularRaiz(valor1):
#     import math
#     print("Raiz quadrada do valor informado:",math.sqrt(valor1))
# a = int(input("Informe um valor: "))
# calcularRaiz(a)
#
# D- Faça um procedimento que calcule a potência de um número (XY) chamado calcularPotencia().
# # O procedimento deve receber os números por parâmetro, efetuar o cálculo e apresentar o resultado.
# def calcularPotencia(valor1,valor2):
#     print("A potência dos valores informados é: ",a**b)
# a = int(input("Informe um valor da base da potência: "))
# b = int(input("Informe o valor que a base será elevada: "))
# calcularPotencia(a,b)
#
# E- Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada().
# O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
# def calcularTabuada(valor1):
#     cont=0
#     print("Tabuada do valor informado")
#     while(cont<=10):
#         print(valor1,"x",cont,"=",valor1*cont)
#         cont=cont+1
# a = int(input("Informe um valor para realizar a tabuada: "))
# calcularTabuada(a)
#
# 2) A- Crie um procedimento que recebe um vetor de números inteiros por parâmetro.
# Esta função deve chamar imprimirVetor() e vai imprimir na tela todos os números do vetor informado.
# def imprimirVetor(v):
#     for cont in range(len(v)):
#         print(v[cont])
#
# tam=int(input("Informe o tamanho do vetor: "))
# vetor=[0]*tam
#
# for cont in range(len(vetor)):
#     vetor[cont]=int(input("Informe um valor do vetor:"))
#
# imprimirVetor(vetor)
#
# B- Faça um procedimento chamado encontrarMaior() que recebe um vetor de números inteiros como parâmetro,
# procure e informe somente o maior valor do vetor.
# def encontrarMaior(vet,maiorvalor):
#     maiorvalor=0
#     for cont in range(len(vet)):
#         if(maiorvalor < vet[cont]):
#             maiorvalor = vet[cont]
#     print("Maior valor encontrado foi: ",maiorvalor)
#
# tam=int(input("Informe o tamanho do vetor: "))
# vetor=[0]*tam
#
# for cont in range(len(vetor)):
#     vetor[cont]=int(input("Informe um valor do vetor:"))
# maior = 0
# encontrarMaior(vetor, maior)
#
# C- Faça um procedimento chamada encontrarMenor() que recebe um vetor de números inteiros como parâmetro,
# procure e informe somente o menor valor do vetor.
# def encontrarMenor(vet,menorvalor):
#     menorvalor=9999999999999999999999999999999
#     for cont in range(len(vet)):
#         if(menorvalor > vet[cont]):
#             menorvalor = vet[cont]
#     print("Menor valor encontrado foi: ",menorvalor)
#
# tam=int(input("Informe o tamanho do vetor: "))
# vetor=[0]*tam
#
# for cont in range(len(vetor)):
#     vetor[cont]=int(input("Informe um valor do vetor:"))
# menor = 999999999999999999
# encontrarMenor(vetor, menor)

"""

LISTA 2

"""

def turma(totalunos, nomedisci, notaA, notaB, notaC):
    nomedisci=input("Informe o nome da disciplina:")
    totalunos=int(input("Informe a quantidade de alunos:"))
    for linha in range(0,3):
        matriz.append([0]*totalunos)


turma(totalunos, nomedisci, notaA, notaB, notaC)
