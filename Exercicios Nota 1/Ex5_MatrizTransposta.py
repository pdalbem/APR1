N=int(input("Digite valor de N: "))
M=int(input("Digite valor de M: "))

A=[]
for i in range(N):
    linha=[]
    for j in range(M):
        n=int(input(f"Digite o valor da linha {i}, coluna {j}: "))
        linha.append(n)
    A.append(linha)

print("Matriz A:")
print(A)

transposta=[]
for i in range(M):
    linha=[]
    for j in range (N):
        linha.append(A[j][i])
    transposta.append(linha)

print("Matriz A Transposta:")
print(transposta)

