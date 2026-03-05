#CRIACAO DE DICIONARIO
pontos = {}
#ENTRADA DE DADOS
for i in range(3):
    nome = input ("Digite o nome:")
    pontuacao = input ("Informe os pontos iniciais:")

    pontos [nome] = pontuacao
    
for jogador , pontuacao in pontos .items():
    print (f"{jogador} | {pontuacao}")