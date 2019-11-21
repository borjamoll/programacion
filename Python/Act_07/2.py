#Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), 
# los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. 
# La cadena final la imprimirá el programa por pantalla.

nombre=str(input("Primer nombre: "))
ape1=str(input("Primer apellido: "))
ape2=str(input("Segundo apellido: "))
def conversor(x,y,z):
    
    return(x + str(" ") + y + str(" ") + z)
print(conversor(nombre,ape1,ape2))



