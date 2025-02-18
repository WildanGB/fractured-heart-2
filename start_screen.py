import pygame
import sys
from settings import *
from level import Level

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.selected_index = 0
        self.show_credits = False
        self.show_howto = False
        self.howto_scroll_offset = 0

        # Load background image
        self.background_image = pygame.image.load("../assets/images/map assets/menu.png")
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Title setup
        self.title_font = pygame.font.Font(UI_FONT, 64)  # Reduced from 72
        self.title_text = self.title_font.render("FRACTURED HEART", True, HOVER_COLOR)
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, 80))

        # Menu setup
        self.menu_font = pygame.font.Font(UI_FONT, 38)  # Reduced from 42
        self.menu_items = [
            {"text": "Start Game in Endless Mode", "action": "endless"},
            {"text": "Start Game in Story Mode", "action": "story"},
            {"text": "How to Play", "action": "howto"},
            {"text": "Credits", "action": "credits"},
            {"text": "Quit", "action": "quit"}
        ]
        self.menu_spacing = 50  # Adjusted for better spacing
        self.menu_start_y = HEIGHT // 3 + 30

        # Credits fonts
        self.credits_font_large = pygame.font.Font(UI_FONT, 42)  # Reduced from 48
        self.credits_font_med = pygame.font.Font(UI_FONT, 30)  # Reduced from 34
        self.credits_font_small = pygame.font.Font(UI_FONT, 22)  # Reduced from 26

        # How To Play fonts
        self.howto_font_large = pygame.font.Font(UI_FONT, 36)  # Reduced from 40
        self.howto_font_medium = pygame.font.Font(UI_FONT, 28)  # Reduced from 32
        self.howto_font_small = pygame.font.Font(UI_FONT, 22)  # Reduced from 28

        self.howto_content = [
            (self.howto_font_large, "How To Play", HOVER_COLOR),
            (self.howto_font_small, "Welcome to Fractured-Heart!", HOVER_COLOR),
            (self.howto_font_small, "Embark on a top-down adventure.", HOVER_COLOR),
            (None, None, None),
            (self.howto_font_medium, "Basic Movement", HOVER_COLOR),
            (self.howto_font_small, "W, A, S, D to move. Use it to your advantage", HOVER_COLOR),
            (None, None, None),
            (self.howto_font_medium, "Combat", HOVER_COLOR),
            (self.howto_font_small, "SPACE: Attack but keep an eye on your health bar", HOVER_COLOR),
            (self.howto_font_small, "Q: Switch weapons", HOVER_COLOR),
            (None, None, None),
            (self.howto_font_medium, "Magic & Spells", HOVER_COLOR),
            (self.howto_font_small, "M: Use spells but be careful not to deplete your energy bar", HOVER_COLOR),
            (self.howto_font_small, "E: Switch spells", HOVER_COLOR),
            (None, None, None),
            (self.howto_font_medium, "Upgrading and Progression", HOVER_COLOR),
            (self.howto_font_small, "Press U for upgrades, but cost more and more each time", HOVER_COLOR),
            (None, None, None),
            (self.howto_font_medium, "Endless Mode", HOVER_COLOR),
            (self.howto_font_small, "Fight waves and waves of respawning enemies", HOVER_COLOR),
            (self.howto_font_small, "Less XP, Stronger enemies, and a Smaller Map", HOVER_COLOR),
            (self.howto_font_small, "For people who enjoy the rush and thrill", HOVER_COLOR),
            (self.howto_font_small, "Get a taste of what mechanics Fractured Heart has to offer", HOVER_COLOR),
            (None, None, None),
            (self.howto_font_medium, "Story Mode", HOVER_COLOR),
            (self.howto_font_small, "Embark on a quest to find the fractured heart", HOVER_COLOR),
            (self.howto_font_small, "Bigger map, New enemies, and Lively NPCs and Dialogs", HOVER_COLOR),
            (self.howto_font_small, "For people who enjoy exploration and compelling stories", HOVER_COLOR),
            (self.howto_font_small, "Be part of the living and breathing Fractured Heart world", HOVER_COLOR),
            (None, None, None),
        ]
        self.howto_font_medium = pygame.font.Font(UI_FONT, 28)  # Reduced from 32
        self.howto_font_small = pygame.font.Font(UI_FONT, 22)  # Reduced from 28

        # Adjusted How To Play Content

    def display_credits(self):
        self.screen.blit(self.background_image, (0, 0))
        elements = [
            (self.credits_font_large, "Fractured Heart", 80, SPARE),
            (self.credits_font_med, "Created for the 2025 Project", 130, SPARE),
            (self.credits_font_med, "Credits:", 180, HOVER_COLOR),
            (self.credits_font_small, "Wildan - Lead Developer", 230, SPARE),
            (self.credits_font_small, "Mahtab - AI Specialist", 270, SPARE),
            (self.credits_font_small, "Abizar - Gameplay Designer", 310, SPARE),
            (self.credits_font_small, "Marwan & Yousif - UI Designers", 350, SPARE),
            (self.credits_font_small, "Press ESC to return", HEIGHT - 70, HOVER_COLOR)
        ]
        for font, text, y_pos, color in elements:
            text_surface = font.render(text, True, color)
            self.screen.blit(text_surface, text_surface.get_rect(center=(WIDTH // 2, y_pos)))

    def display_howto(self):
        self.screen.blit(self.background_image, (0, 0))
        y_pos = 50 - self.howto_scroll_offset
        line_height = 35  # Adjusted for better spacing
        for font, text, color in self.howto_content:
            if font is None:
                y_pos += line_height
                continue
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(topleft=(50, y_pos))
            if text_rect.bottom > 0 and text_rect.top < HEIGHT:
                self.screen.blit(text_surface, text_rect)
            y_pos += line_height

        # Moved the scroll instruction higher so it's fully visible
        prompt = self.howto_font_small.render("Use arrow keys to scroll | Press ESC to return", True, SPARE)
        self.screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT - 80)))

    def display(self):
        if self.show_credits:
            self.display_credits()
            return
        if self.show_howto:
            self.display_howto()
            return
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.title_text, self.title_rect)
        for index, item in enumerate(self.menu_items):
            y_pos = self.menu_start_y + (index * self.menu_spacing)
            color = SPARE if index == self.selected_index else TEXT_COLOR
            text_surface = self.menu_font.render(item["text"], True, color)
            rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
            self.screen.blit(text_surface, rect)

    def handle_input(self, event):
        if self.show_credits:
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                self.show_credits = False
            return None

        if self.show_howto:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                    self.show_howto = False
                    self.howto_scroll_offset = 0
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.howto_scroll_offset = max(0, self.howto_scroll_offset - 20)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.howto_scroll_offset += 20
            return None

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected_index = (self.selected_index + 1) % len(self.menu_items)
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.selected_index = (self.selected_index - 1) % len(self.menu_items)
            elif event.key == pygame.K_RETURN:
                action = self.menu_items[self.selected_index]["action"]
                if action == "credits":
                    self.show_credits = True
                elif action == "howto":
                    self.show_howto = True
                elif action == "endless":
                    return "endless"
                elif action == "story":
                    return "story"
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
        return None
