
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def conectar():
    url = os.getenv("DATABASE_URL")

    if not url:
        raise ValueError("A conexão DATABASE_URL não foi encontrada no arquivo .env")

    return psycopg2.connect(url, connect_timeout=30)


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco NUMERIC(10, 2) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    """)

    conexao.commit()
    cursor.close()
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
            SELECT %s, %s, %s
            WHERE NOT EXISTS (
                SELECT 1 FROM produtos WHERE nome = %s
            )
        """, (
            produto[0],
            produto[1],
            produto[2],
            produto[0]
        ))

    conexao.commit()
    cursor.close()
    conexao.close()
