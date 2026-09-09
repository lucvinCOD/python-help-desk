import platform
import socket
import os
import getpass
import shutil


def informacoes_computador():
    print("\n===== INFORMAÇÕES DO COMPUTADOR =====")

    print("Nome do computador:", socket.gethostname())
    print("Usuário:", getpass.getuser())
    print("Sistema operacional:", platform.system())
    print("Versão do sistema:", platform.release())
    print("Arquitetura:", platform.machine())
    print("Processador:", platform.processor())
    print("Núcleos lógicos:", os.cpu_count())

def testar_internet():
    print("\n===== TESTE DE CONEXÃO COM A INTERNET =====")
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        print("Conexão com a internet: OK")
    except OSError:
        print("Conexão com a internet: Falha")

def testar_dns():
    print("\n===== TESTE DE DNS =====")
    try:
        ip = socket.gethostbyname("google.com")
        print("Resolução de DNS: OK")
        print("google.com resolvido para:", ip)
    except socket.gaierror:
        print("Resolução de DNS: Falha")

def testar_porta():
    print("\n===== TESTE DE PORTA TCP =====")
    host = input("Digite o endereço do servidor: ")
    
    try:
        porta = int(input("Digite a porta: "))
        conexao = socket.create_connection((host, porta), timeout=3)
        print(f"Porta {porta} em {host}: ABERTA")
        conexao.close()

    except ValueError:
        print("Porta inválida. Por favor, insira um número inteiro.")
    except OSError:
        print(f"Porta {porta} em {host}: FECHADA ou INACESSÍVEL")

def verificar_armazenamento():
    print("\n===== VERIFICAR ARMAZENAMENTO =====")
    total, usado, livre = shutil.disk_usage("C:\\")
    gb = 1024 ** 3
    print(f"Espaço total: {total / gb:.2f} GB")
    print(f"Espaço usado: {usado / gb:.2f} GB")
    print(f"Espaço livre: {livre / gb:.2f} GB")

while True:
    print("\n=========================================")
    print("       HELP DESK DIAGNOSTIC TOOL")
    print("=========================================")

    print("1 - Informações do computador")
    print("2 - Testar conexão com a internet")
    print("3 - Testar DNS")
    print("4 - Testar porta TCP")
    print("5 - Verificar armazenamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        informacoes_computador()

    elif opcao == "2":
        testar_internet()

    elif opcao == "3":
        testar_dns()

    elif opcao == "4":
        testar_porta()

    elif opcao == "5":
        verificar_armazenamento()

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")