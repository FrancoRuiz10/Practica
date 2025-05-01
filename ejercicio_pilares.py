"""""
Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
Cada clase hija debe tener un método propio sobrescrito que imprima información
diferente. Crea una función que reciba un vehículo y llame a ese método.
"""
class vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def descripcion(self):
        return f"Este es un vehiculo de la marca {self.marca} y modelo {self.modelo}"
    
class Auto(vehiculo):

    def descripcion(self):
        return super().descripcion()
    
class Moto(vehiculo):
    
    def descripcion(self):
        return super().descripcion()
    
def mostrar_descipcion(vehiculo):
    print(vehiculo.descripcion())

auto=Auto("toyoya", "Nose")


moto=Moto("Goku", "Vegeta")

mostrar_descipcion(auto)
mostrar_descipcion(moto)
