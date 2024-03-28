# Em um programa acadêmico escrito em Python, as matrículas dos alunos em
# disciplinas no 1º sem/2024 são armazenadas em listas da seguinte forma: para cada disciplina
# existe uma lista e os prontuários dos alunos que cursam a disciplina estão nesta lista. Por
# exemplo, na lista poo estão os prontuários de todos os alunos matriculados na disciplina
# Programação Orientada a Objetos. E assim por diante. Faça um programa que leia os prontuários
# de 20 alunos matriculados na disciplina Algoritmos e Programação 1 (APR1). Em seguida, leia os
# prontuários de 30 alunos matriculados na disciplina Introdução à Web (IWEB). Agora, mostre
# quem são os alunos (prontuários) que estão cursando ao mesmo tempo APR1 e IWEB.

apr=[]
iweb=[]

qtd_alunos_apr=5
qtd_alunos_iweb=2

print("Digite os prontuários dos alunos de APR1: ")
for i in range (qtd_alunos_apr):
    pront=input()
    apr.append(pront)

print("Digite os prontuários dos alunos de IWEB: ")
for i in range (qtd_alunos_iweb):
    pront=input()
    iweb.append(pront)   

for i in range(len(apr)):
    for j in range(len(iweb)):
        if apr[i]==iweb[j]:
            print(f"Prontuário {apr[i]} está matriculado nas duas disciplinas")

          