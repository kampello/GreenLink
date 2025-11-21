import sqlite3

def inserir_dados_teste():
    conn = sqlite3.connect("data/greenlink.db")
    cursor = conn.cursor()

    print("🌿 Inserindo dados de teste...")

    # === Inserir utilizadores (admins e clientes) ===
    utilizadores = [
        ("AdminMaster", "admin", "1234"),
        ("Joana", "cliente", "joana123"),
        ("Carlos", "cliente", "carlos123"),
    ]
    cursor.executemany(
        "INSERT INTO utilizadores (nome, tipo, senha) VALUES (?, ?, ?)",
        utilizadores
    )

    # === Inserir fornecedores ===
    fornecedores = [
        ("HortaVerde", "horta@greenlink.pt", "horta123"),
        ("AgroVale", "agro@greenlink.pt", "agro123"),
        ("CampoDourado", "campo@greenlink.pt", "campo123"),
    ]
    cursor.executemany(
        "INSERT INTO fornecedores (nome, contacto, senha) VALUES (?, ?, ?)",
        fornecedores
    )

    # Obter IDs dos fornecedores
    cursor.execute("SELECT id, nome FROM fornecedores")
    fornecedores_dict = {nome: fid for fid, nome in cursor.fetchall()}

    # === Inserir produtos por fornecedor ===
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

    # === Inserir pedidos de teste ===
    cursor.execute("SELECT id FROM utilizadores WHERE nome='Joana'")
    joana_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM produtos WHERE nome='Tomates Frescos'")
    tomate_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO pedidos (cliente_id, produto_id, quantidade, estado) VALUES (?, ?, ?, ?)",
        (joana_id, tomate_id, 10, "feito")
    )

    # === Inserir mensagens de teste ===

    # Mensagem: Cliente Joana → Fornecedor AgroVale
    agrovale_id = fornecedores_dict["AgroVale"]
    cursor.execute(
        """INSERT INTO mensagens (emissor_id, emissor_tipo, destinatario_id, destinatario_tipo, mensagem)
           VALUES (?, 'utilizador', ?, 'fornecedor', ?)""",
        (joana_id, agrovale_id, "Olá AgroVale, gostaria de saber quando chegam mais cenouras!")
    )

    # Mensagem: AdminMaster → Fornecedor AgroVale
    cursor.execute("SELECT id FROM utilizadores WHERE nome='AdminMaster'")
    admin_id = cursor.fetchone()[0]

    cursor.execute(
        """INSERT INTO mensagens (emissor_id, emissor_tipo, destinatario_id, destinatario_tipo, mensagem)
           VALUES (?, 'utilizador', ?, 'fornecedor', ?)""",
        (admin_id, agrovale_id, "AgroVale, verifiquem o stock dos produtos por favor.")
    )

    conn.commit()
    conn.close()
    print("✅ Dados de teste inseridos com sucesso!")


if __name__ == "__main__":
    inserir_dados_teste()
