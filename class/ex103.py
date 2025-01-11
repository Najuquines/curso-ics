class carro:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
class carroeletrico(carro):
    autonomia = None
    
    def add_info_carroeletronico(self, autonomia_passada):
        self.autonomia = autonomia_passada

    def detalhes(self):
        return self.marca + self.modelo + str(self.autonomia)
   
carro_eletrico = carroeletrico('BMW', 'M3')
carro_eletrico.add_info_carroeletronico(680)
detalhes = carro_eletrico.detalhes()
print(detalhes)
     

      
