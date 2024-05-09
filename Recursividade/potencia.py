def potencia(base,expo):
    if expo==0:
        return 1
    else:
        return base*potencia(base,expo-1)

def main():
    base=int(input("Digite a base: "))
    expo=int(input("Digite o expoente: "))
    resultado=potencia(base,expo)
    print(f"{base} elevado a {expo} = {resultado}")
main()