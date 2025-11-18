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

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fornecedor TEXT,
    produto TEXT,
    preco REAL,
    stock INTEGER,
    status TEXT DEFAULT 'pendente'
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS entregas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER,
    produto TEXT NOT NULL,
    fornecedor TEXT NOT NULL,
    supermercado TEXT NOT NULL,
    data_prevista TEXT NOT NULL,
    data_real TEXT,
    status TEXT CHECK(status IN ('no prazo', 'atrasado')),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
)
""")


print("Base de dados criada com sucesso!")
