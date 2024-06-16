# python3-libs-install

**Descripcion:**

﻿La biblioteca `actualiza_librerias` (`actualiza_librerias.py`) es un script **Python 3** que se encarga de actualizar la herramienta de gestión de paquetes `pip`, verificar y instalar las librerías faltantes en un proyecto. A continuación, te presento un breve resumen de su funcionalidad:

1. `**Actualización de pip**`: El script intenta actualizar pip utilizando el comando `pip install --upgrade pip`. Si falla, intentará utilizar la versión de Python para actualizar pip.
2. `**Identificación de dependencias**`(librerias): El script analiza los archivos `.py` en el directorio actual y extrae las importaciones realizadas en cada archivo.
3. `**Instalación de dependencias**`: El script intenta instalar las librerías faltantes utilizando `pip` o `pip3`, según sea necesario. Si falla, intentará utilizar la versión de Python para instalar la librería, segun el sistema operativo que se utilice.

La biblioteca `actualiza_librerias` proporciona cuatro funciones principales:

* `actualizar_ pip()`: **Actualiza pip si es necesario.**
* `identify_dependencies()`: **Identifica las dependencias de los archivos .py**
* `install_dependencies(dependencies)`: **Instala las librerías faltantes en el proyecto.**
* `main_lib()`: **Llama a las tres funciones anteriores.**

Para utilizar esta biblioteca, debes importarla en tu script Python 3 utilizando la sintaxis indicada en los comentarios del código. Luego, puedes llamar a la función `main_lib()` para actualizar `pip` y verificar e instalar las librerías faltantes.

**Funcionalidades**

* Actualiza pip a la versión más reciente.
* Instala automáticamente las librerías necesarias para ejecutar correctamente el proyecto, utilizando pip o pip3 según sea necesario.
* Muestra un informe detallado sobre los resultados de la verificación e instalación.

**Uso**

Para utilizar esta librería en tu proyecto Python, simplemente importa `actualiza_librerias` y llama a la función `main_lib()`. Esta función se encargará de actualizar pip, verificar e instalar las dependencias necesarias para ejecutar correctamente el proyecto.

Para utilizar esta librería en tu proyecto Python, sigue estos pasos:

1. Coloca la libreria `actualiza_librerias` en la carpeta de tu proyecto o sub-carpeta en tu proyecto.  
2. Importa la librería con las siguientes líneas de código:
  * `import actualiza_librerias as lib`
  * `import SUB_CARPETA.actualiza_librerias as lib`
3. Llama a la función que actualiza e instala las dependencias:
  * `lib.main_lib()`

De esta manera, nunca tendrás problemas con las librerías y podrás enfocarte en desarrollar tu proyecto sin preocupaciones sobre la gestión de las dependencias.

**La librería es compatible con `Windows`, `Linux` y `macOS`.**

La libreria utiliza segun corresponda:
  * `pip install`
  * `python.exe -m pip install`
  * `pip3 install`
  * `sudo pip3 install`

# Codigo por Pablo Otero. 15/06/2024 Python 3.11.3 

# Ejemplo:
`prueba.py`
```
import librerias.actualiza_librerias as lib
lib.main_lib()

import time
print("La hora actual es:", time.strftime("%H:%M:%S", time.localtime())) 

""" 
Aqui tu programa
"""
```
Importa y ejecuta la funcion.
`import librerias.actualiza_librerias as lib`
`lib.main_lib()`
Libreria de prueba con ejemplo de funcionalidad
`import time`
`print("La hora actual es:", time.strftime("%H:%M:%S", time.localtime()))`
Una vez probado, puedes borrar lo anterior (time, print), y colocar tu programa (`"""Aqui tu programa"""`)
