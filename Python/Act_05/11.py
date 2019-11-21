numero = int(input("Qué pasa jefe, ponme un número y te calculo los divisores. "))
dividendo=numero
divisor=numero
mensaje="Los divisores son:"
print(mensaje, end=" ")
for i in range(numero):
    if dividendo%divisor==0:
        print (divisor, end=" ")
    divisor=divisor-1

