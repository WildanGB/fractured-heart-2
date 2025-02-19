# Fractured‑Heart: A 2D Zelda‑Inspired Adventure Game

**Project Title:** Fractured‑Heart  
**Student Name:** Wildan, Mahtab, Marwan, Abizar, Yousif Faisal
**Date:** February 2025

---

## Table of Contents

1. [Introduction](#introduction)
2. [Hardware/Software Requirements](#hardwaresoftware-requirements)
3. [Design Strategies](#design-strategies)
   - [Performance Optimizations](#performance-optimizations)
   - [Artificial Intelligence and Dialogue](#artificial-intelligence-and-dialogue)
4. [Project Architecture and Code Overview](#project-architecture-and-code-overview)
   - [Module Structure](#module-structure)
   - [Key Components and Their Roles](#key-components-and-their-roles)
5. [Selected Code Snippets](#selected-code-snippets)
6. [Development Process and Team Collaboration](#development-process-and-team-collaboration)
7. [Screenshots and Output](#screenshots-and-output)
8. [Conclusion](#conclusion)

---

## 1. Introduction

**Fractured‑Heart** is a 2D action-adventure game inspired by classic Zelda titles. The game immerses players in a richly detailed world where exploration, combat, and narrative-driven interactions all play critical roles. Players traverse expansive maps, confront challenging enemies, and engage with NPCs through dynamic, branching dialogues. The project not only emphasizes polished gameplay but also showcases advanced performance optimizations and AI integration to deliver a smooth and engaging experience.

The main objectives of the project are:
- **Engaging Gameplay:** Create a challenging yet rewarding adventure experience.
- **Performance:** Ensure smooth performance even on large maps by using optimization techniques like chunk loading and view culling.
- **AI Integration:** Develop sophisticated enemy behaviors, interactive NPC dialogs, and dynamic dialogue trees that respond to player choices.
- **Collaboration:** Use modern development practices (Git, GitHub Projects) to coordinate work among team members with diverse strengths.

---

## 2. Hardware/Software Requirements

### Hardware Requirements
- **Processor:** Intel Core i3 or equivalent
- **RAM:** 4 GB minimum (8 GB recommended)
- **Graphics:** Integrated or dedicated GPU
- **Storage:** Minimum 500 MB free space
- **Display:** 1280×720 resolution or higher

### Software Requirements
- **Operating System:** Windows, macOS, or Linux (with Python support)
- **Python:** Version 3.7 or higher
- **Pygame:** Version 2.0 or higher
- **Additional Libraries:** os, sys, random, threading (included with Python)
- **IDE/Editor:** PyCharm, VSCode, or any Python-compatible IDE

---

## 3. Design Strategies

### Performance Optimizations

To maintain a smooth gameplay experience on large maps, several optimization techniques have been employed:

- **Chunk Loading and View Culling:**  
  The game divides the map into smaller sections or “chunks.” Only the chunks that are near the player are rendered. This technique minimizes the number of sprites drawn each frame, improving performance.  
  *Example:* The custom `ChunkedCameraGroup` class calculates the visible area based on the player's position and draws only those sprites that fall within or near this area.

- **Enemy Respawn Control and Object Pooling:**  
  An enemy spawner monitors designated enemy spawn points and respawns enemies only when they are off-screen and no enemy is already present nearby. This prevents endless spawns of enemies (e.g. raccoons) and ensures resource efficiency.

### Artificial Intelligence and Dialogue

A major focus of the project is on the integration of AI, which is applied in several areas:

- **Enemy Behavior:**  
  Enemies dynamically evaluate their distance from the player and switch between states (idle, move, attack). They use timers and cooldowns to regulate their actions. For example, an enemy might enter an “attack” state when the player is within a certain range and revert to “idle” if the player moves out of range.

- **NPC Interactions:**  
  Non-player characters (NPCs) are designed to enrich the game’s narrative. They provide quests, offer hints, and sometimes challenge the player. NPCs use a dialogue system that can branch based on player choices.

- **Dialogue System:**  
  The dialogue system is designed to support branching conversations. It loads dialogue trees from external data sources and uses decision-making algorithms (such as binary trees or loop-based searches) to determine the next dialogue node. This creates a dynamic and adaptive narrative experience.

---

## 4. Project Architecture and Code Overview

### Module Structure

The project is organized into several key directories and modules:

- **assets/**  
  Contains all images, sounds, and other media files.

- **code/**  
  Houses the main game logic:
  - **main.py:** Entry point of the game.
  - **level.py / level_story.py:** Manage map creation, sprite grouping, chunk loading, and enemy respawning.
  - **player.py & enemy.py:** Define entity behavior (movement, combat, animation).
  - **particles_story.py:** Handles particle effects (magic spells, enemy death animations).
  - **enemy_spawner.py:** Implements the enemy respawn system.
  - **start_screen.py:** Provides the main menu interface.
  - **npc.py:** Manages NPC behaviors and dialogues.

- **docs/**  
  Contains documentation files.

- **tests/**  
  Houses unit tests and integration tests.

### Key Components and Their Roles

- **Main Game Loop (main.py):**  
  Initializes Pygame, loads assets, displays loading and transition screens, and launches the main menu. It then conditionally starts the regular game or story mode based on user input.

- **Level Management (level.py / level_story.py):**  
  Constructs the game map from CSV files, assigns sprites to chunks, and manages enemy spawn points.

- **Entity Classes (player.py & enemy.py):**  
  Define the behaviors, collision logic, and animations for the player and enemy characters.

- **Optimization Techniques (ChunkedCameraGroup):**  
  Implements chunk loading and view culling to ensure that only visible sprites are rendered.

- **AI Integration (enemy_ai, Dialogue System in npc.py):**  
  Enemies and NPCs use AI logic to interact with the player. Dialogue systems provide branching conversations that influence gameplay.

---

## 5. Selected Code Snippets

### Code Snippet 1: Chunked Camera Group (View Culling & Chunk Loading)
```python
class ChunkedCameraGroup(pygame.sprite.Group):
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
```
### Code Snippet 2: Enemy Respawn Logic (EnemySpawner.update)
```python
class EnemySpawner:
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
                    new_enemy.frame_index = 0
                    new_enemy.status = 'idle'
                    new_enemy.vulnerable = True
                    self.spawn_times[spawn] = current_time
```
### Code Snippet 3: Enemy Behavior (Status and Actions)
```python
def get_status(self, player):
    distance = self.get_player_distance_direction(player)[0]
    if distance <= self.attack_radius and self.can_attack:
        if self.status != 'attack':
            self.frame_index = 0
        self.status = 'attack'
    elif distance <= self.notice_radius:
        self.status = 'move'
    else:
        self.status = 'idle'

def actions(self, player):
    if self.status == 'attack':
        self.attack_time = pygame.time.get_ticks()
        self.damage_player(self.attack_damage, self.attack_type)
        self.attack_sound.play()
    elif self.status == 'move':
        self.direction = self.get_player_distance_direction(player)[1]
    else:
        self.direction = pygame.math.Vector2()
```
### Code Snippet 4: Dialogue System (Concept/Pseudocode)
```python
class DialogueManager:
    def __init__(self):
        self.dialogue_tree = self.load_dialogue_tree()

    def load_dialogue_tree(self):
        # Load dialogue data from a file or dictionary.
        return {}

    def start_dialogue(self, npc_id):
        dialogue = self.dialogue_tree.get(npc_id, [])
        self.display_dialogue(dialogue)

    def process_choice(self, choice):
        next_node = self.get_next_node(choice)
        self.display_dialogue(next_node)
```
### Code Snippet 5: Particle Effect with Placeholder (in particles_story.py)
```python
if not animation_frames or len(animation_frames) == 0:
    placeholder = pygame.Surface((TILESIZE, TILESIZE))
    placeholder.fill((255, 0, 255))
    self.frames = [placeholder]
else:
    self.frames = animation_frames
```
### Code Snippet 6: Main Menu Conditional Launch
```python
if game_mode == "story":
    import main_story
    main_story.main()
    sys.exit()
else:
    from level import Level as LevelClassic
    level = LevelClassic()
```
### Code Snippet 7: Asset Loading Example
```python
def load_assets():
    global assets
    assets['floor'] = pygame.image.load('../assets/images/map assets/game map.png').convert_alpha()
    assets['player'] = pygame.image.load('../assets/images/main character/player.png').convert_alpha()
    assets['foliage'] = pygame.image.load('../assets/images/map assets/foliage.png')
    print("Assets loaded.")
```
## 6. Development Process and Team Collaboration

### Our team leveraged GitHub for version control and GitHub Projects for task management. We divided our responsibilities based on individual strengths:

**Asset & UI Designer:**
-Designed all visual elements (tilesets, NPCs, animations) using Krita and Tiled. Created CSV map files and optimized assets for performance.

**AI Specialist:**
-Developed enemy behavior, NPC interaction, and a branching dialogue system that adapts to player choices. This AI integration forms the heart of the project.

**Core Programmer:**
Implemented core gameplay mechanics, performance optimizations (such as chunk loading and view culling), and integrated AI and dialogue systems into a cohesive codebase.

## Regular commits, pull requests, and code reviews helped ensure that all modules worked together seamlessly.


## 8. Conclusion

### Fractured‑Heart is a feature-rich 2D adventure game that combines engaging gameplay with advanced performance optimizations and AI-driven interactions. The use of chunk loading and view culling ensures smooth performance on expansive maps, while our sophisticated AI integration drives dynamic enemy behavior and interactive NPC dialogues. Our effective use of GitHub for version control and project management allowed for efficient collaboration among team members, ultimately resulting in a polished and immersive game experience.



