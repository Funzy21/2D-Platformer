import pygame
from sys import exit

pygame.init()

SCREEN_HEIGHT = 1280
SCREEN_WIDTH = 720

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Pizza")
clock = pygame.time.Clock()

# Background layers
bg_layer_1 = pygame.image.load("Assets\Levels\dark_forest\\background\\background_layer_1.png")
bg_layer_2 = pygame.image.load("Assets\Levels\dark_forest\\background\\background_layer_2.png")
bg_layer_3 = pygame.image.load("Assets\Levels\dark_forest\\background\\background_layer_3.png")

# Scaling
bg_layer_1 = pygame.transform.scale(bg_layer_1, (1280, 720))
bg_layer_2 = pygame.transform.scale(bg_layer_2, (1280, 720))
bg_layer_3 = pygame.transform.scale(bg_layer_3, (1280, 720))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Rendering here
    screen.blit(bg_layer_1, (0,0))
    screen.blit(bg_layer_2, (0,0))
    screen.blit(bg_layer_3, (0,0))
    
    pygame.display.update()
    clock.tick(60)
        
    