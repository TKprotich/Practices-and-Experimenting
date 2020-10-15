import pygame
pygame.init()

#colors and consttant
RED = (255, 0, 0)
BLUE =(0, 0, 255)
GREEN =(0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE =(600, 400)
#size and screen
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
done = False
while not done:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             done = True
         if event.type == pygame.KEYDOWN:
             print('User pressed a key.')
         if event.type == pygame.KEYUP:
             print('User let go of a key.')
         if event.type == pygame.MOUSEBUTTONDOWN:
             print('User pressed a mouse button')
pygame.quit()
