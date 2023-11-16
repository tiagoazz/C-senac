
using System;

namespace Testes
{
    class Teste
    {
        static void Main(string[] args) // método principal do programa
        {
            int idadeEstatica = 25; // valor inteiro
            string nome = "Joao"; // valor string 
            bool valor = true; // valor booleano

            Console.WriteLine($"Nome: {nome}, Idade: {idadeEstatica}, Adulto: {valor}");
            Console.WriteLine("=================================================");
            // insercao de dados
            Console.WriteLine("Foi só um teste. Agora, voce ira inserir os seus dados!");

            Console.Write("Digite o seu nome: ");
            string nome1 = Console.ReadLine(); /// Entrada de dados "(input)" 

            Console.Write("Digite a sua idade: ");
            string inputIdade = Console.ReadLine(); // valor idade entra como valores de caracteres
            int idade = int.Parse(inputIdade); // valores caracteres sao convertidos em valor inteiro

            Console.WriteLine("=================================================");
            Console.WriteLine($"Olá, {nome1}, é um prazer conhecê-lo!"); // Saída de dados com o valor "nome1"
            Console.WriteLine($"Entao, voce tem {idade} anos, correto? [s/n]");

            if (idade >= 18)
            {  // Abrimos chaves "{}" porque aqui dentro da estrutura "if" queremos um bloco de comando, que é...

                Console.WriteLine($"Você tem {idade} anos, e é considerado um adulto.");
                // Isso é que acontecerá SE (if) a idade inserida for igual ou maior que 18!

            }
            else // Caso o valor for menor que 18, "else" (qualquer outro valor menor que 18)
                 // Entao temos um bloco de comando que sera executado!
            {
                Console.WriteLine($"Você tem {idade} anos, e ainda não é considerado um adulto.");

               
            }

            ExibirMenu();
        }

        static void ExibirMenu()
        {
            Console.WriteLine("=================================================");
            Console.WriteLine("Escolha uma operacao:");
            Console.WriteLine("1. Adição");
            Console.WriteLine("2. Subtração");
            Console.WriteLine("3. Divisão");
            Console.WriteLine("4. Multiplicação");

            // Ler entrada do usuário
            Console.Write("Digite o nome da operação desejada: ");
            int escolhaOperacao = int.Parse(Console.ReadLine());
            // esse bloco converte uma variavel para inteiro e ja exibe o input na tela !


            // realizando operacao com base na escolha
            switch (escolhaOperacao)
            {
                case 1:
                    RealizarAdicao();
                    break;

                case 2:
                    RealizarSubtracao();
                    break;

                case 3:
                    RealizarDivisao();
                    break;

                case 4:
                    RealizarMultiplicacao();
                    break;

                default:
                    Console.WriteLine("Opcao invalida. Tente novamente!");
                    ExibirMenu();
                    break;
            }
        }

        static void RealizarAdicao()
        {
            Console.Write("Digite o primeiro número: ");
            double numero1 = double.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            double numero2 = double.Parse(Console.ReadLine());

            double resultado = numero1 + numero2;

            Console.WriteLine($"O resultado da Operacao é: {resultado}");

        }

        static void RealizarSubtracao()
        {
            Console.Write("Digite o primeiro número: ");
            double numero1 = double.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            double numero2 = double.Parse(Console.ReadLine());

            double resultado = numero1 - numero2;

            Console.WriteLine($"O resultado da Operacao é: {resultado}");

        }

        static void RealizarMultiplicacao()
        {
            Console.Write("Digite o primeiro número: ");
            double numero1 = double.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            double numero2 = double.Parse(Console.ReadLine());

            double resultado = numero1 * numero2;

            Console.WriteLine($"O resultado da Operacao é: {resultado}");

        }

        static void RealizarDivisao()
        {
            Console.Write("Digite o primeiro número: ");
            double numero1 = double.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            double numero2 = double.Parse(Console.ReadLine());

            double resultado = numero1 / numero2;

            Console.WriteLine($"O resultado da Operacao é: {resultado}");

        }

    }
}
