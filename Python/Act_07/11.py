#Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. 
# Ésta debe devolver si es palíndroma o no , y el programa principal escribirá el resultado por pantalla:
#salta lenin el atlas
#dabale arroz a la zorra el abad

print("Ripios")
palindromo=True
dato=str(input("Dime una palabra o numero: "))
def conversor(x,palindromo):
    x=x.replace(" ", "") #Elimino los espacios para que compare los carácteres únicamente.
    for z in x:
        if str(x) != str(x)[::-1]:
            palindromo=False
    return(palindromo)
palindromo=conversor(dato,palindromo)
if palindromo==True:
    print(dato, end=" es capicua. ")


