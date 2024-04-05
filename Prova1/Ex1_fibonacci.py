# A sequência de Fibonacci é uma sucessão infinita de números naturais que
# começa com 0 1 e os números seguintes são a soma dos dois anteriores. Portanto: 0 1 1 2 3 5 8 13
# 21 34… Faça um programa em Python que mostre os N primeiros números da sequência de
# Fibonacci, com N dado pelo usuário. Não permita que N seja menor ou igual a 0 (zero).

N=0
while N<=0:
    N=int(input("Digite a quantidade de termos: "))

a=0
b=1
if N>=1:
    print(a)
if N>=2:
    print(b)

for i in range(3,N+1):
    c=a+b
    print(c)
    a=b
    b=c

