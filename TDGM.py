import pygame
from player import player
from Fireball import fireball
from enemy import enemy
pygame.init()
pygame.display.set_caption("Top down grid game") #set window title
screen = pygame.display.set_mode((1000, 800)) #create game screen
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
ticker = 0
mapNum = 1
screen.fill((0,0,0))

#instantiate a player
p1 = player()

#instantiate Fireball
ball = fireball()

#instantiate enemys
e1 = enemy()
e2 = enemy()

state = 1

#constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

keys = [False, False, False, False,False]
map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2],
       [2,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,3,3,3,3,2,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,3,3,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,3,3,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

map2 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2],
       [2,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,3,3,3,3,2,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,3,3,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,3,3,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

brick = pygame.image.load('brick.png')
dirt = pygame.image.load('dirt.jpg')
water = pygame.image.load('water.png')


while not gameover:#Game loop-------------------------------------------
    clock.tick(60)#FPS
    ticker+=1
    #input section-------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            if event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            if event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
    if state == 1:
        
        #physics section-----------------------------
        p1.move(keys, map)
        ball.move()
        if e1.isAlive == True:
            e1.move(map, ticker, p1.xpos, p1.ypos)
            e1.die(ball.xpos, ball.ypos)
            p1.ouch(e1.xpos, e1.ypos)
        if e2.isAlive == True:
            e2.move(map, ticker, p1.xpos, p1.ypos)
            e2.die(ball.xpos, ball.ypos)
            p1.ouch(e2.xpos, e2.ypos)
        #check if player health is less than 0
        if p1.health <= 0:
            state = 2
        #Check space for shooting
        if keys[SPACE] == True:
            ball.shoot(p1.xpos, p1.ypos, p1.direction)
        if mapNum ==1:
            if map[int((p1.ypos ) / 50)][int( (p1.xpos) / 50)] == 4:
                mapNum = 2
                p1.xpos = 50
        if mapNum == 2:
            if map2[int((p1.ypos ) / 50)][int( (p1.xpos) / 50)] == 4:
                mapNum = 1
                p1.xpos = 850
        if mapNum == 1:
            p1.move(keys , map)
        elif mapNum == 2:
            p1.move(keys , map2)
            
        if mapNum == 1:
            e1.move(map, ticker, p1.xpos, p1.ypos)
            
 
    #render section------------------------------
   
    if state == 1:
        #draw map
        if mapNum == 1:
            screen.fill((0,0,0)) #Wipe screen so it doesn't smear
            for i in range(len(map)):
                for j in range(len(map[i])):
                    if map[i][j] == 1:
                        screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 3:
                        screen.blit(water, (j * 50, i * 50), (0, 0, 50, 50))
        elif mapNum == 2:
            screen.fill((0,0,0))
            for i in range(len(map2)):
                for j in range(len(map2[i])):
                    if map2[i][j] == 1:
                        screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                    if map2[i][j] == 2:
                        screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                    if map2[i][j] == 3:
                        screen.blit(water, (j * 50, i * 50), (0, 0, 50, 50))  
        p1.draw(screen)
        if ball.isAlive == True:
            ball.draw(screen)
            
        e1.draw(screen)
        e2.draw(screen)
        
        pygame.draw.rect(screen, (255, 255, 255), (750, 5, 200, 30)) #white background
        pygame.draw.rect(screen, (150, 0,0), (750, 5, p1.health, 30)) #Red health bar
        pygame.draw.rect(screen, (0,0,0), (750, 5, 200, 30), 3) #Black outline
        
    elif state == 2: #GAME OVER SCREEN
        screen.fill((255,0,0)) #Wipe screen so it doesn't smear
    pygame.display.flip()#This puts the pixel on the screen
    
#end game loop----------------------------------------------------------
pygame.quit()
