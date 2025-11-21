import sqlite3

def resetar_banco():
    conn = sqlite3.connect("data/greenlink.db")
    cursor = conn.cursor()

    print("🔄 A apagar tabelas antigas... ")

    # Remove todas as tabelas antigas, se existirem
    cursor.executescript("""
    DROP TABLE IF EXISTS mensagens;
    DROP TABLE IF EXISTS pedidos;
    DROP TABLE IF EXISTS produtos;
    DROP TABLE IF EXISTS fornecedores;
    DROP TABLE IF EXISTS utilizadores;
    DROP TABLE IF EXISTS mensagens;
    DROP TABLE IF EXISTS tickets_produto;
    """)


    print("🧱 A recriar estrutura de tabelas...")

    # === Tabela de utilizadores ===
    cursor.execute('''
    CREATE TABLE utilizadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        tipo TEXT CHECK(tipo IN ('admin','cliente')) NOT NULL,
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

    # === Tabela de pedidos ===
    cursor.execute('''
    CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        produto_id INTEGER,
        quantidade INTEGER,
        estado TEXT CHECK(estado IN ('feito','pago','enviado','entregue')) DEFAULT 'feito',
        FOREIGN KEY (cliente_id) REFERENCES utilizadores(id),
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    );
    ''')


    # === Tabela de tickets enviados pelos fornecedores ===
    cursor.execute('''
    CREATE TABLE tickets_produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fornecedor TEXT NOT NULL,
        produto TEXT NOT NULL,
        preco REAL NOT NULL,
        stock INTEGER NOT NULL,
        status TEXT CHECK(status IN ('pendente','feito','rejeitado')) DEFAULT 'pendente'
    );
    ''')


    # === Tabela de mensagens ===
    cursor.execute('''
    CREATE TABLE mensagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        emissor_id INTEGER NOT NULL,
        emissor_tipo TEXT CHECK(emissor_tipo IN ('utilizador','fornecedor')) NOT NULL,
        destinatario_id INTEGER NOT NULL,
        destinatario_tipo TEXT CHECK(destinatario_tipo IN ('utilizador','fornecedor')) NOT NULL,
        mensagem TEXT NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        

    );
    ''')

    conn.commit()
    conn.close()
    print("✅ Banco de dados limpo e recriado com sucesso!")


if __name__ == "__main__":
    resetar_banco()

