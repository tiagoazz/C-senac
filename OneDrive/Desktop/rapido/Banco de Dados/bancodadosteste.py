import mysql.connector
from datetime import datetime

conectar = mysql.connector.connect(host='localhost', user='root', password='', database='empresa')
cursor = conectar.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        nascimento DATE NOT NULL,
        idade INT          
    )          
''')

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

nome = input("Digite o nome do funcionário: ")
nascimento = input("Digite a data de nascimento (formato AAAA-MM-DD): ")

idade = calcular_idade(nascimento)

cursor.execute("INSERT INTO funcionarios (nome, nascimento, idade) VALUES (%s, %s, %s)", (nome, nascimento, idade, ))
conectar.commit()

print("Dados inseridos com sucesso!")

conectar.close()