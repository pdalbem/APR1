def contar_pares(lista):
    if len(lista)==0:  
        return 0
    
    sublista = lista[0]
    pares = 0
    
    for x in sublista:
        if x % 2 == 0:
            pares += 1
    
    return pares + contar_pares(lista[1:])

def main():
    lista = [[4, 6, 5, 1], [5, 3, 9], [], [4, 0, 10]]
    print(contar_pares(lista))  

main()