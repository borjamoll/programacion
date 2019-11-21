#Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 
# 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, 
# el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres 
# y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, 
# nota2, etc], etc]

#Dame un nombre: Héctor Quiroga
#Escribe una nota: 4
#Escribe otra nota: 8.5
#Escribe otra nota: 12
#Dame otro nombre: Inés Valls
#Escribe una nota: 7.5
#Escribe otra nota: 1
#Escribe otra nota: 2
#Escribe otra nota: -5
#Dame otro nombre:
#Las notas de los alumnos son:
#Héctor Quiroga: 4.0 - 8.5
#Inés Valls: 7.5 - 1.0 - 2.0

lista=[]
listab=[]
contador=int(0)
contadorb=int(0)
nombre=(str(input("Dame un nombre: ")))
nota=(int(input("Escribe una nota: ")))
nota2=(int(input("Escribe otra nota: ")))
while nota>0 and nota<10 and nota2>0 and nota<10:
    lista+=[nombre,nota,nota2]
    listab+=[lista]
    print("hi")
    nombre=(str(input("Dame otro: ")))
    nota=(int(input("Escribe una nota: ")))
    nota2=(int(input("Escribe otra nota: ")))
    lista=[]
    contador=contador+1
while contador>0:
    print("De nombre",listab[contadorb][0],":",listab[contadorb][1],"-",listab[contadorb][2],)
    contador=contador-1
    contadorb=contadorb+1

