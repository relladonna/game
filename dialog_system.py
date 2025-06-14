import pygame
from config import Config

class DialogSystem:
    def __init__(self, font):
        self.font = font
        self.active_dialog = None
        self.current_line = 0
        self.is_active = False
        self.text_alpha = 0
        self.char_index = 0
        self.text_speed = 0.05
        self.load_dialogs()  # Важно: вызываем здесь!

    def load_dialogs(self):
        self.dialogs = {
            "initial_dialog": {
                "lines": [
                    {"speaker": "Доктор", "text": "Аглая Петровна, вам нужно принимать лекарства регулярно."},
                    {"speaker": "Аглая", "text": "Но я чувствую себя хуже после них, доктор..."},
                    {"speaker": "Доктор", "text": "Это временные эффекты. Вы должны довериться мне."}
                ]
            },
            "aglaia_dialog": {
                "lines": [
                    {"speaker": "Аглая", "text": "Вы тоже их видите? Тени в углах комнат..."},
                    {"speaker": "Аглая", "text": "Мама говорила, что этот дом необычный."},
                    {"speaker": "Аглая", "text": "Может, вы сможете помочь мне разобраться?"}
                ]
            },
            "doctor_dialog": {
                "lines": [
                    {"speaker": "Доктор", "text": "Вам нельзя беспокоить пациентку"},
                    {"speaker": "Доктор", "text": "Пожалуйста, уйдите"}
                ]
            }
        }

    def start_dialog(self, dialog_id):
        if dialog_id in self.dialogs:
            self.active_dialog = self.dialogs[dialog_id]
            self.current_line = 0
            self.is_active = True
            self.char_index = 0
            self.text_alpha = 0
            print(f"Диалог запущен: {dialog_id}")  # Отладочное сообщение

    def next_line(self):
        if self.char_index < len(self.active_dialog["lines"][self.current_line]["text"]):
            # Пропустить анимацию, показать весь текст сразу
            self.char_index = len(self.active_dialog["lines"][self.current_line]["text"])
        else:
            if self.current_line < len(self.active_dialog["lines"]) - 1:
                self.current_line += 1
                self.char_index = 0
            else:
                self.is_active = False

    def update(self, dt):
        if not self.is_active:
            return
        
        # Анимация появления текста
        if self.char_index < len(self.active_dialog["lines"][self.current_line]["text"]):
            self.char_index += self.text_speed * dt
            self.text_alpha = min(255, self.text_alpha + 5)

    def render(self, screen):
        if not self.is_active:
            return

        # Затемнение фона
        overlay = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Текущая реплика
        line = self.active_dialog["lines"][self.current_line]
        speaker_text = self.font.render(f"{line['speaker']}:", True, (255, 255, 255))
        screen.blit(speaker_text, (50, 700))

        # Анимированный текст
        visible_text = line["text"][:int(self.char_index)]
        text_surface = self.font.render(visible_text, True, (255, 255, 255))
        text_surface.set_alpha(self.text_alpha)
        screen.blit(text_surface, (50, 700))