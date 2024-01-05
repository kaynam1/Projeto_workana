class Diaria:
    def __init__(self, qt_dias, valor_diaria, qt_refeicoes, valor_refeicoes) -> object:
        self.qt_dias = qt_dias
        self.valor_diaria = valor_diaria
        self.qt_refeicoes = qt_refeicoes
        self.valor_refeicoes = valor_refeicoes
    
    def calcular_diaria(self):
        return self.qt_dias * self.valor_diaria
    
    def calcular_refeicoes(self):
        return self.qt_refeicoes * self.valor_refeicoes