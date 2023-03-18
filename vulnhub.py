# Imports
import re
from colorama import Fore
import requests

# Colores
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
cyan = Fore.CYAN

# Enlace Web
web = 'https://www.vulnhub.com/'

# Salida
result = requests.get(web)
content = result.text

# Eliminar repetidas
patron = r"/entry/[\w-]*"
maquinasRepetidas = re.findall(patron, str(content))
sinDuplicados = list(set(maquinasRepetidas))

# Salida de maquinas finales
maquinaFinal = []
print(blue + "\n Estas son las máquinas más recientes: ")

for i in sinDuplicados:
    nombreMaquina = i.replace("/entry/", "")
    maquinaFinal.append(nombreMaquina)
    print(cyan + nombreMaquina)

# Check for maquinas nuevas
maquinaNoob = "noob-1"
existeNoob = False

for a in maquinaFinal:
    if a == maquinaNoob:
        existeNoob = True
        break

if existeNoob == True:
    print(green + "No hay máquinas nuevas")
else:
    print(yellow + "Se ha encontrado una máquina nueva")