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

    # Listar todos os destinatários disponíveis (clientes e admins)
    cursor.execute("SELECT id, nome, tipo FROM utilizadores")
    destinatarios = cursor.fetchall()

    if not destinatarios:
        print("Nenhum destinatário disponível.")
        return

    print("\n--- Destinatários disponíveis ---")
    for uid, nome, tipo in destinatarios:
        print(f"{uid} - {nome} ({tipo})")

    try:
        destinatario_id = int(input("\nDigite o ID do destinatário: "))
    except ValueError:
        print("ID inválido.")
        return

    # Verificar se o ID existe
    cursor.execute("SELECT id, nome, tipo FROM utilizadores WHERE id = ?", (destinatario_id,))
    recebe = cursor.fetchone()
    if not recebe:
        print("⚠ Destinatário não encontrado.")
        return

    mensagem = input("Digite a mensagem: ")

    # Inserir no banco
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

        
def abrir_ticket_produto(db, nome_fornecedor):
    cursor = db.cursor()

    # Obter ID do fornecedor
    cursor.execute("SELECT id FROM fornecedores WHERE nome = ?", (nome_fornecedor,))
    fornecedor = cursor.fetchone()
    if not fornecedor:
        print("⚠ Fornecedor não encontrado.")
        return

    fornecedor_id = fornecedor[0]

    print("\n=== Abrir Ticket para Novo Produto ===")
    nome_produto = input("Nome do produto: ").strip()
    try:
        preco = float(input("Preço (€): "))
    except ValueError:
        print("Preço inválido.")
        return
    try:
        stock = int(input("Stock inicial: "))
    except ValueError:
        print("Stock inválido.")
        return

    # Obter todos os admins para enviar a mensagem
    cursor.execute("SELECT id, nome FROM utilizadores WHERE tipo='admin'")
    admins = cursor.fetchall()
    if not admins:
        print("⚠ Nenhum admin encontrado para receber o ticket.")
        return

    print("\nAdmins disponíveis para receber o ticket:")
    for aid, nome in admins:
        print(f"{aid} - {nome}")

    try:
        admin_id = int(input("Escolha o ID do admin destinatário: "))
    except ValueError:
        print("ID inválido.")
        return

    cursor.execute("SELECT id FROM utilizadores WHERE id=? AND tipo='admin'", (admin_id,))
    if not cursor.fetchone():
        print("Admin não encontrado.")
        return

    # Criar mensagem/ticket
    mensagem = f"Solicitação de novo produto:\nNome: {nome_produto}\nPreço: {preco:.2f}€\nStock: {stock}"

    cursor.execute("""
        INSERT INTO mensagens (emissor_id, emissor_tipo, destinatario_id, destinatario_tipo, mensagem)
        VALUES (?, 'fornecedor', ?, 'utilizador', ?)
    """, (fornecedor_id, admin_id, mensagem))

    db.commit()
    print("✔ Ticket enviado com sucesso para o admin!")

