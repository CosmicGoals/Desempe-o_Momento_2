
from persona import Persona
class Empleado(Persona):
    def __init__(self,id,nombre,apellido,correo,contrasena,cargo,salario,tipo_contrato):
        super().__init__(id,nombre,apellido,correo,contrasena)
        self._cargo=cargo
        self._salario=salario
        self._tipo_contrato=tipo_contrato
        
        
        @property
        def cargo(self):
            return self._cargo
        @cargo.setter
        def cargo(self,cargo):
            self._cargo=cargo
        
        @property
        def salario(self):
            return self._salario
        @salario.setter
        def salario(self,salario):
            self._salario=salario
        
        @property
        def tipo_contrato(self):
            return self._tipo_contrato
        @tipo_contrato.setter
        def tipo_contrato(self,tipo_contrato):
            self._tipo_contrato=tipo_contrato
            
#Vamos a sobreescribir los metodos

        def registrar_usuario(self):
                _id=input(f'Ingrese ID del usuario:')
                _nombre=input(f'Ingrese nombre del usuario:') 
                _apellido=input(f'Ingrese apellido del usuario:') 
                _correo=input(f'Ingrese correo del usuario:')
                _contrasena=input(f'Ingrese contrasena del usuario:')
                _cargo=input(f'Ingrese cargo del usuario:')
                _salario=int(input(f'Ingrese salario del usuario:'))
                _tipo_contrato=input(f'Ingrese tipo de contrato del usuario:')
        
        def imprimir_registro(self):
                print(print(f'id:{self._id} nombre:{self._nombre} apellido:{self._apellido} correo:{self._correo} contrasena{self._contraseña} cargo:{self._cargo} salario:{self._salario} tipo de contrato{self._tipo_contrato}'))
        
#Otra forma de imprimir más practica

        def imprimir_registro(self):
            super().imprimir_registro()
            print(f'cargo:{self._cargo} salario:{self._salario} tipo de contrato{self._tipo_contrato}')
        
        def iniciar_sesion(self):
            correo_emp=input('Ingrese el correo resgistrado: ')
            contras_emp=input('Ingrese la contraseña: ')
            if correo_emp==self._correo and contras_emp==self._contraseña:
                return True
            else:
                return False
    