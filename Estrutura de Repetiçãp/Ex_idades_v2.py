soma=0
qtd_pessoas=0
qtd_maior_idade=0
qtd_idosos=0

while True:
    idade = int(input("Digite a idade: "))

    if idade<0:
        break

    soma=soma+idade
    qtd_pessoas+=1

    if idade>=21:
        qtd_maior_idade+=1

    if idade>65:
        qtd_idosos+=1


print("Média das idades: ", soma/qtd_pessoas)
print("Quantidade de maiores de idade: ", qtd_maior_idade)
print("Porcentagem de idosos: ", qtd_idosos/qtd_pessoas)
