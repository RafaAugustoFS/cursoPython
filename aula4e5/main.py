from sistema_mysql.src.controller import produto_controller
from sistema_mysql.src.controller import user_controller

def exibir_menu():
    print("\nA FIRMA")
    print("\n==== MENU ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar produto")
    print("5 - Buscar produto unico")
    print("6 - Cadastrar usuário")
    print("7 - Buscar usuários")
    print("8 - Buscar usuário unico")
    print("9 - Atualizar usuário")
    print("10 - Deletar usuário")
    print("0 - Sair")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Não existe produtos cadastrados")

def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    nome = input("Digite o nome: ")
    preco = input("Digite o valor: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

def atualizar_produto():
    print("\nATUALIZANDO O PRODUTO")
    produto_id = input("Digite o ID do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")

    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhum produto foi atualizado!")

def deletar_produto():
    print("\n--- Deletar Produto ---")
    produto_id = input("Digite o ID do produto: ")
    linhas = produto_controller.remover_produto(produto_id)
    if linhas > 0:
        print("Produto deletado com sucesso!")
    else:
        print("Nenhum produto foi deletado!")

def buscar_produto_unico():
    print("\n--- Buscar Produto Unico ---")
    produto_id = input("Digite o ID do produto: ")
    produto = produto_controller.obter_produto(produto_id)
    if produto:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Produto não encontrado")
        
def cadastrar_usuario():
    print("\n--- Cadastrar usuário ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")
    novo_id = user_controller.cadastrar_usuario(nome, idade, email)
    print(f"Usuário cadastrado com sucesso com o novo ID {novo_id}.")
    
def buscar_usuario_unico():
    print("\n--- Buscar usuário Unico ---")
    usuario_id = input("Digite o ID do usuário: ")
    usuario = user_controller.obter_usuario(usuario_id)
    if usuario:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, idade: {usuario['idade']}, email: {usuario['email']}")
    else:
        print("Usuário não encontrado")

def listar_usuarios():
    print("\n--- Lista de usuários ---")
    usuarios = user_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, idade: {usuario['idade']}, email: {usuario['email']}")
    else:
        print("Não existe usuários cadastrados")

def atualizar_usuario():
    print("\nATUALIZANDO O USUÁRIO")
    user_id = input("Digite o ID do usuário: ")
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")

    linhas = user_controller.atualizar_user(user_id, nome, idade, email)
    if linhas > 0:
        print("Usuário atualizado com sucesso!")
    else:
        print("Nenhum usuário foi atualizado!")

def deletar_usuario():
    print("\n--- Deletar usuário ---")
    user_id = input("Digite o ID do usuario: ")
    linhas = user_controller.remover_user(user_id)
    if linhas > 0:
        print("Usuário deletado com sucesso!")
    else:
        print("Nenhum usuário foi deletado!")
# main -> Inicializar o projeto
def main():
    # While True para repetir mesmo que a opção digitado esteja errada
    while True:

        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
            
        elif opc == "2":
            listar_produtos()
            
        elif opc == "3":
            atualizar_produto()
        
        elif opc == "4":
            deletar_produto()
        
        elif opc == "5":
            buscar_produto_unico()
            
        elif opc == "6":
            cadastrar_usuario()
            
        elif opc == "7":
            listar_usuarios()
            
        elif opc == "8":
            buscar_usuario_unico()
            
        elif opc == "9":
            atualizar_usuario()
            
        elif opc == "10":
            deletar_usuario()
        
        elif opc == "0":
            print("Saiu do programa.")
            break
        else:
            print("Opção Inválida")

if __name__ == '__main__':
    main()