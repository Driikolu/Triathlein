from .runner import Runner
from .screen import Screen
import os

class Stadium:

    def __init__(self,race_length=41415, name = "Driikolu Arena", img_name="stadium.jpg",screen_width=1500,screen_height=1000):
        self.name = name
        self.runners =  []
        self.length = race_length
        self.img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs", img_name)
        self.finishers=[]
        self.screen = Screen(self.img,screen_width,screen_height,name)

    def add_runner(self, runner_name, runner_twitch_points):
        '''Créé et ajoute un coureur dans le stade'''
        self.runners.append(Runner(runner_name, runner_twitch_points))

    def add_runner(self,runner):
        '''Ajoute un coureur déjà créé dans le stade'''
        self.runners.append(runner)

    
    def clear_runners(self):
        '''Supprime tous les courreurs (pour faire de la place pour la course suivante)'''
        self.runners = []



    def tick(self):
        '''Fait effectuer à chaque courreur un déplacement'''
        for r in self.runners:
            if r.position<self.length:
                r.run()


    def get_fastest_runners(self):
        '''Retourne une liste contenant des objets Runner
        Cette liste doit contenir uniquement le ou les joueurs les plus avancés (en cas d'égalité)'''
        fastest=[]
        longest=0
        for r in self.runners:
            if r.position==longest:
                fastest.append(r)
            elif r.position>longest:
                fastest=[r]
                longest=r.position
        return fastest
        #pass
        #return list

    def has_winner(self):
        '''Vérifie si un des courreurs a atteint l'arrivée
        Si 2 courreurs ou plus ont atteint/dépassé l'arrivée, le plus avancé gagne
        S'il y a courreurs joueurs à la même distance après l'arrivée, on les refait courir jusqu'à ce qu'un vainqueur soit trouvé

        Retourne un booléen'''
        fastest = self.get_fastest_runners()
        if len(fastest)==1 and fastest[0].position>=self.length:
            return True
        else:
            return False

        #pass
        #return boolean

    def run(self):
        '''Lance la course'''
        stop=False
        while not self.has_winner():
            self.tick()
            self.screen.display_runners(self.runners)
        winner = self.get_fastest_runners()[0]
        self.screen.display_winner(winner)

    def start(self):
        '''Affiche les courreurs puis lance la course'''
        self.screen.display_infos(self.runners)
        self.run()





