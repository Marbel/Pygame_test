import pygame


# check collision with treasure
def checkCollision(x,y,treasureX,treasureY):
    collisionState = False
    if y >= treasureY and y <= treasureY +40:
        if x >= treasureX and x <= treasureX+35:
            collisionState = True
        elif x + 35 >= treasureX and x + 35 <= treasureX +35:
            collisionState = True
    elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
        if x >= treasureX and x <= treasureX+35:
            collisionState = True
        elif x + 35 >= treasureX and x + 35 <= treasureX +35:
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
enemyY = 450

treasureX = 450-35/2
treasureY = 50

font = pygame.font.SysFont("comicsans",70)
level = 1


frame = pygame.time.Clock()
collisionTreasure = False
while finished == False:
    x, y, playerMoved = movePlayer(x,y)


    #R,G,B
    #color = (0,0,255) #Blue
    #black = (0,0,0)
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage,(x,y))
    screen.blit(enemyImage,(enemyX,enemyY))
    if playerMoved:
        collisionTreasure = checkCollision(x,y,treasureX,treasureY)
    if collisionTreasure:
        level += 1
        textWin = font.render("You reached Level " + str(level),True,(0,0,0))
        screen.blit(textWin,(450-textWin.get_width()/2,350-textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
        x = 450-35/2
        y = 650
        collisionTreasure = False
    #pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip()
    frame.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           finished = True
           pygame.quit()
