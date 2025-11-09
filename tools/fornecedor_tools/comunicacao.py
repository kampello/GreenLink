def enviar_mensagem(db, fornecedor_nome):
    cliente = input("Cliente destinatário: ")
    mensagem = input("Mensagem: ")

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO mensagens (remetente, destinatario, conteudo) VALUES (?, ?, ?)",
        (fornecedor_nome, cliente, mensagem)
    )
    db.commit()
    print(f"Mensagem enviada para {cliente}!")

def ver_mensagens(db, fornecedor_nome):
    cursor = db.cursor()
    cursor.execute(
        "SELECT remetente, conteudo FROM mensagens WHERE destinatario = ?",
        (fornecedor_nome,)
    )
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
