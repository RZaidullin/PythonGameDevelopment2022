import pygame
from objects.weapon.ShootingWeapon import Weapon
from config.Config import *


class Solid(pygame.sprite.Sprite):

    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        """ """
        # def __init__(self, level, groups, image_path, position):

        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface # pygame.image.load(image_path).convert_alpha()
        if sprite_type == 'object':
            self.rect = self.image.get_rect(center=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(center=pos)

        self.hitbox = self.rect.inflate(0, -10)
    