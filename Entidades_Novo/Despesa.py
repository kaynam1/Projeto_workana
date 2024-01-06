class Despesa: 
    def __init__(self, nome, tipo) -> object:
        self.id = 1
        self.tipo = tipo
        self.nome = nome
        self.valores = {}
        self.funcionario = None

    def adicionar_valor(self, chave, valor):
        self.valores[chave] = valor
        
    def vincular_funcionario(self, funcionario):
        self.uncionario = funcionario
