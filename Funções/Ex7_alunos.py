def ler_dados_aluno():
    pront=input("Digite o prontuário: ")
    nome=input("Digite o nome: ")
    notas=[]
    for i in range(3):
        n=float(input(f"Digite a nota {i+1}: "))
        notas.append(n)
    tupla=(pront,nome,notas)
    return tupla    

def inserir_dicionario(dicio,tupla):
    dicio[tupla[0]]=[tupla[1],tupla[2]]
    return dicio

def mostrar_todos(dicio):
    for k,v in dicio.items():
        print(f"Prontuário: {k}")
        print(f"Nome: {v[0]}")
        print("Notas: ")
        for i in range(len(v[1])):
            print(v[1][i])
        print()    

def mostrar_especifico(dicio,pront):
    if pront in dicio:
        print(f"Prontuário: {pront}")
        print(f"Nome: {dicio[pront][0]}")
        print("Notas")
        for i in range(len(dicio[pront][1])):
            print(dicio[pront][1][i])
    else:
        print("Prontuário não encontrado")        


def main():
    dicio={}
    opcao=-1
    while opcao!=0:
        print("1 - Cadastrar aluno")
        print("2 - Mostrar todos")
        print("3 - Mostrar aluno específico")
        print("0 - Sair")
        opcao = int(input("Digite sua opção: "))
        if opcao==1:
            tupla=ler_dados_aluno()
            dicio=inserir_dicionario(dicio,tupla)
        if opcao==2:
            mostrar_todos(dicio)
        if opcao==3:
            pront=input("Digite o prontuário a ser procurado: ")
            mostrar_especifico(dicio,pront)

 
main()    