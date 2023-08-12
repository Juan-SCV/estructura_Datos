class Vehiculo:
    marca = str
    combustible = str
    tipo = str
    combustible_maximo = float
    combustible_tanque = float

    def __init__(self, marca, combustible, combustible_tanque):
        self.marca = marca
        self.combustible = combustible
        self.combustible_tanque = combustible_tanque
    
    def encender(self):
        if ((((self.combustible_tanque) / self.combustible_maximo * 100)) < 10):
            print("Bajo nivel de combustible vaya a una gasolinera")
        else:
            print (f"Se enciende el/la {self.tipo} sin ningun problema") 

    def arrancar(self):
        pass

    def __str__(self) -> str:
        return f"el vehiculo es un/a {self.tipo} {self.marca} y usa {self.combustible} como combustible"
    
class Carro(Vehiculo):
    def __init__(self, marca, combustible, combustible_tanque):
        super().__init__(marca, combustible, combustible_tanque)
        self.tipo = "Carro"
        self.combustible_maximo = 20

class Moto(Vehiculo):
    def __init__(self, marca, combustible, combustible_tanque):
        super().__init__(marca, combustible, combustible_tanque)
        self.tipo = "Moto"
        self.combustible_maximo = 8


carro = Carro("BMW","Corriente", 1)
moto = Moto("Suzuki","Corriente", 0.7)
print(carro)
carro.encender()
print(moto)
moto.encender()