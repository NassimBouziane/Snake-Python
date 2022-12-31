import pygame
import time
import random
pygame.init()
display_width= 500
display_height = 500
display=pygame.display.set_mode((display_width,display_height))

pygame.display.update()
pygame.display.set_caption('Snake game by Nassim Bouziane')
game_over= False
#colors :
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
grass=(0,100,0)

#coordonnates changes
x1= display_width/2
y1 = display_height/2 #Spawn point in the middle
x1_change = 0       
y1_change = 0

snake_width = 10 
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
fontScore = pygame.font.SysFont(None, 25)
appleX = round(random.randrange(10, display_width))
appleY = round(random.randrange(10, display_width)) # random position for apples

points = 0

display.fill(grass)


def isSnakeinRange():
    if x1 >= appleX-10 and x1 <= appleX+10 and y1 >= appleY-10 and y1<=appleY+10:
        return True
    else:
        return False

while not game_over:
    for event in pygame.event.get():

        #Here we have all events
        if event.type== pygame.QUIT:
            game_over=True
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -5
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 5
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    if x1 < 0 or y1 < 0 or x1 >= display_width or y1 >= display_height:
        game_over=True
    if isSnakeinRange() == True:
        points += 2
        appleX = round(random.randrange(10, display_width))
        appleY = round(random.randrange(10, display_width)) # random position for apples

    display.fill(grass) # Reset display behind the snake
    pygame.draw.rect(display,green,[x1,y1,snake_width,snake_width])
    pygame.draw.rect(display,red, [appleX, appleY, snake_width,snake_width])
    display.blit(fontScore.render('Points : ' + str(points), True, red),  [25 ,25]) # Display score

    pygame.display.update()
    clock.tick(30)
display.blit(font.render('You lost with ' + str(points) + ' Points', True, red), [display_width/5,display_height/4]) #Add variable for points
pygame.display.update()
time.sleep(3) # Replace this with a function that show of a menu annd you select if you continue or not
pygame.quit()
quit()