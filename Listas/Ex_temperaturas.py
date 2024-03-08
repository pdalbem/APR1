# 1. Faça um programa que leia números referentes à temperatura diária de uma
# cidade durante uma semana. Na sequência, escreva quantos dias dessa semana a
# temperatura esteve acima da média.

temperaturas=[]   
soma=0
for i in range(7):
    temp = float(input(f"Digite a temperatura {i+1}: "))
    temperaturas.append(temp)
    soma+=temp

media = soma/7
print("Média: ", media)

contador=0
for t in temperaturas:
    if t>media:
        contador+=1

print("Quantidade acima da média: ", contador)
