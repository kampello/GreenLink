def ver_mensagens(db, cliente_nome):
    cursor = db.cursor()

    # Obter ID do cliente
    cursor.execute("SELECT id FROM utilizadores WHERE nome = ?", (cliente_nome,))
    cliente = cursor.fetchone()
    if not cliente:
        print("⚠ Cliente não encontrado.")
        return

    cliente_id = cliente[0]

    print("\n=== 📩 Mensagens Recebidas ===\n")

    cursor.execute("""
        SELECT m.id, u.nome, m.mensagem, m.data
        FROM mensagens m
        JOIN fornecedores u
        ON m.emissor_id = u.id AND m.emissor_tipo = 'fornecedor'
        WHERE m.destinatario_id = ? AND m.destinatario_tipo = 'utilizador'
        ORDER BY m.data DESC
    """, (cliente_id,))

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
 