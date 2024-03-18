inicio=int(input("Digite o termo inicial: "))
razao=int(input("Digite a razão: "))
quantidade_termos=int(input("Digite a quantidade de termos: "))

termo_atual=inicio 
i=1 #responsável por contar a quantidade de loops. Para quando i>quantidade_termos
while i<= quantidade_termos:
    print(termo_atual)
    termo_atual+=razao
    i+=1

  