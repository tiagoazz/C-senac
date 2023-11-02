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
def mostrar_contatos():
    for contato in AGENDA: ## CRIA UMA ESTRUTURA DE REPETICAO PARA "contato"
        buscar_contato(contato)

def buscar_contato(contato):
    print("Nome:", contato) # ADICIONA UMA STRING CONTATENADA AO VALOR DE "CONTATO"
    print("Telefone:", AGENDA[contato]["tel"]) #PEGA O VALOR "TELEFONE" DE "contato" ()
    print("Email:", AGENDA[contato]["email"]) #PEGA O VALOR "EMAIL" DE "contato" ()
    print("Endereço:", AGENDA[contato]["endereco"])
    print("--------------------------------------")

def incluir_contato(contato, telefone, email, endereco): # essas variaveis so valem aqui dentro dessa funcao!
    AGENDA[contato] = {
        "tel": telefone,
        "email": email, ## a string e a chave!
        "endereco": endereco
    }
    print("Contato {} adicionado com sucesso!".format(contato))

incluir_contato("João Pedro", "99183-2294", "joaopedro@tjsecurity.local", "Residencial Setsul")
mostrar_contatos()



