from Construtor.Construtor_Empresa import Construtor_Empresa
from Entrada_dados.Manipulador_Entrada import Manipulado_Entrada
from Servicos.Funcao_Funcionario import Funcao_Funcionario

nome = input('Digite o nome da empresa: ')
construtor = Construtor_Empresa(nome)
Manipulado_Entrada.adicionar_funcionarios_terminal(construtor)

empresa = construtor.obter_empresa()
empresa.gerar_relatorio()

