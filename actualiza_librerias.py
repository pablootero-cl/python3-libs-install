# Codigo por Pablo Otero. 16/06/2024 Python 3.11.9 
"""
# Nota: Si, [actualiza_librerias.py] esta en la misma carpeta que tu programa usa el siguiente script para llamar a la libreria: 
* import actualiza_librerias as lib

# Si, [actualiza_librerias.py] esta en una SUB_CARPETA usa: 
* import SUB_CARPETA.actualiza_librerias as lib

# Luego llama a la funcion para actualizar PIP y verificar e instlar las librerias faltantes:
* lib.main_lib()

Nota: Estos 2 codigo a usar, se colocan en tu script. Sin el *
"""

import subprocess # Utilizado para actualizar pip e instalar dependencias.
import sys        # Utilizado para obtener la lista de módulos cargados (en el bucle `for`)
import os         # Utilizado para limpiar la consola después de actualizar pip y mostrar mensajes de error.
import re          # Importar la biblioteca regular expressions (expresiones regulares)
from os import system, name # Utilizados para interactuar con la consola y mostrar mensajes de error.
import time

def actualizar_pip():
    if os.name == 'nt':  # Windows
        try:
            system("pip install --upgrade pip")
        except Exception as e:
            print(f"Error al actualizar pip con pip: {e}")
            try:
                system("python.exe -m pip install --upgrade pip")  # Intenta utilizar python.exe -m pip
            except Exception as e:
                print(f"Error al actualizar pip con python.exe -m pip: {e}")
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'): # Linux/MacOS
        try:
            subprocess.run(["pip3", "--upgrade", "pip"])
        except Exception as e:
            print(f"Error al actualizar pip sin sudo: {e}")
            try:
                subprocess.run(["sudo", "pip3", "--upgrade", "pip"])  # Intenta utilizar sudo
            except Exception as e:
                print(f"Error al actualizar pip con sudo: {e}")

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def identify_dependencies():
    """
    Identificar los archivos .py en el directorio actual y analizar su contenido.
    """
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]  # Buscar archivos Python
    dependencies = []
    for file in py_files:
        with open(file, 'r') as fd:  # Abrir archivo en modo lectura
            content = fd.read()      # Leer contenido del archivo
            imports = set(re.findall(r'import\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content))  # Encontrar importaciones
            from_imports = set(re.findall(r'from\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s+import', content))  # Encontrar imports "from"

        dependencies.extend(imports)  # Agregar importaciones a la lista de dependencias
        dependencies.extend(from_imports)

    return list(set(dependencies))  # Eliminar duplicados y devolver la lista

def install_dependencies(dependencies):
    """
    Intenta instalar los paquetes utilizando pip o pip3.
    Si falla, intentará utilizar el otro método.
    """
    if os.name == 'nt':  # Windows
        for dependency in dependencies:
            try:
                subprocess.run(['pip', '-q', 'install', dependency])  # Instalar con pip (Windows)                
                print(f"{dependency} instalado correctamente.")
                time.sleep(.7)
                clear()
            except Exception as e:
                print(f"Error installing {dependency}: {e}")
                subprocess.run(['python.exe', '-m', 'pip', '-q', 'install', dependency])
                print(f"{dependency} instalado correctamente.")
                time.sleep(.7)
                clear()
    else:  # Linux/MacOS
        for dependency in dependencies:
            try:
                subprocess.run(['pip3', '-q', 'install', dependency])  # Instalar con pip3 (Linux/MacOS)
                print(f"{dependency} instalado correctamente.")
                time.sleep(.7)
                clear()
            except Exception as e:
                print(f"Error installing {dependency}: {e}")
                subprocess.run(['sudo', 'pip3', '-q', 'install', dependency])
                print(f"{dependency} instalado correctamente.")
                time.sleep(.7)
                clear()

def main_lib():
    
    actualizar_pip()  # Actualiza pip si es necesario
    # Installa dependencias
    dependencies = identify_dependencies()
    if dependencies: 
        install_dependencies(dependencies)


if __name__ == "__main__":
    main_lib()
