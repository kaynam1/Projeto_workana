class Manipulado_Entrada:
    @staticmethod
    def adicionar_funcionarios_terminal(construtor_empresa):
        nome_funcionario = input('Digite nome do funcionario: ')
        cpf_funcionario = input('Digite cpf do funcionario: ')
        funcao_funcionario = input('Digite função do funcionario: ')
        construtor_empresa.adicionar_funcionario(cpf_funcionario, nome_funcionario, funcao_funcionario)   
        
        
        