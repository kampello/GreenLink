import sqlite3

def ver_pedidos(db, cliente_nome):

    """
    Mostra todos os pedidos de um cliente.

    :param db: Conexão com a base de dados.
    :type db: sqlite3.Connection
    :param cliente_nome: Nome do cliente.
    :type cliente_nome: str
    """


    cursor = db.cursor()
    cursor.execute(
        "SELECT id, produto, quantidade, estado FROM pedidos WHERE cliente = ?",
        (cliente_nome,)
    )
    pedidos = cursor.fetchall()

    if pedidos:
        print("\n📋 Seus pedidos:")
        for p in pedidos:
            print(f"ID: {p[0]} | Produto: {p[1]} | Quantidade: {p[2]} | Estado: {p[3]}")
    else:
        print("⚠️ Nenhum pedido encontrado.")

def ver_produtos_disponiveis(db):

    """
    Lista todos os produtos com stock disponível.

    :param db: Conexão com a base de dados.
    :type db: sqlite3.Connection
    """

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

    """
    Permite a um cliente criar um novo pedido se houver stock suficiente.

    :param db: Conexão com a base de dados.
    :type db: sqlite3.Connection
    :param cliente_nome: Nome do cliente que vai fazer o pedido.
    :type cliente_nome: str
    """

    produto = input("Nome do produto que deseja comprar: ")
    quantidade = int(input("Quantidade: "))

    cursor = db.cursor()
    cursor.execute("SELECT stock FROM produtos WHERE nome = ?", (produto,))
    resultado = cursor.fetchone()

    if resultado and resultado[0] >= quantidade:
        cursor.execute(
            "INSERT INTO pedidos (cliente, produto, quantidade, estado) VALUES (?, ?, ?, ?)",
            (cliente_nome, produto, quantidade, "pendente")
        )
        db.commit()
        print(f"✅ Pedido do produto '{produto}' criado com sucesso!")
    else:
        print("❌ Produto inexistente ou stock insuficiente.")