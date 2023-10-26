class Vehiculo:
    def __init__(self,marca,modelo,color,ruedas,ref):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas
        self.ref=ref
        
    def ver_vehiculo(self):
        print(f"Marca: {self.marca} \n Modelo: {self.modelo} \n Color: {self.color}")
    
moto=Vehiculo("Yamaha",2023,"Negro",2,"N-Max 150")

carro=Vehiculo("Mazda",2024,"Blanco",4,"CX-5")

def ver_vehiculo(self):
    print(f"Marca: {self.marca} \n Modelo{self.modelo} \n Color{self.color}")

print(carro.marca)
print(moto.marca)

#También se puede sobreescribir el atributo
carro.marca="Renault"
print(carro.marca)

# Ahora vamos a crear un metodo para ver el vehiculo y sus atributos

carro.ver_vehiculo()
moto.ver_vehiculo()

