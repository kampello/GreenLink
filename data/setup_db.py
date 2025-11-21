import sqlite3

def resetar_banco():
    conn = sqlite3.connect("data/greenlink.db")
    cursor = conn.cursor()

    print(" A apagar tabelas antigas... ")

    # Remove todas as tabelas antigas, se existirem
    cursor.executescript("""
    DROP TABLE IF EXISTS pedidos;
    DROP TABLE IF EXISTS produtos;
    DROP TABLE IF EXISTS fornecedores;
    DROP TABLE IF EXISTS utilizadores;
    DROP TABLE IF EXISTS mensagens;
    DROP TABLE IF EXISTS tickets_produto;
    """)

    print(" A recriar estrutura de tabelas...")

    # === Tabela de utilizadores ===
    cursor.execute('''
    CREATE TABLE utilizadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        tipo TEXT CHECK(tipo IN ('admin','cliente', 'fornecedor')) NOT NULL,
        senha TEXT NOT NULL
    );
    ''')

    # === Tabela de fornecedores ===
    cursor.execute('''
    CREATE TABLE fornecedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        contacto TEXT,
        senha TEXT NOT NULL
    );
    ''')

    # === Tabela de produtos ===
    cursor.execute('''
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        stock INTEGER NOT NULL,
        fornecedor_id INTEGER NOT NULL,
        FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
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

    conn.commit()
    conn.close()

print("Base de dados criada com sucesso!")
