"""
Entradas
*Números enteros-->int-->A,B,C y D
Salida
*Resultados a las expresiones-->e1 y e2

"""
#Entrada
A=int(input("Ingrese el primer número: "))
B=int(input("Ingrese un segundo número: "))
C=int(input("Ingrese un tercer número: "))
D=int(input("Ingrese un cuarto número: "))
#Caja negra
if(D==0):
    E1=(A-C)**2
    print(f"El resultado de la ecuación es: {E1}")
elif(D>0):
    E2=(A-B)**3/D
    print(f"El resultado es: {E2}")
else:
    print("El último número no cumple con las condiciones.")