
import os

def existe_arquivo(arq):
	return os.path.exists(arq)
		
def criar_arquivo(arq):
	a=open(arq,'w')
	a.close()

def limpar_tela():
     os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(texto):
    print("-" * 30)
    print(texto.center(30))
    print("-" * 30)

def exibir_menu():
    limpar_tela()
    exibir_cabecalho("MENU")

    itens_menu=["Cadastrar nota e aluno", "Mostrar alunos e notas", "Pesquisar"]
    for i in range(len(itens_menu)):
         print(f"{i+1} - {itens_menu[i]}")
    print("0 - Sair") 
    print("-" * 30)


def gravar_contato(arq,tupla):
	a=open(arq,'a')
	a.write(tupla[0] +'\t'+tupla[1] +'\t'+ str(tupla[2][0]) +'\t'+ str(tupla[2][1]) +'\t'+ str(tupla[2][2])+'\n')
	a.close()

def ler_nota():
    n=-1
    while n<0 or n>10:
        n = float(input("Digite a nota: "))
    return n

def ler_dados_aluno():
    limpar_tela()
    exibir_cabecalho("Dados do Aluno")
    pront=input("Digite o prontuário: ")
    nome=input("Digite o nome: ")
    lista_notas=[]
    for i in range(3):
        nota=ler_nota()
        lista_notas.append(nota)
    tupla=(pront,nome,lista_notas)
    return tupla  

def calcular_media_notas(notas):
    soma=0
    for i in notas:
        soma+=i
    return soma/3    

def mostrar_situacao(media):
     if media>=6:
          return "Aprovado"
     elif media>=4:
          return "IFA"
     else:
          return "Reprovado"

def mostrar_alunos(dicio):
    limpar_tela()
    exibir_cabecalho("Alunos cadastrados")
    for k,v in dicio.items():
         print("Prontuário: ",k)
         print("Nome: ", v[0])
         for i in range(3):
            print(f"Nota {i+1}: ", v[1][i]) 
         
         media=calcular_media_notas(v[1])
         print(f"Média das notas: {media:.2f} - Situação: ", mostrar_situacao(media))
         print()
    input("Pressione <enter> para continuar")  


def pesquisar_aluno(dicio):
    limpar_tela()
    exibir_cabecalho("Pesquisa")
    pesq=input("Prontuário ser procurado: ")
    achou=False
    for k in dicio.keys():
        if pesq.upper() in k.upper():
            achou=True
            print("Prontuário: ", k)
            print("Nome: ", dicio[k][0])
            for i in range(3):
                print(f"Nota {i+1}: ", dicio[k][1][i]) 
            media=calcular_media_notas(dicio[k][1])
            print(f"Média das notas: {media:.2f} - Situação: ", mostrar_situacao(media))
         
    if achou==False:
        print("Contato não cadastrado") 

    input("Pressione <enter> para continuar")      


def carregar_alunos(arq):
    a=open(arq,'r')
    dicio={}
    for linha in a:
        dados=linha.split('\t')
        dicio[dados[0]]=[dados[1],[float(dados[2]),float(dados[3]), float(dados[4])]]
    a.close()    
    return dicio
     
def inserir_dicionario(dicio,tupla):
     dicio[tupla[0]]=[tupla[1],tupla[2]]

def main():
    arq = 'notas_apr1.txt'
    if not existe_arquivo(arq):
        criar_arquivo(arq)
    
    dicio=carregar_alunos(arq)
    
    opcao=-1
    while opcao!=0:
        exibir_menu()
        opcao = int(input("Digite sua opção: "))
        if opcao==1:
            tupla=ler_dados_aluno()
            inserir_dicionario(dicio,tupla)
            gravar_contato(arq,tupla)
        if opcao==2:
            mostrar_alunos(dicio)
        if opcao==3:
            pesquisar_aluno(dicio)    

main()