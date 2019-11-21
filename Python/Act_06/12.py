#Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de 
# adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta 
# adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, 
# mayor o igual al que se ha buscado.

import random
import time
random.seed (time.time ())
igual=0
respuesta=0
min = int (input ( "Valor mínimo: "))
max = int (input ( "Valor máximo: "))
secreto = random.randint (min, max)
print("Piensa un número entre %d y %d a ver si lo puedo adivinar. "% (min, max) )
while igual == 0:
    respuesta=input("¿El número es %d? Dime si es Menor, Igual o Mayor. "% (secreto))
    if respuesta=="Menor":
        max=secreto-1
        secreto= random.randint(min, max)
    elif respuesta=="Mayor":
        min=secreto+1
        secreto= random.randint(min, max)
    elif respuesta=="Igual":
        print("Gracias por jugar.")
        igual=1
    else:
        print("Respuesta inválida. Prueba de nuevo.")
