### ENTRADA DE DADOS #####

class SomaMedia():
    def obter_nota(self, bimestre):
        while True:
            nota = int(input(f"Digite a nota do aluno no {bimestre}º bimestre: "))
            if 0 <= nota <= 10: ## EXPRESSAO CONDICIONAL! SE NOTA ENTRE 0-10 OK, CASO NAO, ERRO!
                return nota
            else:
                print("Numero invalido!. A nota deve estar entre 0 e 10. Tente novamente!")

    def soma_medias(self):
        alunos = str(input("Digite aqui o nome do aluno: "))

        print("======================================================================================")
        print(f"Perfeito. O aluno {alunos} passou passou por 4 bimestres.")
        print("Queremos calcular a media e, portanto, devemos saber a nota dele em cada um dos bimestres!")

        aluno_1 = self.obter_nota(1)
        aluno_2 = self.obter_nota(2)
        aluno_3 = self.obter_nota(3)
        aluno_4 = self.obter_nota(4)
        
        media = (aluno_1 + aluno_2 + aluno_3 + aluno_4) / 4

        print("===========================================================================================")
        print(f"Aluno: {alunos}. \n1º Bimestre: {aluno_1}\n2º Bimestre: {aluno_2}\n3º Bimestre: {aluno_3}\n4º Bimestre: {aluno_4}")

        return media

    def executar(self):
        while True:
            media_resultante = self.soma_medias()
            print("===========================================================================================")
            escolha = input("Digite 's' caso as informacoes estejam corretas ou 'n' caso precise alterar: ")

            if escolha == "s":
                print("Perfeito. Selecione o que deseja fazer com esses dados:")
                print("1. Obter média e verificar aprovacao/reprovacao")
                print("2. Outra opção...")

                escolha = input("Sua escolha: ")

                if escolha == "1":
                    print("===========================================================================================")
                    print(f"A média desse aluno é: {media_resultante}")
                    if media_resultante < 6:
                        print("Portanto, o aluno está reprovado!")
                    else:
                        print("Portanto, o aluno está aprovado!")
                    print("===========================================================================================")
            elif escolha == "n":
                calculadora = SomaMedia()
                calculadora.executar()

# Criando uma instância da classe e executando o programa
calculadora = SomaMedia()
calculadora.executar()

