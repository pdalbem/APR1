N=0
while N<=0:
    N = int(input("Quantas pessoas você deseja adicionar? "))

pessoas = []

soma_idades=0
for i in range(N):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    tupla=(nome, idade)
    pessoas.append(tupla)
    soma_idades+=idade

media_idades = soma_idades/N
print("Média das idades: ", media_idades)

#Percurso por índice
for i in range(N):
    if pessoas[i][1]>media_idades:
        print ("Nome: ", pessoas[i][0])

#Percurso por valor
for pessoa in pessoas:
    if pessoa[1]>media_idades:
        print("Nome: ", pessoa[0])

