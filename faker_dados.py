
from banco import conectar
from faker import Faker

fake = Faker("pt_BR")


def cadastrar_clientes_faker():

    conexao = conectar()
    cursor = conexao.cursor()

    for i in range(5):

        nome = fake.name()
        telefone = fake.phone_number()

        cursor.execute(
            """
            INSERT INTO clientes (nome, telefone)
            VALUES (?, ?)
            """,
            (nome, telefone)
        )

    conexao.commit()
    conexao.close()

    print("5 clientes fictícios cadastrados com sucesso!")
