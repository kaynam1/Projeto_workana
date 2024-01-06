class Funcionario: 
    def __init__(self, cpf, nome, funcao) -> object:
        self.id = 1
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao
        self.despesas = [] 

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)
