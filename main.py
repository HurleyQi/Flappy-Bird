from operator import length_hint
import pygame
from pygame.locals import *
import random
import time

# possible heights
height=[250,300,400,500,550,600,650]

SIZE = 5

# class the represents the pipes in the game
class Pipes:
    # initialization
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.image = pygame.image.load("./pipe.png").convert()  
        self.pipe_down = pygame.image.load("./pipe_down.png").convert()      
        self.x = []
        self.y = []
        self.direction = "right"
    # drawing and displaying pipes on screen
    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.length):
            self.x.append(1400+(i*500))
        for i in range(self.length):
            self.y.append(random.choice(height))
        for i in range(self.length):
            self.parent_screen.blit(self.image,(self.x[i],self.y[i]))
        for i in range(self.length):
            self.parent_screen.blit(self.pipe_down,(self.x[i],(-1*(950-self.y[i]))))
        # pygame.display.flip()

    def move(self):
        # for i in range(self.length - 1, 0, -1):
        #     self.x[i] = self.x[i - 1]
        # if self.direction == "right":
        #     self.x[0] -= SIZE

        for i in range(self.length):
            self.x[i] = self.x[i] - SIZE

        self.draw()

# class the represents the bird in the game
class Bird:
    # initialization
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.bird = pygame.image.load("./bird.png")
        self.image = pygame.transform.scale(self.bird,(265,180))
        self.direction = "down"
        self.x = 200
        self.y = 0
    # drawing and displaying bird on screen
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    def move(self):
        if self.direction == "down":
            self.y += 7
        self.draw()

# game 
class Game:
    # initialization
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1500,800))
        self.surface.fill((110,110,5))
        self.pipes = Pipes(self.surface,10)
        self.pipes.draw()
        self.bird = Bird(self.surface)
        self.bird.draw()
    def if_collision(self):
        # conditions for when to quit
        for i in range(self.pipes.length):
            if self.bird.y >= self.pipes.y[i] and self.pipes.x[i] == 350:
                exit(0)
            if self.bird.y >= self.pipes.y[i] and self.pipes.x[i] == 340:
                exit(0)
            if self.bird.y >= self.pipes.y[i] and self.pipes.x[i] == 320:
                exit(0)
            # if self.bird.y <= (self.pipes.y[i] - 80) and self.pipes.x[i] == 350:
            #     exit(0)
    # actual running the game
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                # commands and their responses
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pass
                if event.type == pygame.MOUSEBUTTONUP:
                    self.bird.y -= 100
                if event.type == QUIT:
                    running = False

            self.if_collision()
            self.pipes.move()
            self.bird.move()
            pygame.display.flip()

        

if __name__ == "__main__":
    game = Game()
    game.run()
