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

    for e in entregas:
        status = "🟢 No prazo" if e[6] == "no prazo" else "🔴 Atrasado"

        print(f"""
Pedido ID:      {e[0]}
Produto:        {e[1]}
Fornecedor:     {e[2]}
Supermercado:   {e[3]}
Previsto para:  {e[4]}
Entregue em:    {e[5]}
Status:         {status}
---------------------------------------------
        """)
