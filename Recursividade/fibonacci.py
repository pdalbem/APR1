def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def main():
    N=int(input("Digite a quantidade de termos: "))
    print(f"Mostrando os {N} termos da sequência de Fibonacci")
    for i in range(1,N+1):
        print(fibonacci(i))

main()