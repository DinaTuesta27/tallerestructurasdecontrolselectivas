"""
Entradas:
*Sueldo mensual-->float-->Sm
*Ventas departamento 1-->float-->Vd1
*Ventas departamento 2-->float-->Vd2
*Ventas departamento 3-->float-->Vd3
Salida:
*Sueldo de vendedor departamento 1-->float-->Svd1
*Sueldo de vendedor departamento 2-->float-->Svd2
*Sueldo de vendedor departamento 3-->float-->Svd3
"""
#Entradas
Sm=float(input("Ingrese valor del sueldo mensual: "))
Vd1=float(input("Ingrese importe de las ventas del departamento 1: "))
Vd2=float(input("Ingrese importe de las ventas del departamento 2: "))
Vd3=float(input("Ingrese importe de las ventas del departamento 3: "))
#Caja negra
Impt=(Vd1+Vd2+Vd3)*0.33
if(Vd1>Impt):
    Svd1=Sm+(Sm*0.20)
    print(f"El sueldo del vendedor del departamento 1 es:{Svd1}")
else:
    print(f"El pago para el departamento 1 es: {Sm}")

if(Vd2>Impt):
    Svd2=Sm+(Sm*0.20)
    print(f"El sueldo del vendedor del departamento 2 es:{Svd2}")
else:
    print(f"El pago para el vendedor del departamento 2 es: {Sm}")

if(Vd3>Impt):
    Svd3=Sm+(Sm*0.20)
    print(f"El sueldo del vendedor del departamento 3 es:{Svd3}")
else:
    print(f"El pago para el vendedor del departamento 3 es: {Sm}")


