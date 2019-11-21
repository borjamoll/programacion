#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con 
# un carácter en cada línea.
lista=[]
lista+=str(input("Amigo, porfavor, introduzca una frase."))
def conversor(x):  
    for i in x:
        print(i)
conversor(lista)

