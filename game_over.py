import pygame
from settings import *
from level import Level

class GameOverScreen :
    def __init__ ( self , screen , level ) :
        self.screen = screen
        self.level = level
        self.game_over_text_pos = -100
        self.button_width = 200
        self.button_height = 60
        self.button_spacing = 50
        self.restart_button = pygame.Rect (
            (WIDTH // 2) - (self.button_width + self.button_spacing // 2) ,
            HEIGTH // 2 + 100 ,
            self.button_width ,
            self.button_height )
        self.quit_button = pygame.Rect (
            (WIDTH // 2) + (self.button_spacing // 2) ,
            HEIGTH // 2 + 100 ,
            self.button_width ,
            self.button_height )

    def display ( self ) :
        self.level.visible_sprites.custom_draw ( self.level.player )
        font = pygame.font.Font ( None , 100 )
        game_over_text = font.render ( "GAME OVER" , True , "red" )
        text_rect = game_over_text.get_rect ( center = (WIDTH // 2 , self.game_over_text_pos) )
        self.screen.blit ( game_over_text , text_rect )

        if self.game_over_text_pos < HEIGTH // 2 :
            self.game_over_text_pos += 5
        else :
            pygame.draw.rect ( self.screen , "green" , self.restart_button )
            pygame.draw.rect ( self.screen , "red" , self.quit_button )
            button_font = pygame.font.Font ( None , 50 )
            restart_text = button_font.render ( "Restart" , True , "black" )
            quit_text = button_font.render ( "Quit" , True , "black" )
            restart_rect = restart_text.get_rect ( center = self.restart_button.center )
            quit_rect = quit_text.get_rect ( center = self.quit_button.center )
            self.screen.blit ( restart_text , restart_rect )
            self.screen.blit ( quit_text , quit_rect )

    def handle_input ( self , event ) :
        mouse_pos = pygame.mouse.get_pos ()
        if event.type == pygame.MOUSEBUTTONDOWN :
            if self.restart_button.collidepoint ( mouse_pos ) :
                return "restart"
            elif self.quit_button.collidepoint ( mouse_pos ) :
                return "quit"
        return None
