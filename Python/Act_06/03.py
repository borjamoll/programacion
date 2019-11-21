#Escribe un programa que pida notas y los guarde en una lista. 
#Para terminar de introducir notas, escribe una nota que no esta entre 0 y 10. 
#El programa termina escribiendo la lista de notas.

print("Bienvenido al almacenador de notas.")
numero=int(input("Escriba una nota: "))
lista=[]
while numero>=0 and numero<=10:
    lista+=[numero]
    numero=int(input("Escriba otra nota: "))
print (lista)