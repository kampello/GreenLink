from tools.admin_tools.user_manager import criar_utilizador, apagar_utilizador, pesquisar_utilizador
from tools.admin_tools.product_manager import *
from tools.admin_tools.delivery_manager import ver_entregas
from tools.admin_tools.goals_manager import definir_objetivos, ver_objetivos


class Admin:
    """
    Classe que representa o painel de administração.
    Permite a gestão de funções como a criação e eliminação de utilizadores, a gestão
    de produtos, o acompanhamento das entregas, a aprovação de tickets e a definição
    de objetivos.
    :param db_connection: Ligação ativa à base de dados.
    :type db_connection: sqlite3.Connection
    """
    def __init__(self, db_connection):
        self.db = db_connection
    
    def menu(self):
        """
        Mostra o menu principal do administrador e processa as
        opções.
        """
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
            print("10. Objetivos Mensais")
            print("11. Definir Objetivos Mensais")
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
            elif opcao == "10":
                    self.ver_objetivos()
            elif opcao == "11":
                    self.definir_objetivos()
            elif opcao == "0":
                print("Saindo do painel de administração...")
                break
            else:
                print("Opção inválida, tente novamente.")
    def verificar_tickets_pendentes(self):
        """
        Confirma se existem tickets que estejam em espera e mostra
        essa informação no menu.
        """
        verificar_tickets_pendentes(self.db)

    def aprovar_ticket(self):
        """
        Lidera o processo de aprovação ou rejeição do ticket.
        """
        aprovar_ticket(self.db)


    def criar_utilizador(self):
        """
        Regista um novo utilizador no sistema.
        """
        criar_utilizador(self.db)

    def apagar_utilizador(self):
        """
        Elimina um utilizador já existente.
        """
        apagar_utilizador(self.db)

    def pesquisar_utilizador(self):
        """
        Realiza a pesquisa e exibe as informações de um utilizador.
        """
        pesquisar_utilizador(self.db)

    def adicionar_produto(self):
        """
        Regista um novo produto no stock.
        """
        adicionar_produto(self.db)

    def remover_produto(self):
        """
        Elimina um produto registado.
        """
        remover_produto(self.db)
    def ver_stock(self):
        """
        Dá a conhecer o stock atual dos produtos.
        """
        ver_stock(self.db)

    def ver_informacoes_produtos(self):
        """
        def ver_informacoes_produtos(self):
        """
        ver_informacoes_produtos(self.db)
    
    def ver_entregas(self):
        """
        def definir_objetivos(self):
        """
        ver_entregas(self.db)

    def definir_objetivos(self):
        """
        Estabelece os objetivos do sistema para cada mês.
        """
        definir_objetivos(self.db)

    def ver_objetivos(self):
        """
        Dá a conhecer os objetivos mensais já definidos.
        """
        ver_objetivos(self.db)

