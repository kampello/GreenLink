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

    # ================================
    #  MENSAGENS (Cliente → Fornecedor)
    # ================================
    cursor.execute("""
        INSERT INTO mensagens (emissor, recetor, mensagem)
        VALUES ('Joao', 'AgroVale', 'Olá AgroVale, gostaria de saber se têm tomates disponíveis para entrega amanhã.');
    """)

    conn.commit()
    conn.close()
    print("✅ Dados iniciais inseridos com sucesso!")


if __name__ == "__main__":
    inserir_dados_iniciais()
