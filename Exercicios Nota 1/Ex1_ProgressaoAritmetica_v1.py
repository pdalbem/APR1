inicio=int(input("Digite o termo inicial: "))
razao=int(input("Digite a razão: "))
quantidade_termos=int(input("Digite a quantidade de termos: "))

# Usando a propriedade da PA: último termo(an) é dado por an=a1+(n-1)*r
ultimo_termo= inicio+(quantidade_termos-1)*razao

for i in range(inicio,ultimo_termo+1,razao):
    print(i)    