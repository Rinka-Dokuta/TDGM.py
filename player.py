import pygame
import math
#constants
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

class player:
    def __init__(self):
        #player variables
        self.xpos = 400#xpos of player
        self.ypos = 415#ypos of player
        self.vx = 0#x velocity of player
        self.vy = 0#y velocity of player
        self.direction = LEFT
        self.health = 200
        
    def draw(self,screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))
        
    def move(self, keys, map):
        #left movement
        if keys[LEFT] == True:
            self.vx = -3
            print("Moving left")
            self.direction = LEFT
        #Right movement
        elif keys[RIGHT] == True:
            self.vx = 3
            self.direction = RIGHT
            print("Moving right")
        #Turn off x velocity
        else:
            self.vx = 0    
        if keys[UP] == True:
            self.vy = -3
            self.direction = UP
            print("Moving Up")
        
        elif keys[DOWN] == True:
            self.vy = 3
            self.direction = DOWN
            print("Moving Down")
    
        #Turn off y velocity
        else:
            self.vy = 0
        
        #COLLISION
        #left collision
        if map[int((self.ypos) / 50)][int((self.xpos - 10) / 50)] == 2 :
            self.xpos+=3
            
        #right collision
        if map[int((self.ypos) / 50)][int((self.xpos +30 + 5) / 50)] == 2 :
            self.xpos-=3
        #down collison
        if map[int((self.ypos+30 + 5) / 50)][int((self.xpos) / 50)] == 2 :
            self.ypos-=3
        #up collison    
        if map[int((self.ypos+-10) / 50)][int((self.xpos) / 50)] == 2 :
            self.ypos+=3
            
        self.xpos+=self.vx #update player xpos
        self.ypos+=self.vy #update player xpos
        
    def ouch(self, e1xpos, e1ypos):
        if math.sqrt((self.xpos-e1xpos)**2+ (self.ypos-e1ypos)**2) <= 20:
            self.health = -5
        
      
        
        
        
