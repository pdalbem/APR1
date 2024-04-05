a=()
b=()

for i in range(3):
    num=int(input("Digite o número: "))
    a = a + (num,)

for i in range(3):
    num=int(input("Digite o número: "))
    b = b + (num,)

c=()
for i in range(3):
    c = c + (a[i], b[i])
print(c) 

#OUTRA FORMA:
c=()
for i in range(3):
    c = c + (a[i],) + (b[i],)
print(c) 