"""
EJERCICIO 3

Creación
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos

Experimentación
Crea algunos productos
Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto
"""

from ast import main


class producto(): #Creamos la clase alumno
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo # Definimos que el atributo codigo, sera el codigo asignado
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.precio = precio # Definimos que el atributo precio, sera el precio asignado
        self.tipo = tipo # Definimos que el atributo nombre, sera el tipo asignado
        print ("El producto se ha creado con éxito")
    
    def __str__(self):
        producto = ("El producto es {}, cuesta {} euros, su tipo es {} y su codigo es {}") #Mensaje
        print(producto.format(self.nombre, self.precio, self.tipo, self.codigo)) #Usamos FORMAT

#Instancia
producto1 = producto("hfytd233", "cacao", "10", "chocolate")
producto2 = producto("das3", "manzana", "3", "fruta")
producto3 = producto("oitej3", "solomillo", "30", "carne")

#Llamamos al método
producto1.__str__()

producto2.__str__()

producto3.__str__()

producto3.precio = 25 #Modifico el precio del producto 3

producto3.__str__()

if __name__ == "__main__":
    main()