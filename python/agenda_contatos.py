AGENDA = { #dicionario de contatos. MANIPULACAO DE DADOS!  ## VARIAVEL GLOBAL!! CONSTANTE
    "Guilherme": {
        "tel": "99261-7845",
        "email": "guilherme@tjsecurity.local",
        "endereco": "Rua Ganhafoto"
    },
    "Maria": {
        "tel": "9953-2203",
        "email": "maria@tjsecurity.local",
        "endereco": "Rua Palmares"
    },
    "Pedro": {
        "tel": "9943-2105",
        "email": "pedro@tjsecurity.local",
        "endereco": "Rua Godofredo"
    },
}

def menu_usuario():
    print("Bem vindo a agenda de contatos!")
    print("Opcao 1 - buscar contato")
    print("Opcao 2 - criar contato")
    print("Opcao 3 - editar contato")
    print("Opcao 4 - excluir contato")
    print("Opcao 5 - Exportar contatos para CSV")
    print("Opcao 6 - Importar contatos para CSV")
    print("Opcao 0 - sair do programa")


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA: ## CRIA UMA ESTRUTURA DE REPETICAO PARA "contato"
            buscar_contato(contato)
    else:
        print("Agenda vazia!")

def buscar_contato(contato):
    try:
        print("Nome:", contato) # ADICIONA UMA STRING CONTATENADA AO VALOR DE "CONTATO"
        print("Telefone:", AGENDA[contato]["tel"]) #PEGA O VALOR "TELEFONE" DE "contato" ()
        print("Email:", AGENDA[contato]["email"]) #PEGA O VALOR "EMAIL" DE "contato" ()
        print("Endereço:", AGENDA[contato]["endereco"])
        print("--------------------------------------")
    except KeyError as e:
        print("Contato inválido!")
        print(e, "não encontrado!")
    except Exception:
        print("Algum erro inesperado ocorreu!")

def ler_detalhes_contato():
    tel = input("Qual o numero do contato? ")
    email = input("Qual o endereco eletronico do contato? ")
    endereco = input("Qual o endereco fisico do contato? ")
    return tel, email, endereco

def incluir_editar_contato(contato, tel, email, endereco): # essas variaveis so valem aqui dentro dessa funcao!
   
    AGENDA[contato] = {
        "tel": tel,
        "email": email, ## a string e a chave!
        "endereco": endereco
    }
    print("Contato {} adicionado com sucesso!".format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print("Contato {} excluído com sucesso!".format(contato))
    except KeyError as error:
        print("Contato inexistente!")
    except Exception as error:
        print("Um erro ineseprado ocorreu!")

def exportar_contato():
    try:
        with open("agenda.csv", "w") as arquivo:
            arquivo.write("NOME, TELEFONE, EMAIL, ENDERECO\n")
            for contato in AGENDA:
                
                telefone = AGENDA[contato]["tel"]
                email = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]

                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print("Agenda exportado com sucesso!")

    except Exception as error:
        print(error)

def importar_contato(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
                print(detalhes)

    except FileNotFoundError:
        print("Arquivo nao encontrado!")
    
    except Exception as error:
        print("Algum erro inesperado!")
        print(error)

while True:
    menu_usuario()

    escolha = str(input("Sua escolha: "))
    if escolha == "1":
        print("Opcao 'buscar contato' selecionada!")
        contato = input("Digite o nome do contato a ser buscado: ")
        buscar_contato(contato)

    elif escolha == "2":
        print("Opcao 'criar contato' selecionada!")
        contato = input("Qual o nome do contato que voce deseja criar? ")
        try:
            AGENDA[contato]
            print("Contato ja existe!")
        except KeyError:
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato)
        
        buscar_contato(contato)

    elif escolha == "3":
        print("Opcao 'editar' selecionada!")
        contato = input("Qual o nome do contato que voce deseja editar? ")

        try:
            AGENDA[contato]
            print("Editando contato: ", contato)
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato)
            
        except KeyError:
            print("Contato nao existente!")

        buscar_contato(contato)

    elif escolha == "4":
        print("Opcao excluir contato selecionada!")
        contato = input("Qual o contato que voce quer excluir?")
        excluir_contato(contato)

    elif escolha == "5":
        print("Opcao 5 'Exportar contatos' selecionada!")
        exportar_contato()
    
    elif escolha == "6":
        print("Opcao 6 'Importar contatos' selecionada!")
        
        nome_arquivo = input("Digite o nome do arquivo a ser importado: ")
        importar_contato(nome_arquivo)
    
    elif escolha == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opcao nao encontrada!")






