class Coche:
    marca = ""
    color = ""
    __encendido = False
    
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        
    def encender(self):
        self.__encendido = True
        
    def get_encendido(self):
        return self.__encendido
       
    
class CocheDeportivo(Coche):
    cv = 60
    
    def __init__(self, marca, color, cv):
        self.marca = marca
        self.color = color
        self.cv = cv             
              
coche1 = Coche("Fiat", "Azul")
coche1.encender()


print(f'Marca: {coche1.marca}')
print(f'Color: {coche1.color}')
print(f'Encendido: {coche1.get_encendido()}')


print('Coche deportivo: ')

coche_lujo = CocheDeportivo("BMW", "Rojo", 280)
coche_lujo.encender()

print(f'Marca: {coche_lujo.marca}')
print(f'Color: {coche_lujo.color}')
print(f'CV: {coche_lujo.cv}')
print(f'Encendido: {coche_lujo.get_encendido()}')             
        

 