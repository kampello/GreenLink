def enviar_mensagem(db, fornecedor_nome):
    cursor = db.cursor()

    print("\nClientes disponíveis:")
    cursor.execute("SELECT nome FROM utilizadores WHERE tipo='cliente'")
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente registado.")
        return

    for c in clientes:
        print(f"- {c[0]}")

    cliente = input("\nCliente destinatário: ").strip()

    mensagem = input("Mensagem: ")

    cursor.execute("""
        INSERT INTO mensagens (remetente, destinatario, mensagem)
        VALUES (?, ?, ?)
    """, (fornecedor_nome, cliente, mensagem))

    db.commit()
    print(f"Mensagem enviada para {cliente}!")

#ver mensagem
def ver_mensagens(db, fornecedor_nome):
    cursor = db.cursor()
    cursor.execute("""
    SELECT DISTINCT u.nome
    FROM mensagens m
    JOIN utilizadores u ON u.nome = m.remetente
    WHERE m.destinatario = ? AND u.tipo = 'cliente'
    """, (fornecedor_nome,))
    
    clientes = cursor.fetchall()
    
    if clientes:
        print("Clientes que lhe enviaram mensagem:")
        for c in clientes:
            print(f"- {c[0]}")
    else:
        print("Sem mensagens de clientes: ")
        return
    
    remetente = input("De que cliente pretende ver as mensagens?: ")
        
    cursor.execute(
        "SELECT remetente, mensagem FROM mensagens WHERE remetente = ? AND destinatario = ?",
        (remetente, fornecedor_nome)
    )
        
    mensagens = cursor.fetchall()

    if mensagens:
        print("\n Mensagens recebidas:")
        for remetente, texto in mensagens:
            print(f"• De {remetente}: {texto}")
    else:
        print("\n Nenhuma mensagem nova.")

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

    print(f"Ticket para '{nome_produto}' enviado ao admin.")
