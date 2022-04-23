"""
Entradas:
*Temperatura en grados fahrenheit-->float-->t
Salidas:
*Deporte-->cadena (str)-->d

"""
#Entrada
t=float(input("Digite la temperatura: "))
#Caja negra
d=""
if(t>85 and t<=120):
    d="Natación"
elif(t>70 and t<=85): #Se usa para dar más condiciones en una mimsa variables
    d="Tenis"
elif(t>32 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esquí"
elif(t>=0 and t<=10):
    d="Marcha"
else: #No tiene condición
    print("La temperatura no pertenece a ningun deporte.")

#Salida
print(f"El deporte a prácticar es: {d}")