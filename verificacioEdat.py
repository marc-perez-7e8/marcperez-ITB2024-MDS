"""
Marc Pérez Juncas
08/10/2024
"""
#Obtenir les dades
from datetime import datetime

dia=int(input("Dia?"))
if dia>31 or dia<1:
    print("Dia incorrecte")
    exit()

mes=int(input("Mes?"))
if mes>12 or mes<1:
    print("Mes incorrecte")
    exit()
any=int(input("Any?"))
if any > datetime.now().year:
    print("Any incorrecte")
    exit()

dataNaixement =  dia,mes,any

print(dataNaixement)

print(datetime.now())
#edatDia = datetime.now().day - dia
#edatMes = datetime.now().month - mes
#edatAny = datetime.now().year - any

edatTotal = edatDia, edatMes, edatAny
print("Tens",edatTotal)


#Procesar les dades

print("Programa Finalitzat")