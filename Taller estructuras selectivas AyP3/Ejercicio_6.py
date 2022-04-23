"""
Entradas:
*4 números enteros-->int-->A,B,C,D
Salida:
*Numero entero redondeado-->int-->Ner

"""
#Entrada
datos=input("Ingrese cuatro datos: ")
a,b,c,d=datos.split(" ")
#Caja negra
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if(c<5):
    a=a
    b=b
    c=0
    d=0
    print(a,b,c,d)   
elif(b==9 and c>=5):
    a=a+1
    b=0
    c=0
    d=0
    print(a,b,c,d)
elif(c>=5):
    a=a
    b=b+1
    c=0
    d=0
    print(a,b,c,d)


