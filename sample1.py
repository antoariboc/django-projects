class Persona:
    # atributos
    nombre="Josune"
    edad = 24

    def __init__(self, salario, nombre, edad):
        self.salario = salario
        self.nombre = nombre
        self.edad = edad
p1 = Persona(3000,'John',40)
print(f' {p1.nombre} {p1.salario} {p1.edad} ')