import pygame
from enemy_story import create_enemy
class EnemySpawner:
    def __init__(self, level, area_size=100, respawn_interval=5000, update_interval=1000):
        """
        level: the Level instance.
        area_size: size (in pixels) of the rectangular area around each spawn point to check.
        respawn_interval: time in ms to wait before respawning an enemy if absent.
        update_interval: time in ms between each respawn check.
        """
        self.level = level
        self.area_size = area_size
        self.respawn_interval = respawn_interval
        self.update_interval = update_interval
        self.last_update = pygame.time.get_ticks()
        # Record the last spawn time for each enemy spawn point.
        self.spawn_times = {spawn: pygame.time.get_ticks() for spawn in self.level.enemy_spawn_points}

    def enemy_in_area(self, pos):
        """
        Check if a spawn point at pos is either visible on screen or has an enemy nearby.
        """
        player = self.level.player
        cam_width = self.level.display_surface.get_width()
        cam_height = self.level.display_surface.get_height()
        camera_rect = pygame.Rect(0, 0, cam_width, cam_height)
        camera_rect.center = player.rect.center

        # If the spawn point is in view, return True (i.e. don't respawn now).
        if camera_rect.collidepoint(pos):
            return True

        # Otherwise, check for an enemy in a small area around pos.
        area_rect = pygame.Rect(0, 0, self.area_size, self.area_size)
        area_rect.center = pos
        for enemy in self.level.attackable_sprites:
            if enemy.rect.colliderect(area_rect):
                return True
        return False

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update < self.update_interval:
            return
        self.last_update = current_time

        for spawn in self.level.enemy_spawn_points:
            last_spawn_time = self.spawn_times.get(spawn, 0)
            if current_time - last_spawn_time >= self.respawn_interval:
                if not self.enemy_in_area(spawn[1]):
                    monster_name, pos = spawn
                    # Create a new enemy using the factory function
                    new_enemy = create_enemy(
                        monster_name,
                        pos,
                        [self.level.visible_sprites, self.level.attackable_sprites],
                        self.level.obstacle_sprites,
                        self.level.damage_player,
                        self.level.trigger_death_particles,
                        self.level.add_exp,
                    )
                    self.spawn_times[spawn] = current_time
