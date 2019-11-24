import random
import time
#Variables tic tac toe
tabla=[1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_cogidos=[]
turno=True
casillas_usadas=0
#Listas ahorcado
usada=[]
lista_lineas=[]
iguales="========================"
#Vidas piedra papel tijera, en ahorcado se modifican a 6
vidas=3
jugar=True
#Lista de letras en las que se divide la palabra del ahorcado
palabra_ahorcado=[]
#Diccionario para los elementos del piedra papel tijera
diccionario_jugadas = {'1':'Piedra','2' : 'Papel', '3' : 'Tijeras' , '4' : 'Lagarto', '5' : 'Spock'}
#Variables para las opciones de los jugadores y sus puntuaciones
opciones_jugador1=0
opciones_jugador2=0
puntuacion_jugador1=0
puntuacion_jugador2=0
identidad=""
letra=""

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
    if identidad=="La maquina" or identidad=="El jugador 2":
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
        print("Tú puntuación: ", puntuacion_jugador1)
        print("Puntuación de la máquina: ", puntuacion_jugador2)
    jugar=input("¿Quieres volver a jugar? (Si/No) ")
    if (jugar=="Si" or jugar=="si"):
        vidas=3
        piedra_papel_tijeras_big_bang()
    else:
        print("Hasta la vista")
        menu()

#Menu 2 jugadores
def menu_ppt_2j():
    global identidad
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
        for _ in range(20):
            print(" ")
        opciones_ppt_2j=int(input("La opción de %s: "%(jugador2)))
        for _ in range(20):
            print(" ")
        comprueba_resultado(opciones_ppt_1j,opciones_ppt_2j)
        jugadas-=1
    jugar=input("¿Quiere volver a jugar? (True/False)")
    if (jugar==True):
        jugadas=3
    else:
        jugar=False
        menu()

#Funcion para iniciar el Piedra Papel Tijeras. Permite elegir la modalidad (1-2 jugadores)
def piedra_papel_tijeras_big_bang():
    puntuacion_jugador1=0
    puntuacion_jugador2=0
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

#Función que comprueba si ya se ha introducido la letra
def letra_usada():
	global letra
	global usada
	if letra in usada:
		print("Ya has usado esa letra...")
	comprobar_letra(letra)
	return()
        
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
		usada.append(palabra_ahorcado[i])
	if letra_encontrada==False:
		vidas-=1
	
	return()

#Mientras que no se hayan encontrado tantas letra como tiene la palabra, se siguen pidiendo letras. También mientras no la palme el usuario.
def juego_ahorcado():
	global jugar
	global vidas
	global letra
	vidas = 6
	preguntar_palabra()
	crear_lineas()
	while lista_lineas!=palabra_ahorcado and jugar==True:
		print(" ")
		print(iguales)
		letra= input("Letra a comprobar? ")
		letra=letra.upper()
		letra_usada()
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
        
#=============================== TIC TAC TOE ===================================
def vaciar_tabla():
    tabla=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    return tabla

def mostrar_tabla():
    print(tabla[0] , " | " , tabla[1] , " | " , tabla[2])
    print(tabla[3] , " | " , tabla[4] , " | " , tabla[5])
    print(tabla[6] , " | " , tabla[7] , " | " , tabla[8])

def comprobar_resultado():
    if (tabla[0]==tabla[1]==tabla[2] or tabla[3]==tabla[4]==tabla[5] or tabla[6]==tabla[7]==tabla[8] or tabla[0]==tabla[3]==tabla[6] or tabla[1]==tabla[4]==tabla[7] or tabla[2]==tabla[5]==tabla[8] or tabla[0]==tabla[4]==tabla[8] or tabla[2]==tabla[4]==tabla[6]):
        return(True)


def pide_numero(x):
    global casillas_usadas
    global estado_partida
    turno=True
    estado_partida="En juego"
    jugador_tictactoe("X")
    #Empieza el IF DE LA MAQUINA
    if x == 1:
        while turno==True and casillas_usadas<9:
            posicion=random.randint(1,9)
            if tabla[posicion-1] and tabla[posicion-1]!="X" and tabla[posicion-1]!="Y":
                tabla[posicion-1]="Y"
                turno=False
                casillas_usadas+=1
                print("Jugada de la máquina:")
                mostrar_tabla()
            else:
                turno=True
        if comprobar_resultado()==True and estado_partida=="En juego":
            print("Vaya, ha ganado la máquina ...")
            estado_partida="Terminada" 
    #Termina el IF
    #EMPIEZA el IF DEL 2DO JUGADOR
    if x == 2 and casillas_usadas<9 and estado_partida=="En juego":
        jugador_tictactoe("Y")   
        
    #Termina el IF
    if estado_partida=="Terminada":
        print("Se da la partida por terminada.")
    else: 
        pide_numero(opcion)
    #OPCIÓN ALTERNATIVA: LISTA DE POSICIONES USADAS

def jugador_tictactoe(marcador):
    global turno
    global casillas_usadas
    global estado_partida
    while turno==True:
        posicion=int(input("Indica un número que será la posición: "))
        if (tabla[posicion-1]) and tabla[posicion-1]!="X" and tabla[posicion-1]!="Y":
            tabla[posicion-1]=marcador
            turno=False
            casillas_usadas+=1
            print("Tu jugada:")
            mostrar_tabla()
        else:
            print("Esa posición ya está ocupada")
            turno=True
    comprobar_resultado()
    if comprobar_resultado()==True:
        print("Enhorabuena, has ganado campeón.")
        turno=False
        estado_partida="Terminada"
        menu()
    elif casillas_usadas==9:
        estado_partida="Terminada"
        menu()
    else:
        turno=True
    return()

def modo_juego_tictactoe():
    global opcion
    print(("=")*29)
    print("1- 1 jugador")
    print("2- 2 jugadores")
    print(("=")*29)
    opcion=int(input("¿Quieres jugar contra la máquina o contra otro jugador? "))
    vaciar_tabla()
    mostrar_tabla()
    pide_numero(opcion)

#================================= MENÚ DE INICIO PROGRAMA ==============================
def menu():
    print(iguales)
    print("   SELECTOR DE JUEGOS   ")
    print(iguales)
    print(" OPCIÓN 1: PIEDRA PAPEL TIJERAS LAGARTO SPOOK ")
    print(" OPCIÓN 2: JUEGO DEL AHORCADO ")
    print(" OPCIÓN 3: TIC TAC TOE")
    print(" OPCIÓN 4: Salir")
    print(iguales)
    opcion = input("Introduce la opción deseada: ")
    if opcion == "1":
        piedra_papel_tijeras_big_bang()
    elif opcion == "2":
        juego_ahorcado()
    elif opcion == "3":
        modo_juego_tictactoe()
    elif opcion == "4":
        print("Gracias por utilizar nuestro proyecto.")
    else:
        print("Opción inválida. Prueba de nuevo.")
        menu()

menu()
