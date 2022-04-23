import math
"""
Entrada:
*A-->float-->a
*B-->float-->b
*C-->float-->c
Salidas:
x1-->float--> x1
x2-->float-->x2
"""
#Entradas
a=float(input("Digite A: "))
b=float(input("Digite B: "))
c=float(input("Digite C: "))
#Caja negra
d=b**2-(4*a*c)
x1=0.0 #variable global
x2=0.0
if(d>0):
    x1=(-b+math.sqrt(b**2-4*a*c)/(2*a)) #variable local(pertenece al if)
    x2=(-b-math.sqrt(b**2-4*a*c)/(2*a))
else:
    print("No tiene solución en los reales. ")
if(d==0):
    x2=-b/(2*a)
    x1=x2
#Salida
print("x1:",x1)
print("x2:",x2)
