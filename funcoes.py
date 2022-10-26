import os

def limparTela():
    os.system("cls")
    
def lerTexto(mensagemEntrada):
    valor = input(mensagemEntrada)
    return valor

def numeroLetras(palavra):
    valor = len(palavra)
    caracteres = valor * "*"
    return caracteres

def opcao(dica):
    while True:
        print("(1) Jogar")
        print("(2) Solicitar dica")
        op = input("Escolha uma opção: ")
        if op == "1":
            break
        elif op == "2":
            print(dica)
        else:
            print("Opção inválida")
    return