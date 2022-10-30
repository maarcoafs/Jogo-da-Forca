import funcoes

funcoes.limpaTela()

print("JOGO DA FORCA\n")

while True:
    desafiante = input("Desafiante: ")
    competidor = input("Competidor: ")
    funcoes.jogadores(desafiante, competidor)

    funcoes.limpaTela()

    palavraChave = input("Digite a palavra chave: ")
    respostasDicas = ["1ª Dica: ", "2ª Dica: ", "3ª Dica: "]
    dicas = []
    for i in range (len(respostasDicas)):
        print(respostasDicas[i])
        dicas.append(input())
    
    funcoes.limpaTela()
    
    print("A palavra é composta por", len(palavraChave), "letras.")
    for i in range (len(palavraChave)):
         print(end = "")
    
    erros = 0
    tentativas = []
    acertos= []
    vencedor = []

    while True:
        print("\n(1) Para começar o jogo.")
        print("(2) Para ver as dicas (",len(dicas),"disponíveis)")
        print("(0) Para sair.")
        print("Erro:" , erros)
        opcao = input()

        if opcao == "1":
            letra = input("Digite uma letra ou tente acertar a palavra: ")
            if letra in tentativas:
                print("Você já tentou essa letra anteriormente.")
            elif letra not in palavraChave:
                print("Esse letra não pertence a palavra.")
                tentativas.append(letra)
                erros += 1 
            elif letra == palavraChave:
                print("Parabéns! Você acertou!")
                vencedor = competidor
                break
            else:
                print("Você acertou uma letra!")
                acertos.append(letra)
                palavra = ""
                for letra in palavraChave:
                    if letra in acertos:
                        palavra += letra
                    else:
                        palavra += "*"
                print(palavra)
                if palavra == palavraChave:
                    print("Parabéns! Você acertou!")
                    vencedor = competidor
                    break
        elif opcao == "2":
            try:
                print(dicas[0])
                del dicas[0]
            except:
                print("Suas dicas acabaram!")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
        
        if erros >= 5:
            print("Que pena! Você perdeu!")
            break
    funcoes.relatorio(desafiante, competidor, palavraChave, vencedor)
    texto = funcoes.verRelatorio()
    for i in texto:
        texto = i.strip('\n')
        print(texto)

    print("\n(1) Para sair")
    print("(2) Para jogar novamente")
    opcao2 = input()
    if opcao2 == "1":
        break
    elif opcao2 == "2":
        pass
    else:
        print("Opção inválida!")