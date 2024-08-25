'''
https://youtu.be/6yBL1mcd7iY?si=grAq0VnZC3UGiuWR

Las palabras reservadas, son identificadores para uso exclusivo del lenguaje de programacion
que no pueden ser utilizadas para identificar y nombrar variables, metodos, objetos
o cualquier elemento de nuestro codigo

al intentar usar alguna de estas palabras fuera de su uso comun, nos saltara un error

Existe un total de 28 palabras en python para uso exclusivo del lenguaje

son:

-and
-del
-for
-is
-raise
-assert
-if
-else
-elif
-from
-lambda
-return
-break
-global
-not
-try
-class
-except
-or
-while
-continue
-exec
-import
-yield
-def
-finally
-in
-print


'''

# Un ejemplo de este error seria lo siguiente

print = 5 # Sin embargo, si se cambia almenos una letra, estaria correcto
Print = 6
resultado = print = Print
print(resultado)

# Esto salta el error TypeError: 'int' object is not callable

