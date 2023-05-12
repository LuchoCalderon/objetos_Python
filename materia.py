class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.__creditos = creditos
    
    def get_creditos(self):
        return self.__creditos
    
    def set_creditos(self, creditos):
        self.__creditos = creditos
    
    def descripcion(self):
        print(f'materia {self.nombre} de {self.get_creditos()} creditos')
        
class Escuela(Materia):
    def __init__(self, nombre, creditos, escuela):
        super().__init__(nombre, creditos)
        self.escuela = escuela
    
    def descripcion(self):
        return (self.escuela)

materia = Materia('matematicas', 4)
materia.descripcion()

escuela = Escuela('matematicas', 4, 'ingenieria')
print('la materia ',escuela.nombre,'de la escuela:',escuela.descripcion())
        
