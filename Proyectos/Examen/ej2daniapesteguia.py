diccionario={}

def introducir_palabras():
    print("Introduce la lista de palabras y traducciones en formato palabra:traducción")
    palabras = input(str("separas por comas: roja:red,rojo:red;naranja:orange,mesa:table"))
    palabras_agregadas = False
    x = len(diccionario)
    while palabras_agregadas == False:
        
def traducir_texto():
    frase = input("Introduce una frase en español: ")
    frase = frase.split(" ") #Lo paso a lista para un uso más cómodo
    x = len(frase)
    while x > 0:
        print("hi")



def menu():
    print("======================================")
    print(" TRADUCTOR CASTELLANO-INGLES ")
    print("======================================")
    print("1) Introducir palabras")
    print("2) Traducir texto")
    print("3) Salir")
    print("======================================")   
    opcion = input("Que opción deseas?")
    if opcion == 1:
        introducir_palabras()
    elif opcion == 2:
        traducir_texto()
    elif opcion == 3:
        print("")
    else: 
        print("Opción inválida. Prueba de nuevo.")

menu()