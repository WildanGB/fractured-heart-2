import pygame
from enemy import Enemy

class EnemySpawner:
    def __init__(self, level, area_size=100, respawn_interval=5000, update_interval=1000):
        """
        level: the Level instance.
        area_size: size (in pixels) of the area to check around each spawn point.
        respawn_interval: time in ms to wait before respawning an enemy if absent.
        update_interval: time in ms between each respawn check.
        """
        self.level = level
        self.area_size = area_size
        self.respawn_interval = respawn_interval
        self.update_interval = update_interval
        self.last_update = pygame.time.get_ticks()
        # Dictionary mapping spawn point (monster_name, (x,y)) to last spawn time.
        self.spawn_times = {spawn: pygame.time.get_ticks() for spawn in self.level.enemy_spawn_points}

    def enemy_in_area(self, pos):
        """
        First, check if the spawn point is visible on the screen.
        If it is visible, return True (i.e. don't respawn).
        Otherwise, check if any enemy exists in the area around the spawn point.
        """
        # Get the camera view rectangle (assuming camera is centered on the player)
        player = self.level.player
        camera_rect = pygame.Rect(0, 0, self.level.display_surface.get_width(),
                                         self.level.display_surface.get_height())
        camera_rect.center = player.rect.center

        # If spawn point is visible, do not respawn (return True)
        if camera_rect.collidepoint(pos):
            return True

        # Create an area rect around the spawn point
        area_rect = pygame.Rect(0, 0, self.area_size, self.area_size)
        area_rect.center = pos
        for enemy in self.level.attackable_sprites:
            if enemy.rect.colliderect(area_rect):
                return True
        return False

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update < self.update_interval:
            return  # Throttle update calls.
        self.last_update = current_time

        for spawn in self.level.enemy_spawn_points:
            last_spawn_time = self.spawn_times.get(spawn, 0)
            if current_time - last_spawn_time >= self.respawn_interval:
                # spawn is a tuple: (monster_name, (x, y))
                if not self.enemy_in_area(spawn[1]):
                    monster_name, pos = spawn
                    new_enemy = Enemy(
                        monster_name,
                        pos,
                        [self.level.visible_sprites, self.level.attackable_sprites],
                        self.level.obstacle_sprites,
                        self.level.damage_player,
                        self.level.trigger_death_particles,
                        self.level.add_exp
                    )
                    # Update last spawn time for this spawn point.
                    self.spawn_times[spawn] = current_time
