"""
1- É um local na memória em que é possivel alocar algum dado, podendo ser do tipo "int", "float", etc.

2- x = 2

3- Não pode possuir caracteres especiais (com exceção do 'underline'), não pode começar com números e não possuir espaço.

4- É um tipo de valores que uma variável pode receber. Os tipos de dados mais comuns são: string, int, float e boolean.

5- divisão(/), multiplicação(*), soma(+), subtração(-) e potenciação(**).

6- x=64

7- x=40

8- x=3

9-
a)"import math"
b)"math.sqrt(4)"
c)"z=math.floor(x)"
d)"z=math.ceil(x)"
e)"z=math.trunc(x)"
f)"x=math.pow(5,3)"

10-
import math
raio=float(input("Informe o raio do circulo: "))
area=math.pi*(raio*raio)
print("Área do círculo: {}".format(area))

11- Maior(>), menor(<), maior ou igual(<=), menor ou igual (>=), igual (==) e diferente (!=). Operadores relacionais são utilizados para comparar
valores ou variáveis. Vai ser verdadeiro ou falso.

12-
x=10
y=20
z=30
temp=0
print("Valores de X, Y e Z antes da troca respectivamente: {}, {} e {}".format(x,y,z))
temp=x
x=z
z=y
y=temp
print("Valores de X, Y e Z após a troca respectivamente: {}, {} e {}".format(x,y,z))

13-
data=int(input("Informe a data (ddmmaa): "))
ano=data%100
data=int(data/100)
mes=data%100
dia=int(data/100)
print("Dia: {}, mês: {} e ano: {}".format(dia, mes, ano))

14-
x=float(input("Informe um valor: "))
x=x/3
print("A terça parte do valor informado é: {}".format(x))

15-
nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a segunda nota: "))
nota3=float(input("Informe a terceira nota: "))
nota4=float(input("Informe a quarta nota: "))
# media=(nota1+nota2*3+nota3*2+nota4*4)/10
media=(nota1+(nota2*3)+(nota3*2)+(nota4*4))/10
print("A média ponderada é: {}".format(media))

16-
import math
x=int(input("Informe o valor do ângulo: "))
print("Tangente: ",math.tan(x))
print("Seno: ",math.sin(x))
print("Cosseno: ",math.cos(x))

17-fazer regra de tres

import math
salmin=float(input("Informe o valor da salário mínimo: "))
qw=float(input("Informe de energia gasta em quilowatts: "))

18-
nome=input("Informe um nome: ")
print("\nNome completo: ",nome)
print("Primeira letra do nome: ",nome[0:1])
print("Última letra do nome: ",nome[len(nome)-1:len(nome)])
print("Do primeiro ao terceiro caractere: ",nome[0:3])
print("Quarto caractere: ",nome[3:4])
print("Todos caracteres, menos o primeiro: ",nome[1:len(nome)])
print("Os dois últimos caracteres: ",nome[len(nome)-2:len(nome)])

19-
"""
a=int(input("Informe o valor de A: "))
b=int(input("Informe o valor de B: "))
c=int(input("Informe o valor de C: "))
x= ( ( a+(b/(a+c))+2(a-b)+ math.log(64[,2]) ) / 3*math.pi ) + 1 
