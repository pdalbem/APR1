
while True:
    num = int(input("Digite um número: "))
    if num<=0:
        break

    qtd_divisores=0

    for i in range(1,num+1):
        if num % i == 0:
            qtd_divisores+=1

    if qtd_divisores==2:
        print(f"Número {num} é primo")
    else:
        print(f"Número {num} não é primo")