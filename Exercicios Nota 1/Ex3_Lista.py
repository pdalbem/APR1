N=int(input("Digite o valor de N: "))
lista=[]

#Leitura da lista via teclado
for i in range(N):
    num=int(input("Digite um número: "))
    lista.append(num)



X=int(input("Digite um número X: "))    

qtd_igual=0
qtd_maior=0
qtd_menor=0
lista_multiplicacao=[]
for i in lista:
    if i>X:
        qtd_maior+=1
    elif i<X:
        qtd_menor+=1
    else:
        qtd_igual+=1

    lista_multiplicacao.append(i*X)    

print(f"Quantidade de números iguais a {X}: ", qtd_igual)        
print(f"Quantidade de números maiores que {X}: ", qtd_maior)
print(f"Quantidade de números menores que {X}: ", qtd_menor)
print("Lista original:     ",lista)
print("Lista multiplicada: ",lista_multiplicacao)

