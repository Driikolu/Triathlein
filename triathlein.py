from utils.stadium import Stadium
from utils.runner import Runner
import math
import random


class Triathlein:

    def __init__(self):
        self.players = []
        self.stadium = Stadium()
        self.winners = []
        self.nb_winner = None

    def add_runner(self, runner_name, runner_twitch_points):
        '''Ajoute un participant au Triathlein'''
        self.players.append(Runner(runner_name, runner_twitch_points))
        self.calc_nb_winner()
        random.shuffle(self.players)
    
    def calc_nb_winner(self):
        '''Calcule combien il faut de séléctionné par course pour une finale digne de ce nom'''
        self.nb_winner = 8 // math.ceil(len(self.players)/8)

    
    def start(self):
        '''Lance la totalité des courses'''

        #On lance toutes les courses et on garde les vainqueurs
        for i in range(math.ceil(len(self.players)/8)):
            runners = self.players[i*8:(i+1)*8]
            for r in runners:
                self.stadium.add_runner(r)
        
            self.stadium.start()
            self.winners += sorted(self.stadium.runners,key= lambda runner : runner.position,reverse=True)[:self.nb_winner]
            self.stadium.clear_runners()
        
        #On lance la finale
        for r in self.winners:
            r.reset()
            self.stadium.add_runner(r)
        self.stadium.start()


    


if __name__=="__main__":
    '''Un jeu de test un peu nul'''
    t = Triathlein()
    for r in ['Lein','Driikolu AKA The best','Xx_DarkGauffrette_xX','LePoulpeDu78','Jean-Claude', 'Banana Split','el famoso plancton','Kirikou','Carlos Tentacule','Radis de l\'espace','Polo le deglingo','Arashtoo','Yomy','Sarazar']:
        power=random.randint(0,30000)
        t.add_runner(r,power)
    t.start()
