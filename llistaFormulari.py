import xml.etree.ElementTree as ET

tree = ET.parse("C:\\Users\\Usuario\\Desktop\\Incidencias.xml")
root = tree.getroot()

# Contadores
incidenciesTotals = 0
invalid = 0

for child in root:
    incidenciesTotals += 1
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
    valid = True
    if not (1 <= diaInt <= 31):
        valid = False
    if mesInt == 2:
        if (añoInt % 4 == 0) and (añoInt % 100 != 0):
            if diaInt > 29:
                valid = False
        else:
            if diaInt > 28:
                valid = False
    elif not (1 <= mesInt <= 12):
        valid = False
    if añoInt < 2024:
        valid = False

    if valid:
        print('Incidencia válida')
    else:
        print('Incidencia inválida')
        invalid += 1

# Cálculo de porcentaje de incidencias inválidas
if incidenciesTotals > 0:
    porcentaje_invalid = (invalid / incidenciesTotals) * 100
    print(f"N'hi han {incidenciesTotals} incidencies, de les quals {invalid} son invalides ({porcentaje_invalid:.2f}%).")