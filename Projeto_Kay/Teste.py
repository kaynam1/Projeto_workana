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

class Funcao_Funcionario:
    contador_id = 1  # Inicializa o contador de ID

    def __init__(self):
        self.lista_funcoes = [
            {
                'id': 1,
                'funcao': 'Motorista de Retroescavadeira.'
            },
            {
                'id': 2,
                'funcao': 'Motorista de Empilhadeira.'
            },
            {
                'id': 3,
                'funcao': 'Instalador de Equipamentos.'
            },
            {
                'id': 4,
                'funcao': 'Técnico em Mecânica.'
            }
        ]

    def obter_funcoes(self):
        return self.lista_funcoes

    def adicionar_funcao(self, nome_funcao):
        if self.lista_funcoes:
            ultimo_id = self.lista_funcoes[-1]['id']
            novo_id = ultimo_id + 1
        else:
            novo_id = Funcao_Funcionario.contador_id

        self.lista_funcoes.append({
            'id': novo_id,
            'funcao': nome_funcao
        })

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

class Funcionario: 
    def __init__(self, cpf, nome, funcao) -> object:
        self.id = 1
        self.cpf = cpf
        self.nome = nome
        self.funcao = funcao
        self.despesas = [] 

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)

class Manipulado_Entrada:
    @staticmethod
    def adicionar_funcionarios_terminal(construtor_empresa):
        nome_funcionario = input('Digite nome do funcionario: ')
        cpf_funcionario = input('Digite cpf do funcionario: ')
        funcao_funcionario = input('Digite função do funcionario: ')
        construtor_empresa.adicionar_funcionario
        (cpf_funcionario, nome_funcionario, funcao_funcionario)


nome = input('Digite o nome da empresa: ')
construtor = Construtor_Empresa(nome)
Manipulado_Entrada.adicionar_funcionarios_terminal(construtor)

empresa = construtor.obter_empresa()
empresa.gerar_relatorio()

"""
adicionar_funcionarios_terminal
adicionar_equipamentos_terminal
adicionar_despesas_termial
    adicionar uma verificação por tipo de despesas 

"""


