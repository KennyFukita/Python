import sqlite3
import os
import funcionario
import jogos
import gerente
import menup
from colorama import init, Fore
init(autoreset=True)

################################
###### Programa principal ######
################################

conexao = sqlite3.connect("banco.sqlite")

########### PROCECDIMENTOS/FUNÇÕES ########### 
funcionario.criar_tabela_cliente(conexao)
jogos.criar_tabela_genero_jogos(conexao)
jogos.criar_tabela_jogos(conexao)
jogos.criar_tabela_estoque(conexao)
gerente.criar_tabela_funcionarios(conexao)
gerente.inserir_Adm(conexao)

##############################################
print(Fore.LIGHTMAGENTA_EX + "Iniciando o sistema...")
input(Fore.LIGHTMAGENTA_EX + "Pressione Enter para iniciar...")
os.system("cls")

while (True):
    print(Fore.LIGHTMAGENTA_EX + "~~ ~~ ~~ ENTRE NO SISTEMA ~~ ~~ ~~")
    x = menup.login(conexao)
    os.system("cls")
    if(x):
        if(x[0][1] == "adm"):
            while(True):
                menup.menu_adm()
                escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                os.system("cls")
                
                if(escolha == 1):
                    escolha = 0
                    print(Fore.LIGHTCYAN_EX + "1.", Fore.WHITE + "Cadastrar Cliente(s)")
                    print(Fore.LIGHTCYAN_EX + "2.", Fore.WHITE + "Excluir Cliente(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    
                    if(escolha == 1):
                        os.system("cls")
                        funcionario.inserir_cliente(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        funcionario.excluir_cliente(conexao)
                    else:
                        os.system("cls")
                        break
                
                elif(escolha == 2):
                    escolha = 0
                    print(Fore.LIGHTCYAN_EX + "1.", Fore.WHITE + "Cadastrar Jogo(s)")
                    print(Fore.LIGHTCYAN_EX + "2.", Fore.WHITE + "Excluir Jogo(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    if(escolha == 1):
                        os.system("cls")
                        jogos.inserir_jogos(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        jogos.excluir_jogos(conexao)
                    else:
                        os.system("cls")
                        break
                
                elif(escolha == 3):
                    escolha = 0
                    print(Fore.LIGHTCYAN_EX + "1.", Fore.WHITE + "Cadastrar Gênero(s)")
                    print(Fore.LIGHTCYAN_EX + "2.", Fore.WHITE + "Excluir Gênero(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    if(escolha == 1):
                        os.system("cls")
                        jogos.inserir_generos(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        jogos.excluir_generos(conexao)
                    else:
                        os.system("cls")
                        break

                elif(escolha == 4):
                    print(Fore.LIGHTCYAN_EX + "1.", Fore.WHITE + "Cadastrar Funcionário(s)")
                    print(Fore.LIGHTCYAN_EX + "2.", Fore.WHITE + "Excluir Funcionário(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    if(escolha == 1):
                        os.system("cls")
                        gerente.inserir_funcionarios(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        gerente.excluir_funcionario(conexao)
                    else:
                        os.system("cls")
                        break

                elif(escolha == 5):
                    funcionario.confirmar_pagamento(conexao)

                elif(escolha == 6): 
                    jogos.listar_jogos(conexao)
                
                elif(escolha == 7):
                    jogos.listar_generos(conexao)

                elif(escolha == 8):
                    arquivo = open("relatório_jogos.txt", "w")
                    gerente.relatorio_jogos_faltando(conexao, arquivo)
                    arquivo.close()
                    
                elif(escolha == 9):
                    break

                else:
                    input(Fore.RED + "Opção Inválida!\nPressione ENTER para continuar...")
                    os.system("cls")
        else:
            while(True):
                menup.menu_funcio()
                escolha = int(input(Fore.GREEN + "-> Escolha uma opção: "))
                os.system("cls")
                if(escolha == 1):
                    escolha = 0
                    print(Fore.LIGHTGREEN_EX + "1.", Fore.WHITE + "Cadastrar Cliente(s)")
                    print(Fore.LIGHTGREEN_EX + "2.", Fore.WHITE + "Excluir Cliente(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    
                    if(escolha == 1):
                        os.system("cls")
                        funcionario.inserir_cliente(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        funcionario.excluir_cliente(conexao)
                    else:
                        os.system("cls")
                        break
                
                elif(escolha == 2):
                    escolha = 0
                    print(Fore.LIGHTGREEN_EX + "1.", Fore.WHITE + "Cadastrar Jogo(s)")
                    print(Fore.LIGHTGREEN_EX + "2.", Fore.WHITE + "Excluir Jogo(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    if(escolha == 1):
                        os.system("cls")
                        jogos.inserir_jogos(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        jogos.excluir_jogos(conexao)
                    else:
                        os.system("cls")
                        break
                
                elif(escolha == 3):
                    escolha = 0
                    print(Fore.LIGHTGREEN_EX + "1.", Fore.WHITE + "Cadastrar Gênero(s)")
                    print(Fore.LIGHTGREEN_EX + "2.", Fore.WHITE + "Excluir Gênero(s)")
                    escolha = int(input(Fore.CYAN + "-> Escolha uma opção: "))
                    if(escolha == 1):
                        os.system("cls")
                        jogos.inserir_generos(conexao)
                    elif(escolha == 2):
                        os.system("cls")
                        jogos.excluir_generos(conexao)
                    else:
                        os.system("cls")
                        break

                elif(escolha == 4):
                    funcionario.confirmar_pagamento(conexao)

                elif(escolha == 5): 
                    jogos.listar_jogos(conexao)
                
                elif(escolha == 6):
                    jogos.listar_generos(conexao)
                
                elif(escolha == 7):
                    break
                
                else:
                    input(Fore.RED + "Opção Inválida!\nPressione ENTER para continuar...")
                    os.system("cls")
    
conexao.close()
