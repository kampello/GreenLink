from datetime import datetime

def registar_entrega(db, fornecedor_nome):
    cursor = db.cursor()

    pedido_id = input("ID do pedido entregue: ")
    produto = input("Produto entregue: ")
    supermercado = input("Supermercado: ")
    data_prevista = input("Data prevista (YYYY-MM-DD): ")

    data_real = datetime.now().strftime("%Y-%m-%d")

    # comparar datas
    status = "no prazo"
    if data_real > data_prevista:
        status = "atrasado"

    cursor.execute("""
        INSERT INTO entregas (pedido_id, produto, fornecedor, supermercado, data_prevista, data_real, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (pedido_id, produto, fornecedor_nome, supermercado, data_prevista, data_real, status))

    db.commit()

    print(f"Entrega do produto '{produto}' registada com sucesso ({status}).")
