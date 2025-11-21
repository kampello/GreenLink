import sqlite3

def inserir_dados_iniciais():
    conn = sqlite3.connect("data/greenlink.db")
    cursor = conn.cursor()

    print("📥 Inserindo dados iniciais...")

    # ================================
    #  UTILIZADORES
    # ================================
    cursor.execute("""
        INSERT INTO utilizadores (nome, tipo, senha)
        VALUES 
        ('admin', 'admin', 'admin123'),
        ('Joao', 'cliente', '1234'),
        ('Maria', 'cliente', '5678')
    """)
    
    # ================================
    #  FORNECEDORES
    # ================================
    cursor.execute("""
        INSERT INTO fornecedores (nome, contacto, senha)
        VALUES ('AgroVale', 'agrovale@mail.com', 'agro123')
    """)

    # Obter ID do fornecedor AgroVale
    cursor.execute("SELECT id FROM fornecedores WHERE nome='AgroVale'")
    fornecedor_id = cursor.fetchone()[0]

    # ================================
    #  PRODUTOS
    # ================================
    cursor.execute("""
        INSERT INTO produtos (nome, preco, stock, fornecedor_id)
        VALUES ('Tomate', 1.99, 120, ?)
    """, (fornecedor_id,))

    # === Inserir pedidos de teste ===
    cursor.execute("SELECT id FROM utilizadores WHERE nome='Joana'")
    joana_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM produtos WHERE nome='Tomates Frescos'")
    tomate_id = cursor.fetchone()[0]
    cursor.execute(
        "INSERT INTO pedidos (cliente_id, produto_id, quantidade, estado) VALUES (?, ?, ?, ?)",
        (joana_id, tomate_id, 10, "feito")
    )

    conn.commit()
    conn.close()
    print("✅ Dados iniciais inseridos com sucesso!")


if __name__ == "__main__":
    inserir_dados_iniciais()
