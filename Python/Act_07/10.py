#Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, 
# y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:
#Dime algo: 123321
#123321 es capicua.

print("Ripios")
palindromo=True
dato=str(input("Dime una palabra o numero: "))
def conversor(x,palindromo):
    for z in x:
        if str(x) != str(x)[::-1]:
            palindromo=False
    return(palindromo)
palindromo=conversor(dato,palindromo)
if palindromo==True:
    print(dato, end=" es capicua. ")


