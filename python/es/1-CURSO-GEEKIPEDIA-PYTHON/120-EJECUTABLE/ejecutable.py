"""
https://www.youtube.com/watch?v=wGgJ1CqZLD0

Un ejecutable es un archivo que se ejecuta directamente, de tal manera que encapsula
un script de python y las dependencias necesarias para ejecutarlo. Esto permite que el
el usuario no tenga que instalar todas las dependencias en su computadora, sino que
pueda ejecutar el script directamente desde su computadora.

una de las herramientas mas comunes es PyInstaller, que permite crear ejecutables de python.

Cuando utilizas esto, incluye el interprete, el script y todas las dependencias en un solo archivo.

windows:
    - Escribimos cmd al apretar la tecla windows + r
        - Comprobamos con pip --version si tenemos instalado pip
    - Instalamos pyinstaller con pip install pyinstaller
    - En el directorio donde esta el script, escribimos pyinstaller --onefile (nombre del script).py
    pyinstaller --onefile solucion.py
"""