from tools.cliente_tools.pedidos import ver_pedidos, fazer_pedido, ver_produtos_disponiveis
from tools.cliente_tools.comunicacao import enviar_mensagem, ver_mensagens

class Cliente:
    def __init__(self, db_connection, nome):
        self.db = db_connection
        self.nome = nome
    
    def menu(self):
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
