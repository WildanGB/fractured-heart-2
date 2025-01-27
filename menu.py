import pygame
from settings import *
from level import Level

class MainMenuScreen :
    def __init__ ( self , screen ) :
        self.screen = screen
        self.level = Level ()
        self.title_font = pygame.font.Font ( None , 120 )
        self.prompt_font = pygame.font.Font ( None , 50 )
        self.title_text = self.title_font.render ( "FRACTURED HEART" , True , "white" )
        self.prompt_text = self.prompt_font.render ( "PRESS ANY KEY TO BEGIN" , True , "white" )
        self.title_rect = self.title_text.get_rect ( center = (SCREEN_WIDTH // 2 , 100) )
        self.prompt_rect = self.prompt_text.get_rect ( center = (SCREEN_WIDTH // 2 , SCREEN_HEIGTH // 2) )
        self.background_surface = pygame.Surface ( (SCREEN_WIDTH , SCREEN_HEIGTH) , pygame.SRCALPHA )
        self.level.visible_sprites.custom_draw ( self.level.player )
        pygame.image.save ( self.screen , "temp_background.png" )
        self.background_image = pygame.image.load ( "temp_background.png" )
        self.background_blur = pygame.transform.smoothscale ( self.background_image , (
        SCREEN_WIDTH // 4 , SCREEN_HEIGTH // 4) )
        self.background_blur = pygame.transform.smoothscale ( self.background_blur , (SCREEN_WIDTH , SCREEN_HEIGTH) )

    def display ( self ) :
        self.screen.blit ( self.background_blur , (0 , 0) )
        self.screen.blit ( self.title_text , self.title_rect )
        self.screen.blit ( self.prompt_text , self.prompt_rect )

    def handle_input ( self , event ) :
        if event.type == pygame.KEYDOWN :
            return True
        return False
