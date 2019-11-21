#Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de palabras 
# que contiene. Debe imprimir el programa principal el resultado. 
# Asumir que cada palabra está separada por un solo blanco:
#Asumir que cada palabra está separada por un solo blanco.
#No se sabe cómo están separadas las palabras. Pueden estar separadas por más de un blanco o por signos de puntuación.

lista=[]
lista+=str(input("Amigo, porfavor, introduzca una frase."))
def conversor(x):
    palabras=1  
    for i in x:
        if (i == " " or i == "." or i == "!" or i == "?" or i == ":"):
            print("Sumo una palabra.")
            palabras+=1
    return(palabras)
conversor(lista)