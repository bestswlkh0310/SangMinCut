import pygame

from src.entity.Bullet import *
from src.manager.ClockManager import *
from src.view.SettingFragment import *
from src.manager.DrawManager import *
from src.manager.PlayerManager import *
from src.manager.DrawManager import *
from src.entity.Player import *
from src.manager.StageManager import *
from src.manager.HpPotionManager import *
from src.manager.XpPotionManager import *

# TODO: SOUND ON/OFF, CLOSE - 나가기, BACK - 뒤로가기
class GameActivity:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.data = data
            cls._init = True

    def createBullet(self):
        (xMousePos, yMousePos) = pygame.mouse.get_pos()
        (normalizedXPos, normalizedYPos) = Utils.normalized(Utils, Player.xPos + PLAYER_WIDTH / 2 - xMousePos,
                                                      Player.yPos + PLAYER_HEIGHT / 2 - yMousePos)
        bullet = Bullet(Player.xPos + PLAYER_WIDTH / 2, Player.yPos + PLAYER_HEIGHT / 2,
                        -normalizedXPos * BULLET_SPEED,
                        -normalizedYPos * BULLET_SPEED)
        BulletManager.bulletList.append(bullet)


    def onMouseClick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                self.createBullet(self)
                if DrawManager.settingButton.xPos <= xMousePos <= DrawManager.settingButton.xPos + DrawManager.settingButton.width and DrawManager.settingButton.yPos <= yMousePos <= DrawManager.settingButton.yPos + DrawManager.settingButton.height:
                    LifeManager.isPause = True
                    LifeManager.isSetting = True
                    settingFragment()

    def onKeyClick(self):
        deltaTime = pygame.time.Clock().tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if 0 <= Player.xPos - PLAYER_SPEED:
                Player.xPos -= PLAYER_SPEED * deltaTime
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if Player.xPos + PLAYER_SPEED <= SCREEN_WIDTH - PLAYER_WIDTH:
                Player.xPos += PLAYER_SPEED * deltaTime
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if 0 <= Player.yPos - PLAYER_SPEED:
                Player.yPos -= PLAYER_SPEED * deltaTime
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if Player.yPos + PLAYER_SPEED <= SCREEN_HEIGHT - PLAYER_HEIGHT:
                Player.yPos += PLAYER_SPEED * deltaTime
        if keys[pygame.K_SPACE]:
            self.createBullet(self)
        if keys[pygame.K_r]:
            # print("onClickRBTN", Player.isSpecial)
            if Player.isSpecial:
                if not Player.isSpecialing:
                    Player.beforeSpecialTime = time.time()
                    Player.isSpecialing = True
                    Player.playerMaxXp = int(Player.playerMaxXp * 1.2)
                    Player.playerXp = 0

    def startGame(self):
        while LifeManager.isPlaying:
            while not LifeManager.isPause:
                # event
                self.onKeyClick(self)
                self.onMouseClick(self)

                # manage
                BulletManager.manageBullet(BulletManager)

                if STAGES[StageManager.stage][0]:
                    SangMinManager.createSangMin(SangMinManager)
                if STAGES[StageManager.stage][1]:
                    GalManager.createGal(GalManager)
                if STAGES[StageManager.stage][2]:
                    HpPotionManager.createHpPotion(HpPotionManager)
                if STAGES[StageManager.stage][3]:
                    XpPotionManager.createXpPotion(XpPotionManager)

                HpPotionManager.manageHpPotion(HpPotionManager)
                PlayerManager.managePlayer(PlayerManager)
                GalManager.manageGal(GalManager)
                SangMinManager.manageSangMin(SangMinManager)
                StageManager.manageStage(StageManager)
                XpPotionManager.manageXpPotion(XpPotionManager)


                # draw
                DrawManager.drawGame(DrawManager)