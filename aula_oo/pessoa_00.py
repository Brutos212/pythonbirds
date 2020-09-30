class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade=41):
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

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    fabio = Mutante(nome='Fabio')
    vilma = Homem(fabio, nome='Vilma')
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
    print(Pessoa.olhos)
    print(fabio.olhos)
    print(vilma.olhos)
    print(id(Pessoa.olhos), id(fabio.olhos), id(vilma.olhos))
    print(Pessoa.metodo_estatico(), fabio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), fabio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(fabio, Homem))
    print(isinstance(fabio, Homem))
    print(fabio.olhos)
    

