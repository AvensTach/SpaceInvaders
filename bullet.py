import pygame

class Bullet(pygame.sprite.Sprite):


    def __init__(self, screen, gun):
        """create bullet"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 6, 12)
        self.color = 76, 175, 79
        self.speed = 2
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """bullet move up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """bullet draw in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
