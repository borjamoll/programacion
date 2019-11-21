#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. 
# El procedimiento contará el número de vocales (de cada una) que aparecen, 
# y lo imprimirá por pantalla.

lista=[]
lista+=str(input("Dime algo: "))
vocales=0

def conversor(x,y):
    for i in x:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            y+=1
    print("El número de vocales es %d." % (y))
conversor(lista,vocales)
