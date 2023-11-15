import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Função para criar a tabela de alunos no banco de dados MySQL
def criar_tabela_alunos():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT,
        curso VARCHAR(255)
    )
    """)

    conn.commit()
    conn.close()

# Função para cadastrar um aluno no banco de dados MySQL
def cadastrar_aluno(nome, idade, curso):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola"
    )

    cursor = conn.cursor()

    cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, idade, curso))

    conn.commit()
    conn.close()

# Classe da aplicação para cadastro de alunos
class CadastroAlunosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Alunos")

        # Variáveis para armazenar dados
        self.nome_var = tk.StringVar()
        self.idade_var = tk.IntVar()
        self.curso_var = tk.StringVar()

        # Layout da aplicação
        tk.Label(root, text="Nome do Aluno:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.nome_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.idade_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Curso:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.curso_var).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Cadastrar Aluno", command=self.cadastrar_aluno).grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_aluno(self):
        nome = self.nome_var.get()
        idade = self.idade_var.get()
        curso = self.curso_var.get()

        if nome and idade and curso:
            cadastrar_aluno(nome, idade, curso)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

if __name__ == "__main__":
    criar_tabela_alunos()  # Chama a função para criar a tabela de alunos no banco de dados MySQL
    root = tk.Tk()
    app = CadastroAlunosApp(root)
    root.mainloop()
