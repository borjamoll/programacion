#Escribe un programa que te pida numeros y los guarde en una lista. 
#Para terminar de introducir numero, simplemente escribe Salir. 
#El programa termina escribiendo la lista de numeros.

print("Bienvenido al generador de listas. Si desea salir, escriba Salir.")
numero=str(input("Escriba un numero: "))
lista=[]
while numero!='Salir':
    lista+=[numero]
    numero=str(input("Escriba otro numero: "))
print (lista)