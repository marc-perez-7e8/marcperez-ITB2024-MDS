"""
Marc Pérez Juncas
14/10/24
"""
import datetime
try:
    mes = int(input("Introdueix el mes: "))
    any = int(input("introdueix el any: "))

    if mes >=1 and mes <=12:
        if mes in (12,10,8,7,5,3,1):
            print("31")
        elif mes in (11,9,6,4):
            print("30")
        else:
            if (any % 4 == 0) and (any % 100 != 0):
                print("29")
            else:
                print("28")
    else:
        print("Mes invalid")
except ValueError:
    print("Introdueix el mes numeric")

