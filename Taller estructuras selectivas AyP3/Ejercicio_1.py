"""
Entradas:
*Capital-->float-->ca
*Intereses-->int-->inte

Salida:
dinero total-->float-->dt
dinero de intereses-->float-->di

"""
#Entrada
ca=float(input("Ingrese cantidad de capital: "))
inte=int(input("Ingrese valor del los intereses: "))
#Caja Negra
porc=inte/100
di=ca*porc
if(di>100000):
    dt=di+ca
    print(f"El total del dinero en la cuenta es de: {dt}")
else:
    print(f"El total de intereses generados no supera los requeridos: {di}")
    
#Salida
