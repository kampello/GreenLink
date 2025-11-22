import csv
from datetime import datetime

def exportar_relatorio_vendas(db, fornecedor_nome):
    cursor = db.cursor()