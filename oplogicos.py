
"""
a=int(input("Informe o valor de A: "))
b=int(input("Informe o valor de B: "))
c=int(input("Informe o valor de C: "))
if(a>b and a>c):
    print("maior valor é o de A({})".format(a))
elif(c>a and c>b):
    print("maior valor é o de C({})".format(c))
else:
    if(b>c):
        print("maior valor é o de B({})".format(b))
~~~~~~~~
a=int(input("Informe o valor de A: "))
b=int(input("Informe o valor de B: "))
c=int(input("Informe o valor de C: "))
if(a>b and a>c and b>c):
    print("Ordem crescente: {} {} {}".format(c,b,a))
elif(a>b and a>c and b<c):
    print("Ordem crescente: {} {} {}".format(b,c,a))
elif(a>b and c>b and c>a):
    print("Ordem crescente: {} {} {}".format(b,a,c))
elif(b>a and c>b and c>a):
    print("Ordem crescente: {} {} {}".format(a,b,c))
else:
    if(b>a and b>c and a>c):
        print("Ordem crescente: {} {} {}".format(c,a,b))
    else:
        print("Ordem crescente: {} {} {}".format(a,c,b))

a=int(input("Informe o valor de A: "))
b=int(input("Informe o valor de B: "))
c=int(input("Informe o valor de C: "))
d=int(input("Informe o valor de D: "))

if(a>b and a>c and a>d):
    if(b<c and b<d):
        print("Maior é {}, menor é {}".format(a,b))
    elif(c<b and c<d):
        print("Maior é {}, menor é {}".format(a,c))
    elif(d<b and d<c):
        print("Maior é {}, menor é {}".format(a,d))
elif(b>a and b>c and b>d):
    if(a<c and a<d):
        print("Maior é {}, menor é {}".format(b,a))
    elif(c<a and c<d):
        print("Maior é {}, menor é {}".format(b,c))
    elif(d<a and d<c):
        print("Maior é {}, menor é {}".format(b,d))
elif(c>a and c>b and c>d):
    if(a<b and a<d):
        print("Maior é {}, menor é {}".format(c,a))
    elif(b<a and b<d):
        print("Maior é {}, menor é {}".format(c,b))
    elif(d<a and d<b):
        print("Maior é {}, menor é {}".format(c,d))
else:
    if(d>a and d>b and d>c):
        if(a<b and a<c):
            print("Maior é {}, menor é {}".format(d,a))
        elif(b<a and b<c):
            print("Maior é {}, menor é {}".format(d,b))
        else:
            print("Maior é {}, menor é {}".format(d,c))
"""
valor=float(input("Informe o valor do troco: "))
if(valor>100):
    resto=valor%100
    print(resto)
