import pygame
from random import choice , randint
from enemy import Enemy

class EnemySpawner :
    def __init__ ( self , level ) :
        self.level = level
        self.enemies = pygame.sprite.Group ()

    def spawn_enemy ( self ) :
        monster_name = choice ( [ 'bamboo' , 'spirit' , 'raccoon' , 'squid' ] )  # Choose random enemy type
        x = randint ( 100 , 800 )  # Random X position (adjust as needed)
        y = randint ( 100 , 800 )  # Random Y position (adjust as needed)

        new_enemy = Enemy (
            monster_name ,
            (x , y) ,
            [ self.level.visible_sprites , self.level.attackable_sprites , self.enemies ] ,
            self.level.obstacle_sprites ,
            self.level.damage_player ,
            self.level.trigger_death_particles ,
            self.level.add_exp
        )

        return new_enemy

    def check_respawn ( self ) :
        # If all enemies are dead, respawn a batch
        if not self.enemies :
            for _ in range ( randint ( 2 , 5 ) ) :  # Adjust range based on difficulty
                enemy = self.spawn_enemy ()
                self.enemies.add ( enemy )  # Keep track of enemies

    def update ( self ) :
        self.check_respawn ()
