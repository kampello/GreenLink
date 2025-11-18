import sqlite3

def enviar_mensagem(db, fornecedor_nome):
    cursor = db.cursor()

    print("\n=== Enviar Mensagem a Cliente ===")

    # Buscar lista de clientes registados
    cursor.execute("SELECT nome FROM utilizadores WHERE tipo = 'cliente'")
    clientes = cursor.fetchall()

    if not clientes:
        print("❌ Não existem clientes registados.")
        return

    print("\nClientes disponíveis:")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c[0]}")

    try:
        escolha = int(input("\nSelecione o número do cliente: "))
        if escolha < 1 or escolha > len(clientes):
            print("❌ Escolha inválida.")
            return
    except ValueError:
        print("❌ Entrada inválida.")
        return

    recetor = clientes[escolha - 1][0]

    mensagem = input(f"Escreva a mensagem para {recetor}: ").strip()
    if mensagem == "":
        print("❌ A mensagem não pode estar vazia.")
        return

    cursor.execute("""
        INSERT INTO mensagens (emissor, recetor, mensagem)
        VALUES (?, ?, ?)
    """, (fornecedor_nome, recetor, mensagem))

    db.commit()
    print(f"📨 Mensagem enviada para {recetor} com sucesso!")


def ver_mensagens(db, fornecedor_nome):
    cursor = db.cursor()

    print("\n=== Mensagens Recebidas ===")

    cursor.execute("""
        SELECT emissor, mensagem, timestamp
        FROM mensagens
        WHERE recetor = ?
        ORDER BY timestamp DESC
    """, (fornecedor_nome,))

    mensagens = cursor.fetchall()

    if mensagens:
        print("\n Mensagens recebidas:")
        for m in mensagens:
            print(f"De {m[0]}: {m[1]}")
    else:
        print(" Nenhuma mensagem nova.")

#abrir um ticket quando o admin fizer login
def abrir_ticket_produto(db, fornecedor_nome):
    nome_produto = input("Nome do produto: ")
    preco = float(input("Preço sugerido: "))
    stock = int(input("Quantidade inicial: "))

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO tickets_produto (fornecedor, produto, preco, stock, status)
        VALUES (?, ?, ?, ?, ?)
    """, (fornecedor_nome, nome_produto, preco, stock, "pendente"))
    db.commit()

    print(f"✅ Ticket para '{nome_produto}' enviado ao admin.")
