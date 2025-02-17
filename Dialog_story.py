import pygame
from settings import * 
from npc import *

class DialogRenderer:
    def __init__(self,dialog_manager,img):
        self.screen = pygame.display.get_surface()
        self.screen_copy = None
        self.font = pygame.font.Font(UI_FONT, DIALOG_FONT_SIZE)
        self.dialog_manager = dialog_manager
        self.selected_option = 0
        # self.character_image = pygame.image.load("../assets/images/npcs/npc1.png")  # Replace with your image path
        self.character_image = pygame.transform.scale(img, (85, 102))  # Resize to fit
        self.dialog_box = pygame.image.load("../assets/images/npcs/dialogbox.png")
        self.dialog_box = pygame.transform.smoothscale(self.dialog_box,(DIALOG_BOX_WIDTH,DIALOG_BOX_HEIGHT) ) # Resize to fit
        self.character_name = "Merchant"
        self.dialogbox_x , self.dialogbox_y = 180, 430
        self.textbox_x ,self.textbox_y= self.dialogbox_x + 170, self.dialogbox_y + 120
        self.textbox_width, self.textbox_height = DIALOG_TEXT_WIDTH, DIALOG_TEXT_HEIGHT
        self.BLACK = (0,0,0)
        self.BEIGE = (240, 220, 180)
        self.dialog_active = False  # Track if the dialog is active



    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            choices = list(self.dialog_manager.get_choices().keys())
            if event.key == pygame.K_DOWN:
                # Move selection down
                self.selected_option = (self.selected_option + 1) % len(choices)
            elif event.key == pygame.K_UP:
                # Move selection up
                self.selected_option = (self.selected_option - 1) % len(choices)
            elif event.key == pygame.K_RETURN:
                # Confirm selection
                if choices:
                    selected_choice = choices[self.selected_option]
                    self.dialog_manager.choose(selected_choice)
                    self.selected_option = 0  # Reset selection
                    if self.dialog_manager.is_end():
                        self.dialog_active = False  # End dialog if no more choices
                        # self.restore_screen()

    def wrap_text(self,text, font, max_width):
        """
        Wrap text into multiple lines based on the maximum width.
        """
        words = text.split(' ')
        lines = []
        current_line = ''
        
        for word in words:
            # Test if adding the next word exceeds the max width
            test_line = f"{current_line} {word}".strip()
            test_width, _ = font.size(test_line)
            
            if test_width <= max_width:
                current_line = test_line
            else:
                # If it exceeds, start a new line
                lines.append(current_line)
                current_line = word
        
        # Add the last line
        if current_line:
            lines.append(current_line)
        
        return lines

    def render(self):

        if self.dialog_active:

            self.screen.blit(self.dialog_box,(self.dialogbox_x,self.dialogbox_y))

            portrait_x, portrait_y = 250, 550
            self.screen.blit(self.character_image, (portrait_x, portrait_y))

            name_text = self.font.render(self.character_name, True, (205, 127, 50))
            self.screen.blit(name_text, (250,650))
            dialog_box_rect = pygame.Rect(self.textbox_x,self.textbox_y, self.textbox_width, self.textbox_height)
            # pygame.draw.rect(self.screen, self.BEIGE, dialog_box_rect,border_radius=20)
            # pygame.draw.rect(self.screen,self.BLACK, dialog_box_rect,1, border_radius=20)

            text_x = self.textbox_x + 10
            text_y = self.textbox_y + 10
            # self.screen.fill((0, 0, 0))  # Clear screen

            # Get the current dialog text
            current_dialog = self.dialog_manager.get_current_dialog()
            
            # Wrap the text to fit within the dialog box
            # max_text_width = self.textbox_width - 0  # Account for padding
            wrapped_lines = self.wrap_text(current_dialog, self.font, self.textbox_width)
            
            # Render each line of wrapped text
            for i, line in enumerate(wrapped_lines):
                text_surface = self.font.render(line, True, (51, 51, 51))
                self.screen.blit(text_surface, (text_x, text_y + i * self.font.get_height()))
                # Display dialog text

            # text_surface = self.font.render(self.dialog_manager.get_current_dialog(), True, (0,0,0))
            # self.screen.blit(text_surface, (text_x, text_y))

            choices = list(self.dialog_manager.get_choices().keys())

            # Display choices
            for i, choice in enumerate(choices):
                color = (255, 140, 0) if i == self.selected_option else (112, 128, 144)
                choice_surface = self.font.render(f"> {choice}", True, color)
                self.screen.blit(choice_surface, (text_x, (text_y+60) + i * 25))

            pygame.display.update()
        else:
            pygame.display.self.screen2

# def draw_dialog_box(self):

#     self.screen.blit(self.dialog_box, (8,280))

#     portrait_x, portrait_y = 85, 445
#     self.screen.blit(self.character_image, (portrait_x, portrait_y))

#     name_text = self.font.render(self.character_name, True, self.BLACK)
#     self.screen.blit(name_text, (88,545))
