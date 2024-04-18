# # Implemente um programa para armazenar o nome de N (fornecido pelo usuário)
# # alunos, bem como as notas obtidas por eles em 3 avaliações. Armazene os dados em um
# # dicionário, tendo o nome do aluno como chave e o valor sendo uma lista contendo as
# # notas:

N= int(input("Digite a quantidade de pessoas: "))

alunos={}

for i in range(N):
    nome=input("Nome: ")
    notas=[]
    for j in range(3):
        n=float(input(f"Nota {j+1}: "))
        notas.append(n)
    alunos[nome]=notas

print("Chaves:")
for i in alunos.keys():
    print(i)

print("Valores:")
for valor in alunos.values():
    for e in valor:
        print(e)
    print()    

print("Chaves e valores")
for k,v in alunos.items():
    print("Chave: ", k)
    print("Valores")
    for e in v:
        print(e)        
    print()
