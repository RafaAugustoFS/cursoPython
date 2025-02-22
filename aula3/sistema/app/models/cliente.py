class Cliente:
    
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        
    def __str__(self):
        return f"cliente(nome = {self.nome}, email{self.email}, idade={self.idade})"
        