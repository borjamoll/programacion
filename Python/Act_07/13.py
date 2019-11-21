#Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, 
# por tanto, habrán dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), 
# o de otra (con while). Ambas funciones devolverá true (si es es primo) o false (si no es primo). 
# El programa principal informará del resultado. 
# Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra. 
# Comentario: aprovecha el código que tienes ya creado
import time
numero=int(input("Número a calcular si es primo o compuesto: "))
es_primo=0

def funcion_for(x):
    inicio_for=time.time()
    es_primo=True
    dividendo=x
    divisor=x
    for i in range(x):
        divisor=divisor-1
        if divisor!=0 and divisor!=1:
            if dividendo%divisor==0:
                es_primo=False
    fin_for=time.time()
    tiempo=("Numero primo calculado en %fs. "% (fin_for - inicio_for))
    return(es_primo,tiempo)

def funcion_while(x):
    inicio_while = time.time()
    indice=x-1
    es_primo=True
    while es_primo==True and indice>1:
        if x%indice==0:
            es_primo=False
        indice=indice-1
    fin_while = time.time()
    tiempo=("Numero primo calculado en %fs. "% (fin_while - inicio_while))
    return(es_primo,tiempo)

respuesta=str(input("Dime amigo, que quieres usar, un WAIL o un PHOR. "))
if respuesta == "while":
    es_primo=funcion_while(numero)
    print(es_primo)

if respuesta == "for":
    es_primo=funcion_for(numero)
    print(es_primo)