from tools.fornecedor_tools.stock import ver_stock, atualizar_stock, ver_pedidos_recebidos
from tools.fornecedor_tools.comunicacao import enviar_mensagem, ver_mensagens, abrir_ticket_produto
from tools.fornecedor_tools.delivery_actions import registar_entrega
from tools.fornecedor_tools.exportar_relatorio import exportar_relatorio_vendas


class Fornecedor:
    def __init__(self, db_connection, nome):
        self.db = db_connection
        self.nome = nome

    def menu(self):
        while True:
            print("\n===== Painel do Fornecedor =====")
            print("1. Ver pedidos recebidos (em desenvolvimento)")
            print("2. Atualizar stock de produtos (em desenvolvimento: falta mostrar o preço)")
            print("3. Ver stock atual (em desenvolvimento)")
            print("4. Enviar mensagem ao cliente (em desenvolvimento)")
            print("5. Ver mensagens recebidas (em desenvolvimento)")
            print("6. Abrir ticket para adicionar novo produto ao admin")
            print("7. Registar entrega")
            print("8. Exportar relatório de vendas")
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
            elif opcao == "6":
                abrir_ticket_produto(self.db, self.nome)
            elif opcao == "7":
                registar_entrega(self.db, self.nome)
            elif opcao == "8":
                exportar_relatorio_vendas(self.db, self.nome)
            elif opcao == "0":
                print(" Saindo do painel do fornecedor...")
                break
            else:
                print(" Opção inválida, tente novamente.")
