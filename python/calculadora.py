def adicao(numero1, numero2):
    print(numero1 + numero2)

def subtracao(numero1, numero2):
    print(numero1 - numero2)

def multiplicacao(numero1, numero2):
    print(numero1 * numero2)

def divisao(numero1, numero2):
    print(numero1 / numero2 )

def menu():
    print("Calculadora em python")
    print("----------------------==")
    print("[1] -- Para calcular uma adição: ")
    print("[2] -- Para calcular uma subtração: ")
    print("[3] -- Para calcular uma multiplicação: ")
    print("[4] -- Para calcular uma divisao: ")
    print("[0] -- Para sair do programa: ")
    
while True:
    menu()
    
    escolha = str(input("Digite aqui sua escolha?: "))
    if escolha == "1":
        numero1 = int(input("Digite aqui o primeiro número: "))
        numero2 = int(input("Digite aqui o segundo número: "))
        adicao(numero1, numero2)

    elif escolha == "2":
        numero1 = int(input("Digite aqui o primeiro número: "))
        numero2 = int(input("Digite aqui o segundo número: "))
        subtracao(numero1, numero2)

    elif escolha == "3":
        numero1 = int(input("Digite aqui o primeiro número: "))
        numero2 = int(input("Digite aqui o segundo número: "))
        multiplicacao(numero1, numero2)
        
    elif escolha == "4":
        numero1 = int(input("Digite aqui o primeiro número: "))
        numero2 = int(input("Digite aqui o segundo número: "))
        divisao(numero1, numero2)

    elif escolha == "0":
        break
    else:
        print("Opcao nao encontrada!")



    
