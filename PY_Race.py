import pygame
pygame.init()
gameWidth = 1200
gameHeight = 720
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
def gameLoop():
    x=(gameWidth*.45)
    y=(gameHeight*.8)
    x_change = 0


    gameEnd = False
    while not gameEnd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEnd = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(green)
        car(x,y)
        if x > gameWidth or x < 0 :
            gameEnd = True

        pygame.display.update()
        clock.tick(60)
gameLoop()
pygame.quit()
quit()
