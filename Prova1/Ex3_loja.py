# Uma pequena loja comercializa apenas dez tipos de produtos. Faça um programa
# em Python que leia e armazene o valor unitário de cada produto em uma lista. Em seguida, leia e
# armazene em outra lista a quantidade vendida de cada produto na semana. Assuma que há uma
# preservação de posição (índices) nas listas, ou seja, a posição 0 se refere a um produto, a posição 1
# a outro produto e assim por diante.
# Em seguida, o programa deve calcular e mostrar:
# I) a quantidade vendida, valor unitário e valor total de cada produto. Exemplo: para o produto na
# posição 3, seu valor é 25.00 e foram vendidas 4 unidades. Logo, o total é 100.00 (4x25.00). Faça
# isso para todos os produtos!
# II) o valor unitário do produto mais vendido (Não se preocupe com empate).
# III) o valor total (em dinheiro) vendido durante a semana

valor=[]
qtd_vendida=[]
maior=-1

for i in range(10):
    n=float(input(f"Digite o preço do produto {i+1}: "))
    valor.append(n)
    n=int(input(f"Digite a quantidade vendida para o produto {i+1}: "))
    qtd_vendida.append(n)
    if n>maior:
        maior=n
        indice=i

soma=0
for i in range(10):
    print(f"Produto {i+1}")
    print("Valor unitário:", valor[i])
    print("Qtd vendida:" ,qtd_vendida[i])
    total=valor[i]*qtd_vendida[i]
    soma+=total
    print("Total do produto: " , total)
    print()

print("Valor unitário do produto mais vendido: ", valor[indice])    

print("Total geral: ", soma)