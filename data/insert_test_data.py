import sqlite3

conn = sqlite3.connect("data/greenlink.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO utilizadores (nome, tipo, senha) VALUES (?, ?, ?)", [
    ("admin", "admin", "1234"),
    ("paul", "cliente", "123"),
    ("camp", "fornecedor", "123")
])

cursor.executemany("INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)", [
    ("Brócolos", 2.5, 100),
    ("Cenouras", 1.2, 200),
    ("Alfaces", 1.8, 150)
])

# --- Inserir tickets de produto (aprovados ou pendentes) ---
tickets = [
    ("camp", "Brócolos", 2.5, 50, "feito"),
    ("camp", "Tomates", 3.0, 80, "pendente"),
]
cursor.executemany("INSERT INTO tickets_produto (fornecedor, produto, preco, stock, status) VALUES (?, ?, ?, ?, ?)", tickets)

# --- Inserir pedidos (cliente comprando produtos) ---
pedidos = [
    (2, 1, 10, "feito"),   # paul comprou 10 Brócolos
    (2, 3, 5, "feito")     # paul comprou 5 Alfaces
]
cursor.executemany("INSERT INTO pedidos (cliente_id, produto_id, quantidade, estado) VALUES (?, ?, ?, ?)", pedidos)

conn.commit()
conn.close()

print("🌱 Dados de teste inseridos com sucesso!")
