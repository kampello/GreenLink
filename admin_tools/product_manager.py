import sqlite3

def adicionar_produto(db):
    nome = input("Nome do produto: ")
    preco = float(input("Preço (€): "))
    stock = int(input("Quantidade em stock: "))

    try:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)",
            (nome, preco, stock)
        )
        db.commit()
        print(f" Produto '{nome}' adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f" Erro ao adicionar produto: {e}")

def remover_produto(db):
    nome = input("Nome do produto a remover: ")
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
    db.commit()

    if cursor.rowcount > 0:
        print(f" Produto '{nome}' removido.")
    else:
        print(" Produto não encontrado.")

def ver_stock(db):
    cursor = db.cursor()
    cursor.execute("SELECT nome, stock FROM produtos")
    produtos = cursor.fetchall()

    if produtos:
        print("\n Stock Atual:")
        for p in produtos:
            print(f"{p[0]} — {p[1]} unidades")
    else:
        print(" Nenhum produto registado.")

def ver_informacoes_produtos(db):
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, preco, stock FROM produtos")
    produtos = cursor.fetchall()

    if produtos:
        print("\n Lista de Produtos:")
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Preço: €{p[2]:.2f} | Stock: {p[3]}")
    else:
        print("Nenhum produto encontrado.")
