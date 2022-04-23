"""
Entradas:
*Edad del paciente en años-->float-->epa
*Edada del paciente en meses-->float-->epm
*Sexo del paciente-->str-->sp
*Nivel de hemoglobina del paciente(g)-->float-->nhp
Salida:
*Positivo para anemia.-->str-->diagnostico
*Negativo para anemia.-->str-->diagnostico
"""
#Entrada
epa=float(input("Ingrese la edad del paciente en años: "))
epm=float(input("Ingrese la edad del paciente en meses: "))
sp=str(input("Ingrese el sexo del paciente: "))
nhp=float(input("Ingrese nivel de hemoglobina del paciente: "))
#Caja negra
F="femenino"
M="masculino"

if(epm>0 and epm<=1):
    if(nhp>=13 and nhp<=26):
        print("Negativo para anemia.")
    else:
        print("Positivo para anemia.")
elif(epm>1 and epm<=6):
    if(nhp>=10 and nhp<=18):
        print("Negativo para anemia.")
    else:
        print("Positivo para anemia.")   
elif(epm>6 and epm<=12):
    if(nhp>=11 and nhp<=15):
        print("Negativo para anemia.")
    else:
        print("Positivo para anemia.")
elif(epa>1 and epa<=5):
    if(nhp>=11.5 and nhp<=15):
        print("Negativo para anemia.")
    else:
        print("Positivo para anemia. ")
elif(epa>5 and epa<=10):
    if(nhp>=12.6 and nhp<=15.5):
        print("Negativo para anemia. ")
    else:
        print("Positivo para anemia. ")
elif(epa>10 and epa<=15):
      if(nhp>=13 and nhp<=15.5):
        print("Negativo para anemia. ")
      else:
        print("Positivo para anemia. ")
elif(sp==F and epa>15):
      if(nhp>=13 and nhp<=16):
        print("Negativo para anemia. ")
      else:
        print("Positivo para anemia. ")
elif(sp==M and epa>15):
      if(nhp>=14 and nhp<=18):
        print("Negativo para anemia. ")
      else:
        print("Positivo para anemia. ")
