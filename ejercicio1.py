class alumno(): #Creamos la clase alumno
    def _init_(self, nombre, nota):
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada
        print 
    
    def constructor(self):
        alumno = ("Hola soy {} y mi nota es un {}") #Mensaje
        print(alumno.format(self.nombre, self.nota)) #Usamos FORMAT

primero = alumno("Pedro", "10") #Instancia
#Llamamos al método
primero.constructor() 