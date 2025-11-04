def enviar_mensagem(db, cliente_nome):
    fornecedor = input("Fornecedor destinatário: ")
    mensagem = input("Mensagem: ")

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO mensagens (remetente, destinatario, conteudo) VALUES (?, ?, ?)",
        (cliente_nome, fornecedor, mensagem)
    )
    db.commit()
    print(f"📨 Mensagem enviada para {fornecedor}!")

def ver_mensagens(db, cliente_nome):
    cursor = db.cursor()
    cursor.execute(
        "SELECT remetente, conteudo FROM mensagens WHERE destinatario = ?",
        (cliente_nome,)
    )
    mensagens = cursor.fetchall()

    if mensagens:
        print("\n💬 Mensagens recebidas:")
        for m in mensagens:
            print(f"De {m[0]}: {m[1]}")
    else:
        print("📭 Nenhuma mensagem nova.")