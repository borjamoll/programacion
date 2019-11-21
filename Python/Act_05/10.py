a=int(input("klk ponme un numerele: "))
aux=1
aux2=a
for i in range(a):
    b=aux2*(' ')
    aux2=aux2-1 #Cálculo de los espacio (Se va reduciendo por uno cada que vez se reinicia el for).
    c=aux*('*') #Cálculo de los Asteriscos (Se multiplica el Auxiliar por asteriscos).
    aux=2+aux #Variable Auxiliar para ir aumentando los asteriscos, se utiliza en el próximo ciclo.
    d=str(b)+str(c) #D ES LA SUMA DE LOS ESPACIOS (B) + LOS ASTERISCOS (C).
    print(d)

