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

def somar_matriz(A,B):
    mat=[]
    for i in range(len(A)):
        linha=[]
        for j in range(len(A[i])):
            n = A[i][j] + B[i][j]
            linha.append(n)
        mat.append(linha)
    return mat        


def main():
    N=int(input("Digite N: "))
    M=int(input("Digite M: "))
    matriz1=criar_matriz(N,M)
    print("Matriz 1 ")
    mostrar_matriz(matriz1)
    print()

    matriz2=criar_matriz(N,M)
    print("Matriz 2 ")
    mostrar_matriz(matriz2)
    print()

    matriz3 = somar_matriz(matriz1,matriz2)
    print("Soma das matrizes A e B ")
    mostrar_matriz(matriz3)

main()
