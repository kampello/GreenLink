import datetime

def confirmar_entrega(db, pedido_id):
    cursor = db.cursor()

    # data real é hoje
    data_real = datetime.date.today()

    # atualizar a entrega
    cursor.execute("""
        UPDATE entregas
        SET data_real = ?,
            status = CASE 
                        WHEN date(?) <= date(data_prevista) THEN 'no prazo'
                        ELSE 'atrasado'
                     END
        WHERE pedido_id = ?
    """, (data_real, data_real, pedido_id))

    db.commit()
    print("Entrega confirmada. Status atualizado.")
