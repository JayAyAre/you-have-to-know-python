"""
https://www.youtube.com/watch?v=Kadly5Rr7xU

La funcion print es muy utilizada en python, ya que sirve para imprimir en consola, pero también puede imprimir en un archivo, en el caso de que se use la funcion open(). Para imprimir en un archivo se debe abrirlo con el comando open(), y luego utilizar la funcion write(). Para cerrar el archivo se utiliza el comando close().
y permitir la interactividad con el usuario.

Por este motivo, podemos manipular la forma en la que imprimimos con pantalla, y por ello
utilizamos los parametros que nos permite la funcion print().

paramentros:
    - end: termina la linea (Permite añadir cualquier caracteres al final de la linea)
        Por defecto es \n, un saldo de linea
    - sep: separa los elementos con un caracter (Permite separar los elementos)
        Por defecto es espacio
"""

print("Esto es un print normal")
print("Aqui se salto una linea")

print("Aqui se imprime con end igual a \"\"", end="///")
print("No se hizo un salto de linea") 