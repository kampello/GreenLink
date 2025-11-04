def ver_stock(db):
    cursor = db.cursor()

    # Descobre as colunas da tabela "produtos"
    cursor.execute("PRAGMA table_info(produtos)")
    colunas = [c[1] for c in cursor.fetchall()]
    tem_preco = 'preco' in colunas

    # Busca produtos
    if tem_preco:
        cursor.execute("SELECT nome, stock, preco FROM produtos")
    else:
        cursor.execute("SELECT nome, stock FROM produtos")

    produtos = cursor.fetchall()

    if not produtos:
        print(" Nenhum produto registado.")
        return

    # Cálculo automático da largura de cada coluna
    max_nome = max(len(p[0]) for p in produtos)
    max_stock = max(len(str(p[1])) for p in produtos)
    if tem_preco:
        max_preco = max(len(f"{p[2]:.2f}") for p in produtos)
    else:
        max_preco = 0

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


def atualizar_stock(db):
    cursor = db.cursor()
    produto = input("Nome do produto: ").strip()

    # Verifica se o produto existe
    cursor.execute("SELECT id, stock FROM produtos WHERE nome = ?", (produto,))
    resultado = cursor.fetchone()

    if resultado:
        novo_stock = int(input("Novo stock: "))
        cursor.execute("UPDATE produtos SET stock = ? WHERE id = ?", (novo_stock, resultado[0]))
        print(f" Stock de '{produto}' atualizado para {novo_stock}.")
    else:
        print("Produto não encontrado. Criar novo produto:")
        stock = int(input("Stock inicial: "))
        try:
            preco = float(input("Preço (€): "))
            cursor.execute("INSERT INTO produtos (nome, stock, preco) VALUES (?, ?, ?)", (produto, stock, preco))
        except Exception:
            cursor.execute("INSERT INTO produtos (nome, stock) VALUES (?, ?)", (produto, stock))
        print(f" Produto '{produto}' adicionado com {stock} unidades.")

    db.commit()


def ver_pedidos_recebidos(db, fornecedor):
    # Placeholder — ainda por implementar
    print("→ Função ver_pedidos_recebidos() ainda não implementada.")
