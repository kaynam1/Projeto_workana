class Equipamento: 
    def __init__(self, nome, tipo, placa = None) -> object:
        self.id = 1
        self.nome = nome
        self.tipo = tipo
        self.placa = placa
        self.despesas = []
        self.funcionario = None

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)
        
    def vincular_funcionario(self, funcionario):
        self.funcionario = funcionario
