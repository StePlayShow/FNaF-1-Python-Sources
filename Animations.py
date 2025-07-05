from pygame.image import load
from pygame.transform import scale
from pygame import SurfaceType
from ImageManager import resource_path
import time

_animation0 = ()
_animation1 = ()
_animation2 = ()
_animation3 = ()
_animation4 = ()
_animation5 = ()
_animation6 = ()
_animation7 = ()
_animation8 = ()
_animation9 = ()
_animation10 = ()
_animation11 = ()
_animation12 = ()
_animation13 = ()
_animation14 = ()
_animation15 = ()
_animation16 = ()
_animation17 = ()
_animation18 = ()
_animation19 = ()
_animation20 = ()
_animation21 = ()
_animation22 = ()
_animation23 = ()
_animations = ()
_intervals = ()
_frameCounts = []
_start_interval = []
_is_on = []

def InitializeAnimations():
    global _animation0, _animation1, _animation2, _animation3, _animation4, _animation5,\
    _animation6, _animation7, _animation8, _animation9, _animation10, _animation11,\
    _animation12, _animation13, _animation14, _animation15, _animation16, _animation17,\
    _animation18, _animation19, _animation20, _animation21, _animation22, _animation23, \
    _animations, _intervals, _frameCounts, _start_interval, _is_on

    _animation0 = tuple(
        load(resource_path(f"data/sprites/MainMenu/{i}.png")).convert_alpha() for i in range(6, 14)
    )
    _animation1 = tuple(
        load(resource_path(f"data/sprites/MainMenu/{i}.png")).convert_alpha() for i in range(14, 22)
    )
    _animation2 = tuple(
        load(resource_path(f"data/sprites/LoadingScene/{i}.png")).convert_alpha() for i in range(9, 20)
    )
    _animation3 = tuple(
        load(resource_path(f"data/sprites/Nightshift/LeftDoor/1_{i}.png")).convert_alpha() for i in range(1, 17)
    )
    _animation4 = tuple(
        load(resource_path(f"data/sprites/Nightshift/LeftDoor/2_{i}.png")).convert_alpha() for i in range(1, 17)
    )
    _animation5 = tuple(
        load(resource_path(f"data/sprites/Nightshift/RightDoor/1_{i}.png")).convert_alpha() for i in range(1, 17)
    )
    _animation6 = tuple(
        load(resource_path(f"data/sprites/Nightshift/RightDoor/2_{i}.png")).convert_alpha() for i in range(1, 17)
    )
    _animation7 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Fen/{i}.png")).convert_alpha() for i in range(1, 4)
    )
    _animation8 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Tablet/1_{i}.png")).convert_alpha() for i in range(1, 12)
    )
    _animation9 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Tablet/2_{i}.png")).convert_alpha() for i in range(1, 12)
    )
    _animation10 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Camera/Elements/2_{i}.png")).convert_alpha() for i in range(1, 9)
    )
    _animation11 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Camera/Elements/3_{i}.png")).convert_alpha() for i in range(1, 10)
    )
    _animation12 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Camera/Elements/4_{i}.png")).convert_alpha() for i in range(1, 3)
    )
    _animation13 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Camera/Elements/5_{i}.png")).convert_alpha() for i in range(1, 3)
    )
    _animation14 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Camera/Elements/8_{i}.png")).convert_alpha() for i in range(1, 3)
    )
    _animation15 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Camera/2a_4_{i}.png")).convert_alpha() for i in range(1, 34)
    )
    _animation16 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Hallucination/{i}.png")).convert_alpha() for i in range(1, 5)
    )
    _animation17 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Jumpscares/1_{i}.png")).convert_alpha() for i in range(1, 12)
    )
    _animation18 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Jumpscares/2_{i}.png")).convert_alpha() for i in range(1, 17)
    )
    _animation19 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Jumpscares/3_{i}.png")).convert_alpha() for i in range(1, 26)
    )
    _animation20 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Jumpscares/4_{i}.png")).convert_alpha() for i in range(1, 32)
    )
    _animation21 = tuple(
        load(resource_path(f"data/sprites/Gameover/1_{i}.png")).convert_alpha() for i in range(1, 12)
    )
    _animation22 = tuple(
        load(resource_path(f"data/sprites/Gameover/2_{i}.png")).convert_alpha() for i in range(1, 9)
    )
    _animation23 = tuple(
        load(resource_path(f"data/sprites/Nightshift/Jumpscares/5_{i}.png")).convert_alpha() for i in range(1, 22)
    )

    _animations = (_animation0, _animation1, _animation2, _animation3, _animation4, _animation5, _animation6, _animation7,
                   _animation8, _animation9, _animation10, _animation11, _animation12, _animation13, _animation14, _animation15, _animation16,
                   _animation17, _animation18, _animation19, _animation20, _animation21, _animation22, _animation23)
    _intervals = (166.667, 16.835, 22.222, 33.333, 33.333, 33.333, 33.333, 16.835, 22.222, 22.222, 16.667, 16.667, 833.333,
                  666.667, 916.667, 25.641, 22.222, 16.667, 16.667, 16.667, 16.667, 16.667, 16.667, 16.667)
    _frameCounts = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    _start_interval = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    _is_on = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False]
    

def PlayAnimation(animationNumber: int, alpha: int, coord: tuple[int, int], display: SurfaceType, isLoop: bool, size: tuple[int, int] = None, lastFrame: bool = False):
    animation = _animations[animationNumber]
    interval = _intervals[animationNumber]

    if _frameCounts[animationNumber] == -1:
        _start_interval[animationNumber] = time.time() * 1000
        _is_on[animationNumber] = True

    _frameCounts[animationNumber] = int((time.time() * 1000 - _start_interval[animationNumber]) // _intervals[animationNumber])

    if (time.time() * 1000 - _start_interval[animationNumber]) // _intervals[animationNumber] >= len(animation):
        if isLoop:
            _frameCounts[animationNumber] = 0
            _start_interval[animationNumber] = time.time() * 1000
        else:
            _is_on[animationNumber] = False
            if not lastFrame:
                return
            else:
                if _frameCounts[animationNumber] >= len(animation):
                    _frameCounts[animationNumber] = len(animation) - 1
    
    #if (time.time() * 1000) - _start_interval[animationNumber] >= interval:
    #    _start_interval[animationNumber] = time.time() * 1000
    #    _frameCounts[animationNumber] += 1
    
    #if _frameCounts[animationNumber] >= len(animation):
    #    if isLoop:
    #        _frameCounts[animationNumber] = 0
    #    else:
    #        _is_on[animationNumber] = False
    #        return

    image = animation[_frameCounts[animationNumber]]
    if size is not None:
        image = scale(image, size)
    image.set_alpha(alpha)
    display.blit(image, coord)


def ResetAnimation(animationNumbers: list[int]):
    for animationNumber in animationNumbers:
        _frameCounts[animationNumber] = -1
        _start_interval[animationNumber] = 0
        _is_on[animationNumber] = False
    
def AnimationIsOn(animationNumber: int) -> bool:
    return _is_on[animationNumber]

def GetFrame(animationNumber: int) -> int:
    return _frameCounts[animationNumber]