# GreenLink - Sistema de Gestão de Vegetais com SQLite
import sqlite3
from classes.admin import Admin



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
            tipo_user = user[0].lower()
            print(f"Bem-vindo, {nome}! Tipo de utilizador: {user[0].capitalize()}")
            
            nova_conect = conectar()
            if tipo_user == "admin":
                admin = Admin(nova_conect)
                admin.menu()
            break # parar while true
        else:
            print("Credenciais inválidas.")

if __name__ == "__main__":
    print("=== GreenLink ===")
    login()
