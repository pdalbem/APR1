#Outra forma de representação
#A lista vai de 0 a N. Se o índice for um número primo, recebe True; False, caso contrário
# Exemplo para N=10
# [False, False, True, True, False, True, False, True,  False, False, False]

N=int(input("Digite o valor de N: "))
primos = [True] * (N+1) # lista que vai de 0 a  N
primos[0]=False  # 0 não é primo
primos[1]=False  # 1 não é primo

p = 2
while (p * p <= N):
    if primos[p] == True:
        for i in range(p * p, N+1, p):
            primos[i] = False
    p += 1      

print(f"Os números primos de 2 até {N} são:")
for i in range(2, N+1):
    if primos[i]:
        print(i, end=' ')
print()        