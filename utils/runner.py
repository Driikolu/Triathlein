import os
import random

class Runner:
    def __init__(self, name, twitch_points, img_name="runner.png"):
        self.name = name
        self.power = twitch_points
        self.position = 0.
        self.img = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs", img_name)
        self.sprinting = False
        self.sprint_count=10

    def reset(self):
        '''Remet à 0 la position et la possibilité de sprint du courreur pour une nouvelle course'''
        self.position = 0.
        self.sprinting = False
        self.sprint_count=10


    def run(self):
        '''Génère un déplacement aléatoire avec légers avantages selon la "puissance" (points twitchs)'''
        sprint_probability = random.randint(0,200000)+self.power//200
        if self.sprinting!=True and sprint_probability >=199990 and int(self.sprint_count)>0:
            self.sprinting=True
        if self.sprinting==True:
            self.sprint()
        else:
            self.position += random.randint(0,10)
            self.sprint_count+=0.2


    def sprint(self):
        '''On fait sprinter le courreur'''
        self.sprint_count-=1
        self.position += random.randint(5,15)
        if self.sprint_count<1:
            self.sprinting=False
