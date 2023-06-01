from src.util.constants import *
from src.entity.Potion import *
class HpPotion(Potion):
    def __init__(self, xPos, yPos):
        self.hp = 3
        super().__init__(xPos, yPos, True, HP_POTION_WIDTH, HP_POTION_HEIGHT)