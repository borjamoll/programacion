
# Simulacro de Examen de Python | Alumno: Daniel ALfredo Apesteguia Timoner
# Programa para videoclub. Funciones: Agregar peliculas, imprimir lista de películas, reservar películas y buscarlas.
CAPACIDAD_MAXIMA=3000 #(CONSTANTE)
iguales="==========================" #Tantos === me ensucian el programa, para que esté más claro el código.
respuesta=0
peliculas=0
id_pelicula=1
lista_peliculas=[]
nueva_pelicula=[] #Lista en la que se agregan los datos de cada nueva película. Esta de añade a la lista de películas.
pelicula_encontrada=[] #Aquí se acumulan los IDs (Temporalmente) de las películas encontradas con los parámetros del usuario

#Funcion -> Imprimir listado de películas
def anadir_peliculas(lista_peliculas):
    print (iguales)
    print("Listado de películas")
    print (iguales)
    for i in range(len(lista_peliculas)):
            print("Id:",end=" ")
            print(lista_peliculas[i][0], end=" ")
            print("Titulo:",end=" ")
            print(lista_peliculas[i][1], end=" ")
            print("Director:",end=" ")
            print(lista_peliculas[i][2], end=" ")
            print("Género:",end=" ")
            print(lista_peliculas[i][3], end=" ")
            print("Año:",end=" ")
            print(lista_peliculas[i][4])
            print("Duración:",end=" ")
            print(lista_peliculas[i][5], end=" ")
            print("Estado:",end=" ")
            if lista_peliculas[i][6] > 0:
                print("Disponible")
            if lista_peliculas[i][6] < 0:
                print("No disponible")
    return("")

#Funcion -> Añadir peliculas
def add_peliculas():
    global id_pelicula
    global lista_peliculas
    titulo=input("Dame el título de la peli: ")
    director=input("Dame el director de la peli: ")
    genero=input("Dame el género de la peli: ")
    ano=int(input("Dame el año de la peli: "))
    duracion=int(input("Dame la duración en minutos: "))
    copias=int(input("Dame la cantidad de copias que quieres introducir: "))
    nueva_pelicula=[id_pelicula,titulo,director,genero,ano,duracion,copias] #Lista que sumo a mi lista de películas
    lista_peliculas+=[nueva_pelicula]
    id_pelicula+=1 #Augmento 1 al ID para la próxima asignación
    print(anadir_peliculas(lista_peliculas)) #Imprimir la funcion que muestra la lista de peliculas, ahora actualizada

#Funcion -> Reservar peliculas
def reservar_peliculas():
    print(anadir_peliculas(lista_peliculas)) #Imprimir la funcion que muestra la lista de peliculas
    reservar=int(input("Dame el id de la película que quieres reservar: "))
    reservar-=1
    if lista_peliculas[reservar][6] > 0:
        print("La película ha sido reservada.")
        lista_peliculas[reservar][6]-=1
    elif lista_peliculas[reservar][6] < 0:
        print("La película no está disponible.")
    else: 
        print("El id de la pelicula no existe en este videoclub")

#Funcion -> Buscar peliculas. También incluye la fijación del parámetro de búsqueda (Si título, director, género o año.)
def parametro_busqueda():
    parametro=str(input("Elige por que quieres buscar: Titulo, Director, Genero o Año. "))
    if parametro.lower()=="titulo": #El parametro .lower es para evitar error cuando el usuario introduzca su parametro en mayusculas o minusculas. 
        parametro=1
    elif parametro.lower()=="director":
        parametro=2
    elif parametro.lower()=="genero":
        parametro=3
    else:
        parametro=4
    print(parametro)
    buscar_peliculas(parametro)

def buscar_peliculas(parametro):
    global pelicula_encontrada
    texto=str(input("Introduce el texto que quieres que aparezca en la búsqueda: "))
    for x in range(len(lista_peliculas)):
        if lista_peliculas[x][parametro] == texto:
            pelicula_encontrada+=[x] #Aqui se van anotando los IDs de las peliculas que coinciden con el criterio
    if pelicula_encontrada==[]:
            print("No existe ningún título que cumpla con los criterios de búsqueda seleccionados")
    else:
            #El programa imprime solo las peliculas encontradas.
            for i in range(len(pelicula_encontrada)):
                print (iguales)
                print("Listado de películas")
                print (iguales)
                print("Id:",end=" ")
                print(lista_peliculas[pelicula_encontrada[i]][0], end=" ")
                print("Titulo:",end=" ")
                print(lista_peliculas[pelicula_encontrada[i]][1], end=" ")
                print("Director:",end=" ")
                print(lista_peliculas[pelicula_encontrada[i]][2], end=" ")
                print("Género:",end=" ")
                print(lista_peliculas[pelicula_encontrada[i]][3], end=" ")
                print("Año:",end=" ")
                print(lista_peliculas[pelicula_encontrada[i]][4])
                print("Duración:",end=" ")
                print(lista_peliculas[pelicula_encontrada[i]][5], end=" ")
                print("Estado:",end=" ")
                if lista_peliculas[pelicula_encontrada[i]][6] > 0:
                    print("Disponible")
                if lista_peliculas[pelicula_encontrada[i]][6] < 0:
                    print("No disponible")

while respuesta != str(4):
# Estética del menú
    print (iguales)
    print ("=    M   E   N    U      =")
    print (iguales)
    print ("1) Añadir película")
    print ("2) Reserva película")
    print ("3) Busca películas")
    print ("4) Salir")
    print (iguales)
    respuesta=str(input("¿Qué opción deseas? "))

#Respuesta 1: Añadir peliculas
    if respuesta == (str(1)) and len(lista_peliculas) < CAPACIDAD_MAXIMA:
        add_peliculas() #Imprimir la funcion que muestra la lista de peliculas, ahora actualizada
    elif respuesta == (str(1)) and len(lista_peliculas) >= CAPACIDAD_MAXIMA:
        print("Lo siento, no nos queda espacio en la base de datos. Nuestro hosting, BanaHosting, nos ha capado los MB")

#Respuesta 2: Reservar peliculas
    elif respuesta == (str(2)): 
        reservar_peliculas()

#Respuesta 3: Buscar peliculas
    elif respuesta == (str(3)): 
        parametro_busqueda()
#Respuesta 4: Salir del programa
    else:
        print("Gracias por utilizar mi programa, desarrollado por DaniSoft.")