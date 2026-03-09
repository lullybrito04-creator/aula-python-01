def mostrar_menu():
    print("\n===MENU RESTAURANTE====")
    print("1 - VER CARDAPIO")
    print("2 - FAZER PEDIDO")
    print("3 - VER CONTA")
    print("4 -SAIR")
    print("======================")

while True:

    mostrar_menu()
    opcao = str(input("Escolha uma opçao:"))
    match opcao:
        case 1:
            print("-------Cardapio-------")
            print("1 pizza - 35$")
            print("2 hamburguer -20$")
            print("3 refrigerante -10$")
        case 2:
            print("\nOque deseja pedir?")
            print("1 pizza - 35$")
            print("2 hamburguer -20$")
            print("3 refrigerante -10$")
            pedido = input("Escolha")

            match pedido:
                case "1":
                  conta = 0 
                  conta += 35
                  print ("Pedido Selecionado :Pizza")
                case "2":
                  conta = 0 
                  conta += 20 
                  print("Pedido Selecionado : Hamburguer")
                case "3":
                  conta = 0 
                  conta += 10 
                  print("Pedido Selecionado : Refrigerante")
                case _:
                  print("Opçao invalida!")
            break
        
        case "3":
          print(f"\n")
            
       
        case "4":
            print("Obrigado por nos visitar")
            break
