"""
Entrada:
Valores-->int-->P y Q
Salida:
resultado-->int-->res
Valores-->int-->P y Q

"""
#Entrada
P=int(input("Ingrese un valor: "))
Q=int(input("Ingrese un segundo valor: "))
#Caja negra
res=P**3+Q**4-2*P**2
if(res>680):
    print(f"P y Q satisfacen la expresión:{P} y {Q}")
elif(res<680):
    print(f"P y Q no satisfacen la expresión:{P} y {Q}")