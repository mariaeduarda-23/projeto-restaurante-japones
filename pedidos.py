
from banco import conectar


def criar_pedido():
    print("\n--- NOVO PEDIDO ---")

    cliente_id = int(input("ID do cliente: "))
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))

    if quantidade <= 0:
        print("Quantidade inválida!")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO pedidos
        (cliente_id, produto_id, quantidade)
        VALUES (%s, %s, %s)
        """,
        (cliente_id, produto_id, quantidade)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("Pedido criado com sucesso!")


def listar_pedidos():
    print("\n--- PEDIDOS ---")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            pedidos.id,
            clientes.nome,
            produtos.nome,
            pedidos.quantidade,
            produtos.preco
        FROM pedidos
        JOIN clientes
        ON pedidos.cliente_id = clientes.id
        JOIN produtos
        ON pedidos.produto_id = produtos.id
    """)

    pedidos = cursor.fetchall()

    cursor.close()
    conexao.close()

    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
    else:
        for pedido in pedidos:
            total = pedido[3] * pedido[4]

            print(f"Pedido: {pedido[0]}")
            print(f"Cliente: {pedido[1]}")
            print(f"Produto: {pedido[2]}")
            print(f"Quantidade: {pedido[3]}")
            print(f"Total: R$ {total:.2f}")
            print("----------------------")
