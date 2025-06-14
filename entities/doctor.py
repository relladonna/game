from entities.npc import NPC
from config import Config

class Doctor(NPC):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            sprite_path=Config.DOCTOR_SPRITE,
            dialog_id="doctor_dialog"
        )