def enviar_mensagem(db, cliente_nome):

    """
    Envia uma mensagem de um cliente para um fornecedor.

    :param db: Conexão com a base de dados.
    :type db: sqlite3.Connection
    :param cliente_nome: Nome do cliente remetente.
    :type cliente_nome: str
    """

    cursor = db.cursor()
    
    print("\nFornecedores disponíveis: ")
    cursor.execute("SELECT nome FROM utilizadores WHERE tipo='fornecedor'")
    fornecedores = cursor.fetchall()
    
    if not fornecedores:
        print("Nenhum fornecedor registado.")
        return
    
    for f in fornecedores:
        print(f"- {f[0]}")
        
    fornecedor = input("Fornecedor destinatário: ").strip()
    
    mensagem = input("Mensagem: ")

    cursor.execute("""
        INSERT INTO mensagens (remetente, destinatario, mensagem)
        VALUES (?, ?, ?)
    """, (cliente_nome, fornecedor, mensagem))
    
    db.commit()
    print(f" Mensagem enviada para {fornecedor}!")

def ver_mensagens(db, cliente_nome):

    """
    Mostra mensagens recebidas de fornecedores e permite selecionar um remetente.

    :param db: Conexão com a base de dados.
    :type db: sqlite3.Connection
    :param cliente_nome: Nome do cliente destinatário.
    :type cliente_nome: str
    """

    cursor = db.cursor()
    
    cursor.execute("""
    SELECT DISTINCT u.nome
    FROM mensagens m
    JOIN utilizadores u ON u.nome = m.remetente
    WHERE m.destinatario = ? AND u.tipo = 'fornecedor'
    """, (cliente_nome,))
    fornecedores = cursor.fetchall()
    
    if fornecedores:
        print("Fornecedores que lhe enviaram mensagem: ")
        for f in fornecedores:
            print(f"- {f[0]}")
    else:
        print("Sem mensagens de fornecedores:")
        return
    
            
    remetente = input("De que fornecedor pretende ver as mensagens?: ")
    
    cursor.execute(
        "SELECT remetente, mensagem FROM mensagens WHERE remetente = ? AND destinatario = ?",
        (remetente, cliente_nome)
    )
    mensagens = cursor.fetchall()

    if mensagens:
        print("\n Mensagens recebidas:")
        for remetente, texto in mensagens:
            print(f"De {remetente}: {texto}")
    else:
        print(" Nenhuma mensagem nova.")