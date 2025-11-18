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

conn.commit()
conn.close()

print("🌱 Dados de teste inseridos com sucesso!")
