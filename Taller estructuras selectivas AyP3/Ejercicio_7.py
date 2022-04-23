"""
Entrada:
Kilómetros recorridos-->float-->Kmr
Salida:
Total a pagar por servicio-->float-->Tps

"""
#Entrada
Kmr=float(input("Ingrese total de kilómetros recorridos: "))
#Caja negra
if(Kmr<300):
    Tps=50000
    print("El total a pagar es:",Tps)
elif(Kmr>300 and Kmr<1000):
    adi=(Kmr-300)*30000
    Tps=70000+adi
    print("El total a pagar es:",Tps)
elif(Kmr>1000):
    adi=(Kmr-1000)*9000
    Tps=150000+adi
    print("El total a pagar es:",Tps)
else:
    print("El valor no calcula.")
