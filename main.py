"""
Main module for GreenLink - vegetable management system.

This module handles:
- Database connection
- Screen reset and UI utilities
- Login flow and user routing (Admin, Cliente, Fornecedor)
"""

import sqlite3
from tools.toolbox import *
from classes.admin import Admin
from classes.cliente import Cliente
from classes.fornecedor import Fornecedor


def conectar():
    """
    Establish a connection to the SQLite database.

    Returns
    -------
    sqlite3.Connection
        Active connection to ``data/greenlink.db``.
    """
    return sqlite3.connect("data/greenlink.db")


def resetEcra():
    """
    Clear the console and display the application logo.

    Notes
    -----
    Uses utility functions imported from ``tools.toolbox``:
    - ``clear()``
    - ``logo()``
    """
    clear()
    logo()


def login():
    """
    Handle the user authentication process and redirect
    to the correct dashboard based on user type.

    Workflow
    --------
    1. Asks for username and password
    2. Validates against the ``utilizadores`` table
    3. Determines user type (admin, cliente, fornecedor)
    4. Opens the corresponding menu

    Raises
    ------
    None
        Invalid credentials simply restart the login loop.
    """
    while True:
        print("=== LOGIN ===")
        nome = input("Nome: ")
        senha = input_senha()

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT tipo FROM utilizadores WHERE nome=? AND senha=?",
            (nome, senha)
        )
        user = cursor.fetchone()
        conn.close()
        
        if user:
            tipo_user = user[0].lower()
            resetEcra()

            print(f"Bem-vindo, {nome}! Tipo de utilizador: {user[0].capitalize()}")

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
    """
    Application entry point.

    Executes:
    - Screen reset
    - Login process
    """
    resetEcra()
    login()
