from Entidades.Diaria import Diaria
from Servicos.Servico_Funcao import Servico_Funcao

class Funcionarios:
    def __init__(self, id, cpf, nome, funcao) -> object:
        self._id = id
        self._cpf = cpf
        self.nome = nome
        self.funcao = funcao 

class Veiculos:
    def __init__(self, placa, marca, ano, autonomia, combustivel) -> object:
        self._placa = placa
        self.marca = marca
        self.ano = ano 
        self.autonomia = autonomia
        self.combustivel = combustivel

class Equipamentos_Alugaveis:
    def __init__(self, id, func_associado, tipo_equipamento, horas_equipamento) -> object:
        self.id = id
        self.func_associado = func_associado
        self.tipo_equipamento = tipo_equipamento 
        self.horas_equipamento = horas_equipamento

class Orcamento_combustivel:
    def __init__(self, distancia, valor_combustivel) -> object:
        self.distancia = distancia
        self.valor_combustivel = valor_combustivel
## forma de chamar o funcionado da classe equipamentos alugaveis com id da class funcionario
#print(.funcionario_associado._id)

Svc_Funcao = Servico_Funcao()
Svc_Funcao.adicionar_funcao('Pedreiro')
for funcao in Svc_Funcao.obter_funcoes():
    print(f"ID: {funcao['id']}, Função: {funcao['funcao']}")

diarias = Diaria(input=('')) 
valor_diarias = diarias.calcular_diaria()
print(valor_diarias)
