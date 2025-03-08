import mysql.connector
from config import Config

class UserModel:
    
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
        
    def insert_user(self, nome, idade, email):
        query = "INSERT INTO usuarios (nome, idade, email) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nome, idade, email))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_all_users(self):
        """ Retomar a lista de produtos """
        query = "SELECT id, nome, idade, email FROM usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_user_by_id(self, user_id):
        """ Busca o produto pelo ID """
        query = "SELECT id, nome, idade, email FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()
    
    def update_user(self, user_id, nome, idade, email):
        query = "UPDATE usuarios SET nome = %s, idade = %s, email = %s WHERE id = %s"
        self.cursor.execute(query, (nome, idade, email, user_id))
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete_user(self, user_id):
        """Deletar um produto pelo id."""
        query = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.rowcount
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()