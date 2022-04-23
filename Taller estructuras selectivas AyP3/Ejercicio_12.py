"""
Entrada:
*Cantidad de dinero-->float-->Cd
Salida:
*Total de billetes-->float-->Tb
*Total de monedas-->float-->Tm
"""
#Entrada
Cd=float(input("Ingrese una cantidad de dinero: "))
#Caja negra
#Billetes
bc=Cd/100000
bci=(Cd%100000)//50000
bv=(Cd%50000)//20000
bd=(Cd%20000)//10000
bcin=(Cd%10000)//5000
bdo=(Cd%5000)//2000
bm=(Cd%2000)//1000
#Monedas
mq=(Cd%1000)//500
md=(Cd%500)//200
mc=(Cd%200)//100
mci=(Cd%100)//50
#Salida
print(f"Billetes de cien mil:{bc}")
print(f"Billetes de cincuenta mil:{bci}")
print(f"Billetes de veinte mil:{bv}")
print(f"Billetes de diez mil:{bd}")
print(f"Billetes de cinco mil:{bcin}")
print(f"Billetes de dos mil:{bdo}")
print(f"Billetes de mil:{bm}")
print(f"Monedas de quinientos:{mq}")
print(f"Monedas de docientos:{md}")
print(f"Monedas de cien:{mc}")
print(f"Monedas de cincuenta:{mci}")