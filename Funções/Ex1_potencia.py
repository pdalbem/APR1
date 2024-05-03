def potencia(base,expoente):
    return base**expoente

def main():
    opcao='s'
    while opcao.upper()=='S':
        base=int(input("Digite a base: "))
        expoente=int(input("Digite o expoente: "))
        resultado=potencia(base,expoente)
        print(f"{base} elevado a {expoente} = {resultado}")

        opcao=input("Deseja executar novamente? (s/n)")

main()
