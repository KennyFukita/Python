# Importa a biblioteca do sqlite para usar o banco
import sqlite3

# Procedimento que recebe uma conexão e cria uma tabela


def criar_tabela_usuario(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()

    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS usuario (
                nome TEXT NOT NULL,
                login TEXT NOT NULL,
                senha TEXT NOT NULL
            ); '''

    # Executa o SQL
    cursor.execute(sql)

# Procedimento que recebe a conexão


def inserir_usuario(conexao):
    #Pede os dados para o usuário
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    # Cria o cursor
    cursor = conexao.cursor()
    # Monta o SQL
    sql = '''
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    '''.format(nome, login, senha)

    # Executa
    cursor.execute(sql)

    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()


def deletar_usuario(conexao):
    # Cria o cursor
    cursor = conexao.cursor()

    # Monta o SQL
    x = 0
    x = int(input("Informe o ID que deseja deletar: "))
    sql = '''
        DELETE FROM usuario WHERE rowid = {};
    '''.format(x)

    # Executa
    cursor.execute(sql)

    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()


def alterar_senha(conexao):
    # Cria o cursor
    cursor = conexao.cursor()

    # Monta o SQL
    x = 0
    x = int(input("Informe o ID que deseja alterar a senha: "))
    nova_senha = input("Informe a nova senha:")
    sql = '''
        UPDATE usuario SET
        senha = {}
        WHERE rowid = {};
    '''.format(nova_senha,x)

    # Executa
    cursor.execute(sql)
    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()


def listar_usuario(conexao):
    # Criar Cursor
    cursor = conexao.cursor()

    # Monta o Sql
    sql = """
        SELECT rowid, * FROM usuario;
    """
    # Executar o SQL
    cursor.execute(sql)

    lista = cursor.fetchall()

    # Printar a lista
    print("======== LISTANDO USUÁRIOS =========")
    for usuario in lista:
        print("""
        ID: {}
        NOME: {}
        LOGIN {}
        """.format(usuario[0],usuario[1],usuario[2]))




