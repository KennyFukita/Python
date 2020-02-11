def criar_tabela_genero_jogos(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS generos (
                idgenero INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                genero TEXT NOT NULL
            ); '''
    # Executa o SQL
    cursor.execute(sql)

##############################################
def inserir_genero(conexao):
    cursor = conexao.cursor()
    genero = input("Gênero: ")

    sql = '''
        INSERT INTO generos(genero) VALUES(
            '{}'
        );
    '''.format(genero)
    cursor.execute(sql)
    conexao.commit()

#############################################################
def listar_generos(conexao):
    cursor = conexao.cursor()
    sql = """
        SELECT * FROM generos;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()
    # Printar a lista
    print("======== LISTANDO GÊNEROS =========")
    for generos in lista:
        print("""
        ID do Gênero: {}
        Gênero: {}
        """.format(generos[0], generos[1]))

##############################################
def criar_tabela_jogos(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS jogos (
                idjogo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_jogo TEXT NOT NULL,
                preco DECIMAL(8,2) NOT NULL,
                produtora TEXT NOT NULL,
                plataformas TEXT NOT NULL,
                idgenero INTEGER REFERENCES generos(idgenero) 
            ); '''
    # Executa o SQL
    cursor.execute(sql)

############################################################################
def criar_tabela_estoque(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS estoque (
                idjogo INTEGER PRIMARY KEY AUTOINCREMENT REFERENCES jogos (idjogo),
                qtd_estoque INTEGER NOT NULL
            ); '''
            
    # Executa o SQL
    cursor.execute(sql)
##################################################################################

def inserir_jogos(conexao):
    cursor = conexao.cursor()
    nome_jogo = input("Nome do Jogo: ")
    preco = input("Preço do Jogo: R$ ")
    produtora = input("Produtora: ")
    plataformas = input("Plataformas disponíveis: ")
    idgenero = int(input("Gênero do Jogo: "))
    qtd_estoque = int(input("Quantidade em Estoque: ")) 
    sql = '''
        INSERT INTO jogos (nome_jogo, preco, produtora, plataformas, idgenero) VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
        );
    '''.format(nome_jogo, preco, produtora, plataformas, idgenero)
    cursor.execute(sql)
    conexao.commit()

    sql = '''
        INSERT INTO estoque(qtd_estoque) VALUES(
            '{}'
        );
    '''.format(qtd_estoque)  
    cursor.execute(sql)
    conexao.commit()
    

#################################################################
def listar_jogos(conexao):
    cursor = conexao.cursor()
   
    sql = """
        SELECT generos.genero, jogos.nome_jogo, jogos.preco, jogos.produtora, jogos.plataformas, jogos.idgenero
        FROM generos INNER JOIN jogos
        ON generos.idgenero = jogos.idgenero;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()
    # Printar a lista
    print("======== LISTANDO JOGOS =========")
    for jogos in lista:
        print("""
        Nome do Jogo: {}
        Preço do Jogo: R$ {}
        Produtora: {}
        Plataformas Disponíveis: {}
        Gênero do Jogo: {}
        """.format(jogos[1], jogos[2], jogos[3], jogos[4], jogos[5]))
        
            

#################################################################
def excluir_jogos(conexao):
    cursor = conexao.cursor()
    x = 0
    x = int(input("Informe o ID do jogo que deseja deletar: "))
    sql = '''
        DELETE FROM jogos WHERE rowid = {};
    '''.format(x)

    cursor.execute(sql)
    conexao.commit()


def exibirGeneros(conexao):
    cursor = conexao.cursor()

    sql = """
        SELECT preco
        FROM jogos
        WHERE idjogo = 1;
    """
    cursor.execute(sql)
    lista = cursor.fetchone()

    preco = lista[0]
    print(preco)
