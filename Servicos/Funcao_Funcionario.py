
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
