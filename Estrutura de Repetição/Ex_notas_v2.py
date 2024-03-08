maior_nota=0
menor_nota=11

qtd_alunos=0

while True:
    nota  = float(input("Digite a nota: "))

    if nota<0:
        break
    
    qtd_alunos+=1

    if nota>maior_nota:
        maior_nota=nota

    if nota<menor_nota:
        menor_nota=nota
  
print("Quantidade de alunos: ", qtd_alunos)
print("Maior nota: ", maior_nota)
print("Menor nota: ", menor_nota)

