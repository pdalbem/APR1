
import os

def limpar_tela():
     os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(texto):
    print("-" * 30)
    print(texto.center(30))
    print("-" * 30)

def exibir_menu():
    limpar_tela()
    exibir_cabecalho("MENU")

    itens_menu=["Cadastrar contato", "Listar contatos", "Pesquisar contato"]
    for i in range(len(itens_menu)):
         print(f"{i+1} - {itens_menu[i]}")
    print("0 - Sair") 
    print("-" * 30)

