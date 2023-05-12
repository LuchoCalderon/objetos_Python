class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def saludar(self):
        print('Hola, soy', self.nombre , '¡Mucho gusto!')
        return
    def presentarse(self):
        print('Mi nombre es', self.nombre, 'tengo',self.edad , 'años y soy',self.profesion)
        return

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, materia):
        super().__init__(nombre, edad, profesion)
        self.__materia = materia
    
    # Getter y Setter para el atributo privado __materia
    def get_materia(self):
        return self.__materia
    
    def set_materia(self, materia):
        self.__materia = materia
    
    def informacion(self):
        print( f' {self.nombre} ve la materia {self.__materia}') 
    
    #objetos persona
persona1 = Persona('Jose', 28, 'programador')
persona2 = Persona('Lorena', 31, 'psicologa')
    
    #metodo saludar persona
persona1.saludar()
persona2.saludar()
    
    #metodo presentarse persona
persona1.presentarse()
persona2.presentarse()

    # objeto Estudiante
estudiante1 = Estudiante('Camilo', 22, 'Estudiante', 'Programacion')

    # método presentarse de la clase Persona, que ha sido heredado por la clase Estudiante
estudiante1.presentarse()   

    # métodos propios de Estudiante
estudiante1.informacion()   



