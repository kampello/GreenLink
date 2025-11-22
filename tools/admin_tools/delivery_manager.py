from datetime import datetime

def ver_entregas(db):
    """
    Lista de todas as entregas registradas, exibindo datas previstas, datas reais e estado.
    :param db: Conexão ativa para a base de dados SQLite.
    :type db: sqlite3.Connection
    :returns: Nada. Imprime no stdout o acompanhamento completo das entregas.
    :rtype: None
    Esta função recupera todos os registros da tabela ``entregas`` e exibe:
    - produto
    - fornecedor
    - supermercado
    - data prevista
    - data real (se houver)
    - estado da entrega (com um indicador visual, entre outras coisas)
    """
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

