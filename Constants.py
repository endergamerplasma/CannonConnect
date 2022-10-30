from pygame import font


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

COLOURS = [(209, 24, 49),
           (46, 118, 166),
           (255, 200, 0),
           (139, 0, 168)]

TILESIZE = 128
HORIZONTAL = 14
VERTICAL = 8

WIDTH = HORIZONTAL*TILESIZE
HEIGHT = VERTICAL*TILESIZE

TITLE = 'Cannon Connect'
FPS = 60

FONT_NAME = 'arial'
FONT = font.match_font(FONT_NAME)
FONT_MOON = 'Assets/Fonts/Moon Bold.otf'
FONT_MOON_LIGHT = 'Assets/Fonts/Moon Light.otf'

HIGHSCORES_FILE = 'highscores.csv'
MAP_FILE = 'Assets/map.tmx'

PROJECTILE_LAYER = 2

PROJECTILE_VELOCITY = 1200
PROJECTILE_INSERT_VEL = 800
PROJECTILE_OFFSET_RATIO = 0.7

SHOOT_DELAY = 500

ARC_SCALE = 1.05
CANNONBALL_DIM = 90

CANNONBALL_VEL = 2
MIN_CANNONBALL_VEL = 2
SHIFT_VELOCITY = 17
ACCELERATION = -60
REVERSE_VELOCITY = -14
LOSE_REVERSE_DURATION = 5000


VELOCITY_RAMPUP = 1  # per minute
DV = VELOCITY_RAMPUP/60
SLOW_TILE_DIST = 6
DECAY_TILE_DIST = 4

POWERUP_PROBABILITY = 0.001
POWERUP_DURATION = 3000
POWERUP_REVERSE_VELOCITY = -7
POWERUP_SLOW_VELOCITY = 1

COIN_PROBABILITY = 0.001
COIN_BONUS = 200

SLOW_DIST = SLOW_TILE_DIST*TILESIZE
DECAY_DIST = DECAY_TILE_DIST*TILESIZE

POINT_VELOCITY = 100
POINT_FADE = 255