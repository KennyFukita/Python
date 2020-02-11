def criar_tabela_genero_jogos(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS generos (
                idgenero SERIAL NOT NULL PRIMARY KEY,
                genero TEXT NOT NULL
            ); '''
    # Executa o SQL
    cursor.execute(sql)

##############################################
def inserir_genero(conexao):
    cursor = conexao.cursor()
    idgenero = int(input("ID do Gênero: "))
    genero = input("Gênero: ")

    sql = '''
        INSERT INTO generos VALUES(
            '{}',
            '{}'
        );
    '''.format(idgenero, genero)
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
                idjogo SERIAL NOT NULL PRIMARY KEY,
                nome_jogo TEXT NOT NULL,
                preco NUMERIC(8,2) NOT NULL,
                produtora TEXT NOT NULL,
                plataformas TEXT NOT NULL,
                idgenero INTEGER REFERENCES generos(idgenero) 
            ); '''
    # Executa o SQL
    cursor.execute(sql)
# INTEGER REFERENCES criar_tabela_genero_jogos(idgenero) 
# idgenero INTEGER NOT NULL
                # FOREIGN KEY(idgenero) REFERENCES generos(idgenero)  
############################################################################
def criar_tabela_estoque(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS estoque (
                idjogo SERIAL NOT NULL PRIMARY KEY REFERENCES jogos (idjogo),
                qtd_estoque INTEGER NOT NULL
            ); '''
    # Executa o SQL
    cursor.execute(sql)
##################################################################################

def inserir_jogos(conexao):
    cursor = conexao.cursor()
    idjogo = int(input("ID do Jogo: "))
    nome_jogo = input("Nome do Jogo: ")
    preco = input("Preço do Jogo: R$ ")
    produtora = input("Produtora: ")
    plataformas = input("Plataformas disponíveis: ")
    idgenero = int(input("Gênero do Jogo: "))
    qtd_estoque = int(input("Quantidade em Estoque: ")) 
    sql = '''
        INSERT INTO jogos VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
        );
    '''.format(idjogo, nome_jogo, preco, produtora, plataformas, idgenero)
    cursor.execute(sql)
    conexao.commit()

    sql = '''
        INSERT INTO estoque VALUES(
            '{}',
            '{}'
        );
    '''.format(idjogo, qtd_estoque)  
    cursor.execute(sql)
    conexao.commit()
    

#################################################################
def listar_jogos(conexao):
    cursor = conexao.cursor()
   
    sql = """
        SELECT generos.genero, jogos.idjogo, jogos.nome_jogo, jogos.preco, jogos.produtora, jogos.plataformas, jogos.idgenero
        FROM generos INNER JOIN jogos
        ON generos.idgenero = jogos.idgenero;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()
    # Printar a lista
    print("======== LISTANDO JOGOS =========")
    for jogos in lista:
        print("""
        ID do Jogo: {}
        Nome do Jogo: {}
        Preço do Jogo: R$ {}
        Produtora: {}
        Plataformas Disponíveis: {}
        Gênero do Jogo: {}
        """.format(jogos[1], jogos[2], jogos[3], jogos[4], jogos[5], jogos[0]))
        
            

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