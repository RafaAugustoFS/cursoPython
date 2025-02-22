from ..models.cliente import Cliente
from ..database.database import BancoFake

class ClienteController:
    
    def __init__(self):
        self.db = BancoFake()
    
    def _criar_cliente(self, nome, email, idade):
        novo_cliente = Cliente(nome, email, idade)
        
        dict_cliente = {
            "nome" : novo_cliente.nome,
            "email" : novo_cliente.email,
            "idade" : novo_cliente.idade
        }
        self.db._adicionar_cliente(dict_cliente)
        print("Cliente cadastrado no banco de dados")
    
    def _listar_clientes(self):
        """
         Retorna uma lista de clientes
        """
        return self.db._listar_clientes()