"""
Marc Pérez Juncas
08/10/2024
"""
#Obtenir les dades
from datetime import datetime

day = datetime.today().day
month = datetime.today().month
year = datetime.today().year

dia=int(input("Dia?"))
if dia>31 or dia<1:
    print("Dia incorrecte")
    exit()

mes=int(input("Mes?"))
if mes>12 or mes<1:
    print("Mes incorrecte")
    exit()

any=int(input("Any?"))
if any > year:
    print("Any incorrecte")

if year-any >=16 and year-any <=65:
    print("Pots treballar")
else:
    print("No pots treballar")

dataNaixement =  dia,mes,any

print(dataNaixement)

print(day,month,year)

edatAny = year-any
edatMes = month-mes
edatDia = day-dia

edatTotal = edatDia, edatMes, edatAny

print("La teva edat es:", edatTotal)


#Procesar les dades

print("Programa Finalitzat")