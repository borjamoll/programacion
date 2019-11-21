#Escribe un programa que te pida nombres de personas y sus números de teléfono. 
# Para terminar debe pulsar “S” cuando te pida el nombre. 
# El programa termina escribiendo nombres y números de teléfono. Nota: 
# La lista en la que se guardan los nombres y números de teléfono es 
# [[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.

lista=[]
listab=[]
a=(str(input("Dame un nombre: ")))
b=(str(input("Dame el teléfono: ")))
lista+=[a,b]
while a!="Si":
    listab+=[lista]
    lista=[]
    a=(str(input("Dame otro nombre, amigo: ")))
    b=(str(input("Dame otroo número, perfavore: ")))
    lista+=[a,b]
print(listab)
