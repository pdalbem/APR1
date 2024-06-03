# I) criar_matriz(N,M): deverá criar e retornar uma matriz NxM contendo
# valores inteiros fornecidos pelo usuário.
# II) somar_diagonal(matriz): recebe uma matriz e retorna a soma dos
# elementos de sua diagonal principal.
# III) mostrar_matriz(matriz): deverá mostrar a matriz formatada.
# IV) calcular_media(matriz): deverá calcular a média aritmética para cada uma
# das N linhas da matriz. A função retorna, então, uma lista de tamanho N, onde cada
# elemento i da lista representa a média da linha i da matriz


def criar_matriz(N,M):
    mat=[]
    for i in range(N):
        linha=[]
        for j in range(M):
            n=int(input(f"Digite o valor da linha {i+1}, coluna {j+1}: "))
            linha.append(n)
        mat.append(linha)
    return mat        

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()    

def somar_diagonal(matriz):
    soma=0
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[i])):
            if i==j:
                soma+=matriz[i][j]
            
    return soma        

def calcular_media(matriz):
    lista=[]
    for i in range(len(matriz)):
        soma=0
        qtd=len(matriz[i])
        for j in range(qtd):
            soma+=matriz[i][j]
        media=soma/qtd
        lista.append(media)
    return lista

def main():
    N=int(input("Digite N: "))
    M=int(input("Digite M: "))
    matriz=criar_matriz(N,M)
    print("Matriz")
    mostrar_matriz(matriz)
    soma_diagonal=somar_diagonal(matriz)
    print(f"Soma d a diagonal: {soma_diagonal}")

    lista_medias=calcular_media(matriz)
    for i in range(len(lista_medias)):
        print(f"Média da linha {i+1}:", lista_medias[i])

main()
