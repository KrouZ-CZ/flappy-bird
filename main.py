import pygame
import random
from sys import exit
pygame.init()

BLACK = (0, 0, 0)
W, H = 700, 392

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flappy bird")
fon = pygame.image.load("resources\\fon.png").convert()
clock = pygame.time.Clock()
FPS = 60
def stop():
    global test, score, mybird, wall1, wall2, wall3
    score = 0
    mybird = Bird(H)
    wall1 = Wall(0)
    wall2 = Wall(350)
    wall3 = Wall(700)
class Bird(pygame.sprite.Sprite):
    def __init__(self, H):
        self.image = pygame.image.load(f"resources\\bird.png").convert_alpha()
        self.dir = 0 
        self.x = 100
        self.y = H/2
        self.rect = self.image.get_rect(center=(self.x, self.y))
    def jump(self):
        self.dir = -10
    def update(self):
        self.x = self.x + self.dir
        if self.dir >= -10:
            self.dir = self.dir + 1
        self.rect = self.image.get_rect(center=(self.y, self.x))
    def collision(self):
        if self.x <= 10:
            stop()
        elif self.x >= H - 10:
            stop()
class Wall(pygame.sprite.Sprite):
    def __init__(self, x):
        self.imageDown = pygame.image.load("resources\\wall down.png").convert_alpha()
        self.imageUp = pygame.image.load("resources\\wall up.png").convert_alpha()
        self.x = W + x
        self.yDown = random.randint(400, 550)
        self.yUp = self.yDown - 410
        self.rectDown = self.imageDown.get_rect(bottomright=(self.x, self.yDown))
        self.rectUp = self.imageUp.get_rect(bottomright=(self.x, self.yUp))
    def update(self):
        self.x -= 3
        self.rectDown = self.imageDown.get_rect(bottomright=(self.x, self.yDown))
        self.rectUp = self.imageUp.get_rect(bottomright=(self.x, self.yUp))
    def collision(self):
        if self.rectUp.colliderect(mybird.rect):
            stop()
        elif self.rectDown.colliderect(mybird.rect):
            stop()
mybird = Bird(H)
wall1 = Wall(0)
wall2 = Wall(350)
wall3 = Wall(700)
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mybird.jump()
    if wall1.x < 50:
        wall1 = wall2
        wall2 = wall3
        wall3 = Wall(500)
        score += 1
    wall1.collision()
    wall1.update()
    wall2.update()
    wall3.update()
    mybird.update()
    mybird.collision()
    sc.blit(fon, (0, 0))
    sc.blit(mybird.image, mybird.rect)
    sc.blit(wall1.imageDown, wall1.rectDown)
    sc.blit(wall1.imageUp, wall1.rectUp)
    sc.blit(wall2.imageDown, wall2.rectDown)
    sc.blit(wall2.imageUp, wall2.rectUp)
    sc.blit(wall3.imageDown, wall3.rectDown)
    sc.blit(wall3.imageUp, wall3.rectUp)
    f = pygame.font.SysFont(None, 30)
    sc_text = f.render(f"Score: {score }", 1, (0, 0, 0))
    sc.blit(sc_text, (20, 10))
    pygame.display.update()
    clock.tick(FPS)