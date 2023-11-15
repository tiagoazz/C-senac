import mysql.connector
from datetime import datetime

# IMPORTANDO AS BIBLIOTECAS NECESSARIAS

conectar = mysql.connector.connect(host='localhost', user='root', password='', database='empresa')
cursor = conectar.cursor() 

# FAZENDO A CONEXAO AO SERVIDOR MYSQL (XAMPP SERVER)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        nascimento DATE NOT NULL,
        idade INT          
    )          
''')
# CRIANDO A TABELA "funcionarios" | TAMBEM PODERIA SER CRIADA ANTES DENTRO DO BANCO

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

# ALGORITMO PARA CALCULO DE IDADE BASEADO NO NASCIMENTO INSERIDO 

nome = input("Digite o nome do funcionário: ")
nascimento = input("Digite a data de nascimento (formato AAAA-MM-DD): ")

idade = calcular_idade(nascimento)
# ALGORTIMO QUE ARMAZENA OS VALORES DE nome, nascimento e idade (QUE SERAO ACRESCENTADOS À TABELA)

cursor.execute("INSERT INTO funcionarios (nome, nascimento, idade) VALUES (%s, %s, %s)", (nome, nascimento, idade, ))
# INSERE NA TABELA
conectar.commit()
# FAZ AS MUDANCAS
print("Dados inseridos com sucesso!")

conectar.close()
# FECHA A CONEXAO COM O BANCO DE DADOS
