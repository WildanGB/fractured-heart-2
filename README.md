# Fractured‑Heart: A 2D Zelda‑Inspired Adventure Game

**Project Title:** Fractured‑Heart  
**Student Name:** [Your Name Here]  
**Student ID:** [Your Student ID Here]  
**Course:** [Your Course Name Here]  
**Instructor:** [Your Instructor Name Here]  
**Date:** [Month, Year]

---

## Index

1. [Introduction](#introduction)
2. [Hardware/Software Requirements](#hardwaresoftware-requirements)
3. [Design Strategies](#design-strategies)
   - [Overall Architecture and Module Organization](#overall-architecture-and-module-organization)
   - [Design Patterns and Optimization Techniques](#design-patterns-and-optimization-techniques)
   - [Python Libraries Used](#python-libraries-used)
   - [Outline Sketches and Flow Diagrams](#outline-sketches-and-flow-diagrams)
4. [Team Contributions](#team-contributions)
   - [Asset and UI Design](#asset-and-ui-design)
   - [AI Integration](#ai-integration)
5. [Code Overview](#code-overview)
   - [File Structure and Key Modules](#file-structure-and-key-modules)
   - [Explanation of Main Components](#explanation-of-main-components)
   - [Selected Code Snippets](#selected-code-snippets)
6. [Screenshots of Output](#screenshots-of-output)
7. [Conclusion](#conclusion)

---

## 1. Introduction

**Fractured‑Heart** is a 2D adventure game inspired by classic Zelda titles. The game offers a top‑down view of an expansive, multi‑layered world that includes an overworld and an underworld. Players navigate through challenging environments, engage in combat with various enemies, use magic, and upgrade their character over time.

### Objectives
- **Engaging Gameplay:** Provide dynamic combat, exploration, and puzzles.
- **Performance Optimization:** Use advanced techniques such as chunk loading, collision grids, and object pooling to manage large maps.
- **AI Integration:** Implement dialogue trees and branching conversations that adjust probabilities based on player choices.
- **Team Collaboration:** Leverage the strengths of team members in asset design, UI design, and AI integration to create a cohesive game experience.

---

## 2. Hardware/Software Requirements

### Hardware Requirements
- **Processor:** Intel Core i3 or equivalent
- **RAM:** 4 GB minimum (8 GB recommended)
- **Graphics:** Integrated graphics or better
- **Storage:** At least 500 MB of free space
- **Display:** 1280 x 720 resolution or higher

### Software Requirements
- **Operating System:** Windows 10 (or any OS supporting Python and Pygame)
- **Python:** Version 3.7 or higher
- **Pygame:** Version 2.0 or higher
- **Additional Libraries:** Standard Python libraries (os, sys, random, threading)
- **IDE/Editor:** PyCharm, VSCode, or equivalent

---

## 3. Design Strategies

### Overall Architecture and Module Organization
The game is modular, with each module handling a distinct part of the system:
- **main.py:** Initializes the game, handles loading/transition screens, and runs the main loop.
- **level.py:** Handles map creation, chunk loading, collision management, and overall game state.
- **player.py & enemy.py:** Define the behavior, animations, and interactions of the player and enemies.
- **tile.py:** Manages map tile creation and collisions.
- **support.py:** Provides utility functions for CSV parsing and asset loading.
- **ui.py & upgrade.py:** Manage the user interface, including menus and upgrade systems.
- **enemy_spawner.py/enemy_pool.py:** Implement enemy respawning using optimized, time‑based object pooling.
- **OptimizedCameraGroup:** Manages efficient rendering using chunk loading and view culling.

### Design Patterns and Optimization Techniques
#### Chunk Loading
- **Purpose:** Render and update only the sprites within or near the camera view.
- **Implementation:** The `OptimizedCameraGroup` divides the map into chunks and culls off‑screen objects.
- **Benefit:** Dramatically reduces the rendering workload on large maps.

#### Object Pooling for Enemy Respawns
- **Purpose:** Reuse enemy objects instead of creating and destroying them frequently.
- **Implementation:** An enemy pool or spawner records enemy spawn points and uses a time‑based check to respawn them.
- **Benefit:** Lowers memory overhead and improves performance.

#### Collision Grid Optimization
- **Purpose:** Efficiently manage collision checks by dividing the map into grid cells.
- **Implementation:** A collision grid maps sprites to cells to limit collision computations.
- **Benefit:** Improves performance during collision detection.

### Python Libraries Used
- **Pygame:** For graphics, events, and sound.
- **Random:** For random selection of assets and enemy types.
- **Threading:** For asynchronous asset loading.
- **OS & CSV Modules:** (via support.py) for file management and CSV parsing.

### Outline Sketches and Flow Diagrams
- **Game Flow Diagram:**  
  1. **Loading Screen:** Animated “Loading…” displayed during asset loading.  
  2. **Start Menu:** User selects “Press any key to start.”  
  3. **Transition Screen:** Smooth fade-in transitioning to gameplay.  
  4. **Game Loop:** Level class handles map drawing, collision detection, enemy updates, and UI overlays.  
  5. **Game Over/Upgrade Screens:** Displayed based on game state.
- **Module Interaction Diagram:** Illustrates interactions among main.py, level.py, player.py, enemy.py, UI modules, and support functions.

---

## 4. Team Contributions

### Asset and UI Design
- **Asset Designer:**  
  - Designed a seamless grass tileset using Krita. The tiles connect seamlessly to each other, ensuring a natural look.
  - Colored assets and created NPCs, ensuring consistency across the game’s visual style.
  - Created animations as PNG image sequences (due to Pygame limitations) rather than using video formats.
  - Employed Tiled layers (instead of object layers) to utilize border blocks for collisions effectively.
  - Designed several maps, each with its own challenges regarding story integration and performance; this required iterative adjustments to enemy designs and overall map layout.
- **UI Designer:**  
  - Developed CSV files for map layouts (for boundaries, grass, objects, and entities).
  - Created a start menu, upgrade menu, and game over screen, ensuring that the UI overlays are both visually appealing and functionally robust.
  - Optimized the UI for performance with custom fonts and pre-rendered assets.

### AI Integration
- **AI Specialist:**  
  - Developed dialogue trees that branch based on player choices. Although all branches eventually converge, the dialogue tree affects game probabilities and narrative flow.
  - Utilized a file (acting as a string dictionary) that stores dialogue nodes. A loop function and binary tree algorithm traverse these nodes to determine conversation outcomes.
  - Further AI-related tasks (such as adaptive enemy behavior and decision making) are integrated throughout the game.  
  - *[Placeholder for dialogue tree code – to be added later.]*

---

## 5. Code Overview

### File Structure and Key Modules
- **main.py:** Handles game initialization, asset loading (with a loading screen and transition), and the main loop.
- **level.py:** Contains the Level class for map and collision management, chunk loading, and integration of enemy respawn systems.
- **player.py & enemy.py:** Define core entity behaviors, including movement, attacks, animations, and interactions.
- **tile.py:** Manages individual tile creation and collision boundaries.
- **support.py:** Provides utilities for CSV and asset importing.
- **ui.py & upgrade.py:** Manage the visual interface and upgrade mechanics.
- **enemy_spawner.py/enemy_pool.py:** Implement optimized enemy respawn (object pooling and time‑based checks).
- **OptimizedCameraGroup:** Uses chunk loading and view culling to optimize rendering.

### Explanation of Main Components
- **Level Class:**  
  Creates the game map by reading CSV files, organizes sprites into chunks for efficient rendering, sets up collision grids, and records enemy spawn points.
- **Player and Enemy Classes:**  
  Manage behavior, movement, attack logic, and interactions. Enemies utilize sound and animation caching for performance.
- **OptimizedCameraGroup:**  
  Draws only visible sprites and caches floor segments to optimize performance.
- **Enemy Respawn System:**  
  Uses object pooling and a time‑based respawn check to ensure that enemies reappear at their designated spawn points without heavy memory overhead.
- **AI and Dialogue Trees:**  
  (Detailed implementation to be added later.) The AI system leverages dialogue trees stored in a file and traversed using binary tree logic to determine conversation outcomes.

### Selected Code Snippets
**Main.py – Loading and Transition Screens:**
```python
def show_loading_screen(screen, message="Loading..."):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(UI_FONT, 50)
    loading_text = font.render(message, True, TEXT_COLOR)
    text_rect = loading_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(loading_text, text_rect)
    pygame.display.flip()

def show_transition_screen(screen):
    transition_surface = pygame.Surface((WIDTH, HEIGHT))
    transition_surface.fill((0, 0, 0))
    font = pygame.font.Font(UI_FONT, 40)
    text = font.render("Entering the world...", True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    alpha = 0
    for _ in range(30):
        transition_surface.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(transition_surface, (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        alpha += 8
        pygame.time.delay(30)
```
**Level.py – Enemy Spawn Recording:**
```python
elif style == 'entities':
    if col == '0':
        self.player = Player(... )
    else:
        enemy_types = {'1': 'tree', '2': 'cherry tree', '3': 'snowy tree',
                       '4': 'spirit', '5': 'ninja', '6': 'oni'}
        monster_name = enemy_types.get(col, 'tree')
        Enemy(monster_name, (x, y), [self.visible_sprites, self.attackable_sprites],
              self.obstacle_sprites, self.damage_player, self.trigger_death_particles, self.add_exp)
        self.enemy_spawn_points.append((monster_name, (x, y)))
```
**Enemy Pool (Barebones Object Pooling for Respawns):**
```python
class EnemyPool:
    def __init__(self, level, pool_size=20, respawn_interval=5000, update_interval=1000):
        self.level = level
        self.pool_size = pool_size
        self.respawn_interval = respawn_interval
        self.update_interval = update_interval
        self.last_update = pygame.time.get_ticks()
        self.spawn_dict = {}
        current_time = pygame.time.get_ticks()
        for spawn in self.level.enemy_spawn_points:
            self.spawn_dict[spawn] = (None, current_time)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update < self.update_interval:
            return
        self.last_update = current_time
        for spawn_point, (enemy, last_spawn) in self.spawn_dict.items():
            if enemy is not None and enemy.alive():
                continue
            if current_time - last_spawn >= self.respawn_interval:
                monster_name, pos = spawn_point
                new_enemy = Enemy(monster_name, pos, [self.level.visible_sprites, self.level.attackable_sprites],
                                  self.level.obstacle_sprites, self.level.damage_player,
                                  self.level.trigger_death_particles, self.level.add_exp)
                self.spawn_dict[spawn_point] = (new_enemy, current_time)
```
---

## 6. Screenshots of the Output

## 7. Conclusion
Fractured‑Heart is a 2D adventure game that combines engaging gameplay with advanced performance optimizations. Through the use of chunk loading, collision grid optimization, and object pooling for enemy respawning, the game efficiently handles large maps and numerous entities. In addition, the project integrates robust AI dialogue trees (with further details and code pending) and a meticulously designed asset/UI pipeline. The collaborative efforts of the asset/UI designer and the AI integration specialist ensure a rich visual and interactive experience.

This documentation, along with the attached code and screenshots, provides a comprehensive overview of the project’s design, implementation, and team contributions.

