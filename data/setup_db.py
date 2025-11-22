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

cursor.execute('''
CREATE TABLE IF NOT EXISTS objetivos_mensais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes TEXT,
    objetivo_producao REAL,
    objetivo_vendas REAL,
    objetivo_receita REAL,
    realizado_producao REAL DEFAULT 0,
    realizado_vendas REAL DEFAULT 0,
    realizado_receita REAL DEFAULT 0
);
''')

cursor.execute('''
    CREATE TABLE mensagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        remetente VARCHAR(255) NOT NULL,
        destinatario VARCHAR(255) NOT NULL,
        mensagem TEXT NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

print("Base de dados criada com sucesso!")
