def enviar_mensagem(db, cliente_nome):
    cursor = db.cursor()
    
    print("\nFornecedores disponíveis: ")
    cursor.execute("SELECT nome FROM utilizadores WHERE tipo='fornecedor'")
    fornecedores = cursor.fetchall()
    
    if not fornecedores:
        print("Nenhum fornecedor registado.")
        return
    
    for f in fornecedores:
        print(f"- {c[0]}")
        
    fornecedor = input("Fornecedor destinatário: ").strip()
    
    mensagem = input("Mensagem: ")

    cursor.execute("""
        INSERT INTO mensagens (remetente, destinatario, mensagem)
        VALUES (?, ?, ?)
    """, (cliente_nome, fornecedor, mensagem))
    
    db.commit()
    print(f" Mensagem enviada para {fornecedor}!")

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