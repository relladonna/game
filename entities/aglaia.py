from entities.npc import NPC
from config import Config

class Aglaia(NPC):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            sprite_path=Config.AGLAIA_SPRITE,
            dialog_id="aglaia_dialog"
        )