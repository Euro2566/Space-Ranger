import  pygame
import  random
import  os
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SpaceRanger")

SpaceRangerFont = pygame.font.Font("Font\Font1SpaceRanger.ttf",25)
Background = pygame.image.load("background\SpaceBackground.png")
BackgroundF2 = pygame.image.load("background\SpaceBackgroundF2.png")
BlackgroundSound = pygame.mixer.music.load("SoundEffec\JuhaniJunkala[RetroGameMusicPack]TitleScreen.ogg")

# ส่วนของStartMenu
BlackgroundMenu = pygame.image.load("StartUImenu\BlackgroundStart.png")
ButtonStartImg = pygame.transform.scale(pygame.image.load("StartUImenu\Start_BTN.png"), (150, 50))
ButtonExitImg = pygame.transform.scale(pygame.image.load("StartUImenu\Exit_BTN.png"), (150, 50))
ButtonCraditImg = pygame.transform.scale(pygame.image.load("StartUImenu\Info_BTN.png"),(50,50))
SoundClick = pygame.mixer.Sound("SoundEffec\Click_02.wav")


#ส่วนของผู้เล่น
UserSpaceMachine = pygame.image.load("UserImg\SpaceMachine.png")
Bullet = pygame.image.load("Bullet\LaserBlue.png")
F1 = pygame.image.load("UserImg\Flame_01.png")
F2 = pygame.image.load("UserImg\Flame_02.png")
HPtableUser = pygame.image.load("UserImg\Health_Bar_Table.png")
UserHPbar = pygame.image.load("UserImg\HPbar.png")
UserSoundShot = pygame.mixer.Sound("SoundEffec\SoundShotUser.ogg")

JetEngine = (pygame.transform.scale(F1,(120,160)),pygame.transform.scale(F2,(120,160)))
Bullet1 = pygame.transform.scale(Bullet,(50,75))
UserSpaceMachine1 = pygame.transform.scale(UserSpaceMachine,(50,75))
Background1 = pygame.transform.scale(Background,(800,600))
BackgroundF2_1 = pygame.transform.scale(BackgroundF2,(800,600))
HPtableUser1 = pygame.transform.scale(HPtableUser,(200,30))
UserHPbar1 = pygame.transform.scale(UserHPbar, (165, 25))

#ส่วนของลูกกระจ๊อก
EnermyImg = pygame.transform.scale(pygame.image.load("Enermy\Enermy.png"),(50,75))
EnermyBulletImg = pygame.transform.scale(pygame.image.load("Bullet\EnermyLaser.png"),(50,75))
EnermyShotSound = pygame.mixer.Sound("SoundEffec\SoundShotEnermy.ogg")


#ส่วนของบอส
BulletBoss = pygame.image.load("Bullet\LaserRed.png")
Boss = pygame.image.load("BossImg\BigBossV1.png")
Boss2 = pygame.image.load("BossImg\BigBossV2.png")
Boss3 = pygame.image.load("BossImg\BigBossV3.png")
Boss4 = pygame.image.load("BossImg\BigBossV4.png")
Boss5 = pygame.image.load("BossImg\BigBossV5.png")
BossLisImg = (pygame.transform.scale(Boss,(200,160)),pygame.transform.scale(Boss2,(200,160))
              ,pygame.transform.scale(Boss3,(200,160)),pygame.transform.scale(Boss4,(200,160))
              ,pygame.transform.scale(Boss5,(200,160)))
BulletBoss1 = pygame.transform.scale(BulletBoss,(50,75))
JetEngineBoss = (pygame.transform.scale(pygame.image.load("BossImg\FlameBoss_F1.png"),(120,160)),
                 pygame.transform.scale(pygame.image.load("BossImg\FlameBoss_F2.png"),(120,160)))
BossShotSound = pygame.mixer.Sound("SoundEffec\SoundShotBoss.ogg")

pygame.mixer.music.play(-1)

class Button():
    def __init__(self,position_x,position_y,img,scale):
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img,(int(width * scale),int(height * scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (position_x ,position_y)
        self.clicked = False
    def ButtonDraw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.img, (self.rect.x,self.rect.y))
        return action

class SpaceShip():
    def __init__(self,img,position_x,position_y,HP):
        self.img = img
        self.position_x = position_x
        self.position_y = position_y
        self.HP = HP
    def Move(self,Screen):
        Screen.blit(self.img,(self.position_x,self.position_y))
        #pygame.draw.rect(Screen, (255, 0, 0), (self.position_x - 5, self.position_y + 3, 60, 100), 2)

class SpaceShipEnermy():
    def __init__(self,img,position_x,position_y,HP):
        self.img = img
        self.position_x = position_x
        self.position_y = position_y
        self.position_x_Limit = self.position_x + 80
        self.TurnLeft = True
        self.TurnRight = False
        self.HP = HP
        self.HPmax = HP
        self.Flame = 0
    def MoveMent(self,Screen,Mode):
        if Mode == 1:
            if len(self.img) > 0:
                 Screen.blit(self.img[self.Flame],(self.position_x,self.position_y))
            else:
                 Screen.blit(self.img, (self.position_x, self.position_y))
        elif Mode == 2:
            if self.TurnLeft == True:
                self.position_x += 1
                if self.position_x > self.position_x_Limit:
                    self.TurnLeft = False
                    self.TurnRight = True
            elif self.TurnRight == True:
                self.position_x -= 1
                if self.position_x < self.position_x_Limit - 80:
                    self.TurnLeft = True
                    self.TurnRight = False
            Screen.blit(self.img, (self.position_x, self.position_y))
        elif Mode == 3:
            if self.TurnLeft == True:
                self.position_y += 1
                self.position_x += 1
                if self.position_x > self.position_x_Limit:
                    self.TurnLeft = False
                    self.TurnRight = True
            elif self.TurnRight == True:
                self.position_y -= 1
                self.position_x -= 1
                if self.position_x < self.position_x_Limit - 80:
                    self.TurnLeft = True
                    self.TurnRight = False
            Screen.blit(self.img, (self.position_x, self.position_y))
        elif Mode == 4:
            if self.TurnLeft == True:
                self.position_y -= 1
                self.position_x += 1
                if self.position_x > self.position_x_Limit:
                    self.TurnLeft = False
                    self.TurnRight = True
            elif self.TurnRight == True:
                self.position_y += 1
                self.position_x -= 1
                if self.position_x < self.position_x_Limit - 80:
                    self.TurnLeft = True
                    self.TurnRight = False
            Screen.blit(self.img, (self.position_x, self.position_y))
        #pygame.draw.rect(Screen, (255, 0, 0), (self.position_x +2, self.position_y + 3, 190, 145), 2)

class FireBullet():
    def __init__(self,img,position_x,position_y,Damage):
        self.img = img
        self.Damage = Damage
        self.position_x = position_x
        self.position_y = position_y
    def FireShoot(self,Screen):
        Screen.blit(self.img,(self.position_x,self.position_y))
        #pygame.draw.rect(Screen,(255,255,255),(self.position_x + 10 ,self.position_y + 10 ,30,60),2)

def ExamineQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def playing():
    # ส่วนตัวแปรผู้เล่น
    UserPlay = SpaceShip(UserSpaceMachine1, 360, 460, 100)
    FPS = 60
    clock = pygame.time.Clock()
    BulletLis = []
    Delay = 0
    DelayFlame = 0
    Flame = 0
    PositionBg_y = 0
    HPcalUser = 0
    ScoreUser = 0
    HightScore = 0
    TextScore = 'Score :'
    Damage = 2
    ScoreUserMultiply = 1

    # ส่วนตัวแปรลูกกระจ๊อก
    EnermyLis = []
    EnermyPosition = (50, 150, 250, 350, 450)
    EnermySpawn = True
    EnermyGen = True
    EnermyHave = 0
    Action = 2
    PositionYspwan = 80
    EnermyBulletLis = []
    DelayEnermyBullet = 0

    # ส่วนตัวแปรบอส
    BulletBossLis = []
    BossImgFlame = 3
    BossPosition_X = 275
    BossPosition_Y = 15
    DelayTimeBulletBoss = 0
    DamageBulletBoss = 2
    DelayJetEngineBoss = 0
    FlameEngineBoss = 0
    SpeedBoss = 1
    SpeedShotBoss = 80
    PositionBulletLis = (13, 27, 40, 109, 124, 137)
    RndPosition_yBossLis = (0, 20, 30, 40, 45, -10, -20, -25, -30)
    JetEngineBossPosition_X_lis = (0, 10, 40, 72, 82)
    BufferDelayBulletBoss = 0
    RndBossPosition_y = 0
    TimeSpawn = 0
    SpawnBoss = False
    StatusTurnLeft = True
    StatusTurnRight = False
    BossSpaceShip = SpaceShipEnermy(BossLisImg, BossPosition_X, BossPosition_Y, 1000)

    if os.path.exists('ScoreUser.txt'):
        with open('ScoreUser.txt', 'r') as file:
            HightScore = int(file.read())



    while True:

        ExamineQuit()
        TextScore = "Score : " + str(ScoreUser)
        HPcalUser = (UserPlay.HP/100)*165
        UserHPbar1 = pygame.transform.scale(UserHPbar, (HPcalUser, 25))
        ShowScore = SpaceRangerFont.render(TextScore , True, (255,255,255))

        #ส่วนควบคุมตัวละคร
        if UserPlay.HP == 0:
            if ScoreUser > HightScore:
                HightScore = ScoreUser
                with open('ScoreUser.txt','w')as file:
                    file.write(str(HightScore))
            break

        Key = pygame.key.get_pressed()
        if Key[pygame.K_UP] and UserPlay.position_y >= 10:
            UserPlay.position_y -= 6
        if Key[pygame.K_DOWN] and UserPlay.position_y <= 460:
            UserPlay.position_y += 6
        if Key[pygame.K_LEFT] and UserPlay.position_x >= 10:
            UserPlay.position_x -= 6
        if Key[pygame.K_RIGHT] and UserPlay.position_x <= 740:
            UserPlay.position_x += 6
        if Key[pygame.K_SPACE]:
            Delay += 1
            if Delay == 10:
                UserSoundShot.play()
                BulletLis.append(FireBullet(Bullet1,UserPlay.position_x , UserPlay.position_y - 31,Damage))
                Delay = 0

        #การเคลื่อนที่ของภาพพื้นหลัง
        if UserPlay.position_y < 430:
            PositionBg_y += 3
        elif UserPlay.position_y > 460:
            PositionBg_y -= 3

        if PositionBg_y < -600:
            PositionBg_y = 600
        elif PositionBg_y > 600:
            PositionBg_y = -600

        screen.blit(BackgroundF2_1, (0, PositionBg_y - 600))
        screen.blit(Background1,(0,PositionBg_y))
        screen.blit(BackgroundF2_1,(0, PositionBg_y + 600))
        UserPlay.Move(screen)

        if DelayFlame == 10:
            Flame += 1
        elif DelayFlame == 16:
            Flame = 0
            DelayFlame = 0

        screen.blit(JetEngine[Flame],(UserPlay.position_x - 35 ,UserPlay.position_y + 9))
        DelayFlame += 1


        #ส่วนการทำงานของ Enermy
        if EnermySpawn:
            if EnermyGen:
                for Enermy in EnermyPosition:
                    EnermyLis.append(SpaceShipEnermy(EnermyImg,Enermy + 60 , PositionYspwan , 20))
                EnermyGen = False

            for EnermyMove in EnermyLis:
                EnermyMove.MoveMent(screen,Action)

            DelayEnermyBullet += 1
            if DelayEnermyBullet == 150:
                EnermyShotSound.play()
                for PositionBullet in EnermyLis:
                    EnermyBulletLis.append(FireBullet(EnermyBulletImg,PositionBullet.position_x + 5
                                                      ,PositionBullet.position_y + 20,5))
                DelayEnermyBullet = 0

            for BullEn in EnermyBulletLis:
                if BullEn.position_y >= UserPlay.position_y - 77 and BullEn.position_y <= UserPlay.position_y + 27 and \
                        BullEn.position_x >= UserPlay.position_x - 30 and BullEn.position_x <= UserPlay.position_x + 35:
                    EnermyBulletLis.pop(EnermyBulletLis.index(BullEn))
                    if UserPlay.HP != 0:
                        UserPlay.HP -= (BullEn.Damage + DamageBulletBoss)
                        if UserPlay.HP < 0:
                            UserPlay.HP = 0
                else:
                    if BullEn.position_y < 500:
                        BullEn.position_y += 4
                    else:
                        EnermyBulletLis.pop(EnermyBulletLis.index(BullEn))

            for BulInScreen in EnermyBulletLis:
                BulInScreen.FireShoot(screen)

            if len(EnermyLis) == 0:
                EnermyGen = True
                ActionRnd = random.randint(2,4)
                Action = ActionRnd
                if Action == 4:
                    PositionYspwan = 160
                else:
                    PositionYspwan = 80
                EnermyHave += 5
                if EnermyHave == 20:
                    EnermySpawn = False
                    EnermyHave = 0

        # ส่วนของกระสุนผู้เล่น
        for Bull in BulletLis:
            if EnermySpawn:
                if Bull.position_y > 0:
                    Bull.position_y -= 6
                else:
                    BulletLis.pop(BulletLis.index(Bull))
                for EnermyHit in EnermyLis:
                    if EnermyHit.HP != 0:
                        if Bull.position_y <= EnermyHit.position_y + 40 and \
                            Bull.position_x >= EnermyHit.position_x - 20 and Bull.position_x <= EnermyHit.position_x + 20:
                            try:
                                BulletLis.pop(BulletLis.index(Bull))
                            except:
                                pass
                            ScoreUser += 20
                            EnermyHit.HP -= 5
                            if EnermyHit.HP <= 0:
                                EnermyLis.pop(EnermyLis.index(EnermyHit))

            if SpawnBoss == True:
                if BossSpaceShip.HP != 0:
                    if Bull.position_y <= BossSpaceShip.position_y + 77 and \
                        Bull.position_x >= BossSpaceShip.position_x - 18 and Bull.position_x <= BossSpaceShip.position_x + 170:
                        BulletLis.pop(BulletLis.index(Bull))
                        ScoreUser += (60 * ScoreUserMultiply)
                        BossSpaceShip.HP -= 10
                    else:
                        if Bull.position_y > 0:
                            Bull.position_y -= 6
                        else:
                            BulletLis.pop(BulletLis.index(Bull))
                else:
                    if Bull.position_y > 0:
                        Bull.position_y -= 6
                    else:
                        BulletLis.pop(BulletLis.index(Bull))

            if EnermySpawn == False and SpawnBoss == False:
                if Bull.position_y > 0:
                    Bull.position_y -= 6
                else:
                    BulletLis.pop(BulletLis.index(Bull))

        for Bul in BulletLis:
            Bul.FireShoot(screen)

        # ส่วนการทำงานของ Boss
        if TimeSpawn == 120 and SpawnBoss == False:
            BossSpaceShip.HP = 1000
            DamageBulletBoss = 2
            ScoreUserMultiply = 1
            SpeedBoss = 1
            SpeedShotBoss = 80
            DelayTimeBulletBoss = 0
            BulletBossLis.clear()
            BossSpaceShip.position_x = BossPosition_X
            BossSpaceShip.position_y = BossPosition_Y
            BossSpaceShip.Flame = 0
            SpawnBoss = True
            TimeSpawn = 0
        elif SpawnBoss == False and EnermySpawn == False:
            TimeSpawn += 1

        if SpawnBoss :
            DelayTimeBulletBoss += 1
            HPtoPersen = (BossSpaceShip.HP / BossSpaceShip.HPmax) * 100

            if BossSpaceShip.HP < 0.0:
                BossSpaceShip.HP = 0
                DamageBulletBoss = 0
            if str(HPtoPersen) == "80.0":
                BossSpaceShip.Flame = 1
                DamageBulletBoss = 2
                ScoreUserMultiply = 2
                SpeedBoss = 2
                SpeedShotBoss = 75
                DelayTimeBulletBoss = 5
            elif str(HPtoPersen) == "60.0":
                BossSpaceShip.Flame = 2
                DamageBulletBoss = 4
                ScoreUserMultiply = 4
                SpeedBoss = 3
                SpeedShotBoss = 70
                DelayTimeBulletBoss = 5
            elif str(HPtoPersen) == "40.0":
                BossSpaceShip.Flame = 3
                DamageBulletBoss = 6
                ScoreUserMultiply = 6
                SpeedBoss = 5
                SpeedShotBoss = 65
                DelayTimeBulletBoss = 5
            elif str(HPtoPersen) == "20.0":
                BossSpaceShip.Flame = 4
            elif str(HPtoPersen) == "0.0":
                SpawnBoss = False
                EnermySpawn = True

            if StatusTurnLeft :
                BossSpaceShip.position_x -=  SpeedBoss
                if BossSpaceShip.position_x <= 30:
                    StatusTurnLeft = False
                    StatusTurnRight = True
            if StatusTurnRight :
                BossSpaceShip.position_x +=  SpeedBoss
                if BossSpaceShip.position_x >= 550:
                    StatusTurnLeft = True
                    StatusTurnRight = False

            if DelayTimeBulletBoss == SpeedShotBoss:
                if BossSpaceShip.position_y >= 0 and BossSpaceShip.position_y <= 170:
                    RndBossPosition_y = random.choice(RndPosition_yBossLis)
                    BossSpaceShip.position_y += RndBossPosition_y
                    if BossSpaceShip.position_y < 0:
                        BossSpaceShip.position_y = 20
                    if BossSpaceShip.position_y >= 170:
                        BossSpaceShip.position_y = 170

                for PositionBullet in PositionBulletLis:
                    BossShotSound.play()
                    BulletBossLis.append(
                        FireBullet(BulletBoss1, BossSpaceShip.position_x + PositionBullet,
                                   BossSpaceShip.position_y + 85, Damage))

                DelayTimeBulletBoss = 0

            for Bull in BulletBossLis:
                if Bull.position_y >= UserPlay.position_y - 77  and  Bull.position_y <= UserPlay.position_y + 27 and\
                    Bull.position_x >= UserPlay.position_x - 30 and Bull.position_x <= UserPlay.position_x + 35:
                    BulletBossLis.pop(BulletBossLis.index(Bull))
                    if UserPlay.HP != 0:
                        UserPlay.HP -= (Bull.Damage + DamageBulletBoss)
                        if UserPlay.HP < 0:
                            UserPlay.HP = 0
                else:
                    if Bull.position_y < 500:
                        Bull.position_y += 6
                    else:
                        BulletBossLis.pop(BulletBossLis.index(Bull))

            for Bul in BulletBossLis:
                Bul.FireShoot(screen)

            if DelayJetEngineBoss == 10:
                FlameEngineBoss += 1
            elif DelayJetEngineBoss == 16:
                FlameEngineBoss = 0
                DelayJetEngineBoss = 0

            for JetEngineBossPosition_X in JetEngineBossPosition_X_lis:
                screen.blit(JetEngineBoss[FlameEngineBoss], (BossSpaceShip.position_x + JetEngineBossPosition_X
                                                             , BossSpaceShip.position_y - 65))
            DelayJetEngineBoss += 1
            BossSpaceShip.MoveMent(screen,1)


        #ส่วนแสดงพลังและคะแนนของตัวละคร
        screen.blit(HPtableUser1, (550, 550))
        screen.blit(UserHPbar1,(553,553))
        screen.blit(ShowScore,(10,553))
        pygame.display.update()
        clock.tick(FPS)


ButtonStart = Button(220,400,ButtonStartImg,1)
ButtonExit = Button(400,400,ButtonExitImg,1)
FPS = 60
clock = pygame.time.Clock()

while True:
    if os.path.exists('ScoreUser.txt'):
        with open('ScoreUser.txt', 'r') as file:
            HightScoreUser = int(file.read())
    else:
        HightScoreUser = 0

    Score = str(HightScoreUser)
    ScoreHight = SpaceRangerFont.render("HIGHT SCORE",True,(255,255,255))
    ShowScore = SpaceRangerFont.render(Score, True, (255, 255, 255))
    No = SpaceRangerFont.render("64015125",True,(255,255,255))
    Name = SpaceRangerFont.render("WATANYU WASUSIRIKUL", True, (255, 255, 255))

    screen.blit(BlackgroundMenu, (0, 0))
    screen.blit(ScoreHight,(270,240))
    screen.blit(No, (30, 550))
    screen.blit(Name, (220, 550))

    if len(Score) == 1:
        screen.blit(ShowScore, (360, 300))
    elif len(Score) == 2 or len(Score) == 3:
        screen.blit(ShowScore, (350, 300))
    elif len(Score) == 4:
        screen.blit(ShowScore, (333, 300))
    elif len(Score) == 5:
        screen.blit(ShowScore, (320, 300))
    elif len(Score) == 6:
        screen.blit(ShowScore, (310, 300))
    elif len(Score) == 7:
        screen.blit(ShowScore, (305, 300))
    elif len(Score) == 8:
        screen.blit(ShowScore, (295, 300))
    elif len(Score) == 9:
        screen.blit(ShowScore, (285, 300))

    ExamineQuit()

    if ButtonStart.ButtonDraw(screen):
        SoundClick.play()
        playing()
    if ButtonExit.ButtonDraw(screen):
        SoundClick.play()
        pygame.quit()

    pygame.display.update()
    clock.tick(FPS)
