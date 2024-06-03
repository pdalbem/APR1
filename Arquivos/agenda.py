from lib.arquivo import *
from lib.tela import *

def gravar_contato(arq,tupla):
	a=open(arq,'a')
	a.write(tupla[0] +'\t'+tupla[1]+'\t'+tupla[2]+'\n')
	a.close()

def ler_dados_contato():
    limpar_tela()
    exibir_cabecalho("Dados do Contato")
    nome=input("Digite o nome: ")
    email=input("Digite o email: ")
    fone=input("Digite o telefone: ")
    tupla=(nome,email,fone)
    return tupla  

def mostrar_contatos(dicio):
    limpar_tela()
    exibir_cabecalho("Contatos cadastrados")
    for k,v in dicio.items():
         print("Nome: ",k)
         print("Email: ", v[0])
         print("Telefone: ", v[1]) 
   
    input("Pressione <enter> para continuar")  


def pesquisar_contato(dicio):
    limpar_tela()
    exibir_cabecalho("Pesquisa de contato")
    pesq=input("Nome a ser procurado: ")
    achou=False
    for k in dicio.keys():
        if pesq.upper() in k.upper():
            achou=True
            print("Nome: ", k)
            print("Email: ", dicio[k][0])
            print("Telefone: ", dicio[k][1])
    if achou==False:
        print("Contato não cadastrado") 

    input("Pressione <enter> para continuar")      


def carregar_contatos(arq):
    a=open(arq,'r')
    dicio={}
    for linha in a:
        dados=linha.split('\t')
        dicio[dados[0]]=[dados[1],dados[2]]
    a.close()    
    return dicio
     
def inserir_dicionario(dicio,tupla):
     dicio[tupla[0]]=[tupla[1],tupla[2]]

def main():
    arq = 'contatos.txt'
    if not existe_arquivo(arq):
        criar_arquivo(arq)
    
    dicio=carregar_contatos(arq)
    
    opcao=-1
    while opcao!=0:
        exibir_menu()
        opcao = int(input("Digite sua opção: "))
        if opcao==1:
            tupla=ler_dados_contato()
            inserir_dicionario(dicio,tupla)
            gravar_contato(arq,tupla)
        if opcao==2:
            mostrar_contatos(dicio)
        if opcao==3:
            pesquisar_contato(dicio)    

main()