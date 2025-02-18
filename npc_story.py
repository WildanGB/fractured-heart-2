import pygame
from entity import Entity 
from player_story import *
from Dialog_story import *
from Dialog_Tree_story import *
# from level import dialog_active

class Npc(Entity): 
    def __init__(self, pos,groups,npc_name):
        super().__init__(groups)

        self.sprite_type = 'npc'
        if npc_name == "npc1":
            self.image = pygame.image.load('../assets/images/npcs/npc1.png').convert_alpha()
            self.dialog_tree = dialog_tree_1

        elif npc_name == "npc2":
            self.image = pygame.image.load('../assets/images/npcs/npc2.png').convert_alpha()
            self.dialog_tree = dialog_tree_2

        else :
            self.image = pygame.image.load('../assets/images/npcs/npc3.png').convert_alpha()
            self.dialog_tree = dialog_tree_3 

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)  # Adjust as needed


        self.proximity_radius = 100 
        self.proximity_time = None
        self.proxcount = 0
        # self.pause = dialog_active()

        # self.dialog_active = False
        self.dialog_manager = DialogManager(self.dialog_tree)
        self.dialog =  DialogRenderer(self.dialog_manager,self.image)


    def Getimage(self):
        return self.image 


    def proximity(self,player):
        if self.proxcount == 0: 
            npc_vec = pygame.math.Vector2(self.rect.center)
            player_vec = pygame.math.Vector2(player.rect.center)
            distance = (player_vec - npc_vec).magnitude()
            if distance < self.proximity_radius:
                # self.pause.dialog_active()
                # self.dialog_active = True
                self.dialog.dialog_active = True
                self.proximity_time = pygame.time.get_ticks()
                self.proxcount = 1
            else: 
                self.dialog.dialog_active = False

    def proximity_cooldown(self):
        if self.dialog.dialog_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.proximity_time >= 200:
                self.proxcount = 0
        

    def npc_update(self, player):
        # self.dialog.save_screen()
        self.proximity(player)
        self.proximity_cooldown()
        if self.dialog.dialog_active:
            self.dialog.render() 
            # if self.dialog.dialog_manager.is_end():
            #     self.dialog.dialog_active = False
                # self.dialog_active = False
                # self.pause.dialog_active()
                