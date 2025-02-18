import pygame
from support import import_folder
from random import choice
from settings import TILESIZE  # Ensure TILESIZE is imported


class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic animations
            'heal': import_folder('../assets/images/video assets/graphics/particles/heal/frames'),
            'flame': import_folder('../assets/images/video assets/graphics/particles/flame/frames'),
            'aura': import_folder('../assets/images/video assets/graphics/particles/aura'),

            # attack animations
            'claw': import_folder('../assets/images/video assets/graphics/particles/claw'),
            'slash': import_folder('../assets/images/video assets/graphics/particles/slash'),
            'sparkle': import_folder('../assets/images/video assets/graphics/particles/sparkle'),
            'leaf_attack': import_folder('../assets/images/video assets/graphics/particles/leaf_attack'),
            'thunder': import_folder('../assets/images/video assets/graphics/particles/thunder'),

            # monster death animations
            'tree': import_folder('../assets/images/enemies/tree/death'),
            'cherry tree': import_folder('../assets/images/enemies/cherry tree/death'),
            'snowy tree': import_folder('../assets/images/enemies/snowy tree/death'),
            'oni': import_folder('../assets/images/enemies/oni/death'),
            'spirit': import_folder('../assets/images/enemies/spirit/death'),
            'ninja': import_folder('../assets/images/enemies/ninja/death'),

            'smash': import_folder('../assets/images/enemies/oni/attack/1.png'),

            # leaf particles
            'leaf': (
                import_folder('../assets/images/video assets/graphics/particles/leaf1'),
                import_folder('../assets/images/video assets/graphics/particles/leaf2'),
                import_folder('../assets/images/video assets/graphics/particles/leaf3'),
                import_folder('../assets/images/video assets/graphics/particles/leaf4'),
                import_folder('../assets/images/video assets/graphics/particles/leaf5'),
                import_folder('../assets/images/video assets/graphics/particles/leaf6'),
                self.reflect_images(import_folder('../assets/images/video assets/graphics/particles/leaf1')),
                self.reflect_images(import_folder('../assets/images/video assets/graphics/particles/leaf2')),
                self.reflect_images(import_folder('../assets/images/video assets/graphics/particles/leaf3')),
                self.reflect_images(import_folder('../assets/images/video assets/graphics/particles/leaf4')),
                self.reflect_images(import_folder('../assets/images/video assets/graphics/particles/leaf5')),
                self.reflect_images(import_folder('../assets/images/video assets/graphics/particles/leaf6'))
            )
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        # Fallback mechanism: if animation_type not found, use "sparkle" as default
        if animation_type not in self.frames:
            print(f"Warning: Animation type '{animation_type}' not found. Falling back to 'sparkle'.")
            animation_frames = self.frames.get("sparkle", [])
        else:
            animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        # Ensure that we have at least one frame; otherwise, create a placeholder.
        if not animation_frames or len(animation_frames) == 0:
            placeholder = pygame.Surface((TILESIZE, TILESIZE))
            placeholder.fill((255, 0, 255))
            self.frames = [placeholder]
        else:
            self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
