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

    if not mensagens:
        print("📭 Nenhuma mensagem recebida.")
        return

    for m in mensagens:
        emissor, texto, tempo = m
        print("\n-------------------------")
        print(f"De: {emissor}")
        print(f"Hora: {tempo}")
        print(f"Mensagem: {texto}")
        print("-------------------------")
