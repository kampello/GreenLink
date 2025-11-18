from datetime import datetime

def ver_entregas(db):
    cursor = db.cursor()

    cursor.execute("""
        SELECT pedido_id, produto, fornecedor, supermercado,
               data_prevista, data_real, status
        FROM entregas
        ORDER BY data_prevista
    """)

    entregas = cursor.fetchall()

    print("\n===== Acompanhamento de Entregas =====\n")

    if not entregas:
        print("Nenhuma entrega registada ainda.")
        return

    for e in entregas:
        pedido_id, produto, fornecedor, supermercado, data_prevista, data_real, status = e

        cor = "🟢" if status == "no prazo" else "🔴"

        print(f"""
Pedido ID:      {pedido_id}
Produto:        {produto}
Fornecedor:     {fornecedor}
Supermercado:   {supermercado}
Previsto para:  {data_prevista}
Entregue em:    {data_real if data_real else "Ainda não entregue"}
Status:         {cor} {status}
---------------------------------------------
        """)
