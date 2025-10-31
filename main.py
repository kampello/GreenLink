# GreenLink - Sistema de Gestão de Vegetais com SQLite
import sqlite3

def conectar():
    return sqlite3.connect("data/greenlink.db")

def login():
    while True:
        print("=== LOGIN ===")
        nome = input("Nome: ")
        senha = input("Senha: ")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT tipo FROM utilizadores WHERE nome=? AND senha=?", (nome, senha))
        user = cursor.fetchone()
        conn.close()

        if user:
            print(f"Bem-vindo, {nome}! Tipo de utilizador: {user[0].capitalize()}")
            break
        else:
            print("Credenciais inválidas.")

if __name__ == "__main__":
    print("=== GreenLink ===")
    login()
