import pygame
import sys
from settings import *
from level import Level


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.selected_index = 0
        self.show_credits = False
        self.show_howto = False  # How to Play visibility flag
        self.howto_scroll_offset = 0  # Scroll position for How to Play

        # Initialize level for background
        self.level = Level()

        # Title setup
        self.title_font = pygame.font.Font(UI_FONT, 72)
        self.title_text = self.title_font.render("FRACTURED HEART", True, TEXT_COLOR)
        self.title_rect = self.title_text.get_rect(center=(WIDTH // 2, 80))

        # Menu setup
        self.menu_font = pygame.font.Font(UI_FONT, 42)
        self.menu_items = [
            {"text": "Start Game", "action": "start"},
            {"text": "How to Play", "action": "howto"},
            {"text": "Credits", "action": "credits"},
            {"text": "Quit", "action": "quit"}
        ]
        self.menu_spacing = 55
        self.menu_start_y = HEIGHT // 3 + 30

        # Font declarations for all screens
        # Credits fonts
        self.credits_font_large = pygame.font.Font(UI_FONT, 48)
        self.credits_font_med = pygame.font.Font(UI_FONT, 34)
        self.credits_font_small = pygame.font.Font(UI_FONT, 26)

        # How to Play fonts
        self.howto_font_large = pygame.font.Font(UI_FONT, 40)
        self.howto_font_medium = pygame.font.Font(UI_FONT, 32)
        self.howto_font_small = pygame.font.Font(UI_FONT, 28)

        # How to Play content
        self.howto_content = [
            (self.howto_font_large, "How To Play", TEXT_COLOR),
            (self.howto_font_small, "Welcome to Fractured-Heart!", TEXT_COLOR),
            (self.howto_font_small, "Embark on a top-down adventure"
                                    " inspired by classic Zelda titles.", TEXT_COLOR),
            (self.howto_font_small, "Explore a sprawling map,"
                                    " battle fierce enemies, and uncover"
                                    " hidden secrets.",
             TEXT_COLOR),
            (None, None, None),  # Spacer

            (self.howto_font_medium, "Basic Movement", UI_COLOR),
            (self.howto_font_small, "W, A, S, D  to move up, left, down, and right.", TEXT_COLOR),
            (self.howto_font_small, "Avoid hazardous terrain and hidden traps in certain areas!", TEXT_COLOR),
            (None, None, None),

            (self.howto_font_medium, "Combat", UI_COLOR),
            (self.howto_font_small, "SPACE: Perform a melee attack (weapon swing)", TEXT_COLOR),
            (self.howto_font_small, "Q: Switch weapons by pressing Q)", TEXT_COLOR),
            (self.howto_font_small, "Left Shift: Cast a magic spell (requires energy)", TEXT_COLOR),
            (self.howto_font_small, "Monitor health and energy bars at the bottom of the screen", TEXT_COLOR),
            (None, None, None),

            (self.howto_font_medium, "Magic & Spells", UI_COLOR),
            (self.howto_font_small, "Switch spells by pressing E", TEXT_COLOR),
            (self.howto_font_small, "Casting spells costs energy - manage resources wisely", TEXT_COLOR),
            (self.howto_font_small, "Different spells have unique effects (healing, fire, etc.)", TEXT_COLOR),
            (None, None, None),

            (self.howto_font_medium, "Upgrading Your Character", UI_COLOR),
            (self.howto_font_small, "Press U to open the Upgrade Menu", TEXT_COLOR),
            (self.howto_font_small, "Spend EXP to improve health, energy, attack, and more", TEXT_COLOR),
            (self.howto_font_small, "Each upgrade helps you survive tougher enemies", TEXT_COLOR),
            (None, None, None),

            (self.howto_font_medium, "Objectives & Exploration", UI_COLOR),
            (self.howto_font_small, "Navigate the map to find quests, items, and bosses", TEXT_COLOR),
            (self.howto_font_small, "Interact with NPCs to learn about the world", TEXT_COLOR),
            (self.howto_font_small, "Some areas require special items or spells to access", TEXT_COLOR),
            (None, None, None),

        ]

        # Background setup
        self.level.visible_sprites.custom_draw(self.level.player)
        pygame.image.save(self.screen, "../assets/images/map assets/temp_background.png")
        self.background_image = pygame.image.load("../assets/images/map assets/temp_background.png")
        self.background_blur = pygame.transform.smoothscale(self.background_image, (WIDTH // 4, HEIGHT // 4))
        self.background_blur = pygame.transform.smoothscale(self.background_blur, (WIDTH, HEIGHT))

    def display_credits(self):
        self.screen.blit(self.background_blur, (0, 0))

        elements = [
            (self.credits_font_large, "Fractured Heart", 80, TEXT_COLOR),
            (self.credits_font_med, "Created for the 2025 "
                                    " Computer Science Game Project", 130, TEXT_COLOR),
            (self.credits_font_med, "Credits:", 200, UI_COLOR),
            (self.credits_font_small, "Wildan - Lead Developer", 250, TEXT_COLOR),
            (self.credits_font_small, "Mahtab - AI Integration Specialist", 300, TEXT_COLOR),
            (self.credits_font_small, "Abizar - Gameplay Designer", 350, TEXT_COLOR),
            (self.credits_font_small, "Marwan & Yousif - Assets & UI Designers", 400, TEXT_COLOR),
            (self.credits_font_small, "This game is protected under an open source license.", 500, TEXT_COLOR),
            (self.credits_font_small, "Fork the game from Fractured-Heart on GitHub", 540, TEXT_COLOR),
            (self.credits_font_small, "Press ESC to return to menu", HEIGHT - 60, SPARE)
        ]

        for font, text, y_pos, color in elements:
            text_surface = font.render(text, True, color)
            self.screen.blit(text_surface, text_surface.get_rect(center=(WIDTH // 2, y_pos)))

    def display_howto(self):
        self.screen.blit(self.background_blur, (0, 0))
        y_pos = 60 - self.howto_scroll_offset
        line_height = 40

        for font, text, color in self.howto_content:
            if font is None:  # Spacer
                y_pos += line_height
                continue

            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect(topleft=(50, y_pos))

            # Only draw visible text
            if text_rect.bottom > 0 and text_rect.top < HEIGHT:
                self.screen.blit(text_surface, text_rect)

            y_pos += line_height

        # Scroll instructions
        prompt = self.howto_font_small.render("Use arrow keys to scroll | Press ESC to return", True, SPARE)
        self.screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT - 30)))

    def display(self):
        if self.show_credits:
            self.display_credits()
            return
        if self.show_howto:
            self.display_howto()
            return

        self.screen.blit(self.background_blur, (0, 0))
        self.screen.blit(self.title_text, self.title_rect)

        for index, item in enumerate(self.menu_items):
            y_pos = self.menu_start_y + (index * self.menu_spacing)
            color = HOVER_COLOR if index == self.selected_index else TEXT_COLOR
            text_surface = self.menu_font.render(item["text"], True, color)
            rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
            self.screen.blit(text_surface, rect)

    def handle_input(self, event):
        if self.show_credits:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
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
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
                return None  # Prevent accidental game start

        return None