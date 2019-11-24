
import random
import time
JUGADAS=3
diccionario_jugadas = {'1':'Piedra','2' : 'Papel', '3' : 'Tijeras' , '4' : 'Lagarto', '5' : 'Spock'}

def aleatorio_ppt():
    opcion_maquina=random.randint(1,3)
    return opcion_maquina

def comprueba_resultado(opciones_jugador1,opciones_jugador2):
    global diccionario_jugadas
    print("La máquina ha seleccionado: ", end="")
    print(diccionario_jugadas['%s' %(opciones_jugador2)])
    print("Tú has seleccionado: ", end="")
    print(diccionario_jugadas['%s' %(opciones_jugador1)])
    if (opciones_jugador1)==opciones_jugador2:
        print("Has empatado")
    elif (opciones_jugador1==3) and (opciones_jugador2==2):
        print("Has ganado")
    elif (opciones_jugador1==2) and (opciones_jugador2==1):
        print("Has ganado")
    elif (opciones_jugador1==1) and (opciones_jugador2==4):
        print("Has ganado")
    elif (opciones_jugador1==4) and (opciones_jugador2==5):
        print("Has ganado")
    elif (opciones_jugador1==5) and (opciones_jugador2==3):
        print("Has ganado")
    elif (opciones_jugador1==3) and (opciones_jugador2==4):
        print("Has ganado")
    elif (opciones_jugador1==4) and (opciones_jugador2==2):
        print("Has ganado")
    elif (opciones_jugador1==2) and (opciones_jugador2==5):
        print("Has ganado")
    elif (opciones_jugador1==5) and (opciones_jugador2==1):
        print("Has ganado")
    elif (opciones_jugador1==1) and (opciones_jugador2==3):
        print("Has ganado")
    else:
        print("Has perdido")
        
def menu_ppt_1j():
    global JUGADAS
    while(JUGADAS>=1):
        print(("=")*29)
        print("Indica la opción que quieres. ")
        print(("=")*29)
        print("1-Piedra")
        print("2-Papel")
        print("3-Tijeras")
        print("4-Lagarto")
        print("5-Spock")
        print(("=")*29)
        opciones_ppt_1j=int(input("Indica tu opción? "))
        print(("=")*29)
        opcion_maquina=aleatorio_ppt()
        comprueba_resultado(opciones_ppt_1j,opcion_maquina)
        JUGADAS-=1
    continuar=input("¿Quiere volver a jugar(s/n)?")
    if (continuar=="s"):
        JUGADAS=3
        menu_ppt_1j()
    else:
        print("Hasta la vista")

def menu_ppt_2j():
    JUGADAS=3
    terminar=False
    while(JUGADAS>0) and (terminar==False):
        print(("=")*29)
        jugador1=input("Indica el nombre del jugador 1.")
        jugador2=input("Indica el nombre del jugador 1.")
        print(("=")*29)
        print(("=")*29)
        print("Indica la opción que quieres.")
        print(("=")*29)
        print("1-Piedra")
        print("2-Papel")
        print("3-Tijeras")
        opciones_ppt_1j=int(input("La opción de %s:"))
        for x in 50:
            print(" ")
        opciones_ppt_2j=int(input("La opción de %s:"))
        for x in 50:
            print(" ")
        comprueba_resultado(opciones_ppt_1j,opcion_maquina)
        JUGADAS-=1
    continuar=input("¿Quiere volver a jugar?")
    if (continuar=="s"):
        JUGADAS=3
        terminar=False
    else:
        terminar=True


    
def piedra_papel_tijeras_big_bang():
    print(("=")*29)
    print("1- 1 jugador")
    print("2- 2 jugadores")
    print(("=")*29)
    opciones_ppt=input("¿Quieres jugar contra la máquina o contra otro jugador? ")
    if(opciones_ppt=="1"):
        menu_ppt_1j()
    #elif(opciones_ppt=="2"):
        #menu_ppt_2j()
    else:
        print("Opción incorrecta")
    


    
