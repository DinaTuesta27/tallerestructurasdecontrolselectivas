"""
Entradas:
*Valor a pagar total(Monto total)-->float-->Mt
Salidas
*cantidad a invertir en fondos de la empresa-->float-->Fe
*Cantidad pago a crédito al fabricante (Intereses)-->float-->Pcf
*Prestamo al fabricante-->float-->Pf
*Cantidad prestada al banco-->float-->Pb
"""
#Entrada
Mt=float(input("Ingrese cantidad a pagar: "))
#Caja negra
if(Mt>5000000):
    Fe=Mt*0.55
    Pb=Mt*0.30
    Pf=Mt*0.15
    #Pcf=Pf+(Pf*0.20)
    Pcf=(Pf*0.20)
    print(f"La cantidad a invertir por fondos de la empresa es:{round(Fe,7)}")
    print("La cantidad a pagar por crédito al fabricante es:",Pcf)
    print("El monto a pagar por intereses son:",Pf)
    print("La cantidad prestada al banco es:",Pb)
elif(Mt<5000000):
    Fe=Mt*0.70
    Pf=Mt*0.30
    Pcf=Pf*0.20
    print(f"La cantidad a invertir por fondos de la empresa es:{round(Fe,7)}")
    print("La cantidad a pagar por crédito al fabricante es:",Pcf)
    print("El monto a pagar por intereses son:",Pf)
else:
    print("El valor es igual a 5000000.")  

