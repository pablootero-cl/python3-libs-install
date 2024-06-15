# python3-libs-install

**Descripcion:**

La librería `actualiza_librerias` es una herramienta diseñada para automatizar el proceso de actualización y verificación de dependencias en proyectos Python. Esta librería se enfoca en actualizar pip, verificar e instalar las librerías faltantes y mostrar un informe detallado sobre los resultados.

**Funcionalidades**

* Actualiza pip a la versión más reciente.
* Verifica si existen librerías instaladas que no están siendo utilizadas por el proyecto actual.
* Instala automáticamente las librerías necesarias para ejecutar correctamente el proyecto, utilizando pip o pip3 según sea necesario.
* Muestra un informe detallado sobre los resultados de la verificación e instalación.

**Uso**

Para utilizar esta librería en tu proyecto Python, simplemente importa `actualiza_librerias` y llama a la función `main_lib()`. Esta función se encargará de actualizar pip, verificar e instalar las dependencias necesarias para ejecutar correctamente el proyecto.

Para utilizar esta librería en tu proyecto Python, sigue estos pasos:

1. Coloca la libreria `actualiza_librerias` en la carpeta de tu proyecto.
2. Importa la librería con las siguientes líneas de código:

import actualiza_librerias as lib

3. Llama a la función que actualiza e instala las dependencias:

lib.main_lib()


De esta manera, nunca tendrás problemas con las librerías y podrás enfocarte en desarrollar tu proyecto sin preocupaciones sobre la gestión de dependencias.

La librería es compatible con Windows, Linux y macOS.

"""
# Nota: Si, [actualiza_librerias.py] esta en la misma carpeta que tu programa usa el siguiente script para llamar a la libreria: 
* import actualiza_librerias as lib

# Si, [actualiza_librerias.py] esta en una SUB_CARPETA usa: 
* import SUB_CARPETA.actualiza_librerias as lib

# Luego llama a la funcion para actualizar PIP y verificar e instlar las librerias faltantes:
* lib.main_lib()

Nota: Estos 2 codigo a usar, se colocan en tu script. Sin el *
"""
# Codigo por Pablo Otero. 15/06/2024 Python 3.11.3 
