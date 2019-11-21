h=int(input('La altura, crack. '))
l=int(input('Ahora uno de los lados jefe... '))
if l==h:
    print("Mira jefe, te voy a ser sincero, lo que me has puesto es un cuadrado pero te lo calculo igual, por pena o por burla, como quieras tomártelo.")
halt=h*"*"
for i in range(l):
    l=l-1
    print(halt)