from datetime import datetime

from datetime import datetime

def registar_entrega(db, fornecedor_nome):
    cursor = db.cursor()
    cursor.execute("""Select nome from produtos """)
    produto = cursor.fetchall()
    for p in produto:
        print(f"- {p[0]}")
    produto = input("Produto entregue: ")
    supermercado = input("Supermercado: ")
    data_prevista = input("Data prevista (YYYY-MM-DD): ")

    data_real = datetime.now().strftime("%Y-%m-%d")

    status = "no prazo" if data_real <= data_prevista else "atrasado"

    cursor.execute("""
        INSERT INTO entregas (produto, fornecedor, supermercado, data_prevista, data_real, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (produto, fornecedor_nome, supermercado, data_prevista, data_real, status))

    db.commit()

    entrega_id = cursor.lastrowid  # pega o ID autoincrementado
  
    print(f"Entrega registada com sucesso! ID da entrega: {entrega_id} ({status}).")
