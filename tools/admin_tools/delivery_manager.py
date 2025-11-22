from datetime import datetime

def ver_entregas(db):
    cursor = db.cursor()

    cursor.execute("""
        SELECT 
            id,             -- ID da entrega (autoincremento)
            produto,
            fornecedor,
            supermercado,
            data_prevista,
            data_real,
            status
        FROM entregas
        ORDER BY date(data_prevista) ASC
    """)

    entregas = cursor.fetchall()

    print("\n===== Acompanhamento de Entregas =====\n")

    if not entregas:
        print("Nenhuma entrega registada ainda.")
        return

    for entrega in entregas:
        entrega_id, produto, fornecedor, supermercado, data_prevista, data_real, status = entrega

        # cor de status
        cor = "🟢" if status == "no prazo" else "🔴"

        print(f"""
Entrega ID:     {entrega_id}
Produto:        {produto}
Fornecedor:     {fornecedor}
Supermercado:   {supermercado}
Previsto para:  {data_prevista}
Entregue em:    {data_real if data_real else "Ainda não entregue"}
Status:         {cor} {status}
---------------------------------------------
        """)

