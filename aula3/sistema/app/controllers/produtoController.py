from ..models.produto import Produto
from ..database.database import BancoFake

class ProdutoController:
    
    def __init__(self):
        self.db = BancoFake()
        
    def _criar_produto(self, nome, preco):
        novo_produto = Produto(nome, preco)
        
        dict_produto = {
            "nome" : novo_produto.nome,
            "preco" : novo_produto.preco
        }
        self.db._adicionar_produto(dict_produto)
        print("Produto cadastrado no banco de dados")
    
    def _listar_produtos(self):
        """
         Retorna uma lista de clientes
        """
        return self.db._listar_produtos()