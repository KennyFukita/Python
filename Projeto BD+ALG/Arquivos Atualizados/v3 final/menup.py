from colorama import init, Fore
init(autoreset=True)
import os

def login(conexao):
    cursor = conexao.cursor()
    login = input("Login: ")
    senha = input("Senha: ")

    sql = ''' SELECT * FROM funcionarios WHERE login = '{}' AND senha = '{}'
    '''.format(login, senha)
    cursor.execute(sql)
    lista = cursor.fetchall()
    # confirm = 0
    for i in range (0, len(lista)):
        if(lista[i][9] == login and lista[i][10] == senha):
            print("Bem Vindo,",Fore.YELLOW + "{}!".format(lista[i][1]))    
            # confirm = 1
            input("Pressione Enter para continuar...")
            os.system("cls")
            return lista
        else:
            print(Fore.RED + "Login ou Senha incorreto(s)!")
            input("Pressione Enter para continuar...")
            os.system("cls")
            return False

######################################
def menu_adm():
    print(Fore.CYAN + "~~ ~~ ~~ ~~ Menu Principal do Sistema ~~ ~~ ~~ ~~")
    print(Fore.LIGHTCYAN_EX + "1.", Fore.WHITE + "Cadastrar/Excluir Clientes")
    print(Fore.LIGHTCYAN_EX + "2.", Fore.WHITE + "Cadastrar/Excluir Jogos")
    print(Fore.LIGHTCYAN_EX + "3.", Fore.WHITE + "Cadastrar/Excluir Gênero de Jogos")
    print(Fore.LIGHTCYAN_EX + "3.", Fore.WHITE + "Cadastrar/Excluir Funcionários")
    print(Fore.LIGHTCYAN_EX + "5.", Fore.WHITE + "Confirmar Compra")
    print(Fore.LIGHTCYAN_EX + "6.", Fore.WHITE + "Listar Jogos Disponíveis")
    print(Fore.LIGHTCYAN_EX + "7.", Fore.WHITE + "Listar Gêneros de Jogos Disponíveis")
    print(Fore.LIGHTCYAN_EX + "8.", Fore.WHITE + "Relatório de Jogos em Falta no Estoque")
    print(Fore.LIGHTCYAN_EX + "9.", Fore.WHITE + "Sair")

########################################
def menu_funcio():
    print(Fore.GREEN + "~~ ~~ ~~ ~~ Menu Principal do Sistema ~~ ~~ ~~ ~~")
    print(Fore.LIGHTGREEN_EX + "1.", Fore.WHITE + "Cadastrar/Excluir Clientes")
    print(Fore.LIGHTGREEN_EX + "2.", Fore.WHITE + "Cadastrar/Excluir Jogos")
    print(Fore.LIGHTGREEN_EX + "3.", Fore.WHITE + "Cadastrar/Excluir Gênero de Jogos")
    print(Fore.LIGHTGREEN_EX + "4.", Fore.WHITE + "Confirmar Compra")
    print(Fore.LIGHTGREEN_EX + "5.", Fore.WHITE + "Listar Jogos Disponíveis")
    print(Fore.LIGHTGREEN_EX + "6.", Fore.WHITE + "Listar Gêneros de Jogos Disponíveis")
    print(Fore.LIGHTGREEN_EX + "7.", Fore.WHITE + "Sair")
        
    
