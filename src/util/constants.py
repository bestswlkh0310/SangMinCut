from math import *

from circleRotate import normalized

DEFAULT_FRAME = 200

# init
# SCREEN_WIDTH = 1440
# SCREEN_HEIGHT = 960

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 960

PLAYER_XP_TEXT_WIDTH = 20

# Player
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
PLAYER_SPEED = 2
PLAYER_SPECIAL_BULLETS_CNT = 48
PLAYER_SPECIAL_BULLET_SHOOT_CNT = 3
PLAYER_INIT_HP = 10
PLAYER_INIT_MAX_XP = 200
PLAYER_INIT_XPOS = (SCREEN_WIDTH - PLAYER_WIDTH) / 2
PLAYER_INIT_YPOS = (SCREEN_HEIGHT - PLAYER_HEIGHT) / 2

x = [normalized(1, tan(i * (360 / PLAYER_SPECIAL_BULLETS_CNT))) for i in range(1, PLAYER_SPECIAL_BULLETS_CNT // 4)] # 궁 각도 계산
# print(x)
PLAYER_SPECIAL_BULLET_DEGREE = []
PLAYER_SPECIAL_BULLET_DEGREE.extend([(i[0], i[1]) for i in x])
PLAYER_SPECIAL_BULLET_DEGREE.extend([(i[0], -i[1]) for i in x])
PLAYER_SPECIAL_BULLET_DEGREE.extend([(-i[0], i[1]) for i in x])
PLAYER_SPECIAL_BULLET_DEGREE.extend([(-i[0], -i[1]) for i in x])
PLAYER_SPECIAL_BULLET_DEGREE.extend([(1, 0), (-1, 0), (0, 1), (0, -1)])
# print(PLAYER_SPECIAL_BULLET_DEGREE)

SANGMIN_WIDTH = 30
SANGMIN_HEIGHT = 30
SANGMIN_SPEED = 1
SANGMIN_CREATE_TIME_1 = 0.5
SANGMIN_CREATE_TIME_2 = 1

GAL_WIDTH = 70
GAL_HEIGHT = 70
GAL_SPEED = 3
GAL_CREATE_TIME_1 = 0.6
GAL_CREATE_TIME_2 = 1

HOJOON_WIDTH = 100
HOJOON_HEIGHT = 100
HOJOON_SPEED = 10
HOJOON_CREATE_TIME_1 = 1
HOJOON_CREATE_TIME_2 = 2

BULLET_WIDTH = 40
BULLET_HEIGHT = 40
BULLET_SPEED = 20

HP_POTION_WIDTH = 20
HP_POTION_HEIGHT = 40
HP_CREATE_TIME_1 = 1
HP_CREATE_TIME_2 = 2

XP_POTION_WIDTH = 60
XP_POTION_HEIGHT = 60
XP_CREATE_TIME_1 = 1
XP_CREATE_TIME_2 = 2

# stage
STAGES = [
    ("SM", "MK", "HP", "MP", "HJ"),
    (True, True, True, True, True),
    (True, False, False, False, False),
    (True, False, True, False, False),
    (False, True, False, True, True),
    (False, True, True, False, True),
    (False, True, False, True, False),
    (True, True, False, False, False),
    (True, True, False, False, True),
    (True, True, True, True, False),
    (True, True, False, False, True),
    (True, True, False, True, False),
    (True, True, True, True, True)
]
