"""
https://www.youtube.com/watch?v=dPkoI6BQc0E

El manejo de excepciones es una forma de controlar errores en el programa.
gestionando situaciones imprevistas o errores durante la ejecucion del programa.
de tal manera que tenemos una forma elegante de anticipar, detectar y
manejar errores.

"""

try:
    # codigo que puede lanzar una excepcion
    numero = int(input("Ingrese un numero: "))
    resultado = 50 // numero
    print(f"El resultado es: {resultado}")
except ValueError as e:
    print("Error: El numero ingresado no es un numero", e)
except ZeroDivisionError as e:
    print("Error: No se puede dividir por cero")
except Exception as e:
    print("Error: Algo salio mal", e)

else:
    print("Todo bien")
finally:
    print("Finalizado")
# Podemos poner las veces que queramos except