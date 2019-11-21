lista=[]
a=int(input("Escribe límite: "))
b=int(input("Escribe un valor: "))
lista+=[b]
while b<=a:    
    c=int(input("Escriba otro valor: "))
    lista+=[c]
    b=b+c
print("El límite a superar es",a,". La lista creada es ", end="")
for i in range(len(lista)):
    print(lista[i], end="")
    if i < len(lista)-1:
        print(end=", ")
print(", ya que la suma de estos números es:",b,)