from Entidades_Novo.Empresa import Empresa
from Entidades_Novo.Equipamento import Equipamento
from Entidades_Novo.Funcionario import Funcionario
from Entidades_Novo.Despesa import Despesa

class Construtor_Empresa:
    def __init__(self, nome):
        self.empresa = Empresa(nome)
    
    def adicionar_despesas(self, nome, tipo):
        despesa = Despesa(nome, tipo)
        self.empresa.adicionar_despesa(despesa)
        return self

    def adicionar_equipamento(self, nome, tipo, placa = None):
        equipamento = Equipamento(nome, tipo, placa)
        self.empresa.adicionar_equipamento(equipamento)
        return self

    def adicionar_funcionario(self, cpf, nome, funcao):
        funcionario = Funcionario(cpf, nome, funcao)
        self.empresa.adicionar_funcionario(funcionario)
        return self

    def remover_funcionario(self, funcionario):
        self.funcionarios.pop(funcionario)

    def adicionar_valor_despesa(self, chave, valor):
        if self.empresa.despesas:
            despesa_atual = self.empresa.despesas[-1]
            despesa_atual.adicionar_valor(chave, valor)
        return self

    def obter_empresa(self):
        return self.empresa
