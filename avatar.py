import random

import pygame
from pygame.math import Vector2

import asteroid
import core
from core import screen


class Avatar:
    def __init__(self, largeur=400, hauteur=400,):
        self.position = Vector2(400,400)
        self.taille = 20
        self.couleur = (255,255,0)
        self.vel = Vector2(0,0)
        self.acc = Vector2()
        self.maxAcc = 300
        self.maxVel = 20
        self.count = 0
        self.force = 0


    def deplacement(self, destination):
        print(destination)





    def tirer (self, asteroid):
        if asteroid.position.distance_to(self.position) < asteroid.taille + self.taille:
            self.taille = self.taille + asteroid.taille
            asteroid.RAZ()

    def show(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.taille)

    def bordure(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y = 0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0