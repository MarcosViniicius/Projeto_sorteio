from ast import Break
from random import choice
import random
import time
import os


class Sorteios:
    def __init__(self):
        self.menu()

    def sorteio_lol(self):
        campeoes = ['Ahri', 'Akali', 'akshan', 'amumu','alistar', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'aatrox', 'azir', 'bardo', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'cho gath', 'corki', 'darius', 'diana', 'dr mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddle', 'galio', 'fiora', 'fizz', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'JANNA', 'jarvan', 'jax', 'jayce', 'jhin', 'jinx', 'kaisa', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'kha zix', 'kindred', 'kled', 'kog maw', 'le blanc', 'lee sin', 'leona', 'lilian', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar','maokai', 'master yi', 'miss fortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunu e willump', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'ranmus', 'rek sai', 'rell', 'renata glasc', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine','sett', 'shaco', 'shen', 'shyvana','singed','sion', 'sivir ','skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahm kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'vel koz', 'vex', 'VI', 'viego', 'viktor', 'vladmir', 'voliber', 'warwick', 'wukong', 'xayah', 'xerath', 'xin zhao', 'yasuo', 'yone','yorick', 'yuumi', 'zac', 'zed', 'zeri', 'ziggs', 'zilean', 'zoe', 'zyra']
        sorteio = random.choice(campeoes)
        return sorteio.upper()

    def sorteio_vava(self):
        agentes = ['Brimstone', 'Phoenix', 'Sage', 'Neon', 'Sova', 'Viper', 'Chypher', 'Reyna','Killjoy', 'Breach', 'Omen', 'Jett', 'Raze', 'Skye', 'Yoru', 'Astra', 'Kay/o', 'Chamber', 'Fade', 'Omen']
        sorteio = random.choice(agentes)
        return sorteio.upper()

    def menu(self):
        menu_principal = int(input('BEM VINDO AO MENU PRINCIPAL!\n\nEscolha o tipo de sorteio.\n\n1.Sorteio de personagens\n2.Sorteio de posições/lanes\n4.SAIR DO PROGRAMA\n\n10. Suporte\n\n\nESCOLHA UMA OPÇÃO: '))
        if menu_principal == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.menu_personagens())
        elif menu_principal == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.menu_posicoes())
        elif menu_principal == 10:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Para reportar bugs e/ou dar ideias de jogos para o programa usar os seguintes meios de contato.\n\nTwitter: @MaRcOsViNiCiUx\nDiscord: KAmPeR-SA#1532\n\n')
            return self.menu_voltar()
        elif menu_principal == 4:
            print('Obrigado por usar o sorteador de personagens!\n\n\n\n\n\n\n\nDesenvolvido por Marcos Vinicius\ntwitter: @MaRcOsViNiCiUx')
            print('programa fechando em')
            time.sleep(1)
            print(5)
            time.sleep(1)
            print(4)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            Break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.menu()

    def menu_voltar(self):
        menu_voltar1 = int(input('\n\nEscolha uma opção.\n\n1. Menu principal\n\nESCOLHA UMA OPÇÃO: '))
        if menu_voltar1 == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Obrigado por usar o sorteador de personagens!\n\n\n\n\n\n\n\nDesenvolvido por Marcos Vinicius\ntwitter: @MaRcOsViNiCiUx')
            print('programa fechando em')
            return self.menu()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.menu_voltar()
        
    def menu_personagens(self):
        escolha_personagens = int(input('BEM VINDO AO MENU DE SORTEIOS\n\nEscolha um sorteio.\n\nSorteio de personagens:\n1. VALORANT\n2. LEAGUE OF LEGENDS\n\nESCOLHA UMA OPÇÃO: '))
        if escolha_personagens == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Seu agente sorteado foi {self.sorteio_vava()}')
            time.sleep(1)
            return self.escolha_depois_sorteio()
        elif escolha_personagens == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Seu campeão sorteado foi {self.sorteio_lol()}')
            time.sleep(1)
            return self.escolha_depois_sorteio()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.menu_personagens()
            
    def menu_posicoes(self):
        print('Esse local ainda está em desenvolvimento.')
        time.sleep(3)
        print('Voltando ao Menu...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return self.menu()

    def escolha_depois_sorteio(self):
        depois_sorteio = int(input('\n\nEscolha uma opção.\n\n1. Menu principal\n2. Menu de personagens\n3. SAIR DO PROGRAMA\n\nESCOLHA UMA OPÇÃO: '))
        if depois_sorteio == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            return self.menu()
        elif depois_sorteio == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            return self.menu_personagens()
        elif depois_sorteio == 3:
            print('Obrigado por usar o sorteador de personagens!\n\n\n\n\n\n\n\nDesenvolvido por Marcos Vinicius\ntwitter: @MaRcOsViNiCiUx')
            print('programa fechando em')
            time.sleep(1)
            print(5)
            time.sleep(1)
            print(4)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            Break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.escolha_depois_sorteio()
        
sorteio = Sorteios()
