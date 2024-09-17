# Excepciones

# Try: ira el codigo dentro de la excepcion, si no se ejecuta bien, se lanzara una excepcion

# Except: si no se ejecuta bien, se lanzara una excepcion, se ejecutara el codigo dentro de la excepcion

# Else: Si no hay excepciones, se ejecutara el codigo

# Finally: Se ejecutara siempre al finalizar la ejecucion del codigo

try:
    # Se ejecuta y comprobraremos si hay una excepcion o no
    print(5 + "5")
except:
    # Se ejecuta si hay una excepcion
    print("Error")
else:  # optional
    # Se ejecuta si no hay excepciones
    print("No error")
finally:  # optional
    # Se ejecuta siempre al finalizar la ejecucion del codigo, si hay o no excepciones
    print("Final")

# Especificar excepciones

try:
    print(5 + "5")
except TypeError:
    print("Error")
except ValueError:
    print("Error")
else:
    print("No error")
finally:
    print("Final")

# Especificar excepciones agrupadas

try:
    print(5 + "5")
except (TypeError, ValueError):
    print("Error")

# Capturar informacion de la excepcion

try:
    print(5 + "5")
except TypeError as error:
    print(error)
except Exception as error:
    print(error)
