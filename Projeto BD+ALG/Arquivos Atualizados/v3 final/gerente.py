import jogos
import os
from colorama import init, Fore
init(autoreset=True)

def criar_tabela_funcionarios(conexao):
    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()
    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS funcionarios (
                idfuncio INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                rg TEXT NOT NULL,
                datanasc DATE NOT NULL,
                cell TEXT NOT NULL,
                email TEXT NOT NULL,
                data_admissao DATE NOT NULL,
                salario DECIMAL(8,2) NOT NULL, 
                login TEXT NOT NULL,
                senha TEXT NOT NULL,
                CONSTRAINT uk_cpf UNIQUE (cpf)  
            ); '''
    # Executa o SQL
    cursor.execute(sql)

#################################################################
def inserir_funcionarios(conexao):
    cursor = conexao.cursor()
    nome = input("Nome: ")
    cpf = input("CPF(somente números): ")
    rg = input("RG(somente números): ")
    datanasc = input("Data de Nascimento: ")
    cell = input("Celular: ")
    email = input("Email: ")
    data_admissao = input("Data de admissão: ")
    salario = input("Salário: R$")
    login = input("Login: ")
    senha = input("Senha de acesso: ")

    sql = '''
        INSERT INTO funcionarios(nome, cpf, rg, datanasc, cell, email, data_admissao, salario, login, senha) VALUES(
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}',
            '{}'
        );
    '''.format(nome, cpf, rg, datanasc, cell, email, data_admissao, salario, login, senha)
    input("Pressione Enter para continuar...")
    os.system("cls")
    cursor.execute(sql)
    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()

#################################################################
def inserir_Adm(conexao):
    cursor = conexao.cursor()
    sql = ''' SELECT * FROM funcionarios
              WHERE nome = 'adm'
    '''
    cursor.execute(sql)
    
    lista = cursor.fetchall()
    if(not lista):
        sql = ''' INSERT INTO funcionarios(nome, cpf, rg, datanasc, cell, email, data_admissao, salario, login, senha)
                  VALUES('adm', 06995818123, 159422863, 27/01/1995, 44999442299, 'adm@gmail.com', 12/05/2015, 3000, 'adm', 'adm2019')
        '''
        cursor.execute(sql)
        conexao.commit()

#################################################################        
def listar_funcionarios(conexao):
    cursor = conexao.cursor()
    sql = """
        SELECT * FROM funcionarios;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()
    # Printar a lista
    print(Fore.LIGHTMAGENTA_EX + "======== LISTANDO FUNCIONARIOS =========")
    for funcionarios in lista:
        print("""
        ID: {}
        NOME: {}
        CPF: {}
        RG: {}
        DATA DE NASCIMENTO: {}
        CELULAR: {}
        EMAIL: {}
        DATA DE ADMISSÃO: {}
        SALÁRIO: R${}
        LOGIN: {}
        SENHA: {}
        """.format(funcionarios[0], funcionarios[1], funcionarios[2], funcionarios[3], funcionarios[4], funcionarios[5], funcionarios[6], funcionarios[7], funcionarios[8], funcionarios[9],  funcionarios[10]))
    input("Pressione Enter para continuar...")
    os.system("cls")

#################################################################
def excluir_funcionario(conexao):
    cursor = conexao.cursor()
    x = 0
    x = int(input("Informe o ID do funcionário que deseja deletar: "))
    sql = '''
        DELETE FROM funcionarios WHERE idfuncio = {};
    '''.format(x)
    print("Funcionário deletado com sucesso!")
    input("Pressione Enter para continuar...")
    os.system("cls")

    cursor.execute(sql)

    conexao.commit()

#################################################################
def estoque_jogos(conexao):
    cursor = conexao.cursor()
    print(Fore.LIGHTMAGENTA_EX + "======== LISTANDO ESTOQUE DOS JOGOS =========")
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
    input("Pressione Enter para continuar...")
    os.system("cls")    

####################################################################################
def relatorio_jogos_faltando(conexao, arquivo):
    cursor = conexao.cursor()
    
    sql = """
        SELECT jogos.idjogo, jogos.nome_jogo, estoque.qtd_estoque
        FROM estoque INNER JOIN jogos 
        ON estoque.idjogo = jogos.idjogo
        WHERE estoque.qtd_estoque < 3;
    """
    cursor.execute(sql)
    lista = cursor.fetchall()

    for u in lista:
        arquivo.write("ID do Jogo: {}\n".format(u[0]))
        arquivo.write("Nome do Jogo: {}\n".format(u[1]))
        arquivo.write("Quantidade em Estoque: {}\n".format(u[2]))
        arquivo.write("-~--~--~--~--~--~--~--~--~--~-\n")
      

###############################################################################

            
        

    

        
                
        
   
   

