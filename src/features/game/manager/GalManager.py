from src.entity.Gal import *
from src.entity.Player import *
from features.game.manager.BulletManager import *
import time
import random

class GalManager:
    galList = []
    galLoadTime = 0
    galStartTime = time.time()


    def manageGal(self):
        activeGalList = []
        for (idx, gal) in enumerate(GalManager.galList):
            if not isObjectInMap(gal):
                gal.isActive = False
            # 플레이어와 충돌
            if gal.objectRect.colliderect(pygame.Rect(Player.xPos, Player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT)):
                gal.isActive = False
                Player.playerHp -= 1
                print("PlayerHP : -%d" % (Player.playerHp))
        # 총알과 충돌
            for (bulletIdx, bullet) in enumerate(BulletManager.bulletList):
                if gal.objectRect.colliderect(bullet.objectRect):
                    gal.isActive = False
                    Player.playerXp += 1
                    print("playerXP : +%d" % Player.playerXp)
            gal.move()
            gal.yPos = gal.a * (gal.xPos - gal.s) ** 2 + gal.h
            if gal.isActive:
                activeGalList.append(gal)
                GalManager.galList = activeGalList
            if gal.yPos > SCREEN_HEIGHT:
                setGalQuadraticGraph(gal)
                gal.yPos = SCREEN_HEIGHT - 10
        self.galList = activeGalList

    def createGal(self):
        now = time.time()
        if now - GalManager.galStartTime >= GalManager.galLoadTime:
            GalManager.galLoadTime = random.uniform(GAL_CREATE_TIME_1, GAL_CREATE_TIME_2)
            GalManager.galStartTime = time.time()
            gal = Gal(0, SCREEN_HEIGHT)
            if random.randint(0, 1):
                gal.d = True
                gal.xPos = 0
                gal.xMove = GAL_SPEED
            else:
                gal.d = False
                gal.xPos = SCREEN_WIDTH - 50
                gal.xMove = -GAL_SPEED
            setGalQuadraticGraph(gal)

            # print(gal.a, gal.s, gal.h)
            GalManager.galList.append(gal)

def galInit():
    GalManager.galList.clear()
    GalManager.galLoadTime = 0
    GalManager.galStartTime = time.time()