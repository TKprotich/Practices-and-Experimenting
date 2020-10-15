"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random

# Initializae the game engine
pygame.init()
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SIZE = [400, 400]
# Define the variables needed
#1. Create an empty list for snowflakes
snow_list = []
#2. Generate the snowflakes positions/coordinates
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(SIZE)
 
pygame.display.set_caption("Show Animation")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button
done = False
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # background color black.
    screen.fill(BLACK)
    
    # --- Drawing code should go here
    for i in range(len(snow_list)):
        # Draw the snowflakes
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        #move the snowflakes 1 pixels
        snow_list[i][1] +=1
        #
        if snow_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
