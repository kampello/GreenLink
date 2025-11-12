import sqlite3

conn = sqlite3.connect("data/greenlink.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS utilizadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('admin','cliente','fornecedor')) NOT NULL,
    senha TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    stock INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    estado TEXT CHECK(estado IN ('feito','pago','enviado','entregue')) DEFAULT 'feito',
    FOREIGN KEY (cliente_id) REFERENCES utilizadores(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
''')
cursor.execute('''
def verificar_tickets_pendentes(db):
    cursor = db.cursor()
    cursor.execute("SELECT id, fornecedor, produto, preco, stock FROM tickets_produto WHERE status='pendente'")
    tickets = cursor.fetchall()

    if tickets:
        print("\n📌 Tickets pendentes de aprovação:")
        for t in tickets:
            print(f"ID: {t[0]} | Fornecedor: {t[1]} | Produto: {t[2]} | Preço: €{t[3]:.2f} | Stock: {t[4]}")
        print("Aguarda aprovação do admin...\n")
    else:
        print(" Nenhum ticket pendente no momento.")

conn.commit()
conn.close()
''')
print("Base de dados criada com sucesso!")
