from datetime import datetime

from datetime import datetime

def registar_entrega(db, fornecedor_nome):

    """
    Regista uma entrega de produto feita por um fornecedor.

    Solicita ao fornecedor o produto entregue, o supermercado, a data prevista
    e calcula automaticamente a data real e o status da entrega (no prazo ou atrasado).

    :param db: Conexão com a base de dados.
    :type db: sqlite3.Connection
    :param fornecedor_nome: Nome do fornecedor que realiza a entrega.
    :type fornecedor_nome: str
    """

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
