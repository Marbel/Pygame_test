import pygame
import random

# check collision with treasure
def checkCollision(x,y,targetX,targetY):
    collisionState = False
    if y >= targetY and y <= targetY +40:
        if x >= targetX and x <= targetX+35:
            collisionState = True
        elif x + 35 >= targetX and x + 35 <= targetX +35:
            collisionState = True
    elif y + 40 >= targetY and y + 40 <= targetY + 40:
        if x >= targetX and x <= targetX+35:
            collisionState = True
        elif x + 35 >= targetX and x + 35 <= targetX +35:
            collisionState = True
    return collisionState
# move player
def movePlayer(x,y):
    playerMoved = False
    pressedKeys = pygame.key.get_pressed()
    # Moving player
    if pressedKeys[pygame.K_LEFT] == True:
        playerMoved = True
        x -= 2
    if pressedKeys[pygame.K_RIGHT] == True:
        playerMoved = True
        x += 2
    if pressedKeys[pygame.K_UP] == True:
        playerMoved = True
        y -= 2
    if pressedKeys[pygame.K_DOWN] == True:
        playerMoved = True
        y += 2
    return x,y,playerMoved

pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False # To close the game

x = 450-35/2
y = 650
#load image
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage,(35,40))
playerImage = playerImage.convert_alpha()

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage,(900,700))
screen.blit(backgroundImage,(0,0))

treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage,(35,40))
treasureImage = treasureImage.convert_alpha()

enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(35,40))
enemyImage = enemyImage.convert_alpha()

enemyX = 50
enemyY = 440
enemymovingright = True

treasureX = 450-35/2
treasureY = 50

font = pygame.font.SysFont("comicsans",70)
level = 1

enemyNames = {0:"Bob",1:"Will",2:"Smith",3:"Joe",4:"Jill"}

enemyName = enemyNames[random.choice(list(enemyNames))]

frame = pygame.time.Clock()
collisionTreasure = False
collisionEnemy = False
while finished == False:
    x, y, playerMoved = movePlayer(x,y)

    if enemyX < 800 and enemymovingright == True:
        enemyX += 2 + (level*2)
    elif enemyX >= 800 and enemymovingright == True:
        enemymovingright = False
    if enemyX > 100 and enemymovingright == False:
        enemyX -= 2 + (level*2)
    elif enemyX <= 100 and enemymovingright == False:
        enemymovingright = True


    #R,G,B
    #color = (0,0,255) Blue
    #black = (0,0,0)
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage,(x,y))
    screen.blit(enemyImage,(enemyX,enemyY))
    textEnemy = font.render(enemyName,True,(0,0,0))
    screen.blit(textEnemy,(enemyX,enemyY-60))

    collisionEnemy = checkCollision(x,y,enemyX,enemyY)
    if playerMoved:
        collisionTreasure = checkCollision(x,y,treasureX,treasureY)
    if collisionTreasure:
        level += 1
        enemyName = enemyNames[random.choice(list(enemyNames))]
        textWin = font.render("You reached Level " + str(level),True,(0,0,0))
        screen.blit(textWin,(450-textWin.get_width()/2,350-textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
        x = 450-35/2
        y = 650
        collisionTreasure = False
    elif collisionEnemy:
        textWin = font.render("You lost",True,(0,0,0))
        screen.blit(textWin,(450-textWin.get_width()/2,350-textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
        level = 1
        enemyName = enemyNames[random.choice(list(enemyNames))]
        x = 450-35/2
        y = 650
        collisionEnemy = False

    #pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip()
    frame.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           finished = True
           pygame.quit()
