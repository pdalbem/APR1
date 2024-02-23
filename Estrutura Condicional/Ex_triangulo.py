a = int(input("Digite o lado a: "))
b = int(input("Digite o lado b: "))
c = int(input("Digite o lado c: "))

if a<(b+c) and b<(a+c) and c<(a+b):
    if (a==b and b==c):
        print("Triângulo equilátero")
    elif (a==b or b==c or a==c):
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não forma um triângulo")            