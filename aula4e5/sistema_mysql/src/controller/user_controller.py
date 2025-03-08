from ..model.user_model import UserModel

def listar_usuarios():
    model = UserModel()
    usuarios = model.get_all_users()
    model.close_connection()
    return usuarios

def cadastrar_usuario(nome, idade, email):
    model = UserModel()
    novo_user = model.insert_user(nome, idade, email)
    model.close_connection()
    return novo_user

def obter_usuario(user_id):
    model = UserModel()
    usuario = model.get_user_by_id(user_id)
    model.close_connection()
    return usuario

def atualizar_user(user_id, nome, idade, email):
    model = UserModel()
    linhas_afetadas = model.update_user(user_id, nome, idade, email)
    model.close_connection()
    return linhas_afetadas

def remover_user(user_id):
    model = UserModel()
    linhas_afetadas = model.delete_user(user_id)
    model.close_connection()
    return linhas_afetadas