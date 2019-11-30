num = 0
lista_primos = []
lista_primos_espejo = []
num_multiplicacion = []

#Funcion que comprueba si es primo o no.
def esPrimo(entero):
    indice=entero-1
    primo=True
    while primo==True and indice>1:
        if entero%indice==0:
            primo=False
            return primo
        indice-=1
    if primo==True:
        return primo

#Funcion que invierte el número (Modo espejo)
def obtenerEspejo(numero):
    numero_espejo = []
    espejo = ""
    for x in range(len(str(numero))):
        numero_espejo+=str(numero)[x]
    for x in range(len(str(numero))):
        y = len(str(numero))-x-1
        espejo+=str(numero)[y]
    espejo = int(espejo) #Lo paso a integuer para utilizarlo más cómodamente.
    return espejo

#Funcion para calcular todos los primos desde 0 hasta el número a comprobar.
def anyadirPrimos(numero,lista):
    for x in range(numero):
        if x > 1:
            indice=x-1
            primo=True
            while primo==True and indice>1:
                if x%indice==0:
                    primo=False
                indice-=1
            if primo==True:
                lista+=[x] #Valor que se ha comprobado.
        
#Funcion para obtener los múltiples
def obtenerNumMult(numero):
    num_multiplicacion = []
    multiplicacion = 1
    numero_str = str(numero)
    for x in numero_str:
        num_multiplicacion+=[int(x)]
    for x in range(len(num_multiplicacion)):
        multiplicacion*=num_multiplicacion[x]
    return(multiplicacion) 

#Funcion para calcular el primo inverso
def primo_inverso():
    global num
    return esPrimo(obtenerEspejo(num))


#Menu de comprobación de número
def menu():
    global num
    print("======================================")
    print(" PROGRAMA CÁLCULO CONJETURA SHELDON")
    print("======================================")
    num=int(input("Dame el número para el que quieres comprobar si cumple el teorema de Sheldon: "))
    anyadirPrimos(num,lista_primos) #Creacion de la lista de números primos del número, para poder fijar su posición.
    anyadirPrimos(obtenerEspejo(num),lista_primos_espejo) #Creacion de la lista de números primos del espejo para fijar su posición.
    posicion = len(lista_primos)+1 #Así calculo la posición entre los números primos
    posicion_espejo = len(lista_primos_espejo)+1 #Así calculo la posición entre los números primos del número espejo.
    if posicion == obtenerNumMult(num) == obtenerEspejo(posicion_espejo) and primo_inverso()==True and esPrimo(num)==True:
        print("El número",num,"cumple con la teoria de Sheldon.")
    else:
        print("El número",num,"no cumple con la teoria de Sheldon.")

menu()
