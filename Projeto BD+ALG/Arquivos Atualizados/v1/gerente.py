def jogos_em_falta(conexao):
    print("======== LISTANDO JOGOS EM FALTA NO ESTOQUE =========")
    sql = """
        SELECT * FROM cliente;
    """