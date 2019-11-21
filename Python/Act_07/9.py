#Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no. 
# Si coinciden las tres últimas letras tiene que decir que riman. 
# Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
#Riman (3 letras), riman un poco (2 letras), no riman (1 o -)

print("Ripios")
palabra1=str(input("Dime una palabra: "))
palabra2=str(input("Dime otra palabra: "))
def conversor(x,y):
    if x[-3:]==y[-3:]:
        print("Las palabras " + x + " y " + y + " riman.")
    elif x[-2:]==y[-2:]:
        print("Las palabras " + x + " y " + y + " riman un poco.")  
    else:
        print("Las palabras " + x + " y " + y + " no riman.")  
conversor(palabra1,palabra2)