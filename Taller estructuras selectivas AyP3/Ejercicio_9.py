"""Entrada:
*Nombre cliente-->str-->N
*Monto de la compra-->float-->Mc
Salida:
*Nombre cliente-->str-->N
*Monto de la compra-->float-->Mc
*Monto a pagar con descuento-->float-->Mpd
*Descuento-->float-->desc
"""
#Entrada
N=str(input("Digite el nombre del cliente: "))
Mc=float(input("Digite el valor de la compra: "))
#Caja negra
if(Mc<50000):
    print(f"Nombre del cliente:{N} .")
    print(f"Total a pagar:{Mc}")
    print("No hay descuento.")
elif(50000<Mc<100000):
    desc=5/100
    Mpd=Mc-(Mc*desc)
    print(f"Nombre del cliente:{N} .") 
    print(f"Monto de compra:{Mc}")
    print(f"Monto a pagar:{Mpd} ") 
    print(f"Descuento aplicado es:{desc}")
elif(100000<Mc<700000):
    desc=11/100
    Mpd=Mc-(Mc*desc)
    print(f"Nombre del cliente:{N} .") 
    print(f"Monto de compra:{Mc}")
    print(f"Monto a pagar:{Mpd} ") 
    print(f"Descuento aplicado es:{desc}")
elif(700000<Mc<1500000):
    desc=18/100
    Mpd=Mc-(Mc*desc)
    print(f"Nombre del cliente:{N} .") 
    print(f"Monto de compra:{Mc}")
    print(f"Monto a pagar:{Mpd} .") 
    print(f"Descuento aplicado es:{desc}")
elif(Mc>1500000):
    desc=25/100
    Mpd=Mc-(Mc*desc)
    print(f"Nombre del cliente:{N} .") 
    print(f"Monto de compra:{Mc}")
    print(f"Monto a pagar:{Mpd} ") 
    print(f"Descuento aplicado es:{desc}")