numero = int(input("Qué pasa jefe, ponme un número y te calculo los divisores. "))
a=0
dividendo=numero
divisor=numero
for i in range(numero):
    divisor=divisor-1
    if divisor!=0 and divisor!=1:
        if dividendo%divisor==0:
            a=1
if a==1:
    print("Jefe, este número no es primo.")
else:
    print("Jefe, efectivamente, este número es primo.")


