import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from enemy_spawner import EnemySpawner  # Import the enemy spawner
from npc import Npc


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

        # --- CHUNK LOADING SETUP ---
        self.chunk_size = 10  # Number of tiles per chunk; adjust as needed
        self.chunks = {}  # Dictionary to hold sprites by chunk key

        # sprite group setup: use the new ChunkedCameraGroup instead of YSortCameraGroup
        self.visible_sprites = ChunkedCameraGroup(self.chunks, self.chunk_size)
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # Collision grid setup (if used)
        self.collision_grid = {}
        self.grid_size = COLLISION_GRID_SIZE

        # Initialize enemy spawn points list (for respawning)
        self.enemy_spawn_points = []

        # sprite setup: create map (this also records enemy spawn points)
        self.create_map()

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

        # particles and magic
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

        # Instantiate the enemy spawner (area-based and time-based respawn)
        self.enemy_spawner = EnemySpawner(self, area_size=100, respawn_interval=5000, update_interval=1000)

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../assets/csv files/game map_FloorBlocks.csv'),
            'grass': import_csv_layout('../assets/csv files/game map_breakable grass.csv'),
            'object': import_csv_layout('../assets/images/video assets/map/map_Objects.csv'),
            'entities': import_csv_layout('../assets/csv files/game map_entities.csv')
        }
        graphics = {
            'grass': import_folder('../assets/images/map assets/grass'),
            'objects': import_folder('../assets/images/video assets/graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col == '-1':
                        continue

                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    # Compute chunk key based on tile indices divided by chunk_size
                    chunk_x = col_index // self.chunk_size
                    chunk_y = row_index // self.chunk_size
                    chunk_key = (chunk_x, chunk_y)
                    if chunk_key not in self.chunks:
                        self.chunks[chunk_key] = []

                        if style == 'boundary':
                            sprite = Tile((x, y), [self.obstacle_sprites], 'invisible')
                            self.chunks[chunk_key].append(sprite)
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            sprite = Tile(
                                (x, y),
                                [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                                'grass',
                                random_grass_image)
                            self.chunks[chunk_key].append(sprite)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            sprite = Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                            self.chunks[chunk_key].append(sprite)
                        if style == 'entities':
                            if col == '0':
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)
                                # Optionally, add player to a chunk:
                                # self.chunks[chunk_key].append(self.player)
                            elif col == '80':
                                    npc = Npc((x,y),[self.visible_sprites, self.obstacle_sprites],"npc1")
                                    self.chunks[chunk_key].append(npc)
                            elif col == '81':
                                    npc = Npc((x,y),[self.visible_sprites, self.obstacle_sprites],"npc2")
                                    self.chunks[chunk_key].append(npc)
                            elif col == '82':
                                    npc = Npc((x,y),[self.visible_sprites, self.obstacle_sprites],"npc3")
                                    self.chunks[chunk_key].append(npc)
                            else:
                                if col == '1':
                                    monster_name = 'tree'
                                elif col == '2':
                                    monster_name = 'cherry tree'
                                elif col == '3':
                                    monster_name = 'snowy tree'
                                elif col == '4':
                                    monster_name = 'spirit'
                                elif col == '5':
                                    monster_name = 'ninja'
                                elif col == '6':
                                    monster_name = 'oni'
                                else:
                                    monster_name = 'tree'
                                enemy = Enemy(
                                    monster_name,
                                    (x, y),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles,
                                    self.add_exp)
                                self.chunks[chunk_key].append(enemy)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
        if style == 'flame':
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 75)
                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def toggle_menu(self):
        self.game_paused = not self.game_paused

    def dialog_active(self):
        self.game_paused = not self.game_paused

    def run(self):
        if self.game_paused:
            if not hasattr(self, 'pause_background'):
                self.pause_background = self.display_surface.copy()
            self.display_surface.blit(self.pause_background, (0, 0))
            self.ui.display(self.player)
            self.upgrade.display()
        else:
            if hasattr(self, 'pause_background'):
                del self.pause_background
            self.visible_sprites.custom_draw(self.player)
            for sprite in self.attack_sprites:
                if not sprite.alive():
                    continue
                offset_pos = sprite.rect.topleft - self.visible_sprites.offset
                self.display_surface.blit(sprite.image, offset_pos)
            self.ui.display(self.player)
            self.visible_sprites.update()
            self.visible_sprites.npc_update(self.player)
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()
            # Update enemy respawn based on area and time intervals
            self.enemy_spawner.update()

            for npc in self.visible_sprites:
                if hasattr(npc, 'sprite_type') and npc.sprite_type == 'npc'and npc.dialog.dialog_active:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            npc.dialog.handle_events(event)  # Pass events to the dialog


# New ChunkedCameraGroup for chunk loading
class ChunkedCameraGroup(pygame.sprite.Group):
    def __init__(self, chunks, chunk_size):
        super().__init__()
        self.chunks = chunks  # Dictionary with keys: (chunk_x, chunk_y) and values: lists of sprites
        self.chunk_size = chunk_size  # in tiles
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()
        self.floor_surf = pygame.image.load('../assets/images/map assets/game map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        player_chunk_x = player.rect.centerx // (self.chunk_size * TILESIZE)
        player_chunk_y = player.rect.centery // (self.chunk_size * TILESIZE)
        sprites_to_draw = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                key = (player_chunk_x + dx, player_chunk_y + dy)
                if key in self.chunks:
                    sprites_to_draw.extend(self.chunks[key])
        view_rect = pygame.Rect(self.offset.x, self.offset.y,
                                self.display_surface.get_width(),
                                self.display_surface.get_height())
        for sprite in sorted(sprites_to_draw, key=lambda spr: spr.rect.centery):
            if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'invisible':
                continue
            if not sprite.alive():
                continue
            if sprite.rect.colliderect(view_rect):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
        offset_pos = player.rect.topleft - self.offset
        self.display_surface.blit(player.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)

    def npc_update(self, player):
        npc_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'npc']
        for npc in npc_sprites:
            npc.npc_update(player)  # Call the NPC's update method
