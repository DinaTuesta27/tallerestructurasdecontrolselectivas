"""
Entradas
*Sueldo del trabajador-->float-->sdt
Salida:
*Sueldo total-->float-->st

"""
sdt=float(input("Ingrese valor de sueldo del trabajador: "))
if(sdt<900000):
    st=(sdt*0.15)+sdt
    print(f"El sueldo total es:{st}")
elif(sdt>900000):
    st=(sdt*0.12)+sdt
    print(f"El sueldo del trabajador es:{st}")
else:
    print("El sueldo no optiene ningún aumento.")