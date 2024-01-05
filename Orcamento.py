class _Funcionarios:
    def __init__(self, id, cpf, nome, funcao) -> object:
        self._id = id
        self._cpf = cpf
        self._nome = nome
        self._funcao = funcao 

class Veiculos:
    def __init__(self, marca, placa, ano, autonomia, combustivel) -> object:
        self._marca = marca
        self._placa = placa
        self._ano = ano 
        self._autonomia = autonomia
        self._combustivel = combustivel


class Equipamentos_Alugaveis:
    def __init__(self, id, func_associado, tipo_equipamento, horas_equipamento) -> object:
        self.id = id
        self.func_associado = func_associado
        self.tipo_equipamento = tipo_equipamento 
        self.horas_equipamento = horas_equipamento

## forma de chamar o funcionado da classe equipamentos alugaveis com id da class funcionario
#print(.funcionario_associado._id)
        

funcoes_funcionarios = [
    {
        'id_funçoes': 1,
        'funçao': 'Motorista de Retroescavadeira.'
    },
    {
        'id_funçoes': 2,
        'funçao': 'Motorista de Empilhadeira.'
    },
    {
        'id_funçoes': 3,
        'funçao': 'Instalador de Equipamentos.'
    },
    {
        'id_funçoes':4,
        'funçao': 'Técnico em Mecânica.'
    }
]


