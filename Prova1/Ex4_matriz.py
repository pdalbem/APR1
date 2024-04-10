# Faça um programa que leia uma matriz A de dimensão N x M, sendo N e M
# fornecidos pelo usuário. Em seguida, o programa deve criar e mostrar uma segunda matriz
# resultante da multiplicação dos elementos da matriz A pelo seu valor do seu maior elemento.

matriz=[]
maior_valor=-1

N=int(input("Digite o valor de N:"))
M=int(input("Digite o valor de M:"))

for i in range(N):
    linha=[]
    for j in range(M):
        num=int(input("Digite o número: "))
        linha.append(num)
        if num>maior_valor:
            maior_valor=num
    matriz.append(linha)   


print("Matriz original")
for i in range(N):
    for j in range(M):
        print(matriz[i][j], end=' ')
    print() 


# solução abaixo realiza uma cópia rasa, alterando a matriz original também
# matriz_multiplicada=matriz #shallow copy (cópia rasa) 

# for i in range(N):
#     for j in range(M):
#         matriz_multiplicada[i][j] = matriz[i][j]*maior_valor

#Solução melhor. Preserva matriz original
matriz_multiplicada=[]
for linha in matriz:
        nova_linha=[]
        for elemento in linha:
             nova_linha.append(elemento * maior_valor)
        matriz_multiplicada.append(nova_linha)


print(matriz_multiplicada)
print("Matriz multiplicada")
for i in range(N):
    for j in range(M):
        print(matriz_multiplicada[i][j], end=' ')
    print()         

 