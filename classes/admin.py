from tools.admin_tools.user_manager import criar_utilizador, apagar_utilizador, pesquisar_utilizador
from tools.admin_tools.product_manager import *
from tools.admin_tools.delivery_manager import ver_entregas


class Admin:
    def __init__(self, db_connection):
        self.db = db_connection

    def menu(self):
        
        while True:
            self.verificar_tickets_pendentes()
            print("\n===== Painel de Administração =====")
            print("1. Criar utilizador")
            print("2. Apagar utilizador")
            print("3. Pesquisar utilizador")
            print("4. Adicionar produto")
            print("5. Remover produto")
            print("6. Ver stock")
            print("7. Ver informações de produtos")
            print("8. Aprovar / Negar Ticket")
            print("9. Acompanhar Entrega")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_utilizador()
            elif opcao == "2":
                self.apagar_utilizador()
            elif opcao == "3":
                self.pesquisar_utilizador()
            elif opcao == "4":
                self.adicionar_produto()
            elif opcao == "5":
                self.remover_produto()
            elif opcao == "6":
                self.ver_stock()
            elif opcao == "7":
                self.ver_informacoes_produtos()
            elif opcao == "8":
                    self.aprovar_ticket()
            elif opcao == "9":
                    self.ver_entregas()
            elif opcao == "0":
                print("Saindo do painel de administração...")
                break
            else:
                print("Opção inválida, tente novamente.")
    def verificar_tickets_pendentes(self):
        verificar_tickets_pendentes(self.db)

    def aprovar_ticket(self):
        aprovar_ticket(self.db)


    def criar_utilizador(self):
        criar_utilizador(self.db)

    def apagar_utilizador(self):
        apagar_utilizador(self.db)

    def pesquisar_utilizador(self):
        pesquisar_utilizador(self.db)

    def adicionar_produto(self):
        adicionar_produto(self.db)

    def remover_produto(self):
        remover_produto(self.db)
    def ver_stock(self):
        ver_stock(self.db)

    def ver_informacoes_produtos(self):
        ver_informacoes_produtos(self.db)
    
    def ver_entregas(self):
        ver_entregas(self.db)

