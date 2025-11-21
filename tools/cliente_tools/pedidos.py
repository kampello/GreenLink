import sqlite3

def ver_pedidos(db, cliente_nome):
    cursor = db.cursor()

    # Pega o ID do cliente
    cursor.execute("SELECT id FROM utilizadores WHERE nome=?", (cliente_nome,))
    cliente = cursor.fetchone()
    if not cliente:
        print("⚠️ Cliente não encontrado.")
        return
    cliente_id = cliente[0]

    # Procurar pedidos do cliente
    cursor.execute("""
        SELECT produtos.nome, pedidos.quantidade, pedidos.estado
        FROM pedidos
        JOIN produtos ON pedidos.produto_id = produtos.id
        WHERE pedidos.cliente_id = ?
    """, (cliente_id,))
    pedidos = cursor.fetchall()

    if pedidos:
        print("\n📋 Seus pedidos:")
        for p in pedidos:
            print(f"Produto: {p[0]} | Quantidade: {p[1]} | Estado: {p[2]}")
    else:
        print("⚠️ Nenhum pedido encontrado.")

def ver_produtos_disponiveis(db):
    cursor = db.cursor()
    cursor.execute("SELECT nome, preco, stock FROM produtos WHERE stock > 0")
    produtos = cursor.fetchall()

    if produtos:
        print("\n🥦 Produtos disponíveis:")
        for p in produtos:
            print(f"{p[0]} — €{p[1]:.2f} ({p[2]} unidades em stock)")
    else:
        print("⚠️ Nenhum produto disponível no momento.")

def fazer_pedido(db, cliente_nome):
    cursor = db.cursor()
    
    cursor.execute("SELECT nome, preco, stock FROM produtos ")
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto disponível.")
        return
    
    print("\n Produto disponíveis: ")
    for nome, preco, stock in produtos:
        print(f"- {nome} | Preço: €{preco} | Stock: {stock}")
        
    produto_escolhido = input("\n Nome do produto que deseja comprar: ").strip()
    
    cursor.execute("SELECT id, stock FROM produtos WHERE nome = ?", (produto_escolhido,))
    produto = cursor.fetchone()
    
    if not produtos:
        print("Nenhum produto disponível.")
        return
    
    produto_id, stock = produto
    
    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade Inválida.")
        return
    if quantidade <= 0 or quantidade > stock:
        print("Quantidade inválida.")
        return
    elif quantidade > stock:
        print("Stock insuficiente")
        return
    
    cursor.execute("SELECT id FROM utilizadores WHERE nome = ?", (cliente_nome,))
    cliente = cursor.fetchone()
    
    if not cliente:
        print("Erro interno: cliente não encontrado.")
        return
    
    cliente_id = cliente[0]
    
    cursor.execute("""
        INSERT INTO pedidos (cliente_id, produto_id, quantidade, estado)
        VALUES (?, ?, ?, 'feito')
        """, (cliente_id, produto_id, quantidade))
    
    
    cursor.execute("UPDATE produtos SET stock = stock - ? WHERE id = ?", (quantidade, produto_id))

    db.commit()
    print(f"Pedido de {quantidade}x {produto_escolhido} realizado com sucesso.")