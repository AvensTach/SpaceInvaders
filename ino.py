import pygame

class Ino(pygame.sprite.Sprite):
    """1 alien"""

    def __init__(self, screen):
        """initialization"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        """draw ino"""
        self.screen.blit(self.image, self.rect)



    def update(self):
        """move inos"""
        self.y += 0.05
        self.rect.y = self.y


