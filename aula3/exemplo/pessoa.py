class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho')
        print(f'{self.idade} anos, e tenho')
        print(f'{self.altura} tudo isso de altura.')
        
p1 = Pessoa("Rafael", 18, "1.65")
p2 = Pessoa("Thiago", 15, "1.60")
p3 = Pessoa("Giba", 80, "1.70")

p1.apresentar()
p2.apresentar()
p3.apresentar()