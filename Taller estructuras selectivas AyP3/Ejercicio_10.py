"""
Entrada:
*Categoría-->int-->Ct
*Sueldo bruto-->float-->Sb
porcentaje de aunmento-->float-->por
Salida:
*categoría del trabajador-->int-->Ct
*Nuevo sueldo-->float-->Ns
"""
#Entrada
Ct=int(input("Ingrese la categoria del trabajador: "))
Sb=float(input("Ingrese sueldo bruto: "))
#Caja Negra
if(Ct==1):
    por=10/100
    Ns=Sb+(Sb*por)
    print(f"La categoría del trabajador es:{Ct}")
    print(f"El nuevo sueldo bruto es:{Ns}")
elif(Ct==2):
    por=15/100
    Ns=Sb+(Sb*por)
    print(f"La categoría del trabajador es:{Ct}")
    print(f"El nuevo sueldo bruto es:{Ns}")
elif(Ct==3):
    por=20/100
    Ns=Sb+(Sb*por)
    print(f"La categoría del trabajador es:{Ct}")
    print(f"El nuevo sueldo bruto es:{Ns}")
elif(Ct==4):
    por=40/100
    Ns=Sb+(Sb*por)
    print(f"La categoría del trabajador es:{Ct}")
    print(f"El nuevo sueldo bruto es:{Ns}")
elif(Ct==5):
    por=60/100
    Ns=Sb+(Sb*por)
    print(f"La categoría del trabajador es:{Ct}")
    print(f"El nuevo sueldo bruto es:{Ns}")
else:
    print("La categoría no clasifica en ninguna.")
