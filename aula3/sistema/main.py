from app.controllers.clienteController import ClienteController
from app.controllers.produtoController import ProdutoController

def exibir_menu():
    print("\n==== MENU ====")
    print('1 = Cadastrar cliente')
    print('2 = Listar clientes')
    print('3 = Cadastrar produtos')
    print('4 = Listar produtos')
    print('0 = Sair do sistema')
    
def main():
    cntrlCliente = ClienteController()
    cntrlProduto = ProdutoController()
    
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")
        
        if opc == "1":
            nome = input("Nome do cliente:")
            email = input("Email do cliente:")
            idade = int(input("Idade:"))
            cntrlCliente._criar_cliente(nome, email, idade)
        elif opc == "2":
            #listar do banco de dados do cliente
            clientes = cntrlCliente._listar_clientes()
            #__str__ -> cliente -> Cliente(nome="", email="", idade="" )
            for index, cliente in enumerate(clientes, 1):
                print(f"{index}. {cliente}")
        elif opc == "3":
            nome = input("Nome do produto:")    
            preco = float(input("Preço:"))
            cntrlProduto._criar_produto(nome, preco)
        elif opc == "4":
            #Listar do banco de dados os produtos
            produtos = cntrlProduto._listar_produtos()
            for index, produto in enumerate(produtos, 1):
                print(f"{index}. {produto}")
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida do sistema")
            
if __name__ == "__main__":         
    main()