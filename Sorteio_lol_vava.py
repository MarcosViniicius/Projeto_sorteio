from ast import Break
from random import choice
import random
import time

class Sorteios:
    def __init__(self):
        self.menu()

    def sorteio_lol(self):
        campeoes = ['Ahri', 'Akali', 'akshan', 'amumu','alistar', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'aatrox', 'azir', 'bardo', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'cho gath', 'corki', 'darius', 'diana', 'dr mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddle', 'galio', 'fiora', 'fizz', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'gwen', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'JANNA', 'jarvan', 'jax', 'jayce', 'jhin', 'jinx', 'kaisa', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'kha zix', 'kindred', 'kled', 'kog maw', 'le blanc', 'lee sin', 'leona', 'lilian', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar','maokai', 'master yi', 'miss fortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunu e willump', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'ranmus', 'rek sai', 'rell', 'renata glasc', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine','sett', 'shaco', 'shen', 'shyvana','singed','sion', 'sivir ','skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahm kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'vel koz', 'vex', 'VI', 'viego', 'viktor', 'vladmir', 'voliber', 'warwick', 'wukong', 'xayah', 'xerath', 'xin zhao', 'yasuo', 'yone','yorick', 'yuumi', 'zac', 'zed', 'zeri', 'ziggs', 'zilean', 'zoe', 'zyra']
        sorteio = random.choice(campeoes)
        return sorteio.upper()

    def sorteio_vava(self):
        agentes = ['Brimstone', 'Phoenix', 'Sage', 'Sova', 'Viper', 'Chypher', 'Reyna','Killjoy', 'Breach', 'Omen', 'Jett', 'Raze', 'Skye', 'Yoru', 'Astra', 'Kay/o', 'Chamber', 'Fade', 'Omen']
        sorteio = random.choice(agentes)
        return sorteio.upper()

    def menu(self):
        menu_principal = int(input('BEM VINDO AO MENU PRINCIPAL!\n\nEscolha o tipo de sorteio.\n\n1.Sorteio de personagens\n2.Sorteio de posições/lanes\n\nESCOLHA UMA OPÇÃO: '))
        if menu_principal == 1:
            print(self.menu_personagens())
        elif menu_principal == 2:
            print(self.menu_posicoes())
        else:
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.menu()
        
    def menu_personagens(self):
        escolha_personagens = int(input('BEM VINDO AO MENU DE SORTEIOS\n\nEscolha um sorteio.\n\nSorteio de personagens:\n1. VALORANT\n2. LEAGUE OF LEGENDS\n\nESCOLHA UMA OPÇÃO: '))
        if escolha_personagens == 1:
            print(f'Seu agente sorteado foi {self.sorteio_vava()}')
            time.sleep(1)
            return self.escolha_depois_sorteio()
        elif escolha_personagens == 2:
            print(f'Seu campeão sorteado foi {self.sorteio_lol()}')
            time.sleep(1)
            return self.escolha_depois_sorteio()
        else:
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.menu_personagens()
            
    def menu_posicoes(self):
        print('Em desenvolvimento')

    def escolha_depois_sorteio(self):
        depois_sorteio = int(input('\n\nEscolha uma opção.\n\n1. Menu principal\n2. Menu de personagens\n3. SAIR DO PROGRAMA\n\nESCOLHA UMA OPÇÃO: '))
        if depois_sorteio == 1:
            return self.menu()
        elif depois_sorteio == 2:
            return self.menu_personagens()
        elif depois_sorteio == 3:
            Break
        else:
            print("\nERRO:\nEscolha uma opção válida.\nVoltando ao menu de escolha...\n")
            return self.escolha_depois_sorteio()

sorteio = Sorteios()
