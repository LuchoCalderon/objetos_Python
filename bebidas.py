class Bebidas:
    def __init__(self,nombre,marca,color):
        self.nombre = nombre    
        self.marca = marca
        self.color = color
        return

    def hidratar(self):
        print(f"soy una bebida para hidratar, {self.nombre},de la marca: {self.marca} , de color: {self.color}")
        return
    
    def refrescar(self):
        print('soy una bebida para refrescar', self.nombre,'de la marca', self.marca , 'de color' , self.color)
        return

#objetos bebidas

bebida1 = Bebidas('gaterorade', 'coca-cola', 'rojo')
bebida2 = Bebidas('agua', 'brisa', 'transparente')

#metodo hidratar

bebida1.hidratar()

#metodo refrescar

bebida2.refrescar()

# Herencia

class Tipo(Bebidas):
    def __init__(self, nombre, marca, color, tipo):
        super().__init__(nombre, marca, color)
        self.__tipo = tipo
        
    def get_tipo(self):
            return self.__tipo
    
    def set_tipo(self, tipo):
        self.__tipo = tipo
        
    def consecuencia(self):
        if self.__tipo == 'azucarada':
            print('esta bebida' ,self.nombre, 'es', self.__tipo,'mala para la salud')
        else:
            print(f"esta bebida {self.nombre} es {self.__tipo} Buena para la salud")
    
#objeto  tipo

tipo1 = Tipo('vive100', 'quala', 'amarillo', 'azucarada')
tipo2 = Tipo('h2oh', 'postobon', 'blanco', 'no azucarada')

#metodo refrescar de clase bebida
tipo1.refrescar()

#metodo hidratar
tipo2.hidratar()

#metodos de tipos de bebida
tipo1.consecuencia()
tipo2.consecuencia()
