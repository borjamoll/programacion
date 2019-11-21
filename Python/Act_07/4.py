#Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. 
# La función debe sustituir todos los espacios en blanco de una frase por un asterisco, 
# y devolver el resultado para que el programa principal la imprima por pantalla.
lista=[]
lista+=str(input("Amigo, porfavor, introduzca una frase."))
def conversor(x):  
    for i in x:
        if i == " ":
            print("*", end="")
        else:
            print(i, end="")
conversor(lista)
