### 🏫 Sistema Escolar com CRUD em Python + SQLite
Este projeto é um sistema de gerenciamento de alunos desenvolvido em Python, com persistência de dados utilizando o banco de dados SQLite. A aplicação permite cadastrar, listar, atualizar e deletar informações de estudantes, armazenando-as em um banco local.

##  Funcionalidades:
- 📥 Adicionar aluno com nome, idade, série e nota final

- 📋 Listar todos os alunos cadastrados

- ✏️ Atualizar informações de um aluno existente

- 🗑️ Deletar aluno do sistema

- 📊 Cálculo automático da situação (Aprovado ou Reprovado) com base na nota final

## 🛠️ Tecnologias Utilizadas
- Python 3.x

- SQLite (*via sqlite3, biblioteca padrão do Python)

## ▶️ Como Executar
Certifique-se de ter o Python instalado:

```bash
python --version
```

Execute o script:
```bash
python main.py
```

* Use o menu interativo exibido no terminal para operar o sistema.

## 🧠 Conceitos Abordados

- 📌 CRUD (Create, Read, Update, Delete)
As 4 operações fundamentais em sistemas de banco de dados:

- CREATE: Inserção de alunos

- READ: Listagem dos alunos

- UPDATE: Atualização dos dados do aluno

- DELETE: Exclusão de registros

# 🗄️ SQLite
Banco de dados leve e embutido, ideal para aplicações simples, sem necessidade de servidor externo.

## 🧮 Lógica 
A situação do aluno é determinada pela nota final:

- Nota ≥ 6.0 → Aprovado

- Nota < 6.0 → Reprovado

## 👨‍💻 Boas práticas de código
- Separação por funções

- Conexão persistente com o banco

- CREATE TABLE IF NOT EXISTS para evitar recriação

- Fechamento adequado da conexão com conn.close()

## 📂 Estrutura do Projeto
sistema-escolar/

├── main.py            - Código principal do sistema

├── banco_de_dados.db  - Arquivo SQLite gerado automaticamente

├── README.md          - Documentação do projeto


🧑‍💻 Autor:
- Desenvolvido por [@Devmoises79].
- 📧 Contato: [https://www.linkedin.com/in/moises-aniceto-71042a251/] | 🔗 LinkedIn
