
#CLASES
import random
class Perro:
    #DEFINIR ATRIBUTOS EN UN CONSTRUCTOR 
    def __init__(self, nombre, color, edad):
        self._nombre = nombre    
        self._color = color
        self._edad = edad
    def Perro_Ladrar(self):
        print("waauuu, wauuu¡ ")
    def Perro_Camina(self):
        print("Se mueve a la derecha ")   
    def Perro_Saluda(self):
        return "Da la pata" if random.randint(0,1) == 1 else "Mueve la cola"
#Crear un objeto
Perro1=Perro("Escai","Negro",5)
print(Perro1._nombre,Perro1._color,Perro1._edad)
Perro1.Perro_Ladrar()
Perro1.Perro_Camina()
print(Perro1.Perro_Saluda())




# p= Perro()
# p._nombre = "asd"
# print(p._nombre)
# q = Perro("Escai","Negro,blanco",5)
# print(q._color)
# Ladrar()