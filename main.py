from funcoes import lerTexto, limparTela, numeroLetras

limparTela()

print("JOGO DA FORCA")

desafiante = lerTexto("Nome do desafiante: ")
competidor = lerTexto("Nome do competidor: ")
palavraChave = lerTexto("Palavra Chave: ")
dica1 = lerTexto("Dica 1: ")
dica2 = lerTexto("Dica 2: ")
dica3 = lerTexto("Dica 3: ")

limparTela()

print("A palavra tem", (numeroLetras(palavraChave)), "letras." )

opcao(dica1)




