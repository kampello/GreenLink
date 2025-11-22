def exportar_relatorio_vendas(db, fornecedor_nome):
    cursor = db.cursor()

    # Pega todos os produtos (ou apenas os do fornecedor, se tiveres essa info)
    cursor.execute("SELECT id, nome FROM produtos")
    produtos = cursor.fetchall()

    total_vendas = 0
    total_receita = 0.0

    print(f"\n===== Relatório de Vendas - Fornecedor: {fornecedor_nome} =====\n")

    for produto_id, nome in produtos:
        # JOIN com produtos para pegar o preço
        cursor.execute("""
            SELECT SUM(pedidos.quantidade), SUM(pedidos.quantidade * produtos.preco)
            FROM pedidos
            JOIN produtos ON pedidos.produto_id = produtos.id
            WHERE pedidos.produto_id = ?
        """, (produto_id,))
        result = cursor.fetchone()
        qtd_vendas = result[0] if result[0] is not None else 0
        receita = result[1] if result[1] is not None else 0.0

        total_vendas += qtd_vendas
        total_receita += receita

        print(f"Produto: {nome}")
        print(f"Vendas: {qtd_vendas} pedidos")
        print(f"Receita: €{receita:.2f}")
        print("-"*30)

    print(f"Total de vendas: {total_vendas} pedidos")
    print(f"Receita total: €{total_receita:.2f}\n")
