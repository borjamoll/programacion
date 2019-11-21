#Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. 
#Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. 
#El programa termina escribiendo la lista de números:

print("Bienvenido al verificador de números superiores.")
numero=int(input("Porfavor, introduzca un número: "))
lista=[]
lista+=[numero]
contador=0
contadorb=0
numero2=int(input("Introduce un número más grande, jefe: "))
while numero2>numero:
    numero=numero2
    lista+=[numero2]
    numero2=int(input("Introduce un número más grande, jefe: "))
print ("Los números escritos son: ", end=" ")
for i in range(len(lista)):
    print(lista[i], end="")
    if i < len(lista)-1:
        print(end=", ")