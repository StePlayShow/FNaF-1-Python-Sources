from Main import run_game
from Scenes import WarningScene
from pygame import OPENGL, DOUBLEBUF, FULLSCREEN, HWSURFACE
from Sounds import set_sound
from ImageManager import resource_path
from Variables import Vars
from pathlib import Path
import os
import pygame


def set_high_priority():
    from sys import getwindowsversion

    try:
        getwindowsversion()
    except AttributeError:
        iswindows = False
    else:
        iswindows = True

    if iswindows:
        from win32api import GetCurrentProcessId, OpenProcess
        from win32process import SetPriorityClass, HIGH_PRIORITY_CLASS
        from win32con import PROCESS_ALL_ACCESS

        pid = GetCurrentProcessId()
        handle = OpenProcess(PROCESS_ALL_ACCESS, True, pid)
        SetPriorityClass(handle, HIGH_PRIORITY_CLASS)
    else:
        os.nice(1)


def set_sounds():
    set_sound("data/sounds/darkness music.wav", 0)
    set_sound("data/sounds/static2.wav", 1)
    set_sound("data/sounds/blip3.wav", 2)
    set_sound("data/sounds/BallastHumMedium2.wav", 3)
    set_sound("data/sounds/SFXBible_12478.wav", 4)
    set_sound("data/sounds/chimes 2.wav", 5)
    set_sound("data/sounds/CROWD_SMALL_CHIL_EC049202.wav", 6)
    set_sound("data/sounds/pirate song2.wav", 7)
    set_sound("data/sounds/XSCREAM2.wav", 8)
    set_sound("data/sounds/PartyFavorraspyPart_AC01__3.wav", 9)
    set_sound("data/sounds/CAMERA_VIDEO_LOA_60105303.wav", 10)
    set_sound("data/sounds/put down.wav", 11)
    set_sound("data/sounds/MiniDV_Tape_Eject_1.wav", 12)
    set_sound("data/sounds/Buzz_Fan_Florescent2.wav", 13)
    set_sound("data/sounds/ColdPresc B.wav", 14)
    set_sound("data/sounds/circus.wav", 15)
    set_sound("data/sounds/DOOR_POUNDING_ME_D0291401.wav", 16)
    set_sound("data/sounds/Laugh_Giggle_Girl_1.wav", 17)
    set_sound("data/sounds/robotvoice.wav", 18)
    set_sound("data/sounds/windowscare.wav", 19)
    set_sound("data/sounds/error.wav", 20)
    set_sound("data/sounds/XSCREAM.wav", 21)
    set_sound("data/sounds/static.wav", 22)
    set_sound("data/sounds/run.wav", 23)
    set_sound("data/sounds/knock2.wav", 24)
    set_sound("data/sounds/deep steps.wav", 25)
    set_sound("data/sounds/COMPUTER_DIGITAL_L2076505.wav", 26)
    set_sound("data/sounds/garble1.wav", 27)
    set_sound("data/sounds/garble2.wav", 28)
    set_sound("data/sounds/garble3.wav", 29)
    set_sound("data/sounds/Laugh_Giggle_Girl_1d.wav", 30)
    set_sound("data/sounds/Laugh_Giggle_Girl_2d.wav", 31)
    set_sound("data/sounds/Laugh_Giggle_Girl_8d.wav", 32)
    set_sound("data/sounds/running fast3.wav", 33)
    set_sound("data/sounds/whispering2.wav", 34)
    set_sound("data/sounds/EerieAmbienceLargeSca_MV005.wav", 35)
    set_sound("data/sounds/OVEN-DRA_1_GEN-HDF18119.wav", 36)
    set_sound("data/sounds/OVEN-DRA_2_GEN-HDF18120.wav", 37)
    set_sound("data/sounds/OVEN-DRA_7_GEN-HDF18121.wav", 38)
    set_sound("data/sounds/OVEN-DRAWE_GEN-HDF18122.wav", 39)
    set_sound("data/sounds/music box.wav", 40)
    set_sound("data/sounds/voiceover1c.wav", 41)
    set_sound("data/sounds/voiceover2a.wav", 42)
    set_sound("data/sounds/voiceover3.wav", 43)
    set_sound("data/sounds/voiceover4.wav", 44)
    set_sound("data/sounds/voiceover5.wav", 45)
    set_sound("data/sounds/Vocals_Breaths_S_35972006.wav", 46)
    set_sound("data/sounds/Vocals_Breaths_S_35972008.wav", 47)
    set_sound("data/sounds/Vocals_Breaths_S_35972012.wav", 48)
    set_sound("data/sounds/Vocals_Breaths_S_35972014.wav", 49)
    set_sound("data/sounds/powerdown.wav", 50)
    set_sound("data/sounds/ambience2.wav", 51)


def main():
    set_high_priority()
    set_sounds()
    pygame.mixer.set_num_channels(32)

    run_game(1280, 720, 60, WarningScene(), OPENGL | DOUBLEBUF | HWSURFACE | FULLSCREEN)

    Path(os.path.join(os.getenv('APPDATA'), 'fnaf python')).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(os.getenv('APPDATA'), "fnaf python\\freddy.txt"), "w+") as File:
        if Vars.Night >= 5:
            File.write(f"5\n{Vars.BeatGame}\n{Vars.Beat6}\n{Vars.Beat7}\n{Vars.BeatHardMode}")
        elif Vars.Night <= 0:
            File.write(f"1\n{Vars.BeatGame}\n{Vars.Beat6}\n{Vars.Beat7}\n{Vars.BeatHardMode}")
        else:
            File.write(f"{Vars.Night}\n{Vars.BeatGame}\n{Vars.Beat6}\n{Vars.Beat7}\n{Vars.BeatHardMode}")
    pygame.quit()

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    pygame.display.set_icon(pygame.image.load(resource_path('data/sprites/icon.png')))
    pygame.display.set_caption('FNaF Python')

    if os.path.isfile(os.path.join(os.getenv('APPDATA'), "fnaf python\\freddy.txt")):
        with open(os.path.join(os.getenv('APPDATA'), "fnaf python\\freddy.txt"), "r") as file:
            data = []
            for i in file:
                data.append(i.replace("\n",""))
            try:
                Vars.Night = int(data[0])
                if data[1] == 'False': Vars.BeatGame = False
                else: Vars.BeatGame = True
                if data[2] == 'False': Vars.Beat6 = False
                else: Vars.Beat6 = True
                if data[3] == 'False': Vars.Beat7 = False
                else: Vars.Beat7 = True
                if data[4] == 'False': Vars.BeatHardMode = False
                else: Vars.BeatHardMode = True
            except IndexError:
                pass
            if Vars.Night >= 6: Vars.Night = 5
            if Vars.Night <= 0: Vars.Night = 1

    if os.path.isfile(resource_path("data/sprites/Screen/screenshot_1.png")):
        os.remove(resource_path("data/sprites/Screen/screenshot_1.png"))

    if os.path.isfile(resource_path("data/sprites/Screen/screenshot_2.png")):
        os.remove(resource_path("data/sprites/Screen/screenshot_2.png"))

    main()