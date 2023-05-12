class Cuerposcelestes:
    def __init__(self,nombre,color,masa, ):         
        self.nombre = nombre 
        self.color = color
        self.__masa = masa
    
    def get_masa(self):
            return self.__masa
    
    def set_masa(self, masa):
        self.__masa = masa
    
    def informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Color: {self.color}')
        print(f'Masa: {self.__masa}')

class Planetas(Cuerposcelestes):
    def __init__(self,nombre,color,masa,cantidad_lunas):
       super().__init__(nombre,color,masa) 
       self.cantidad_lunas = cantidad_lunas
    
    def informacion(self):
        super().informacion()
        print(f'El planeta {self.nombre} tiene la cantidad de lunas: {self.cantidad_lunas}')

cuerpo_celeste = Cuerposcelestes('luna', 'gris', 9.98e30)
cuerpo_celeste.informacion()

planeta = Planetas('jupiter', 'marron y blanco', 1.898e27, 79)
planeta.informacion()
          
       
       

    