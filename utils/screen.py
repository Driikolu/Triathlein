import pygame

import time

class Screen:

    def __init__(self,racetrack,width=1500,height=1000,stadium_name="Driikolu Arena"):
        pygame.init()

        self.display = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Grande course dans le stade %s" % stadium_name)

        self.font = pygame.font.SysFont(None,24)

        self.clock = pygame.time.Clock()

        self.racetrack = pygame.image.load(racetrack).convert()
        self.display.blit(self.racetrack,(0,0))

        pygame.display.update()
        self.clock.tick(60)


    def display_runners(self,runners):
        '''Affiche les courreurs sur la course et centre sur le 1er courreur'''

        #On récupère le premier courreur
        first=max([runner.position//15 + 20 for runner in runners])
        racetrack_x=0

        #On vérifie s'il dépasse la moitié de l'écran pour centrer, ou non, sur sa position
        if first>self.display.get_width()//2:
            racetrack_x = - min(first-self.display.get_width()//2, self.racetrack.get_width()-self.display.get_width()//2)
        
        #On affiche le terrain de course
        self.display.blit(self.racetrack,(racetrack_x,0))
        
        #On ajoute chaque courreurs et leurs noms
        for i in range(len(runners)):
            runner=runners[i]
            
            runner_img = pygame.image.load(runner.img)
            runner_img.convert_alpha()
            
            y_pos = 400 + 75*i + (i%2==0) 
            x_pos = runner.position // 15 + 20 + racetrack_x

            runner_name = self.font.render(runner.name,True, (0,0,0) )
            y_name = y_pos + runner_img.get_height()
            x_name = x_pos - len(runner.name)*2
            self.display.blit(runner_img, (x_pos,y_pos) )
            self.display.blit(runner_name, (x_name,y_name) )

        pygame.display.update()

    

    def display_infos(self,runners):
        '''Affiche la liste des courreurs ainsi que leurs puissances'''
        while True:
            mouse = pygame.mouse.get_pos()

            #On dessine le tableau d'affichage
            pygame.draw.rect(self.display,(80,35,10) , (195,5,1110,810),border_radius=10)
            pygame.draw.rect(self.display,(115,50,15) , (200,10,1100,800))
            for i in range(8):
                pygame.draw.line(self.display, (80,35,10), (200,10+100*i) , (1300,10+100*i), width=3)

            pygame.draw.line(self.display, (80,35,10), (1000, 10), (1000,810), width=3)

            info_font = pygame.font.SysFont(None,65)
            
            #On affiche les nom & puissances des courreurs
            for i in range(len(runners)):
                runner = runners[i]

                name = info_font.render(runner.name, True, (255,255,255))
                power = info_font.render(str(runner.power), True, (230,230,20))

                self.display.blit(name, (210, 30 + 100*i))
                self.display.blit(power, (1010, 30 + 100*i))

             
            #On vérifie si la souris est sur le bouton "RACE" pour le grossir un peu
            if 700<mouse[0]<900 and 850<mouse[1]<900:
                pygame.draw.rect(self.display, (180,0,20), (700, 850, 200, 100), border_radius=20)
            else:
                pygame.draw.rect(self.display, (230,0,40), (700, 850, 200, 100), border_radius=20)

            RACE = info_font.render("RACE !", True, (0,0,0) )
            self.display.blit(RACE, (725,880))
            
            #Si on appuie sur le bouton "RACE", on quitte l'affichage
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 700<mouse[0]<900 and 850<mouse[1]<900:
                        return 0
            pygame.display.update()





            
    def display_winner(self,winner):
        '''Affiche le nom du vainqueur'''

        while True:
            mouse = pygame.mouse.get_pos()
            info_font = pygame.font.SysFont(None,65)
            
            winning_font = pygame.font.SysFont(None,100)
            back_print = winning_font.render("%s est le vainqueur !" % winner.name, True, (0,0,0) )
            to_print = winning_font.render("%s est le vainqueur !" % winner.name, True, (190,20,150) )
            
            y=self.display.get_height()//2
            winning_x = (self.display.get_width()-to_print.get_width())//2
            
            #Pour avoir un petit contour tout mignon
            self.display.blit(back_print, (winning_x-2,y))
            self.display.blit(back_print, (winning_x+2,y))
            self.display.blit(back_print, (winning_x,y-2))
            self.display.blit(back_print, (winning_x,y+2))
            self.display.blit(to_print, (winning_x,y) )
            pygame.display.update()

            #On vérifie si la souris est sur le bouton "NEXT" pour le grossir un peu
            if 700<mouse[0]<900 and 850<mouse[1]<900:
                pygame.draw.rect(self.display, (180,0,20), (700, 850, 200, 100), border_radius=20)
            else:
                pygame.draw.rect(self.display, (230,0,40), (700, 850, 200, 100), border_radius=20)

            
            next_button = info_font.render("Next !", True, (0,0,0) )
            self.display.blit(next_button, (725,880))

            #Si on appuie sur le bouton "NEXT", on quitte l'affichage
            for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if 700<mouse[0]<900 and 850<mouse[1]<900:
                            return 0
            pygame.display.update()


                
