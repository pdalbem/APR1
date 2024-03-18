total_pessoas=0
soma_idades=0
menor_altura=3.0
qtd_pessoas_peso_altura=0 #contador para pessoas com peso >90 or altura <1.5
qtd_pessoas_acima_190=0   #contador para pessoas acima de 1.90m
qtd_pessoas_entre_10e30=0 #contador para pessoas com idade entre 10 e 30 anos

idade=int(input("Digite a idade: "))

while idade>=0:
    total_pessoas+=1
    soma_idades+=idade
    
    peso=float(input("Digite o peso: "))
    
    altura=float(input("Digite a altura: "))

    if altura<menor_altura:
        menor_altura=altura

    if peso>90 or altura<1.50:
        qtd_pessoas_peso_altura+=1    

    if altura>1.90:
        qtd_pessoas_acima_190+=1 # preciso contar, pois vou precisar dela para calcular a porcentagem
        if idade>=10 and idade <=30:
            qtd_pessoas_entre_10e30+=1

    idade=int(input("Digite a idade: "))

if total_pessoas>0:
    print("Média das idades: ", soma_idades/total_pessoas)
    print("Menor altura: ", menor_altura)
    print("Qtd de pessoas acima de 90Kg ou altura inferior a 1.50m: ", qtd_pessoas_peso_altura)

    #Repare que é a porcentagem de pessoas com idade entre 10 e 30, 
    #dentre as que possuem mais de 1.90
    #Por isso não devemos dividar pelo total de pessoas, mas somente pela quantidade de pessoas com mais de 1.90m
    if qtd_pessoas_acima_190>0:
        porcentagem=(qtd_pessoas_entre_10e30/qtd_pessoas_acima_190)*100
    else:
        porcentagem=0.0

    print(f"Porcentagem de pessoas com idade entre 10 e 30 anos, dentre aquelas com altura maior que 1.90m: {porcentagem}%") 
