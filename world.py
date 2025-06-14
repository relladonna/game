import pygame
from config import Config
from entities.player import Player
from entities.doctor import Doctor
from entities.aglaia import Aglaia
from dialog_system import DialogSystem
from items import Item
from inventory import Inventory


class World:
    def __init__(self):
        # Инициализация шрифта
        self.font = pygame.font.Font(Config.FONT_PATH, 24) if hasattr(Config, 'FONT_PATH') else pygame.font.SysFont("Arial", 24)
        
        # Создание игрока
        self.player = Player()
        
        # Создание NPC
        self.npcs = [
            Doctor(1400, 350),
            Aglaia(1600, 370)
        ]
        
        # Загрузка фона
        try:
            self.background = pygame.image.load(Config.BACKGROUND).convert()
        except:
            self.background = pygame.Surface((4056, Config.SCREEN_HEIGHT))
            self.background.fill(Config.BG_COLOR)
        
        # Система диалогов
        self.dialog_system = DialogSystem(self.font)
        self.world_offset_x = 0
        self.initial_dialog_shown = False

        # Начинаем с правого края мира
        self.world_offset_x = 4056 - Config.SCREEN_WIDTH
        self.player = Player()  # Игрок создается после установки offset

        self.items = self._init_items()
        self.inventory = Inventory()

    def _init_items(self) -> list[Item]:
        return [
            Item(
                x=1000, y=500,
                item_data={
                    'id': 'main_key',
                    'name': 'Ключ от чердака',
                    'description': 'Старый ржавый ключ с гравировкой',
                    'world_sprite': Config.KEY_SPRITE,
                    'inventory_sprite': Config.KEY_ICON,
                    'pickup_dialog': 'found_key_dialog'
                }
            ),
            # Другие предметы...
        ]

    def handle_interactions(self):
        if self.dialog_system.is_active:
            return
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            for npc in self.npcs:
                npc_rect = pygame.Rect(
                    npc.rect.x - self.world_offset_x,
                    npc.rect.y,
                    npc.rect.width,
                    npc.rect.height
                )
                if self.player.rect.colliderect(npc_rect) and npc.dialog_id:
                    self.dialog_system.start_dialog(npc.dialog_id)
                    break

    def update(self):
        keys = pygame.key.get_pressed()
        movement = self.player.update(keys)

        # Смещаем мир в противоположную сторону
        self.world_offset_x -= movement

        # Границы мира
        self.world_offset_x = max(0, min(
            self.world_offset_x,
            4056 - Config.SCREEN_WIDTH
        ))
        
        # Автоматический диалог
        if not self.initial_dialog_shown and 1100 < self.world_offset_x < 1200:
            self.dialog_system.start_dialog("initial_dialog")
            self.initial_dialog_shown = True
            
        # Обновление NPC
        for npc in self.npcs:
            npc.update(self.player.rect, self.world_offset_x, self.dialog_system.dialogs)
        
        self.handle_interactions()
        self.dialog_system.update(16)

        # Обновление предметов
        for item in self.items[:]:
            dialog_id = item.update(self.player.rect, (self.world_offset_x, 0))
            if dialog_id:
                if self.inventory.add_item(item):
                    self.dialog_system.start_dialog(dialog_id)
                    self.items.remove(item)

    def render(self, screen):
        # Отрисовка фона
        screen.blit(self.background, (-self.world_offset_x, 0))
        
        # Отрисовка NPC
        for npc in self.npcs:
            npc.render(screen, self.world_offset_x)

        for item in self.items:
            item.render(screen, (self.world_offset_x, 0))

        self.inventory.render(screen, self.font)
        
        # Отрисовка игрока
        self.player.render(screen)
        
        # Отрисовка диалогов
        self.dialog_system.render(screen)