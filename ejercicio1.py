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

alumno1 = alumno("Pedro", "4") #Instancia
alumno2 = alumno("Cristina", "10") 
alumno3 = alumno("Lucia", "10") 


#Llamamos al método
alumno1.constructor() 
alumno1.calificacion()

alumno2.constructor() 
alumno2.calificacion()

alumno3.constructor() 
alumno3.calificacion()
    