'Parametros modificables'
nombreArchivo = 'PRO-99-99-99-VV.xml'
layerHeights=[0.10]
linesWith = [0.4]
temperatures=[205,210,215,220]
speeds=[3000,5000,3500]
vArchivo = 0

'importar modulos para manejar fechas y fechas'
from datetime import datetime
import xml.etree.ElementTree as ET


'identificar en el xml los parametros que vamos a cambiar'

'analiza gramaticalmente todo el archivo'
tree = ET.parse(nombreArchivo)
'almacena los atributos de la raiz del perfil'
rootAttrib = tree.getroot().attrib
'layerHeigth info'
layerheightXml = tree.find('layerHeight')
'extruder-wdth'
extrudersXml = tree.findall('extruder')
widthXml = extrudersXml[0].find('width'),extrudersXml[1].find('width')
'Speed info'
speedXml = tree.find('defaultSpeed')
'temperatureController--setpoint'
temperaturesXml= tree.findall('temperatureController')
setpoint1 = temperaturesXml[1][3].attrib
setpoint2 = temperaturesXml[2][3].attrib
'based profile info'
tree.find('baseProfile').text = nombreArchivo

'''Modifica el archivo con los parametros asignados al principio y
hace todas las combinaciones posibles,genera para cada combinacion un archivo 
con su numero de version '''
for layer in layerHeights: 
    layerheightXml.text = str(layer)
    for line in linesWith: 
        widthXml[0].text = str(line)
        widthXml[1].text = str(line)
        for speed in speeds:
            speedXml.text = str(speed)
            for temperature in temperatures:
                newTemp = {'temperature':str(temperature)} 
                setpoint1.update(newTemp)
                setpoint2.update(newTemp)
                'genera una nueva version de archivo y crea el archivo nuevo'
                vArchivo +=1
                nombre= str(nombreArchivo[0:13]+ str(vArchivo) +'.xml')
                rootAttrib.update({'name':nombre})
                rootAttrib.update({'version':str(datetime.now())})
               
                tree.write(nombre)
#    
#   
