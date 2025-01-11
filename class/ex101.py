class pessoa:
    def _init_(self,_nome,_idade):
        self.nome = _nome
        self.idade = _idade

class estudante(pessoa):
    escola = None
    serie = None
    frequencia = None

    def add_info_estudante(self, escola, serie, frequencia):
        self.escola = escola
        self.serie = serie
        self.frequencia = frequencia

    def retornar_informacoes(self):
        return self.nome + str(self.idade) + self.escola + self.serie + self.frequencia

Estudante = estudante("naju ", 15)
Estudante.add_info_estudante(" escola silva de alencar ", "1 ano ", " 22")
exibir_informacoes = Estudante.retornar_informacoes()
print(exibir_informacoes)



        