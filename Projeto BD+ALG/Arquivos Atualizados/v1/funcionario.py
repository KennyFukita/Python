###################### FUNCIONARIO ######################
import jogos
# Procedimento que recebe uma conexão e cria uma tabela
def criar_tabela_cliente(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS cliente (
                idcliente SERIAL NOT NULL PRIMARY KEY,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                datanasc DATE NOT NULL,
                cell TEXT NOT NULL,
                CONSTRAINT uk_cpf UNIQUE (cpf)  
            ); '''
    # Executa o SQL
    cursor.execute(sql)

#################################################################
def selecionar_tabela_cliente(conexao):
    cursor = conexao.cursor()
    sql = '''SELECT * FROM jogos;'''
    cursor.execute(sql)

#################################################################
def inserir_cliente(conexao):
    cursor = conexao.cursor()
    idcliente = input ("ID do Cliente: ")
    nome = input("Nome: ")
    cpf = input("CPF(somente números): ")
    datanasc = input("Data de Nascimento: ")
    cell = input("Celular: ")

    sql = '''
        INSERT INTO cliente VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
        );
    '''.format(idcliente, nome, cpf, datanasc, cell)
    cursor.execute(sql)
    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()

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
        """.format(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))

#################################################################
def deletar_cliente(conexao):
    cursor = conexao.cursor()
    x = 0
    x = int(input("Informe o ID do usuário que deseja deletar: "))
    sql = '''
        DELETE FROM cliente WHERE idcliente = {};
    '''.format(x)
    print("Usuário deletado com sucesso!")

    cursor.execute(sql)

    conexao.commit()

#################################################################

def confirmar_pagamento(conexao):
    cursor = conexao.cursor()
    continuar = ""
    valort = 0
    while (continuar != 'N'):
        jogo = int(input("Jogo comprado: "))
        qtd = int(input("Quantidade comprada: "))
        valor = float(input("Preço do jogo: R$"))
        valort = valort + (valor * qtd)
        print("Valor total da compra: R$",valort)
        sql = '''
            UPDATE jogos SET
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

    

#################################################################


    

    

