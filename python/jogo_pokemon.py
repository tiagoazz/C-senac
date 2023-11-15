import pickle
import random

class Pokemon(): 
    def __init__(self, especie, level=None, nome=None):   ### ATRIBUINDO DINAMICAMENTE OS ATRIBUTOS
        self.especie = especie
        
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        
        if nome:
            self.nome = nome
        else:
            self.nome = especie # caso o pokemon nao tenha nome, sera o nome da especie
        
        self.ataque = self.level * 5
        self.vida = self.level * 10
        
    def __str__(self):
        return "{} ({})".format(self.especie, self.level) ## "SELF" porque queremos acessar um atributo do próprio objeto!

    def atacar(self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo
        
        print("{} perdeu {} pontos de vida!".format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print("{} foi derrotado!".format(pokemon))
            return True
        else:
            return False
# print(pokemon_top)

#pokemon_selvagem = PokemonFogo("Charmander")

#eu.capturar(pokemon_selvagem)



class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio em {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
       print("{} lançou uma bola de fogo em {}".format(self, pokemon))
       return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        
        print("{} lançou um jato d'água em {}".format(self, pokemon))
        return super().atacar(pokemon)

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Squirtle"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Magicarp"),
]

class Pessoa:
    
    NOMES = ["João", "Isabela", "Lorena", "Ricardo", "Rodrigo", "Luis", "Pedro", "Marcelo", "Gary"]
    
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(self.NOMES)
        
        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:   
            print("Pokemons de {}:".format(self)) 
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))

        else:  # caso o player nao possua pokemons, o algoritmo exibira essa informacao
                print("{} nao tem nenhum pokemon!".format(self))

# player.batalhar(inimigo1)
#player.mostrar_dinheiro()

#escolher_pokemon_inicial(player)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Erro: Esse jogador nao possui nenhum pokemon para ser escolhido!")
    
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Voce ganhou ${}".format(self.dinheiro))
        self.mostrar_dinheiro()
    
    def mostrar_dinheiro(self):
        print("Voce possui ${}".format(self.dinheiro))
    
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        print("Esses sao os pokemons de {}: ".format(self, pessoa))
        
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:

            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} Ganhou a batalha!".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 10)
                    break
                
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} Ganhou a batalha!".format(pessoa))
                    break

        else:
            print("Esse batalha nao pode ocorrer!")
#escolher_pokemon_inicial(player)
# player.mostrar_pokemons()

# inimigo1.mostrar_pokemons()

class Player(Pessoa):
    tipo = "Player"

    def capturar(self,pokemon):  # append (adiciona um pokemon dentro da lista)
        self.pokemons.append(pokemon)
        print("{} capturou {}".format(self, pokemon))
    
    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha o seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho voce!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                
                except:
                    print("Escolha inválida!")
        else:
            print("Erro: esse jogador nao possui nenhum pokemon a ser escolhido!")
    
    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice[POKEMONS]
            print("Um pokemon selvagem apareceu: {}".format(pokemon))
            
            escolha = input("Deseja capturar esse pokemon? [s/n]: ")
            if escolha == "s":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu!".format(pokemon))
            else:
                print("Ok, boa viagem")
        else:
            print("Essa exploracao foi mal-sucedida!")

#eu = Player() ## EM FORMA DE LISTA, CONSEGUIMOS ADICIONAR UM OBJETO A UM OUTRO OBJETO
#print(eu)

#eu.mostrar_pokemons() ## mostra pokemons 
#print("antes de capturar")        

class Inimigo(Pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

            super().__init__(nome=None, pokemons=pokemons_aleatorios)
        else:  
            super().__init__(nome=None, pokemons=pokemons)

def escolher_pokemon_inicial(player):
    print("Ola {}, voce podera escolher o pokemon que ira lhe acompanhar nessa jornada!".format(player))

    pokemon1 = PokemonEletrico("Pikachu", level=1)
    pokemon2 = PokemonFogo("Charmander", level=1)
    pokemon3 = PokemonFogo("Charizard", level=1)
    pokemon_amigo = PokemonEletrico("Luxio", level=1)
#meu_inimigo = Inimigo()
#player = Player("João Pedro")
#print(player)

    print("Voce possui 3 escolhas: ")
    print("1 - ", pokemon1)
    print("2 - ", pokemon2)
    print("3 - ", pokemon3)
##  print(pokemon.tipo)  ###  Printa o atributo "tipo" da classe/objeto "Pokemon"
##  print(pokemon.especie)  ### 


    while True:
        escolha = input("Escolha o seu pokemon: ")

        if escolha == "1":
            player.capturar(pokemon1)
            break
        elif escolha == "2":
            player.capturar(pokemon2)
            break
        elif escolha == "3":
            player.capturar(pokemon3)
            break
        else:
            print("Escolha inválida")
##  print(pokemon_amigo.tipo)  ### 
##  print(pokemon_amigo.especie)  ### Printa o atributo "espécie" da classe/objeto "Pokemon"

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as file:
            pickle.dump(player, file)
        print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error) 

def carregar_jogo():
    try:
        with open("database.db", "rb") as file:
            player = pickle.load(file)
            print("Loading feito com sucesso!")
            return player
    except Exception as error:
        print("Erro ao carregar jogo")
        print(error)       


if __name__ == "__main__":
    print("Bem vindo ao game Pokemon de terminal!")

    player = carregar_jogo()

    if not player:

        nome = input("Digite seu nome: ")
        player = Player(nome)
        print("Olá, {}, esse é um mundo habitado por pokemons e a sua missao é capturar e vencer quantos conseguir!".format(player))

    if player.pokemons:
        print("Ja vi que voce tem alguns pokemons!")
        player.mostrar_pokemons()
    else:
        print("Voce nao tem nenhum pokemon!, precisa escolher um!")
        escolher_pokemon_inicial(player)

    print("Agora que voce ja tem pokemon(s), enfrente seu arque-inimigo Gary!")
    inimigo1 = Inimigo("Gary", pokemons=[PokemonAgua("Magicarp", level=1)])
    player.batalhar(inimigo1)
    salvar_jogo(player)
    
    while True:
        print("O que deseja fazer?")
        print("[1] - Explorar o mundo")
        print("[2] - Lutar contra um inimigo")
        print("[3] - Mostrar Pokeagenda")
        print("[4] - Mostrar saldo")
        print("[0] - Sair do jogo")
        escolha = input("Sua escolha... ")

        if escolha == "1":
            player.explorar()
            salvar_jogo(player)

        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)

        elif escolha == "3":
            player.mostrar_pokemons()
        
        elif escolha == "4":
            player.mostrar_dinheiro()

        else:
            break
    
    player.mostrar_dinheiro()


#print(pokemon) 
# print(pokemon_amigo)

# pokemon_amigo.atacar(pokemon) ## o retorno do método "atacar" direcionado a outro objeto!
