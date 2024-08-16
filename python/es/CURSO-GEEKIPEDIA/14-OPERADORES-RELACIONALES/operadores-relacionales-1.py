"""

https://www.youtube.com/watch?v=4vKrYztae2I

Son simbolos que nos permiten comparar valores y tomar decisiones en función de ellos.
Si el resultado es verdadero, entonces se ejecutará el bloque de código que está dentro de la
condición. Si el resultado es falso, entonces se ejecutará el bloque de código que está dentro
de la condición inversa.

Operadores lógicos
    ( < ) => menor que => 5 < 4 => False
    ( > ) => mayor que => 5 > 4 => True
    ( <= ) => menor o igual que => 5 <= 4 => False
    ( >= ) => mayor o igual que => 5 >= 4 => True
    ( == ) => igual a => 5 == 4 => False
    ( != ) => no igual a => 5 != 4 => True

"""

print("Introduce dos numeros a comparar:\n")

input_first_number = int(input("introduce el primer numero: "))
input_second_number = int(input("introduce el segundo numero: "))

print(f"Los numeros a comparar son: {input_first_number} y {input_second_number} \n")

if input_first_number == input_second_number:
    print("Los numeros son iguales")
    if input_first_number >= input_second_number:
        print("Es mayor o igual que")
    else:
        print("Es menor o igual que")
else:
    print("Los numeros son diferentes")
    if input_first_number > input_second_number:
        print("Es mayor que")
    else:
        print("Es menor que")



