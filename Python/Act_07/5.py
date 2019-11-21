#Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función 
# que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. 
# Devolverá la función la frase modificada, y el programa principal la imprimirá:

lista=[]
lista+=str(input("Dime algo: "))
vocal=str(input("Dime una vocal: "))

def conversor(x):  
    print("La frase es ahora: ", end="")
    for i in x:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print(vocal, end="")
        else:
            print(i, end="")
conversor(lista)
