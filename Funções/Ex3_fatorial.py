def fatorial(num):
    fat=1
    for i in range(2,num+1):
        fat=fat*i
    return fat

num=int(input("Digite um número: "))
while num>0:
    resultado=fatorial(num)
    print(f"O fatorial de {num} é {resultado}")    
    num=int(input("Digite um número: "))