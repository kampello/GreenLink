from tools.fornecedor_tools.stock import ver_stock, atualizar_stock, ver_pedidos_recebidos
from tools.fornecedor_tools.comunicacao import enviar_mensagem, ver_mensagens

class Fornecedor:
    def __init__(self, db_connection, nome):
        self.db = db_connection
        self.nome = nome

    def menu(self):
        while True:
            print("\n===== Painel do Fornecedor =====")
            print("(Não Funciona)")
            print("1. Ver pedidos recebidos ")
            print(" (Funciona menos a parte de adicionar novos produtos)")
            print("2. Atualizar stock de produtos")
            print("(Falta mostrar o preço)")
            print("3. Ver stock atual")
            print("(Não Funciona)")
            print("4. Enviar mensagem ao cliente")
            print("(Não Funciona)")
            print("5. Ver mensagens recebidas")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                ver_pedidos_recebidos(self.db, self.nome)
            elif opcao == "2":
                atualizar_stock(self.db)
            elif opcao == "3":
                ver_stock(self.db)
            elif opcao == "4":
                enviar_mensagem(self.db, self.nome)
            elif opcao == "5":
                ver_mensagens(self.db, self.nome)
            elif opcao == "0":
                print(" Saindo do painel do fornecedor...")
                break
            else:
                print(" Opção inválida, tente novamente.")
