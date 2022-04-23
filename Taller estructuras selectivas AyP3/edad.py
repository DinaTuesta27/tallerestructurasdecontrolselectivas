#Entrada
edaddias=int(input(""))
#Caja negra
años=edaddias/365
meses=(edaddias-365)/30
dias=(edaddias-365)-30
#Salida
print(f"El total de la edad en años es: {round(años,0)}. En meses: {round(meses,0)}. En dias:{round(dias,0)}")