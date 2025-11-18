import sqlite3

conn = sqlite3.connect("data/greenlink.db")
cursor = conn.cursor()

# ==============================
# UTILIZADORES
# ==============================
cursor.executemany("""
    INSERT OR IGNORE INTO utilizadores (nome, tipo, senha)
    VALUES (?, ?, ?)
""", [
    ("admin", "admin", "1234"),
    ("paul", "cliente", "123"),
    ("camp", "fornecedor", "123")
])

# ==============================
# PRODUTOS
# ==============================
cursor.executemany("""
    INSERT OR IGNORE INTO produtos (nome, preco, stock)
    VALUES (?, ?, ?)
""", [
    ("Brócolos", 2.5, 100),
    ("Cenouras", 1.2, 200),
    ("Alfaces", 1.8, 150)
])

conn.commit()
conn.close()

print("🌱 Dados de teste inseridos com sucesso!")
