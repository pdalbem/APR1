def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def main():
    num=int(input("Digite o número: "))
    while num >= 0:
        resultado=fatorial(num)
        print(f"O fatorial de {num} é {resultado}")
        num=int(input("Digite o número: "))

main()        