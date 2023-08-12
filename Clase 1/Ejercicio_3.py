class Vehiculo:
    marca = str
    combustible = str
    tipo = str

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
        self.tipo = ""
    
    def encender(self):
        pass

    def arrancar(self):
        pass

    def __str__(self) -> str:
        return f"el vehiculo es un/a {self.tipo} {self.marca} y usa {self.combustible} como combustible"
    
class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = "Carro"

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = "Moto"


carro = Carro("BMW","Corriente")
moto = Moto("Suzuki","Corriente")
print(carro)
print(moto)