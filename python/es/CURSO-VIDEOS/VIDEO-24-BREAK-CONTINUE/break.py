"""
https://www.youtube.com/watch?v=Jh7xb5d8hvw

En python, los bucles o ciclos pueden ser interrumpidos
o simplemente dejar de ejecutarse. o parar la iteracion y ejecutar
otra iteracion.

Para ello, se utilizan las siguientes sentencias:
    - break
    - continue

break:
    Se utiliza para detener la ejecucion de un ciclo y detener la iteracion
    de la misma. Para que seguidamente ejecute el codigo fuera del ciclo.

continue:
    Se utiliza parar la iteracion del ciclo y continuar con la siguiente iteracion.
"""

# break

print("While con la sentencia break\n")
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        # Se detiene la ejecucion del bucle y sale del mismo
        break
    print("valor de counter: ", counter)

print("\n Fin del programa.")