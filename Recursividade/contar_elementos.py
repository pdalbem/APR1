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


def procurar(lista,item):
    if len(lista)==0:
        return 0
    elif lista[0]==item:
           return 1 + procurar(lista[1:],item)
    else:
           return 0 + procurar(lista[1:],item)
    

def main():    
    N=int(input("Digite o tamanho da lista: "))
    lista=criar_lista(N)
    mostrar_lista(lista)
    proc=int(input("Digite o item a ser procurado: ")) 
    qtd=procurar(lista,proc)
    if qtd>0:
        print(f"O item {proc} aparece {qtd} vezes na lista")
    else:
        print(f"O item {proc} não aparece na lista") 
main()