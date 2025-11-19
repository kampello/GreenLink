def enviar_mensagem(db, cliente_nome):
    cursor = db.cursor()

    print("\n=== Enviar Mensagem a Fornecedor ===")

    # Buscar lista de fornecedores registados
    cursor.execute("SELECT nome FROM utilizadores WHERE tipo = 'fornecedor'")
    fornecedores = cursor.fetchall()

    if not fornecedores:
        print("❌ Não existem fornecedores registados.")
        return

    print("\nFornecedores disponíveis:")
    for i, f in enumerate(fornecedores, 1):
        print(f"{i}. {f[0]}")

    try:
        escolha = int(input("\nSelecione o número do fornecedor: "))
        if escolha < 1 or escolha > len(fornecedores):
            print("❌ Escolha inválida.")
            return
    except ValueError:
        print("❌ Entrada inválida.")
        return

    recetor = fornecedores[escolha - 1][0]

    mensagem = input(f"Escreva a mensagem para {recetor}: ").strip()
    if not mensagem:
        print("❌ A mensagem não pode estar vazia.")
        return

    cursor.execute("""
        INSERT INTO mensagens (emissor, recetor, mensagem)
        VALUES (?, ?, ?)
    """, (cliente_nome, recetor, mensagem))

    db.commit()
    print(f"📨 Mensagem enviada para {recetor} com sucesso!")


def ver_mensagens(db, cliente_nome):
    cursor = db.cursor()

    print("\n=== Mensagens Recebidas ===")

    cursor.execute("""
        SELECT emissor, mensagem, timestamp
        FROM mensagens
        WHERE recetor = ?
        ORDER BY timestamp DESC
    """, (cliente_nome,))

    mensagens = cursor.fetchall()

    if mensagens:
        print("\n Mensagens recebidas:")
        for m in mensagens:
            print(f"De {m[0]}: {m[1]}")
    else:
        print(" Nenhuma mensagem nova.")