class Funcionario:
    nome = None
    salario = None

    def _init_(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_salario(self):
        return self.salario

class FuncionarioHorista(Funcionario):
    horas_trabalhadas = None
    taxa_por_hora = None

    def add_info_funcionarioHorista(self, horas_trabalhadas, taxa_por_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.taxa_por_hora = taxa_por_hora
    
    def calcular_salario(self):
        return int(self.horas_trabalhadas) - int(self.taxa_por_hora)

funcionario = Funcionario(" João ", 3000)
print("O Salário do funcionário " + funcionario.nome + "é: " + str(funcionario.calcular_salario()))
funcionario_horista = FuncionarioHorista(" Maria ", 0)
funcionario_horista.add_info_funcionarioHorista(5000, 500)
print("O Salário da funcionária horista" + funcionario_horista.nome + str(funcionario_horista.calcular_salario()))
