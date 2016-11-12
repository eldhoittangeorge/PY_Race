import pygame
pygame.init()
gameWidth = 800
gameHeight = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
carImage = pygame.image.load('/Users/eldhoittangeorge/Desktop/PY_Game/car50.png')
gameDisplay = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption("PY_Race")
clock = pygame.time.Clock()

def car(x,y):
    gameDisplay.blit(carImage,(x,y))

x=(gameWidth*.45)
y=(gameHeight*.8)

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill(green)
    car(x,y)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
