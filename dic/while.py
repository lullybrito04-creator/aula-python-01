while True:

    escolha = str(input("Confirmar operação? "))

    match escolha:
        case "sim" | "yes" | "s" | "y" :
            print ("confirmado!")
            break
        case "nao" | "no" | "n" | "nope" :
            print("rejeitado")
            break
        case _:
            print("selecione novamente: ")