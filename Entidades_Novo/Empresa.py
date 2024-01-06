class Empresa: 
    def __init__(self, nome) -> object:
        self.id = 1
        self.nome = nome
        self.despesas = []
        self.funcionarios = []
        self.equipamentos = []

    def adicionar_despesas(self, despesa):
        self.despesas.append(despesa)

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, funcionario):
        self.funcionarios.pop(funcionario)
        
        
    def gerar_relatorio(self):
        
        print(f'\n Relatorio da empresa é {self.nome} \n')
        
        print(f'Funcionarios:  ')
        for funcionario in self.funcionarios:
            print(f' {funcionario.nome = } | {funcionario.cpf = } | {funcionario.funcao = }') ## laterar formataçao
    