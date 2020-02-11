#Faça um programa para armazenar 6 números inteiros para uma loteria,
#permitindo que o usuário informe os números sorteados. Depois de preencher, informe uma mensagem e os números sorteados
v = [0]*6
x = 0
while(x < 6):
    v[x] = int(input("Informe um valor: "))
    x = x + 1
x = 0
print("Valores sorteados:")
while(x < 6):
    print(v[x])
    x = x + 1
