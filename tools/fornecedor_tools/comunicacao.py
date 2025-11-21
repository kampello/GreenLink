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

def ver_mensagens(db, nome_fornecedor):
    cursor = db.cursor()

    # Obter ID do fornecedor
    cursor.execute("SELECT id FROM fornecedores WHERE nome = ?", (nome_fornecedor,))
    fornecedor = cursor.fetchone()

    if not fornecedor:
        print("⚠ Erro: fornecedor não encontrado.")
        return

    fornecedor_id = fornecedor[0]

    print("\n=== 📩 Mensagens Recebidas ===\n")

    cursor.execute("""
        SELECT m.id, u.nome, m.mensagem, m.data
        FROM mensagens m
        JOIN utilizadores u
        ON m.emissor_id = u.id AND m.emissor_tipo = 'utilizador'
        WHERE m.destinatario_id = ? AND m.destinatario_tipo = 'fornecedor'
        ORDER BY m.data DESC
    """, (fornecedor_id,))

    mensagens = cursor.fetchall()

    if not mensagens:
        print("Nenhuma mensagem recebida.")
        return

    for mid, nome, msg, data in mensagens:
        print(f"📨 Mensagem #{mid}")
        print(f"👤 De: {nome}")
        print(f"📅 Data: {data}")
        print(f"💬 Conteúdo: {msg}")
        print("-" * 40)