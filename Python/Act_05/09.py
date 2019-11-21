h=int(input('Un lado, un lado !!! '))
l=int(input('Dame la altura, compañero. '))
if l==h:
    print("Mira jefe, te voy a ser sincero, lo que me has puesto es un cuadrado pero te lo calculo igual, por pena o por burla, como quieras tomártelo.")
halt=h*"*"
halt2=(h-2)*(' ')
halt3=("*"+str(halt2)+("*"))
a=l
for i in range(l):
    if a==l or l==1:
        print(halt)
    else:
        print(halt3)
    l=l-1