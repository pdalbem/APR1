nota  = float(input("Digite a nota: "))

maior_nota=nota
menor_nota=nota

qtd_alunos=0

while nota >=0:
    qtd_alunos+=1

    if nota>maior_nota:
        maior_nota=nota

    if nota<menor_nota:
        menor_nota=nota

    nota  = float(input("Digite a nota: "))

print("Quantidade de alunos: ", qtd_alunos)
print("Maior nota: ", maior_nota)
print("Menor nota: ", menor_nota)

