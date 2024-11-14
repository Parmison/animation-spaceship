import pygame
pygame.init()

screen = pygame.display.set_mode((1250,690))

yellow_ship = pygame.image.load("lesson 6/image/spaceship yellow.png")
yellow_ship= pygame.transform.scale(yellow_ship,(100,100))

orange_ship = pygame.image.load("lesson 6/image/spaceship orange.png")
orange_ship = pygame.transform.scale(orange_ship,(100,100))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [orange_ship,yellow_ship]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
    def update(self):
        self.counter += 1 
        if self.counter >= 3:
            self.counter = 0
            self.index += 1
            if self.index >= 2:
                self.index = 0
        self.image = self.images[self.index]

spaceship = Spaceship(625,450)
Spaceship1 = pygame.sprite.Group()
Spaceship1.add(spaceship)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("black")
    Spaceship1.draw(screen)
    Spaceship1.update()
    pygame.display.update()
    