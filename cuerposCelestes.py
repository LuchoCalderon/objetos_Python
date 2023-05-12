class CuerposCelestes:
    def __init__(self, nombre, masa):
        self.nombre = nombre
        self.__masa = masa

    def get_masa(self):
        return self.__masa

    def set_masa(self, masa):
        self.__masa = masa

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}')
        print(f'Masa: {self.__masa}')

class Planetas(CuerposCelestes):
    def __init__(self, nombre, masa, distancia_sol):
        super().__init__(nombre, masa)
        self.distancia_sol = distancia_sol

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Distancia al Sol: {self.distancia_sol}')

cuerpo_celeste1 = CuerposCelestes('Sol', 1.989e30)
cuerpo_celeste1.mostrar_info()

planeta1 = Planetas('Tierra', 5.972e24, 149.6e6)
planeta1.mostrar_info()