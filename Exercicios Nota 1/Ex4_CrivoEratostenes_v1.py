# Nesta solução, a representação adotada foi:
# [2,3,4,5,...,N]

N=int(input("Digite o valor de N: "))

primos = list(range(2,N+1))

p = 2
while (p * p <= N):
    if p in primos:
        for i in range(p * p, N+1, p):
            if i in primos:
                primos.remove(i)
    p += 1    
print(f"Os números primos de 2 até {N} são:")
print(primos)