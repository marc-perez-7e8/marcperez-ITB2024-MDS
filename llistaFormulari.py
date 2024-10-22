import xml.etree.ElementTree as ET
from os.path import isdir

tree = ET.parse('/home/marc.perez.7e8/Incidencias.xml')
root = tree.getroot()
incidenciesTotals = 0


for child in root:
    incidenciesTotals = incidenciesTotals + 1
    data = child.find('DATA_DE_LA_INCIDÈNCIA').text
    dataFiltro = data.replace("/", " ")
    print(dataFiltro)

    # Separar el dia, mes i any
    dia = data[:2]  # Asumiendo que el día tiene 2 caracteres
    diaInt = int(dia)
    mes = data[3:5]  # Asumiendo que el mes tiene 2 caracteres
    mesInt = int(mes)
    año = data[6:]  # El resto es el año
    añoInt = int(año)

    # Comprovació de dades

    if diaInt >= 1 and diaInt <= 31:
        print('Dia valid')
    else:
        print('Dia invalid')
    if mesInt >= 1 and mesInt <= 12:
        print('Mes valid')
    else:
        print('Mes invalid')
    if añoInt >= 2024:
        print('Any valid')
    else:
        print('Any invalid')

    # Imprimir los valores separados
    print(f"Día: {dia}, Mes: {mes}, Año: {año}")

print("N'hi han", incidenciesTotals, "incidencies.")
