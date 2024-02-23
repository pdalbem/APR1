nota_p1 = float(input("Digite a nota da prova 1: "))
nota_p2 = float(input("Digite a nota da prova 2: "))

nota_ex1 = float(input("Digite a nota do exercício 1: "))
nota_ex2 = float(input("Digite a nota da exercício 2: "))

media_exercicios = (nota_ex1+nota_ex2)/2
print("Média dos exercícios: ",media_exercicios)

nota_final = nota_p1*0.4 + nota_p2*0.4 + media_exercicios*0.2
print("Nota final: ",nota_final)

if nota_final>=6:
    print("Aprovado")
elif nota_final>=4:
    print("IFA")
else:
    print("Reprovado")