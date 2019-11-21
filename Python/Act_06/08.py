#Escribe un programa que te pida primero un número y luego te pida 
# números hasta que la suma de los números introducidos coincida con 
# el número inicial. El programa termina escribiendo la lista de números.
a=int(input("Escribe límite: "))
b=int(input("Escribe un valor: "))
lista=[]
lista+=[b]
while b<a:
    c=int(input("Escribe otro valor: "))
    if c+b>a:
        print("El valor",c,"es demasiado grande. Escribe otro valor:")
    else:
        b=b+c
        lista+=[c]
print("El límite a alcanzar es",a,". La lista creada es: ", end="")
for i in range(len(lista)):
    print(lista[i], end="")
    if i < len(lista)-1:
        print(end=", ")

