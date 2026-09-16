import sqlite3


def conectar():
    return sqlite3.connect("restaurante.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()

    produtos = [
        ("Sushi de Salmão", "Sushi", 28.90),
        ("Sushi de Atum", "Sushi", 26.90),
        ("Temaki de Salmão", "Temaki", 24.90),
        ("Temaki de Atum", "Temaki", 22.90),
        ("Yakisoba", "Prato Quente", 32.90),
        ("Guioza", "Entrada", 19.90),
        ("Refrigerante", "Bebida", 6.00),
        ("Água", "Bebida", 4.00),
        ("Sushi Doce", "Sobremesa", 12.90)
    ]

    for produto in produtos:
        cursor.execute("""
            INSERT INTO produtos (nome, categoria, preco)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM produtos WHERE nome = ?
            )
        """, (
            produto[0],
            produto[1],
            produto[2],
            produto[0]
        ))

    conexao.commit()
    conexao.close()