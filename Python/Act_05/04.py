a=int(input('Dime un numero crack: '))
factorial=a
for i in range(a-1):
    a=a-1
    factorial=(factorial*(a))
print(factorial)
