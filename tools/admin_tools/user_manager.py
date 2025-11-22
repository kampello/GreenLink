import sqlite3

def criar_utilizador(db):
    """
        Adiciona um novo utilizador à base de dados.
        :param db: Ligação ao SQLite já aberta.
        :type db: sqlite3.Connection
        :returns: Nothing. Escreve o resultado no stdout.
        :rtype: None
        :raises sqlite3.Error: Se ocorrer um erro na inserção do utilizador.
    
    """
    
    nome = input("Nome do novo utilizador: ")
    senha = input("Senha: ")
    tipo = input("Tipo (admin / cliente / fornecedor): ")

    try:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO utilizadores (nome, senha, tipo) VALUES (?, ?, ?)",
            (nome, senha, tipo)
        )
        db.commit()
        print(f"Utilizador '{nome}' criado com sucesso como {tipo}.")
    except sqlite3.Error as e:
        print(f"Erro ao criar utilizador: {e}")

def apagar_utilizador(db):
    """
    Remover um utilizador que existe dado o nome.
    :param db: Ligação SQLite já aberta.
    :type db: sqlite3.Connection
    :returns: Nada. Imprime o resultado no stdout.
    :rtype:None
    """
    nome = input("Nome do utilizador a apagar: ")
    cursor = db.cursor()
    cursor.execute("DELETE FROM utilizadores WHERE nome = ?", (nome,))
    db.commit()

    if cursor.rowcount > 0:
        print(f" Utilizador '{nome}' removido com sucesso.")
    else:
        print("Utilizador não encontrado.")

def pesquisar_utilizador(db):
    nome = input("Nome do utilizador a pesquisar: ")
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, tipo FROM utilizadores WHERE nome LIKE ?", (f"%{nome}%",))
    resultados = cursor.fetchall()

    if resultados:
        print("\n🔍 Resultados da pesquisa:")
        for r in resultados:
            print(f"ID: {r[0]} | Nome: {r[1]} | Tipo: {r[2]}")
    else:
        print("Nenhum utilizador encontrado.")
