###################### FUNCIONARIO ######################
import jogos
import os
# Procedimento que recebe uma conexão e cria uma tabela
def criar_tabela_cliente(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS cliente (
                idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                datanasc DATE NOT NULL,
                cell TEXT NOT NULL,
                email TEXT NOT NULL,
                CONSTRAINT uk_cpf UNIQUE (cpf)  
            ); '''
    # Executa o SQL
    cursor.execute(sql)

#################################################################
def inserir_cliente(conexao):
    cursor = conexao.cursor()
    nome = input("Nome: ")
    cpf = input("CPF(somente números): ")
    datanasc = input("Data de Nascimento: ")
    cell = input("Celular: ")
    email = input("Email: ")

    sql = '''
        INSERT INTO cliente(nome, cpf, datanasc, cell, email) VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
        );
    '''.format(nome, cpf, datanasc, cell, email)
    cursor.execute(sql)
    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()
    input("Pressione Enter para continuar...")
    os.system("cls")

#################################################################
def listar_cliente(conexao):
    cursor = conexao.cursor()
    sql = """
        SELECT * FROM cliente;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()
    # Printar a lista
    print("======== LISTANDO CLIENTES =========")
    for cliente in lista:
        print("""
        ID: {}
        NOME: {}
        CPF: {}
        DATA DE NASCIMENTO: {}
        CELULAR: {}
        EMAIL: {}
        """.format(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]))
    input("Pressione Enter para continuar...")
    os.system("cls")

#################################################################
def excluir_cliente(conexao):
    cursor = conexao.cursor()
    x = 0
    x = int(input("Informe o ID do usuário que deseja deletar: "))
    sql = '''
        DELETE FROM cliente WHERE idcliente = {};
    '''.format(x)
    print("Cliente deletado com sucesso!")
    input("Pressione Enter para continuar...")
    os.system("cls")

    cursor.execute(sql)

    conexao.commit()

#################################################################

def confirmar_pagamento(conexao):
    cursor = conexao.cursor()
    continuar = ""
    valort = 0
    while(continuar != 'N'):
        jogo = ""
        print("-> Caso não souber o ID do jogo, apenas pressione ENTER...")

        while(jogo == ""):
            jogo = input("ID do jogo comprado: ")

            if(jogo == ""):
                print("======== LISTA DE JOGOS CADASTRADOS ========\n")
  
                sql = """
                    SELECT idjogo, nome_jogo FROM jogos;
                """
                cursor.execute(sql)
                lista = cursor.fetchall()
    
                for jogos in lista:
                    print("""         ID do Jogo: {}         \n         Nome do Jogo: {}
                    """.format(jogos[0],jogos[1]))
                print("=============================================")    
            else:
                jogo = int(jogo)

        qtd = int(input("Quantidade comprada: "))
        sql = """
            SELECT preco FROM jogos
            WHERE idjogo = {};
        """.format(jogo)
        cursor.execute(sql)
        lista = cursor.fetchone()

        valor = lista[0]
        valor = float(valor)
        valort = valort + (valor * qtd)
        print("Valor total da compra: R$",valort)

        sql = '''
            UPDATE estoque SET
            qtd_estoque = qtd_estoque - {}
            WHERE idjogo = {};
        '''.format(qtd,jogo)
        continuar = input("Continuar adicionando produtos ao pedido?(S/N)  ")

        cursor.execute(sql)
        conexao.commit()

    #troco
    recebido = float(input("Valor recebido do cliente: R$ "))
    print("Valor total da compra: R$ ", valort)
    troco = recebido - valort

    if (troco == 0.00):
        print("Não possui troco!")
    else:
        print("Valor do troco: R$", troco)

    print("Compra finalizada com sucesso!")
    input("Pressione Enter para continuar...")
    os.system("cls")
#################################################################


    

    

