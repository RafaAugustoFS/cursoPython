import mysql.connector
from config import Config

class ProdutoModel:

    def __init__(self):
        # Iniciando a configuração
        self.config = Config()

        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )

        # Faz o cursor trazer o resultado em dicionários
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_products(self):
        query = "SELECT id, nome, preco FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_product(self, nome, preco):
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        self.cursor.execute(query, (nome, preco))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_product_by_id(self, product_id):
        query = "SELECT id, nome, preco FROM produtos WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def delete_product_by_id(self, product_id):
        query = "DELETE FROM produtos WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        return self.cursor.rowcount
    
    def update_product_by_id(self, product_id, nome, preco):
        query = "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s"
        self.cursor.execute(query, (nome, preco, product_id))
        self.connection.commit()
        return self.cursor.rowcount
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()