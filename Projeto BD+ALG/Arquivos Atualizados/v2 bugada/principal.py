import sqlite3
import funcionario
import jogos
import gerente

################################
###### Programa principal ######
################################

conexao = sqlite3.connect("banco.sqlite")

# def deletar_tabela(conexao):
#     cursor = conexao.cursor()
#     sql = '''DROP TABLE jogos;'''
#     cursor.execute(sql)

# deletar_tabela(conexao)
########### PROCECDIMENTOS/FUNÇÕES ########### 

# funcionario.criar_tabela_cliente(conexao)
# funcionario.inserir_cliente(conexao)
# funcionario.listar_cliente(conexao)
# funcionario.deletar_cliente(conexao)
# funcionario.confirmar_pagamento(conexao)
# jogos.criar_tabela_genero_jogos(conexao)
# jogos.criar_tabela_jogos(conexao)
# jogos.criar_tabela_estoque(conexao)
# jogos.inserir_genero(conexao)
# jogos.listar_generos(conexao)
jogos.inserir_jogos(conexao)
# jogos.excluir_jogos(conexao)
# jogos.listar_jogos(conexao)
# gerente.estoque_jogos(conexao)
# jogos.exibirGeneros(conexao)

##############################################
conexao.close()
