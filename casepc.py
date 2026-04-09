escolha = int(input("escolha \n pc gamer\n computador para escritorio \n computador pra empresa \n computador para estudos \n numero do pedido :" ))

match escolha:
    case 1:
        print("pc gamer")
    case 2:
        print("computador para escritorio")
    case 3:
        print("computador pra empresa")
    case 4:
        print("computador para estudos")
    case _:
        print("selecione o numero do pedido:")

