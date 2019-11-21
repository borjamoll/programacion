#Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, 
# y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

a=str(input("Porfavor, introduzca un texto largo: "))
def conversor(n):
    print(n.capitalize())
    print(n.lower())
    print(n.upper())
conversor(a)