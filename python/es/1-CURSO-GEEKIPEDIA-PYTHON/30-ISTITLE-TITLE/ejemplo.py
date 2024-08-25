name = input("Introduce un nombre: ")
last_name = input("Introduce apellido: ")
full_name = f"{name} {last_name}"
print(f"El metodo title se ha aplicado?: {full_name.istitle()}")
print("Aplicando el metodo title...\n")
print(f"El metodo title se ha aplicado correctamente: {full_name.title()}") 