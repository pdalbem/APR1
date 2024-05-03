def positivo_negativo(num):
    if num>0:
        valor =1
    elif num<0:
        valor = -1
    else:
        valor= 0
    return valor    

def mostrar_mensagem(result):
    if result==1:
        print(f"Número {num} é positivo")
    elif result==-1:
        print(f"Número {num} é negativo")
    else:
        print(f"Número é {num}")

def main():
    num=int(input("Digite o número: "))    
    resultado=positivo_negativo(num)
    mostrar_mensagem(resultado)

main()    