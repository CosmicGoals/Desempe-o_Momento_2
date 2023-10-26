class Persona:
    def __init__(self,id,nombre,apellido,correo,contrasena):
        self._id=id
        self._nombre=nombre
        self._apellido=apellido
        self._correo=correo
        self._contrasena=contrasena
        
#En este caso ya va ser encapsulado utilizando getter and setter
    
    @property #Es decir que es un Get
    def id(self):
        return self._id
    
    #Ahora vienen los Set
    @id.setter
    def id(self,id):
        self._id=id
        
    # Y continuamos haciendo lo mismo con todos los atributos a esta altura
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido
    
    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self,correo):
        self._correo=correo
    
    @property
    def contrasena(self):
        return self._contrasena
    @contrasena.setter
    def contrasena(self,contrasena):
        self._contrasena=contrasena
    
        
        
#Vamos a generar los metodos, para registrar los usuarios e imprimir el registro

    def registrar_usuario(self):
        _id=input(f'Ingrese ID del usuario:')
        _nombre=input(f'Ingrese nombre del usuario:') 
        _apellido=input(f'Ingrese apellido del usuario:') 
        _correo=input(f'Ingrese correo del usuario:')
        _contrasena=input(f'Ingrese contrasena del usuario:')
    
    def imprimir_registro(self):
        print(print(f'id:{self._id} nombre:{self._nombre} apellido:{self._apellido} correo:{self._correo} contrasena{self._contraseña}'))
            
