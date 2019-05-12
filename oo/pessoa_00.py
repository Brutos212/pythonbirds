class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    fabio.olhos = 1
    del fabio.olhos
    print(fabio.__dict__)
    print(vilma.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fabio.olhos)
    print(vilma.olhos)
    print(id(Pessoa.olhos), id(fabio.olhos), id(vilma.olhos))
    print(Pessoa.metodo_estatico(), fabio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), fabio.nome_e_atributos_de_classe())

