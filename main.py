import random

import pygame

import core
from asteroid import Asteroid

from avatar import Avatar


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1000, 1000]

    core.memory("a", Avatar())
    core.memory("p",Asteroid())

    core.memory("listasteroid", [])
    core.memory("nbrasteroid", 5)


    for c in range(0, core.memory("nbrasteroid")):
        core.memory("listasteroid").append(Asteroid(1000, 1000))

    print("Setup END-----------")

def run():
   core.cleanScreen()
   for c in core.memory("listasteroid"):
       c.show(core.screen)

   core.memory("a").deplacement(core.getMouseLeftClick())
   if core.getKeyPressList("q"):
       quit()




   core.memory("a").show(core.screen)


core.main(setup, run)