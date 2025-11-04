def ver_stock(db):
    cursor = db.cursor()
    cursor.execute("SELECT nome, stock FROM produtos")
    produtos = cursor.fetchall()

    if produtos:
        print("\n Stock atual:")
        for p in produtos:
            print(f"{p[0]} — {p[1]} unidades")
    else:
        print(" Nenhum produto registado.")

def atualizar_stock(db):
    nome = input(" Nome do produto a atualizar: ")
    novo_stock = int(input("Novo valor de stock: "))

    cursor = db.cursor()
    cursor.execute("UPDATE produtos SET stock = ? WHERE nome = ?", (novo_stock, nome))
    db.commit()

    if cursor.rowcount > 0:
        print(f" Stock do produto '{nome}' atualizado para {novo_stock}.")
    else:
        print(" Produto não encontrado.")

def ver_pedidos_recebidos(db, fornecedor_nome):
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, cliente, produto, quantidade, estado FROM pedidos WHERE fornecedor = ?",
        (fornecedor_nome,)
    )
    pedidos = cursor.fetchall()

    if pedidos:
        print("\n Pedidos recebidos:")
        for p in pedidos:
            print(f"ID: {p[0]} | Cliente: {p[1]} | Produto: {p[2]} | Quantidade: {p[3]} | Estado: {p[4]}")
    else:
        print(" Nenhum pedido recebido.")
