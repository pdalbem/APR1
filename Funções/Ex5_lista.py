def criar_lista(tam):
    lista=[]
    for i in range(tam):
        n=float(input(f"Digite o valor {i+1}: "))
        lista.append(n)
    return lista

def calcular_media(lista):
    soma=0
    for i in range(len(lista)):
        soma+=lista[i]
    media=soma/len(lista)
    return media    

def maior_salario(lista):
    maior=0
    for num in lista:
        if num>maior:
            maior=num
    return maior        

def atualizar_salario(lista,porc):
    media=calcular_media(lista)
    for i in range(len(lista)):
        if lista[i]<media:
            lista[i]*=(1+porc)
          
def mostrar_lista(lista):
    for num in lista:
        print(num)

def main():
    N=int(input("Digite o tamanho da lista: "))
    lista=criar_lista(N)
    media=calcular_media(lista)
    print(f"Média dos elementos: {media:.2f} ")
    print(f"O maior salário é {maior_salario(lista):.2f}")
    porcentagem=float(input("Digite a porcentagem do reajuste: "))
    atualizar_salario(lista,porcentagem)
    mostrar_lista(lista)


main()    