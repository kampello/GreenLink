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
