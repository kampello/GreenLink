class Admin:
    def __init__(self, db_connection):
        self.db = db_connection

    def menu(self):
        while True:
            print("\n===== Painel de Administração =====")
            print("1. Criar utilizador")
            print("2. Apagar utilizador")
            print("3. Pesquisar utilizador")
            print("4. Adicionar produto")
            print("5. Remover produto")
            print("6. Ver stock")
            print("7. Ver informações de produtos")
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
            elif opcao == "0":
                print("Saindo do painel de administração...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def criar_utilizador(self):
        print("→ Função criar_utilizador() ainda não implementada.")

    def apagar_utilizador(self):
        print("→ Função apagar_utilizador() ainda não implementada.")

    def pesquisar_utilizador(self):
        print("→ Função pesquisar_utilizador() ainda não implementada.")

    def adicionar_produto(self):
        print("→ Função adicionar_produto() ainda não implementada.")

    def remover_produto(self):
        print("→ Função remover_produto() ainda não implementada.")

    def ver_stock(self):
        print("→ Função ver_stock() ainda não implementada.")

    def ver_informacoes_produtos(self):
        print("→ Função ver_informacoes_produtos() ainda não implementada.")
