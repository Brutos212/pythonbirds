DIRECOES = ['Norte', 'Leste', 'Sul', 'Oeste']

class Direcao:
    def __init__(self):
        self.__direcao = 0
        self.valor = DIRECOES[self.__direcao]

    def girar_a_direita(self):
        self.__direcao = (self.__direcao + 1) % len(DIRECOES)
        self.valor = DIRECOES[self.__direcao]

    def girar_a_esquerda(self):
        self.__direcao = (self.__direcao - 1) % len(DIRECOES)
        self.valor = DIRECOES[self.__direcao]




