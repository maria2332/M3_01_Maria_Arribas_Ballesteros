class alumno(): #Creamos la clase alumno
    def __init__(self, nombre, nota):
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada
        print 
    
    def constructor(self):
        alumno = ("Hola soy {} y mi nota es un {}") #Mensaje
        print(alumno.format(self.nombre, self.nota)) #Usamos FORMAT

    def calificacion(self):
        if int(self.nota) < 5:
            print("Ha suspendido")
        else :
            print("Ha aprobado")
        return

primero = alumno("Pedro", "10") #Instancia
#Llamamos al método
primero.constructor() 
primero.calificacion()

    