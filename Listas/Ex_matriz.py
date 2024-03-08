# Faça um programa que leia uma matriz N x M (N e M fornecidos pelo usuário)
# de números inteiros e mostre:
# I) A soma dos números na diagonal principal da matriz
# II) A quantidade de números pares existentes em cada linha da matriz
# III) A média dos números, por coluna.

N=int(input("Digite o valor de N: "))
M=int(input("Digite o valor de M: "))

mat=[]

for i in range(N):
    linha=[]
    for j in range(M):
        n=int(input("Digite o valor: "))
        linha.append(n)
    mat.append(linha)

print(mat)

soma_diagonal=0
for i in range(N):
    for j in range(M):
        if i==j:
            soma_diagonal+=mat[i][j]
print("Soma da diagonal: ", soma_diagonal)

for i in range(N):
    qtd_pares=0
    for j in range(M):
        if mat[i][j]%2==0:
            qtd_pares+=1
    print(f"Quantidade de números pares na linha {i+1}: ", qtd_pares)        

for i in range(M):
    soma=0
    for j in range(N):
        soma+=mat[j][i]
    print(f"Média da coluna {i+1}", soma/N)             

