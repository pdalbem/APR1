def criar_lista(tam):
    lista=[]
    for i in range(tam):
        n=float(input(f"Digite o valor {i+1}: "))
        lista.append(n)
    return lista

def mostrar_lista(lista):
    for num in lista:
        print(num, end=' ')
    print()    

def maior_valor(lista):
    if len(lista)==1:
        return lista[0]
    if lista[0]>maior_valor(lista[1:]):
          return lista[0]
    else:
          return maior_valor(lista[1:])

def main():    
    N=int(input("Digite o tamanho da lista: "))
    lista=criar_lista(N)
    mostrar_lista(lista)
    maior=maior_valor(lista)
    print("O maior valor da lista é: ",maior)    

main()