import sqlite3

def adicionar_produto(db):
    nome = input("Nome do produto: ")
    preco = float(input("Preço (€): "))
    stock = int(input("Quantidade em stock: "))

    try:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)",
            (nome, preco, stock)
        )
        db.commit()
        print(f" Produto '{nome}' adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f" Erro ao adicionar produto: {e}")

def remover_produto(db):
    nome = input("Nome do produto a remover: ")
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
    db.commit()

    if cursor.rowcount > 0:
        print(f" Produto '{nome}' removido.")
    else:
        print(" Produto não encontrado.")
        
#funcao para ver na base de dados os stock 
def ver_stock(db):
    cursor = db.cursor()
    cursor.execute("SELECT nome, preco, stock FROM produtos ORDER BY nome")
    produtos = cursor.fetchall()

    if produtos:
        print("\nStock Atual dos Produtos:\n")
        print(f"{'Produto':<20} {'Preço (€)':<10} {'Stock':<6} {'Status'}")
        print("-" * 50)

        for nome, preco, stock in produtos:
            status = "Baixo" if stock <= 5 else "OK"
            print(f"{nome:<20} {preco:<10.2f} {stock:<6} {status}")

        total_produtos = sum([p[2] for p in produtos])
        print(f"\nTotal de produtos em stock: {total_produtos}")
    else:
        print("Nenhum produto registado.")


def ver_informacoes_produtos(db):
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, preco, stock FROM produtos")
    produtos = cursor.fetchall()

    if produtos:
        print("\n Lista de Produtos:")
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Preço: €{p[2]:.2f} | Stock: {p[3]}")
    else:
        print("Nenhum produto encontrado.")

def verificar_tickets_pendentes(db):
    cursor = db.cursor()
    cursor.execute("SELECT id, fornecedor, produto, preco, stock FROM tickets_produto WHERE status='pendente'")
    tickets = cursor.fetchall()

    if tickets:
        print("\n Tickets pendentes de aprovação:")
        for t in tickets:
            print(f"ID: {t[0]} | Fornecedor: {t[1]} | Produto: {t[2]} | Preço: €{t[3]:.2f} | Stock: {t[4]}")
        print("Aguarda aprovação do admin...\n")
    else:
        print("Nenhum ticket pendente no momento.")



def aprovar_ticket(db):
    cursor = db.cursor()

    # Pega todos os tickets pendentes
    cursor.execute("SELECT id, fornecedor, produto, preco, stock FROM tickets_produto WHERE status='pendente'")
    tickets = cursor.fetchall()

    if not tickets:
        print("Nenhum ticket pendente no momento.")
        return

    print("\nTickets pendentes:")
    for t in tickets:
        print(f"ID: {t[0]} | Fornecedor: {t[1]} | Produto: {t[2]} | Preço: €{t[3]:.2f} | Stock: {t[4]}")

    escolha = input("\nDeseja Aprovar ou Negar? - (A/N): ").strip().upper()
    if escolha not in ("A", "N"):
        print("Opção inválida.")
        return

    try:
        ticket_id = int(input("Digite o ID do ticket que deseja processar: "))
    except ValueError:
        print("ID inválido.")
        return

    cursor.execute("SELECT fornecedor, produto, preco, stock FROM tickets_produto WHERE id=? AND status='pendente'", (ticket_id,))
    ticket = cursor.fetchone()
    if not ticket:
        print(" Ticket não encontrado ou já processado.")
        return

    fornecedor, produto, preco, stock = ticket


    #Obter fornecedor_id
    cursor.execute("SELECT id FROM fornecedores WHERE nome = ?", (fornecedor,))
    res = cursor.fetchone()
    if not res:
    if escolha == "A":
        cursor.execute("INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)", (produto, preco, stock))
        cursor.execute("UPDATE tickets_produto SET status='feito' WHERE id=?", (ticket_id,))
        print(f"✅ Ticket do produto '{produto}' aprovado e adicionado ao catálogo.")
    else:
        cursor.execute("UPDATE tickets_produto SET status='rejeitado' WHERE id=?", (ticket_id,))
        print(f"❌ Ticket do produto '{produto}' rejeitado pelo admin.")

    db.commit()
