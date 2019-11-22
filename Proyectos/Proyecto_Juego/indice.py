import random
import time
lista_lineas=[]
iguales="========================"
vidas=3
jugar=True
palabra_ahorcado=[]
diccionario_jugadas = {'1':'Piedra','2' : 'Papel', '3' : 'Tijeras' , '4' : 'Lagarto', '5' : 'Spock'}
opciones_jugador1=0
opciones_jugador2=0
puntuacion_jugador1=0
puntuacion_jugador2=0
identidad=""

### =================== JUEGO PIEDRA PAPEL TIJERAS LAGARTO SPOCK  =================== ###

#Funcion maquina. Genera un valor aleatorio entre 1 y 5
def aleatorio_ppt():
    opcion_maquina=random.randint(1,5)
    return opcion_maquina

#Funcion comprobar resultado
def comprueba_resultado(opciones_jugador1,opciones_jugador2):
    global diccionario_jugadas
    global identidad
    global puntuacion_jugador1
    global puntuacion_jugador2
    print("" + str(identidad) + " ha seleccionado: ", end="")
    print(diccionario_jugadas['%s' %(opciones_jugador2)])
    print("Tú has seleccionado: ", end="")
    print(diccionario_jugadas['%s' %(opciones_jugador1)])
    if (opciones_jugador1)==opciones_jugador2:
        mensaje = "Has empatado"
    elif (opciones_jugador1==3) and (opciones_jugador2==2):
        mensaje = "Has ganado"
    elif (opciones_jugador1==2) and (opciones_jugador2==1):
        mensaje = "Has ganado"
    elif (opciones_jugador1==1) and (opciones_jugador2==4):
        mensaje = "Has ganado"
    elif (opciones_jugador1==4) and (opciones_jugador2==5):
        mensaje = "Has ganado"
    elif (opciones_jugador1==5) and (opciones_jugador2==3):
        mensaje = "Has ganado"
    elif (opciones_jugador1==3) and (opciones_jugador2==4):
        mensaje = "Has ganado"
    elif (opciones_jugador1==4) and (opciones_jugador2==2):
        mensaje = "Has ganado"
    elif (opciones_jugador1==2) and (opciones_jugador2==5):
        mensaje = "Has ganado"
    elif (opciones_jugador1==5) and (opciones_jugador2==1):
        mensaje = "Has ganado"
    elif (opciones_jugador1==1) and (opciones_jugador2==3):
        mensaje = "Has ganado"
    else:
        mensaje = "Has perdido"
    print(mensaje)
    print(identidad)
    if identidad == "El jugador 2":
        if mensaje == "Has ganado":
            puntuacion_jugador1+=1
        elif mensaje == "Has perdido":
            puntuacion_jugador2+=1 


#Menu 1 jugador       
def menu_ppt_1j():
    global vidas
    global identidad
    global puntuacion_jugador1
    global puntuacion_jugador2
    identidad="La maquina"
    while(vidas>=1):
        print(iguales)
        print("Indica la opción que quieres. ")
        print(iguales)
        print("1-Piedra")
        print("2-Papel")
        print("3-Tijeras")
        print("4-Lagarto")
        print("5-Spock")
        print(iguales)
        opciones_ppt_1j=int(input("Indica tu opción? "))
        print(iguales)
        comprueba_resultado(opciones_ppt_1j,aleatorio_ppt())
        vidas-=1
    jugar=input("¿Quiere volver a jugar? (True/False)")
    if (jugar==True):
        jugadas=3
        menu_ppt_1j()
    else:
        print("Hasta la vista")
        menu()

#Menu 2 jugadores
def menu_ppt_2j():
    global identidad
    puntuacion_jugador1=0
    puntuacion_jugador2=0
    identidad="El jugador 2"
    jugadas=3
    jugar=True
    while(jugadas>0) and (jugar==True):
        print(iguales)
        if jugadas == 3:
            jugador1=input("Indica tu nombre: ")
            jugador2=input("Indica el nombre del jugador 2: ")
            print(iguales)
        print("Tú puntuación: %i" %puntuacion_jugador1)
        print("Puntuación del jugador 2: %i" %puntuacion_jugador2)
        print(iguales)
        print("Indica la opción que quieres.")
        print(iguales)
        print("1-Piedra")
        print("2-Papel")
        print("3-Tijeras")
        print("4-Lagarto")
        print("5-Spock")
        opciones_ppt_1j=int(input("La opción de %s: "%(jugador1)))
        print(iguales)
        for i in range(20):
            print(" ")
        opciones_ppt_2j=int(input("La opción de %s: "%(jugador2)) )
        for x in range(20):
            print(" ")
        comprueba_resultado(opciones_ppt_1j,opciones_ppt_2j)
        jugadas-=1
    continuar=input("¿Quiere volver a jugar? (True/False)")
    if (jugar==True):
        jugadas=3
    else:
        jugar=False
        menu()

#Funcion para iniciar el Piedra Papel Tijeras. Permite elegir la modalidad (1-2 jugadores)
def piedra_papel_tijeras_big_bang():
    print(("=")*29)
    print("1- 1 jugador")
    print("2- 2 jugadores")
    print(("=")*29)
    opciones_ppt=input("¿Quieres jugar contra la máquina o contra otro jugador? ")
    if(opciones_ppt=="1"):
        menu_ppt_1j()
    elif(opciones_ppt=="2"):
        menu_ppt_2j()
    else:
        print("Opción inválida.")

### ====================================== JUEGO DEL AHORCADO =============================== ###

#Funcion que pregunta la palabra del juego
def preguntar_palabra():
	global palabra_ahorcado
	palabra = input("Palabra a introducir? ")
	palabra=palabra.upper()
	palabra_ahorcado=split(palabra)

#Función que crea la lista de líneas (_ _ _ _)
def crear_lineas():
	global palabra_ahorcado
	for i in range (len(palabra_ahorcado)):
		lista_lineas.append("_")
		print(lista_lineas[i],end=" ")  

#Función que divide palabras.
def split(palabra): 
	return [caracter for caracter in palabra]  

#Función que comprueba la letra introducida en la palabra. (**No sé que poner en return)
def comprobar_letra(letra):
	global palabra_ahorcado
	global vidas
	letra_encontrada=False
	for i in range(len(palabra_ahorcado)):
		if palabra_ahorcado[i] == letra:
			letra_encontrada=True
			lista_lineas[i]=palabra_ahorcado[i]
		print (lista_lineas[i],end=" ")
	if letra_encontrada==False:
		vidas-=1
	return()

#Mientras que no se hayan encontrado tantas letra como tiene la palabra, se siguen pidiendo letras. También mientras no la palme el usuario.
def juego_ahorcado():
	global jugar
	global vidas
	vidas = 6
	preguntar_palabra()
	crear_lineas()
	while lista_lineas!=palabra_ahorcado and jugar==True:
		print(" ")
		print(iguales)
		letra= input("Letra a comprobar? ")
		letra=letra.upper()
		comprobar_letra(letra)
		print("\nTe quedan %s vidas." % (vidas))
		print ("______")
		print ("| |")
		if vidas == 6:
			print ("|")
			print ("|")
			print ("|")
		else:
			if vidas == 5:
				print ("| (uwu)")
				print ("|")
				print ("|")
			else:
				if vidas == 4:
					print ("| (uwu)")
					print ("| |")
					print ("|")
				else:
					if vidas == 3:
						print ("| (uwu)")
						print ("| /|")
						print ("|")
					else:
						if vidas == 2:
							print ("| (uwu)")
							print ("| /|\ ")
							print ("|")
						else:
							if vidas == 1:
								print ("| (uwu)")
								print ("| /|\ ")
								print ("| / ")
							else:
								if vidas == 0:
									print ("| (uwu)")
									print ("| /|\ ")
									print ("| / \ ")
									print ("|")
									print ("|___")
									print(" ")
									print("La has cagado, máquina. Pero no pasa nada. Puedes pasar a otro juego, a ver si se te da mejor.")
									jugar=False
									menu()
	if lista_lineas==palabra_ahorcado:
		print("Enhorabuena. Te has pasado el juego, eres una bestia. Puedes pasar a otro juego, que eres un genio.")
		menu()

def menu():
    print(iguales)
    print("   SELECTOR DE JUEGOS   ")
    print(iguales)
    print(" OPCIÓN 1: PIEDRA PAPEL TIJERAS LAGARTO SPOOK ")
    print(" OPCIÓN 2: JUEGO DEL AHORCADO ")
    print(" OPCIÓN 3: TIC TAC TOE")
    print(iguales)
    opcion = input("Introduce la opción deseada: ")
    if opcion == "1":
        piedra_papel_tijeras_big_bang()
    elif opcion == "2":
        juego_ahorcado()
    elif opcion == "3":
        juego_ahorcado()
    else:
        print("Opción inválida. Prueba de nuevo.")
        menu()

menu()
