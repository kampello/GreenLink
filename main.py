# GreenLink - Sistema de Gestão de Vegetais com SQLite
import sqlite3
from tools.toolbox import *
from classes.admin import Admin
from classes.cliente import Cliente
from classes.fornecedor import Fornecedor

def conectar():
    return sqlite3.connect("data/greenlink.db")

# Função que reseta o ecrã
def resetEcra():
    clear()
    logo()

def login():
    while True:
        print("=== LOGIN ===")
        nome = input("Nome: ").strip()
        senha = input_senha().strip()

        tipo_user = None
        conn = conectar()
        cursor = conn.cursor()

        # Tenta primeiro na tabela 'utilizadores' (admin/cliente)
        cursor.execute("SELECT tipo FROM utilizadores WHERE nome=? AND senha=?", (nome, senha))
        result = cursor.fetchone()
        if result:
            tipo_user = result[0].lower()
            print(f"DEBUG: encontrado em utilizadores -> {tipo_user}")
        
        # Se não encontrou, tenta na tabela 'fornecedores'
        if not tipo_user:
            cursor.execute("SELECT id FROM fornecedores WHERE nome=? AND senha=?", (nome, senha))
            result = cursor.fetchone()
            if result:
                tipo_user = "fornecedor"
                print(f"DEBUG: encontrado em fornecedores -> id={result[0]}")
        
        conn.close()
        
        if tipo_user:
            resetEcra()
            print(f"Bem-vindo, {nome}! Tipo de utilizador: {tipo_user.capitalize()}")
            nova_conect = conectar()
            if tipo_user == "admin":
                admin = Admin(nova_conect)
                admin.menu()
            elif tipo_user == "cliente":
                cliente = Cliente(nova_conect, nome) 
                cliente.menu()
            elif tipo_user == "fornecedor":
                fornecedor = Fornecedor(nova_conect, nome)
                fornecedor.menu()
            break
        else:
            print("Credenciais inválidas.")


if __name__ == "__main__": 
    resetEcra()
    login()
