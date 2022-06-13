import pygame.math

from objects.enemy.Enemy import Enemy
from config.Config import *
from objects.weapon.ShootingWeapon import ShootingWeapon
from objects.weapon.Bow import Bow


class Turret(Enemy):
    """Enemy turret class."""
    def __init__(self, level: "Level", position: pygame.math.Vector2):
        
        """
        Create turret.

        :param level: Level
        :param position: position where turret is created
        """
        super().__init__(level, (level.visible, level.obstacle, level.entity), TURRET_ANIMATION, TURRET_SOUNDS, position, 0, 0, TURRET_HEALTH, TURRET_ATTACK_RADIUS, TURRET_NOTICE_RADIUS)
        self.equip_weapon(Bow(level, self))
