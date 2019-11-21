#Practica 6: Escribe un programa que te pida palabras y las guarde en una lista. 
#Para terminar de introducir palabras, simplemente pulsa Enter. 
#El programa termina escribiendo la lista de palabras.

print("Bienvenido al generador de listas. Si desea salir, presione enter.")
palabra=str(input("Escriba una palabra: "))
lista=[]
while palabra!='':
    lista+=[palabra]
    palabra=str(input("Escriba otra palabra: "))
print (lista)