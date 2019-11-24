import random
import time
tabla=[1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_cogidos=[]
turno=True
casillas_usadas=0
print("Bienvenido al famoso juego TIC TAC TOE, mejor conocido como TRES EN RAYA.")
print("El sistema de juego es simple: Deberás introducir el número de la casilla que quieras, esta no debe estar pillada.")

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
    elif casillas_usadas==9:
        estado_partida="Terminada"
    else:
        turno=True
    return()

def modo_juego_tictactoe():
    global opcion
    opcion=int(input("Aqui viene lo q viene a ser la opcion. 1 es maquina, 2 para incorporar jugador extra: "))
    vaciar_tabla()
    mostrar_tabla()
    pide_numero(opcion)

modo_juego_tictactoe()



#1- usuario elige [XXY] x=espacio
                # [YYX] y
                # [XXY]
#2- comprobar resultado
#si derrepente se cumple la condicion del if es q gana el usuario
#3- maquina elige al azar
#4- comprobar resultado
#si derrepente se cumple la condicion del if es q gana la maquina

#arreglar problema de q se declara victoria automaticamente porq hay espacios en las tablas:
#- poniendo numeros en las tablas en vez de espacio
#- poniendo un caracter especial idéntico al espacio sin serlo

        
