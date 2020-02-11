import jogos

def estoque_jogos(conexao):
    cursor = conexao.cursor()
    print("======== LISTANDO ESTOQUE DOS JOGOS =========")
    sql = """
        SELECT jogos.idjogo, jogos.nome_jogo, estoque.qtd_estoque
        FROM estoque INNER JOIN jogos 
        ON estoque.idjogo = jogos.idjogo;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()
    for jogos in lista:
        print("""
        ID do Jogo: {}
        Nome do Jogo: {}
        Quantidade em Estoque: {}
        """.format(jogos[0], jogos[1], jogos[2]))

####################################################################################
