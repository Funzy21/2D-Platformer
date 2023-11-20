import pygame as pg
from settings import *
from sys import exit

# Background layers
bg_layer_1 = pg.image.load("Assets\Levels\dark_forest\\background\\background_layer_1.png")
bg_layer_2 = pg.image.load("Assets\Levels\dark_forest\\background\\background_layer_2.png")
bg_layer_3 = pg.image.load("Assets\Levels\dark_forest\\background\\background_layer_3.png")

# Scaling
bg_layer_1 = pg.transform.scale(bg_layer_1, (1280, 720))
bg_layer_2 = pg.transform.scale(bg_layer_2, (1280, 720))
bg_layer_3 = pg.transform.scale(bg_layer_3, (1280, 720))


class Game():
    def __init__(self):
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        pg.display.set_caption("Pizza")
        self.clock = pg.time.Clock()
    
    def newgame(self):
        #self.sprites = pg.sprite.Group()
        self.run()
        pass
        
    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.render()
        
    def update(self):
        #self.sprites = pg.sprite.Group)
        pass
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def render(self):
        self.screen.blit(bg_layer_1, (0,0))
        self.screen.blit(bg_layer_2, (0,0))
        self.screen.blit(bg_layer_3, (0,0))
        pg.display.update()
    def show_start_screen(self):
        pass
    def show_game_over(self):
        pass


g = Game()
g.show_start_screen
while g.running:
    g.newgame()
    g.show_game_over()
        
