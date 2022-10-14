import math
import random
from matplotlib.pyplot import grid
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0

def snake(color, pos):
    pass
def redrawWindow(surface):
    win.fill(0,0,0)
    drawGrid(rows, w, surface)
    pygame.display.update()
    pass
def drawGrid(w, rows, surface):

    pass
def main():
    width = 500
    height = 500
    rows  = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))
    flag = True
    clock = pygame.time.Clock
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    pass