import pygame
from settings import *
from level import Level

class StartScreen :
    def __init__ ( self , screen ) :
        self.screen = screen

        # Create a Level instance to generate a background image
        self.level = Level ()
        # It is assumed that self.level.player is set during Level initialization.

        # Set up fonts using the declared UI_FONT from settings.py with smaller sizes
        self.title_font = pygame.font.Font ( UI_FONT , 80 )  # reduced size
        self.prompt_font = pygame.font.Font ( UI_FONT , 40 )  # reduced size

        # Render texts for the title and the prompt using TEXT_COLOR
        self.title_text = self.title_font.render ( "FRACTURED HEART" , True , TEXT_COLOR )
        self.prompt_text = self.prompt_font.render ( "PRESS ANY KEY TO BEGIN" , True , TEXT_COLOR )

        # Calculate rectangles for centering the texts
        self.title_rect = self.title_text.get_rect ( center = (WIDTH // 2 , 100) )
        self.prompt_rect = self.prompt_text.get_rect ( center = (WIDTH // 2 , HEIGHT // 2) )

        # Create a temporary background by drawing the current level’s background
        self.level.visible_sprites.custom_draw ( self.level.player )
        pygame.image.save ( self.screen , "../graphics/tilemap/temp_background.png" )
        self.background_image = pygame.image.load ( "../graphics/tilemap/temp_background.png" )

        # Create a blurred version of the background by scaling down then up
        self.background_blur = pygame.transform.smoothscale ( self.background_image , (WIDTH // 4 , HEIGHT // 4) )
        self.background_blur = pygame.transform.smoothscale ( self.background_blur , (WIDTH , HEIGHT) )

    def display ( self ) :
        self.screen.blit ( self.background_blur , (0 , 0) )
        self.screen.blit ( self.title_text , self.title_rect )
        self.screen.blit ( self.prompt_text , self.prompt_rect )

    def handle_input ( self , event ) :
        if event.type == pygame.KEYDOWN :
            return True
        return False
