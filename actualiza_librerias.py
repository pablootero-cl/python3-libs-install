# Codigo por Pablo Otero. 15/06/2024 Python 3.11.3 
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
from os import system # Utilizados para interactuar con la consola y mostrar mensajes de error.

def actualizar_pip():
    print("Actualizando pip...")
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(["pip", "install", "--upgrade", "-q", "pip"]) # Actualiza pip
        else:  # Linux/macOS
            try:
                subprocess.run(["pip3", "install", "--upgrade", "-q", "pip"])  # Intenta actualizar con pip3
            except Exception as e:
                print(f"Error al actualizar pip con pip3: {e}")
                subprocess.run(["sudo", "pip3", "install", "--upgrade", "-q", "pip"])  # Actualiza con sudo y pip3 si no funciona

        if os.name == 'nt':  # Windows
            system("cls")
        else:
            system("clear")  # Linux/macOS
        print("Pip actualizado.")
    except Exception as e:
        print(f"Error al actualizar pip: {e}")


def verificar_y_instalar_dependencias(dependencies):
    need_install = False
    for dependency in dependencies:
        try:
            __import__(dependency)  # Intenta importar la dependencia
        except ImportError:
            print(f"La librería {dependency} no está instalada. Instalando...")
            if os.name == 'nt':  # Windows
                subprocess.run(["pip", "install", dependency])  # Instala la dependencia
            elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):  # Linux/macOS
                try:
                    subprocess.run(["pip3", "install", dependency])  # Intenta instalar con pip3
                except Exception as e:
                    print(f"Error al instalar {dependency} con pip3: {e}")
                    subprocess.run(["sudo", "pip3", "install", dependency])  # Instala la dependencia con sudo si no funciona

    if not need_install:
        print("Librerías cargadas.")

def main_lib():
    actualizar_pip() # Actualiza PIP
    # Verifica e instala librerias
    dependencies = [] # Se utiliza para almacenar los nombres de las dependencias.
    for name, module in sys.modules.items(): # Nombre del módulo y el objeto que representa el módulo.
        if not name.startswith('__'): # Se utiliza para filtrar los módulos
            dependencies.append(module.__name__) # Agrega el nombre del módulo a la lista de dependencias. El método `__name__` devuelve el nombre del módulo como una cadena.

    verificar_y_instalar_dependencias(dependencies)

if __name__ == "__main__":
    main_lib()
