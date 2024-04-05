import pygame

#initialize the game engine
pygame.init()

#------------------------------------
#set window settings (size and name)
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My Game")
#------------------------------------

#used to manage how fast the screen updates
clock = pygame.time.Clock()

#------------------------------------

#-------------------------
# Initialize global variables

#-------------------------
#------------Main program loop-----------
running = True
while running
    #----- Event Handling -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#----- Game State Updates -----------------
#All game math and comparisons happen here
            
#----- Drawing -----
screen.fill((255 ,255 ,255)) # always the first drawing comand

# Must be the last two lines of the game loop 
pygame.display.flip()
clock.tick(30)
#--------------------------

pygame.quit()
