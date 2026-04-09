import json
import os

ARQUIVO = "notas.json"

def carregar_notas():
    if os.path.exists(ARQUIVO):
        try:
            with open (ARQUIVO, "r", encoding= "utf-8") as f:

                return json.load(f)
        except(json.JSONDEcodeerror, IOError):
            return[]
    return[]

def salvar_notas(notas):
    try:
         with open (ARQUIVO, "w", encoding= "utf-8") as f:
             json.dump(notas, f, indent=4,ensure_ascii=False )
    except IOError as e :
        print(f"Erro ao salvar notas:{e}")

def adicionar_notas():
    titulo = input("Titulo da nota: ").script()
    conteudo =input("Conteudo da nota: ").script()

    if not titulo or not conteudo:
        print("As informaçoes precisam ser preenchidas!")
        return

    notas = carregar_notas()

    nota = {
        "titulo": titulo, 
        "conteudo": conteudo
    }
     
    notas.append ("novas_notas")
    salvar_notas(notas)
    print("Nota Salva com Sucesso !!!! ")

def listar_notas():
    notas = carregar_notas()

    if not notas:
        print ("Nenhuma Nota Encontrada.")
        return
    print("\nLista de Notas ")
    for i, nota in enumerate(notas,1):
        titulo = nota.get("titulo", "sem titulo")
        print(f"{i:2d} - {"titulo"}")


def ler_notas():
    notas = carregar_notas()
    if not notas:
        print ("Nenhuma nota Disponivel. ")
        return
    listar_notas()
    indice= int(input("Digite o numero da nota: "))
    if 0 <= indice < len(notas):
        print("\ntitulo: " , notas[indice]["titulo"])
        print("Conteudo", notas[indice]["conteudo"])
    else:
        print("Nota invalida!")

def deletar_nota():
    notas=carregar_notas()
    if not notas:
        print("Nenhuma nota pra Apagar! ")
        return
    listar_notas()
    indice = int(input("Informe a nota a ser Apagada: "))
    if 0 <= indice < len(notas):
        notas.pop(indice)
        salvar_notas()
        print("Nota Apagada! ")
    else:
        print("Nota Invalida! ")
def menu():
    while True:
        print ("\n=====APP DE NOTAS=====")
        print("1 - Adicionar nota")
        print("2  -Listar notas")
        print("3 - Ler nota")
        print("4 - Excluir nota")
        print("5 - SAIR ")
        opcao = str(input("Escolha uma opção: "))
        match opcao:
            case"1":
                adicionar_notas()
            case"2":
                listar_notas()
            case "3":
                ler_notas
            case "4":
                deletar_nota
            case "5":
                print("saindo")