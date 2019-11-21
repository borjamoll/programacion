# P06E15:
import time
text = input("Introduce un texto: ")
palabra = input("Palabra a encontrar: ")
lista = text.split(" ")

iteracion = 0
inicio_while = time.time()
while lista[iteracion] != palabra:
    iteracion += 1
fin_while = time.time()

print("Palabra encontrada en %fs: %s; En el indice: %d" % (fin_while - inicio_while, lista[iteracion], iteracion))

indice=0
palabra_encontrada=False
inicio_for = time.time()
for i in range(len(lista)-1):
    if lista[i] == palabra and palabra_encontrada == False:
        indice=i
        palabra_encontrada=True
fin_for = time.time()
print("Palabra encontrada en %fs: %s; En el indice: %d" % (fin_for - inicio_for, palabra, indice))
# Don Serafin Nebot Ginard y Don Daniel Alfredo Apesteguia Timoner ©