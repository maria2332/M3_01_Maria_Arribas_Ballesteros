"""
EJERCICIO 1

Creación
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota

Experimentación
Crea algunos alumnos
Prueba a ejecutar el método calificacion de cada objeto que has creado
"""

class alumno(): #Creamos la clase alumno
    def __init__(self, nombre, nota):
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada 
        print ("El alumno se ha creado con éxito")
        
    def calificacion(self):
        if int(self.nota) < 5:
            print("Ha suspendido")
        else :
            print("Ha aprobado")
        return

#Instancia
alumno1 = alumno("Pedro", "4") 
alumno2 = alumno("Cristina", "10") 
alumno3 = alumno("Lucia", "10") 

#Llamamos al método
alumno1.calificacion()

alumno2.calificacion()

alumno3.calificacion()
    