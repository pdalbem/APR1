escolas=int(input("Digite a quantidade de escolas de samba: "))
categorias=int(input("Digite a quantidade de categorias de julgamento: "))
jurados=int(input("Digite a quantidade de jurados: "))

# matriz notas terá 3 dimensões: escolas X categorias X jurados
notas=[]
for i in range(escolas):
    linha=[]
    for j in range(categorias):
        col=[]
        for k in range(jurados):
            n=float(input(f"Digite a nota do jurado {k+1} para categoria {j+1} da escola{i+1}: "))
            col.append(n)
        linha.append(col)
    notas.append(linha)        

 
print(notas)

#Soma dos pontos
for i in range(escolas):  # equivalente a: for i in range(len(notas))
    soma=0
    for j in range(categorias): # equivalente a: for j in range(len(notas[i])) 
        for k in range(jurados):  # equiv. a: for k in range(len(notas[i][j]))
            soma+=notas[i][j][k]
    print(f"Total de pontos da escola {i+1}: ", soma)  

#Média por categoria
for i in range(escolas):
    for j in range(categorias):
        soma=0
        for k in range(jurados):
            soma+=notas[i][j][k]
        print(f"Escola {i} tem média {soma/jurados} na categoria {j}")    

