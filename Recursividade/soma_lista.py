def criar_lista(tam):
    lista=[]
    for i in range(tam):
        n=int(input(f"Digite o valor {i+1}: "))
        lista.append(n)
    return lista

def mostrar_lista(lista):
    for num in lista:
        print(num, end=' ')
    print()    

def somar_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somar_lista(lista[1:])

def main():
    N=int(input("Digite a quantidade de elementos: "))
    lista=criar_lista(N)
    mostrar_lista(lista)
    soma = somar_lista(lista)

    print(f"A soma dos elementos é: {soma:.2f}")

main()
    