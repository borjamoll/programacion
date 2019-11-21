a=0
b=0
a=int(input("Introduzca el primer número: "))
b=int(input("Introduzca el segundo número: "))

for i in range(a,b):
    if a%2 == 0:
        print('El numero %s es par' % a)
    else:
         print('El numero %s es impar' % a)
    a=a+1
    
