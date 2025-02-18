import pygame
from enemy import Enemy

class EnemySpawner:
    def __init__(self, level, area_size=100, respawn_interval=5000, update_interval=1000):
        """
        level: the Level instance.
        area_size: size (in pixels) of the base area to check around each spawn point.
        respawn_interval: time (ms) to wait before respawning an enemy if absent.
        update_interval: time (ms) between each respawn check.
        """
        self.level = level
        self.area_size = area_size
        self.respawn_interval = respawn_interval
        self.update_interval = update_interval
        self.last_update = pygame.time.get_ticks()
        # Dictionary mapping each spawn point (monster_name, (x, y)) to last spawn time.
        self.spawn_times = {spawn: pygame.time.get_ticks() for spawn in self.level.enemy_spawn_points}

    def enemy_in_area(self, pos):
        """
        Returns True if the spawn point is either visible on screen or if an enemy is already
        present in a larger area around pos.
        """
        # Build the camera rectangle based on the player's position.
        player = self.level.player
        cam_width = self.level.display_surface.get_width()
        cam_height = self.level.display_surface.get_height()
        camera_rect = pygame.Rect(0, 0, cam_width, cam_height)
        camera_rect.center = player.rect.center

        # If spawn point is visible, don't respawn.
        if camera_rect.collidepoint(pos):
            return True

        # Increase the check area (e.g., twice the base area_size) so that if an enemy exists nearby, do not spawn.
        check_size = self.area_size * 2
        area_rect = pygame.Rect(0, 0, check_size, check_size)
        area_rect.center = pos
        for enemy in self.level.attackable_sprites:
            if enemy.rect.colliderect(area_rect):
                return True
        return False

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update < self.update_interval:
            return  # Throttle updates.
        self.last_update = current_time

        for spawn in self.level.enemy_spawn_points:
            last_spawn_time = self.spawn_times.get(spawn, 0)
            if current_time - last_spawn_time >= self.respawn_interval:
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
                    # Reset key properties so that the enemy starts properly.
                    new_enemy.frame_index = 0
                    new_enemy.status = 'idle'
                    new_enemy.vulnerable = True
                    self.spawn_times[spawn] = current_time
