# Faça um programa que fique lendo o cpf, nome e email de pessoas de uma
# comunidade. O programa deverá parar de ler dados pessoais quando for digitado
# ‘X’ para o cpf.
# Em seguida, o programa deverá ficar lendo dados de veículos:
# placa, marca, ano de de fabricação e cpf do proprietário (já armazenado no outro
# dicionário). O programa deverá parar de ler dados dos veículos quando for digitado
# ‘X’ para a placa
# Após as leituras, o programa deverá solicitar para digitar uma
# placa e, caso esteja armazenada no programa, deverá mostrar o nome do
# proprietário do veículo referente à placa digitada
# Por fim, o programa deverá mostrar, para cada pessoa armazenada
# no dicionário ‘pessoas’, os dados de seus veículos.

pessoas={}
cpf=input("CPF: ")
while cpf!='X' and cpf!='x':
    nome=input("Nome: ")
    email=input("Email: ")
    pessoas[cpf]=[nome,email]
    cpf=input("CPF: ")

carros={}
placa=input("Placa: ")
while placa!='X' and placa!='x':
    marca=input("Marca: ")
    ano=int(input("Ano: "))
    proprietario=input("CPF do proprietário: ")
    carros[placa]=[marca,ano,proprietario]
    placa=input("Placa: ")

placa_procurada=input("Digite uma placa já cadastrada: ")
for k,v in carros.items():
    if k==placa_procurada:
        print(f"O carro de placas {k}, marca {v[0]} percente a {pessoas[v[2]][0]} ")  # pessoas[v[2]][0] retorna o nome da pessoa

#Para cada pessoa no dicionário pessoas, eu pego o cpf(key) 
#e percorro o dicionário carros procurando (na parte valor) quem está associado a este cpf
#Ao encontrar, mostro as informações do carro 
for k,v in pessoas.items():
    print(f"Carros de {v[0]}:")
    for i,j in carros.items():
        if j[2]==k:
            print(f"Placa: {i}, marca: {j[0]}, ano: {j[1]}")

