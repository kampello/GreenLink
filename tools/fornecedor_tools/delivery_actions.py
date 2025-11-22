from datetime import datetime

from datetime import datetime

def registar_entrega(db, fornecedor_nome):
    cursor = db.cursor()

    cursor.execute("SELECT nome FROM produtos")
    # transformar em lista de strings e normalizar espaços
    produtos = [p[0].strip() for p in cursor.fetchall()]

    print("Produtos disponíveis:")
    for p in produtos:
        print(f"- {p}")

    # loop de verificação (case-insensitive)
    while True:
        produto = input("Produto entregue: ").strip()
        # comparar sem diferenciar maiúsculas/minúsculas
        if produto.lower() in (x.lower() for x in produtos):
            print(f"✔ Produto selecionado: {produto}")
            break
        else:
            print("Esse produto não está listado. Abra um ticket se quiser que seja adicionado!\n")


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
