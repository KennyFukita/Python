from Aluno import Aluno 
# from Data import Data

def exibirAluno(a):
    print("Aluno")
    print("Nome: ", a.nome)
    print("Idade: ", a.idade)
    if(a.status == True):
        print("Status: Regular!")
    else:
        print("Status: Não Matriculado")
    print("{}/{}/{}".format(a.dataNasc.dia, a.dataNasc.mes, a.dataNasc.ano))

# def exibirData(d):
#     print("{}/{}/{}".format(d.dia, d.mes, d.ano))

# def obterTextoData(d):
#     return "{}/{}/{}".format(d.dia, d.mes, d.ano)
 
alu1 = Aluno()
alu1.nome = "Kenny"
alu1.idade = 19
alu1.status = True
alu1.dataNasc.dia = 12
alu1.dataNasc.mes = 9
alu1.dataNasc.ano = 2000

alu2 = Aluno()
alu2.nome = "sei la mano"
alu2.idade = 33
alu2.status = False
alu2.dataNasc.dia = 1
alu2.dataNasc.mes = 3
alu2.dataNasc.ano = 1997


exibirAluno(alu1)

# dataNascimento = Data()
# dataNascimento.dia = int(input("Informe o dia de nascimento:"))
# dataNascimento.mes = int(input("Informe o mês de nascimento:"))
# dataNascimento.ano = int(input("Informe o ano de nascimento:"))

# exibirData(dataNascimento)
# print(obterTextoData(dataNascimento))
