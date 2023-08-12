class Vehiculo:
    marca = str
    combustible = str

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible

    def encender(self):
        pass

    def arrancar(self):
        pass

    def __str__(self) -> str:
        return f"el vehiculo es un {self.marca} y usa {self.combustible} como combustible"
    
class Carro(Vehiculo):
    pass

class Moto(Vehiculo):
    pass


carro = Vehiculo("BMW","Corriente")
moto = Vehiculo("Suzuki","Corriente")
print(carro)
print(moto)