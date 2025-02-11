# game setup
WIDTH = 1280
HEIGTH = 720
TILE_SIZE = 64
HITBOX_OFFSET = {
    'player' : -39 ,
    'object' : -40 ,
    'grass' : -10 ,
    'invisible' : 0 }

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons 
weapon_data = {
    'katana' : { 'cooldown' : 100 , 'damage' : 15 , 'graphic' : '../graphics/weapons/katana/full.png' } }

# enemy
monster_data = {
    'squid' : { 'health' : 100 , 'damage' : 20 , 'attack_type' : 'slash' ,
                'attack_sound' : '../audio/attack/slash.wav' , 'speed' : 3 , 'resistance' : 3 , 'attack_radius' : 80 ,
                'notice_radius' : 360 } ,
    'raccoon' : { 'health' : 300 , 'damage' : 40 , 'attack_type' : 'claw' ,
                  'attack_sound' : '../audio/attack/claw.wav' , 'speed' : 2 , 'resistance' : 3 , 'attack_radius' : 120 ,
                  'notice_radius' : 400 } ,
    'spirit' : { 'health' : 100 , 'damage' : 8 , 'attack_type' : 'thunder' ,
                 'attack_sound' : '../audio/attack/fireball.wav' , 'speed' : 4 , 'resistance' : 3 ,
                 'attack_radius' : 60 , 'notice_radius' : 350 } ,
    'bamboo' : { 'health' : 70 , 'damage' : 6 , 'attack_type' : 'leaf_attack' ,
                 'attack_sound' : '../audio/attack/slash.wav' , 'speed' : 3 , 'resistance' : 3 , 'attack_radius' : 50 ,
                 'notice_radius' : 300 } }
