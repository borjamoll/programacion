#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números 
# intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre 
# los dos valores iniciales. El programa termina escribiendo la lista de números.
lista=[]
a=int(input("Escribe un número: "))
b=int(input("Escribe otro número mayor: "))
while a>b:
    b=int(input("%d no es mayor que %d. Vuelve a probar: " % (b, a)))
lista+=[a,b]
c=int(input("Escribe un número entre %d y %d: " % (b, a)))
while c>a and b>c:
    lista+=[c]
    c=int(input("Escribe otro numero entre %d y %d: " % (b, a)))
print("Los números situados entre %d y %d que has escrito son:" % (b, a), end=" ")
for i in range(len(lista)):
    print(lista[i], end="")
    if i < len(lista)-1:
        print(end=", ")
