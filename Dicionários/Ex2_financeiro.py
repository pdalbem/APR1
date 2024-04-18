# Implemente um mini gerenciador financeiro que armazena o total gasto do
# usuário em cada mês de um ano qualquer. Utilizando dicionário, a chave deverá ser
# o mês e o valor deverá ser o total de gasto no referido mês. 
# O programa deverá:
# - ler o mês e o referido valor gasto
# - calcular a média de gasto mensal
# - mostrar o mês que o usuário gastou menos dinheiro
# - mostrar o mês que o usuário gastou mais dinheiro

qtd_meses=3
gastos={}
for i in range(qtd_meses):
    mes=int(input("Mês: "))
    valor=float(input("Valor: "))
    gastos[mes]=valor

soma=0
for v in gastos.values():
    soma+=v
print(f"Média: {soma/qtd_meses:.2f}")

maior=-1
menor=999999999
for k,v in gastos.items():
    if v>maior:
        maior=v
        mes_maior_gasto=k
    if v<menor:
        menor=v
        mes_menor_gasto=k

print(f"O mês que mais gastou foi {mes_maior_gasto}: {maior:.2f}")
print(f"O mês que menos gastou foi {mes_menor_gasto}: {menor:.2f}")        