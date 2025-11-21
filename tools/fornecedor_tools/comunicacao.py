import sqlite3

def enviar_mensagem(db, nome_fornecedor):
    cursor = db.cursor()

    # Obter ID do fornecedor
    cursor.execute("SELECT id FROM fornecedores WHERE nome = ?", (nome_fornecedor,))
    fornecedor = cursor.fetchone()

    if not fornecedor:
        print("⚠ Erro: fornecedor não encontrado.")
        return

    fornecedor_id = fornecedor[0]

    # Escolher destinatário
    print("\n=== Enviar Mensagem ===")
    print("1. Enviar para Cliente")
    print("2. Enviar para Admin")
    opcao = input("Escolha a opção: ")

    if opcao not in ["1", "2"]:
        print("Opção inválida.")
        return

    # Listar utilizadores para escolher
    cursor.execute("SELECT id, nome, tipo FROM utilizadores")
    utilizadores = cursor.fetchall()

    print("\n--- Utilizadores disponíveis ---")
    for uid, nome, tipo in utilizadores:
        print(f"{uid} - {nome} ({tipo})")

    try:
        destinatario_id = int(input("ID do destinatário: "))
    except ValueError:
        print("ID inválido.")
        return

    # Verificar se existe
    cursor.execute("SELECT id, nome FROM utilizadores WHERE id = ?", (destinatario_id,))
    recebe = cursor.fetchone()

    if not recebe:
        print("⚠ Destinatário não encontrado.")
        return

    mensagem = input("Digite a mensagem: ")

    cursor.execute("""
        INSERT INTO mensagens (emissor_id, emissor_tipo, destinatario_id, destinatario_tipo, mensagem)
        VALUES (?, 'fornecedor', ?, 'utilizador', ?)
    """, (fornecedor_id, destinatario_id, mensagem))

    db.commit()
    print("✔ Mensagem enviada com sucesso!")


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


