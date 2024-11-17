import requests
from bs4 import BeautifulSoup
from socket import *
from datetime import datetime
import ftplib
import whois
from colorama import init, Fore
import sqlite3

connect = sqlite3.connect('dba.csv')
cursor = connect.cursor()

connect.commit()



init(autoreset=True)

class WebScrapping:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(Fore.CYAN + "O que deseja procurar?\t")
            search = input(Fore.CYAN + "◇")
            titles = soup.find_all(search)
            print(Fore.CYAN + "Resultados encontrados:")
            for title in titles:
                print(title.text)
        else:
            print(Fore.RED + f"Erro ao acessar o site. Código de status: {response.status_code}")


class PortScan:
    @staticmethod
    def inicio():
        print(Fore.CYAN + 'Conectado com sucesso...')
        print(Fore.CYAN + 'Selecione uma opção:')
        print('\t[1] - Scan Port')
        print('\t[2] - Bruteforce Ftp Server')
        opt = int(input('\t>>> '))
        if opt == 1:
            PortScan.ScanPort()
        elif opt == 2:
            PortScan.brute()

    @staticmethod
    def ScanPort():
        def Buscador(arquivo):
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip = str(input("Digite o IP do servidor: "))
            start = int(input("Porta Inicial: "))
            end = int(input("Porta Final: "))

            arquivo.write(f"{dt} IP do Servidor: {ip}\n")
            arquivo.write(f"{dt} Porta Inicial: {start}\n")
            arquivo.write(f"{dt} Porta Final: {end}\n")
            print(f"Scanning IP {ip}...")
            for port in range(start, end):
                print(f"Teste Port {port}....")
                s = socket(AF_INET, SOCK_STREAM)
                s.settimeout(5)
                if s.connect_ex((ip, port)) == 0:
                    print(f"Porta {port} aberta")
                    arquivo.write(f"{dt} Porta Aberta: {port}\n")
                s.close()

        def WriteLog():
            msg = "Scanneamento finalizado com sucesso."
            try:
                with open("ScannerPort.log", "w") as arquivo:
                    Buscador(arquivo)
            except Exception as e:
                msg = f"Erro: {e}"
            finally:
                print(msg)

        WriteLog()

    @staticmethod
    def brute():
        try:
            ip = str(input("Digite o IP do servidor FTP: "))
            ftp_login = str(input("Login do usuário FTP: "))
            wordlist = str(input("Digite sua wordlist para iniciar o ataque: "))
            with open(wordlist, 'r') as ler:
                for i in ler.readlines():
                    try:
                        servidor = ftplib.FTP(ip)
                        servidor.login(ftp_login, i.rstrip())
                        print("Senha encontrada! ", i.rstrip())
                        raise SystemExit
                    except ftplib.error_perm:
                        print("Senha incorreta! ", i.rstrip())
        except KeyboardInterrupt:
            print("Fim do Programa!")

class reques:
	def __init__(self):
		pass
	def get(self):
		url = input("Digite a Url:\t• ")
		response = requests.get(url)
		print(response.status_code)
		print(response.text)
	def post(self):
		pass


class WhoisConsulta:
    @staticmethod
    def consulta():
        print("\nDigite o domínio:")
        dominio = input(">> ")
        info = whois.whois(dominio)
        print("\nDomínio registrado em:", info.creation_date)
        print("\nÚltima atualização:", info.updated_date)
        print("\nExpiração:", info.expiration_date)
        print("\nRegistrador:", info.registrar)
        print("\nServidores WHOIS:", info.whois_server)




# Menu principal --> Estrutura de Arquitetura do App.
while True:
    data = datetime.now()
    print(Fore.CYAN + f"{data}\tMANPHIS.PY\t\tV1.0\n")
    print(
        """
.  . .-. . . .-. . . .-. .-.
|\/| |-| |\| |-' |-|  |  `-.
'  ` ` ' ' ` '   ' ` `-' `-'

"""
    )
    print(Fore.CYAN + "\t[1] - WebScrapping \n\t[2] - Port Scan e Bruteforce FTP\n\t[3] - Whois Consulta\n\t[4] - Gerando senhas criptografadas\n\t[5] - Banco de Dados Pessoal SQLite3\n\t[6] - Requests\n\t[exit] - Sair\n\t[help] - Informações e anotações")
    decision_menu = input(Fore.CYAN + "[•]》")
    if decision_menu == "1":
        url = input(Fore.CYAN + "Digite a URL: ")
        scraper = WebScrapping(url)
        scraper.fetch_data()
    elif decision_menu == "2":
        PortScan.inicio()
    elif decision_menu == "3":
        WhoisConsulta.consulta()
    elif decision_menu == "exit":
        print(Fore.GREEN + "Saindo...")
        break
    elif decision_menu == "help":
        print(Fore.BLUE+"\n\nO manphis foi criado com o intuito de realizar análise de dados e segurança.O modelo ainda se encontra na versão protótipo (V1.0) e foi desenvolvido por Bruno Pedrogan Cordeiro, analista de sistemas e investigador digital.\n\n")
    elif decision_menu == "6":
        print(Fore.YELLOW+"\n\tREQUESTS:\n\n1. GET\n2. POST\n")
        decision_reques = input("¤ ")
        if decision_reques == "1":
            reques().get()
    else:
        print(Fore.RED + "Opção inválida!")
        
        
        
        
connect.close()