"""
EJERCICIO 2

Creación
Copia el ejercicio anterior y realicemos una modificación:
Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:
def __str__(self): return "Lo que quiero mostrar"
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

Experimentación
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
"""

class alumno(): #Creamos la clase alumno
    def __init__(self, nombre, nota):
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada  
        print ("El alumno se ha creado con éxito")

    def __str__(self):
        print ("Hola soy {} y mi nota es un {}".format(self.nombre, self.nota)) #Mensaje

    def calificacion(self):
        if int(self.nota) < 5:
            print("{} ha suspendido".format(self.nombre))
        else :
            print("{} ha aprobado".format(self.nombre))
        return

#Instancia
alumno1 = alumno("Pedro", "4") 
alumno2 = alumno("Cristina", "10") 
alumno3 = alumno("Lucia", "10") 

#Llamamos al método
alumno1.__str__()
alumno1.calificacion()

alumno2.__str__()
alumno2.calificacion()

alumno3.__str__()
alumno3.calificacion()
    