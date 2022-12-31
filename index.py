import pygame
import time
import random
def main():
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

    #coordinates changes
    x1= display_width/2
    y1 = display_height/2 #Spawn point in the middle
    x1_change = 0       
    y1_change = 0
    speed = 30 
    snake_width = 10 
    snake_List = []
    Length_of_snake = 1
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)
    fontScore = pygame.font.SysFont(None, 25)
    fontLosing = pygame.font.SysFont(None, 35)
    appleX = round(random.randrange(10, display_width))
    appleY = round(random.randrange(10, display_width)) # random position for apples

    points = 0

    display.fill(grass)

    def snakedraw(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])
    

    def isSnakeinRange():
        if x1 >= appleX-16 and x1 <= appleX+16 and y1 >= appleY-16 and y1<=appleY+16:
            return True
        else:
            return False
    game_lost = False
    while not game_over:
        while game_lost == True:
                display.blit(font.render('You lost with ' + str(points) + ' Points', True, red), [display_width/5,display_height/4]) #Add variable for points
                display.blit(fontLosing.render('- Press SPACE to replay', True, red), [display_width/5,display_height/3])
                display.blit(fontLosing.render('- Press ESCAPE to quit the game', True, red), [display_width/5,display_height/2.5])
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_lost = False
                            main()            
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        quit()        

        for event in pygame.event.get():
        
            #Here we have all events
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
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
            game_lost=True
        if isSnakeinRange() == True:
            points += 2
            Length_of_snake += 5
            speed += 5
            appleX = round(random.randrange(10, display_width))
            appleY = round(random.randrange(10, display_width)) # random position for apples

        display.fill(grass) # Reset display behind the snake
        #Snake spawning 
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        snakedraw(snake_width, snake_List)

        pygame.draw.rect(display,red, [appleX-10, appleY-10, snake_width,snake_width]) #Apple spawning
        if len(snake_List)>Length_of_snake:
            del snake_List[0]
        display.blit(fontScore.render('Points : ' + str(points), True, red),  [25 ,25]) # Display score

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    quit()

main()