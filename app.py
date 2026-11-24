
from flask import Flask, render_template, request, redirect
from banco import conectar

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


# CLIENTES

@app.route("/clientes")
def clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    lista_clientes = cursor.fetchall()

    conexao.close()

    return render_template("clientes.html", clientes=lista_clientes)


@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():

    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, telefone) VALUES (?, ?)",
            (nome, telefone)
        )

        conexao.commit()
        conexao.close()

        return redirect("/clientes")

    return render_template("cadastrar_cliente.html")


@app.route("/editar_cliente/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]

        cursor.execute(
            "UPDATE clientes SET nome = ?, telefone = ? WHERE id = ?",
            (nome, telefone, id)
        )

        conexao.commit()
        conexao.close()

        return redirect("/clientes")

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    cliente = cursor.fetchone()

    conexao.close()

    return render_template("editar_cliente.html", cliente=cliente)


@app.route("/excluir_cliente/<int:id>")
def excluir_cliente_web(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()

    return redirect("/clientes")


# PRODUTOS

@app.route("/produtos")
def produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    lista_produtos = cursor.fetchall()

    conexao.close()

    return render_template("produtos.html", produtos=lista_produtos)


@app.route("/cadastrar_produto", methods=["GET", "POST"])
def cadastrar_produto():

    if request.method == "POST":
        nome = request.form["nome"]
        categoria = request.form["categoria"]
        preco = float(request.form["preco"])

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO produtos (nome, categoria, preco)
            VALUES (?, ?, ?)
            """,
            (nome, categoria, preco)
        )

        conexao.commit()
        conexao.close()

        return redirect("/produtos")

    return render_template("cadastrar_produto.html")


@app.route("/editar_produto/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":
        nome = request.form["nome"]
        categoria = request.form["categoria"]
        preco = float(request.form["preco"])

        cursor.execute(
            """
            UPDATE produtos
            SET nome = ?, categoria = ?, preco = ?
            WHERE id = ?
            """,
            (nome, categoria, preco, id)
        )

        conexao.commit()
        conexao.close()

        return redirect("/produtos")

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto = cursor.fetchone()

    conexao.close()

    return render_template("editar_produto.html", produto=produto)


@app.route("/excluir_produto/<int:id>")
def excluir_produto_web(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()

    return redirect("/produtos")


# PEDIDOS

@app.route("/pedidos")
def pedidos():
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

    lista_pedidos = cursor.fetchall()

    conexao.close()

    return render_template("pedidos.html", pedidos=lista_pedidos)


@app.route("/cadastrar_pedido", methods=["GET", "POST"])
def cadastrar_pedido():
    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        produto_id = int(request.form["produto_id"])
        quantidade = int(request.form["quantidade"])

        if quantidade <= 0:
            conexao.close()
            return "Quantidade inválida!"

        cursor.execute(
            """
            INSERT INTO pedidos (cliente_id, produto_id, quantidade)
            VALUES (?, ?, ?)
            """,
            (cliente_id, produto_id, quantidade)
        )

        conexao.commit()
        conexao.close()

        return redirect("/pedidos")

    cursor.execute("SELECT * FROM clientes")
    lista_clientes = cursor.fetchall()

    cursor.execute("SELECT * FROM produtos")
    lista_produtos = cursor.fetchall()

    conexao.close()

    return render_template(
        "cadastrar_pedido.html",
        clientes=lista_clientes,
        produtos=lista_produtos
    )


@app.route("/editar_pedido/<int:id>", methods=["GET", "POST"])
def editar_pedido(id):
    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        produto_id = int(request.form["produto_id"])
        quantidade = int(request.form["quantidade"])

        if quantidade <= 0:
            conexao.close()
            return "Quantidade inválida!"

        cursor.execute(
            """
            UPDATE pedidos
            SET cliente_id = ?, produto_id = ?, quantidade = ?
            WHERE id = ?
            """,
            (cliente_id, produto_id, quantidade, id)
        )

        conexao.commit()
        conexao.close()

        return redirect("/pedidos")

    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (id,))
    pedido = cursor.fetchone()

    cursor.execute("SELECT * FROM clientes")
    lista_clientes = cursor.fetchall()

    cursor.execute("SELECT * FROM produtos")
    lista_produtos = cursor.fetchall()

    conexao.close()

    return render_template(
        "editar_pedido.html",
        pedido=pedido,
        clientes=lista_clientes,
        produtos=lista_produtos
    )


@app.route("/excluir_pedido/<int:id>")
def excluir_pedido_web(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pedidos WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()

    return redirect("/pedidos")


if __name__ == "__main__":
    app.run(debug=True)
