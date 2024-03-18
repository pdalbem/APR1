#Outra forma de representação
# A lista vai de 0 a N. 
# Cada número está armazenado na posição i da lista, 
# sendo que i corresponde ao seu próprio valor
# Se o índice for um número primo, o número permanece na lista; 
# Caso contrário, é alterado para 0 (zero)
# Exemplo para N=10
# [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0]

N=int(input("Digite o valor de N: "))

primos = list(range(N+1)) # lista que vai de 0 a N
primos[1]=0  # número 1 não é primo

p = 2
while (p * p <= N):
    if primos[p] != 0:
        for i in range(p * p, N+1, p):
            primos[i] = 0
    p += 1      

print(f"Os números primos de 2 até {N} são:")
for i in range(2, N+1):
    if primos[i] !=0:
        print(i, end=' ')
print()        