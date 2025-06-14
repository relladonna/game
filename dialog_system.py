import pygame
import json
from pathlib import Path
from config import Config
from items import Item

class DialogSystem:
    def __init__(self, font):
        """Система диалогов с анимацией текста
        
        Args:
            font (pygame.font.Font): Шрифт для отображения текста
        """
        self.font = font
        self.active_dialog = None
        self.current_line = 0
        self.is_active = False
        self.text_alpha = 0        # Прозрачность текста (0-255)
        self.char_index = 0        # Текущий символ для анимации
        self.text_speed = 3        # Символов в кадр (при 60 FPS)
        self.dialogs = {}          # Загруженные диалоги
        self.speaker_positions = { # Позиции спрайтов говорящих
            "Доктор": (Config.SCREEN_WIDTH//3, 400),
            "Аглая": (Config.SCREEN_WIDTH//3*2, 400)
        }
        
        self.load_dialogs()
        self.setup_surfaces()

    def setup_surfaces(self):
        """Создание поверхностей для рендеринга"""
        self.dialog_bg = pygame.Surface(
            (Config.SCREEN_WIDTH, 200), 
            pygame.SRCALPHA
        )
        self.dialog_bg.fill((0, 0, 0, 200))  # Полупрозрачный чёрный
        
        self.overlay = pygame.Surface(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT),
            pygame.SRCALPHA
        )
        self.overlay.fill((0, 0, 0, 120))     # Затемнение фона

    def load_dialogs(self):
        """Загрузка диалогов из JSON файла"""
        try:
            with open(Path('data') / 'dialogs.json', 'r', encoding='utf-8') as f:
                self.dialogs = json.load(f)
            print(f"Успешно загружены диалоги: {list(self.dialogs.keys())}")
        except Exception as e:
            print(f"Ошибка загрузки диалогов: {e}")
            self.dialogs = {
                "error_dialog": {
                    "lines": [{
                        "speaker": "Система",
                        "text": "Ошибка загрузки диалогов"
                    }]
                }
            }

    def start_dialog(self, dialog_id):
        """Начать диалог
        
        Args:
            dialog_id (str): Ключ диалога из dialogs.json
            
        Returns:
            bool: Успешно ли начат диалог
        """
        if dialog_id not in self.dialogs:
            print(f"Диалог '{dialog_id}' не найден! Доступные: {list(self.dialogs.keys())}")
            return False
            
        if not self.dialogs[dialog_id].get("lines"):
            print(f"Диалог '{dialog_id}' не содержит строк!")
            return False
            
        self.active_dialog = self.dialogs[dialog_id]
        self.current_line = 0
        self.char_index = 0
        self.text_alpha = 0
        self.is_active = True
        return True

    def next_line(self):
        """Перейти к следующей строке диалога"""
        if not self.is_active:
            return
            
        current_text = self.get_current_text()
        
        # Если текст ещё анимируется - показать весь сразу
        if self.char_index < len(current_text):
            self.char_index = len(current_text)
        # Иначе перейти к следующей строке или закончить
        elif self.current_line < len(self.active_dialog["lines"]) - 1:
            self.current_line += 1
            self.char_index = 0
            self.text_alpha = 0
        else:
            self.is_active = False

    def get_current_text(self):
        """Получить текущий текст диалога с обработкой ошибок"""
        try:
            return self.active_dialog["lines"][self.current_line]["text"]
        except:
            return "..."

    def get_current_speaker(self):
        """Получить текущего говорящего с обработкой ошибок"""
        try:
            return self.active_dialog["lines"][self.current_line]["speaker"]
        except:
            return "???"

    def update(self, dt):
        """Обновление анимации текста
        
        Args:
            dt (int): Время в миллисекундах с прошлого кадра
        """
        if not self.is_active:
            return
            
        current_text = self.get_current_text()
        
        # Анимация появления текста
        if self.char_index < len(current_text):
            self.char_index = min(
                self.char_index + self.text_speed * (dt / 16),
                len(current_text)
            )
            self.text_alpha = min(255, self.text_alpha + 5)

    def render(self, screen):
        """Отрисовка диалогового окна
        
        Args:
            screen (pygame.Surface): Целевая поверхность для отрисовки
        """
        if not self.is_active:
            return
            
        # Затемнение фона
        screen.blit(self.overlay, (0, 0))
        
        # Отрисовка диалогового окна
        screen.blit(self.dialog_bg, (0, Config.SCREEN_HEIGHT - 200))
        
        # Получение текущих данных диалога
        speaker = self.get_current_speaker()
        visible_text = self.get_current_text()[:int(self.char_index)]
        
        # Отрисовка имени персонажа
        name_surface = self.font.render(
            f"{speaker}:",
            True,
            (255, 255, 255)
        )
        screen.blit(name_surface, (50, Config.SCREEN_HEIGHT - 180))
        
        # Отрисовка текста с анимацией
        text_surface = self.font.render(
            visible_text,
            True,
            (255, 255, 255)
        )
        text_surface.set_alpha(self.text_alpha)
        screen.blit(text_surface, (50, Config.SCREEN_HEIGHT - 150))