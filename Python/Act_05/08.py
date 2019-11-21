h=int(input('La altura, crack. '))
halt=1
for i in range (h):
    asteriscos=halt*"*"
    halt=halt+1
    print (asteriscos)
halt=halt-1
for i in range (h-1):
    halt=halt-1
    asteriscos=halt*"*"
    print (asteriscos)