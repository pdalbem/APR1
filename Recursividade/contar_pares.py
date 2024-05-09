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


def contar_pares(lista):
    if len(lista)==0:
        return 0
    elif lista[0]%2==0:
           return 1 + contar_pares(lista[1:])
    else:
           return 0 + contar_pares(lista[1:])
    

def main():    
    N=int(input("Digite o tamanho da lista: "))
    lista=criar_lista(N)
    mostrar_lista(lista)
    
    pares=contar_pares(lista)
    if pares>0:
        print(f"Há {pares} números pares na lista")
    else:
        print(f"Não há números pares na lista") 
main()