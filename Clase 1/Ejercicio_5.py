import time

class Vehiculo:
    marca = ""
    combustible = ""
    tipo = str
    combustible_maximo = float
    combustible_tanque = float
    
    def __init__(self, marca, combustible, combustible_tanque):
        self.marca = marca
        self.combustible = combustible
        self.combustible_tanque = combustible_tanque
    
   
    def encender(self):
        if (((self.combustible_tanque / self.combustible_maximo * 100)) < 10):
            print("Bajo nivel de combustible vaya a una gasolinera")
        else:
            print (f"Se enciende el/la {self.tipo} sin ningun problema") 
    
    def arrancar(self):
        
        while (self.combustible_tanque > 0): 
            
            if (((self.combustible_tanque / self.combustible_maximo * 100)) > 10):
                print (f"El Vehiculo esta avanzando sin problemas quedan {self.combustible_tanque} galones en el tanque")   
            
            elif (((self.combustible_tanque / self.combustible_maximo * 100)) <= 10):
                print(f"Quedan {self.combustible_tanque} galones, el/la {self.tipo} se va a detener pronto vaya a una gasolinera")
            
            self.combustible_tanque -= 1
            time.sleep(1)
        print ("Deteniendo marcha")
    
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
        self.combustible_maximo = 10  

carro = Carro("BMW", "Corriente", 16)
carro.encender()
carro.arrancar()

moto = Moto("Honda", "Corriente", 10)
moto.encender()
moto.arrancar()
