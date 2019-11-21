a=int(input('Dime un numero crack: '))
b=int(input('Dime otro numero crack: '))
numero=0
for i in range((b-a)+1):
    numero=numero+(a+1)
    if i==b-a:
        print (a+i, end=' ')
        print('=',numero)
    else:
        print(a+i, '+ ', end='')

