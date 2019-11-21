#Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos 
# a una función que comprobará si dicho carácter está en su nombre. 
# El resultado de dicha función lo imprimirá el programa principal por pantalla.

lista=[]
lista+=str(input("Dime tu nombre, querido amigo. "))
caracter=str(input("Dime un caracter: "))


def conversor(x):  
    for i in x:
        if i == caracter:
            print("Efectivamente. Ese carácter encúentrase en el nombre que introduciste.")
            caracter
conversor(lista)