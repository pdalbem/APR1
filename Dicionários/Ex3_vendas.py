# Faça um programa que leia N (fornecido pelo usuário) produtos, seu preço
# unitário e a quantidade vendida deste produto na semana.
# APÓS ler todos os produtos, o programa deverá percorrer o
# dicionário e mostrar:
# - o valor total por produto
# - o valot total geral
# - encontrar e mostrar o produto mais vendido em termos de quantidade

vendas={}
N=int(input("Digite a quantidade de produtos: "))
for i in range(N):
    produto=input("Digite o nome do produto: ")
    preco=float(input("Digite o preço do produto: "))
    qtd=int(input("Digite a quantidade vendida: "))
    vendas[produto]=[preco,qtd]

total_geral=0
for k,v in vendas.items():
    total_produto=v[0]*v[1]
    print(f"Produto {k} -> {v[0]:.2f} X {v[1]}={total_produto:.2f}")
    total_geral+=total_produto
print(f"Total geral das vendas: {total_geral:.2f}")    

maior=-1
for k,v in vendas.items():
    if (v[1]>maior):
        maior=v[1]
        prod_mais_vendido=k
print(f"O produto mais vendido foi {prod_mais_vendido} com {maior} unidades e seu valor unitário é {vendas[prod_mais_vendido][0]:.2f}")        