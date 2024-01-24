import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
import time


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 800))
        pygame.display.set_caption("Space invaders")
        self.bg_color = 0, 0, 16
        self.gun = Gun(self.screen)
        self.bullets = Group()
        self.inos = Group()
        controls.create_army(self.screen, self.inos)
        self.stats = Stats()
        
        
    def run(self):
        while True:
            controls.handle_events(self.screen,
                                   self.gun,
                                   self.bullets)
            if self.stats.run_game:
                self.gun.update_gun()
                controls.update(self.bg_color,
                                self.screen,
                                self.gun,
                                self.inos,
                                self.bullets)
                controls.update_bullets(self.screen,
                                        self.inos,
                                        self.bullets)
                controls.update_inos(self.stats,
                                     self.screen,
                                     self.gun,
                                     self.inos,
                                     self.bullets)
            time.sleep(1.0/70)
