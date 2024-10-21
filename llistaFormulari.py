import xml.etree.ElementTree as ET
tree = ET.parse('/home/marc.perez.7e8/Incidencias.xml')
root = tree.getroot()

for child in root:
    for child in child:
        print(child.tag, child.attrib, child.text)