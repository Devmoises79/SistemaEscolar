import sqlite3

# Conectar ou criar o banco de dados
conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

# Criar a tabela alunos se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    serie TEXT,
    nota_final REAL,
    situacao TEXT
)
''')
conn.commit()

# Funções CRUD
def calcular_situacao(nota):
    if nota >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

def adicionar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    serie = input("Série: ")
    nota_final = float(input("Nota final: "))
    situacao = calcular_situacao(nota_final)

    cursor.execute('''
    INSERT INTO alunos (nome, idade, serie, nota_final, situacao)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, idade, serie, nota_final, situacao))
    conn.commit()
    print("Aluno adicionado com sucesso!\n")

def listar_alunos():
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print("Nenhum aluno encontrado.\n")
    else:
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Série: {aluno[3]}, Nota: {aluno[4]}, Situação: {aluno[5]}")
        print()

def atualizar_aluno():
    listar_alunos()
    id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))

    nome = input("Novo nome: ")
    idade = int(input("Nova idade: "))
    serie = input("Nova série: ")
    nota_final = float(input("Nova nota final: "))
    situacao = calcular_situacao(nota_final)

    cursor.execute('''
    UPDATE alunos
    SET nome = ?, idade = ?, serie = ?, nota_final = ?, situacao = ?
    WHERE id = ?
    ''', (nome, idade, serie, nota_final, situacao, id_aluno))
    conn.commit()
    print("Aluno atualizado com sucesso!\n")

def deletar_aluno():
    listar_alunos()
    id_aluno = int(input("Digite o ID do aluno que deseja deletar: "))

    cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
    conn.commit()
    print("Aluno deletado com sucesso!\n")

# Menu principal
def menu():
    while True:
        print("=== Sistema Escolar ===")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Deletar aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            deletar_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Rodar o sistema
menu()

# Fechar a conexão no final
conn.close()
