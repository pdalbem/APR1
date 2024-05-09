def hanoi(n,origem,destino,aux):
    if n > 0:
       hanoi(n-1, origem, aux, destino)
       print("Mova o disco", n, "de", origem, "para", destino)
       hanoi(n-1, aux, destino, origem)

def main():
    discos=int(input("Digite a quantidade de discos: "))
    hanoi(discos,"A","C","B")

main()