from tools.cliente_tools.pedidos import ver_pedidos, fazer_pedido, ver_produtos_disponiveis
from tools.cliente_tools.comunicacao import enviar_mensagem, ver_mensagens

class Cliente:
    """
    Representa um cliente do sistema GreenLink.

    Permite ao cliente:
    - Ver produtos disponíveis
    - Fazer pedidos
    - Consultar pedidos já realizados
    - Enviar mensagens a fornecedores
    - Ler mensagens recebidas

    :param db_connection: Conexão com a base de dados SQLite
    :type db_connection: sqlite3.Connection
    :param nome: Nome do cliente
    :type nome: str
    """

    def __init__(self, db_connection, nome):
        
        self.db = db_connection
        self.nome = nome

    def menu(self):
        """
        Exibe o menu interativo do cliente no terminal.

        O menu oferece as seguintes opções:

        1. Ver produtos disponíveis
        2. Fazer um pedido
        3. Ver meus pedidos
        4. Enviar mensagem ao fornecedor
        5. Ver mensagens recebidas
        0. Sair

        O método fica em loop até o utilizador escolher "0" para sair.

        Cada opção chama a função correspondente importada de:
        - tools.cliente_tools.pedidos
        - tools.cliente_tools.comunicacao
        """
        while True:
            print("\n===== Painel do Cliente =====")
            print("1. Ver produtos disponíveis")
            print("2. Fazer um pedido")
            print("3. Ver meus pedidos")
            print("4. Enviar mensagem ao fornecedor")
            print("5. Ver mensagens recebidas")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                ver_produtos_disponiveis(self.db)
            elif opcao == "2":
                fazer_pedido(self.db, self.nome)
            elif opcao == "3":
                ver_pedidos(self.db, self.nome)
            elif opcao == "4":
                enviar_mensagem(self.db, self.nome)
            elif opcao == "5":
                ver_mensagens(self.db, self.nome)
            elif opcao == "0":
                print("Saindo do painel do cliente...")
                break
            else:
                print("Opção inválida, tente novamente.")
