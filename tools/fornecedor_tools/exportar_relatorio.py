import csv
from datetime import datetime

def exportar_relatorio_vendas(db, fornecedor_nome):
    cursor = db.cursor()

    # Pega ID do fornecedor
    cursor.execute("SELECT id FROM utilizadores WHERE nome=? AND tipo='fornecedor'", (fornecedor_nome,))
    fornecedor = cursor.fetchone()

    if not fornecedor:
        print("Fornecedor não encontrado.")
        return

    fornecedor_id = fornecedor[0]

    # Pega produtos do fornecedor
    cursor.execute("SELECT id, nome FROM produtos WHERE fornecedor_id=?", (fornecedor_id,))
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto associado a este fornecedor.")
        return

    produto_ids = [p[0] for p in produtos]

    # Busca pedidos relacionados
    cursor.execute(f"""
        SELECT pedidos.id, produtos.nome, pedidos.quantidade, pedidos.estado
        FROM pedidos
        JOIN produtos ON produtos.id = pedidos.produto_id
        WHERE produto_id IN ({','.join('?'*len(produto_ids))})
    """, produto_ids)

    vendas = cursor.fetchall()

    # Criar ficheiro CSV
    filename = f"relatorio_vendas_{fornecedor_nome}_{datetime.now().strftime('%Y%m%d')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID Pedido", "Produto", "Quantidade", "Estado"])

        for v in vendas:
            writer.writerow(v)

    print(f"📄 Relatório exportado: {filename}")
