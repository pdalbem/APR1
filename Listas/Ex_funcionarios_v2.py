# Faça um programa que fique lendo números reais positivos correspondentes aos
# salários de funcionários de uma empresa.
# O programa deve parar de fazer a leitura quando o usuário digitar um número negativo.
# Em seguida, o programa deve calcular a média desses salários e reajustá-los da seguinte
# forma:
# - salários acima da média receberão reajuste de 5%
# - salários abaixo da média receber]ao reajuste de 10%
# Mostre os valores dos novos salários

salarios=[]
soma=0

sal = float(input("Digite o salário: "))
while sal>=0:
    salarios.append(sal)
    soma+=sal
    sal = float(input("Digite o salário: "))


if len(salarios)>0:
    media = soma/len(salarios)
    print("Média: ", media)

    for i in range (len(salarios)):
        if salarios[i]>=media:
           salarios[i] = salarios[i] * 1.05
        else:
           salarios[i] = salarios[i] * 1.10

for s in salarios:
    print(s)        
