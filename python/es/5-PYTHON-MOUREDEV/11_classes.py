# Clases

# La clase nos sirve para crear objetos, es decir, guardar toda la logica relacionada con un objeto
# Las clases en python las escribimos con camelCase.

class MyEmptyPerson:
    pass

# pass sirve para que no se ejecute nada, o que esta vacion.


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    # __init__ es el metodo que se ejecuta al crear un objeto de la clase Person
    # De esta manera recibe parametros.
    # Este no es una funcion, es un constructor
    # Self se refiere a el mismo, a la instancia de la clase Person
    def __init__(self, name, lasT_name, alias="Sin alias"):
        self.name = name
        self.lasT_name = lasT_name
        self.full_name = f"{name} {lasT_name}"
        self.alias = alias

    # Para crear un metodo de esta clase, debemos siempre usar self
    def walk(self):
        print(f"{self.full_name} is walking")
        print(f"My alias is {self.alias}")


my_person = Person("Juan", "Perez")
print(my_person.name)
print(f"My name is {my_person.name}")
print(f"My last name is {my_person.lasT_name}")
my_person.walk()


my_person = Person("Juan", "Perez", "Juan Perez")
my_person.walk()

# Modificar una propiedad

my_person.full_name = "Juan Perez Fernandez"
my_person.walk()

# Herencia


class Student(Person):
    def im_a_student(self):
        print(f"{self.full_name} is a student")
        print(f"My alias is {self.alias}")

    def walk(self):
        print(f"{self.full_name} is walking and is a student")

    def walk_2(self):
        super().walk()


student_1 = Student("Diego", "Perez")
student_1.im_a_student()
student_1.walk()
student_1.walk_2()

# Podemos usar tambien la function super(), la cual nos permite acceder a los metodos de la superclase
# O mejor dicho la clase padre

# propiedades privadas


class Person_2:
    def __init__(self, name, lasT_name, alias="Sin alias"):
        self.__name = name
        self.__lasT_name = lasT_name
        self.__full_name = f"{name} {lasT_name}"
        self.__alias = alias

    def get_name(self):
        return self.__name

    def get_lasT_name(self):
        return self.__lasT_name

    def get_full_name(self):
        return self.__full_name

    def get_alias(self):
        return self.__alias


person_2 = Person_2("Juan", "Perez")
print(person_2.get_name())
print(person_2.get_lasT_name())
print(person_2.get_full_name())
print(person_2.get_alias())
print(person_2.__name)
