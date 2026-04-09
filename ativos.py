import os
 
while True:
    print ("\n --------Menu Comandos------")
    print ("1 - Mostrar arquivos da pasta(dir)")
    print ("2 - Mostrar data do sistema (date)")
    print ("3 - Mostrar fhora do sistema(time)")
    print ("4 -Limpar tela (cls)")
    print ("5 - Ver IP do computador (ipconfig)")
    print ("6 - Ver informacoes do sistema (systeminfo)")
    print ("7 - Abrir calculadora ")
    print ("8 - Abrir bloco de notas ")
    print ("9 - Abrir explorado de arquivo ")
    print ("10 -Listar tarefas ativas(talklist) ")
    print ("0 - SAIR ")

    opcao = input("Escolha uma opcao: ")
    if opcao == "1":
        os.system("dir")
    elif opcao == "2":
        os.system("date /t")
    elif opcao == "3":
        os.system("time /t")
    elif opcao == "4":
        os.system ("cls")
    elif opcao =="5":
        os.system ("ipconfig")
    elif opcao =="6":
        os.system ("systeminfo")
    elif opcao == "7":
        os .system ("calc")
    elif opcao == "8":
        os .system ("notepad")
    elif opcao == "9":
        os .system("talklist")
    elif opcao == "0":
        print("Saindo do programa ...")
        break
    else:
        print("OPÇÃO INVALIDA!")