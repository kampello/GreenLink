def ver_stock(db, fornecedor_nome):
    cursor = db.cursor()

    # Descobre se a tabela tem coluna 'preco'
    cursor.execute("PRAGMA table_info(produtos)")
    colunas = [c[1] for c in cursor.fetchall()]
    tem_preco = 'preco' in colunas

    # Busca produtos do fornecedor
    query = f"""
        SELECT p.nome, p.stock, p.preco
        FROM produtos p
        JOIN fornecedores f ON p.fornecedor_id = f.id
        WHERE f.nome = ?
    """ if tem_preco else f"""
        SELECT p.nome, p.stock
        FROM produtos p
        JOIN fornecedores f ON p.fornecedor_id = f.id
        WHERE f.nome = ?
    """
    cursor.execute(query, (fornecedor_nome,))
    produtos = cursor.fetchall()

    if not produtos:
        print(" Nenhum produto registado para este fornecedor.")
        return

    # Cálculo automático da largura de cada coluna
    max_nome = max(len(p[0]) for p in produtos)
    max_stock = max(len(str(p[1])) for p in produtos)
    max_preco = max(len(f"{p[2]:.2f}") for p in produtos) if tem_preco else 0

    print("\n Stock atual:\n")

    # Cabeçalho
    if tem_preco:
        print(f"{'Produto':<{max_nome}} | {'Stock':>{max_stock}} | {'Preço (€)':>{max_preco + 3}}")
        print("-" * (max_nome + max_stock + max_preco + 10))
    else:
        print(f"{'Produto':<{max_nome}} | {'Stock':>{max_stock}}")
        print("-" * (max_nome + max_stock + 5))

    # Linhas da tabela
    for p in produtos:
        nome = p[0].ljust(max_nome)
        stock = str(p[1]).rjust(max_stock)
        if tem_preco:
            preco = f"{p[2]:.2f}".rjust(max_preco + 3)
            print(f"{nome} | {stock} | {preco}")
        else:
            print(f"{nome} | {stock}")


def atualizar_stock(db, fornecedor_nome):
    cursor = db.cursor()
    produto = input("Nome do produto: ").strip()

    # Verifica se o produto existe e pertence a este fornecedor
    cursor.execute("""
        SELECT p.id, p.stock
        FROM produtos p
        JOIN fornecedores f ON p.fornecedor_id = f.id
        WHERE p.nome = ? AND f.nome = ?
    """, (produto, fornecedor_nome))
    resultado = cursor.fetchone()

    if resultado:
        novo_stock = int(input("Novo stock: "))
        cursor.execute("UPDATE produtos SET stock = ? WHERE id = ?", (novo_stock, resultado[0]))
        print(f" Stock de '{produto}' atualizado para {novo_stock}.")
    else:
        print("Produto não encontrado. Criar novo produto:")
        stock = int(input("Stock inicial: "))
        preco = float(input("Preço (€): "))
        # Obter id do fornecedor
        cursor.execute("SELECT id FROM fornecedores WHERE nome = ?", (fornecedor_nome,))
        fornecedor_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO produtos (nome, stock, preco, fornecedor_id) VALUES (?, ?, ?, ?)",
            (produto, stock, preco, fornecedor_id)
        )
        print(f" Produto '{produto}' adicionado com {stock} unidades para {fornecedor_nome}.")

    db.commit()
