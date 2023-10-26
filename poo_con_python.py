
#Privado

class Persona:
    def __init__(self,id,nombre,apellido,correo,contraseña):
        self._id=id
        self._nombre=nombre
        self._apellido=apellido
        self._correo=correo
        self._contraseña=contraseña
    
    @property
    def id(self):
        return self.id
    @id.setter
    def id(self,id):
        self._id=id
        
    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
        
    @property
    def apellido(self):
        return self.apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

    @property
    def correo(self):
        return self.correo
    @correo.setter
    def correo(self,correo):
        self.correo=correo
        
    @property
    def contraseña(self):
        return self.contraseña
    @contraseña.setter
    def constraseña(self,contraseña):
        self.contraseña=contraseña
        
def imprimir_persona(self):
        print(f'id:{self._id} nombre:{self.nombre} apellido:{self.apellido} correo:{self.correo} contraseña{self.contraseña}')
    
    
 #-----------------------------------------       
class Empleado:
    def __init__(self,cargo,salario):
        self._cargo=cargo
        self._salario

class Cliente:
    def __init__(self,telefono,direccion):
        self._telefono=telefono
        self._direccion=direccion
        





    

        

        
        