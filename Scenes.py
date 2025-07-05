from Animatronics import Freddy, Bonny, Chica, Foxy, GoldenFreddy
from Variables import Vars
from random import randrange
from os import path, getenv, remove
from ImageManager import get_image, resource_path, remove_image, screenshot
from Sounds import get_sound
from Animations import PlayAnimation, ResetAnimation, AnimationIsOn, GetFrame
import Events
import pygame

class SceneBase:
    def __init__(self):
        self.next = self
        self.start_time = pygame.time.get_ticks()
        self.time = (pygame.time.get_ticks() - self.start_time) / 1000

    def ProcessInput(self, events, pressed_keys, display1, display2):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, display1, display2):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)



# The rest is code where you implement your game using the Scenes model



class WarningScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and Vars.Opacity[3] >= 255 and Vars.Opacity[11] <= 0:
                self.start_time = pygame.time.get_ticks() - 3500
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and Vars.Opacity[3] >= 255 and Vars.Opacity[11] <= 0:
                self.start_time = pygame.time.get_ticks() - 3500


    def Update(self):
        Vars.Frames += 1
        if self.time >= 0.5 and Vars.Opacity[3] <= 255:
            Vars.Opacity[3] += (255 / 1.01) * Vars.dTime
        if self.time > 3.5:
            Vars.Opacity[11] += (255 / 1.01) * Vars.dTime
        if Vars.Opacity[11] >= 255 + (255 / 1.01) * 0.5:
            if randrange(0,1000) == 1:
                self.SwitchToScene(CreepyStart())
            else:
                self.SwitchToScene(MainMenu())


    def Render(self, display1, display2):
        if path.isfile(resource_path("data/sprites/Screen/screenshot_1.png")):
            display2.blit(get_image('data/sprites/Screen/screenshot_2.png', 255), (0, 0))
        if path.isfile(resource_path("data/sprites/Screen/screenshot_2.png")):
            display1.blit(get_image('data/sprites/Screen/screenshot_1.png', 255), (0, 0))
        display1.blit(get_image('data/sprites/WarningText.png', Vars.Opacity[3]), (0, 0))
        display1.blit(get_image('data/sprites/Black.png', Vars.Opacity[11]), (0, 0))



class MainMenu(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not Vars.Extra:
                    if (174 <= Vars.CursorPosX <= 377) and (404 <= Vars.CursorPosY <= 437):
                        self.SwitchToScene(NewspaperScene())
                    elif (173 <= Vars.CursorPosX <= 377) and (476 <= Vars.CursorPosY <= 510):
                        self.SwitchToScene(LoadingScene())
                    elif (172 <= Vars.CursorPosX <= 399) and (549 <= Vars.CursorPosY <= 593) and Vars.BeatGame:
                        Vars.Night = 6
                        self.SwitchToScene(LoadingScene())
                    elif (171 <= Vars.CursorPosX <= 477) and (617 <= Vars.CursorPosY <= 661) and Vars.Beat6 :
                        Vars.Night = 7
                        self.SwitchToScene(Customize())
                    elif (1120 <= Vars.CursorPosX <= 1244) and (30 <= Vars.CursorPosY <= 63) and Vars.BeatGame:
                        get_sound(2).play(0)
                        Vars.Extra = True
                else:
                    if (1120 <= Vars.CursorPosX <= 1221) and (30 <= Vars.CursorPosY <= 64):
                        get_sound(2).play(0)
                        Vars.Extra = False
                    elif (174 <= Vars.CursorPosX <= 487) and (204 <= Vars.CursorPosY <= 239):
                        get_sound(2).play(0)
                        Vars.OptionNumber1 = 0
                    elif (174 <= Vars.CursorPosX <= 430) and (279 <= Vars.CursorPosY <= 320):
                        get_sound(2).play(0)
                        Vars.OptionNumber1 = 1
                    elif (174 <= Vars.CursorPosX <= 327) and (354 <= Vars.CursorPosY <= 388) and Vars.Beat6:
                        get_sound(2).play(0)
                        Vars.OptionNumber1 = 2
                        Vars.CheatsOption = False
                    elif (174 <= Vars.CursorPosX <= 420) and (429 <= Vars.CursorPosY <= 515) and Vars.Beat6:
                        get_sound(2).play(0)
                        Vars.OptionNumber1 = 3
                        Vars.DMOption = False

                    if Vars.OptionNumber1 == 0:
                        if (770 <= Vars.CursorPosX <= 830) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            Vars.OptionNumber2 = 0
                        elif (850 <= Vars.CursorPosX <= 910) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            Vars.OptionNumber2 = 1
                        elif (930 <= Vars.CursorPosX <= 990) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            Vars.OptionNumber2 = 2
                        elif (1010 <= Vars.CursorPosX <= 1070) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            Vars.OptionNumber2 = 3

                    elif Vars.OptionNumber1 == 1:
                        if (770 <= Vars.CursorPosX <= 830) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            ResetAnimation([20])
                            Vars.OptionNumber3 = 0
                        elif (850 <= Vars.CursorPosX <= 910) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            ResetAnimation([23])
                            Vars.OptionNumber3 = 1
                        elif (930 <= Vars.CursorPosX <= 990) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            ResetAnimation([17])
                            Vars.OptionNumber3 = 2
                        elif (1010 <= Vars.CursorPosX <= 1070) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            ResetAnimation([18])
                            Vars.OptionNumber3 = 3
                        elif (1090 <= Vars.CursorPosX <= 1150) and (600 <= Vars.CursorPosY <= 660):
                            get_sound(2).play(0)
                            ResetAnimation([19])
                            Vars.OptionNumber3 = 4

                    elif Vars.OptionNumber1 == 2:
                        if (740 <= Vars.CursorPosX <= 982) and (250 <= Vars.CursorPosY <= 292) and not Vars.LongNight:
                            get_sound(2).play(0)
                            Vars.CheatsOption = True
                            Vars.OptionNumber4 = 0
                            Vars.FastNight = not Vars.FastNight
                        elif (740 <= Vars.CursorPosX <= 861) and (325 <= Vars.CursorPosY <= 357):
                            get_sound(2).play(0)
                            Vars.CheatsOption = True
                            Vars.OptionNumber4 = 1
                            Vars.Radar = not Vars.Radar
                        elif (740 <= Vars.CursorPosX <= 1058) and (400 <= Vars.CursorPosY <= 440):
                            get_sound(2).play(0)
                            Vars.CheatsOption = True
                            Vars.OptionNumber4 = 2
                            Vars.EndlessPower = not Vars.EndlessPower

                    elif Vars.OptionNumber1 == 3:
                        if (740 <= Vars.CursorPosX <= 982) and (250 <= Vars.CursorPosY <= 292) and not Vars.FastNight:
                            get_sound(2).play(0)
                            Vars.DMOption = True
                            Vars.OptionNumber5 = 0
                            Vars.LongNight = not Vars.LongNight
                        elif (740 <= Vars.CursorPosX <= 1112) and (325 <= Vars.CursorPosY <= 367):
                            get_sound(2).play(0)
                            Vars.DMOption = True
                            Vars.OptionNumber5 = 1
                            Vars.Aggrmode = not Vars.Aggrmode
                        elif (740 <= Vars.CursorPosX <= 961) and (400 <= Vars.CursorPosY <= 432):
                            get_sound(2).play(0)
                            Vars.DMOption = True
                            Vars.OptionNumber5 = 2
                            Vars.Darkmode = not Vars.Darkmode


            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if not Vars.Extra:
                    if Vars.OptionNumber == 0:
                        self.SwitchToScene(NewspaperScene())
                    elif Vars.OptionNumber == 1:
                        self.SwitchToScene(LoadingScene())
                    elif Vars.OptionNumber == 2:
                        Vars.Night = 6
                        self.SwitchToScene(LoadingScene())
                    elif Vars.OptionNumber == 3:
                        Vars.Night = 7
                        self.SwitchToScene(Customize())
                else:
                    if Vars.OptionNumber1 == 2 and Vars.CheatsOption:
                        get_sound(2).play(0)
                        if Vars.OptionNumber4 == 0 and not Vars.LongNight:
                            Vars.FastNight = not Vars.FastNight
                        elif Vars.OptionNumber4 == 1:
                            Vars.Radar = not Vars.Radar
                        elif Vars.OptionNumber4 == 2:
                            Vars.EndlessPower = not Vars.EndlessPower

                    elif Vars.OptionNumber1 == 3 and Vars.DMOption:
                        get_sound(2).play(0)
                        if Vars.OptionNumber5 == 0 and not Vars.FastNight:
                            Vars.LongNight = not Vars.LongNight
                        elif Vars.OptionNumber5 == 1:
                            Vars.Aggrmode = not Vars.Aggrmode
                        elif Vars.OptionNumber5 == 2:
                            Vars.Darkmode = not Vars.Darkmode

            if not Vars.Extra:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    get_sound(2).play(0)
                    Vars.OptionNumber += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    get_sound(2).play(0)
                    Vars.OptionNumber -= 1
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    get_sound(2).play(0)
                    if Vars.OptionNumber1 == 2 and Vars.CheatsOption:
                        Vars.OptionNumber4 += 1
                    elif Vars.OptionNumber1 == 3 and Vars.DMOption:
                        Vars.OptionNumber5 += 1
                    else:
                        Vars.OptionNumber1 += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    get_sound(2).play(0)
                    if Vars.OptionNumber1 == 2 and Vars.CheatsOption:
                        Vars.OptionNumber4 -= 1
                    elif Vars.OptionNumber1 == 3 and Vars.DMOption:
                        Vars.OptionNumber5 -= 1
                    else:
                        Vars.OptionNumber1 -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    if Vars.OptionNumber1 == 0:
                        get_sound(2).play(0)
                        Vars.OptionNumber2 += 1
                    elif Vars.OptionNumber1 == 1:
                        get_sound(2).play(0)
                        Vars.OptionNumber3 += 1
                    elif Vars.OptionNumber1 == 2:
                        get_sound(2).play(0)
                        Vars.CheatsOption = True
                    elif Vars.OptionNumber1 == 3:
                        get_sound(2).play(0)
                        Vars.DMOption = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    if Vars.OptionNumber1 == 0:
                        get_sound(2).play(0)
                        Vars.OptionNumber2 -= 1
                    elif Vars.OptionNumber1 == 1:
                        get_sound(2).play(0)
                        Vars.OptionNumber3 -= 1
                    elif Vars.OptionNumber1 == 2:
                        get_sound(2).play(0)
                        Vars.CheatsOption = False
                    elif Vars.OptionNumber1 == 3:
                        get_sound(2).play(0)
                        Vars.DMOption = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                get_sound(2).play(0)
                Vars.Extra = not Vars.Extra

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
                Vars.start_ticks = pygame.time.get_ticks()

        if pressed_keys[pygame.K_DELETE] and ((pygame.time.get_ticks() - Vars.start_ticks) / 1000) >= 1:
            Vars.Night = 1
            Vars.BeatGame = False
            Vars.Beat6 = False
            Vars.Beat7 = False
            Vars.BeatHardMode = False
            Vars.Extra = False
            if path.isfile(path.join(getenv('APPDATA'), "fnaf python\\freddy.txt")):
                get_sound(2).play(0)
                remove(path.join(getenv('APPDATA'), "fnaf python\\freddy.txt"))
        if pressed_keys[pygame.K_c] and pressed_keys[pygame.K_d] and pressed_keys[pygame.K_KP1]:
            Vars.BeatGame = True
        if pressed_keys[pygame.K_c] and pressed_keys[pygame.K_d] and pressed_keys[pygame.K_KP2]:
            Vars.Beat6 = True


    def Update(self):
        Vars.Frames += 1
        if Events.Every(self.time, 0.08, 1): # попробовать реализовать влияние DeltaTime на все события связанные с кадрами
            Vars.RandomNum = randrange(100)
            Vars.Opacity[2] = 155 - randrange(0, 100)
        if self.time > 0.08:
            Vars.Y1 += 38 * Vars.dTime
        if Vars.Y1 >= 729:
            Vars.Y1 = -38
        if Events.Every(self.time, 0.3, 2):
            Vars.Opacity[0] = randrange(6,256)
            Vars.Visibility = randrange(0,3)
        if Events.Every(self.time, 0.09, 1):
            Vars.Opacity[1] = 205 - randrange(0,100)

        if not Vars.Extra:
            if (174 <= Vars.CursorPosX <= 377) and (404 <= Vars.CursorPosY <= 437) and Events.OnceEvent(1):
                if Vars.OptionNumber != 0: get_sound(2).play(0)
                Vars.OptionNumber = 0
            elif (173 <= Vars.CursorPosX <= 377) and (476 <= Vars.CursorPosY <= 510) and Events.OnceEvent(2):
                if Vars.OptionNumber != 1: get_sound(2).play(0)
                Vars.OptionNumber = 1
            elif (172 <= Vars.CursorPosX <= 399) and (549 <= Vars.CursorPosY <= 593) and Vars.BeatGame and Events.OnceEvent(3):
                if Vars.OptionNumber != 2: get_sound(2).play(0)
                Vars.OptionNumber = 2
            elif (171 <= Vars.CursorPosX <= 477) and (617 <= Vars.CursorPosY <= 661) and Vars.Beat6 and Events.OnceEvent(4):
                if Vars.OptionNumber != 3: get_sound(2).play(0)
                Vars.OptionNumber = 3


            if Vars.OptionNumber <= -1:
                if Vars.Beat6: Vars.OptionNumber = 3
                elif Vars.BeatGame: Vars.OptionNumber = 2
                else: Vars.OptionNumber = 1
            if (Vars.Beat6 and Vars.OptionNumber >= 4) or \
            (not Vars.Beat6 and Vars.BeatGame and Vars.OptionNumber >= 3) or \
            (not Vars.BeatGame and Vars.OptionNumber >= 2):
                Vars.OptionNumber = 0

        else:
            if Vars.OptionNumber1 <= -1:
                if Vars.Beat6: Vars.OptionNumber1 = 3
                else: Vars.OptionNumber1 = 1
            if (not Vars.Beat6 and Vars.OptionNumber1 >= 2) or \
            (Vars.Beat6 and Vars.OptionNumber1 >= 4):
                Vars.OptionNumber1 = 0

            if Vars.OptionNumber1 == 0:
                if Vars.OptionNumber2 <= -1:
                    Vars.OptionNumber2 = 3
                if Vars.OptionNumber2 >= 4:
                    Vars.OptionNumber2 = 0

            elif Vars.OptionNumber1 == 1:
                if Vars.OptionNumber3 <= -1:
                    Vars.OptionNumber3 = 4
                if Vars.OptionNumber3 >= 5:
                    Vars.OptionNumber3 = 0

            elif Vars.OptionNumber1 == 2:
                if Vars.OptionNumber4 <= -1:
                    Vars.OptionNumber4 = 2
                if Vars.OptionNumber4 >= 3:
                    Vars.OptionNumber4 = 0

            elif Vars.OptionNumber1 == 3:
                if Vars.OptionNumber5 <= -1:
                    Vars.OptionNumber5 = 2
                if Vars.OptionNumber5 >= 3:
                    Vars.OptionNumber5 = 0


    def Render(self, display1, display2):
        display1.blit(get_image('data/sprites/Black.png', 255), (0, 0))
        if Vars.RandomNum == 97:
            display1.blit(get_image('data/sprites/MainMenu/3.png', Vars.Opacity[0]), (0, 0))
        elif Vars.RandomNum == 98:
            display1.blit(get_image('data/sprites/MainMenu/4.png', Vars.Opacity[0]), (0, 0))
        elif Vars.RandomNum == 99:
            display1.blit(get_image('data/sprites/MainMenu/5.png', Vars.Opacity[0]), (0, 0))
        else:
            display1.blit(get_image('data/sprites/MainMenu/2.png', Vars.Opacity[0]), (0, 0))

        if Vars.Visibility == 1:
            PlayAnimation(0, Vars.Opacity[2], (0, 0), display1, True)
        PlayAnimation(1, Vars.Opacity[1], (0, 0), display1, True)

        if not Vars.Extra:
            display1.blit(get_image('data/sprites/MainMenu/23.png', 255), (0, Vars.Y1))
            display1.blit(get_image('data/sprites/MainMenu/24.png', 255), (175, 79))
            display1.blit(get_image('data/sprites/MainMenu/25.png', 255), (174, 404))
            display1.blit(get_image('data/sprites/MainMenu/26.png', 255), (173, 476))

            if Vars.BeatGame:
                display1.blit(get_image('data/sprites/MainMenu/27.png', 255), (172, 549))
            if Vars.Beat6:
                display1.blit(get_image('data/sprites/MainMenu/28.png', 255), (171, 617))

            if Vars.OptionNumber == 0:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (104, 407))
            if Vars.OptionNumber == 1:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (104, 478))
                display1.blit(get_image('data/sprites/MainMenu/30.png', 255), (175, 517))
                match Vars.Night:
                    case 1: display1.blit(get_image('data/sprites/MainMenu/31.png', 255), (250, 518))
                    case 2: display1.blit(get_image('data/sprites/MainMenu/32.png', 255), (250, 518))
                    case 3: display1.blit(get_image('data/sprites/MainMenu/33.png', 255), (250, 518))
                    case 4: display1.blit(get_image('data/sprites/MainMenu/34.png', 255), (250, 518))
                    case _: display1.blit(get_image('data/sprites/MainMenu/35.png', 255), (250, 518))
            if Vars.OptionNumber == 2 and Vars.BeatGame == True:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (99, 558))
            if Vars.OptionNumber == 3 and Vars.Beat6 == True:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (111, 626))

            if Vars.BeatGame: display1.blit(get_image('data/sprites/MainMenu/22.png', 255), (172, 311))
            if Vars.Beat6: display1.blit(get_image('data/sprites/MainMenu/22.png', 255), (249, 311))
            if Vars.Beat7: display1.blit(get_image('data/sprites/MainMenu/22.png', 255), (324, 311))
            if Vars.BeatHardMode: display1.blit(get_image('data/sprites/MainMenu/40.png', 255), (401, 311))
        else:
            display1.blit(get_image('data/sprites/MainMenu/Extra/2.png', 255), (174, 204))
            display1.blit(get_image('data/sprites/MainMenu/Extra/4.png', 255), (174, 279))
            if Vars.Beat6:
                display1.blit(get_image('data/sprites/MainMenu/Extra/5.png', 255), (174, 354))
                display1.blit(get_image('data/sprites/MainMenu/Extra/6.png', 255), (174, 429))
            else:
                display1.blit(get_image('data/sprites/MainMenu/Extra/5.png', 100), (174, 354))
                display1.blit(get_image('data/sprites/MainMenu/Extra/6.png', 100), (174, 429))

            if Vars.OptionNumber1 == 0:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (104, 208))
            elif Vars.OptionNumber1 == 1:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (104, 283))
            elif Vars.OptionNumber1 == 2 and Vars.Beat6 and not Vars.CheatsOption:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (104, 358))
            elif Vars.OptionNumber1 == 3 and Vars.Beat6 and not Vars.DMOption:
                display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (104, 433))

            if Vars.OptionNumber1 == 0:
                if Vars.OptionNumber2 == 0:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b1_1.png', 255), (770, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b1_0.png', 255), (770, 600))

                if Vars.OptionNumber2 == 1:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b2_1.png', 255), (850, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b2_0.png', 255), (850, 600))

                if Vars.OptionNumber2 == 2:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b3_1.png', 255), (930, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b3_0.png', 255), (930, 600))

                if Vars.OptionNumber2 == 3:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b4_1.png', 255), (1010, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/b4_0.png', 255), (1010, 600))

                if Vars.OptionNumber2 == 0:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/Freddy_Fazbear_Original.png', 255), (710, 90))
                elif Vars.OptionNumber2 == 1:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/Bonnie_Original.png', 255), (740, 90))
                elif Vars.OptionNumber2 == 2:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/Chica_Original.png', 255), (640, 90))
                elif Vars.OptionNumber2 == 3:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Animatronics/Foxy_Original.png', 255), (671, 90))

            elif Vars.OptionNumber1 == 1:
                if Vars.OptionNumber3 == 0:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b1_1.png', 255), (770, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b1_0.png', 255), (770, 600))

                if Vars.OptionNumber3 == 1:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b2_1.png', 255), (850, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b2_0.png', 255), (850, 600))

                if Vars.OptionNumber3 == 2:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b3_1.png', 255), (930, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b3_0.png', 255), (930, 600))

                if Vars.OptionNumber3 == 3:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b4_1.png', 255), (1010, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b4_0.png', 255), (1010, 600))

                if Vars.OptionNumber3 == 4:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b5_1.png', 255), (1090, 600))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Jumpscares/b5_0.png', 255), (1090, 600))

                if Vars.OptionNumber3 == 0:
                    PlayAnimation(20, 255, (600, 190), display1, True, (640, 288))
                elif Vars.OptionNumber3 == 1:
                    PlayAnimation(23, 255, (600, 190), display1, True, (640, 360))
                elif Vars.OptionNumber3 == 2:
                    PlayAnimation(17, 255, (600, 190), display1, True, (640, 288))
                elif Vars.OptionNumber3 == 3:
                    PlayAnimation(18, 255, (600, 190), display1, True, (640, 288))
                elif Vars.OptionNumber3 == 4:
                    PlayAnimation(19, 255, (600, 190), display1, True, (640, 288))

            elif Vars.OptionNumber1 == 2:
                if Vars.LongNight:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/5.png', 255), (740, 250))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/1.png', 255), (740, 250))
                display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/2.png', 255), (740, 325))
                display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/3.png', 255), (740, 400))

                if Vars.CheatsOption:
                    if Vars.OptionNumber4 == 0:
                        display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (670, 258))
                    elif Vars.OptionNumber4 == 1:
                        display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (670, 328))
                    elif Vars.OptionNumber4 == 2:
                        display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (670, 407))

                if Vars.FastNight:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/4.png', 255), (1002, 246))
                if Vars.Radar:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/4.png', 255), (881, 316))
                if Vars.EndlessPower:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/Cheats/4.png', 255), (1078, 395))

            elif Vars.OptionNumber1 == 3:
                if Vars.FastNight:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/DM/5.png', 255), (740, 250))
                else:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/DM/1.png', 255), (740, 250))
                display1.blit(get_image('data/sprites/MainMenu/Extra/DM/2.png', 255), (740, 325))
                display1.blit(get_image('data/sprites/MainMenu/Extra/DM/3.png', 255), (740, 400))

                if Vars.DMOption:
                    if Vars.OptionNumber5 == 0:
                        display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (670, 258))
                    elif Vars.OptionNumber5 == 1:
                        display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (670, 333))
                    elif Vars.OptionNumber5 == 2:
                        display1.blit(get_image('data/sprites/MainMenu/29.png', 255), (670, 403))

                if Vars.LongNight:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/DM/4.png', 255), (1002, 246))
                if Vars.Aggrmode:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/DM/4.png', 255), (1132, 321))
                if Vars.Darkmode:
                    display1.blit(get_image('data/sprites/MainMenu/Extra/DM/4.png', 255), (981, 391))

        if not Vars.Extra:
            display1.blit(get_image('data/sprites/MainMenu/36.png', 255), (1044, 644)) # 1044 644
            display1.blit(get_image('data/sprites/MainMenu/37.png', 255), (1026, 666)) # 1026 666
            display1.blit(get_image('data/sprites/MainMenu/38.png', 255), (590, 691)) # 590 691
            display1.blit(get_image('data/sprites/MainMenu/39.png', 255), (27, 689)) # 27 689

        if Vars.BeatGame and not Vars.Extra:
            display1.blit(get_image('data/sprites/MainMenu/Extra/1.png', 255), (1120, 30))
        elif Vars.BeatGame and Vars.Extra:
            display1.blit(get_image('data/sprites/MainMenu/Extra/3.png', 255), (1120, 30))



class NewspaperScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and Vars.Opacity[4] >= 255 and Vars.Opacity[5] <= 0:
                self.start_time = pygame.time.get_ticks() - 6900
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and Vars.Opacity[4] >= 255 and Vars.Opacity[5] <= 0:
                self.start_time = pygame.time.get_ticks() - 6900


    def Update(self):
        Vars.Frames += 1
        if Vars.Opacity[4] <= 255:
            Vars.Opacity[4] += (255 / 2) * Vars.dTime
        if self.time >= 7:
            Vars.Opacity[5] += (255 / 2) * Vars.dTime
        if Vars.Opacity[5] >= 255 + (255 / 2) * 0.5:
            self.SwitchToScene(LoadingScene())


    def Render(self, display1, display2):
        display1.blit(get_image('data/sprites/Screen/screenshot_1.png', 255), (0, 0))
        display1.blit(get_image('data/sprites/Newspaper.png', Vars.Opacity[4]), (0, 0))
        display1.blit(get_image('data/sprites/Black.png', Vars.Opacity[5]), (0, 0))



class LoadingScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        pass


    def Update(self):
        Vars.Frames += 1
        if Vars.Frames == 1:
            get_sound(2).play()
        if self.time > 2.167:
            Vars.Opacity[6] -= (255 / 1.01) * Vars.dTime
        if Vars.Opacity[6] <= 0 - (255 / 1.01) * 1.3:
            self.SwitchToScene(Nightshift())


    def Render(self, display1, display2):
        display1.blit(get_image('data/sprites/Black.png', 255), (0, 0))
        match Vars.Night:
            case 1: display1.blit(get_image('data/sprites/LoadingScene/1.png', Vars.Opacity[6]), (533, 270))
            case 2: display1.blit(get_image('data/sprites/LoadingScene/2.png', Vars.Opacity[6]), (531, 270))
            case 3: display1.blit(get_image('data/sprites/LoadingScene/3.png', Vars.Opacity[6]), (531, 270))
            case 4: display1.blit(get_image('data/sprites/LoadingScene/4.png', Vars.Opacity[6]), (531, 270))
            case 5: display1.blit(get_image('data/sprites/LoadingScene/5.png', Vars.Opacity[6]), (531, 270))
            case 6: display1.blit(get_image('data/sprites/LoadingScene/6.png', Vars.Opacity[6]), (530, 270))
            case _: display1.blit(get_image('data/sprites/LoadingScene/7.png', Vars.Opacity[6]), (526, 270))

        if Vars.Opacity[6] <= 0 - (255 / 1.01) * 0.3:
            display1.blit(get_image('data/sprites/LoadingScene/8.png', 255), (1206, 657))

        PlayAnimation(2, 255, (0,0), display1, False)



class Nightshift(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #344 399: 468 570
                if not Vars.FreddyJumpscare and not Vars.BonnyJumpscare and not Vars.ChicaJumpscare and not Vars.FoxyJumpscare:
                    if not Vars.CameraIsOn and not Vars.PowerDown:
                        if (Vars.X1+24 <= Vars.CursorPosX <= Vars.X1+79) and (288 <= Vars.CursorPosY <= 390) and not Vars.LeftDoorIsMoving and \
                        ((Vars.LeftDoorIsClosed and Vars.ControlRoom[0]) or (not Vars.LeftDoorIsClosed and not Vars.ControlRoom[0])) and not Vars.TabletIsUsing:
                            if not Vars.LeftButtonsAreBroken:
                                Vars.LeftDoorIsClosed = not Vars.LeftDoorIsClosed
                                Vars.LeftDoorIsMoving = True
                                ResetAnimation([4])
                                ResetAnimation([3])
                                get_sound(4).play(0)
                            else:
                                get_sound(20).play(0)
                        elif (Vars.X1+24 <= Vars.CursorPosX <= Vars.X1+79) and (411 <= Vars.CursorPosY <= 513) and not Vars.TabletIsUsing:
                            if not Vars.LeftButtonsAreBroken:
                                Vars.LeftLightIsOn = not Vars.LeftLightIsOn
                                Vars.RightLightIsOn = False
                            else:
                                get_sound(20).play(0)
                        if (Vars.X1+1515 <= Vars.CursorPosX <= Vars.X1+1570) and (304 <= Vars.CursorPosY <= 405) and not Vars.RightDoorIsMoving and \
                        ((Vars.RightDoorIsClosed and Vars.ControlRoom[1]) or (not Vars.RightDoorIsClosed and not Vars.ControlRoom[1])) and not Vars.TabletIsUsing:
                            if not Vars.RightButtonsAreBroken:
                                Vars.RightDoorIsClosed = not Vars.RightDoorIsClosed
                                Vars.RightDoorIsMoving = True
                                ResetAnimation([6])
                                ResetAnimation([5])
                                get_sound(4).play(0)
                            else:
                                get_sound(20).play(0)
                        elif (Vars.X1+1515 <= Vars.CursorPosX <= Vars.X1+1570) and (423 <= Vars.CursorPosY <= 529) and not Vars.TabletIsUsing:
                            if not Vars.RightButtonsAreBroken:
                                Vars.RightLightIsOn = not Vars.RightLightIsOn
                                Vars.LeftLightIsOn = False
                            else:
                                get_sound(20).play(0)
                        elif (Vars.X1+674 <= Vars.CursorPosX <= Vars.X1+682) and (236 <= Vars.CursorPosY <= 244):
                            get_sound(9).play(0)

                    elif Vars.CameraIsOn:
                        if (954 <= Vars.CursorPosX <= 1014) and (334 <= Vars.CursorPosY <= 374):
                            Vars.Camera = {'1a': True, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (934 <= Vars.CursorPosX <= 994) and (390 <= Vars.CursorPosY <= 430):
                            Vars.Camera = {'1a': False, '1b': True, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (902 <= Vars.CursorPosX <= 962) and (468 <= Vars.CursorPosY <= 508):
                            Vars.Camera = {'1a': False, '1b': False, '1c': True, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (954 <= Vars.CursorPosX <= 1014) and (584 <= Vars.CursorPosY <= 624):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': True, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (954 <= Vars.CursorPosX <= 1014) and (624 <= Vars.CursorPosY <= 664):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': True, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (870 <= Vars.CursorPosX <= 930) and (566 <= Vars.CursorPosY <= 606):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': False, '3': True,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (1060 <= Vars.CursorPosX <= 1120) and (585 <= Vars.CursorPosY <= 625):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': True, '4b': False, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (1060 <= Vars.CursorPosX <= 1120) and (625 <= Vars.CursorPosY <= 665):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': True, '5': False, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (828 <= Vars.CursorPosX <= 888) and (417 <= Vars.CursorPosY <= 457):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': True, '6': False, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (1157 <= Vars.CursorPosX <= 1217) and (549 <= Vars.CursorPosY <= 589):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': True, '7': False}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)
                        elif (1166 <= Vars.CursorPosX <= 1226) and (418 <= Vars.CursorPosY <= 458):
                            Vars.Camera = {'1a': False, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                           '4a': False, '4b': False, '5': False, '6': False, '7': True}
                            ResetAnimation([11, 13])
                            get_sound(2).play(0)

                if (27 <= Vars.CursorPosX <= 148) and (22 <= Vars.CursorPosY <= 53):
                    Vars.CallIsMuted = True

        if not Vars.CameraIsOn:
            if Vars.CursorPosX <= 144 and Vars.X1 < 0:
                Vars.X1 += 720 * Vars.dTime
            elif Vars.CursorPosX <= 303 and Vars.X1 < 0:
                Vars.X1 += 420 * Vars.dTime
            elif Vars.CursorPosX <= 519 and Vars.X1 < 0:
                Vars.X1 += 120 * Vars.dTime

            if Vars.CursorPosX >= 1136 and Vars.X1 > -320:
                Vars.X1 -= 720 * Vars.dTime
            elif Vars.CursorPosX >= 977 and Vars.X1 > -320:
                Vars.X1 -= 420 * Vars.dTime
            elif Vars.CursorPosX >= 761 and Vars.X1 > -320:
                Vars.X1 -= 120 * Vars.dTime

        if not Vars.FreddyJumpscare and not Vars.BonnyJumpscare and not Vars.ChicaJumpscare and not Vars.FoxyJumpscare and not Vars.PowerDown:
            if (256 <= Vars.CursorPosX <= 854) and (Vars.CursorPosY >= 645) and not Vars.TabletIsUsing and not Vars.TabletIsMoving and Vars.AbleToUseTablet:
                    ResetAnimation([8, 11])
                    Vars.TabletIsMoving= True
                    Vars.TabletIsUsing = True
                    Vars.AbleToUseTablet = False
                    get_sound(10).play(0)
            elif (256 <= Vars.CursorPosX <= 854) and (Vars.CursorPosY >= 645) and Vars.TabletIsUsing and not Vars.TabletIsMoving and Vars.AbleToUseTablet:
                    ResetAnimation([9])
                    Vars.RandomForPic = randrange(0, 100) + 1
                    Vars.TabletIsMoving= True
                    Vars.TabletIsUsing = False
                    Vars.AbleToUseTablet = False
                    Vars.CameraIsOn = False
                    get_sound(2).stop()
                    get_sound(10).stop()
                    get_sound(12).stop()
                    get_sound(11).play(0)
            elif not(256 <= Vars.CursorPosX <= 854) or (Vars.CursorPosY < 645):
                Vars.AbleToUseTablet = True


    def Update(self):
        Vars.Frames += 1
        if Vars.X1 < -320:
            Vars.X1 = -320
        elif Vars.X1 > 0:
            Vars.X1 = 0
        Vars.RandomNum1 = randrange(0,10) + 1

        if Events.Every(self.time, 0.05, 1):
            Vars.RandomNum3 = randrange(0, 30) + 1

        if Events.Every(self.time, 5, 1):
            if randrange(0, 30) + 1 == 1:
                get_sound(15).play(0)

        if Events.Every(self.time, 10, 1):
            if randrange(0, 50) + 1 == 1:
                get_sound(16).set_volume(randrange(0, 40)/100 + 0.1)
                get_sound(16).play(0)

        if Events.Every(self.time, 4, 1):
            if randrange(0, 30) + 1 == 1 and Vars.FoxyPosition == 0:
                get_sound(7).play(0)

        if Events.Every(self.time, 1, 1):
            Vars.RandomNum2 = randrange(0, 3)

        if Vars.IndicatorX2 == 0:
            if Vars.X2 <= -320:
                Vars.IndicatorX2 += 1
                Vars.X2 = -320
            else:
                Vars.X2 -= 60 * Vars.dTime
        elif Vars.IndicatorX2 == 2:
            if Vars.X2 >= 0:
                Vars.IndicatorX2 += 1
                Vars.X2 = 0
            else:
                Vars.X2 += 60 * Vars.dTime
        elif Vars.IndicatorX2 == 1 or Vars.IndicatorX2 == 3:
            if Vars.IntervalX2 >= 100:
                Vars.IntervalX2 = 0
                if Vars.IndicatorX2 == 3:
                    Vars.IndicatorX2 = 0
                else:
                    Vars.IndicatorX2 += 1
            else:
                Vars.IntervalX2 += 60 * Vars.dTime

        if Vars.LeftDoorIsClosed and not Vars.LeftDoorIsMoving and not Vars.ControlRoom[0]:
            Vars.ControlRoom[0] = True
        elif not Vars.LeftDoorIsClosed and not Vars.LeftDoorIsMoving and Vars.ControlRoom[0]:
            Vars.ControlRoom[0] = False

        if Vars.RightDoorIsClosed and not Vars.RightDoorIsMoving and not Vars.ControlRoom[1]:
            Vars.ControlRoom[1] = True
        elif not Vars.RightDoorIsClosed and not Vars.RightDoorIsMoving and Vars.ControlRoom[1]:
            Vars.ControlRoom[1] = False

        if Vars.RightLightIsOn and not Vars.ControlRoom[2]:
            Vars.ControlRoom[2] = True
        elif not Vars.RightLightIsOn and Vars.ControlRoom[2]:
            Vars.ControlRoom[2] = False

        if Vars.LeftLightIsOn and not Vars.ControlRoom[3]:
            Vars.ControlRoom[3] = True
        elif not Vars.LeftLightIsOn and Vars.ControlRoom[3]:
            Vars.ControlRoom[3] = False

        if Vars.CameraIsOn and not Vars.ControlRoom[4]:
            Vars.ControlRoom[4] = True
        elif not Vars.CameraIsOn and Vars.ControlRoom[4]:
            Vars.ControlRoom[4] = False

        Vars.Usage = sum(Vars.ControlRoom) + 1

        if Vars.Hour == 2:
            if Events.Every(self.time, 6, 1):
                Vars.Power -= 1
        elif Vars.Hour == 3:
            if Events.Every(self.time, 5, 5):
                Vars.Power -= 1
        elif Vars.Hour == 4:
            if Events.Every(self.time, 4, 3):
                Vars.Power -= 1
        elif Vars.Hour >= 5:
            if Events.Every(self.time, 3, 1):
                Vars.Power -= 1

        if Events.Every(self.time, 1, 2):
            Vars.Power -= Vars.Usage

        if Vars.EndlessPower:
            Vars.Power = 999

        if Vars.Power <= 0 and not Vars.PowerDown:
            Vars.Power = 0
            Vars.PowerDown = True
            Vars.LeftLightIsOn = False
            Vars.RightLightIsOn = False
            pygame.mixer.stop()
            get_sound(50).play(0)
            get_sound(51).play(0)

        if Vars.CameraIsOn and Vars.PowerDown:
            ResetAnimation([9])
            Vars.TabletIsMoving = True
            Vars.TabletIsUsing = False
            Vars.CameraIsOn = False
            get_sound(11).play(0)

        if Vars.PowerDown and not Vars.LeftDoorIsMoving and Vars.LeftDoorIsClosed:
            Vars.LeftDoorIsClosed = False
            Vars.LeftDoorIsMoving = True
            ResetAnimation([4])
            ResetAnimation([3])
            get_sound(4).play(0)

        if Vars.PowerDown and not Vars.RightDoorIsMoving and Vars.RightDoorIsClosed:
            Vars.RightDoorIsClosed = False
            Vars.RightDoorIsMoving = True
            ResetAnimation([6])
            ResetAnimation([5])
            get_sound(4).play(0)

        if Events.Every(self.time, 5, 2) and randrange(0, 5) + 1 == 1 and Vars.PowerDown and Vars.PowerDownVars[0] == 0:
            Vars.PowerDownVars[0] = 1
            get_sound(40).set_volume(1)
            get_sound(40).play(0)
        elif Events.Every(self.time, 20, 1) and Vars.PowerDown and Vars.PowerDownVars[0] == 0:
            Vars.PowerDownVars[0] = 1
            get_sound(40).set_volume(1)
            get_sound(40).play(0)
        elif Vars.PowerDownVars[0] == 1 and Events.Every(self.time, 5, 3) and randrange(0, 5) + 1 == 1:
            Vars.PowerDownVars[0] = 2
            pygame.mixer.stop()
            get_sound(13).set_volume(0)
            get_sound(13).play(0)
        elif Vars.PowerDownVars[0] == 1 and Events.Every(self.time, 20, 2):
            Vars.PowerDownVars[0] = 2
            pygame.mixer.stop()
            get_sound(13).set_volume(0)
            get_sound(13).play(0)
        elif Vars.PowerDownVars[0] == 2 and Vars.PowerDownVars[3] < -20:
            Vars.PowerDownVars[0] = 3
            pygame.mixer.stop()
            get_sound(25).play(0)
        elif Vars.PowerDownVars[0] == 3 and Events.Every(self.time, 2, 1) and randrange(0, 5) + 1 == 1:
            Vars.PowerDownVars[0] = 4
            pygame.mixer.stop()
            get_sound(21).play(0)
        elif Vars.PowerDownVars[0] == 3 and Events.Every(self.time, 20, 3):
            Vars.PowerDownVars[0] = 4
            pygame.mixer.stop()
            get_sound(21).set_volume(1)
            get_sound(21).play(0)
        elif Vars.PowerDownVars[0] == 4 and AnimationIsOn(23):
            Vars.PowerDownVars[0] = 5

        if Events.Every(self.time, 0.05, 2) and Vars.PowerDown:
            Vars.PowerDownVars[1] = randrange(0, 4) + 1

        if Vars.PowerDownVars[0] == 2:
            Vars.PowerDownVars[2] = randrange(0, 2) + 1
            Vars.PowerDownVars[3] -= 60 * Vars.dTime

        if Vars.CameraIsOn and not Vars.PowerDown and Events.OnceEvent(6):
            get_sound(2).play(0)
            get_sound(12).play(0)

        if not Vars.TabletIsMoving and Vars.TabletIsUsing and Events.OnceEvent(5):
            Vars.CameraIsOn = True

        if Vars.CameraIsOn and Events.OnceEvent(7):
            Vars.LeftLightIsOn = False
            Vars.RightLightIsOn = False
            get_sound(3).set_volume(0)
            get_sound(13).set_volume(0.1)
        elif not Vars.CameraIsOn and Events.OnceEvent(8):
            get_sound(13).set_volume(0.25)

        Vars.HallucinationVars[1] = randrange(0, 10)

        if Events.Every(self.time, 1, 3):
            if randrange(0, 1000) == 1:
                Vars.HallucinationVars[0] = 1

        if Vars.HallucinationVars[0] == 1:
            Vars.HallucinationVars[2] += 60 * Vars.dTime
            if Vars.HallucinationVars[2] >= 100:
                Vars.HallucinationVars[0] = 0
                Vars.HallucinationVars[2] = 0

        if Vars.HallucinationVars[0] == 1 and Vars.HallucinationVars[1] == 1 and Vars.HallucinationVars[3] == 0:
            get_sound(18).set_volume(1)
            Vars.HallucinationVars[3] = 1
        elif Vars.HallucinationVars[0] == 0 and Vars.BonnyPosition != '2b' and Vars.ChicaPosition != '4b':
            Vars.HallucinationVars[3] = 0
            get_sound(18).set_volume(0)

        if Vars.CameraIsOn and Vars.Camera['1c'] and Events.OnceEvent(9):
            get_sound(7).set_volume(0.15)
        elif (not Vars.CameraIsOn or not Vars.Camera['1c']) and Events.OnceEvent(10):
            get_sound(7).set_volume(0.05)

        if Events.Every(self.time, 0.1, 1):
            if Vars.Night >= 4 and (Vars.BonnyPosition == '2b' or Vars.ChicaPosition == '4b')  and not Vars.CameraIsOn:
                get_sound(18).set_volume((1 + (randrange(0, 5) * 5))/100)
            elif Vars.Night >= 4 and ((Vars.BonnyPosition == '2b' and Vars.Camera['2b']) or
                 (Vars.ChicaPosition == '4b' and Vars.Camera['4b'])) and Vars.CameraIsOn:
                get_sound(18).set_volume((1 + (randrange(0, 5) * 20)) / 100)
            elif Vars.Night >= 4 and ((Vars.BonnyPosition == '2b' and not Vars.Camera['2b']) or
                 (Vars.ChicaPosition == '4b' and not Vars.Camera['4b'])) and Vars.CameraIsOn:
                get_sound(18).set_volume((1 + (randrange(0, 5) * 5)) / 100)
            else:
                get_sound(18).set_volume(0)

        if Vars.ChicaPosition == '6':
            if not Vars.CameraIsOn and Events.OnceEvent(11):
                get_sound(36).set_volume(0.1)
                get_sound(37).set_volume(0.1)
                get_sound(38).set_volume(0.1)
                get_sound(39).set_volume(0.1)
            elif Vars.CameraIsOn and not Vars.Camera['6'] and Events.OnceEvent(12):
                get_sound(36).set_volume(0.2)
                get_sound(37).set_volume(0.2)
                get_sound(38).set_volume(0.2)
                get_sound(39).set_volume(0.2)
            elif Vars.CameraIsOn and Vars.Camera['6'] and Events.OnceEvent(13):
                get_sound(36).set_volume(0.75)
                get_sound(37).set_volume(0.75)
                get_sound(38).set_volume(0.75)
                get_sound(39).set_volume(0.75)
        elif Vars.ChicaPosition != '6' and Events.OnceEvent(14):
            get_sound(36).set_volume(0)
            get_sound(37).set_volume(0)
            get_sound(38).set_volume(0)
            get_sound(39).set_volume(0)

        if Vars.FreddyPosition == '6' and not Vars.PowerDown:
            if not Vars.CameraIsOn and Events.OnceEvent(15):
                get_sound(40).set_volume(0.05)
            elif Vars.CameraIsOn and not Vars.Camera['6'] and Events.OnceEvent(16):
                get_sound(40).set_volume(0.05)
            elif Vars.CameraIsOn and Vars.Camera['6'] and Events.OnceEvent(17):
                get_sound(40).set_volume(0.5)

        if Events.Every(self.time, 4, 2) and Vars.ChicaPosition == '6':
            match randrange(0, 10) + 1:
                case 1: get_sound(36).play(0)
                case 2: get_sound(37).play(0)
                case 3: get_sound(38).play(0)
                case 4: get_sound(38).play(0)
                case 5: get_sound(39).play(0)

        if Events.Every(self.time, 300, 1):
            if Vars.FreddyPosition == '6' and not Vars.PowerDown:
                get_sound(40).play(0)

        if Events.Every(self.time, 5, 4):
            if (Vars.BonnyPosition == 'office' or Vars.ChicaPosition == 'office') and Vars.CameraIsOn and randrange(0, 3) + 1 == 1:
                match randrange(0, 4) + 1:
                    case 1: get_sound(46).play(0)
                    case 2: get_sound(47).play(0)
                    case 3: get_sound(48).play(0)
                    case 4: get_sound(49).play(0)

        if Events.Every(self.time, 30, 1):
            if Vars.CameraIsOn and (Vars.BonnyPosition == 'office' or Vars.ChicaPosition == 'office'):
                ResetAnimation([9])
                Vars.TabletIsMoving = True
                Vars.TabletIsUsing = False
                Vars.CameraIsOn = False
                get_sound(2).stop()
                get_sound(10).stop()
                get_sound(12).stop()
                get_sound(11).play(0)

        if Vars.NoSignalVars[0] == 1:
            if Vars.NoSignalVars[1] > 0:
                Vars.NoSignalVars[1] -= 60 * Vars.dTime
            elif Vars.NoSignalVars[1] <= 0:
                Vars.NoSignalVars[0] = 0

        if Vars.BonnyVars[1] > 0:
            Vars.BonnyVars[1] -= 60 * Vars.dTime

        if Vars.ChicaVars[1] > 0:
            Vars.ChicaVars[1] -= 60 * Vars.dTime

        if Events.Every(self.time, 1, 4):
            Vars.BonnyVars[0] = randrange(0, 2) + 1
            Vars.ChicaVars[0] = randrange(0, 2) + 1

        if Events.Every(self.time, 1, 5) and Vars.GoldenFreddyVars[2] == 0:
            if randrange(0, 100000) == 1: # 100000
                Vars.GoldenFreddyVars[0] = 1
                Vars.GoldenFreddyVars[2] = 1

        if Vars.CameraIsOn and Vars.Camera['2b'] and Vars.BonnyPosition != '2b' and Vars.GoldenFreddyVars[0] == 1:
            get_sound(17).play(0)
            Vars.GoldenFreddyVars[0] = 2

        if Vars.CameraIsOn and Vars.GoldenFreddyVars[0] == 2 and Vars.GoldenFreddyVars[1] == 1:
            GoldenFreddy.Reset()
            Vars.GoldenFreddyVars[0] = 0
            Vars.GoldenFreddyVars[1] = 0

        if not Vars.CameraIsOn and Vars.GoldenFreddyVars[0] == 2:
            if Vars.GoldenFreddyVars[3] == 0:
                Vars.HallucinationVars[0] = 1
            Vars.GoldenFreddyVars[1] = 1
            Vars.GoldenFreddyVars[3] += 60 * Vars.dTime
            if Vars.GoldenFreddyVars[3] >= 300:
                Vars.GoldenFreddyVars[2] = 2

        if Vars.BonnyPosition != 'door' and Events.OnceEvent(18):
            Vars.BonnyVars[3] = 0

        if Vars.ChicaPosition != 'door' and Events.OnceEvent(19):
            Vars.ChicaVars[3] = 0

        if Vars.CameraIsOn:
            if Events.Every(self.time, 0.1, 2):
                Vars.FoxyVars[2] = 50 + randrange(0, 1000)
        elif Vars.FoxyVars[2] > 0:
            Vars.FoxyVars[2] -= 60 * Vars.dTime

        if (Vars.FreddyPosition == 'office' or Vars.BonnyPosition == 'office' or
            Vars.ChicaPosition == 'office' or Vars.FoxyPosition == 'office') and Vars.CameraIsOn and Events.OnceEvent(20):
            Vars.ReadyToJumpscare = True
            Vars.X1 = -160

        if Vars.BonnyPosition == 'office' and not Vars.CameraIsOn and Vars.ReadyToJumpscare and Events.OnceEvent(21):
            Vars.BonnyJumpscare = True
        elif Vars.ChicaPosition == 'office' and not Vars.CameraIsOn and Vars.ReadyToJumpscare and Events.OnceEvent(22):
            Vars.ChicaJumpscare = True

        if AnimationIsOn(20) and Events.OnceEvent(23):
            Vars.FreddyVars[2] = 1

        if Vars.FreddyPosition == 'office' and not Vars.CameraIsOn and not Vars.PowerDown and Vars.FoxyPosition < 5:
            if Events.Every(self.time, 1, 6):
                if randrange(0, 4) == 1:
                    Vars.TabletIsUsing = False
                    Vars.TabletIsMoving = False
                    ResetAnimation([8, 9])
                    Vars.FreddyJumpscare = True

        if AnimationIsOn(19) and Events.OnceEvent(24):
            Vars.FoxyVars[3] = 1

        if Vars.FoxyJumpscare and Events.OnceEvent(25):
            Vars.TabletIsUsing = False
            Vars.TabletIsMoving = False
            ResetAnimation([8, 9])

        if not Vars.PowerDown:
            Freddy.CheckMovement(self.time)
            Bonny.CheckMovement(self.time)
            Chica.CheckMovement(self.time)
            Foxy.CheckMovement(self.time)
            GoldenFreddy.CheckMovement(self.time)

        if not Vars.CameraIsOn and (Vars.BonnyJumpscare or Vars.ChicaJumpscare):
            if Vars.JumpscareVars[0] > 0:
                Vars.JumpscareVars[0] -= 60 * Vars.dTime
            if Vars.JumpscareVars[1] > 0:
                Vars.JumpscareVars[1] -= 60 * Vars.dTime

        if (Vars.JumpscareVars[0] <= 1 or GetFrame(20) >= 6) and Events.OnceEvent(26):
            get_sound(21).play(0)

        if Vars.FreddyPosition != 'office':
            if Vars.FoxyPosition < 2:
                if Vars.BonnyPosition != '2a' and Vars.BonnyPosition != '2b' and Vars.BonnyPosition != '3' and Vars.BonnyPosition != 'door' and \
                   Vars.ChicaPosition != '4a' and Vars.ChicaPosition != '4b' and Vars.ChicaPosition != 'door' and Events.OnceEvent(27):
                    get_sound(35).set_volume(0)
                elif (Vars.BonnyPosition == '2a' or Vars.BonnyPosition == '2b' or Vars.BonnyPosition == '3' or Vars.BonnyPosition == 'door') and \
                     Vars.ChicaPosition != '4a' and Vars.ChicaPosition != '4b' and Vars.ChicaPosition != 'door' and Events.OnceEvent(28):
                    get_sound(35).set_volume(0.3)
                elif Vars.BonnyPosition != '2a' and Vars.BonnyPosition != '2b' and Vars.BonnyPosition != '3' and Vars.BonnyPosition != 'door' and \
                     (Vars.ChicaPosition == '4a' or Vars.ChicaPosition == '4b' or Vars.ChicaPosition == 'door') and Events.OnceEvent(29):
                    get_sound(35).set_volume(0.3)
                elif (Vars.BonnyPosition == '2a' or Vars.BonnyPosition == '2b' or Vars.BonnyPosition == '3' or Vars.BonnyPosition == 'door') and \
                     (Vars.ChicaPosition == '4a' or Vars.ChicaPosition == '4b' or Vars.ChicaPosition == 'door') and Events.OnceEvent(30):
                    get_sound(35).set_volume(0.5)
            elif Vars.FoxyPosition >= 2:
                if Vars.BonnyPosition != '2a' and Vars.BonnyPosition != '2b' and Vars.BonnyPosition != '3' and Vars.BonnyPosition != 'door' and \
                   Vars.ChicaPosition != '4a' and Vars.ChicaPosition != '4b' and Vars.ChicaPosition != 'door' and Events.OnceEvent(31):
                    get_sound(35).set_volume(0.3)
                elif (Vars.BonnyPosition == '2a' or Vars.BonnyPosition == '2b' or Vars.BonnyPosition == '3' or Vars.BonnyPosition == 'door') and \
                     Vars.ChicaPosition != '4a' and Vars.ChicaPosition != '4b' and Vars.ChicaPosition != 'door' and Events.OnceEvent(32):
                    get_sound(35).set_volume(0.5)
                elif Vars.BonnyPosition != '2a' and Vars.BonnyPosition != '2b' and Vars.BonnyPosition != '3' and Vars.BonnyPosition != 'door' and \
                     (Vars.ChicaPosition == '4a' or Vars.ChicaPosition == '4b' or Vars.ChicaPosition == 'door') and Events.OnceEvent(33):
                    get_sound(35).set_volume(0.5)
                elif (Vars.BonnyPosition == '2a' or Vars.BonnyPosition == '2b' or Vars.BonnyPosition == '3' or Vars.BonnyPosition == 'door') and \
                     (Vars.ChicaPosition == '4a' or Vars.ChicaPosition == '4b' or Vars.ChicaPosition == 'door') and Events.OnceEvent(34):
                    get_sound(35).set_volume(0.75)
        elif Vars.FreddyPosition == 'office' and Events.OnceEvent(35):
            get_sound(35).set_volume(1)

        if not Vars.CameraIsOn and not Vars.CallIsMuted and Events.OnceEvent(36):
            get_sound(41).set_volume(1)
            get_sound(42).set_volume(1)
            get_sound(43).set_volume(1)
            get_sound(44).set_volume(1)
            get_sound(45).set_volume(1)
        elif Vars.CameraIsOn and not Vars.CallIsMuted and Events.OnceEvent(37):
            get_sound(41).set_volume(0.5)
            get_sound(42).set_volume(0.5)
            get_sound(43).set_volume(0.5)
            get_sound(44).set_volume(0.5)
            get_sound(45).set_volume(0.5)
        elif Vars.CallIsMuted and Events.OnceEvent(38):
            get_sound(41).set_volume(0)
            get_sound(42).set_volume(0)
            get_sound(43).set_volume(0)
            get_sound(44).set_volume(0)
            get_sound(45).set_volume(0)

        if Events.Once(self.time, 180, 1):
            Vars.BonnyActivity += 1
        if Events.Once(self.time, 270, 1):
            Vars.BonnyActivity += 1
            Vars.ChicaActivity += 1
            Vars.FoxyActivity += 1
        if Events.Once(self.time, 360, 1):
            Vars.BonnyActivity += 1
            Vars.ChicaActivity += 1
            Vars.FoxyActivity += 1

        if Vars.EndlessPower:
            Vars.Power = 999

        if Events.Every(self.time, Vars.HourLength, 99):
            Vars.Hour += 1

        if Vars.Hour >= 6: #32400
            self.SwitchToScene(NextDay())
        elif Vars.GoldenFreddyVars[2] == 2:
            self.SwitchToScene(CreepyEnd())
        elif Vars.JumpscareVars[1] <= 1:
            self.SwitchToScene(Gameover())
        elif Vars.FreddyJumpscare and not AnimationIsOn(20) and Vars.FreddyVars[2] == 1:
            self.SwitchToScene(Gameover())
        elif not(AnimationIsOn(19)) and Vars.FoxyVars[3] == 1:
            self.SwitchToScene(Gameover())
        elif Vars.PowerDownVars[0] == 5 and not AnimationIsOn(23):
            self.SwitchToScene(Gameover())


    def Render(self, display1, display2):
        if Vars.CameraIsOn:
            PlayAnimation(10, 255-(150+randrange(0, 50)+(Vars.RandomNum2*15)), (0, 0), display1, True)

        if 20 <= self.time <= 40 and not Vars.CallIsMuted and Vars.Night <= 5 and not Vars.PowerDown:
            display1.blit(get_image('data/sprites/Nightshift/Text/MuteCall/1.png', 255), (27, 22))

        if not Vars.PowerDown:
            display1.blit(get_image('data/sprites/Nightshift/Text/TopRight/1.png', 255), (1200, 31))
            display1.blit(get_image('data/sprites/Nightshift/Text/TopRight/2.png', 255), (1148, 74))

            if Vars.Hour == 0:
                display1.blit(get_image('data/sprites/Nightshift/Text/TopRight/1_1.png', 255), (1137, 29))
                display1.blit(get_image('data/sprites/Nightshift/Text/TopRight/1_2.png', 255), (1161, 29))
            else:
                display1.blit(get_image(f'data/sprites/Nightshift/Text/TopRight/1_{Vars.Hour}.png', 255), (1161, 29))

            display1.blit(get_image(f'data/sprites/Nightshift/Text/TopRight/2_{Vars.Night}.png', 255), (1223, 72))

            display1.blit(get_image('data/sprites/Nightshift/Text/BottomLeft/1.png', 255), (38, 631))
            display1.blit(get_image('data/sprites/Nightshift/Text/BottomLeft/2.png', 255), (38, 667))
            display1.blit(get_image('data/sprites/Nightshift/Text/BottomLeft/3.png', 255), (224, 632))

            if Vars.Power >= 1000:
                display1.blit(get_image(f'data/sprites/Nightshift/Text/BottomLeft/1_{Vars.Power//1000 - (Vars.Power//10000)*10}.png', 255), (167, 624))
            if Vars.Power >= 100:
                display1.blit(get_image(f'data/sprites/Nightshift/Text/BottomLeft/1_{Vars.Power//100 - (Vars.Power//1000)*10}.png', 255), (185, 624))
            display1.blit(get_image(f'data/sprites/Nightshift/Text/BottomLeft/1_{Vars.Power//10 - (Vars.Power//100)*10}.png', 255), (203, 624))

            display1.blit(get_image(f'data/sprites/Nightshift/Text/BottomLeft/2_{Vars.Usage}.png', 255), (120, 657))

            if not ((256 <= Vars.CursorPosX <= 854) and (Vars.CursorPosY >= 645)):
                display1.blit(get_image(f'data/sprites/Nightshift/Text/Camera/1.png', 255), (255, 638))

        if Vars.TabletIsMoving and Vars.TabletIsUsing:
            PlayAnimation(8, 255, (0, 0), display1, False, lastFrame=True)

        if Vars.TabletIsMoving and not Vars.TabletIsUsing:
            PlayAnimation(9, 255, (0, 0), display1, False)

        Vars.TabletIsMoving = AnimationIsOn(8) or AnimationIsOn(9)

        if Vars.HallucinationVars[0] == 1 and Vars.HallucinationVars[1] == 1:
            PlayAnimation(16, 255, (0, 0), display1, True)


        if not Vars.CameraIsOn:
            if not Vars.PowerDown:
                if Vars.LeftLightIsOn and Vars.RandomNum1 > 1:
                    if Vars.BonnyPosition != 'door':
                        get_sound(3).set_volume(1)
                        display2.blit(get_image('data/sprites/Nightshift/Office/2.png', 255), (Vars.X1, 0))
                    else:
                        if Vars.BonnyVars[3] == 0:
                            Vars.BonnyVars[3] = 1
                            get_sound(19).play(0)
                        get_sound(3).set_volume(1)
                        display2.blit(get_image('data/sprites/Nightshift/Office/4.png', 255), (Vars.X1, 0))
                elif Vars.RightLightIsOn and Vars.RandomNum1 > 1:
                    if Vars.ChicaPosition != 'door':
                        get_sound(3).set_volume(1)
                        display2.blit(get_image('data/sprites/Nightshift/Office/3.png', 255), (Vars.X1, 0))
                    else:
                        if Vars.ChicaVars[3] == 0:
                            Vars.ChicaVars[3] = 1
                            get_sound(19).play(0)
                        get_sound(3).set_volume(1)
                        display2.blit(get_image('data/sprites/Nightshift/Office/5.png', 255), (Vars.X1, 0))
                elif Vars.BonnyJumpscare:
                    PlayAnimation(17, 255, (Vars.X1, 0), display2, True)
                elif Vars.ChicaJumpscare:
                    PlayAnimation(18, 255, (Vars.X1, 0), display2, True)
                elif Vars.FreddyJumpscare:
                    PlayAnimation(20, 255, (Vars.X1, 0), display2, False)
                elif Vars.FoxyJumpscare:
                    PlayAnimation(19, 255, (Vars.X1, 0), display2, False)
                else:
                    get_sound(3).set_volume(0)
                    display2.blit(get_image('data/sprites/Nightshift/Office/1.png', 255), (Vars.X1, 0))
            else:
                if Vars.PowerDownVars[0] == 0:
                    display2.blit(get_image('data/sprites/Nightshift/Office/6.png', 255), (Vars.X1, 0))
                elif Vars.PowerDownVars[0] == 1:
                    if Vars.PowerDownVars[1] == 1:
                        display2.blit(get_image('data/sprites/Nightshift/Office/7.png', 255), (Vars.X1, 0))
                    elif Vars.PowerDownVars[1] >= 2:
                        display2.blit(get_image('data/sprites/Nightshift/Office/6.png', 255), (Vars.X1, 0))
                elif Vars.PowerDownVars[0] == 2:
                    if Vars.PowerDownVars[2] == 1:
                        display2.blit(get_image('data/sprites/Nightshift/Office/6.png', 255), (Vars.X1, 0))
                        get_sound(13).set_volume(0.5)
                    elif Vars.PowerDownVars[2] == 2:
                        get_sound(13).set_volume(0)
                elif Vars.PowerDownVars[0] >= 4:
                    PlayAnimation(23, 255, (0, 0), display1, False)

            if not Vars.FreddyJumpscare and not Vars.BonnyJumpscare and not Vars.ChicaJumpscare:
                if not Vars.PowerDown:
                    PlayAnimation(7, 255, (Vars.X1+780, 303), display2, True)

                if Vars.GoldenFreddyVars[0] == 2 and not(Vars.BonnyJumpscare or Vars.ChicaJumpscare or Vars.FreddyJumpscare):
                    display2.blit(get_image('data/sprites/Nightshift/Office/6666.png', 255), (Vars.X1+390, 218))

                if not Vars.FoxyJumpscare:
                    if not Vars.LeftDoorIsClosed and Vars.LeftDoorIsMoving:
                        PlayAnimation(4, 255, (Vars.X1 + 72, -1), display2, False)
                    if Vars.LeftDoorIsClosed and Vars.LeftDoorIsMoving:
                        PlayAnimation(3, 255, (Vars.X1 + 72, -1), display2, False)

                    if not Vars.RightDoorIsClosed and Vars.RightDoorIsMoving:
                        PlayAnimation(6, 255, (Vars.X1 + 1270, -2), display2, False)
                    if Vars.RightDoorIsClosed and Vars.RightDoorIsMoving:
                        PlayAnimation(5, 255, (Vars.X1 + 1270, -2), display2, False)

                    Vars.LeftDoorIsMoving = AnimationIsOn(4) or AnimationIsOn(3)
                    Vars.RightDoorIsMoving = AnimationIsOn(6) or AnimationIsOn(5)

                    if not Vars.LeftDoorIsClosed and not Vars.LeftDoorIsMoving:
                        display2.blit(get_image('data/sprites/Nightshift/LeftDoor/1.png', 255), (Vars.X1 + 72, -1))
                    if Vars.LeftDoorIsClosed and not Vars.LeftDoorIsMoving:
                        display2.blit(get_image('data/sprites/Nightshift/LeftDoor/2.png', 255), (Vars.X1 + 72, -1))

                    if not Vars.RightDoorIsClosed and not Vars.RightDoorIsMoving:
                        display2.blit(get_image('data/sprites/Nightshift/RightDoor/1.png', 255), (Vars.X1 + 1270, -2))
                    if Vars.RightDoorIsClosed and not Vars.RightDoorIsMoving:
                        display2.blit(get_image('data/sprites/Nightshift/RightDoor/2.png', 255), (Vars.X1 + 1270, -2))


                if not Vars.PowerDown:
                    if not Vars.LeftDoorIsClosed and not Vars.LeftLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/1.png', 255), (Vars.X1+2, 267))
                    elif not Vars.LeftDoorIsClosed and Vars.LeftLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/3.png', 255), (Vars.X1+2, 267))
                    elif Vars.LeftDoorIsClosed and not Vars.LeftLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/2.png', 255), (Vars.X1+2, 267))
                    elif Vars.LeftDoorIsClosed and Vars.LeftLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/4.png', 255), (Vars.X1+2, 267))

                    if not Vars.RightDoorIsClosed and not Vars.RightLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/5.png', 255), (Vars.X1+1500, 277))
                    elif not Vars.RightDoorIsClosed and Vars.RightLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/7.png', 255), (Vars.X1+1500, 277))
                    elif Vars.RightDoorIsClosed and not Vars.RightLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/6.png', 255), (Vars.X1+1500, 277))
                    elif Vars.RightDoorIsClosed and Vars.RightLightIsOn:
                        display2.blit(get_image('data/sprites/Nightshift/Buttons/8.png', 255), (Vars.X1+1500, 277))

                if Vars.FoxyPosition == 4:
                    PlayAnimation(15, 255, (2000, 0), display2, False)

        elif Vars.CameraIsOn and not Vars.PowerDown:
            PlayAnimation(14, 255, (68, 52), display1, True)
            PlayAnimation(11, 255, (0, 0), display1, False)
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/1.png', 255), (0, -1))
            PlayAnimation(12, 255, (848, 313), display1, True)

            if Vars.Camera['1a']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_1.png', 255), (832, 292))
                PlayAnimation(13, 255, (954, 334), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (954, 334))

            if Vars.Camera['1b']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_2.png', 255), (832, 292))
                PlayAnimation(13, 255, (934, 390), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (934, 390))

            if Vars.Camera['1c']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_3.png', 255), (832, 292))
                PlayAnimation(13, 255, (902, 468), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (902, 468))

            if Vars.Camera['2a']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_4.png', 255), (832, 292))
                PlayAnimation(13, 255, (954, 584), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (954, 584))

            if Vars.Camera['2b']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_5.png', 255), (832, 292))
                PlayAnimation(13, 255, (954, 624), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (954, 624))

            if Vars.Camera['3']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_6.png', 255), (832, 292))
                PlayAnimation(13, 255, (870, 566), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (870, 566))

            if Vars.Camera['4a']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_7.png', 255), (832, 292))
                PlayAnimation(13, 255, (1060, 585), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (1060, 585))

            if Vars.Camera['4b']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_8.png', 255), (832, 292))
                PlayAnimation(13, 255, (1060, 625), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (1060, 625))

            if Vars.Camera['5']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_9.png', 255), (832, 292))
                PlayAnimation(13, 255, (828, 417), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (828, 417))

            if Vars.Camera['6']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_10.png', 255), (832, 292))
                PlayAnimation(13, 255, (1157, 549), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (1157, 549))

            if Vars.Camera['7']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/7_11.png', 255), (832, 292))
                PlayAnimation(13, 255, (1166, 418), display1, True)
            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/5_2.png', 255), (1166, 418))

            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_1a.png', 255), (962, 341))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_1b.png', 255), (940, 397))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_1c.png', 255), (909, 475))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_2a.png', 255), (961, 590))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_2b.png', 255), (961, 630))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_3.png', 255), (878, 574))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_4a.png', 255), (1067, 592))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_4b.png', 255), (1067, 632))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_5.png', 255), (835, 424))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_6.png', 255), (1164, 556))
            display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/6_7.png', 255), (1173, 424))

            if Vars.Radar:
                Freddy.DisplayLocation(display1)
                Bonny.DisplayLocation(display1)
                Chica.DisplayLocation(display1)
                Foxy.DisplayLocation(display1)

            if Vars.FoxyPosition == 4 and AnimationIsOn(15) and not Vars.Camera['2a']:
                PlayAnimation(15, 255, (2000, 0), display2, False)

            if Vars.Camera['1a'] and Vars.NoSignalVars[0] == 0:
                if Vars.FreddyPosition == '1a' and Vars.BonnyPosition == '1a' and Vars.ChicaPosition == '1a':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1a_1.png', 255), (Vars.X2, 0))
                elif Vars.BonnyPosition != '1a' and Vars.ChicaPosition == '1a':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1a_2.png', 255), (Vars.X2, 0))
                elif Vars.BonnyPosition == '1a' and Vars.ChicaPosition != '1a':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1a_3.png', 255), (Vars.X2, 0))
                elif Vars.FreddyPosition == '1a' and Vars.BonnyPosition != '1a' and Vars.ChicaPosition != '1a':
                    if Vars.RandomForPic <= 10:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1a_6.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1a_4.png', 255), (Vars.X2, 0))
                else:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1a_5.png', 255), (Vars.X2, 0))

            elif Vars.Camera['1b'] and Vars.NoSignalVars[0] == 0:
                if Vars.ChicaPosition == '1b':
                    if Vars.ChicaVars[2] == 1:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1b_3.png', 255), (Vars.X2, 0))
                    elif Vars.ChicaVars[2] == 2:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1b_4.png', 255), (Vars.X2, 0))
                elif Vars.BonnyPosition == '1b':
                    if Vars.BonnyVars[2] == 1:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1b_5.png', 255), (Vars.X2, 0))
                    elif Vars.BonnyVars[2] == 2:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1b_6.png', 255), (Vars.X2, 0))
                elif Vars.FreddyPosition == '1b':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1b_2.png', 255), (Vars.X2, 0))
                else:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1b_1.png', 255), (Vars.X2, 0))

            elif Vars.Camera['1c'] and Vars.NoSignalVars[0] == 0:
                if Vars.FoxyPosition == 0:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1c_1.png', 255), (Vars.X2, 0))
                elif Vars.FoxyPosition == 1:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1c_2.png', 255), (Vars.X2, 0))
                elif Vars.FoxyPosition == 2:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/1c_3.png', 255), (Vars.X2, 0))
                else:
                    if Vars.RandomForPic > 10:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1c_4.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/1c_5.png', 255), (Vars.X2, 0))

            elif Vars.Camera['2a'] and Vars.NoSignalVars[0] == 0:
                if Vars.FoxyPosition == 4:
                    PlayAnimation(15, 255, (Vars.X2, 0), display2, False)
                    if not AnimationIsOn(15):
                        display2.blit(get_image('data/sprites/Nightshift/Camera/2a_4_33.png', 255), (Vars.X2, 0))
                elif Vars.BonnyPosition == '2a' and Vars.RandomNum1 <= 3:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/2a_3.png', 255), (Vars.X2, 0))
                elif Vars.RandomNum1 <= 3:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/2a_2.png', 255), (Vars.X2, 0))
                elif Vars.RandomNum1 > 3:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/2a_1.png', 255), (Vars.X2, 0))

            elif Vars.Camera['2b'] and Vars.NoSignalVars[0] == 0:
                if Vars.BonnyPosition != '2b':
                    if Vars.GoldenFreddyVars[0] == 0:
                        if Vars.RandomForPic >= 2:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/2b_1.png', 255), (Vars.X2, 0))
                        else:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/2b_2.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/2b_3.png', 255), (Vars.X2, 0))
                else:
                    if Vars.Night >= 4:
                        if 25 <= Vars.RandomNum3 < 29:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/2b_5.png', 255), (Vars.X2, 0))
                        elif Vars.RandomNum3 >= 29:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/2b_6.png', 255), (Vars.X2, 0))
                        else:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/2b_4.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/2b_4.png', 255), (Vars.X2, 0))

            elif Vars.Camera['3'] and Vars.NoSignalVars[0] == 0:
                if Vars.BonnyPosition == '3':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/3_2.png', 255), (Vars.X2, 0))
                else:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/3_1.png', 255), (Vars.X2, 0))

            elif Vars.Camera['4a'] and Vars.NoSignalVars[0] == 0:
                if Vars.ChicaPosition == '4a':
                    if Vars.ChicaVars[2] == 1:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4a_3.png', 255), (Vars.X2, 0))
                    elif Vars.ChicaVars[2] == 2:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4a_4.png', 255), (Vars.X2, 0))
                elif Vars.FreddyPosition == '4a':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/4a_2.png', 255), (Vars.X2, 0))
                else:
                    if Vars.RandomForPic <= 98:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4a_1.png', 255), (Vars.X2, 0))
                    elif Vars.RandomForPic == 99:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4a_5.png', 255), (Vars.X2, 0))
                    elif Vars.RandomForPic == 100:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4a_6.png', 255), (Vars.X2, 0))

            elif Vars.Camera['4b'] and Vars.NoSignalVars[0] == 0:
                if Vars.ChicaPosition == '4b':
                    if Vars.Night >= 4:
                        if 25 <= Vars.RandomNum3 < 29:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/4b_4.png', 255), (Vars.X2, 0))
                        elif Vars.RandomNum3 >= 29:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/4b_5.png', 255), (Vars.X2, 0))
                        else:
                            display2.blit(get_image('data/sprites/Nightshift/Camera/4b_3.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4b_3.png', 255), (Vars.X2, 0))
                elif Vars.FreddyPosition == '4b':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/4b_2.png', 255), (Vars.X2, 0))
                else:
                    if Vars.RandomForPic <= 96:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4b_1.png', 255), (Vars.X2, 0))
                    elif Vars.RandomForPic == 97:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4b_6.png', 255), (Vars.X2, 0))
                    elif Vars.RandomForPic == 98:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4b_7.png', 255), (Vars.X2, 0))
                    elif Vars.RandomForPic == 99:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4b_8.png', 255), (Vars.X2, 0))
                    elif Vars.RandomForPic == 100:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/4b_9.png', 255), (Vars.X2, 0))

            elif Vars.Camera['5'] and Vars.NoSignalVars[0] == 0:
                if Vars.BonnyPosition == '5':
                    if Vars.RandomForPic > 10:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/5_3.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/5_4.png', 255), (Vars.X2, 0))
                else:
                    if Vars.RandomForPic > 5:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/5_1.png', 255), (Vars.X2, 0))
                    else:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/5_2.png', 255), (Vars.X2, 0))

            elif Vars.Camera['6']:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/9.png', 255), (464, 69))

            elif Vars.Camera['7'] and Vars.NoSignalVars[0] == 0:
                if Vars.ChicaPosition == '7':
                    if Vars.ChicaVars[2] == 1:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/7_3.png', 255), (Vars.X2, 0))
                    elif Vars.ChicaVars[2] == 2:
                        display2.blit(get_image('data/sprites/Nightshift/Camera/7_4.png', 255), (Vars.X2, 0))
                elif Vars.FreddyPosition == '7':
                    display2.blit(get_image('data/sprites/Nightshift/Camera/7_2.png', 255), (Vars.X2, 0))
                else:
                    display2.blit(get_image('data/sprites/Nightshift/Camera/7_1.png', 255), (Vars.X2, 0))

            else:
                display1.blit(get_image('data/sprites/Nightshift/Camera/Elements/9.png', 255), (464, 69))

        if Vars.Darkmode:
            display2.blit(get_image('data/sprites/Nightshift/Office/Light.png', 255), (Vars.CursorPosX-1500, Vars.CursorPosY-1500))
        #display1.blit(get_image('data/sprites/LoadingScene/8.png', 255), (1206, 657))

        #pygame.draw.line(display1, (255, 0, 0), (144, 0), (144, 720))
        #pygame.draw.line(display1, (255, 0, 0), (303, 0), (303, 720))
        #pygame.draw.line(display1, (255, 0, 0), (519, 0), (519, 720))

        #pygame.draw.line(display1, (255, 0, 0), (761, 0), (761, 720))
        #pygame.draw.line(display1, (255, 0, 0), (977, 0), (977, 720))
        #pygame.draw.line(display1, (255, 0, 0), (1136, 0), (1136, 720))

        #pygame.draw.line(display1, (255, 255, 255), (640, 0), (640, 720))



class Gameover(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        if Events.Once(self.time, 10, 1):
            remove_image('data/sprites/Screen/screenshot_1.png')
            screenshot(display1, 1)

    def Update(self):
        Vars.Frames += 1
        if Events.Once(self.time, 10, 2):
            pygame.mixer.stop()
        if self.time > 10 and Vars.Opacity[12] > 0:
            Vars.Opacity[12] -= (255 / 1.01) * Vars.dTime

        if Events.Every(self.time, 1, 1):
            Vars.RandomNum4 = randrange(0, 10000) + 1

        if self.time > 21:
            if Vars.RandomNum4 == 1:
                self.SwitchToScene(CreepyEnd())
            else:
                self.SwitchToScene(MainMenu())

    def Render(self, display1, display2):
        if self.time <= 10:
            PlayAnimation(22, 255, (0, 0), display1, True)
            PlayAnimation(21, 255, (0, 0), display1, False)
        else:
            display1.blit(get_image('data/sprites/Gameover/3.png', 255), (0, 0))
            display1.blit(get_image('data/sprites/Gameover/4.png', 255), (1046, 660))
            display1.blit(get_image('data/sprites/Screen/screenshot_1.png', Vars.Opacity[12]), (0, 0))



class NextDay(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        pass

    def Update(self):
        Vars.Frames += 1
        if Vars.Opacity[7] <= 255:
            Vars.Opacity[7] += (255 / 1.01) * Vars.dTime
        if self.time >= 9:
            Vars.Opacity[8] += (255 / 0.9) * Vars.dTime
        if Vars.Opacity[7] >= 255 and Vars.Y2 > -112:
            Vars.Y2 -= 24 * Vars.dTime
        if Vars.Y2 <= -112 and Events.OnceEvent(40):
            get_sound(6).play(0)
        if Vars.Opacity[8] >= 255 + (255 / 0.9) * 0.5:
            if Vars.Night >= 6:
                self.SwitchToScene(TheEnd())
            else:
                self.SwitchToScene(LoadingScene())


    def Render(self, display1, display2):
        if self.time <= 1:
            display2.blit(get_image('data/sprites/Screen/screenshot_2.png', 255), (0, 0))
            display1.blit(get_image('data/sprites/Screen/screenshot_1.png', 255), (0, 0))
        display1.blit(get_image('data/sprites/Black.png', Vars.Opacity[7]), (0, 0))
        display1.blit(get_image('data/sprites/NextDay/1.png', Vars.Opacity[7]), (645, 296))
        display1.blit(get_image('data/sprites/NextDay/2.png', Vars.Opacity[7]), (549, Vars.Y2+298))
        if Vars.Opacity[7] >= 255:
            display1.blit(get_image('data/sprites/NextDay/3.png', Vars.Opacity[7]), (553, Vars.Y2+408))
            display1.blit(get_image('data/sprites/NextDay/4.png', Vars.Opacity[7]), (498, 169))
            display1.blit(get_image('data/sprites/NextDay/4.png', Vars.Opacity[7]), (498, 385))
        display1.blit(get_image('data/sprites/Black.png', Vars.Opacity[8]), (0, 0))



class TheEnd(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        pass

    def Update(self):
        Vars.Frames += 1
        if self.time < 17 and Vars.Opacity[9] >= 0:
            Vars.Opacity[9] -= (255 / 2) * Vars.dTime
        if self.time >= 17:
            Vars.Opacity[9] += (255 / 2) * Vars.dTime
        if self.time >= 19 and Vars.Opacity[9] >= 255 + (255 / 2) * 0.5:
            self.SwitchToScene(MainMenu())

    def Render(self, display1, display2):
        if Vars.Night == 6:
            display1.blit(get_image('data/sprites/TheEnd/1.png', 255), (0, 0))
        elif Vars.Night == 7:
            display1.blit(get_image('data/sprites/TheEnd/2.png', 255), (0, 0))
        else:
            display1.blit(get_image('data/sprites/TheEnd/3.png', 255), (0, 0))
        display1.blit(get_image('data/sprites/Black.png', Vars.Opacity[9]), (0, 0))



class Customize(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and Vars.Opacity[10] >= 255:
                if (117 <= Vars.CursorPosX <= 151) and (470 <= Vars.CursorPosY <= 522) and Vars.FreddyAI > 0: # 117, 470
                    Vars.FreddyAI -= 1
                elif (283 <= Vars.CursorPosX <= 317) and (470 <= Vars.CursorPosY <= 522) and Vars.FreddyAI < 20: # 117, 470
                    Vars.FreddyAI += 1
                if (401 <= Vars.CursorPosX <= 435) and (470 <= Vars.CursorPosY <= 522) and Vars.BonnyAI > 0: # 117, 470
                    Vars.BonnyAI -= 1
                elif (565 <= Vars.CursorPosX <= 599) and (470 <= Vars.CursorPosY <= 522) and Vars.BonnyAI < 20: # 117, 470
                    Vars.BonnyAI += 1
                if (685 <= Vars.CursorPosX <= 719) and (470 <= Vars.CursorPosY <= 522) and Vars.ChicaAI > 0: # 117, 470
                    Vars.ChicaAI -= 1
                elif (848 <= Vars.CursorPosX <= 882) and (470 <= Vars.CursorPosY <= 522) and Vars.ChicaAI < 20: # 117, 470
                    Vars.ChicaAI += 1
                if (964 <= Vars.CursorPosX <= 998) and (470 <= Vars.CursorPosY <= 522) and Vars.FoxyAI > 0: # 117, 470
                    Vars.FoxyAI -= 1
                elif (1126 <= Vars.CursorPosX <= 1160) and (470 <= Vars.CursorPosY <= 522) and Vars.FoxyAI < 20: # 117, 470
                    Vars.FoxyAI += 1

                if (1049 <= Vars.CursorPosX <= 1235) and (628 <= Vars.CursorPosY <= 686):
                    if Vars.FreddyAI == 1 and Vars.BonnyAI == 9 and Vars.ChicaAI == 8 and Vars.FoxyAI == 7:
                        self.SwitchToScene(CreepyEnd())
                    else:
                        self.SwitchToScene(LoadingScene())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and Vars.Opacity[10] >= 255:
                self.SwitchToScene(LoadingScene())


    def Update(self):
        Vars.Frames += 1
        if Vars.Opacity[10] < 255:
            Vars.Opacity[10] += (255 / 0.56) * Vars.dTime


    def Render(self, display1, display2):
        display1.blit(get_image('data/sprites/Screen/screenshot_1.png', 255), (0, 0))

        display1.blit(get_image('data/sprites/Black.png', Vars.Opacity[10]), (0, 0))

        display1.blit(get_image('data/sprites/Customize/1.png', Vars.Opacity[10]), (420, 40)) # Customize Night
        display1.blit(get_image('data/sprites/Customize/2.png', Vars.Opacity[10]), (116, 654)) # Levels of Difficulty
        display1.blit(get_image('data/sprites/Customize/3.png', Vars.Opacity[10]), (1049, 628)) # Button Ready

        display1.blit(get_image('data/sprites/Customize/4.png', Vars.Opacity[10]), (145, 119)) # Names
        display1.blit(get_image('data/sprites/Customize/5.png', Vars.Opacity[10]), (429, 119))
        display1.blit(get_image('data/sprites/Customize/6.png', Vars.Opacity[10]), (716, 119))
        display1.blit(get_image('data/sprites/Customize/7.png', Vars.Opacity[10]), (1009, 121))

        display1.blit(get_image('data/sprites/Customize/8.png', Vars.Opacity[10]), (118, 187)) # Sprites
        display1.blit(get_image('data/sprites/Customize/9.png', Vars.Opacity[10]), (403, 187))
        display1.blit(get_image('data/sprites/Customize/10.png', Vars.Opacity[10]), (682, 187))
        display1.blit(get_image('data/sprites/Customize/11.png', Vars.Opacity[10]), (957, 187))

        display1.blit(get_image('data/sprites/Customize/12.png', Vars.Opacity[10]), (118, 425)) # A.I. Level
        display1.blit(get_image('data/sprites/Customize/12.png', Vars.Opacity[10]), (402, 425))
        display1.blit(get_image('data/sprites/Customize/12.png', Vars.Opacity[10]), (684, 425))
        display1.blit(get_image('data/sprites/Customize/12.png', Vars.Opacity[10]), (960, 425))

        display1.blit(get_image('data/sprites/Customize/13.png', Vars.Opacity[10]), (117, 470)) # Buttons
        display1.blit(get_image('data/sprites/Customize/13.png', Vars.Opacity[10]), (401, 470))
        display1.blit(get_image('data/sprites/Customize/13.png', Vars.Opacity[10]), (685, 470))
        display1.blit(get_image('data/sprites/Customize/13.png', Vars.Opacity[10]), (964, 470))

        display1.blit(get_image('data/sprites/Customize/14.png', Vars.Opacity[10]), (283, 470))
        display1.blit(get_image('data/sprites/Customize/14.png', Vars.Opacity[10]), (565, 470))
        display1.blit(get_image('data/sprites/Customize/14.png', Vars.Opacity[10]), (848, 470))
        display1.blit(get_image('data/sprites/Customize/14.png', Vars.Opacity[10]), (1126, 470))

        display1.blit(get_image(f'data/sprites/Customize/1_{Vars.FreddyAI % 10}.png', Vars.Opacity[10]), (232, 457))
        if Vars.FreddyAI > 9:
            display1.blit(get_image(f'data/sprites/Customize/1_{Vars.FreddyAI // 10}.png', Vars.Opacity[10]), (197, 457))

        display1.blit(get_image(f'data/sprites/Customize/1_{Vars.BonnyAI % 10}.png', Vars.Opacity[10]), (515, 457))
        if Vars.BonnyAI > 9:
            display1.blit(get_image(f'data/sprites/Customize/1_{Vars.BonnyAI // 10}.png', Vars.Opacity[10]), (480, 457))

        display1.blit(get_image(f'data/sprites/Customize/1_{Vars.ChicaAI % 10}.png', Vars.Opacity[10]), (797, 457))
        if Vars.ChicaAI > 9:
            display1.blit(get_image(f'data/sprites/Customize/1_{Vars.ChicaAI // 10}.png', Vars.Opacity[10]), (762, 457))

        display1.blit(get_image(f'data/sprites/Customize/1_{Vars.FoxyAI % 10}.png', Vars.Opacity[10]), (1077, 457))
        if Vars.FoxyAI > 9:
            display1.blit(get_image(f'data/sprites/Customize/1_{Vars.FoxyAI // 10}.png', Vars.Opacity[10]), (1042, 457))

        if Vars.FastNight and Vars.Radar and Vars.EndlessPower:
            display1.blit(get_image(f'data/sprites/Customize/16.png', 255), (118, 570))
        elif not Vars.FastNight and not Vars.Radar and not Vars.EndlessPower:
            pass
        else:
            display1.blit(get_image(f'data/sprites/Customize/15.png', 255), (118, 570))

        if Vars.LongNight and Vars.Aggrmode and Vars.Darkmode:
            display1.blit(get_image(f'data/sprites/Customize/18.png', 255), (118, 600))
        elif not Vars.LongNight and not Vars.Aggrmode and not Vars.Darkmode:
            pass
        else:
            display1.blit(get_image(f'data/sprites/Customize/17.png', 255), (118, 600))



class CreepyStart(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        pass


    def Update(self):
        Vars.Frames += 1
        if self.time >= 10:
            self.SwitchToScene(MainMenu())


    def Render(self, display1, display2):
        display1.blit(get_image('data/sprites/CreepyBonny.png', 255), (0, 0))
        if self.time >= 9.5:
            display1.blit(get_image('data/sprites/Eye.png', 255), (494, 176))
            display1.blit(get_image('data/sprites/Eye.png', 255), (788, 180))



class CreepyEnd(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys, display1, display2):
        pass


    def Update(self):
        Vars.Frames += 1
        if self.time > 1:
            self.Terminate()


    def Render(self, display1, display2):
        display1.blit(get_image('data/sprites/YellowBear.png', 255), (0, 0))