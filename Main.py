from Scenes import WarningScene
from Sounds import get_sound
from Animations import ResetAnimation
from ImageManager import resource_path, remove_image, screenshot
from Variables import Vars
from random import randrange
from Animatronics import Freddy, Bonny, Chica, Foxy, GoldenFreddy
from Animations import InitializeAnimations
from Events import ClearEvents
import pygame
import pygame_shaders
import gc


#ProcessInput — этот метод получит все события, произошедшие с момента последнего кадра.
#Update - Разместите здесь свою игровую логику для сцены.
#Render — поместите сюда свой код рендеринга. Он будет получать в качестве входных данных поверхность главного экрана.


def run_game(width, height, fps, starting_scene, mode):
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height), flags=mode)
    display1 = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)
    display2 = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)
    screen_shader1 = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, pygame_shaders.DEFAULT_FRAGMENT_SHADER, display1)
    screen_shader2 = pygame_shaders.Shader(pygame_shaders.DEFAULT_VERTEX_SHADER, resource_path("data/fragment.glsl"), display2)
    InitializeAnimations()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN])
    my_font = pygame.font.SysFont('Comic Sans MS', 20)

    is_fullscreen = True

    active_scene = starting_scene
    active_scene.start_time = pygame.time.get_ticks()

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()
        tick_time = clock.tick(fps)
        Vars.dTime =  1 / (clock.get_fps() + 1)

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
                if event.key == pygame.K_RETURN and alt_pressed:
                    is_fullscreen = not is_fullscreen
                    if is_fullscreen: screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
                    else: screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
                if event.key == pygame.K_F2 and not type(active_scene).__name__ == 'EasterEgg':
                    active_scene.SwitchToScene(WarningScene())
            if event.type == pygame.MOUSEMOTION:
                Vars.CursorPos = event.pos
                Vars.CursorPosX = Vars.CursorPos[0]
                Vars.CursorPosY = Vars.CursorPos[1]

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.time = (pygame.time.get_ticks() - active_scene.start_time) / 1000
        active_scene.ProcessInput(filtered_events, pressed_keys, display1, display2)
        active_scene.Update()
        screen_shader1.clear((0, 0, 0, 0))
        screen_shader2.clear((0, 0, 0, 0))
        active_scene.Render(display1, display2)

        if active_scene.next != active_scene:
            ClearEvents()
            if type(active_scene.next).__name__ == 'WarningScene':
                Vars.Frames = 0
                Vars.Opacity[3] = 0
                Vars.Opacity[11] = 0
                remove_image('data/sprites/Screen/screenshot_1.png')
                remove_image('data/sprites/Screen/screenshot_2.png')
                screenshot(display1, 1)
                screenshot(display2, 2)
            elif type(active_scene.next).__name__ == 'CreepyStart':
                Vars.Frames = 0
            elif type(active_scene.next).__name__ == 'MainMenu':
                Vars.Frames = 0
                Vars.RandomNum = 0
                Vars.Visibility = 0
                Vars.Y1 = -33
                Vars.Opacity[0] = 255
                Vars.Opacity[1] = 255
                Vars.Opacity[2] = 0
                Vars.Extra = False
                Vars.CheatsOption = False
                Vars.DMOption = False
                Vars.OptionNumber1 = 0
                Vars.OptionNumber2 = 0
                Vars.OptionNumber3 = 0
                Vars.OptionNumber4 = 0
                Vars.OptionNumber5 = 0
                pygame.mixer.stop()
                get_sound(0).play(-1)
                get_sound(1).play()
                ResetAnimation([0, 1])
                if Vars.Night < 1: Vars.Night = 1
                elif Vars.Night > 5: Vars.Night = 5
                if Vars.Night > 1: Vars.OptionNumber = 1
                else: Vars.OptionNumber = 0
            elif type(active_scene.next).__name__ == 'NewspaperScene':
                Vars.Night = 1
                remove_image('data/sprites/Screen/screenshot_1.png')
                screenshot(display1, 1)
                Vars.Frames = 0
                Vars.Opacity[4] = 0
                Vars.Opacity[5] = 0
            elif type(active_scene.next).__name__ == 'LoadingScene':
                Vars.Frames = 0
                Vars.Opacity[6] = 255
                pygame.mixer.stop()
                ResetAnimation([2])
            elif type(active_scene.next).__name__ == 'Nightshift':
                Vars.Frames = 0
                Vars.X1 = 0
                Vars.X2 = 0
                Vars.IndicatorX2 = 0
                Vars.IntervalX2 = 0
                Vars.Power = 999 # 999
                Vars.Usage = 1
                if Vars.FastNight:
                    Vars.HourLength = 45 # 45
                elif Vars.LongNight:
                    Vars.HourLength = 135 # 135
                    Vars.Power = 1499 # 1499
                else:
                    Vars.HourLength = 90 # 90
                Vars.Hour = 0
                Vars.RandomForPic = randrange(0, 100) + 1
                Vars.PowerDown = False
                Vars.CallIsMuted = False
                Vars.ControlRoom = [False, False, False, False, False]
                Vars.LeftDoorIsClosed = False
                Vars.LeftLightIsOn = False
                Vars.RightDoorIsClosed = False
                Vars.RightLightIsOn = False
                Vars.LeftDoorIsMoving = False
                Vars.RightDoorIsMoving = False
                Vars.LeftButtonsAreBroken = False
                Vars.RightButtonsAreBroken = False
                Vars.CameraIsOn = False
                Vars.TabletIsUsing = False
                Vars.TabletIsMoving = False
                Vars.AbleToUseTablet = True
                Vars.Camera = {'1a': True, '1b': False, '1c': False, '2a': False, '2b': False, '3': False,
                                    '4a': False, '4b': False, '5': False, '6': False, '7': False}
                Vars.FreddyPosition = '1a'
                Vars.BonnyPosition = '1a'
                Vars.ChicaPosition = '1a'
                Vars.FoxyPosition = 0
                Vars.FreddyVars = [0, 0, 0]
                Vars.BonnyVars = [1, 0, 1, 0]
                Vars.ChicaVars = [1, 0, 1, 0]
                Vars.FoxyVars = [0, 0, 0, 0, 0]
                Vars.GoldenFreddyVars = [0, 0, 0, 0]
                Vars.HallucinationVars = [0, 0, 0, 0]
                Vars.JumpscareVars = [10, 40]
                Vars.NoSignalVars = [0, 0]
                Vars.PowerDownVars = [0, 0, 0, 0]
                Vars.ReadyToJumpscare = False
                Vars.FreddyJumpscare = False
                Vars.BonnyJumpscare = False
                Vars.ChicaJumpscare = False
                Vars.FoxyJumpscare = False
                Freddy.Reset()
                Bonny.Reset()
                Chica.Reset()
                Foxy.Reset()
                GoldenFreddy.Reset()

                Freddy.CheckInterval()
                Bonny.CheckInterval()
                Chica.CheckInterval()
                Foxy.CheckInterval()

                if Vars.Night == 1:
                    Vars.FreddyActivity = 0
                    Vars.BonnyActivity = 0
                    Vars.ChicaActivity = 0
                    Vars.FoxyActivity = 0
                    get_sound(41).set_volume(1)
                    get_sound(41).play(0)
                if Vars.Night == 2:
                    Vars.FreddyActivity = 0
                    Vars.BonnyActivity = 3
                    Vars.ChicaActivity = 1
                    Vars.FoxyActivity = 1
                    get_sound(42).set_volume(1)
                    get_sound(42).play(0)
                if Vars.Night == 3:
                    Vars.FreddyActivity = 1
                    Vars.BonnyActivity = 0
                    Vars.ChicaActivity = 5
                    Vars.FoxyActivity = 2
                    get_sound(43).set_volume(1)
                    get_sound(43).play(0)
                if Vars.Night == 4:
                    Vars.FreddyActivity = randrange(0, 2) + 1
                    Vars.BonnyActivity = 2
                    Vars.ChicaActivity = 4
                    Vars.FoxyActivity = 6
                    get_sound(44).set_volume(1)
                    get_sound(44).play(0)
                if Vars.Night == 5:
                    Vars.FreddyActivity = 3
                    Vars.BonnyActivity = 5
                    Vars.ChicaActivity = 7
                    Vars.FoxyActivity = 5
                    get_sound(45).set_volume(1)
                    get_sound(45).play(0)
                if Vars.Night == 6:
                    Vars.FreddyActivity = 4
                    Vars.BonnyActivity = 10
                    Vars.ChicaActivity = 12
                    Vars.FoxyActivity = 6
                if Vars.Night == 7:
                    Vars.FreddyActivity = Vars.FreddyAI
                    Vars.BonnyActivity = Vars.BonnyAI
                    Vars.ChicaActivity = Vars.ChicaAI
                    Vars.FoxyActivity = Vars.FoxyAI

                ResetAnimation([8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23])
                get_sound(3).set_volume(0)
                get_sound(3).play(-1)
                get_sound(7).set_volume(0.05)
                get_sound(13).set_volume(0.25)
                get_sound(13).play(-1)
                get_sound(14).set_volume(0.5)
                get_sound(14).play(-1)
                get_sound(15).set_volume(0.05)
                get_sound(18).play(-1)
                get_sound(35).set_volume(0)
                get_sound(35).play(-1)
                get_sound(46).set_volume(0.5)
                get_sound(47).set_volume(0.5)
                get_sound(48).set_volume(0.5)
                get_sound(49).set_volume(0.5)
                get_sound(50).set_volume(1)
                get_sound(51).set_volume(0.5)
            elif type(active_scene.next).__name__ == 'Gameover':
                Vars.Frames = 0
                Vars.Opacity[12] = 255
                pygame.mixer.stop()
                get_sound(22).play(0)
                ResetAnimation([21, 22])
            elif type(active_scene.next).__name__ == 'NextDay':
                Vars.Frames = 0
                Vars.Opacity[7] = 0
                Vars.Opacity[8] = 0
                Vars.Y2 = 0
                Vars.Night += 1
                if Vars.Night == 6:
                    Vars.BeatGame = True
                elif Vars.Night == 7:
                    Vars.Beat6 = True
                elif Vars.Night == 8 and Vars.FreddyAI == 20 and Vars.BonnyAI == 20 and \
                Vars.ChicaAI == 20 and Vars.FoxyAI == 20:
                    if Vars.LongNight and Vars.Aggrmode and Vars.Darkmode:
                        Vars.Beat7 = True
                        Vars.BeatHardMode = True
                    else:
                        Vars.Beat7 = True
                remove_image('data/sprites/Screen/screenshot_1.png')
                remove_image('data/sprites/Screen/screenshot_2.png')
                screenshot(display1, 1)
                screenshot(display2, 2)
                pygame.mixer.stop()
                get_sound(5).play(0)
            elif type(active_scene.next).__name__ == 'TheEnd':
                Vars.Frames = 0
                Vars.Opacity[9] = 255
                pygame.mixer.stop()
                get_sound(40).set_volume(1)
                get_sound(40).play(0)
            elif type(active_scene.next).__name__ == 'Customize':
                Vars.Frames = 0
                Vars.Opacity[10] = 0
                remove_image('data/sprites/Screen/screenshot_1.png')
                screenshot(display1, 1)
            elif type(active_scene.next).__name__ == 'CreepyEnd':
                Vars.Frames = 0
                pygame.mixer.stop()
                get_sound(8).play(0)

            gc.collect()

        active_scene = active_scene.next

        text_surface = my_font.render(str(int(clock.get_fps())), False, (255, 255, 255))
        display1.blit(text_surface, (10, 5))

        screen_shader2.render_direct(pygame.Rect(0, 0, 1280, 720))
        screen_shader1.render_direct(pygame.Rect(0, 0, 1280, 720))

        pygame.display.flip()