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
