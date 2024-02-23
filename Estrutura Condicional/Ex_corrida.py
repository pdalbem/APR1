x= int(input("Digite a KM: "))
v1 = float(input("Digite o valor para v1: "))
v2 = float(input("Digite o valor para v2: "))
p = int(input("Digite a distância da corrida: "))

if (p<=x):
    total = p * v1
else:
    total = p * v2

print("Valor total da corrida: ", total)