from Variables import Vars
from random import randrange
from Sounds import get_sound
from Animations import ResetAnimation
from pygame import SurfaceType
from ImageManager import get_image

class Freddy:
    _INTERVAL = 3.02
    _start_interval = None
    _time = None

    @staticmethod
    def CheckInterval():
        if Vars.Aggrmode:
            Freddy._INTERVAL = 1.51
        else:
            Freddy._INTERVAL = 3.02

    @staticmethod
    def Reset():
        Freddy._start_interval = None
        Freddy._time = None

    @staticmethod
    def DisplayLocation(display: SurfaceType):
        if Vars.FreddyPosition == '1a':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1014, 361))
        elif Vars.FreddyPosition == '1b':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1014, 452))
        elif Vars.FreddyPosition == '7':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1202, 447))
        elif Vars.FreddyPosition == '6':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1127, 582))
        elif Vars.FreddyPosition == '4a':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1081, 568))
        elif Vars.FreddyPosition == '4b':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1081, 650))
        elif Vars.FreddyPosition == 'office':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Freddy.png', 255), (1015, 657))

    @staticmethod
    def CheckMovement(time: float):
        Freddy._time = time
        if Freddy._start_interval is None:
            Freddy._start_interval = time
        if Freddy._time - Freddy._start_interval >= Freddy._INTERVAL:
            Freddy._start_interval = time
            if randrange(20) + 1 <= Vars.FreddyActivity and not Vars.CameraIsOn:
                Vars.FreddyVars[0] = 1

        if Vars.FreddyVars[0] == 1:
            Vars.FreddyVars[1] += 60 * Vars.dTime

        if Vars.CameraIsOn and Vars.FreddyPosition != 'office' and Vars.Camera[Vars.FreddyPosition]:
            Vars.FreddyVars[1] = 0

        if Vars.FreddyVars[0] == 1 and Vars.FreddyVars[1] >= 1000-(Vars.FreddyActivity * 100) and \
        not Vars.CameraIsOn:
            Vars.FreddyVars[0] = 2
            Vars.FreddyVars[1] = 0


        if Vars.FreddyVars[0] == 2:
            if Vars.FreddyPosition == '1a' and Vars.BonnyPosition != '1a' and Vars.ChicaPosition != '1a':
                Vars.FreddyPosition = '1b'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.15)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.15)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.15)
                        get_sound(32).play(0)
                get_sound(33).set_volume(0.3)
                get_sound(33).play(0)
            elif Vars.FreddyPosition == '1b':
                Vars.FreddyPosition = '7'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.2)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.2)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.2)
                        get_sound(32).play(0)
                get_sound(33).set_volume(0.35)
                get_sound(33).play(0)
            elif Vars.FreddyPosition == '7':
                Vars.FreddyPosition = '6'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.3)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.3)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.3)
                        get_sound(32).play(0)
                get_sound(33).set_volume(0.4)
                get_sound(33).play(0)
                get_sound(40).play(-1)
            elif Vars.FreddyPosition == '6':
                Vars.FreddyPosition = '4a'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.4)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.4)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.4)
                        get_sound(32).play(0)
                get_sound(33).set_volume(0.6)
                get_sound(33).play(0)
                get_sound(40).stop()
            elif Vars.FreddyPosition == '4a':
                Vars.FreddyPosition = '4b'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.6)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.6)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.6)
                        get_sound(32).play(0)
                get_sound(33).set_volume(0.75)
                get_sound(33).play(0)

        if Vars.FreddyVars[0] == 2 and Vars.CameraIsOn and Vars.FreddyPosition == '4b':
            if not(Vars.Camera['4b']) and not Vars.RightDoorIsClosed:
                Vars.FreddyPosition = 'office'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.8)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.8)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.8)
                        get_sound(32).play(0)
                get_sound(33).set_volume(1)
                get_sound(33).play(0)
                get_sound(34).play(0)
            elif not(Vars.Camera['4b']) and not(Vars.Camera['4a']) and Vars.RightDoorIsClosed:
                Vars.FreddyPosition = '4a'
                Vars.FreddyVars[0] = 0
                match randrange(0, 3) + 1:
                    case 1:
                        get_sound(30).set_volume(0.6)
                        get_sound(30).play(0)
                    case 2:
                        get_sound(31).set_volume(0.6)
                        get_sound(31).play(0)
                    case 3:
                        get_sound(32).set_volume(0.6)
                        get_sound(32).play(0)
                get_sound(33).set_volume(0.75)
                get_sound(33).play(0)




class Bonny:
    _INTERVAL = 4.97
    _start_interval = None
    _time = None

    @staticmethod
    def CheckInterval():
        if Vars.Aggrmode:
            Bonny._INTERVAL = 3.2305
        else:
            Bonny._INTERVAL = 4.97

    @staticmethod
    def Reset():
        Bonny._start_interval = None
        Bonny._time = None

    @staticmethod
    def DisplayLocation(display: SurfaceType):
        if Vars.BonnyPosition == '1a':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (982, 361))
        elif Vars.BonnyPosition == '1b':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (982, 452))
        elif Vars.BonnyPosition == '5':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (864, 396))
        elif Vars.BonnyPosition == '2a':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (962, 568))
        elif Vars.BonnyPosition == '2b':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (962, 650))
        elif Vars.BonnyPosition == '3':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (910, 582))
        elif Vars.BonnyPosition == 'door':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (989, 638))
        elif Vars.BonnyPosition == 'office':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Bonny.png', 255), (1015, 621))

    @staticmethod
    def CheckMovement(time: float):
        Bonny._time = time
        if Bonny._start_interval is None:
            Bonny._start_interval = time
        if Bonny._time - Bonny._start_interval >= Bonny._INTERVAL:
            Bonny._start_interval = time
            if randrange(20) + 1 <= Vars.BonnyActivity:
                Vars.BonnyVars[1] = 10
                Vars.BonnyVars[2] = randrange(0, 2) + 1
                if Vars.BonnyPosition != 'door' and Vars.BonnyPosition != 'office' and Vars.CameraIsOn and Vars.Camera[Vars.BonnyPosition]:
                    Vars.NoSignalVars[0] = 1
                    Vars.NoSignalVars[1] = 300
                    Vars.BonnyVars[1] = 0
                    ResetAnimation([11])
                    match randrange(0, 4) + 1:
                        case 1: get_sound(26).play(0)
                        case 2: get_sound(27).play(0)
                        case 3: get_sound(28).play(0)
                        case 4: get_sound(29).play(0)

                if Vars.BonnyPosition == '1a':
                    if Vars.BonnyVars[0] == 1:
                        Vars.BonnyPosition = '5'
                    elif Vars.BonnyVars[0] == 2:
                        Vars.BonnyPosition = '1b'
                    if not Vars.Camera[Vars.BonnyPosition]:
                        get_sound(25).set_volume(0.1)
                        get_sound(25).play(0)
                elif Vars.BonnyPosition == '1b':
                    if Vars.BonnyVars[0] == 1:
                        Vars.BonnyPosition = '5'
                    elif Vars.BonnyVars[0] == 2:
                        Vars.BonnyPosition = '2a'
                    if not Vars.Camera[Vars.BonnyPosition]:
                        get_sound(25).set_volume(0.2)
                        get_sound(25).play(0)
                elif Vars.BonnyPosition == '5':
                    if Vars.BonnyVars[0] == 1:
                        Vars.BonnyPosition = '1b'
                    elif Vars.BonnyVars[0] == 2:
                        Vars.BonnyPosition = '2a'
                    if not Vars.Camera[Vars.BonnyPosition]:
                        get_sound(25).set_volume(0.1)
                        get_sound(25).play(0)
                elif Vars.BonnyPosition == '2a':
                    if Vars.BonnyVars[0] == 1:
                        Vars.BonnyPosition = '3'
                    elif Vars.BonnyVars[0] == 2:
                        Vars.BonnyPosition = '2b'
                    if not Vars.Camera[Vars.BonnyPosition]:
                        get_sound(25).set_volume(0.3)
                        get_sound(25).play(0)
                elif Vars.BonnyPosition == '3':
                    if Vars.BonnyVars[0] == 1:
                        Vars.BonnyPosition = 'door'
                        Vars.LeftLightIsOn = False
                        get_sound(25).set_volume(0.3)
                        get_sound(25).play(0)
                    elif Vars.BonnyVars[0] == 2:
                        Vars.BonnyPosition = '2a'
                        if not Vars.Camera[Vars.BonnyPosition]:
                            get_sound(25).set_volume(0.3)
                            get_sound(25).play(0)
                elif Vars.BonnyPosition == '2b':
                    if Vars.BonnyVars[0] == 1:
                        Vars.BonnyPosition = '3'
                        if not Vars.Camera[Vars.BonnyPosition]:
                            get_sound(25).set_volume(0.4)
                            get_sound(25).play(0)
                    elif Vars.BonnyVars[0] == 2:
                        Vars.BonnyPosition = 'door'
                        Vars.LeftLightIsOn = False
                        get_sound(25).set_volume(0.4)
                        get_sound(25).play(0)
                elif Vars.BonnyPosition == 'door':
                    if not Vars.LeftDoorIsClosed:
                        Vars.BonnyPosition = 'office'
                        Vars.LeftButtonsAreBroken = True
                        Vars.LeftLightIsOn = False
                    elif Vars.LeftDoorIsClosed:
                        Vars.BonnyPosition = '1b'
                        Vars.LeftLightIsOn = False
                        if not Vars.Camera[Vars.BonnyPosition]:
                            get_sound(25).set_volume(0.3)
                            get_sound(25).play(0)

                if Vars.BonnyPosition != 'door' and Vars.BonnyPosition != 'office' and Vars.CameraIsOn and \
                   Vars.Camera[Vars.BonnyPosition] and Vars.BonnyVars[1] > 0:
                    Vars.NoSignalVars[0] = 1
                    Vars.NoSignalVars[1] = 300
                    Vars.BonnyVars[1] = 0
                    ResetAnimation([11])
                    match randrange(0, 4) + 1:
                        case 1: get_sound(26).play(0)
                        case 2: get_sound(27).play(0)
                        case 3: get_sound(28).play(0)
                        case 4: get_sound(29).play(0)


class Chica:
    _INTERVAL = 4.98
    _start_interval = None
    _time = None

    @staticmethod
    def CheckInterval():
        if Vars.Aggrmode:
            Chica._INTERVAL = 3.237
        else:
            Chica._INTERVAL = 4.98

    @staticmethod
    def Reset():
        Chica._start_interval = None
        Chica._time = None

    @staticmethod
    def DisplayLocation(display: SurfaceType):
        if Vars.ChicaPosition == '1a':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1046, 361))
        elif Vars.ChicaPosition == '1b':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1046, 452))
        elif Vars.ChicaPosition == '7':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1162, 462))
        elif Vars.ChicaPosition == '6':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1127, 552))
        elif Vars.ChicaPosition == '4a':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1066, 568))
        elif Vars.ChicaPosition == '4b':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1066, 650))
        elif Vars.ChicaPosition == 'door':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1041, 638))
        elif Vars.ChicaPosition == 'office':
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Chica.png', 255), (1015, 621))

    @staticmethod
    def CheckMovement(time: float):
        Chica._time = time
        if Chica._start_interval is None:
            Chica._start_interval = time
        if Chica._time - Chica._start_interval >= Chica._INTERVAL:
            Chica._start_interval = time
            if randrange(20) + 1 <= Vars.ChicaActivity:
                Vars.ChicaVars[1] = 10
                Vars.ChicaVars[2] = randrange(0, 2) + 1
                if Vars.ChicaPosition != 'door' and Vars.ChicaPosition != 'office' and Vars.CameraIsOn and Vars.Camera[Vars.ChicaPosition]:
                    Vars.NoSignalVars[0] = 1
                    Vars.NoSignalVars[1] = 300
                    Vars.ChicaVars[1] = 0
                    ResetAnimation([11])
                    match randrange(0, 4)+1:
                        case 1: get_sound(26).play(0)
                        case 2: get_sound(27).play(0)
                        case 3: get_sound(28).play(0)
                        case 4: get_sound(29).play(0)


                if Vars.ChicaPosition == '1a':
                    Vars.ChicaPosition = '1b'
                    if not Vars.Camera[Vars.ChicaPosition]:
                        get_sound(25).set_volume(0.1)
                        get_sound(25).play(0)
                elif Vars.ChicaPosition == '1b':
                    if Vars.ChicaVars[0] == 1:
                        Vars.ChicaPosition = '7'
                    elif Vars.ChicaVars[0] == 2:
                        Vars.ChicaPosition = '6'
                    if not Vars.Camera[Vars.ChicaPosition]:
                        get_sound(25).set_volume(0.1)
                        get_sound(25).play(0)
                elif Vars.ChicaPosition == '6':
                    if Vars.ChicaVars[0] == 1:
                        Vars.ChicaPosition = '7'
                        if not Vars.Camera[Vars.ChicaPosition]:
                            get_sound(25).set_volume(0.1)
                            get_sound(25).play(0)
                    elif Vars.ChicaVars[0] == 2:
                        Vars.ChicaPosition = '4a'
                        if not Vars.Camera[Vars.ChicaPosition]:
                            get_sound(25).set_volume(0.2)
                            get_sound(25).play(0)
                elif Vars.ChicaPosition == '7':
                    if Vars.ChicaVars[0] == 1:
                        Vars.ChicaPosition = '6'
                    elif Vars.ChicaVars[0] == 2:
                        Vars.ChicaPosition = '4a'
                    if not Vars.Camera[Vars.ChicaPosition]:
                        get_sound(25).set_volume(0.2)
                        get_sound(25).play(0)
                elif Vars.ChicaPosition == '4a':
                    if Vars.ChicaVars[0] == 1:
                        Vars.ChicaPosition = '1b'
                    elif Vars.ChicaVars[0] == 2:
                        Vars.ChicaPosition = '4b'
                    if not Vars.Camera[Vars.ChicaPosition]:
                        get_sound(25).set_volume(0.3)
                        get_sound(25).play(0)
                elif Vars.ChicaPosition == '4b':
                    if Vars.ChicaVars[0] == 1:
                        Vars.ChicaPosition = '4a'
                        if not Vars.Camera[Vars.ChicaPosition]:
                            get_sound(25).set_volume(0.4)
                            get_sound(25).play(0)
                    elif Vars.ChicaVars[0] == 2:
                        Vars.ChicaPosition = 'door'
                        Vars.RightLightIsOn = False
                        get_sound(25).set_volume(0.4)
                        get_sound(25).play(0)
                elif Vars.ChicaPosition == 'door':
                    if not Vars.RightDoorIsClosed:
                        Vars.ChicaPosition = 'office'
                        Vars.RightButtonsAreBroken = True
                        Vars.RightLightIsOn = False
                    elif Vars.RightDoorIsClosed:
                        Vars.ChicaPosition = '4a'
                        Vars.RightLightIsOn = False
                        if not Vars.Camera[Vars.ChicaPosition]:
                            get_sound(25).set_volume(0.4)
                            get_sound(25).play(0)

                if Vars.ChicaPosition != 'door' and Vars.ChicaPosition != 'office' and Vars.CameraIsOn and \
                   Vars.Camera[Vars.ChicaPosition] and Vars.ChicaVars[1] > 0:
                    Vars.NoSignalVars[0] = 1
                    Vars.NoSignalVars[1] = 300
                    Vars.ChicaVars[1] = 0
                    ResetAnimation([11])
                    match randrange(0, 4) + 1:
                        case 1: get_sound(26).play(0)
                        case 2: get_sound(27).play(0)
                        case 3: get_sound(28).play(0)
                        case 4: get_sound(29).play(0)


class Foxy:
    _INTERVAL = 5.01
    _start_interval = None
    _time = None

    @staticmethod
    def CheckInterval():
        if Vars.Aggrmode:
            Foxy._INTERVAL = 2.505
        else:
            Foxy._INTERVAL = 5.01

    @staticmethod
    def Reset():
        Foxy._start_interval = None
        Foxy._time = None

    @staticmethod
    def DisplayLocation(display: SurfaceType):
        if Vars.FoxyPosition == 0:
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Foxy.png', 255), (878, 487))
        elif Vars.FoxyPosition == 1:
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Foxy.png', 255), (897, 487))
        elif Vars.FoxyPosition == 2:
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Foxy.png', 255), (922, 502))
        elif Vars.FoxyPosition == 3:
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Foxy.png', 255), (962, 502))
        elif Vars.FoxyPosition == 4:
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Foxy.png', 255), (962, 549))
        elif Vars.FoxyPosition == 5:
            display.blit(get_image('data/sprites/Nightshift/Camera/Elements/Foxy.png', 255), (998, 638))

    @staticmethod
    def CheckMovement(time: float):
        Foxy._time = time
        if Foxy._start_interval is None:
            Foxy._start_interval = time
        if Foxy._time - Foxy._start_interval >= Foxy._INTERVAL and Vars.FoxyPosition < 3:
            Foxy._start_interval = time
            if randrange(20) + 1 <= Vars.FoxyActivity and Vars.FoxyVars[2] <= 0:
                Vars.FoxyPosition += 1
        if Vars.FoxyPosition == 3:
            Vars.FoxyVars[1] += 60 * Vars.dTime
        if Vars.FoxyPosition == 3 and Vars.CameraIsOn and Vars.Camera['2a']:
            ResetAnimation([15])
            Vars.FoxyPosition = 4
            get_sound(23).play(0)
        elif Vars.FoxyPosition == 4:
            Vars.FoxyVars[0] += 60 * Vars.dTime
        if ((Vars.FoxyVars[1] > 1500 and Vars.FoxyPosition == 3) or (Vars.FoxyVars[0] > 100 and Vars.FoxyPosition == 4)) and not Vars.PowerDown:
            Vars.FoxyPosition = 5
            Vars.FoxyVars[0] = 0
            Vars.FoxyVars[1] = 0
            if Vars.CameraIsOn:
                ResetAnimation([9])
                Vars.RandomForPic = randrange(0, 100) + 1
                Vars.TabletIsMoving = True
                Vars.TabletIsUsing = False
                Vars.CameraIsOn = False
                Vars.AntiRepeat2 = True
                get_sound(2).stop()
                get_sound(10).stop()
                get_sound(12).stop()
                get_sound(11).play(0)

            if not Vars.CameraIsOn:
                if not Vars.LeftDoorIsClosed:
                    Vars.FoxyJumpscare = True
                    get_sound(21).play(0)
                elif Vars.LeftDoorIsClosed:
                    Vars.FoxyPosition = randrange(0, 2)
                    Vars.Power -= 10 + (Vars.FoxyVars[4] * 50)
                    Vars.FoxyVars[4] += 1
                    get_sound(24).play(0)


class GoldenFreddy:
    _INTERVAL = 5
    _start_interval = None
    _time = None

    @staticmethod
    def Reset():
        GoldenFreddy._start_interval = None
        GoldenFreddy._time = None

    @staticmethod
    def CheckMovement(time: float):
        GoldenFreddy._time = time
        if Vars.GoldenFreddyVars[0] == 2 and not Vars.CameraIsOn:
            if GoldenFreddy._start_interval is None:
                GoldenFreddy._start_interval = time
            if GoldenFreddy._time - GoldenFreddy._start_interval >= GoldenFreddy._INTERVAL:
                Vars.GoldenFreddyVars[2] = 2