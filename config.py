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
    
    # Спрайты
    PLAYER_SPRITE = os.path.join(SPRITES_DIR, "player.png")
    AGLAIA_SPRITE = os.path.join(SPRITES_DIR, "aglaia.png")
    DOCTOR_SPRITE = os.path.join(SPRITES_DIR, "doctor.png")
    BACKGROUND = os.path.join(SPRITES_DIR, "background.png")
    HINT_SPRITE = os.path.join(SPRITES_DIR, "hint.png")
    DIALOGS_PATH = os.path.join("data", "dialogs.json")
    FONT_PATH = os.path.join(ASSETS_DIR, "font.ttf")