"""
Entrada:
*Lectura del recibo anterior-->float-->lra
*Lectura del recibo actual-->float-->lrac
*horas de uso-->int-->ukw
*precio de kilovatio por hora-->float-->kwh
Salida:
*Total a pagar-->float-->tp
"""
#Entrada
lra=float(input("Ingrese valor de recibo anterior: "))
lrac=float(input("Ingrese valor de recibo actual: "))
ukw=float(input("Ingrese horas de uso en energía: "))
#Caja negra
dif=lrac-lra
if(dif<0):
    dif=dif*(-1)
if(ukw>0 and ukw<100):
    tp=dif*4600
    
elif(ukw>101 and ukw<300):
    tp=dif*80000
    
elif(ukw>301 and ukw<500):
    tp=dif*100000
    
elif(ukw>501):
    tp=dif*120000
    
#Salida
print(f"El total a pagar es:{tp}")

