def ler_peso():
    peso=0
    while peso<=0:
        peso = float(input("Digite seu peso: "))
    return peso

def ler_altura():
    altura=0
    while altura<=0:
        altura = float(input("Digite sua altura: "))
    return altura

def calcular_imc(peso,altura):
    imc = peso / altura**2
    return imc

def mostrar_classificacao(imc):
    if (imc<18.5):
        print("Abaixo do peso")
    elif (imc<24.9):
        print("Peso normal")
    elif (imc<29.9):
        print("Acima do peso")
    elif (imc<34.9):
        print("Obesidade I")
    elif (imc<39.9):
        print("Obesidade II")
    else:
        print("Obesidade III")        

opcao='s'
while opcao.upper()=='S':
    peso=ler_peso()
    altura = ler_altura()
    imc=calcular_imc(peso,altura)
    mostrar_classificacao(imc)
    opcao=input("Executar com outros valores? (s/n)")
