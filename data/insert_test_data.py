import sqlite3

def inserir_dados_iniciais():
    conn = sqlite3.connect("data/greenlink.db")
    cursor = conn.cursor()

    print("📥 Inserindo dados iniciais...")

    # ================================
    #  UTILIZADORES
    # ================================
    cursor.executemany("""
        INSERT INTO utilizadores (nome, tipo, senha)
        VALUES (?, ?, ?)
    """, [
        ('AdminMaster', 'admin', '1234'),
        ('Joana', 'cliente', 'joana123'),
        ('Carlos', 'cliente', 'carlos123')
    ])

    # ================================
    #  FORNECEDORES
    # ================================
    cursor.executemany("""
        INSERT INTO fornecedores (nome, contacto, senha)
        VALUES (?, ?, ?)
    """, [
        ('HortaVerde', 'horta@greenlink.pt', 'horta123'),
        ('AgroVale', 'agro@greenlink.pt', 'agro123'),
        ('CampoDourado', 'campo@greenlink.pt', 'campo123')
    ])

    # Obter IDs dos fornecedores
    cursor.execute("SELECT id, nome FROM fornecedores")
    fornecedores_dict = {nome: fid for fid, nome in cursor.fetchall()}

    # ================================
    #  PRODUTOS
    # ================================
    produtos = [
        ("Tomates Frescos", 2.50, 120, fornecedores_dict["HortaVerde"]),
        ("Alfaces", 1.80, 85, fornecedores_dict["HortaVerde"]),
        ("Cenouras Doces", 1.20, 150, fornecedores_dict["AgroVale"]),
        ("Batatas Douradas", 2.00, 200, fornecedores_dict["AgroVale"]),
        ("Cebolas Roxas", 1.75, 95, fornecedores_dict["CampoDourado"]),
    ]
    cursor.executemany(
        "INSERT INTO produtos (nome, preco, stock, fornecedor_id) VALUES (?, ?, ?, ?)",
        produtos
    )

    # ================================
    #  PEDIDOS DE TESTE
    # ================================
    cursor.execute("SELECT id FROM utilizadores WHERE nome='Joana'")
    joana_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM produtos WHERE nome='Cenouras Doces'")
    cenoura_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO pedidos (cliente_id, produto_id, quantidade, estado) VALUES (?, ?, ?, ?)",
        (joana_id, cenoura_id, 10, "feito")
    )

    # ================================
    #  MENSAGENS DE TESTE
    # ================================
    agrovale_id = fornecedores_dict["AgroVale"]

    # Joana → AgroVale
    cursor.execute(
        """INSERT INTO mensagens (emissor_id, emissor_tipo, destinatario_id, destinatario_tipo, mensagem)
           VALUES (?, 'utilizador', ?, 'fornecedor', ?)""",
        (joana_id, agrovale_id, "Olá AgroVale, gostaria de saber quando chegam mais cenouras!")
    )

    # AdminMaster → AgroVale
    cursor.execute("SELECT id FROM utilizadores WHERE nome='AdminMaster'")
    admin_id = cursor.fetchone()[0]

    cursor.execute(
        """INSERT INTO mensagens (emissor_id, emissor_tipo, destinatario_id, destinatario_tipo, mensagem)
           VALUES (?, 'utilizador', ?, 'fornecedor', ?)""",
        (admin_id, agrovale_id, "AgroVale, verifiquem o stock dos produtos por favor.")
    )

    conn.commit()
    conn.close()
    print("✅ Dados iniciais inseridos com sucesso!")

if __name__ == "__main__":
    inserir_dados_iniciais()
