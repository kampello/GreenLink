# tools/admin_tools/goals_manager.py
def definir_objetivos(db):
    """
    Define os objetivos de produção, vendas e receita mensais.
    :param db: Conexão ativa para a base de dados SQLite.
    :type db: sqlite3.Connection
    :returns: Nada. Define os objetivos na base de dados e notifica o utilizador.
    :rtype: None
    A função pede ao utilizador o mês do objetivo e os valores dos objetivos,
    adicionando-os na tabela ``objetivos_mensais``.
    """
    cursor = db.cursor()
    mes = input("Mês dos objetivos (YYYY-MM): ")
    objetivo_producao = float(input("Objetivo de produção (kg): "))
    objetivo_vendas = float(input("Objetivo de vendas (pedidos): "))
    objetivo_receita = float(input("Objetivo de receita (€): "))

    cursor.execute("""
        INSERT INTO objetivos_mensais (mes, objetivo_producao, objetivo_vendas, objetivo_receita)
        VALUES (?, ?, ?, ?)
    """, (mes, objetivo_producao, objetivo_vendas, objetivo_receita))
    db.commit()
    print(f"✅ Objetivos para {mes} definidos com sucesso.")


def ver_objetivos(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM objetivos_mensais ORDER BY mes")
    rows = cursor.fetchall()

    if not rows:
        print("Nenhum objetivo definido ainda.")
        return

    print("\n===== Objetivos e Desempenho Mensal =====\n")
    for r in rows:
        _, mes, obj_prod, obj_vend, obj_rec, real_prod, real_vend, real_rec = r
        pct_prod = (real_prod / obj_prod * 100) if obj_prod else 0
        pct_vend = (real_vend / obj_vend * 100) if obj_vend else 0
        pct_rec = (real_rec / obj_rec * 100) if obj_rec else 0

        print(f"Mês: {mes}")
        print(f"Produção: {real_prod}/{obj_prod} kg ({pct_prod:.0f}%)")
        print(f"Vendas: {real_vend}/{obj_vend} pedidos ({pct_vend:.0f}%)")
        print(f"Receita: €{real_rec:.2f}/€{obj_rec:.2f} ({pct_rec:.0f}%)")
        print("-"*40)
