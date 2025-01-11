class Pessoa:
    nome = None
    idade = None

    def _init_(self, nome_passado, idade_passada):
        self.nome = nome_passado
        self.idade = idade_passada

    def retornar_nome(self):
        return self.nome

    def alterar_nome(self, nome):
        self.nome = nome

    def retornar_idade(self):
        return self.idade

    def alterar_idade(self, idade):
        self.idade = idade

class Funcionario(Pessoa):
    salario = None

    def add_info_funcionario(self, salario_passado):
        self.salario = salario_passado

    def retorna_salario(self):
        return self.salario

    def alterar_salario(self, salario):
        self.salario = salario

    def detalhes(self):
        return "Nome: " + self.nome + "Idade: " + str(self.idade) + " Salário: " + str(self.salario)

pessoa = Pessoa("Alice ", 30)
print("Nome: " + pessoa.nome + "Idade: " + str(pessoa.idade) )

funcionario = Funcionario("Kaique ", 21)
funcionario.add_info_funcionario(9000)
print(funcionario.detalhes())

(funcionario.alterar_nome("Roberto "))
(funcionario.alterar_idade(45))
(funcionario.alterar_salario(5500))
print(funcionario.detalhes())