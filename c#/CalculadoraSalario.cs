using System;

class Programa
{
    static void Main()
    {
        bool sair = false;


        do
        {
            Console.WriteLine("Escolha uma opção:");
            Console.WriteLine("1. Calcular Salário");
            Console.WriteLine("2. Sair");
            Console.Write("Opção: ");

            string opcao = Console.ReadLine();

            switch (opcao)
            {
                case "1":
                    CalcularSalario();
                    break;
                case "2":
                    sair = true;
                    break;
                default:
                    Console.WriteLine("Opção inválida. Tente novamente.");
                    break;

            }
        } while (!sair);
    }

    static void CalcularSalario()
    {

        Console.WriteLine("Calculadora de Salário\n");
        // salario por hora
        Console.Write("Informe o salário por hora: ");
        double salarioHora = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Informe o número de horas trabalhas por dia: ");
        double horasporDia = Convert.ToDouble(Console.ReadLine());

        double salarioDiario = salarioHora * horasporDia;
        double salarioSemanal = salarioDiario * 5;
        double salarioPorHoraCalculado = salarioHora;
        double salarioMensal = salarioSemanal * 4;
        double salarioAnual = salarioMensal * 12;

        // exibe resultado
        Console.WriteLine("\nResultados: ");
        Console.WriteLine($"Salário por Hora: R${salarioPorHoraCalculado:F2}");
        Console.WriteLine($"Salário por Dia: R${salarioDiario:F2}");
        Console.WriteLine($"Salário por Semana: R${salarioSemanal:F2}");
        Console.WriteLine($"Salário por mês: R${salarioMensal:F2}");
        Console.WriteLine($"Salário por ano: R${salarioAnual:F2}");

        Console.ReadLine();


    }

}


