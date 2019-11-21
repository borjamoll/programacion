#Escribe un programa que te pida dos numeros, de manera que el segundo sea mayor que el 
#primero. El programa termina escribiendo los dos numeros tal y como se pide:


print("Bienvenido al verificador de números superiores.")
numero=int(input("Porfavor, introduzca un número: "))
lista=[]
lista+=[numero]
numero2=int(input("Ahora escriba otro más grande. "))
while numero2<numero:
    numero2=int(input("ERROR. EL SEGUNDO NÚMERO ES IGUAL O MÁS PEQUEÑO. INTRODUZCA DE NUEVO. "))
lista+=[numero2]
print (lista)
