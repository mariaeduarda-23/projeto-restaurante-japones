from banco import conectar
4

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))

    # Dicionário com os dados do produto
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco
    }

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO produtos (nome, categoria, preco)
        VALUES (?, ?, ?)
        """,
        (
            produto["nome"],
            produto["categoria"],
            produto["preco"]
        )
    )

    conexao.commit()
    conexao.close()

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("\n--- CARDÁPIO ---")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    conexao.close()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Categoria: {produto[2]}")
            print(f"Preço: R$ {produto[3]:.2f}")
            print("----------------------")


def buscar_produto():
    print("\n--- BUSCAR PRODUTO ---")

    nome = input("Digite o nome do produto: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM produtos WHERE nome LIKE ?",
        ("%" + nome + "%",)
    )

    produtos = cursor.fetchall()

    conexao.close()

    if len(produtos) == 0:
        print("Produto não encontrado.")
    else:
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Categoria: {produto[2]}")
            print(f"Preço: R$ {produto[3]:.2f}")


def atualizar_preco():
    print("\n--- ATUALIZAR PREÇO ---")

    id_produto = int(input("Digite o ID do produto: "))
    novo_preco = float(input("Digite o novo preço: R$ "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE produtos SET preco = ? WHERE id = ?",
        (novo_preco, id_produto)
    )

    conexao.commit()
    conexao.close()

    print("Preço atualizado com sucesso!")


def excluir_produto():
    print("\n--- EXCLUIR PRODUTO ---")

    id_produto = int(input("Digite o ID do produto: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM produtos WHERE id = ?",
        (id_produto,)
    )

    conexao.commit()
    conexao.close()

    print("Produto excluído com sucesso!")