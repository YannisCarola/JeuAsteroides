import random

import pygame
from pygame.math import Vector2

import core


class Asteroid:
    def __init__(self, largeur=400, hauteur=400,):
        self.maxVitesse = Vector2(random.randint(0, 400), random.randint(0, 400))
        self.maxAcceleration = Vector2(0,0)
        self.position = Vector2(random.randint(0,largeur),random.randint(0,hauteur))
        self.rayon = 25
        self.couleur = (255,255,255)
        self.masse = 5
        self.vivante = True
        self.deplacement = Vector2(random.randint(0, 400), random.randint(0, 400))



    def show(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)


    def deplacement (self,destination):
        destination = self.postion





    def bordure(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0
