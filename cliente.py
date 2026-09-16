from banco import conectar


def cadastrar_cliente():
    print("\n--- CADASTRAR CLIENTE ---")

    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")

    # Dicionário com os dados do cliente
    cliente = {
        "nome": nome,
        "telefone": telefone
    }

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO clientes (nome, telefone) VALUES (?, ?)",
        (cliente["nome"], cliente["telefone"])
    )

    conexao.commit()
    conexao.close()

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\n--- CLIENTES CADASTRADOS ---")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    conexao.close()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"Telefone: {cliente[2]}")
            print("----------------------")


def buscar_cliente():
    print("\n--- BUSCAR CLIENTE ---")

    nome = input("Digite o nome do cliente: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE nome LIKE ?",
        ("%" + nome + "%",)
    )

    clientes = cursor.fetchall()

    conexao.close()

    if len(clientes) == 0:
        print("Cliente não encontrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"Telefone: {cliente[2]}")


def excluir_cliente():
    print("\n--- EXCLUIR CLIENTE ---")

    id_cliente = int(input("Digite o ID do cliente: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id_cliente,)
    )

    conexao.commit()
    conexao.close()

    print("Cliente excluído com sucesso!")