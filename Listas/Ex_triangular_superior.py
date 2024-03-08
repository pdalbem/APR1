# Faça um programa que leia um valor inteiro N representando o tamanho de uma
# matriz quadradada de N x N. Em seguida, o programa deve solicitar ao usuário valores
# para preencher a matriz. Por fim, o programa deve mostrar os elementos acima da
# diagonal principal (inclusive)

N=int(input("Digite o valor de N: "))
mat=[]

for i in range(N):
    linha=[]
    for j in range(N):
        num=int(input("Digite um número: "))
        linha.append(num)
    mat.append(linha)

for i in range(N):
    for j in range(N):
        if j>=i:
            print(mat[i][j])        