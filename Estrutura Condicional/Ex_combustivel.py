gasolina = float(input("Digite o preço da gasolina: "))
etanol = float(input("Digite o preço da etanol: "))

comb = int(input("Digite o combustível desejado (1-gasolina, 2-etanol)"))
quantidade = float(input("Digite a quantidade comprada: "))

if (quantidade<=20):
    if (comb==1):
        total = (gasolina*quantidade) * 0.96
    else:
        total = (etanol*quantidade) * 0.97
else:
    if (comb==1):
        total = (gasolina*quantidade) * 0.94
    else:
        total = (etanol*quantidade) * 0.95    

print("Total a ser pago: ", total)

