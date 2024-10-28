import xml.etree.ElementTree as ET
import json
from logging import exception

# Parse the XML file
try:
    tree = ET.parse("Incidencias.xml")
    root = tree.getroot()

    # Contadores
    incidenciesTotals = 0
    invalid = 0
    adrecesCounter = {}
    claseCounter = {}
    tipusCounter = {}
    urgenciaCounter = {}

    for child in root:
        incidenciesTotals += 1
        data = child.find('DATA_DE_LA_INCIDÈNCIA').text
        correu = child.find('Adreça_electrònica').text
        clase = child.find('AULA_SALAConsulteu_cartell_d_entrada_a_l_aula_o_l_espai_').text
        tipusIncidencia = child.find('TIPUS_INCIDÈNCIA').text
        urgencia = child.find('NIVELL_URGÈNCIA_DE_SOLUCIÓ').text

        dataFiltro = data.replace("/", " ")
        print(data)

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
        if añoInt != 2024:
            valid = False

        if valid:
            print('Incidencia válida')
        else:
            print('Incidencia inválida')
            invalid += 1

        # Conta les Adreces
        if correu:
            if correu in adrecesCounter:
                adrecesCounter[correu] += 1
            else:
                adrecesCounter[correu] = 1

        # Conta les classes
        if clase:
            if clase in claseCounter:
                claseCounter[clase] += 1
            else:
                claseCounter[clase] = 1

        # Conta els diferents tipus d'incidencia
        if tipusIncidencia:
            if tipusIncidencia in tipusCounter:
                tipusCounter[tipusIncidencia] += 1
            else:
                tipusCounter[tipusIncidencia] = 1

        # Conta l'urgencia
        if urgencia:
            if urgencia in urgenciaCounter:
                urgenciaCounter[urgencia] += 1
            else:
                urgenciaCounter[urgencia] = 1

    # Càlcul de porcentaje de incidències inválides
    if incidenciesTotals > 0:
        porcentaje_invalid = (invalid / incidenciesTotals) * 100
        print("N'hi han", incidenciesTotals, "incidencies, de les quals", invalid, "son invalides. El percentantge d'incidencies invalides és:", round(porcentaje_invalid, 2), "%)")

    # Trobar el correu més utilitzat
    correuMesUtilitzat = max(adrecesCounter, key=adrecesCounter.get, default=None)
    print("L'Adreça electrònica més utilitzada és:", correuMesUtilitzat, "(usos:", adrecesCounter[correuMesUtilitzat], ")")

    # Trobar la clase més utilitzada
    claseMesUtilitada = max(claseCounter, key=claseCounter.get, default=None)
    print("La clase més utilitzada és:", claseMesUtilitada, "(usos:", claseCounter[claseMesUtilitada], ")")

    # Trobar el tipus d'incidencia més utilitzat
    tipusIncidenciaMesUtilitzat = max(tipusCounter, key=tipusCounter.get, default=None)
    print("El tipus d'incidencia més comú és:", tipusIncidenciaMesUtilitzat, "(usos:", tipusCounter[tipusIncidenciaMesUtilitzat], ")")

    # Trobar l'urgencia més comú
    urgenciaMesComu = max(urgenciaCounter, key=urgenciaCounter.get, default=None)
    print("L'urgencia més comú és:", urgenciaMesComu, "(usos:", urgenciaCounter[urgenciaMesComu], ")")

    # Formateja per JSON
    export_data = {
        "totals": {
            "incidenciesTotals": incidenciesTotals,
            "invalid": invalid,
            "porcentaje_invalid": round((invalid / incidenciesTotals) * 100, 2) if incidenciesTotals > 0 else 0
        },
        "most_common": {
            "correu": max(adrecesCounter, key=adrecesCounter.get, default=None),
            "clase": max(claseCounter, key=claseCounter.get, default=None),
            "tipusIncidencia": max(tipusCounter, key=tipusCounter.get, default=None),
            "urgencia": max(urgenciaCounter, key=urgenciaCounter.get, default=None)
        }
    }

    # Exporta a JSON
    with open("incidencias_report.json", "w") as json_file:
        json.dump(export_data, json_file, indent=4)

    print("Report exported to 'incidencias_report.json'")

except FileNotFoundError:
    print("No s'ha trobat l'arixu")
except ET.ParseError:
    print("L'arxiu está buit")
