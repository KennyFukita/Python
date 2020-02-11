# Um professor precisa armazenar em uma lista os nomes dos alunos presentes em um minicurso.
# Faça um programa para armazenar 5 nomes e permitir que o professor digite o nome da cada um.
# Em seguida, apresente na tela todos os nomes informados.
v1 = [0] * 5
x = 0

while(x < len(v1)):
    v1[x] = input("Informe um nome:")
    x = x + 1
x = 0
print("Nomes informados: ")
while(x < len(v1)):
    print(v1[x])
    x = x + 1
