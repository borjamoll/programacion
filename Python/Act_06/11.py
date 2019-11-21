#Escribir un programa para jugar a adivinar un número 
# (el ordenador "piensa" el número y el usuario lo ha de adivinar). 
# El programa empieza pidiendo entre qué números está el número a 
# adivinar, se "inventa" un número al azar y luego el usuario va 
# probando valores. El programa va decidiendo si son demasiado 
# grandes o pequeños. pista:

import random
import time
random.seed (time.time ())
intento = ""
n_intentos=0
min = int (input ( "Valor mínimo: "))
max = int (input ( "Valor máximo: "))
secreto = random.randint (min, max)
print(secreto)
while intento != secreto:
    intento=(int(input("Escribe un número: ")))
    n_intentos=n_intentos+1
    if intento>secreto:
        print("Demasiado grande! Vuelve a probar.", end=" ")
    elif intento<secreto:
        print("Demasiado pequeño! Vuelve a probar.", end=" ")
    else:
        print("Correcto, y con solo ",n_intentos," intentos.")
    
    