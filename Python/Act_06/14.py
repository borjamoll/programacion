# P06E14:
# Desarrolla un programa junto con tu compañero, apoyándote en la “metodología pair programming” que tenga las siguientes características:
# While
import time

print("Calculadora Fibonacci")
iteraciones = int(input("Introduce el numero de valores que quieres: "))
num_1 = 0
num_2 = 1

print("%d, %d, " % (num_1, num_2), end="")
inicio_while = time.time()
while iteraciones > 2:
    resultado = num_1 + num_2
    print(resultado, end="")

    if iteraciones > 3:
        print(end=", ")

    num_1 = num_2
    num_2 = resultado
    iteraciones -= 1
print("")
fin_while = time.time()

# For
iteraciones = int(input("Introduce el numero de valores que quieres: "))

num_1 = 0
num_2 = 1

print("%d, %d, " % (num_1, num_2), end="")
inicio_for = time.time()
for i in range(iteraciones - 2):
    resultado = num_1 + num_2
    print(resultado, end="")

    if i < iteraciones - 3:
        print(end=", ")

    num_1 = num_2
    num_2 = resultado
print("")
fin_for = time.time()
print("Duracion de while en s: %f" % (fin_while - inicio_while))
print("Duracion de for en s: %f" % (fin_for - inicio_for))

# Reflexion:
# En adecuacion, el for es mas apropiado para este caso puesto que es una secuencia a la que el usuario fija la cantidad de veces que se repetira la misma, si bien el while puede utilizarse para la misma funcion agregando una variable auxiliar, este es mas apropiado para un entorno en el que se desconozca la cantidad de veces que se repetira la secuencia.

# Reflexion sobre tiempo de ejecucion:
# En cuanto a tiempo de ejcucion los resultados, fijando distintos valores de iteraciones (1, 100, 10.000) los intervalos de tiempo no han diferido en una cantidad suficiente como para poder afirmar que uno sea mas rapido que el otro pues, en las mismas circunstancias, a veces uno era mas rapido que el otro (Con un margen de diferencia de 0,0001%).

# Don Serafin Nebot Ginard y Don Daniel Alfredo Apesteguia Timoner ©