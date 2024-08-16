"""

https://www.youtube.com/watch?v=r4zmpyPaEzw

La compañia multinacional rappi, solicita un sistema que determine
los dias de vacaciones a los que tiene derecho un trabajador. tomando
en cuenta las siguientes caraterísticas:

Existen 3 departamentos dentro de la compañia:
    1. Departamento de atencion al cliente (Clave 1)
    2. Departamento de logística (Clave 2)
    3. Gerencia (Clave 3)

Trabajadores con clave 1:
    1. con 1 año de servicio: reciben 6 dias de vacaciones
    2. con 2 a 6 años de servicio: reciben 14 dias de vacaciones
    3. con 7 o mas años de servicio: reciben 20 dias de vacaciones

Trabajadores con clave 2:
    1. con 1 año de servicio: reciben 7 dias de vacaciones
    2. con 2 a 6 años de servicio: reciben 15 dias de vacaciones
    3. con 7 o mas años de servicio: reciben 22 dias de vacaciones

Trabajadores con clave 3:
    1. con 1 año de servicio: reciben 10 dias de vacaciones
    2. con 2 a 6 años de servicio: reciben 20 dias de vacaciones
    3. con 7 o mas años de servicio: reciben 30 dias de vacaciones

Requisitos:
    1. El sistema debe solicitar nombre, clave del departamento y antiguedad del trabajador
        desde el teclado
    2. Posteriormente, el sistema debe mostrar un mensaje en pantalla que
        contenga el nombre y los dias de vacaciones que corresponde al trabajador

"""
INCORRECT_VALUE_MESSAGE = "Se ha introducido un valor incorrecto"

print("=================================")
print("Calculadora de dias de vacaciones")
print("=================================\n")

employee_name = input("Introduce el nombre del empleado: ")
departament_key = int(input("Introduce la clave del departamento: "))
experience_years = float(input("Introduce la antiguedad del empleado: "))

if departament_key == 1:
    if experience_years == 1:
        print(f"El empleado {employee_name} recibe 6 dias de vacaciones")
    elif experience_years >= 2 and experience_years <= 6:
        print(f"El empleado {employee_name} recibe 14 dias de vacaciones")
    elif experience_years >= 7:
        print(f"El empleado {employee_name} recibe 20 dias de vacaciones")
    else:
        print(INCORRECT_VALUE_MESSAGE)
elif departament_key == 2:
    if experience_years == 1:
        print(f"El empleado {employee_name} recibe 7 dias de vacaciones")
    elif experience_years >= 2 and experience_years <= 6:
        print(f"El empleado {employee_name} recibe 15 dias de vacaciones")
    elif experience_years >= 7:
        print(f"El empleado {employee_name} recibe 22 dias de vacaciones")
    else:
        print(INCORRECT_VALUE_MESSAGE)
elif departament_key == 3:
    if experience_years == 1:
        print(f"El empleado {employee_name} recibe 10 dias de vacaciones")
    elif experience_years >= 2 and experience_years <= 6:
        print(f"El empleado {employee_name} recibe 20 dias de vacaciones")
    elif experience_years >= 7:
        print(f"El empleado {employee_name} recibe 30 dias de vacaciones")
    else:
        print(INCORRECT_VALUE_MESSAGE)
else:
    print(INCORRECT_VALUE_MESSAGE)
