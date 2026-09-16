from banco import criar_tabelas, cadastrar_cardapio

from cliente import (
    cadastrar_cliente,
    listar_clientes,
    buscar_cliente,
    excluir_cliente
)

from produtos import (
    cadastrar_produto,
    listar_produtos,
    buscar_produto,
    atualizar_preco,
    excluir_produto
)

from pedidos import (
    criar_pedido,
    listar_pedidos
)


# Cria as tabelas do banco
criar_tabelas()

# Cadastra o cardápio automaticamente
cadastrar_cardapio()


while True:

    print("\n================================")
    print("       RESTAURANTE JAPÔNES ")
    print("================================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Excluir cliente")
    print("--------------------------------")
    print("5 - Cadastrar produto")
    print("6 - Listar cardápio")
    print("7 - Buscar produto")
    print("8 - Atualizar preço")
    print("9 - Excluir produto")
    print("--------------------------------")
    print("10 - Criar pedido")
    print("11 - Listar pedidos")
    print("0 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        buscar_cliente()

    elif opcao == "4":
        excluir_cliente()

    elif opcao == "5":
        cadastrar_produto()

    elif opcao == "6":
        listar_produtos()

    elif opcao == "7":
        buscar_produto()

    elif opcao == "8":
        atualizar_preco()

    elif opcao == "9":
        excluir_produto()

    elif opcao == "10":
        criar_pedido()

    elif opcao == "11":
        listar_pedidos()

    elif opcao == "0":
        print("\nObrigado por comprar com a gente!")
        break

    else:  
        print("\nOpção inválida!")