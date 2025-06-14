import os
import pygame

class Config:
    # Настройки экрана
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 860
    BG_COLOR = (30, 30, 50)
    
    # Настройки игрока
    PLAYER_SPEED = 5
    
    # Пути к ресурсам
    ASSETS_DIR = os.path.join("assets")
    SPRITES_DIR = os.path.join(ASSETS_DIR, "sprites")
    FONT_PATH = os.path.join(ASSETS_DIR, "font.ttf")
    ITEMS_DIR = os.path.join(SPRITES_DIR, "items")
    
    # Спрайты
    PLAYER_SPRITE = os.path.join(SPRITES_DIR, "player.png")
    AGLAIA_SPRITE = os.path.join(SPRITES_DIR, "aglaia.png")
    DOCTOR_SPRITE = os.path.join(SPRITES_DIR, "doctor.png")
    BACKGROUND = os.path.join(SPRITES_DIR, "background.png")

    DIALOGS_PATH = os.path.join("data", "dialogs.json")
    KEY_SPRITE = os.path.join(ITEMS_DIR, "bottle_world.png")
    KEY_ICON = os.path.join(ITEMS_DIR, "bottle_icon.png")
    HINT_SPRITE = "assets/sprites/ui/hint.png"