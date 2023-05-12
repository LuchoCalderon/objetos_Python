class Animal:
    def __init__(self, nombre, color, clasificacion):
        self.nombre = nombre
        self.color = color
        self.__clasificacion = clasificacion
        
    def get_clasificacion(self):
        return self.__clasificacion
    
    def set_clasificacion(self, clasificacion):
        self.__clasificacion = clasificacion
    
    def accion(self):
        print(f'El {self.nombre} es de color {self.color} , {self.__clasificacion} y puede Volar')

class Perro(Animal):
    def __init__(self, nombre, color, clasificacion, raza):
        super().__init__(nombre, color, clasificacion)
        self.raza = raza
        
    def sonido(self):
        return "Guau"
    
animal = Animal('Loro', 'Verde', 'Vertebrado')
animal.accion()

perro = Perro('Tony', 'Cafe', 'Vertebrado', 'Labrador')
print('El perro es raza:' ,perro.raza)
print('clasificado:', perro.get_clasificacion())
print ('hace sonido:',perro.sonido())
    
    