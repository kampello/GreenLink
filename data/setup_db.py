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
CREATE TABLE tickets_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fornecedor TEXT,
    produto TEXT,
    preco REAL,
    stock INTEGER,
    status TEXT DEFAULT 'pendente'
);

''')
print("Base de dados criada com sucesso!")
