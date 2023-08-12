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
    
carro = Vehiculo("BMW","Corriente")
print(carro)