total_pessoas=0
soma_idades=0
menor_altura=3.0
qtd_pessoas_peso_altura=0 #contador para pessoas com peso >90 or altura <1.5
qtd_pessoas_acima_190=0
qtd_pessoas_entre_10e30=0

while True:
    idade=int(input("Digite a idade: "))
    if idade<0:
        break

    peso=float(input("Digite o peso: "))
  
    altura=float(input("Digite a altura: "))

    total_pessoas+=1
    soma_idades+=idade

    if altura<menor_altura:
        menor_altura=altura

    if peso>90 or altura<1.50:
        qtd_pessoas_peso_altura+=1    

    if altura>1.90:
        qtd_pessoas_acima_190+=1
        if idade>=10 and idade <=30:
            qtd_pessoas_entre_10e30+=1


if total_pessoas>0:
    print("Média das idades: ", soma_idades/total_pessoas)
    print("Menor altura: ", menor_altura)
    print("Qtd de pessoas acima de 90Kg ou altura inferior a 1.50m: ", qtd_pessoas_peso_altura)

    if qtd_pessoas_acima_190>0:
        porcentagem=(qtd_pessoas_entre_10e30/qtd_pessoas_acima_190)*100
    else:
        porcentagem=0.0

    print(f"Porcentagem de pessoas com idade entre 10 e 30 anos, dentre aquelas com altura maior que 1.90m: {porcentagem}%") 
