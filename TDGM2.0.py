import pygame
import math
from player import player
from Fireball import fireball
from enemy import enemy
from NPC import npc
pygame.init()
pygame.display.set_caption("Top down grid game") #set window title
screen = pygame.display.set_mode((1000, 800)) #create game screen
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
ticker = 0
mapNum = 1
pygame.mixer.music.load("CME.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
endscreen = pygame.image.load("GAME OVER.png")
#Distance checker for NPC
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#game state variable
state = 4 #1 is menu, 2 is playing, 3 is credits
button1 = False
button2 = False
button3 = False
#add more buttons here!
quitGame = False
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 70)
title_text = font.render("THE LOST LABYRINTH", True, WHITE)
screen.fill((0,0,0))
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False
#instantiate a player
p1 = player()

#instantiate Fireball
ball = fireball()

#instantiate enemys
e1 = enemy()
e2 = enemy()

#instantiate NPC
n1 = npc()

state = 4

#constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
ENTER = 5


keys = [False, False, False, False,False, False]
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
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,2,2,2],
       [2,1,1,1,1,2,2,2,2,1,1,2,2,2,2,2,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2],
       [2,1,1,2,2,2,2,2,2,1,1,2,2,2,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,3,3,2,1,1,2,3,3,2],
       [2,1,1,1,1,1,1,1,1,1,1,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,1,1,2,2,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,1,1,2,2,2,1,1,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

map3 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,2],
       [2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2],
       [2,1,1,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,3,3,3,3,2,1,1,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,3,3,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,3,3,3,3,2,1,1,2,3,3,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4],
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
        
         #Mouse input section=========================================
        if event.type == pygame.QUIT:
            running = False
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        
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
                
            
          
        
    if state == 4 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
            button1 = True
    else:
            button1 = False
            
    if state == 4 and button1 == True and mouseDown == True:
        state = 5
    #state 5: playing state!---------------------------When button1 pressed
    if state == 5 and quitGame == True: #pressing quit takes you back to menu
        state = 4
        #Button2---------------------------------------------------------------------   
    if state == 4 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<550:
        button2 = True
    else:
        button2 = False
        
    if state == 4 and button2 == True and mouseDown == True:
        state = 6
    
    if state == 6 and quitGame == True: #pressing quit takes you back to menu
        state = 4
        
     #button3----------------------------------------------------------------------
    if state == 4 and mousePos[0]>700 and mousePos[0]<900 and mousePos[1]>400 and mousePos[1]<550:
        button3 = True
    else:
        button3 = False
        
    if state == 4 and button3 == True and mouseDown == True:
        state = 7
    
    if state == 7 and quitGame == True: #pressing quit takes you back to menu
        state = 4
        
        
        
    if state == 1:    
        p1.move(keys, map)
        ball.move()
        n1.move(map, ticker)
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
                mapNum = 3
                p1.xpos = 850
        if mapNum == 3:
            if map2[int((p1.ypos ) / 50)][int( (p1.xpos) / 50)] == 4:
                mapNum = 1
                p1.xpos = 850
        if mapNum == 1:
            p1.move(keys , map)
        elif mapNum == 2:
            p1.move(keys , map2)
        elif mapNum == 3:
            p1.move(keys, map3)
            
        if mapNum == 1:
            e1.move(map, ticker, p1.xpos, p1.ypos)
            
        if mapNum == 2:
            e1.move(map2, ticker, p1.xpos, p1.ypos)
            
            
       
    
        
        
 
    #render section------------------------------
   
    #menu state-------------------------------
    if state == 4:
        screen.fill((230,100,100))# Clear the screen pink
        screen.blit(title_text, (250, 131))
      
        
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
        else: #when button1 == True or pressed down
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))# 1st box (Color), (position)
        if button2 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))#2nd box
        else:
            pygame.draw.rect(screen, (200, 250, 200), (400, 400, 200, 150))
        if button3 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))#3rd box
        else:
            pygame.draw.rect(screen, (200, 250, 200), (700, 400, 200, 150))
            
        if button1 == True:
            state = 1

    
    #game state-------------------------------
    if state == 5:
        screen.fill((80,150,100))# Clear the screen green
     
    if state == 6:
        screen.fill((255,51,51))# Clear the screen red
    
    if state == 7:
        screen.fill((0,0,255))# Clear the screen blue
    
    
    
    
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
                    
                        
        if keys[ENTER] == True and dist(p1.xpos, p1.ypos, bob.xpos, bob.ypos)<10:
            bob.talk()
            
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
                        
        elif mapNum == 3:
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
        
        n1.draw(screen, ticker)
        
        pygame.draw.rect(screen, (255, 255, 255), (750, 5, 200, 30)) #white background
        pygame.draw.rect(screen, (150, 0,0), (750, 5, p1.health, 30)) #Red health bar
        pygame.draw.rect(screen, (0,0,0), (750, 5, 200, 30), 3) #Black outline
        
    elif state == 2: #GAME OVER SCREEN
        screen.fill((255,0,0)) #Wipe screen so it doesn't smear
        screen.blit(endscreen,(0,0), (0,0,1000,800))
    pygame.display.flip()#This puts the pixel on the screen
    


#end game loop----------------------------------------------------------
pygame.quit()
