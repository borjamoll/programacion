#Escribe un programa que pida una frase, y pase la frase como parámetro a una función 
# que debe eliminar los espacios en blanco (compactar la frase). 
# El programa principal imprimirá por pantalla el resultado final.
lista=[]
lista+=str(input("Amigo, porfavor, introduzca una frase."))
def conversor(x):  
    for i in x:
        if i == " ":
            print("", end="")
        else:
            print(i, end="")
conversor(lista)
