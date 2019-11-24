lista_lineas=[]
iguales="========================"
vidas=6
jugar=True
usada=[]

#Función que divide palabras.
def split(palabra): 
	return [caracter for caracter in palabra]  

palabra = input("Palabra a introducir? ")
palabra=palabra.upper()
palabra_ahorcado=split(palabra)

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
	usada.append(palabra_ahorcado[i])
	return()
def letra_usada():
	if letra in usada:
		print("Ya has usado esa letra")
		comprobar_letra(letra)


#(**)APPEND . Sirve para iniciar pero no cuando se desarrolla el juego. bueno con parche funcionaría, Edu está en proceso de ello.
for i in range (len(palabra_ahorcado)):
	lista_lineas.append("_")
	print(lista_lineas[i],end=" ")  

#Mientras que no se hayan encontrado tantas letra como tiene la palabra, se siguen pidiendo letras. También mientras no la palme el usuario.
while lista_lineas!=palabra_ahorcado and jugar==True:
		print(" ")
		print(iguales)
		letra= input("Letra a comprobar? ")
		letra=letra.upper()
		comprobar_letra(letra)
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
                  
  
if lista_lineas==palabra_ahorcado:
	print("Enhorabuena. Te has pasado el juego, eres una bestia. Puedes pasar a otro juego, que eres un genio.")
#Y ahora...PAL MENU