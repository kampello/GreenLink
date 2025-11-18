<<<<<<< HEAD
from tools.fornecedor_tools.stock import ver_stock, atualizar_stock
from tools.fornecedor_tools.comunicacao import enviar_mensagem, ver_mensagens
=======
from tools.fornecedor_tools.stock import ver_stock, atualizar_stock, ver_pedidos_recebidos
from tools.fornecedor_tools.comunicacao import enviar_mensagem, ver_mensagens, abrir_ticket_produto
>>>>>>> main

class Fornecedor:
    def __init__(self, db_connection, nome):
        self.db = db_connection
        self.nome = nome

    def menu(self):
        while True:
            print("\n===== Painel do Fornecedor =====")
            print("1. Ver pedidos recebidos")
            print("2. Atualizar stock de produtos")
            print("3. Ver stock atual")
            print("4. Enviar mensagem ao cliente")
            print("5. Ver mensagens recebidas")
            print("6. Abrir ticket para adicionar novo produto ao admin")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                # Ver pedidos recebidos (implementar)
                print("→ Função ver_pedidos_recebidos() ainda não implementada")
            elif opcao == "2":
                atualizar_stock(self.db, self.nome)
            elif opcao == "3":
                ver_stock(self.db, self.nome)
            elif opcao == "4":
                enviar_mensagem(self.db, self.nome)
            elif opcao == "5":
                ver_mensagens(self.db, self.nome)
            elif opcao == "6":
<<<<<<< HEAD
                print("→ Função abrir ticket ainda não implementada")
=======
                abrir_ticket_produto(self.db, self.nome)
>>>>>>> main
            elif opcao == "0":
                print("Saindo do painel do fornecedor...")
                break
            else:
                print("Opção inválida, tente novamente.")

