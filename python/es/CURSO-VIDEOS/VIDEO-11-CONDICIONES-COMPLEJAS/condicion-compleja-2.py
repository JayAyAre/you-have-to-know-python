print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, cual es su nombre? ")

nota_matematicas = float(input("Ingrese la calificacion en matematicas: "))
nota_quimica = float(input("Ingrese la calificacion en quimica: "))
nota_programacion = float(input("Ingrese la calificacion en programacion: "))

nota_total = nota_matematicas + nota_quimica + nota_programacion
promedio = nota_total / 3

"""

Para imprimir el promedio con unicamente 2 decimales:

    1 - round(nota_total / 3, 2)
    2 - print(f"el promedio es: {promedio:.2f}"))

"""

print(f"El promedio es: {promedio:.2f}")

if promedio >= 5.0:
    # print("Felicidades " + nombre + "!!!, aprobaste con nota promedio de", promedio)
    print('Felicidades ' + nombre + ' "aprobaste" con una nota promedio de ' + str(round(promedio, 2)))
else:
    print("Lo siento, no aprobaste, su nota promedio es", promedio)

print("Fin.")