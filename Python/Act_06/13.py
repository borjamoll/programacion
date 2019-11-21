numero_primo=int(input("Numero primo:"))
indice=numero_primo-1
es_primo=0
while indice>1:
    if numero_primo%indice==0:
        es_primo=1
    indice=indice-1
if es_primo==1:
    print("El número no es primo, jefe. ")
else:
    print("El número es primo, jefe. ")

#Reflexión, ¿Qué opción es mejor?: Un while es mejor que un for porque permite terminar el proceso una vez que 
#se comprueba que el numero en cuestión tiene residuo (Que no es número primo), en el for se repetirá el 
# proceso las veces estipuladas sí o sí.