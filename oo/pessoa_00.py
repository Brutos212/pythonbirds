class Pessoa:
    def __init__(self, *filhos, nome = None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    fabio = Pessoa(nome='Fabio')
    vilma = Pessoa(fabio, nome='Vilma')
    print(Pessoa.comprimentar(vilma))
    print(id(vilma))
    print(vilma.comprimentar())
    print(vilma.nome)
    print(vilma.idade)
    for filhos in vilma.filhos:
        print(filhos.nome)
    fabio.sobrenome = 'Santos'
    del vilma.filhos
    print(fabio.__dict__)
    print(vilma.__dict__)
