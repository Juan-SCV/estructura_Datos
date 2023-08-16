import pandas as pd

class Cultura_2015:
    referencia = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2015.csv"   
    nombre = "Encuesta cultural 2015"
    suma = int
    edades = float
    promedio = float

    def __init__(self, archivo, referencia, nombre):
        self.df = pd.read_csv(archivo, sep=";")
        self.referencia = referencia
        self.nombre = nombre

    def __str__(self):
        return f"Ahora realizaremos la suma y el promedio de edades en los encuestados en el archivo de nombre {self.nombre} y de referencia {self.referencia}"

    def suma_edades(self):
        self.suma = self.df['años'].sum()
        print("La suma de las edades es de", self.suma)
        
    def promedio_edades(self):
        self.suma = self.df['años'].sum()
        self.edades = len(self.df['años'])
        self.promedio = self.suma / self.edades
        print("La edad promedio en el censo es de", self.promedio)

archivo_df = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2015.csv"
cultura = Cultura_2015(archivo_df, Cultura_2015.referencia, Cultura_2015.nombre)
print(cultura) 
cultura.suma_edades()
cultura.promedio_edades()

