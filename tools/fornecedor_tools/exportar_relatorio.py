import sqlite3

def exportar_relatorio_vendas(db, fornecedor_nome):
    cursor = db.cursor()

    # Pega os produtos que o fornecedor adicionou e que foram aprovados
    cursor.execute("""
        SELECT p.id, p.nome, p.preco
        FROM produtos p
        JOIN tickets_produto t ON t.produto = p.nome
        WHERE t.fornecedor=? AND t.status='feito'
    """, (fornecedor_nome,))
    
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto encontrado para este fornecedor.")
        return

    print(f"\n===== Relatório de Vendas do fornecedor {fornecedor_nome} =====\n")
    total_vendas = 0
    total_receita = 0

    for prod_id, prod_nome, prod_preco in produtos:
        cursor.execute("""
            SELECT SUM(quantidade) FROM pedidos
            WHERE produto_id=?
        """, (prod_id,))
        quantidade = cursor.fetchone()[0] or 0
        receita = quantidade * prod_preco

        print(f"Produto: {prod_nome}")
        print(f"Vendas: {quantidade} pedidos")
        print(f"Receita: €{receita:.2f}")
        print("-"*30)

        total_vendas += quantidade
        total_receita += receita

    print(f"Total de vendas: {total_vendas} pedidos")
    print(f"Receita total: €{total_receita:.2f}")
